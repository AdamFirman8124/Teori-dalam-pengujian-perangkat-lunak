

# Generated at 2022-06-13 07:17:39.709952
# Unit test for function from_yaml
def test_from_yaml():
    '''Simple test to verify that from_yaml implements expected functionality.'''

    # Convert empty string to empty dictionary
    assert from_yaml('') == {}

    # Convert empty JSON to empty dictionary
    assert from_yaml('{}') == {}

    # Convert JSON to Python dictionary
    assert from_yaml('{ "one": "1", "two": 2.0, "three": [ 1, 2, 3] }') == dict(one='1', two=2.0, three=[1, 2, 3])

    # Convert empty YAML to empty list
    assert from_yaml('[]') == []

    # Convert YAML to Python list
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

    # Convert empty YAML to empty dictionary

# Generated at 2022-06-13 07:17:48.413864
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.utils.vars import combine_vars
    import json
    import os

    test_dir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(test_dir, 'test_utils')

    test_files = ['test_vars.yml', 'test_vars1.yml', 'test_vars2.yml']
    test_files = [os.path.join(test_dir, x) for x in test_files]

    vars = combine_vars(test_files)

    for x in vars:
        if isinstance(vars[x], dict):
            vars[x] = dict((k, str(v)) for k, v in vars[x].items())

# Generated at 2022-06-13 07:17:58.754620
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[ 1, 2, 3 ]') == [1, 2, 3]
    assert from_yaml('[ 1, 1.5, 3 ]') == [1, 1.5, 3]
    assert from_yaml('{ "foo": "bar" }') == {u'foo': u'bar'}
    assert from_yaml('{ "foo": [ "bar", 1, { "baz": "quux" } ] }') == {u'foo': [u'bar', 1, {u'baz': u'quux'}]}
    assert from_yaml('"foo"') == u'foo'
    assert from_yaml('"foo bar"') == u'foo bar'
    assert from_yaml('"foo\nbar"') == u'foo\nbar'

# Generated at 2022-06-13 07:18:01.808708
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'{"foo":"bar"}') == {"foo": "bar"}
    assert from_yaml(u'foo: bar') == {"foo": "bar"}

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:08.781797
# Unit test for function from_yaml
def test_from_yaml():
    # JSON dict
    data = "{\"test\": 123}"
    assert from_yaml(data) == {"test": 123}

    # JSON list
    data = "[\"test\", 123]"
    assert from_yaml(data) == ["test", 123]

    # YAML dict
    data = "test: 123"
    assert from_yaml(data) == {"test": 123}

    # YAML list
    data = "- test\n- 123"
    assert from_yaml(data) == ["test", 123]

# Generated at 2022-06-13 07:18:16.455055
# Unit test for function from_yaml
def test_from_yaml():
    '''Testing from_yaml'''
    
    bad_yamls = [
        # whitespace only
        '',
        '   ',
        # missing colon in key:value pair
        '{"host": "hostname"}',
        # missing quotes for string
        '{host: "hostname"}',
        # YAML does not support integer keys:
        '{1: "hostname"}',
        # YAML does not support integer keys:
        '{"1": "hostname"}',
        # json requires quotes for keys
        '{host: "hostname"}',
        # trailing comma at end of dict
        '{"host": "hostname",}',
        # trailing comma at end of list
        '[1,2,3,]',

    ]


# Generated at 2022-06-13 07:18:20.759553
# Unit test for function from_yaml
def test_from_yaml():
    yaml_str = """
        ---
        name: test_from_yaml
    """
    assert from_yaml(yaml_str) == {
        'name': 'test_from_yaml'
    }

# Generated at 2022-06-13 07:18:24.036117
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"a":1}') == {'a': 1}
    assert from_yaml('{a:1}') == {'a': 1}
    from_yaml('a: 1', json_only=True)

# Generated at 2022-06-13 07:18:33.668782
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Just a simple test for the YAML results of the datastructures since it's
    # handled by PyYAML

    yaml_str1 = '{"foo":"bar","bam":["one", "two", "three"]}'
    assert yaml_str1 == AnsibleDumper().dump(from_yaml(yaml_str1, json_only=True), default_flow_style=None)

    yaml_str2 = '''
    foo: bar
    bam:
      - one
      - two
      - three
    '''

