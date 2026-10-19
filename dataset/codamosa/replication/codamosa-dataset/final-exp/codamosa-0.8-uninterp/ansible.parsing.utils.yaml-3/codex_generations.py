

# Generated at 2022-06-13 07:17:46.104706
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import yaml
    test_case = yaml.load(open(os.path.join(os.path.dirname(__file__), 'from_yaml_testcase.yml')))
    for t in test_case:
        assert from_yaml(t['given']) == t['expected']

    # Parsing a dictionary with a wrong key
    data = '''
    a_key:
      - recurse: true
        tasks:
        - name: do stuff
          command: do stuff
          when: "{{ recurse }}"
      - recurse: false
        tasks:
        - name: do stuff
          command: do stuff
          when: "{{ recurse }}"
    '''
    try:
        from_yaml(data)
    except Exception:
        pass

# Generated at 2022-06-13 07:17:51.751619
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"key": "value", "key2": "value2"}'
    data_out = from_yaml(data)
    assert data_out == json.loads(data)

    data = '''key: "value"
key2: "value2"
'''
    data_out = from_yaml(data)
    assert data_out == {"key": "value", "key2": "value2"}

# Generated at 2022-06-13 07:18:01.159324
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml(dict(hello='world')) == dict(hello='world')
    assert from_yaml(dict(hello_world='bogus')) == dict(hello_world='bogus')
    assert from_yaml(dict(hello_world='bogus')) == dict(hello_world='bogus')
    assert from_yaml('''{"hello":"world"}''') == dict(hello='world')
    assert from_yaml('''{"hello_world":"bogus"}''') == dict(hello_world='bogus')
    assert from_yaml('''
    hello_world:
      nested: 'bogus'
    ''') == dict(hello_world=dict(nested='bogus'))

# Generated at 2022-06-13 07:18:06.636562
# Unit test for function from_yaml
def test_from_yaml():

    # Test YAML data
    data = """
    ---
    - name: foo
      bar: 1
      baz:
        - 123
        - [1, 2]
    """

    # Python equivalent data structure
    expected = [
        {'name': 'foo', 'bar': 1, 'baz': [123, [1, 2]]}
    ]

    # Assert from_yaml function returns an array
    assert isinstance(from_yaml(data), list), "from_yaml should return a list!"

    # Assert the array returned by from_yaml is equal to our expected data
    assert from_yaml(data) == expected, "from_yaml should return a list of dictionaries!"

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:15.365465
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.module_utils._text import to_bytes

    test_data = """
      foo:
      - '1'
      - '2'
      - '3'
    """

    expected_data = {'foo': ['1', '2', '3']}
    result_data = from_yaml(to_bytes(test_data))
    assert result_data == expected_data, 'got: %s' % result_data

    test_data = """
      foo:
      - 1
      - 2
      - 3
    """

    result_data = from_yaml(to_bytes(test_data))
    assert result_data == expected_data, 'got: %s' % result_data


# Generated at 2022-06-13 07:18:19.619521
# Unit test for function from_yaml
def test_from_yaml():
    yaml_file = open('collection.yml', 'r')
    data = yaml_file.read()
    yaml_file.close()
    json_data = from_yaml(data)
    print(json_data)

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:18:27.235269
# Unit test for function from_yaml
def test_from_yaml():

    # Test normal functionality of from_yaml
    data = None
    try:
        data = from_yaml("""
        ---
        - hosts: localhost
          vars:
            foo: '{{bar}}'
            baz: "{{quux}}"
        """)
    except AnsibleParserError:
        assert data is None

    data = None
    try:
        data = from_yaml("""
        ---
        - hosts: localhost
          vars:
            foo: "{{ bar }}"
            baz: "{{ quux }}
        """)
    except AnsibleParserError:
        assert data is None

    data = None

# Generated at 2022-06-13 07:18:37.047813
# Unit test for function from_yaml
def test_from_yaml():
    json_string = '{"foo": "bar"}'
    assert from_yaml(json_string) == json.loads(json_string)
    assert from_yaml(json_string, json_only=True) == json.loads(json_string)

    yaml_string = 'foo: bar'
    assert from_yaml(yaml_string) == yaml.safe_load(yaml_string)

    try:
        from_yaml(yaml_string, json_only=True)
        assert False
    except AnsibleParserError:
        pass

    try:
        from_yaml('{"foo": bar')
        assert False
    except AnsibleParserError:
        pass


