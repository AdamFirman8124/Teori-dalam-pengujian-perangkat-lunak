

# Generated at 2022-06-13 07:17:36.422089
# Unit test for function from_yaml
def test_from_yaml():
    json_string = '{"a": ["b", {"c": "d"}], "e": "f"}'
    yaml_string = '''
a:
- b
- c: d
e: f
'''

    assert from_yaml(json_string) == from_yaml(yaml_string)
    assert from_yaml(json_string) == {"a": ["b", {"c": "d"}], "e": "f"}

# Generated at 2022-06-13 07:17:36.906914
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:17:46.547247
# Unit test for function from_yaml

# Generated at 2022-06-13 07:17:57.023629
# Unit test for function from_yaml
def test_from_yaml():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Arbitrary test data.
    correct_json = '{ "foo": "bar" }'
    correct_yaml = '---\nfie: baz'
    incorrect_json = '{ "foo": "bar"'  # Missing "}".
    incorrect_yaml = '---\nfie: baz'  # Missing "!include".

    # The "file_name" arg is used by AnsibleParserError to display the
    # problematic file path/line/column.
    err_file_name = '/path/to/a/file'

    #
    # Test the case where ansible.errors.AnsibleParserError is raised from
    # failed JSON parsing.
    #

    # Data that is only valid JSON.

# Generated at 2022-06-13 07:18:03.380978
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml("x: y\n")
    except AnsibleParserError as e:
        assert(e.message == "We were unable to read either as JSON nor YAML, these are the errors we got from each:\nJSON: Expecting value: line 1 column 1 (char 0)\n\nSyntax Error while loading YAML.\n  did not find expected key\n\nThe error appears to be in '/dev/stdin': line 1, column 1, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\nx: y\n")

# Generated at 2022-06-13 07:18:13.530149
# Unit test for function from_yaml
def test_from_yaml():
    """
    This is the function which test the function from_yaml.
    """
    # Invalid data type
    passing_data = {}
    try:
        from_yaml(passing_data)
    except Exception as exception:
        assert True
    else:
        assert False

    # Invalid JSON
    passing_data = "{a: 'b'}"
    try:
        from_yaml(passing_data)
    except Exception as exception:
        assert True
    else:
        assert False

    # Invalid YAML
    passing_data = "a: 'b'"
    try:
        from_yaml(passing_data)
    except Exception as exception:
        assert True
    else:
        assert False

    # Passing data type
    passing_data = "{'a': 'b'}"

# Generated at 2022-06-13 07:18:24.036103
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3, b
    from ansible.module_utils.common._collections_compat import string_types
    import os

    t_yaml_file = os.path.join(os.path.dirname(__file__), "test_data", "test.yaml")
    with open(t_yaml_file, 'r') as f:
        data = f.read()
        if PY3:
            data_in = data
        else:
            data_in = b(data)

    # test function from_yaml
    result = from_yaml(data,
                       file_name='<test_data>',
                       show_content=True,
                       vault_secrets=None,
                       json_only=False)

    assert isinstance(result, dict)

# Generated at 2022-06-13 07:18:29.401814
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils import basic

    basic._ANSIBLE_ARGS = None

    test_string = "{'a': {'b': 'c'}}"
    assert from_yaml(test_string, file_name='/tmp/test_from_yaml', show_content=True, vault_secrets=None) == {'a': {'b': 'c'}}

    test_string = """---
'a': {'b': 'c'}
"""
    assert from_yaml(test_string, file_name='/tmp/test_from_yaml', show_content=True, vault_secrets=None) == {'a': {'b': 'c'}}

# Generated at 2022-06-13 07:18:37.162560
# Unit test for function from_yaml
def test_from_yaml():
    # This should work correctly as json:
    assert {'foo': 'bar', 'bam': [1, 2, 3]} == from_yaml('{\n    "foo": "bar",\n    "bam": [1, 2, 3]\n}\n')

    # This is Yaml and should succeed:
    assert {'foo': 'bar', 'bam': [1, 2, 3]} == from_yaml('foo: bar\nbam:\n  - 1\n  - 2\n  - 3\n')

    # This is neither json nor yaml:

# Generated at 2022-06-13 07:18:41.123810
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestYaml(unittest.TestCase):
        def test_from_yaml_valid(self):
            data = """---
a: string
b: 1
c:
  - foo
  - bar"""
            result = from_yaml(data)
            self.assertEqual(result, {'a': 'string', 'c': ['foo', 'bar'], 'b': 1})

        def test_from_yaml_invalid(self):
            data = """---
a: string
b: 1
c:
- foo
- bar"""
            with self.assertRaises(AnsibleParserError):
                from_yaml(data)

    unittest.main()

# Generated at 2022-06-13 07:18:50.949783
# Unit test for function from_yaml
def test_from_yaml():
    test1 = '''
    - test:
        - dev_port: 5
        - prod_port: 5
    '''
    test2 = '''
    test:
        dev_port: 5
        prod_port: 5
    '''
    expected_result = [{'test':[{'dev_port': 5},{'prod_port': 5}]}]
    result1 = from_yaml(test1)
    result2 = from_yaml(test2)
    assert result1 == result2 == expected_result

# Generated at 2022-06-13 07:18:59.493648
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    assert from_yaml('{"foo": "bar"}') == {'foo': 'bar'}
    assert from_yaml('foo: bar\n') == {'foo': 'bar'}

# Generated at 2022-06-13 07:19:07.912897
# Unit test for function from_yaml
def test_from_yaml():
	try:
		data = "http://hongtaoli.com"
		new_data = json.loads(data, cls=AnsibleJSONDecoder)
	except Exception as err:
		raise
	else:
		print("json load this data")
		print(new_data)
	finally:
		print("json load over.")

	try:
		stream = open("d:/data.yaml","rb")
		new_data2 = _safe_load(stream, file_name=None, vault_secrets=None)
	except Exception as err:
		raise
	else:
		print("yaml load this data")
		print(new_data2)
	finally:
		print("yaml load over.")


# Generated at 2022-06-13 07:19:21.490462
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.objects
    import os
    import sys

    my_dict = {u'a': u'hello', u'b': {u'c': 1, u'd': [2, 3, 4]}}
    assert my_dict == from_yaml(to_text(json.dumps(my_dict), errors='surrogate_or_strict'))

    # Ensure that a non-string sequence/mapping/scalar won't error out
    assert from_yaml({u'a': u'hello', u'b': {u'c': 1, u'd': [2, 3, 4]}}) == my_dict