# Generated at 2022-06-13 07:18:41.833426
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.vault import VaultLib
    vault = VaultLib()
    if vault.is_encrypted('$ANSIBLE_VAULT;1.1;AES256\n34623462384273846237846238462384\n'):
        data = vault.decrypt('$ANSIBLE_VAULT;1.1;AES256\n34623462384273846237846238462384\n')
        assert data == ''
    assert isinstance(from_yaml('- foo'), list)
    assert isinstance(from_yaml('foo: bar\n'), dict)
    assert isinstance(from_yaml('---\nfoo: bar\n'), dict)

# Generated at 2022-06-13 07:18:55.646067
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    import unittest
    import StringIO
    import tempfile
    import contextlib
    @contextlib.contextmanager
    def redirect_stdin(input):
        oldstdin = sys.stdin
        sys.stdin = StringIO.StringIO(input)
        yield
        sys.stdin = oldstdin
    try:
        from ansible.parsing.dataloader import DataLoader
        from ansible.parsing.vault import VaultLib
    except ImportError:
        sys.stderr.write("SKIP: unable to import ansible libs\n")
        sys.exit(0)
    # Test that from_yaml can parse a dict
    assert from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    #

# Generated at 2022-06-13 07:19:06.319103
# Unit test for function from_yaml
def test_from_yaml():
    test_data = '''
        - hosts: localhost
          gather_facts: no
          tasks:
          - name: test
            debug:
                msg: "foo {{ ansible_user_id }} {{ foo }}"
          vars:
              foo: hello
          vars_files:
            - files1
            - files2
          roles:
            - { role: apache }
            - { role: postgres, param1: value1, param2: value2 }
    '''

    # provide trivial default for test purposes
    vault_secrets = [('default@prompt', 'defaultpass')]


# Generated at 2022-06-13 07:19:20.119099
# Unit test for function from_yaml
def test_from_yaml():
    # test for correct processing of lists
    data = from_yaml('[1, 2, 3]')
    assert data == [1, 2, 3]

    # test for correct processing of dictionaries, as well as non-string percent-encoded unicode
    data = from_yaml(u'{ "%s": "%s", "%s": "%s" }' % (u'\u20ac', u'euro', u'\u00e4', u'aumlaut'))
    assert data == { u'\u20ac': u'euro', u'\u00e4': u'aumlaut'}

    # test for correct processing of unicode
    # NOTE: The python 3 json decoder doesn't support percent-encoded unicode, but data is not
    # percent-encoded, so this test should still pass.
    data

# Generated at 2022-06-13 07:19:29.505636
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils._text import to_text
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import is_encrypted
    import sys
    import io

    v = VaultLib([])
    key = 'testkey'
    password = 'testpass'
    data = '{"foo": "bar", "ansible_secret": "!vault |' + v.encrypt(password, key) + '"}'

    # Write the data to disk and use it in the test
    with io.open('/tmp/test_from_yaml', 'wb') as f:
        f.write(to_text(data).encode('utf-8'))

# Generated at 2022-06-13 07:19:31.938165
# Unit test for function from_yaml
def test_from_yaml():
    data = "foo: 1"
    file_name = '<string>'
    vault_secrets = None
    assert(from_yaml(data, file_name, True, vault_secrets) == {u'foo': 1})

# Generated at 2022-06-13 07:19:44.061057
# Unit test for function from_yaml
def test_from_yaml():
    data_json = b'''
    {
        "name": "John",
        "age": 18
    }
    '''
    data_yaml = b'''
    - name: John
      age: 18
    '''
    data_json_wrong = b'''
    {
        "name": "John",
        "age": 18
    '''
    data_yaml_wrong = b'''
    - name: John
      age: 18
    -
    '''

    # 1. Test case: simple json data - should return json
    assert from_yaml(data_json) == {"name": "John", "age": 18}

    # 2. Test case: yaml data - should return yaml

# Generated at 2022-06-13 07:19:45.402297
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("foo: 1") == {"foo": 1}

# Generated at 2022-06-13 07:19:53.968652
# Unit test for function from_yaml
def test_from_yaml():
    # Note that this test is invalidated by any changes to the Ansible JSON encoder/decoder.
    assert from_yaml('[1,2,3]') == [1, 2, 3]
    json_exc = from_yaml('[1,2', json_only=True)
    assert isinstance(json_exc, AnsibleParserError)
    yaml_exc = from_yaml('[1,2')
    assert isinstance(yaml_exc, AnsibleParserError)
    test_exc = from_yaml('''
    - foo: one
    - bar:
        baz: two
      baz: three
    ''', json_only=True)
    assert isinstance(test_exc, AnsibleParserError)

