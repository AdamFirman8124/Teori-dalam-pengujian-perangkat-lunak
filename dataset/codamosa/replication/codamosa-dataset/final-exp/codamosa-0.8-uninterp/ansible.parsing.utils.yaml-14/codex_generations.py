

# Generated at 2022-06-13 07:17:37.256270
# Unit test for function from_yaml
def test_from_yaml():
    class secret(object):
        def __init__(self, vault_wrapped):
            self.vault_wrapped = vault_wrapped
        def get_decrypted_text(self):
            return u"super secret!"
    assert from_yaml("""---\nfoo: {{ vault_secret }}\n""", vault_secrets=[secret("vault_secret")]) == {"foo" : "super secret!"}
    # If a vault secret is not passed we should receive the content of it as is
    assert from_yaml("""---\nfoo: {{ vault_secret }}\n""") == {"foo" : "{{ vault_secret }}"}
    # Check that a vault secret is not leaked - in the next test we should still see: "{{ vault_secret }}"

# Generated at 2022-06-13 07:17:46.738958
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    from_yaml_str = """
    hello: world
    foo: !!str 42
    """

    from_json_str = """
    {
        "hello": "world",
         "foo": "42"
    }
    """


# Generated at 2022-06-13 07:17:57.352496
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml("""
    - hosts: localhost
      tasks:
      - ping:
    """)
    from_yaml("""
    - hosts: localhost
      tasks:
      - ping:
      - ping:
    """)
    from_yaml("""
    - hosts: localhost
      user: root
      tasks:
      - ping:
    """)
    from_yaml("""
    - hosts: localhost
      gather_facts: yes
      tasks:
      - ping:
    """)
    from_yaml("""
    - hosts: localhost
      gather_facts: false
      tasks:
      - ping:
    """)
    from_yaml("""
    - hosts: localhost
      serial: 3
      tasks:
      - ping:
    """)

# Generated at 2022-06-13 07:18:06.459132
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import shutil
    import tempfile
    import unittest


# Generated at 2022-06-13 07:18:14.789184
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.manager import VariableManager

    ansible_mod_1 = AnsibleMapping()
    ansible_mod_1['foo'] = 'bar'
    ansible_mod_1['baz'] = AnsibleSequence()
    ansible_mod_1['baz'].append('quux')
    res = from_yaml(AnsibleDumper(None, 0, VariableManager(), True).dump(ansible_mod_1))
    assert res.get('foo') == 'bar'
    assert res.get('baz') == ['quux']

# Generated at 2022-06-13 07:18:22.515116
# Unit test for function from_yaml
def test_from_yaml():
    data = """
    - hosts: localhost
      connection: local
      gather_facts: no
      tasks:
        - name: hello world
          debug:
            msg: "hello world!"
    """

    res = from_yaml(data)
    assert res == [
        {
            'hosts': 'localhost',
            'connection': 'local',
            'gather_facts': 'no',
            'tasks': [
                {
                    'name': 'hello world',
                    'debug': {
                        'msg': 'hello world!'
                    }
                }
            ]
        }
    ]



# Generated at 2022-06-13 07:18:29.203795
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader

    dl = DataLoader()
    if dl is not None:
        # Create a new dictionary
        testDict = {
            "testStr": "test",
            "testInt": 42,
            "testBool": True,
            "testList": [1,2,3,4,5],
            "testDict": {
                "test1": "test1",
                "test2": "test2",
                "test3": "test3"
            },
            "testNone": None
        }
        # Create yaml string
        testString = dl.dict_to_yaml(testDict)
        # Load yaml string
        testYaml = from_yaml(testString)
        # Do test
        assert testDict

# Generated at 2022-06-13 07:18:30.623027
# Unit test for function from_yaml
def test_from_yaml():
    pass

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:18:38.605935
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.vault import VaultLib
    import crypt

    vault_password = "vaultpass"
    vault = VaultLib(vault_password)
    secret = "secret"
    if crypt.CRYPT_AVAILABLE:
        secret = vault.encrypt(secret)

    test_string = '''
---
test: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          %s
    ''' % (secret)
    assert "secret" == from_yaml(test_string, vault_secrets=[vault_password])['test']