# Generated at 2022-06-13 07:19:30.426381
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test case for from_yaml function
    '''
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib

    # Common data for files
    data_base = """
%YAML 1.1
---
a: 1
b:
  c: 3
  d: 4
"""
    data = to_bytes(data_base, errors='surrogate_or_strict')

    # Test file name
    file_name = 'unit_test.yml'

    # Test vault_secrets
    vault_secrets = VaultLib([])

    expected_data = {'a': 1, 'b': {'c': 3, 'd': 4}}

    # Test with valid data and no vault secrets
    result_data = from_yaml

# Generated at 2022-06-13 07:19:41.272917
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(':') == None
    assert from_yaml(': 1') == 1
    assert from_yaml('a: 1') == {'a': 1}
    assert from_yaml('3.14') == 3.14
    assert from_yaml('[1,2,3]') == [1,2,3]
    assert from_yaml('[1,2,3.14]') == [1,2,3.14]
    assert from_yaml('{"a":1}') == {"a":1}
    assert from_yaml('{"a":1, "b":2.3, "c":"yep"}') == {"a":1, "b":2.3, "c":"yep"}

# Generated at 2022-06-13 07:19:51.367587
# Unit test for function from_yaml
def test_from_yaml():
    print("Test Ansible Yaml module")
    print("Test data:")
    print("---")
    print("- hosts: localhost")
    print("  tasks:")
    print("  - name: Ansible Yaml module test")
    print("    debug:")
    print("      msg: Hello from Ansible")
    print("    yaml_test: True")
    print("...")
    print("")
    print("Output:")
    test_file = "- hosts: localhost\n  tasks:\n  - name: Ansible Yaml module test\n    debug:\n      msg: Hello from Ansible\n    yaml_test: True"
    test_data = from_yaml(test_file, "test", False)
    print(test_data)



# Generated at 2022-06-13 07:20:01.701247
# Unit test for function from_yaml
def test_from_yaml():
    import yaml
    yml = """---
foo: bar
list:
- 1
- 2
- 3"""
    expected = {'foo': 'bar', 'list': [1, 2, 3]}
    result = from_yaml(yml, json_only=True)
    assert result == expected

    # refs issue #25107
    from_json_only = from_yaml(yml, json_only=True)
    from_yaml_default = from_yaml(yml)
    from_yaml_explicit = from_yaml(yml, json_only=False)
    assert from_json_only == from_yaml_default
    assert from_json_only == from_yaml_explicit
    assert from_yaml_default == from_yaml_explicit

    # refs issue

# Generated at 2022-06-13 07:20:06.067922
# Unit test for function from_yaml
def test_from_yaml():
    import os

    data = open(os.path.join(os.path.dirname(__file__), '../../lib/ansible/playbook/data_loader.py')).read()
    print(from_yaml(data))
    print(from_yaml('{"key": "value"}', file_name='/path/to/file'))

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:20:17.247544
# Unit test for function from_yaml
def test_from_yaml():
    yaml_str = """\
    {% raw %}- name: Create a list of users
  hosts: localhost
  gather_facts: no

  tasks:
  - name: Create users
    user:
      name: "{{ item }}"
    loop:
    - testuser1
    - testuser2

  - name: Create groups
    group:
      name: "{{ item }}"
    loop:
    - testgroup1
    - testgroup2{% endraw %}
    """
    python_data = from_yaml(yaml_str)
    assert isinstance(python_data, list)
    assert python_data[0]['name'] == 'Create a list of users'
    assert python_data[0]['hosts'] == 'localhost'

# Generated at 2022-06-13 07:20:27.718704
# Unit test for function from_yaml
def test_from_yaml():
    ('Unit test for function from_yaml')
    try:
        from_yaml('[1,2,3]')
    except Exception as e:
        assert False, "function from_yaml with argument '[1,2,3]' throw exception with message {}".format(e.message)

    try:
        from_yaml('[1,2,3]', json_only=True)
    except Exception as e:
        assert False, "function from_yaml with argument '[1,2,3]' throw exception with message {}".format(e.message)

    try:
        from_yaml('{"key": "value"}')
    except Exception as e:
        assert False, "function from_yaml with argument '{\"key\": \"value\"}' throw exception with message {}".format(e.message)


# Generated at 2022-06-13 07:20:38.143812
# Unit test for function from_yaml
def test_from_yaml():
    ''' This function should be used with nose.tools.assert_raises '''
    def _test_from_yaml_el(data, show_content=True, vault_secrets=None, json_only=False):
        from_yaml(data, show_content=show_content, vault_secrets=vault_secrets, json_only=json_only)

    # Check if from_yaml return a python datastructure on JSON data
    data = '{"foo": "bar"}'
    _test_from_yaml_el(data)

    # Check if from_yaml return a python datastructure on YAML data
    data = 'foo: bar'
    _test_from_yaml_el(data)

    # Check if from_yaml raise an exception on malformed JSON data

# Generated at 2022-06-13 07:20:45.330457
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("[foo]") == ["foo"]
    assert from_yaml("foo: [1, 2, 3]") == {"foo": [1,2,3]}
    assert from_yaml("foo: bar") == {"foo": "bar"}
    assert from_yaml("foo: !!bool True") == {"foo": True}
    assert from_yaml("foo: !!str bar") == {"foo": "bar"}
    assert from_yaml("[foo, !!str bar]") == ["foo", "bar"]



# Generated at 2022-06-13 07:20:51.493721
# Unit test for function from_yaml
def test_from_yaml():
    # Simple integer test
    assert from_yaml('3') == 3

    # Simple boolean test
    assert from_yaml('true') is True

    # Simple list test
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]

    # Simple dict test
    assert from_yaml('{"a": 1, "b": 2}') == {"a": 1, "b": 2}



# Generated at 2022-06-13 07:20:53.214697
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{'key': 'value'}") == {'key': 'value'}

# Generated at 2022-06-13 07:20:57.346444
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "hello": "world" }') == { "hello": "world" }
    assert from_yaml('hello: world') == { "hello": "world" }
    try:
        from_yaml('''hello: {
                      world: 1
                   ''')
        assert False, "Should throw an error"
    except AnsibleParserError as e:
        pass
    assert from_yaml('''---
hello: world
''') == { "hello": "world" }

# Generated at 2022-06-13 07:21:02.835016
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(u'{ "somestring": "somevalue" }') == {u'somestring': u'somevalue'}
    assert from_yaml(u'somestring: somevalue') == {u'somestring': u'somevalue'}

# Generated at 2022-06-13 07:21:16.742734
# Unit test for function from_yaml
def test_from_yaml():

    from ansible.parsing.yaml.dumper import AnsibleDumper

    def _test_from_yaml_equivalence(data):
        '''
        Tests that the data argument does not change when encoded
        and decoded using from_yaml.
        '''

        data2 = from_yaml(to_yaml(data))
        assert data == data2

    _test_from_yaml_equivalence(None)
    _test_from_yaml_equivalence(1)
    _test_from_yaml_equivalence(1.0)
    _test_from_yaml_equivalence({})
    _test_from_yaml_equivalence([])
    _test_from_yaml_equivalence([{}, {}])
    _test_from_yaml_

# Generated at 2022-06-13 07:21:24.560694
# Unit test for function from_yaml
def test_from_yaml():
    v = frozenset([1,2,3])
    def check(data, expected):
        d = from_yaml(data)
        assert d == expected, '%r != %r' % (d, expected)
        if v:
            d = from_yaml(data, vault_secrets=v)
            assert d == expected, '%r != %r' % (d, expected)
    # BOOLEAN
    check('true', True)
    check('True', True)
    check('false', False)
    check('False', False)
    # STRING
    check('foo', u'foo')
    check('"foo"', u'foo')
    check("'foo'", u'foo')
    # SEQUENCE
    check('[1,2,3]', [1,2,3])

# Generated at 2022-06-13 07:21:28.351320
# Unit test for function from_yaml
def test_from_yaml():
    result = from_yaml('{ "a": 1 }')
    assert result == {'a': 1}
    result = from_yaml('{"a": 1}', json_only=True)
    assert result == {'a': 1}
    # The YAML block scalar style is explicitly not supported in json
    result = from_yaml('|-\n  a\n')
    assert result == 'a\n'

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:21:40.001638
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.loader
    import pprint

# Generated at 2022-06-13 07:21:45.670841
# Unit test for function from_yaml
def test_from_yaml():
    assert json.loads(from_yaml('{"a": [1, 2, 3], "b": false, "c": true, "d": null}')) == \
           json.loads('{"a": [1, 2, 3], "b": false, "c": true, "d": null}')


test_from_yaml()

# Generated at 2022-06-13 07:21:49.496149
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Tests to make sure we can parse yaml correctly
    '''

    assert from_yaml('[{ "foo": {"bar": [1, 2, 3] } }]') == [{'foo': {'bar': [1, 2, 3]}}]

# Generated at 2022-06-13 07:21:57.399300
# Unit test for function from_yaml
def test_from_yaml():
    import unittest

    class TestFromYaml(unittest.TestCase):
        def test_none(self):
            self.assertEqual(None, from_yaml(None))

        def test_dict(self):
            _dict = {'key': 'value'}
            self.assertEqual(_dict, from_yaml(u'key: value'))
            self.assertEqual(_dict, from_yaml(u'{key: value}'))
            self.assertEqual(_dict, from_yaml(u'{ "key": "value" }'))

        def test_list(self):
            _list = [1, 2, 3]
            self.assertEqual(_list, from_yaml(u'[1, 2, 3]'))

# Generated at 2022-06-13 07:22:05.509246
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
        foo:
          - value1
          - value2
          - value3
        bar:
          key1: value4
          key2: value5
          key3: value6
        '''

    expected = {
        u'foo': [u'value1', u'value2', u'value3'],
        u'bar': {u'key1': u'value4', u'key2': u'value5', u'key3': u'value6'}
    }

    assert from_yaml(data) == expected

# Generated at 2022-06-13 07:22:11.451300
# Unit test for function from_yaml
def test_from_yaml():

    # Test with valid test data
    test_data = '{"foo": "{{ bar }}"}'
    assert from_yaml(test_data) == {'foo': '{{ bar }}'}

    # Test with invalid test data
    with pytest.raises(AnsibleParserError):
        # Note that this test assumes that the string '{' is not valid YAML.
        # If this assumption changes in the future, this test will fail,
        # but the function will still work.
        test_data = '{'
        from_yaml(test_data)

# Generated at 2022-06-13 07:22:25.648153
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test YAML and JSON conversion
    '''
    import os
    import unittest

    TEST_DIR = os.path.dirname(os.path.abspath(__file__))
    TEST_FILE = os.path.join(TEST_DIR, '../../lib/ansible/parsing/yaml/__init__.py')

    class TestYamlUtils(unittest.TestCase):

        def test_from_yaml(self):

            # Test conversion of YAML, JSON and invalid data
            yaml_str = """---
            a:
                1: 2
                2: 3
                3:
                    4: 5
            """
            res = from_yaml(yaml_str)
            self.assertIsInstance(res, dict)

# Generated at 2022-06-13 07:22:39.986460
# Unit test for function from_yaml

# Generated at 2022-06-13 07:22:46.840453
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    - hosts:
        - server1
        - server2
    tasks:
    - name: install nginx
      apt: name=nginx state=latest
    - name: ensure nginx config file
      template: src=templates/nginx.j2 dest=/etc/nginx/nginx.conf
    '''
    result = from_yaml(data)
    assert result['tasks'][1]['template']['dest'] == '/etc/nginx/nginx.conf'

# Generated at 2022-06-13 07:22:57.303465
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    test_vault_password = '$ANSIBLE_VAULT;1.1;AES256\n3866363534306162326639613932653064616338613333323930666338626235616231393961633866\n3438306533303532393639656433343836393363626162343164656537643834333130313466393537\n34323930383765373336363037356233396533\n'

    # test vault secrets
    secrets = {'vault_password' : test_vault_password}
    in_data = {'testing': '{{testing}}'}

# Generated at 2022-06-13 07:23:07.925979
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import unittest

    os.environ['ANSIBLE_LIBRARY'] = '..'
    sys.modules['ansible'] = None

    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils._text import to_bytes

    class TestYamlParsing(unittest.TestCase):

        def roundtrip_test(self, data, expected=None):

            # When we get a number back it is a string in python 2 and a
            # number in python 3.  This ensures that numbers are converted
            # to the appropriate type.
            dumper = AnsibleD

# Generated at 2022-06-13 07:23:10.629297
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    {
        "some_var": "test value"
    }

    '''

    new_data = from_yaml(data)
    assert new_data == {'some_var': 'test value'}



# Generated at 2022-06-13 07:23:18.765219
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.common.frozendict import frozendict
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-13 07:23:27.720673
# Unit test for function from_yaml
def test_from_yaml():

    # Test that it returns a list
    yaml_str = "---\n- hosts: all\n  tasks: []"
    result = from_yaml(yaml_str)
    assert isinstance(result, list), 'from_yaml did not return a list'

    # Test that it returns a dictionary
    yaml_str = "---\nhosts: all\ntasks: []"
    result = from_yaml(yaml_str)
    assert isinstance(result, dict), 'from_yaml did not return a dictionary'

    # Test that it passes json string correctly to json.loads
    json_str = '{"k1":"v1", "k2":"v2"}'
    result = from_yaml(json_str)

# Generated at 2022-06-13 07:23:35.977867
# Unit test for function from_yaml
def test_from_yaml():
    # Case 0: JSON
    data = '{ "foo": { "bar": { "baz": "blah" }}}'
    result = from_yaml(data)
    assert result == {'foo': {'bar': {'baz': 'blah'}}}
    assert type(result) == dict

    # Case 1: YAML
    data = '''
    foo:
      bar:
        baz: blah
    '''
    result = from_yaml(data)
    assert result == {'foo': {'bar': {'baz': 'blah'}}}
    assert type(result) == dict

# Generated at 2022-06-13 07:23:49.267398
# Unit test for function from_yaml
def test_from_yaml():
    # Test failure when content is neither JSON nor YAML
    yaml_content = "---\nname: test"
    json_content = "{\"---\": {\"name\": \"test\"}}"

    try:
        from_yaml(yaml_content, json_only=True)
    except AnsibleParserError as exc:
        assert "We were unable to read either as JSON nor YAML, these are the errors we got from each:\n" in to_native(exc)
        assert "JSON: Expecting property name enclosed in double quotes:" in to_native(exc)
        assert "YAML: mapping values are not allowed here" in to_native(exc)

    # Test that function can parse JSON content
    json_content = "{\"name\": \"test\"}"

# Generated at 2022-06-13 07:24:00.235289
# Unit test for function from_yaml
def test_from_yaml():
    data = {"foo": "bar"}
    new_data = from_yaml(json.dumps(data), json_only=True)
    assert data == new_data
    new_data = from_yaml(json.dumps(data), json_only=False)
    assert data == new_data
    new_data = from_yaml(data, json_only=False)
    assert data == new_data
    new_data = from_yaml(json.dumps(data))
    assert data == new_data
    new_data = from_yaml(data)
    assert data == new_data
    data = '{"foo": "bar"}'
    new_data = from_yaml('{"foo": "bar"}')
    assert data == new_data
    data = '"foo": "bar"}'
   

# Generated at 2022-06-13 07:24:09.228633
# Unit test for function from_yaml
def test_from_yaml():
    import tempfile

    # test that an error is raised with invalid yaml
    try:
        data = u"this is some invalid yaml\n  with a second line"
        ansible.parsing.yaml.objects.from_yaml(data, '<test_data>')
        assert False, "from_yaml should have raised an exception with invalid yaml"
    except Exception as e:
        print("Invalid yaml exception: %s" % to_native(e))

    # test that an error is raised with invalid json

# Generated at 2022-06-13 07:24:20.298989
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import shutil
    import ansible.constants as C

    FIXTURES_DIR = os.path.join(C.DEFAULT_MODULE_PATH, 'test/fixtures/parse')
    FIXTURES_OUTPUT = os.path.join(C.DEFAULT_MODULE_PATH, 'test/output/ansible_module_parse')

    for fname in os.listdir(FIXTURES_DIR):
        if os.path.isfile(os.path.join(FIXTURES_DIR, fname)) and fname.endswith('.yml'):

            fname_output = os.path.join(FIXTURES_OUTPUT, fname.replace('.yml', '.py'))

# Generated at 2022-06-13 07:24:27.280649
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"data": "this is a json string"}') == {'data': 'this is a json string'}
    assert from_yaml('this is a json string') is None
    assert from_yaml('---\n- one') == ["one"]
    assert from_yaml('---\n- one\n- two') == ["one", "two"]