# Generated at 2022-06-13 07:19:58.324965
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('foo: bar') == {'foo': 'bar'}

# Generated at 2022-06-13 07:20:05.746769
# Unit test for function from_yaml
def test_from_yaml():
    files_to_test = [
        'test_from_yaml.json',
        'test_from_yaml.yaml'
    ]
    for f in files_to_test:
        data = open(f, 'rb').read()
        print(from_yaml(data))
        print('============')


if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:20:18.780820
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    aveu = AnsibleVaultEncryptedUnicode("test")
    aveu.vault_secret = 'test'
    aveu.vault_version = 'test'
    aveu.vault_id = 'test'

    assert from_yaml("test") == "test"
    assert from_yaml("test", json_only=True) == "test"
    assert from_yaml(aveu) == str(aveu)
    assert from_yaml([1, 2, 3]) == [1, 2, 3]
    assert from_yaml({"test": 1}) == {"test": 1}
    assert from_yaml({"test": []}) == {"test": []}
    assert from_

# Generated at 2022-06-13 07:20:27.496586
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib

    def _test_eq(data, expect):
        res = from_yaml(data)
        if expect != res:
            raise AssertionError('expect=%s, res=%s' % (expect, res))

    # test json
    _test_eq('{"hello": "world", "foo": true}', {'hello': 'world', 'foo': True})

    # test yaml
    _test_eq('hello: world', {'hello': 'world'})
    _test_eq('hello: "world"', {'hello': 'world'})
    _test_eq('hello: 123', {'hello': 123})
    _test_eq('hello: 12.3', {'hello': 12.3})

# Generated at 2022-06-13 07:20:31.497560
# Unit test for function from_yaml
def test_from_yaml():
    # Just to ensure that function works as expected in a few simple cases
    assert from_yaml(u'hello\n') == 'hello\n'
    assert from_yaml(u'\n-a\n-b\n') == ['a', 'b']

# Generated at 2022-06-13 07:20:40.167541
# Unit test for function from_yaml
def test_from_yaml():
    # ------------ Comments at the beginning ------------------------
    # Tests for yaml.safe_load
    yaml_data = '\n'.join((
        '#!/bin/bash\n',
        '# This is a comment',
        'hostname: server1.example.com',
    ))
    data = from_yaml(yaml_data)
    assert data == {'hostname': 'server1.example.com'}
    # Tests for json.loads
    json_data = '\n'.join((
        '#!/bin/bash\n',
        '# This is a comment',
        '{',
        '   # A comment in the middle',
        '   "hostname": "server1.example.com"',
        '}',
    ))
    data = from_yaml(json_data)
   

# Generated at 2022-06-13 07:20:49.255549
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Make sure from_yaml is able to handle string types, unicode types, and file objects
    '''

    import io
    import sys

    if sys.version_info[0] == 2 and sys.version_info[1] < 7:
        # can't test this on python 2.6, since it doesn't have io.StringIO
        return

    data_unicode = u"{ 'a': 'b' }"
    data_str = "{ 'a': 'b' }"


    # Get the file object
    file_object = io.StringIO(data_unicode)

    # YAML will like the unicode version, but not the byte version, so it should work with any version

# Generated at 2022-06-13 07:21:02.465626
# Unit test for function from_yaml
def test_from_yaml():
    json_str = '''
    {
    "key1" : "value1",
    "key2" : "value2",
    "dict_key" : {
        "key3" : "value3"
    },
    "list_key" : [
        "value4",
        "value5"
    ]
    }
    '''
    yaml_str = '''
    key1 : value1
    key2 : value2
    dict_key:
        key3 : value3
    list_key:
        - value4
        - value5
    '''
    json_obj = json.loads(json_str)
    yaml_obj = from_yaml(yaml_str)
    assert json_obj == yaml_obj

    # test with error

# Generated at 2022-06-13 07:21:16.332442
# Unit test for function from_yaml
def test_from_yaml():
    import unittest
    class TestFromYaml(unittest.TestCase):
        def test_basic(self):
            input = b'''
- key: value
  key2: value2
'''
            self.assertEqual(from_yaml(input), [{'key': 'value', 'key2': 'value2'}])

        def test_basic_doubled(self):
            input = b'''
- key: value
  key2: value2
- key: value
  key2: value2