# Generated at 2022-06-13 07:18:43.448628
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    assert loader.load_from_file('test.json', '{"a": 1, "b": 2, "c": 3}') == {'a': 1, 'b': 2, 'c': 3}
    assert loader.load_from_file('test.json', '["a", 1, "b", 2, "c", 3]') == ['a', 1, 'b', 2, 'c', 3]
    assert loader.load_from_file('test.yaml', 'a: 1\nb: 2\nc: 3\n') == {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-13 07:18:54.940785
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.vault import VaultLib
    vault_secrets = VaultLib([])
    vault_secrets.secrets = {
        'password': 'secret'
    }

    assert from_yaml("{'foo': 'bar'}", vault_secrets=vault_secrets) == {u'foo': u'bar'}
    assert from_yaml("{'foo': 'bar'}", vault_secrets=None) == {u'foo': u'bar'}
    assert from_yaml("{'foo': 'bar'}", json_only=True) == {u'foo': u'bar'}

# Generated at 2022-06-13 07:19:05.950496
# Unit test for function from_yaml
def test_from_yaml():
    '''
        from_yaml test
    '''
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_secrets = None

    if not isinstance(vault_secrets, VaultLib):
        vault_secrets = VaultLib([])


# Generated at 2022-06-13 07:19:19.743353
# Unit test for function from_yaml
def test_from_yaml():

    string = """
hello:
  x: 1
  y: b
  z: "1"
    """

    data = from_yaml(string)
    assert data['hello']['x'] == 1
    assert data['hello']['y'] == 'b'
    assert data['hello']['z'] == '1'

    string = """
- [ 'http://foo.com', 'http://bar.com' ]
- [ 'http://baz.com' ]
    """

    data = from_yaml(string)
    assert data[0] == ['http://foo.com', 'http://bar.com']
    assert data[1] == ['http://baz.com']

    string = "{'a': 1, 'b': 'b'}"

    data = from_yaml(string)

# Generated at 2022-06-13 07:19:29.287732
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.dataloader import DataLoader

    ds = dict(
        a=[dict(b=1), dict(c=2, d=3)],
        e=dict(f=4)
    )

    yaml = """
a:
- b: 1
- c: 2
  d: 3
e:
  f: 4
"""

    loader = DataLoader()
    yaml_data = loader.load(yaml)
    assert yaml_data == ds
    assert loader.dump(ds) == yaml

    # Test custom python class encoding
    class Test(object):
        def __init__(self, val=None):
            self.val = val


# Generated at 2022-06-13 07:19:39.094090
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.vars.hostvars import HostVars
    import os

    cur_dir = os.getcwd()
    os.chdir(os.path.join(cur_dir, '..', 'test_vars'))
    play_yml = open('play_test.yml', 'r').read()
    play = from_yaml(play_yml)
    assert isinstance(play, Play)


# Generated at 2022-06-13 07:19:44.775481
# Unit test for function from_yaml
def test_from_yaml():
    assert (from_yaml(None) is None)
    assert(from_yaml({}) == [])
    assert(from_yaml({1: 1}) == {1: 1})
    assert(from_yaml([1, 2]) == [1, 2])
    assert(from_yaml([1, 2, 3]) == [1, 2, 3])

# Generated at 2022-06-13 07:19:53.237334
# Unit test for function from_yaml
def test_from_yaml():
    yaml_data = '''
---
- name: Test Playbook
  hosts: testhost
  tasks:
    - name: Test task
      debug:
        msg: 'Testing ansible-doc, ansible-playbook, etc...'
'''
    yaml_list = from_yaml(yaml_data)
    assert type(yaml_list[0]) == dict
    assert yaml_list[0]['name'] == 'Test Playbook'
    assert type(yaml_list[0]['hosts']) == str
    assert type(yaml_list[0]['tasks']) == list
    assert type(yaml_list[0]['tasks'][0]) == dict
    assert yaml_list[0]['tasks'][0]['name'] == 'Test task'
    assert type

# Generated at 2022-06-13 07:20:07.659251
# Unit test for function from_yaml
def test_from_yaml():
    # Test bad json and good json
    assert from_yaml("{'key':'value'}") == {'key': 'value'}
    assert from_yaml("{'key':'value}") is None
    # Test bad yaml and good yaml
    assert from_yaml("- key: value\n- foo: bar") == [{'key': 'value'}, {'foo': 'bar'}]
    assert from_yaml("- key: value\n  foo: bar") is None
    # Test bad json and good yaml
    assert from_yaml("- key: value\n  foo: bar", json_only=True) is None
    assert from_yaml("{'key':'value'}", json_only=True) == {'key': 'value'}

# Generated at 2022-06-13 07:20:12.019185
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.ajson import _find_in_dict


# Generated at 2022-06-13 07:20:20.358505
# Unit test for function from_yaml
def test_from_yaml():
    json_return = { 'changed': False, 'msg': 'Successfully initialized the Ansible Vault' }
    assert json_return == from_yaml(json.dumps(json_return), file_name="f", show_content=True, vault_secrets=None, json_only=False)

    yaml_return = { 'changed': False, 'msg': 'Successfully initialized the Ansible Vault' }
    assert yaml_return == from_yaml(yaml.dump(yaml_return), file_name="f", show_content=True, vault_secrets=None, json_only=False)

# Generated at 2022-06-13 07:20:35.064108
# Unit test for function from_yaml
def test_from_yaml():
    yaml_1 = """\
            ---
            - hosts:
                - localhost
              connection: local
            tasks:
            - name: test
              debug: msg={{ test_var }}
            """
    yaml_2 = """\
            ---
            - hosts:
                - localhost
              connection: local
            tasks:
            - name: test
              debug: msg={{ test_var }}
            """
    json_1 = '{"test" : "test"}'
    json_2 = '{"test" : "test"}'

    assert from_yaml(yaml_1) == from_yaml(yaml_2)
    assert from_yaml(json_1) == from_yaml(json_2)

# Generated at 2022-06-13 07:20:45.638547
# Unit test for function from_yaml
def test_from_yaml():
    import ansible.parsing.vault
    from ansible.parsing.vault import VaultLib

    a = VaultLib()

    data = '"plain text"'
    assert from_yaml(data) == "plain text"

    data = "{'foo': 'bar'}"
    assert from_yaml(data) == {"foo": "bar"}

    data = "{'foo': {{ foo }} }"
    data_vault = a.encrypt(data)
    assert from_yaml(data_vault, vault_secrets=a) == {'foo': '{{ foo }}'}

    data = "---\n{'foo': {{ foo }} }\n"
    data_vault = a.encrypt(data)

# Generated at 2022-06-13 07:20:55.159339
# Unit test for function from_yaml
def test_from_yaml():
    from yaml.constructor import ConstructorError
    from yaml.parser import ParserError

    # Test YAML parser
    test_dict = {'test': {'test'}}

    # test json
    assert isinstance(from_yaml(json.dumps(test_dict)), dict)

    # test yaml
    assert isinstance(from_yaml(yaml.safe_dump(test_dict)), dict)

    # error handling

# Generated at 2022-06-13 07:20:58.492265
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    with pytest.raises(AnsibleParserError):
        from_yaml("{\"foo\" : [1,2")

# Generated at 2022-06-13 07:21:09.721583
# Unit test for function from_yaml
def test_from_yaml():
    # Try JSON
    jstring = '{"foo": 1, "bar": "baz", "k": ["one", "two"], "m": {"k1": [1, 2, 3], "k2": {"k3": "okay" }}}'
    assert from_yaml(jstring) == json.loads(jstring)

    # Try YAML
    ystring = 'foo: 1\nbar: baz\nk:\n  - one\n  - two\nm:\n  k1:\n    - 1\n    - 2\n    - 3\n  k2:\n    k3: okay'
    assert from_yaml(ystring) == json.loads(jstring)

    # Try non-existent data

# Generated at 2022-06-13 07:21:17.390670
# Unit test for function from_yaml
def test_from_yaml():
    # Simple input test
    data = '{"foo": "bar"}'
    assert isinstance(from_yaml(data), dict)
    assert from_yaml(data)['foo'] == 'bar'

    # Multiple JSON strings input test
    data = '{"foo": "bar"} {"abc": "def"}'
    assert isinstance(from_yaml(data), dict)
    assert from_yaml(data)['foo'] == 'bar'

    # YAML strings input test
    data = 'foo: bar\nabc: def'
    assert isinstance(from_yaml(data), dict)
    assert from_yaml(data)['foo'] == 'bar'
    assert from_yaml(data)['abc'] == 'def'

    # YAML with JSON strings input test

# Generated at 2022-06-13 07:21:19.058999
# Unit test for function from_yaml
def test_from_yaml():
    data = "{\"a\": 1}"
    assert from_yaml(data) == {"a": 1}



# Generated at 2022-06-13 07:21:28.819981
# Unit test for function from_yaml
def test_from_yaml():
    import sys
    # Create a test case.
    class TestCase(object):
        def __init__(self, desc, data, expected, expected_exc_type=None, expected_exc_err=None):
            self.desc = desc
            self.data = data
            self.expected = expected
            self.expected_exc_type = expected_exc_type
            self.expected_exc_err = expected_exc_err

        def run(self):
            print('Running test: %s' % self.desc, end=' ')

# Generated at 2022-06-13 07:21:39.032651
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Test from_yaml() with a yaml file.
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    input_data = """
    ---
    - hosts: localhost
      tasks:
        - name: Print a message
          debug:
              msg: The hostname is {{ ansible_hostname }}
    """
    input_file = "input_data.yml"
    with open(input_file, 'w') as f:
        f.write(input_data)

    loader = DataLoader()
    play = Play.load(input_file, loader=loader)

    # Test with an empty PlayContext
    context = PlayContext()
    play.set

# Generated at 2022-06-13 07:21:46.115496
# Unit test for function from_yaml
def test_from_yaml():

    # Positive test for YAML
    yaml_file_path = os.path.dirname(os.path.realpath(__file__)) +'/fixtures/test.yml'
    yaml_data = open(yaml_file_path, 'r').read()
    assert from_yaml(yaml_data) == {'key': 'value'}

    # Positive test for JSON
    json_file_path = os.path.dirname(os.path.realpath(__file__)) +'/fixtures/test.json'
    json_data = open(json_file_path, 'r').read()
    assert from_yaml(json_data, json_only=True) == {'key': 'value'}

    # Negative test for None
    assert from_yaml(None) == None

    # Negative

# Generated at 2022-06-13 07:21:58.061679
# Unit test for function from_yaml
def test_from_yaml():
    import os
    from ansible.module_utils.six import BytesIO

    class AnsibleJsonDecoder(AnsibleJSONDecoder):
        def __init__(self, *args, **kwargs):
            super(AnsibleJsonDecoder, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 07:22:08.286828
# Unit test for function from_yaml
def test_from_yaml():
    test_str = '''
- hosts:
    - foo
    - bar
  become: False
  become_user: root
  tasks:
    - name: test task
      debug:
        var: test_var
    - name: test2 task
      debug:
        var: test2_var
'''
    result = from_yaml(test_str)
    assert result == [{'become': False, 'become_user': 'root', 'hosts': ['foo', 'bar'], 'tasks': [{'debug': {'var': 'test_var'}, 'name': 'test task'}, {'debug': {'var': 'test2_var'}, 'name': 'test2 task'}]}]

# Generated at 2022-06-13 07:22:22.717474
# Unit test for function from_yaml
def test_from_yaml():

    assert from_yaml('[1,2,3]') == [1, 2, 3]
    assert from_yaml('{"a": "b"}') == {'a': 'b'}
    assert from_yaml('{"a": "b"}', json_only=True) == {'a': 'b'}
    assert from_yaml('{"a": "b"}', json_only=True) == {'a': 'b'}
    assert from_yaml('[1,2,3]', json_only=True) == [1, 2, 3]
    assert from_yaml('[nothing to see here]', json_only=True)
    assert from_yaml('[nothing to see here]', json_only=True).get('skip_ansible_lint')

# Generated at 2022-06-13 07:22:29.748528
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing import vault
    from ansible.parsing.vault import VaultLib

    # Define the test data to be used for the tests
    vault_test_data = """
vault_password_file: vault_password_file_path

vars:
  play_role_id: xxx
  play_vault_password: yyy

tasks:

- name: Do something
  import_role:
    name: "{{ play_role_id }}"
    vault_password: "{{ play_vault_password }}"
"""

    # Test data with a JSON string
    json_test_data = '{"a": "{{ b }}", "c": "{{ d }}"}'

    # Test data with a YAML string

# Generated at 2022-06-13 07:22:38.243212
# Unit test for function from_yaml
def test_from_yaml():
    # JSON unit test
    yaml_data = dict(a=5)
    json_data = json.dumps(yaml_data)
    assert from_yaml(json_data) == yaml_data

    # YAML unit test
    from_yaml_data = from_yaml(yaml_data)
    assert from_yaml_data == yaml_data

    # JSON and YAML unit test
    assert from_yaml(yaml_data, json_only=True) == yaml_data

# Generated at 2022-06-13 07:22:47.546238
# Unit test for function from_yaml
def test_from_yaml():
    # Test for valid input
    data = '''
    - hosts: all
      tasks:
        - name: check if the test file is setup
          stat:
            path: "/tmp/test"
          register: file_stat

        - name: create test file
          file:
            path: "/tmp/test"
            state: touch

        - name: Append line to test file
          lineinfile:
            path: "/tmp/test"
            line: "Hello World"

        - name: check if the test file is setup
          stat:
            path: "/tmp/test"
          register: file_stat
    '''


# Generated at 2022-06-13 07:22:57.817873
# Unit test for function from_yaml
def test_from_yaml():
    # We test the case of JSON_only=True in the unit tests for ansible-vault
    # Here we test it with JSON_only=False
    assert from_yaml('test') == 'test'
    assert from_yaml('test', json_only=False) == 'test'
    assert from_yaml('{"test": "value"}', json_only=False) == {'test': 'value'}
    assert from_yaml('- test\n- one\n', json_only=False) == ['test', 'one']
    assert from_yaml('[test, one]', json_only=False) == ['test', 'one']
    assert from_yaml('[test, one]', json_only=True) == AnsibleParserError

# Generated at 2022-06-13 07:22:59.643905
# Unit test for function from_yaml
def test_from_yaml():
    pass

if __name__ == "__main__":
    test_from_yaml()

# Generated at 2022-06-13 07:23:07.925695
# Unit test for function from_yaml
def test_from_yaml():
    data = """
{
        "name": "test",
        "command": "echo hello"
}
"""

    try:
        new_data = from_yaml(data)
        assert new_data is not None
        assert new_data['name'] == 'test'
        assert new_data['command'] == 'echo hello'

    except AnsibleParserError as e:
        print('AnsibleParserError in python code %s' % e)

    try:
        data = """
{
    {
        "name": "test",
        "command": "echo hello"
}
"""
        new_data = from_yaml(data)
        assert new_data is None
    except AnsibleParserError as e:
        assert e is not None
        print('AnsibleParserError in python code %s' % e)

# Generated at 2022-06-13 07:23:15.482062
# Unit test for function from_yaml
def test_from_yaml():
    """Verify that we get the expected data structure after parsing a JSON string as YAML"""
    json_string = '''
    { "name": "Bob", "phone": "555-1234", "age": 35, "address": { "city": "San Francisco", "state": "CA"} }
    '''
    expected_result = {u'address': {u'state': u'CA', u'city': u'San Francisco'}, u'name': u'Bob', u'phone': u'555-1234', u'age': 35}
    actual_result = from_yaml(json_string, file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert actual_result == expected_result

# Generated at 2022-06-13 07:23:30.395367
# Unit test for function from_yaml
def test_from_yaml():
    # testing for JSON failover
    test_data = [
        # test JSON failover
        (dict(data="{}"), type(dict())),
        (dict(data="[]"), type(list())),
        (dict(data="1"), type(1)),
        # testing filters
        (dict(data="{{nested}}", filters=dict(nested='{ "testing": 123 }')), type(dict())),
    ]
    tmp_results = []
    for test in test_data:
        tmp_results.append(from_yaml(**test[0]) == test[1])
    assert all(tmp_results)

# Generated at 2022-06-13 07:23:34.123168
# Unit test for function from_yaml
def test_from_yaml():
    assert isinstance(from_yaml('[1, 2, 3]'), list)
    assert isinstance(from_yaml('{"a": "b"}'), dict)

# Generated at 2022-06-13 07:23:39.594133
# Unit test for function from_yaml
def test_from_yaml():
    assert (from_yaml("{a: 1}", json_only=True) == {'a': 1})
    assert (from_yaml("{a: 1}") == {'a': 1})
    assert (from_yaml("\n1\n") == 1)

# Generated at 2022-06-13 07:23:48.506051
# Unit test for function from_yaml
def test_from_yaml():
    data = [{'foo': 'bar'}]
    json_data = json.dumps(data)
    yaml_data = "---\n- foo: bar\n"
    yaml2_data = "[{ foo: bar }]\n"
    assert data == from_yaml(json_data, json_only=True)
    assert data == from_yaml(yaml_data, json_only=True)
    assert data == from_yaml(yaml2_data, json_only=True)

# Generated at 2022-06-13 07:23:59.256480
# Unit test for function from_yaml
def test_from_yaml():
    try:
        from collections import OrderedDict
    except ImportError:
        # Python < 2.7
        from ansible.utils.ordereddict import OrderedDict


# Generated at 2022-06-13 07:24:05.052012
# Unit test for function from_yaml
def test_from_yaml():
    data = '{"foo": 1, "bar": [2, 3]}'

    # Test with JSON string
    new_data = from_yaml(data)
    assert new_data == json.loads(data)

    # Test with YAML string
    data2 = '{"foo": 1,\n"bar": [2, 3]}'
    new_data = from_yaml(data2)
    assert new_data == json.loads(data)

# Generated at 2022-06-13 07:24:09.228239
# Unit test for function from_yaml
def test_from_yaml():
    ret = from_yaml('''{
        "a": 1,
        "b": 2,
        "c": null
    }''', file_name='<string>', show_content=True, vault_secrets=None, json_only=False)
    assert(ret['a'] == 1)
    assert(ret['b'] == 2)
    assert(ret['c'] is None)

# Generated at 2022-06-13 07:24:11.114983
# Unit test for function from_yaml
def test_from_yaml():
    print('from_yaml', from_yaml('''--- # just a comment
# another comment
a: b
c:
- 1
- 2
- 3
'''))



# Generated at 2022-06-13 07:24:19.987015
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    _test_string = u"""
{
    "key1": "value1",
    "key2": [ "item1", "item2" ],
    "key3": { "key4": "value4", "key5": "value5" },
    "key6": null
}"""

    assert from_yaml(_test_string, json_only=True) == json.loads(_test_string)
    assert from_yaml(_test_string) == yaml.load(_test_string, Loader=yaml.Loader, Dumper=AnsibleDumper)

# Generated at 2022-06-13 07:24:33.931788
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import tempfile
    import fixtures

    # Create a test file and directory in the temp directory
    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, 'test.yml')
    test_dir = os.path.join(temp_dir, 'test')
    os.mkdir(test_dir)

    # Create the test data

# Generated at 2022-06-13 07:24:51.897488
# Unit test for function from_yaml
def test_from_yaml():
    '''
    This function runs as a unit test to ensure the from_yaml() function
    conforms to the expected behavior.
    '''
    import unittest

    class AnsibleFromYamlTestCase(unittest.TestCase):

        def test_json_input(self):
            json_input = '{"some": "data"}'
            res = from_yaml(json_input)
            self.assertEqual(res['some'], 'data')


# Generated at 2022-06-13 07:24:56.187267
# Unit test for function from_yaml
def test_from_yaml():
    print(from_yaml('{ "a": [1,2] }'))
    """
    {'a': [1, 2]}
    """


if __name__ == '__main__':
    test_from_yaml()

# Generated at 2022-06-13 07:25:02.846081
# Unit test for function from_yaml
def test_from_yaml():
    test_json = '{"a": 1, "b": "c"}'
    assert isinstance(from_yaml(test_json), dict) is True

    test_yaml = '''
                ---
                # test yaml doc
                a: 1
                b: c
                '''
    assert isinstance(from_yaml(test_yaml), dict) is True

    test_invalid = "this is not valid yaml or json"
    try:
        from_yaml(test_invalid)
    except AnsibleParserError:
        pass # pass the test if exception was successfully generated

# Generated at 2022-06-13 07:25:04.261203
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml import from_yaml
    assert from_yaml('true') == True

# Generated at 2022-06-13 07:25:09.022529
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml("{}") == {}, "Failed on JSON"
    assert from_yaml("[1,2,3]") == [1,2,3], "Failed on JSON"
    assert from_yaml("''") == '', "Failed on JSON"
    assert from_yaml("foo") == 'foo', "Failed on JSON"

# Generated at 2022-06-13 07:25:11.959160
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('') == None
    assert from_yaml('{}') == {}
    assert from_yaml('{"test":1}') == {"test": 1}
    assert from_yaml('"test"') == "test"
    assert from_yaml('1') == 1
    assert from_yaml('[1,2]') == [1,2]
    assert from_yaml('{"test":[1,2]}') == {"test": [1,2]}

# Generated at 2022-06-13 07:25:15.272453
# Unit test for function from_yaml
def test_from_yaml():
    test_data = """
    #!yaml
    foo:
      - game: "test game"
        name: "test name"

      - game: "test game1"
        name: "test name2"
    """
    expected_data = dict(
        foo=[
            dict(
                game="test game",
                name="test name",
            ),
            dict(
                game="test game1",
                name="test name2",
            ),
        ],
    )
    assert from_yaml(test_data) == expected_data

# Generated at 2022-06-13 07:25:21.861889
# Unit test for function from_yaml
def test_from_yaml():

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    data = """
    - hosts: all
      vars:
          zoo: 42
      tasks:
      - debug:
          msg: "Zoo is {{ zoo }}"
    """

    file_name = '<string>'
    show_content = True

    # from_yaml should be checked using vault_secrets=None, i.e. when no decryption was done.
    # This is because AnsibleJSONDecoder.set_secrets() sets the vault_secrets for further
    # decryption and AnsibleJSONDecoder does not have a reset method.
    vault_secrets = None # None will skip vault decryption.
   

# Generated at 2022-06-13 07:25:32.094039
# Unit test for function from_yaml
def test_from_yaml():
    import os
    import yaml_testcases
    import yaml

    yaml_test_dir = os.path.dirname(yaml_testcases.__file__)

    for k in yaml_testcases.testcases:
        testfile = yaml_test_dir + "/" + k
        vyaml = open(testfile, "r")
        vdata = vyaml.read()
        vyaml.close()

        vyaml = open(testfile, "r")
        vyaml = yaml.load(vyaml)

        # check data from both parsers
        assert from_yaml(vdata, file_name=testfile) == vyaml, "Data from vyaml doesn't match YAML parser data for input file %s" % testfile


# Generated at 2022-06-13 07:25:41.670819
# Unit test for function from_yaml
def test_from_yaml():
    ansible_vars = """
    ---
    - hosts: all
      gather_facts: no
      tasks:
      - name: Check if puppet is installed
        raw: dpkg -s puppet; echo $?
        register: puppet_installed
"""
    # Test YAML file, Ansible support this file
    try:
        from_yaml(ansible_vars)
    except AnsibleError:
        raise AssertionError("Failed to load ansible_vars")
    # Test JSON file, Ansible does not support this file

# Generated at 2022-06-13 07:25:59.744053
# Unit test for function from_yaml
def test_from_yaml():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.reader import AnsibleFileReader
    from ansible.parsing.yaml.scanner import AnsibleScanner

    new_data = _safe_load(
        AnsibleFileReader(file_name="tests/lib/ansible/parsing/yaml/data/comments.yml"),
        file_name="tests/lib/ansible/parsing/yaml/data/comments.yml"
    )

    assert isinstance(new_data, AnsibleMapping)
    assert new_data.ansible_pos == ("tests/lib/ansible/parsing/yaml/data/comments.yml", 1, 1)


# Generated at 2022-06-13 07:26:02.917429
# Unit test for function from_yaml
def test_from_yaml():
    data = "{'foo': 'bar'}"
    result = from_yaml(data)
    assert result == {'foo': 'bar'}

# Generated at 2022-06-13 07:26:13.026825
# Unit test for function from_yaml
def test_from_yaml():
    from_yaml("", json_only=True)
    try:
        from_yaml("{a:1}")
        raise AssertionError("JSON Exception expected")
    except AnsibleParserError as e:
        assert(isinstance(e.orig_exc, ValueError))
    from_yaml("a: 1", show_content=False)
    from_yaml("a: 1", show_content=True)
    try:
        from_yaml("c", show_content=False)
        raise AssertionError("JSON Exception expected")
    except AnsibleParserError as e:
        assert(isinstance(e.orig_exc, ValueError))

# Generated at 2022-06-13 07:26:16.662384
# Unit test for function from_yaml
def test_from_yaml():
    test = from_yaml('{"foo": "bar"}')
    assert test['foo'] == 'bar'
    test = from_yaml('{"foo": "bar"}', json_only=True)
    assert test['foo'] == 'bar'

# Generated at 2022-06-13 07:26:26.947974
# Unit test for function from_yaml
def test_from_yaml():

    # Test that valid JSON string that is not valid YAML throws AnsibleParserError
    data = '{"foo": "bar"}'
    try:
        new_data = from_yaml(data, False)
        assert(False)
    except AnsibleParserError:
        assert(True)

    # Test that valid JSON string that is not valid YAML throws AnsibleParserError
    # with show_content set to False
    data = '{"foo": "bar"}'
    try:
        new_data = from_yaml(data, False)
        assert(False)
    except AnsibleParserError:
        assert(True)

    # Test that valid JSON string that is not valid YAML throws AnsibleParserError
    # with json_only set to True
    data = '{"foo": "bar"}'

# Generated at 2022-06-13 07:26:34.950551
# Unit test for function from_yaml
def test_from_yaml():

    # Test data 1
    data = """
    foo:
      bar:
        baz: string
        list:
          - a
          - b
          - c
        dict:
          d: 1
          e: 2
          f: 3
    """
    res = from_yaml(data)
    assert(res == {'foo': {'bar': {'baz': 'string',
                                   'dict': {'d': 1, 'e': 2, 'f': 3},
                                   'list': ['a', 'b', 'c']}}})

    # Test data 2

# Generated at 2022-06-13 07:26:37.719735
# Unit test for function from_yaml
def test_from_yaml():
    # TODO: some more tests
    assert from_yaml('{"key": "value"}') == {u'key': u'value'}

# Generated at 2022-06-13 07:26:42.442804
# Unit test for function from_yaml
def test_from_yaml():
    assert from_yaml('{"key": "value", "key_a": "value"}') == {'key': 'value', 'key_a': 'value'}
    assert from_yaml('key: "value"') == {'key': 'value'}
    assert from_yaml('{"key": value}') == {'key': 'value'}

# Generated at 2022-06-13 07:26:51.138713
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Unit tests for from_yaml
    '''
    from ansible.utils import json
    from io import StringIO
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.ajson import AnsibleJSONEncoder

    stream = StringIO('{"a": "b"}')
    data = from_yaml(stream.read())
    assert data == {u'a': u'b'}
    assert isinstance(data, dict)

    stream = StringIO('a: b')
    data2 = from_yaml(stream.read())
    assert data2 == {u'a': u'b'}
    assert isinstance(data2, dict)


# Generated at 2022-06-13 07:26:55.990013
# Unit test for function from_yaml
def test_from_yaml():
    import unittest
    class from_yaml_TestCase(unittest.TestCase):
        def test_from_yaml_2(self):
            self.assertEqual(from_yaml('a: 1'), {'a': 1})

        def test_from_yaml_3(self):
            self.assertEqual(from_yaml('a: 1\n'), {'a': 1})

        def test_from_yaml_4(self):
            self.assertEqual(from_yaml('a: 1\n\nb: 2'), {'a': 1, 'b': 2})


# Generated at 2022-06-13 07:27:18.741803
# Unit test for function from_yaml
def test_from_yaml():
    '''
    Run unit test to make sure that yaml key value pairs are treated the same
    whether they are separated by a colon or dash.
    '''
    test_yaml = '''
    a: b
    c-d: e
    '''

    from_yaml_result = from_yaml(test_yaml)

    # Since AnsibleBaseYAMLObject is not imported directly in to_yaml add object
    # to ensure that its loaded properly.
    if isinstance(from_yaml_result, AnsibleBaseYAMLObject):
        test_yaml_object = {'a': 'b', 'c-d': 'e'}
    else:
        test_yaml_object = from_yaml_result


# Generated at 2022-06-13 07:27:29.967245
# Unit test for function from_yaml
def test_from_yaml():
    import pytest
    from ansible.module_utils.six import PY3

    # Setup the test
    data_str = '---\ntest string\n'
    file_name = 'test_string.yml'
    show_content = True
    vault_secrets = None

    # Test with good data
    result = from_yaml(data_str, file_name=file_name, show_content=show_content, vault_secrets=vault_secrets)
    assert result == 'test string'

    # Test with good data
    data_str = '''
        ---
        test: string
        '''
    result = from_yaml(data_str, file_name=file_name, show_content=show_content, vault_secrets=vault_secrets)