# Generated at 2022-06-13 07:24:38.712622
# Unit test for function from_yaml
def test_from_yaml():
    data = '{ "foo": 1, "bar": 2 }'
    assert from_yaml(data) == { u'foo': 1, u'bar': 2 }
    assert from_yaml(data, json_only=True) == { u'foo': 1, u'bar': 2 }

    data = 'foo: 1\nbar: 2'
    assert from_yaml(data) == { u'foo': 1, u'bar': 2 }

    data = '"foo": 1'
    try:
        from_yaml(data)
        assert False
    except AnsibleParserError as e:
        pass


# Generated at 2022-06-13 07:24:49.240606
# Unit test for function from_yaml
def test_from_yaml():
    import collections
    import json
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence

    ansible_parse_exc = None
    ansible_yaml_obj  = None
    ansible_exc_info  = None
    ansible_exc_msg   = None
    json_parse_exc    = None
    json_exc_info     = None
    json_exc_msg      = None
    json_fail_msg     = None
    ansible_fail_msg  = None

    # Testcase: Valid JSON
    data = '''{ "key": "value" }'''

# Generated at 2022-06-13 07:24:59.608828
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test from_yaml function.
    '''

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import ensure_str


# Generated at 2022-06-13 07:25:08.583631
# Unit test for function from_yaml
def test_from_yaml():
    # 1. Invalid YAML
    json_only = False
    data = "foo: 1\nbar:\n- baz\n-\nbaz:\n"
    file_name = 'test.yml'
    try:
        from_yaml(data, file_name, json_only)
    except AnsibleParserError as e:
        #print("Caught exception: {}".format(e))
        assert len(e.errors) == 1
        line, column, error = e.errors[0][1]
        assert line == 4
        assert column == 1
        assert error == 'mapping values are not allowed here'

    # 2. Valid YAML
    data = "foo: 1\nbar:\n  - baz\n  -\n  baz:\n"

# Generated at 2022-06-13 07:25:12.746682
# Unit test for function from_yaml
def test_from_yaml():

    # Invalid json string
    assert from_yaml('{') is None

    # Valid json string
    assert from_yaml('{"a":1}') == {"a": 1}

    # Valid yaml string
    assert from_yaml('a: 1') == {"a": 1}

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:18.712429
# Unit test for function from_yaml
def test_from_yaml():
    mydata_dict = { 'var1': 'value1', 'var2': 'value2' }
    mydata_json = json.dumps(mydata_dict)
    mydata_yaml = "{ var1: value1, var2: value2 }"
    mydata_json_new = from_yaml(mydata_json)
    assert mydata_json_new == mydata_dict
    mydata_yaml_new = from_yaml(mydata_yaml)
    assert mydata_yaml_new == mydata_dict

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:25.786512
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.module_utils._text import to_bytes, to_text


# Generated at 2022-06-13 07:25:33.722399
# Unit test for function from_yaml
def test_from_yaml():
    from collections import namedtuple
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 07:25:43.404198
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import PY3, StringIO

    def assert_from_yaml(good_yaml, file_name='<string>'):
        data = from_yaml(good_yaml, file_name=file_name)
        assert data == {'y': 1, 'x': [1, 2, 3]}

    assert_from_yaml('{ "y" : 1, "x" : [ 1, 2, 3 ] }')
    assert_from_yaml('y: 1\nx: [1, 2, 3]\n')

    # Make sure that when we insert a newline at the end of our good YAML
    # we don't get a failure

# Generated at 2022-06-13 07:25:46.658753
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml('{"test": false}', file_name='test_from_yaml.json')
    except Exception as e:
        print('%s' % e)
        raise Exception('test_from_yaml failed')
    try:
        from_yaml('test: false', file_name='test_from_yaml.yaml')
    except Exception as e:
        print('%s' % e)
        raise Exception('test_from_yaml failed')


# Generated at 2022-06-13 07:26:08.384397
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import types

    content = '''
    vars:
        - name: path
          value: /openshift-ansible
    '''
    content_as_yaml = '\n'.join(content.split())

    result = from_yaml('[{}]'.format(content_as_yaml))
    assert(type(result) is types.ListType)
    assert(len(result) == 1)

    result = from_yaml('{{{}}}'.format(content_as_yaml))
    assert(type(result) is types.DictType)
    assert(len(result) == 1)
    assert(len(result.get('vars')) == 1)
    assert(result.get('vars')[0].get('name') == 'path')

    result = from_y

# Generated at 2022-06-13 07:26:14.015902
# Unit test for function from_yaml
def test_from_yaml():
    fy = from_yaml

    assert fy('"string"') == 'string'
    assert fy('1') == 1
    assert fy('-1') == -1
    assert fy('1.1') == 1.1
    assert fy('-1.1') == -1.1
    assert fy('true') is True
    assert fy('false') is False
    assert fy('null') is None
    assert fy('[1,2,3]') == [1,2,3]
    assert fy('{"foo": "bar"}') == {'foo': 'bar'}

# Generated at 2022-06-13 07:26:14.605814
# Unit test for function from_yaml
def test_from_yaml():
    pass

# Generated at 2022-06-13 07:26:25.535915
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultSecret

    # Test a file that is parsable as YAML but not as JSON
    # this is a minimal example, to keep the size (and the diff while debugging) small
    illformed_yaml = '''
            [
                {
                    "provider": "aws",
                    "region_name": "us-east-1",
                    "aws_access_key_id": "my_access_key"
                }
            ]
        '''

    vault_secret = VaultSecret({'vault_id': 'ATLAS'})
    yaml_data = from_yaml(illformed_yaml, vault_secrets=vault_secret)
    assert len(yaml_data) == 1

    # Test a file that is neither JSON, nor YAML
    ill

# Generated at 2022-06-13 07:26:34.939908
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six import StringIO

    test_data = StringIO(u'---\n')
    assert from_yaml(test_data) is None
    test_data = StringIO(u'--- # comment\n - 1\n- 2\n- 3\n')
    assert from_yaml(test_data) == [1, 2, 3]
    test_data = StringIO(u'--- { "a": 1 }\n')
    assert from_yaml(test_data) == {"a": 1}
    test_data = StringIO(u'---\n- 1\n- 2\n- 3\n...\n')
    assert from_yaml(test_data) == [1, 2, 3]

# Generated at 2022-06-13 07:26:36.352017
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from_yaml(data)
    except:
        pass

# Generated at 2022-06-13 07:26:45.178593
# Unit test for function from_yaml
def test_from_yaml():

    test_data = u'''
    foo: 1
    bar:
        - 2
        - 3
    '''
    ansibledata = from_yaml(test_data)

    # test if it is really a dictionary and the value of the key 'foo' is 1
    assert type(ansibledata) == dict
    assert ansibledata['foo'] == 1

    # test if the value of the key 'bar' is a list that includes 2 and 3
    assert type(ansibledata['bar']) == list
    assert 2 in ansibledata['bar']
    assert 3 in ansibledata['bar']

# Generated at 2022-06-13 07:26:52.034074
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import from_yaml
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.module_utils._text import to_text, to_bytes
    import ansible.module_utils.six as six

    def _do_test(input_data, expected_output_data):
        '''
        Tests whether function from_yaml converts input_data correctly.
        '''
        data = from_yaml(input_data)
        if not isinstance(data, (AnsibleMapping, AnsibleSequence)):
            data = type(data)
        assert isinstance(data, type(expected_output_data))

# Generated at 2022-06-13 07:27:01.404485
# Unit test for function from_yaml
def test_from_yaml():

    # Test a simple example from the documentation
    data = from_yaml('''
    a simple dict:
        key 1:
            key 2:
                - one
                - two
    ''')
    assert data == {'a simple dict': {'key 1': {'key 2': ['one', 'two']}}}

    # Test for vault json string

# Generated at 2022-06-13 07:27:06.411752
# Unit test for function from_yaml
def test_from_yaml():
    # Test AnsibleJSONDecoder (which is encapsulated by from_yaml)
    class TestClass(object):
        def __init__(self, data):
            self.data = data

    test_object = TestClass(42)
    test_data = {
        "test": test_object
    }
    obj_str = json.dumps(test_data, cls=AnsibleJSONDecoder)

# Generated at 2022-06-13 07:27:26.678266
# Unit test for function from_yaml
def test_from_yaml():
    import os
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = 'test_from_yaml'
    file_name = os.path.join(test_dir, test_file)
    with open(file_name) as test_f:
        data = test_f.read()
    new_data = from_yaml(data, file_name=file_name)

# Generated at 2022-06-13 07:27:38.465235
# Unit test for function from_yaml
def test_from_yaml():
    import sys

    # Just in case the assert below fails, print exception
    # TODO: How do I get pytest to print errors?
    def excepthook(type, value, tb):
        sys.__excepthook__(type, value, tb)
    sys.excepthook = excepthook

    # Show error on assert
    try:
        from_yaml('- foo', file_name='font.yml', show_content=True, vault_secrets='foo')
        assert False
    except AnsibleParserError as e:
        assert e.show_content == '''- foo
  ^'''