# Generated at 2022-06-13 07:18:44.522001
# Unit test for function from_yaml
def test_from_yaml():
    datas = [
        {'foo': 123},
        ['bar', 'baz'],
        "test_str",
        13,
        13.0,
    ]
    for data in datas:
        assert(from_yaml(json.dumps(data)) == data)
        assert(from_yaml(json.dumps(data), json_only=True) == data)
        assert(from_yaml(json.dumps(data), json_only=False) == data)
        assert(from_yaml(data) == data)
        assert(from_yaml(data, json_only=True) == data)
        assert(from_yaml(data, json_only=False) == data)

    for data in datas:
        assert(from_yaml(json.dumps(data)) == data)


# Generated at 2022-06-13 07:18:49.210912
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.module_utils.six.moves import StringIO
    data = StringIO('{"hello": "world"}')
    result = from_yaml(data)
    assert type(result) == dict

# Generated at 2022-06-13 07:18:57.125016
# Unit test for function from_yaml
def test_from_yaml():
    import doctest
    results = doctest.testmod()
    for count, (failed, attempted) in enumerate(zip(results.failed, results.attempted)):
        if failed:
            print("Error in test #{}".format(count + 1), file=sys.stderr)

if __name__ == "__main__":
    # If run as a script, this will run the doctests
    import sys
    sys.exit(test_from_yaml())

# Generated at 2022-06-13 07:19:06.805885
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""
        foo:
          bar:
            - 1
            - 2
            - 3
          baz:
            - 1
            - 2
            - 3
        """) == {'foo': {'bar': [1, 2, 3], 'baz': [1, 2, 3]}}
    try:
        from_yaml("""
        foo:
        - bar:
        """)
        assert False, "YAML should have failed"
    except AnsibleParserError:
        pass
    try:
        from_yaml("""
        foo:
          bar:
        """)
        assert False, "YAML should have failed"
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 07:19:18.816065
# Unit test for function from_yaml
def test_from_yaml():
    # test an empty string
    assert from_yaml('') == None

    # test a comment
    assert from_yaml('# a comment') == None

    # test a string
    assert from_yaml('a string') == 'a string'

    # test a string in a list
    assert from_yaml('- a string') == ['a string']

    # test a string in a dict embeded in a list
    assert from_yaml('- a string: hi') == [{'a string': 'hi'}]

    # test invalid yaml
    try:
      from_yaml('invalid:- yaml')
    except AnsibleParserError:
      pass
    else:
      assert False, 'should throw AnsibleParserError'

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:19:28.661849
# Unit test for function from_yaml
def test_from_yaml():
    print("running yaml_dumper test")
    #import pdb; pdb.set_trace()
    # Test loading of IPv4 address
    yaml_str = """---
--- 192.168.0.1
--- 192.168.0.1
"""
    ips = from_yaml(yaml_str)
    #print("IPs: %s" % ips)
    assert ips[0] == ips[1]
    assert ips[0] != ips[2]

    # Test loading of IPv6 address
    yaml_str = """---