'''
            self.assertEqual(from_yaml(input), [{'key': 'value', 'key2': 'value2'},
                                                {'key': 'value', 'key2': 'value2'}])

        def test_complicated(self):
            input = b

# Generated at 2022-06-13 07:21:26.257129
# Unit test for function from_yaml
def test_from_yaml():
    # Test with bad character inside quotes
    bad_text = u"{'bad_text': 'this is bad text }'}"
    try:
        from_yaml(bad_text)
        assert False, "Should have failed since the text is not valid Yaml."
    except AnsibleParserError:
        pass
    
    # Test with bad character outside quotes
    bad_text = "{'bad_text': this is bad text }"
    try:
        from_yaml(bad_text)
        assert False, "Should have failed since the text is not valid Yaml."
    except AnsibleParserError:
        pass

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:32.105377
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"msg": "Lorem ipsum dolor"}'
    results = from_yaml(data)
    assert results['msg'] == 'Lorem ipsum dolor'
    # print(json.dumps(results, indent=2))

    data = '{"msg": "Lorem ipsum dolor"}\n'
    results = from_yaml(data)
    assert results['msg'] == 'Lorem ipsum dolor'
    # print(json.dumps(results, indent=2))

    data = '''
    - name: hello world
      hosts: localhost
      gather_facts: True
      connection: local
      tasks:
        - name: say "hello world"
          debug:
            msg: "hello world"
    '''
    results = from_yaml(data)
   

# Generated at 2022-06-13 07:21:40.970083
# Unit test for function from_yaml
def test_from_yaml():
    # Test with valid json
    data = '{"foo": "bar"}'
    result = from_yaml(data)
    assert result == dict(foo='bar')

    # Test with valid yaml
    data = '''
    ---
    foo: bar
    '''

    result = from_yaml(data)
    assert result == dict(foo='bar')

    # Test with invalid json
    data = '{"foo": "bar'

    try:
        from_yaml(data)
        assert False, "Should have raised a YAMLException"
    except YAMLError as e:
        assert str(e).startswith("mapping values are not allowed here")

    # Test with invalid yaml
    data = '''
    ---
    foo: bar
    bar: foo
    '''


# Generated at 2022-06-13 07:21:54.877191
# Unit test for function from_yaml
def test_from_yaml():
    jsn = json.loads('{"foo": "bar"}')
    yml = yaml.load('foo: bar', Loader=yaml.FullLoader)
    assert from_yaml('{"foo": "bar"}') == jsn
    assert from_yaml('foo: bar') == yml
    assert from_yaml('{"foo": "bar"}', vault_secrets=None, json_only=True) == jsn
    # jsn2 is an invalid JSON string
    jsn2 = json.loads('{"foo": "bar",}')
    with pytest.raises(AnsibleParserError) as excinfo:
        from_yaml('{"foo": "bar",}', vault_secrets=None, json_only=True)

# Generated at 2022-06-13 07:22:06.561564
# Unit test for function from_yaml
def test_from_yaml():
    test_json_data = """{"test": 123}"""
 
    ret = from_yaml(test_json_data, json_only=True)
    assert(ret['test'] == 123)

    test_json_data = """{"test": 123"""
    try:
        ret = from_yaml(test_json_data, json_only=True)
    except Exception:
        pass
    else:
        assert(False)

    test_yaml_data = """
      test: 123
    """
    ret = from_yaml(test_yaml_data)
    assert(ret['test'] == 123)

    test_json_yaml_data = """
      test: 123
    """
    ret = from_yaml(test_json_yaml_data, json_only=True)

# Generated at 2022-06-13 07:22:10.529244
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}

# Generated at 2022-06-13 07:22:25.186434
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('[1, 2, 3]', json_only=True))
    print(from_yaml('[1, 2, 3]', json_only=False))
    print(from_yaml('{"a": 1, "b": 2}', json_only=True))
    print(from_yaml('{"a": 1, "b": 2}', json_only=False))
    print(json.loads('[1, 2, 3]'))
    print(json.loads('{"a": 1, "b": 2}'))
    try:
        print(json.loads('`[]'))
    except Exception as e:
        print(type(e), str(e))

# Generated at 2022-06-13 07:22:30.009251
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    # create a vault with a test password
    vault = VaultLib(b'test')
    vault_text = vault.encrypt(b'test')
    vault_text = vault.dump_one_line(vault_text)

    # try a json load
    data = '{"test": 4, "value": "{{%s}}"}' % vault_text.decode('utf-8')
    result = from_yaml(data)
    assert(hasattr(result, '__getitem__'))
    assert(result['test'] == 4)
    assert(isinstance(result['value'], AnsibleVaultEncryptedUnicode))

    # try a yaml

# Generated at 2022-06-13 07:22:43.972296
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('[]') == []
    assert from_yaml('{"a": 1}') == {'a': 1}
    assert from_yaml('a: 1') == {'a': 1}
    assert from_yaml('a: 1\n') == {'a': 1}
    assert from_yaml('a: 1\nb: 2\n') == {'a': 1, 'b': 2}
    assert from_yaml('a: 1\n\nb: 2\n') == {'a': 1, 'b': 2}
    assert from_yaml('a: 1\nb: 2\n\n') == {'a': 1, 'b': 2}
    assert from_yaml('- a\n- b') == ['a', 'b']

# Generated at 2022-06-13 07:22:54.869063
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestFromYAML(unittest.TestCase):
        def test_empty_doc(self):
            # NOTE: JSON parsing expects a list or a dict at the top level and will fail to parse
            # an empty string.
            self.assertEqual(from_yaml('', json_only=True), None)
            self.assertEqual(from_yaml('', json_only=False), None)

        def test_string_doc(self):
            self.assertEqual(from_yaml('a', json_only=True), None)
            self.assertEqual(from_yaml('a', json_only=False), u'a')

        def test_list_docs(self):
            self.assertEqual(from_yaml('[]', json_only=True), [])


# Generated at 2022-06-13 07:23:05.126192
# Unit test for function from_yaml
def test_from_yaml():

    import os
    import sys
    import unittest

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    ANSIBLE_TEST_DATA_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../unit/parsing/")

    # Function under test
    from ansible.parsing.yaml import from_yaml

    def read_file(filename):
        return open(os.path.join(ANSIBLE_TEST_DATA_ROOT, filename)).read()

    class TestAnsibleYAML(unittest.TestCase):

        def test_vault_decoding(self):
            vault_data = read_file("vault_data.yml")

# Generated at 2022-06-13 07:23:13.810960
# Unit test for function from_yaml
def test_from_yaml():
    case1 = '{"name": "test", "tags": ["test"]}'
    if from_yaml(case1, 'test-case', True, None, False) != json.loads(case1):
        raise AssertionError()

    case2 = '{invalid-json'
    try:
        from_yaml(case2, 'test-case', True, None, False)
        raise AssertionError('Invalid json should raise exception')
    except AnsibleParserError:
        pass

    case3 = ''
    try:
        from_yaml(case3, 'test-case', True, None, False)
        raise AssertionError('Invalid json should raise exception')
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:23:18.627191
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "a": "b" }') == { u'a': u'b' }
    assert from_yaml('', file_name='foo') == None
    assert from_yaml('{ "a": "b" }', json_only=True) == { u'a': u'b' }
    assert from_yaml('foo: { ansible_var: yay }', file_name='foo') == { u'foo': { u'ansible_var': u'yay' } }

# Generated at 2022-06-13 07:23:30.696986
# Unit test for function from_yaml
def test_from_yaml():
    testdata_error = '''
        - task: debug var={{ non_existing_var }}

        - test something

          extra line
        '''

    testdata_error_msg = YAML_SYNTAX_ERROR % u'while scanning for the next token\n' \
                                            u'found character \'<tab>\' that cannot start any token'
    try:
        from_yaml(testdata_error)
        assert False
    except AnsibleParserError as e:
        assert testdata_error_msg in to_native(e)

    testdata1 = """
        ---
        - hosts: all
          gather_facts: no
          tasks:
            - debug:
                msg: '{{ test_var }}'
              vars:
                test_var: test var
    """
    testdata2 = u

# Generated at 2022-06-13 07:23:45.262696
# Unit test for function from_yaml
def test_from_yaml():
    #from ansible.parsing.yaml.dumper import AnsibleDumper
    #from ansible.parsing.yaml.objects import AnsibleSequence
    assert from_yaml("1") == 1
    assert from_yaml("- 1") == [-1]
    assert from_yaml("- 1\n- 2") == [-1, -2]
    assert from_yaml("foo: !!str 'bar'") == {'foo': 'bar'}
    assert from_yaml("- !!str 'one'\n- !!str 'two'\n") == ['one', 'two']
    # FIXME: Enable this when list may be a string
    #assert from_yaml("!!python/object/apply:ansible.parsing.yaml.objects.AnsibleSequence\n"
    #

# Generated at 2022-06-13 07:23:56.362735
# Unit test for function from_yaml
def test_from_yaml():
   import unittest
   from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject


# Generated at 2022-06-13 07:24:06.510934
# Unit test for function from_yaml
def test_from_yaml():
    test_data = '''
    ---
    This is supposed to be an example of a YAML file
    '''
    # test if we can load the above string in YAML
    new_data = from_yaml(test_data)
    assert new_data[0] == 'This is supposed to be an example of a YAML file'

    # test if we can load some extra vars in YAML
    new_data = from_yaml('{"a": "hello", "b": 1}')
    assert new_data['a'] == 'hello'
    assert new_data['b'] == 1

    # test if we can load some extra vars in JSON
    new_data = from_yaml('{"a": "hello", "b": 1}', json_only=True)
    assert new_data['a']

# Generated at 2022-06-13 07:24:10.563100
# Unit test for function from_yaml
def test_from_yaml():
    # Empty string or None
    assert from_yaml('') is None
    assert from_yaml(None) is None
    assert from_yaml(None, json_only=True) is None

    # JSON
    assert from_yaml('{}') == {}
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('{"foo": "bar", "baz": 42}') == {"foo": "bar", "baz": 42}
    assert from_yaml('["foo", "bar"]') == ["foo", "bar"]
    assert from_yaml('{"foo": "bar", "baz": [1, 2, 3]}') == {"foo": "bar", "baz": [1, 2, 3]}

# Generated at 2022-06-13 07:24:20.900489
# Unit test for function from_yaml
def test_from_yaml():
    # Test for expected valid JSON and YAML data
    assert from_yaml("[]") == []
    assert from_yaml("{}") == {}
    assert from_yaml("{'foo': 5}") == {'foo': 5}
    assert from_yaml("{'foo': 'bar'}") == {'foo': 'bar'}
    assert from_yaml("{'foo': 5, 'bar': 'baz'}") == {'foo': 5, 'bar': 'baz'}
    assert from_yaml("""{'foo': 5, 'bar': {'baz': 'qux'}}""") == {'foo': 5, 'bar': {'baz': 'qux'}}

# Generated at 2022-06-13 07:24:28.614213
# Unit test for function from_yaml
def test_from_yaml():

    class obj(object):
        pass

    test_data = {}

    # Return the original value
    test_data['1'] = ['foo','bar','baz']
    test_data['2'] = 123
    test_data['3'] = None
    test_data['4'] = obj()

    for k in test_data:
        n = from_yaml(yaml.dump(test_data[k]))
        assert(test_data[k] == n)

# Generated at 2022-06-13 07:24:37.073519
# Unit test for function from_yaml
def test_from_yaml():
    # Test for unicode
    ansible_str = u"{'a': '1', 'b': 2, 'c': None, 'd': [1, 2, 3]}"
    assert from_yaml(ansible_str) == {"a": "1", "b": 2, "c": None, "d": [1, 2, 3]}

    # Test for string
    ansible_str = "{'a': '1', 'b': 2, 'c': None, 'd': [1, 2, 3]}"
    assert from_yaml(ansible_str) == {"a": "1", "b": 2, "c": None, "d": [1, 2, 3]}

    # Test for unicode

# Generated at 2022-06-13 07:24:47.800896
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Ensures that the from_yaml funciton works as expected :
      - with a valid YAML script
      - with a valid JSON script
      - with an invalid script
      - when json_only is set to True
    '''
    valid_yaml_data = """
    - hosts: localhost
      connection: local

    - hosts: localhost
      connection: local
      gather_facts: no

      tasks:
        - name: check uptime
          command: uptime
    """