--- 2001:0db8:85a3:08d3:1319:8a2e:0370:7334
--- 2001:0db8:85a3:08d3:1319:8a2e:0370:7334
"""

# Generated at 2022-06-13 07:19:35.284949
# Unit test for function from_yaml
def test_from_yaml():
    data = b"""
    {
        "foo": "bar",
        "baz": "quux",
        "corge": null,
        "grault": false,
        "waldo": "false",
        "fred": "",
        "empty": "",
        "quoted": "'single quoted'",
        "doublequoted": "\"double quoted\"",
        "ansible": "yaml"
    }
    """

# Generated at 2022-06-13 07:19:47.416407
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("""
    - hosts:
      - all
    """) == [{'hosts': ['all']}]
    assert from_yaml("""
    ---
    a: b
    """) == {'a': 'b'}
    assert from_yaml("""
    ---
    - a
    - b
    """) == ['a', 'b']
    assert from_yaml("""
    - a: b
    """) == [{'a': 'b'}]
    assert from_yaml("""
    {a: b}
    """) == {'a': 'b'}
    assert from_yaml("""
    {a: {b: {c: d}}}
    """) == {'a': {'b': {'c': 'd'}}}

# Generated at 2022-06-13 07:19:51.679565
# Unit test for function from_yaml
def test_from_yaml():
    # JSON will be loaded normally
    result = from_yaml('{"foo": "bar"}')
    assert result == {"foo": "bar"}

    # YAML will be loaded normally
    result = from_yaml('foo: bar')
    assert result == {"foo": "bar"}

    # A JSON string will be loaded as YAML if it contains line-breaks
    result = from_yaml('[\n1,\n2,\n3\n]')
    assert result == [1, 2, 3]

    # A string that is neither JSON nor YAML will be loaded as YAML if it contains line-breaks
    result = from_yaml('[\n1,\n2,\nA\n]')
    assert result == [1, 2, "A"]

    # A string that is neither JSON nor Y

# Generated at 2022-06-13 07:19:57.738806
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('[1,2,3]'))
    print(from_yaml('{"a":1,"b":2,"c":3}'))
    print(from_yaml('a:1\nb:2\nc:3'))
    print(from_yaml('[1, 2, true, false, null]'))

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:20:03.125985
# Unit test for function from_yaml
def test_from_yaml():
    yaml_str = """
    name: my vm
    ip: 192.168.0.1
    hostname: test
    """

    data = from_yaml(yaml_str)

    print ("data: ", data)
    assert data["name"] == "my vm"
    assert data["ip"] == "192.168.0.1"
    assert data["hostname"] == "test"


if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:20:09.694235
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"json": ["1", "2", "3"]}'
    json_result = from_yaml(data)
    assert json_result == {u'json': [u'1', u'2', u'3']}, json_result

    data = '{"json": ["1", "2", "3"]}'
    json_result = from_yaml(data, json_only=True)
    assert json_result == {u'json': [u'1', u'2', u'3']}, json_result

    data = '{"json": ["1", "2", "3"]}'
    yaml_result = from_yaml(data, json_only=False)
    assert yaml_result == {u'json': [u'1', u'2', u'3']}, yaml_result

   

# Generated at 2022-06-13 07:20:22.078702
# Unit test for function from_yaml
def test_from_yaml():
    data_json = '[{"foo": "bar"}]'
    data_yaml = '''
- foo: bar
'''
    # create a class to test a function using arbitrary data
    class TestActions:
        def test_anothing_test(self):
            # test a function using arbitrary data
            try:
                from_yaml(data_json)
                from_yaml(data_yaml)
            except:
                print("from_yaml function test failed!")
                exit(1)
            print("from_yaml function test passed!")

    # invoke the class and it's test
    test = TestActions()
    test.test_anothing_test()

# invoke the unit test
test_from_yaml()

# Generated at 2022-06-13 07:20:29.881141
# Unit test for function from_yaml

# Generated at 2022-06-13 07:20:39.267934
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('') == None
    assert from_yaml('{}') == dict()
    assert from_yaml('[]') == list()
    assert from_yaml('{"a_key": "a_value"}') == dict(a_key='a_value')
    assert from_yaml('[1, 2, 3]') == [1, 2, 3]
    assert from_yaml('a_string') == 'a_string'

    assert from_yaml('123') == 123
    assert from_yaml('123.45') == 123.45
    assert not from_yaml('true')
    assert not from_yaml('false')
    assert from_yaml('null') == None
    assert from_yaml('{"a_key": "a_value"}', json_only=True) == dict

# Generated at 2022-06-13 07:20:44.528969
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    import os
    import ast
    import yaml
    from collections import OrderedDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    _loader = DataLoader()

    _ROLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'test', 'units', 'module_utils', 'basic', 'test_yaml.yml')
    base_path = os.path.basename(_ROLE_PATH)
    parent_dir = os.path.dirname(_ROLE_PATH)
    # initialize vault
    vault_lib = VaultLib()

# Generated at 2022-06-13 07:20:56.980656
# Unit test for function from_yaml
def test_from_yaml():
    data = """
    ---
    - hosts: all
      gather_facts: no
      tasks:
      - debug:
          msg: "Hello World"
    """
    playbook = from_yaml(data)
    assert playbook == {u'plays': [{u'hosts': u'all', u'tasks': [{u'debug': {u'msg': u'Hello World'}}], u'gather_facts': u'no'}]}


if __name__ == '__main__':
    data = """
    ---
    - hosts: all
      gather_facts: no
      tasks:
      - debug:
          msg: "Hello World"
    """
    from_yaml(data)

# Generated at 2022-06-13 07:21:08.964807
# Unit test for function from_yaml
def test_from_yaml():
    # Verify that from_yaml throws an exception if the input is not valid JSON or YAML
    try:
        from_yaml('''This is not valid JSON or YAML''', 'from_yaml_test.txt')
        assert False, 'from_yaml should have thrown an exception for invalid YAML'
    except AnsibleParserError as e:
        assert 'We were unable to read either as JSON nor YAML' in str(e)
        assert 'from_yaml_test.txt' in str(e)
        assert e.show_content() == '''This is not valid JSON or YAML'''

    # Verify that from_yaml throws an exception if the input is valid JSON, but
    # not valid YAML.

# Generated at 2022-06-13 07:21:16.949914
# Unit test for function from_yaml
def test_from_yaml():
    test_1 = """
    - hosts: localhost
      gather_facts: no
      tasks:
      - shell: 'echo "{{ test.yml }}"'
        register: test_out
      - debug:
          var: test_out.stdout_lines
    """
    test_2 = """
    - hosts: localhost
      gather_facts: no
      tasks:
      - shell: 'echo "{{ test.json }}"'
        register: test_out
      - debug:
          var: test_out.stdout_lines
    """
    test_1_result = from_yaml(test_1)
    test_2_result = from_yaml(test_2, json_only=True)

# Generated at 2022-06-13 07:21:24.669508
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.yaml.dumper
    dumper = getattr(ansible.parsing.yaml.dumper, 'AnsibleDumper', None)  # low-level API changed in PyYAML 5.1

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert from_yaml('{}') == {}
    assert from_yaml('{}', json_only=True) == {}
    assert from_yaml('[]') == []
    assert from_yaml('[]', json_only=True) == []
    assert from_yaml('{"foo": "bar"}') == {"foo": "bar"}
    assert from_yaml('{"foo": "bar"}', json_only=True) == {"foo": "bar"}

# Generated at 2022-06-13 07:21:30.566315
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    data = '''---
- hosts: all
  tasks:
    - name: this is a task
      debug:
          msg: '{{ item }}'
          test: '{{ test_var }}'
      with_items:
        - item1
        - item2
    - name: multi line task
      debug:
          msg: this is a
                  multi line
                  yaml string
'''
    from_yaml(data)

# Generated at 2022-06-13 07:21:40.067195
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Tests for function from_yaml
    '''
    assert from_yaml('HeisenBug') == 'HeisenBug'
    assert from_yaml('- HeisenBug') == ['HeisenBug']
    assert from_yaml('{ key1: HeisenBug }') == {'key1': 'HeisenBug'}

    assert from_yaml('[1, 2, 3]') == [1, 2, 3]
    assert from_yaml('[1,\n 2, 3]') == [1, 2, 3]
    assert from_yaml('[1,\n 2, 3]') == [1, 2, 3]
    assert from_yaml('[\n - one\n - two]') == ['one', 'two']


# Generated at 2022-06-13 07:21:50.110480
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('foo') == 'foo'
    assert from_yaml('[foo]') == ['foo']
    assert from_yaml('{"foo": "bar"}') == {'foo': 'bar'}
    assert from_yaml('12345') == 12345
    assert from_yaml('true') is True
    assert from_yaml('false') is False
    assert from_yaml('null') is None

# Generated at 2022-06-13 07:21:55.880506
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"nested":{"foo":"bar"}}') == {u'nested': {u'foo': u'bar'}}
    assert from_yaml('{"foo":"bar"}') == {u'foo': u'bar'}
    assert from_yaml('[{"foo":"bar"}]') == [{u'foo': u'bar'}]
    assert from_yaml('{"foo":"bar","baz":"baq"}') == {u'foo': u'bar', u'baz': u'baq'}

# Generated at 2022-06-13 07:22:07.286807
# Unit test for function from_yaml
def test_from_yaml():
    y1 = '{"foo": "bar"}'
    assert from_yaml(y1) == {"foo": "bar"}

    y2 = 'foo: bar'
    assert from_yaml(y2) == {"foo": "bar"}

    y3 = '"foo": "bar"'
    assert from_yaml(y3) == {"foo": "bar"}

    y4 = '{"foo": "bar", "baz": [1,2,3], "qux": {"a": "b"}}'
    assert from_yaml(y4) == {"foo": "bar", "baz": [1, 2, 3], "qux": {"a": "b"}}

    y5 = "{foo: 'bar'}"

# Generated at 2022-06-13 07:22:11.497112
# Unit test for function from_yaml
def test_from_yaml():
    data = "yaml: test\nparsing:\n\t" + "success"
    assert from_yaml(data) == {'yaml': 'test', 'parsing': 'success'}

# Generated at 2022-06-13 07:22:20.729451
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('1') == 1
    assert from_yaml('1.0') == 1.0
    assert from_yaml('true') == True
    assert from_yaml('false') == False
    assert from_yaml('"hello world"') == 'hello world'
    assert from_yaml('[1, 2, "3"]') == [1, 2, "3"]
    assert from_yaml('{"key": 1, "list": [1, 2, 3]}') == {"key": 1, "list": [1, 2, 3]}

# Generated at 2022-06-13 07:22:29.036132
# Unit test for function from_yaml
def test_from_yaml():
    # Test 1: Pass invalid json string
    json_string = '{"a": "b",}'
    try:
        from_yaml(json_string)
    except AnsibleParserError:
        pass
    else:
        raise Exception("Json string passed invalid test")

    # Test 2: Pass valid json string
    json_string = '{"a": "b"}'
    ansible_dict = from_yaml(json_string)
    assert ansible_dict == {"a": "b"}

    # Test 3: Pass invalid yaml string
    yaml_string = 'key: "value"'
    try:
        from_yaml(yaml_string)
    except AnsibleParserError:
        pass
    else:
        raise Exception("Yaml string passed invalid test")

    # Test 4: Pass valid yaml string


# Generated at 2022-06-13 07:22:40.772757
# Unit test for function from_yaml
def test_from_yaml():
    # import needed for unit test
    from ansible.parsing.vault import VaultLib

    # from_yaml should load a simple YAML string
    assert from_yaml(u'{"foo": "bar"}') == {u'foo': u'bar'}

    # from_yaml should load a simple JSON string
    assert from_yaml(u'{"foo": "bar"}', json_only=True) == {u'foo': u'bar'}

    # from_yaml should not load a string that is neither JSON nor YAML
    try:
        from_yaml(u'{"foo": "')
    except AnsibleParserError as e:
        assert 'We were unable to read either as JSON nor YAML' in e.message

    # from_yaml should not load a simple YAML that cannot be

# Generated at 2022-06-13 07:22:46.615834
# Unit test for function from_yaml
def test_from_yaml():
    print("testing from_yaml")
    data = """
    a: 1
    b:
        c: 3
        d: 4
    """
    data_json = json.dumps(from_yaml(data))
    assert '{"a": 1, "b": {"c": 3, "d": 4}}\n' == data_json

if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:22:58.115322
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.vars import VaultSecret
    from ansible.utils.vars import combine_vars
    from ansible.parsing.ajson import AnsibleJSONDecoder

    AnsibleJSONDecoder.set_secrets(None)
    d = {'foo': 'bar', 'baz': 'qux'}
    assert from_yaml(AnsibleJSONDecoder.encode(d)) == d
    assert from_yaml(AnsibleJSONDecoder.encode(d), json_only=True) == d

    assert from_yaml('{"foo":"bar"}') == d
    assert from_yaml('{"foo":"bar"}', json_only=True) == d
    assert from_yaml('foo: bar') == d
    assert from_yaml('{foo: bar}') == d

# Generated at 2022-06-13 07:23:06.927773
# Unit test for function from_yaml
def test_from_yaml():
    d1 = from_yaml('---\nhello')
    assert d1 == {'hello': None}

    d2 = from_yaml('---\nfoo: bar')
    assert d2 == {'foo': 'bar'}

    d3 = from_yaml('---\nfoo: bar\nbar: baz')
    assert d3 == {'foo': 'bar', 'bar': 'baz'}

    d4 = from_yaml('---\nfoo\nbar')
    assert d4 == ['foo', 'bar']

    d5 = from_yaml('---\n- foo\n- bar')
    assert d5 == ['foo', 'bar']

    d6 = from_yaml('---\n- foo\n- bar\n')
    assert d6 == ['foo', 'bar']

   

# Generated at 2022-06-13 07:23:19.424217
# Unit test for function from_yaml
def test_from_yaml():
    data = """---
a: 1
b:
- 2
- 3
- 4
"""

    new_data = from_yaml(data)

    assert new_data == {'a': 1, 'b': [2, 3, 4]}

# Generated at 2022-06-13 07:23:28.279882
# Unit test for function from_yaml
def test_from_yaml():
    """
    run "python -m ansible.parsing.yaml.dumper" to run this unit test
    """

    # testing with valid json
    file_name = '/tmp/test_from_yaml.json'
    json_data = '{"test": true }'
    with open(file_name, 'w') as f:
        f.write(json_data)
    new_data = from_yaml(json_data)
    with open(file_name, 'r') as f:
        assert f.read() == json_data
    with open(file_name, 'w') as f:
        f.write(json.dumps(new_data))
    with open(file_name, 'r') as f:
        assert f.read() == json_data

    # testing with valid yaml


# Generated at 2022-06-13 07:23:37.642197
# Unit test for function from_yaml

# Generated at 2022-06-13 07:23:41.730305
# Unit test for function from_yaml
def test_from_yaml():
    
    msg = '''{
        "msg": "This is a test message",
        "type": "test",
        "@version": "1",
        "source": "/dev/null",
        "tags": [
          "test"
        ],
        "test_string": "This is another test message",
        "test_number": 1,
        "test_bool": false
    }'''
    
    data = from_yaml(msg)
    # print(data)
    assert data['msg'] == "This is a test message"
    assert data['type'] == "test"
    assert data['@version'] == "1"
    assert data['source'] == "/dev/null"
    assert data['tags'] == ["test"]
    assert data['test_string'] == "This is another test message"

# Generated at 2022-06-13 07:23:48.190975
# Unit test for function from_yaml
def test_from_yaml():
    result = from_yaml("""
        - _hosts: localhost
          _debug: true
          _tasks:
            - shell: echo hi
          hostgroups:
            - localhost
            - test
          roles:
            - role1
            - role2
          _role_names:
              - testrole
            """)
    assert result == [{'_hosts': 'localhost',
                       '_debug': True,
                       '_tasks': [{'shell': 'echo hi'}],
                       'hostgroups': ['localhost', 'test'],
                       'roles': ['role1', 'role2'],
                       '_role_names': ['testrole']}]

# Generated at 2022-06-13 07:23:55.614442
# Unit test for function from_yaml
def test_from_yaml():
    data = u"""
            ---
             - egg
             - spam
             - bacon
            """
    assert from_yaml(data) == ['egg', 'spam', 'bacon'], 'failed test'

    data = u"""
            ---
             - 1
             - 2
             - 3
            """
    assert from_yaml(data) == [1, 2, 3], 'failed test'

    data = u"""
            ---
             - {spam: 1, bacon: 2}
            """
    assert from_yaml(data) == [{'spam': 1, 'bacon': 2}], 'failed test'

    data = u"""
            ---
             -
               - 1
               - 2
               - 3
            """

# Generated at 2022-06-13 07:23:57.628605
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{ "test": "yes" }') == { u'test': u'yes'}

# Generated at 2022-06-13 07:24:07.284840
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml('---\n1\n')
    from_yaml('---\n1\n', json_only=True)
    try:
        from_yaml('{')
        assert False, 'unexpected success on bad JSON'
    except AnsibleParserError:
        pass
    try:
        from_yaml('{', json_only=True)
        assert False, 'unexpected success on bad JSON'
    except AnsibleParserError:
        pass
    try:
        from_yaml('---\n1\n'[:3])
        assert False, 'unexpected success on partial YAML'
    except AnsibleParserError:
        pass



# Generated at 2022-06-13 07:24:18.890476
# Unit test for function from_yaml
def test_from_yaml():
    array = ['item1', 'item2']
    assert from_yaml("['item1', 'item2']") == array
    assert from_yaml("{'item1':'item2'}") == {'item1':'item2'}
    assert from_yaml("['item1', 'item2', {'item3':'item4'}]") == ['item1', 'item2', {'item3':'item4'}]

# Generated at 2022-06-13 07:24:33.112694
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # TEST: Parse string containing valid json
    valid_json = '{"foo": "bear"}'
    assert json.loads(valid_json) == from_yaml(valid_json)

    # TEST: Parse string containing json and ansible vault
    # NOTE: We need to include valid json here because the
    #       YAMLError we get when our json contains a vault
    #       happens when the underlying safe_load() function
    #       tries to load what's left of the json after vault
    #       decoding.

# Generated at 2022-06-13 07:24:51.416436
# Unit test for function from_yaml
def test_from_yaml():
    # FIXME:
    # This is useless since we're not testing anything if not all
    # exceptions are caught, and other than a single print statement
    # at the end we're not asserting anything either.
    print('''
************************************************************************************
WARNING!  This test was run against the version of PyYAML installed on the system,
which means it may not test the PyYAML that ansible is using.
************************************************************************************
''')
    from_yaml('')
    from_yaml('{}')
    from_yaml('---')
    from_yaml('---{}')
    from_yaml('{}{}')
    from_yaml('[]')
    from_yaml('---\n...\n')
    from_yaml('---{}\n...\n')
    from_yaml

# Generated at 2022-06-13 07:24:57.639486
# Unit test for function from_yaml
def test_from_yaml():
    import six
    yaml_string = "---\nkey: value\n"
    test_dict = {"key": "value"}
    assert from_yaml(yaml_string) == test_dict
    assert isinstance(from_yaml(yaml_string), six.types.DictType)


if __name__ == '__main__':
    from_yaml()

# Generated at 2022-06-13 07:25:02.882092
# Unit test for function from_yaml
def test_from_yaml():

    # simple test of a yaml-encoded string
    json_str = '''
        { "string": "test", "one": 1 }
    '''

    # this should work
    new_data = from_yaml(json_str, '<string>')
    assert new_data is not None
    assert isinstance(new_data, dict)
    assert new_data.get('string') == u'test'
    assert new_data.get('one') == 1

# Generated at 2022-06-13 07:25:05.117085
# Unit test for function from_yaml
def test_from_yaml():
    data = "foo bar"
    new_data = from_yaml(data)
    assert new_data == data



# Generated at 2022-06-13 07:25:13.713749
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 07:25:20.747291
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert from_yaml("{}") == {}
    assert from_yaml("{'a': 'b'}") == {u'a': u'b'}
    assert from_yaml("{'a': 'b'}", json_only=True) == {u'a': u'b'}


# Generated at 2022-06-13 07:25:31.499046
# Unit test for function from_yaml
def test_from_yaml():
    # The following is valid JSON
    json_string = """{
        "array": [1,2,3],
        "boolean": true,
        "null": null,
        "number": 123,
        "object": {"a":"b","c":"d","e":"f"},
        "string": "Hello World"
    }"""
    # The following is valid JSON but with a syntax error
    json_error = """{
        "array": [1,2,3],
        "boolean": true,
        "null":
        "number": 123,
        "object": {"a":"b","c":"d","e":"f"},
        "string": "Hello World"
    }"""
    # The following is valid YAML but not valid JSON
    # Note that 1. is not a float but an integer

# Generated at 2022-06-13 07:25:37.320748
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('''
    ---
    foo: [ 1, 2, 3 ]
    bar:
      baz: [ "one", "two", "thr**ee" ]
    ''') == {
        'foo': [1, 2, 3],
        'bar': {
            'baz': ['one', 'two', 'thr**ee']
        }
    }

# Generated at 2022-06-13 07:25:51.763284
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import sys
    import unittest

    test_dir = os.path.dirname(os.path.realpath(__file__))
    ansible_dir = os.path.dirname(test_dir)
    lib_dir = os.path.join(ansible_dir, "lib")

    sys.path.append(lib_dir)

    from ansible import constants as C
    C.HOST_KEY_CHECKING = False
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 4

    from ansible.parsing.dataloader import DataLoader

    class Test_from_yaml(unittest.TestCase):
        def test_from_yaml(self):
            dl = DataLoader()
            # Tests loading JSON without vault string
           

# Generated at 2022-06-13 07:25:59.914723
# Unit test for function from_yaml
def test_from_yaml():
    #
    # from_yaml
    #

    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    tests = [
        {'in': 'not json or yaml', 'out': 'not json or yaml'},
        {'in': '{}', 'out': {}},
        {'in': 'foo: bar', 'out': {'foo': 'bar'}},
        {'in': 'foo:\n  - bar', 'out': {'foo': ['bar']}},
        {'in': 'foo:\n  - bar\n  - baz', 'out': {'foo': ['bar', 'baz']}}
    ]


# Generated at 2022-06-13 07:26:15.827628
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit test for function from_yaml
    '''
    print('Testing:')
    data =  """
    ---
    hosts:
      - localhost
        a: 1
        b: 2
      - remotehost
        a: 2
        b: 1
    """
    json_data = "{\"hosts\": [{\"localhost\": {\"a\": 1, \"b\": 2}}, {\"remotehost\": {\"a\": 2, \"b\": 1}}]}"
    print(json.dumps(from_yaml(data), indent=4))
    print(json.dumps(json.loads(json_data), indent=4))
    print(json.dumps(from_yaml(json_data), indent=4))

if __name__ == '__main__':
    test_from_yaml

# Generated at 2022-06-13 07:26:20.175365
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleDict

    assert from_yaml("{'a': 5}") == {u'a': 5}
    assert from_yaml("{'a': 5}", json_only=True) == {u'a': 5}
    assert from_yaml("{ a: 5 }") == {u'a': 5}
    assert from_yaml("a: 5") == {u'a': 5}
    assert from_yaml("a: 5") != {u'a': '5'}

    assert from_yaml('''{ 'a': 5,
                          'b': 10}''') == {u'a': 5, u'b': 10}

    assert isinstance

# Generated at 2022-06-13 07:26:25.547621
# Unit test for function from_yaml
def test_from_yaml():
    test_text = u"{ 'user': 'test' }\n"
    show_content = True
    file_name = 'test.yml'
    vault_secrets = None
    new_data = {}

    new_data = from_yaml(test_text, show_content=show_content,
        file_name=file_name, vault_secrets=vault_secrets)


# Generated at 2022-06-13 07:26:29.572256
# Unit test for function from_yaml
def test_from_yaml():
    data = '''
    - hosts: localhost

      tasks:
        - name: Test plugin

          test:
            hello: world
          register: result
    '''

    new_data = from_yaml(data, "test_from_yaml", True, None, False)
    assert new_data[0]["hosts"] == 'localhost'

# Generated at 2022-06-13 07:26:33.273025
# Unit test for function from_yaml
def test_from_yaml():

    results = from_yaml("""
    '''
    testing dict
    '''
    - test:
        - 1
        - 2
        - 3
    """, vault_secrets=None, json_only=False)
    print(results)


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:26:37.293058
# Unit test for function from_yaml
def test_from_yaml():
    data = {}
    # add this to bottom of file
    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from units.mock.vault_secrets import VaultSecretStub


# Generated at 2022-06-13 07:26:48.296804
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.loader import _construct_mapping
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from contextlib import contextmanager

    loader = DataLoader()
    vault_password = 'ansible'

    @contextmanager
    def vault_context(text_input):
        vault = VaultLib(password='ansible')
        ret = AnsibleVaultEncryptedUnicode.from_bytes(vault.encrypt(text_input))
        yield ret

# Generated at 2022-06-13 07:26:59.909541
# Unit test for function from_yaml
def test_from_yaml():
    test_vars = dict(
        string="This is a string",
        integer=100,
        float=100.1,
        bool_true=True,
        bool_false=False,
        list_ints=[1, 2, 3],
        list_strings=["a", "b", "c"],
        dict_ints=dict(a=1, b=2, c=3),
    )

# Generated at 2022-06-13 07:27:05.830771
# Unit test for function from_yaml
def test_from_yaml():
	data = '{"a":1,"b":{"c":2,"d":3},"e":[1,2,3]}'
	file_name = "<string>"
	new_data = json.loads(data, cls = AnsibleJSONDecoder) 
	print(new_data)

if __name__ == '__main__':
	test_from_yaml()

# Generated at 2022-06-13 07:27:09.146160
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'key': 'value'}"
    from_yaml(data)
if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:27:31.631956
# Unit test for function from_yaml
def test_from_yaml():
    assert None == from_yaml('', True)


if __name__ == "__main__":
    test_from_yaml()