# Generated at 2022-06-13 07:24:58.582224
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test function from_yaml
    :return:
    '''
    from ansible.parsing.yaml import from_yaml

    TEXT = u"""\
        {
          'copy': 'copy two files',
          'copy_two': { 'second': 'second_file' },
          'archive': {
            'copy': 'copy directory listing',
            'copy_two': { 'second': 'second_file' },
            'path': { 'path': '~/somewhere' },
            'copy_files': 'copy files recursively',
            'other': {'other_file': 'other_file'}
          },
          'when': 'when_test'
        }"""

    print(from_yaml(TEXT))

# Generated at 2022-06-13 07:25:06.300367
# Unit test for function from_yaml
def test_from_yaml():
    data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
    }
    yaml_data = '''
key1: value1
key2: value2
key3: value3
'''
    assert from_yaml(yaml_data) == data

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:12.242668
# Unit test for function from_yaml
def test_from_yaml():
    first = 'vars:\n  test: "{{ item }}"\n\nwith_items:\n  - 1\n  - 2\n  - 3'
    second = '{\n"vars": {\n  "test": "{{ item }}"\n},\n"with_items": [\n  "1",\n  "2",\n  "3"\n]\n}'

    assert from_yaml(first) == from_yaml(second)

# Generated at 2022-06-13 07:25:18.838187
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("[""   "", "    "", "    ""]") == [u'', u'', u'']
    assert from_yaml("""[{ "a" : "b", "c" : "d" }, { "e" : "f" }]""") == [{u'a': u'b', u'c': u'd'}, {u'e': u'f'}]
    assert from_yaml("""[{ "a" : "b", "c" : "d" }, { "e" : "f" }]""") == [{u'a': u'b', u'c': u'd'}, {u'e': u'f'}]

# Generated at 2022-06-13 07:25:22.127396
# Unit test for function from_yaml
def test_from_yaml():
    test_str = '{"a":1, "b":2}'
    data = from_yaml(test_str)
    assert data == {"a":1, "b":2}

# Generated at 2022-06-13 07:25:25.990067
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"test": "foo", "bar": "foobar"}'
    result = from_yaml(data)
    assert result == {'test': 'foo', 'bar': 'foobar'}


# Generated at 2022-06-13 07:25:31.636959
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('42') == 42
    assert from_yaml('') == None
    assert from_yaml('[]') == []
    assert from_yaml('{}') == {}
    assert from_yaml('{"foo": "bar"}') == {'foo': 'bar'}
    assert from_yaml('{foo: bar}') == {'foo': 'bar'}
    assert from_yaml('{foo: bar', False) == '{foo: bar'

# Generated at 2022-06-13 07:25:41.384061
# Unit test for function from_yaml
def test_from_yaml():
    import json
    import yaml
    from ansible.parsing.ajson import AnsibleJSONEncoder

    # Test data from ansible.module_utils.common.yaml_utils.dump
    test_data = [
        ({"a": "b", "d": {"e": "f"}}, "{\"a\": \"b\", \"d\": {\"e\": \"f\"}}"),
        ([1, 2, 3], "[1, 2, 3]"),
        ("", "\"\""),
        (u"", "\"\""),
        (0, "0"),
        (1, "1"),
        ("abcd", "\"abcd\""),
        (u"abcd", "\"abcd\""),
        ("a", "\"a\""),
        (u"a", "\"a\"")
    ]


# Generated at 2022-06-13 07:25:55.514935
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.text_parser_common import fix_newline

    data_good_json = '{"foo":"bar"}'
    data_good_yaml = 'foo:\n  bar'

    good_json = from_yaml(data_good_json, json_only=True)
    assert good_json == {u'foo': u'bar'}

    good_yaml = from_yaml(data_good_yaml)
    assert good_yaml == {u'foo': {u'bar': None}}

    # TODO: Need to find a better way to test this.
    try:
        bad_data = 'foo:\n  bar\n  [\n    foobar'
        from_yaml(bad_data)
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:26:07.984330
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test function for function from_yaml
    '''
    import os
    import pytest

    # Test: yaml parsing
    data = '''\
---
test:
- 1
- "test"
- - 1
  - 2
  - - 1
    - 2
'''
    test_result = from_yaml(data)

    assert test_result['test'][0] == 1
    assert test_result['test'][1] == 'test'
    assert test_result['test'][2][0] == 1
    assert test_result['test'][2][1] == 2
    assert test_result['test'][2][2][0] == 1
    assert test_result['test'][2][2][1] == 2

    # Test: yaml parsing with json

# Generated at 2022-06-13 07:26:11.953571
# Unit test for function from_yaml
def test_from_yaml():
    data = {}
    file_name = '<string>'
    show_content = True
    vault_secrets = None
    json_only = False
    new_data = from_yaml(data,file_name,show_content,vault_secrets,json_only)
    assert new_data is None

# Generated at 2022-06-13 07:26:28.628836
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{bad json') == None
    assert from_yaml('{"a": "b"}') == {"a": "b"}
    assert from_yaml('a: b') == {"a": "b"}
    assert from_yaml('---\n{"a": "b"}') == {"a": "b"}
    assert 'a' in from_yaml('a: b\nc: d')
    assert 'c' in from_yaml('a: b\nc: d')
    assert from_yaml('a: b\nc: d\n') == {"a": "b", "c": "d"}

# Generated at 2022-06-13 07:26:34.857162
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test function from_yaml
    '''
    try:
        from_yaml('{"key":"value"}', '<string>', True, None)
    except AnsibleParserError as e:
        print(e)
        assert False
    assert True

    try:
        from_yaml('''
        [
            {
                "key": "value"
            }
        ]''', '<string>', True, None)
    except AnsibleParserError as e:
        print(e)
        assert True
    assert False


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:26:39.609766
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence, AnsibleUnicode, AnsibleVaultEncryptedUnicode
    f = open('unittest_data/test_yaml_serializer.yaml')

# Generated at 2022-06-13 07:26:43.788104
# Unit test for function from_yaml
def test_from_yaml():
    vault_secrets = None
    file_name = '<string>'
    show_content = True
    json_only = False

    # Test case 1: Call the function without any data, expect an exception
    # Call the function
    try:
        from_yaml(None, file_name, show_content, vault_secrets, json_only)
    except AnsibleParserError as error:
        # Verify the exception
        assert(error.message == 'We were unable to read either as JSON nor YAML, these are the errors we got from each:\n'
                                'JSON: No JSON object could be decoded\n\n'
                                'ERROR! Syntax Error while loading YAML.')
    else:
        assert False, 'Did not find expected exception'

    # Test case 2: Call the function with an invalid json,

# Generated at 2022-06-13 07:26:57.744726
# Unit test for function from_yaml
def test_from_yaml():
    # Test replacement of the `from` keyword with `from_`
    data = """
- hosts: localhost
  tasks:
   - name: test from
     fail:
       msg: this is a {{ from }} test
    """
    parsed_data = from_yaml(data)
    assert parsed_data[0]['tasks'][0]['fail']['msg'] == u"this is a {{ from_ }} test"

    data = """
- hosts: localhost
  tasks:
   - name: test from
     fail:
       msg: this is a {{ "from" }} test
    """
    parsed_data = from_yaml(data)
    assert parsed_data[0]['tasks'][0]['fail']['msg'] == u"this is a {{ from_ }} test"


# Generated at 2022-06-13 07:27:05.126933
# Unit test for function from_yaml
def test_from_yaml():
    data = '{ "a": "b", "c": "d" }'
    file_name = "myfile"
    show_content = True
    vault_secrets = "secret"
    json_only = False
    new_data = from_yaml(data, file_name=file_name, show_content=show_content, vault_secrets=vault_secrets, json_only=json_only)
    assert new_data != None

# Generated at 2022-06-13 07:27:11.836227
# Unit test for function from_yaml
def test_from_yaml():
    yaml_str = '''
        a: 1
        b: "2"
        c: [1, 2, 3]
        d:
          - 1
          - 2
          - 3
    '''
    assert from_yaml(yaml_str) == dict(
        a=1,
        b="2",
        c=[1, 2, 3],
        d=[1, 2, 3]
    )

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:27:19.286407
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import tempfile
    import shutil

    dir_name = tempfile.mkdtemp()
    file_name = os.path.join(dir_name, 'test.yml')

    # Write out a valid yaml file with a list in it
    with open(file_name, 'w') as f:
        f.write("""
        - foo
        - bar
        """)

    # Check to make sure we can read it back with from_yaml
    data = from_yaml(open(file_name, 'r').read(), file_name)
    assert isinstance(data, list)

    # Now write out a bad yaml file
    with open(file_name, 'w') as f:
        f.write("""
        foo: bar
        - lol
        """)

    # Check to

# Generated at 2022-06-13 07:27:30.617694
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"a": 1, "b": [2, 3, 4]}'
    json_only = False
    new_data = from_yaml(data, file_name='', show_content=True, vault_secrets=None, json_only=json_only)
    assert new_data == {u'a': 1, u'b': [2, 3, 4]}

    data = '{"a": 1, "b": [2, 3, 4]}'
    json_only = True
    new_data = from_yaml(data, file_name='', show_content=True, vault_secrets=None, json_only=json_only)
    assert new_data == {u'a': 1, u'b': [2, 3, 4]}
