

# Generated at 2022-06-13 07:38:43.725251
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    import io
    import unittest
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    if sys.version_info[0] > 2:
        # py3 base class name changed.
        # Also, py3 uses a bytes stream, not a str stream.
        # Also, py3 base loaders don't have stream
        class TestBase(unittest.TestCase):
            pass
    else:
        class TestBase(unittest.TestCase):
            def test_stream_no_unicode(self):
                # this stream does _not_ have unicode
                stream = Ans

# Generated at 2022-06-13 07:38:44.831155
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('')

    assert loader.file_name == None

# Generated at 2022-06-13 07:38:45.517274
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:38:46.663756
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''test AnsibleLoader()'''
    assert AnsibleLoader

# Generated at 2022-06-13 07:38:47.176503
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:38:56.723822
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import sys
    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO
    yaml_str = u'{ foo : [ "bar", "baz" ] }'

    # Test default string pattern
    obj = AnsibleLoader(StringIO(yaml_str)).get_single_data()
    assert obj == {'foo': ['bar', 'baz']}

    # Test regexp string pattern
    obj = AnsibleLoader(StringIO(yaml_str), regexp_patterns=[r'^foo$']).get_single_data()
    assert obj == {'foo': ['bar', 'baz']}

    # Test regexp string pattern does not match

# Generated at 2022-06-13 07:39:02.509088
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    stream = '''
# This is a playbook.
- name: echo
  hosts: localhost
  tasks:
      - name: echo hello
        shell: echo hello
'''
    loader = AnsibleLoader(stream, file_name="test")
    loader.get_single_data()


# Generated at 2022-06-13 07:39:13.168645
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=invalid-name
    import sys
    import os
    from io import StringIO
    from ansible.module_utils.common.yaml import _loader_class
    from ansible.module_utils.common.yaml import HAS_LIBYAML

    if not HAS_LIBYAML:
        return

    class TestAnsibleLoader:  # pylint: disable=too-few-public-methods
        def __init__(self):
            self.stream = StringIO(
                '''
                #
                ---
                - name: "test Ansible Loader"
                  hosts: localhost
                  connection: local
                  gather_facts: no
                  tasks:
                    - debug:
                        msg: "test Ansible Loader"
                '''
            )
            self.loader = _loader_

# Generated at 2022-06-13 07:39:13.699592
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:39:25.371084
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import yaml

    data = '''
        foobar:
            key1: val1
            key2: val2
            key3: val3
            key4: val4
            key5: val5
            key6: val6
    '''

    stream = io.StringIO(data)
    stream.name = 'foobar.yml'

    loader = AnsibleLoader(stream)
    try:
        data = yaml.load(stream, loader)
    except yaml.YAMLError as e:
        print("Yaml Error")
        print(e)
    else:
        print("Yaml is fine")
        print(data)

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:39:30.007508
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml = AnsibleLoader(file_name='/dev/null')
    print(yaml)

# Generated at 2022-06-13 07:39:41.690000
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import datetime
    from ansible.parsing.yaml.dumper import AnsibleDumper
    yaml = YAML(typ='unsafe')
    yaml.Constructor = AnsibleConstructor
    yaml.Representer.add_representer(datetime.date,
                                     AnsibleDumper.date_representer)
    yaml.Representer.add_representer(datetime.datetime,
                                     AnsibleDumper.datetime_representer)
    yaml.Representer.add_representer(datetime.time,
                                     AnsibleDumper.time_representer)
    yaml.Representer.add_multi_representer(
        type(None),
        AnsibleDumper.represent_none,
    )

# Generated at 2022-06-13 07:39:47.915841
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    assert isinstance(AnsibleLoader("!encrypted |$ANSIBLE_VAULT;1.1;AES256\nAAA...\n").get_single_data(), AnsibleVaultEncryptedUnicode)
    assert AnsibleLoader("!encrypted |$ANSIBLE_VAULT;1.1;AES256\nAAA...\n").get_single_data() == '$ANSIBLE_VAULT;1.1;AES256\nAAA...'

# Generated at 2022-06-13 07:39:57.848720
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys

    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO
    test_string = '''
    - name: test
      name: test2
      name: test3
    - name: test4
    - name: {{ test5 }}
      name: {{ test6 }}
    - name: test7
    - name: {% test8 %}
    - name: {% test9 %}
    '''
    test_file = StringIO(test_string)
    AnsibleLoader(test_file, file_name=os.path.abspath("test_AnsibleLoader"))
    assert True

# Generated at 2022-06-13 07:40:03.400420
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (2, 7):
        import unittest
    else:
        import unittest2 as unittest

    class TestConstructor(unittest.TestCase):

        def test_init(self):
            AnsibleLoader.__init__ = AnsibleConstructor.__init__

    loader = AnsibleLoader(file_name='filename', vault_secrets='vault_secrets')
    assert loader


# Generated at 2022-06-13 07:40:13.531876
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = u'\n'.join((
        u'test:',
        u' - include: foobar.yml',
        u' - import_tasks: foobar.yml',
        u' - name: user1',
        u'   user:',
        u'     name: user1',
        u'     password: $1$s3cr3t',
        u'     groups:',
        u'       - group1',
        u'       - group2',
        u' - name: user2',
        u'   user:',
        u'     name: user2',
        u'     password: $6$s3cr3t',
        u'     groups:',
        u'       - group2',
        u'       - group3',
        u'',
    ))
    import io


# Generated at 2022-06-13 07:40:14.505733
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    pass

# Generated at 2022-06-13 07:40:29.102697
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_in = """
        ---
        - hosts: all
          tasks:
            - name: test
              from_task:
                name: test
    """
    # AnsibleLoader should be able to retrieve the file name from the output of docs[0]
    # and populate AnsibleConstructor.file_name
    # The file name is set to be default when constructing AnsibleLoader
    ansibleloader = AnsibleLoader(yaml_in)
    ansibleloader.get_single_data()

    # AnsibleConstructor should not be able to retrieve the file name from the output of docs[0]
    # since AnsibleConstructor.file_name is not set.
    # The file name is set to be default when constructing AnsibleLoader
    ansibleconstructor = AnsibleConstructor(yaml_in)

    assert ansibleloader.file

# Generated at 2022-06-13 07:40:30.640707
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(1).__init__(1)

# Generated at 2022-06-13 07:40:32.446859
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestLoader(AnsibleLoader):
        pass

    cls = TestLoader
    assert cls is not None

# Generated at 2022-06-13 07:40:42.277945
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    if HAS_LIBYAML:
        from yaml import load
        assert load.__name__ == 'load'
        assert load.__doc__ == AnsibleLoader.__doc__
    else:
        from yaml import load, FullLoader
        assert load.__name__ == 'load'
        assert load.__doc__ == FullLoader.__doc__
        assert load.func_globals['Loader'] == AnsibleLoader

# Generated at 2022-06-13 07:40:44.848590
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Tests constructor of class AnsibleLoader
    loader = AnsibleLoader(None)
    assert(loader != None)

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:40:57.114436
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = u"""
    - hosts: all
      tasks:
      - name: test 9
        debug:
            msg: "{{ '{
                a: 1
                b: 2
                c: '3'
            }' | to_nice_json }}"
    """
    loader = AnsibleLoader(yaml_str)

    # Make sure that our constructor has loaded the YAML correctly.
    assert loader.get_single_data() == [
        {'hosts': 'all',
        'tasks': [{
            'debug': {'msg': u'{\n    "a": 1,\n    "b": 2,\n    "c": "3"\n}'},
            'name': 'test 9'}]}
    ]
    assert loader._yaml_get_lineno() == 11

# Generated at 2022-06-13 07:41:03.095464
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    test_data = dict(
        test_var="test var value",
    )

    test_data_as_string = """
---
test_var: test var value
"""

    loader = AnsibleLoader(test_data_as_string)

    # doc is the root node
    assert loader.get_single_data() == test_data

# Generated at 2022-06-13 07:41:16.573980
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import sys
    # test AnsibleLoader with Python3 I/O (Python2 uses str)
    if sys.version_info[0] >= 3:
        testYaml = io.StringIO("""
        - name: test
          state: present
          groups:
              - group1
              - group2
        """)
    else:
        testYaml = io.BytesIO("""
        - name: test
          state: present
          groups:
              - group1
              - group2
        """)

# Generated at 2022-06-13 07:41:20.432298
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    loader = AnsibleLoader(sys.stdin)
    assert loader


# Generated at 2022-06-13 07:41:21.138369
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:41:21.750412
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    return

# Generated at 2022-06-13 07:41:30.137962
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class Test:
        def test(self, data):
            assert data == 'working'

    test = Test()
    loader = AnsibleLoader(None)
    loader.add_constructor('!test', loader.construct_yaml_str)
    loader.add_multi_constructor('!test', loader.construct_yaml_str)
    loader.add_implicit_resolver('!test', loader.yaml_str_re)
    yaml_str = """
test: !test working
test2: !test "working"
"""
    data = loader.get_single_data(yaml_str)
    for k, v in data.items():
        getattr(test, k)(v)

# Generated at 2022-06-13 07:41:39.758153
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import copy
    import os
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    def list_duplicate(src_list):
        return list(set([x for x in src_list if src_list.count(x) > 1]))

    def dict_duplicate(src_dict):
        key_list = []
        dup_dict = {}
        for k, v in src_dict.items():
            if k not in key_list:
                key_list.append(k)
            else:
                if k in dup_dict.keys():
                    dup_dict[k].append(v)
                else:
                    dup_dict[k] = [v]
        return dup_dict


# Generated at 2022-06-13 07:41:51.328128
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    vars = {'foo': 42}
    data = '{{ foo }}'

    loader = AnsibleLoader(data, vault_secrets={})
    output = loader.get_single_data()
    assert str(output) == "42"

# Generated at 2022-06-13 07:41:54.203455
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    filenames = ['constructor.yml']
    for filename in filenames:
        with open(filename, 'r') as fin:
            data = AnsibleLoader(fin).get_single_data()
            assert data == {'key': 'value'}

# Generated at 2022-06-13 07:42:03.992312
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Load yaml file
    loader = AnsibleLoader(stream="""
        - hosts: localhost
          tasks:
            - name: test
              debug:
                msg: "{{ var.ansible_default_ipv4.address }}"
              no_log: True
        """, vault_secrets=[{'password': '123'}])
    datastructure = loader.get_single_data()
    assert isinstance(datastructure, list)
    assert isinstance(datastructure[0], dict)
    assert isinstance(datastructure[0]['tasks'], list)
    assert isinstance(datastructure[0]['tasks'][0], dict)
    assert datastructure[0]['tasks'][0]['name'] == 'test'

# Generated at 2022-06-13 07:42:07.602309
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Load yaml in AnsibleParser using AnsibleLoader
    doc = AnsibleLoader(stream={'test': 1}).get_single_data()
    # Verify test key
    assert 'test' in doc

# Generated at 2022-06-13 07:42:09.648041
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO
    s = StringIO.StringIO()
    loader = AnsibleLoader(s)
    assert loader



# Generated at 2022-06-13 07:42:10.573486
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:42:16.143540
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # AnsibleLoader
    # Define a stream
    stream = """
    ---
    name: testhost
    foo: bar
    """

    # Need a file name for the test.
    file_name = "/tmp/testhosts"

    # Call the constructor
    loader = AnsibleLoader(stream, file_name)

    # Load the stream and check
    data = loader.get_single_data()

    assert isinstance(data, dict)
    assert data == {'name': 'testhost', 'foo': 'bar'}

# Generated at 2022-06-13 07:42:16.837972
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:42:22.246732
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = {
        "item1": "value1",
        "item2": "value2",
        "item3": "value3",
    }

    import StringIO
    stream = StringIO.StringIO(AnsibleLoader.convert_to_yaml(data))
    loader = AnsibleLoader(stream)

    for d in loader.get_single_data():
        for k in d:
            assert data[k] == d[k]

# Generated at 2022-06-13 07:42:29.024483
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Unit test for AnsibleLoader
    '''
    from ansible.module_utils.common.text.converters import to_bytes
    from io import BytesIO

    obj = AnsibleLoader(BytesIO(to_bytes(u'6 * 7')))
    data = obj.get_single_data()
    assert data == 42

# Generated at 2022-06-13 07:42:53.954757
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO
    class DummyVaultSecret(object):
        def decrypt(self,v):
            return v

    try:
        s = StringIO.StringIO("""
        foo: '1' + '2'
        baz: $blah
        bam: !include notthere.yml
        """)
        l = AnsibleLoader(s, file_name='asdf', vault_secrets=DummyVaultSecret())
        assert isinstance(l, AnsibleLoader)
    except AssertionError:
        pass # not being run as a unit test

# Generated at 2022-06-13 07:42:56.687192
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io  # pylint: disable=unused-import
    stream = io.open('/dev/null', 'rb')
    AnsibleLoader(stream)

# Generated at 2022-06-13 07:43:06.814734
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("")
    assert(loader)

    # Test of constructor has attribute 'file_name'
    assert(hasattr(loader, 'file_name'))
    assert(loader.file_name is None)
    loader = AnsibleLoader("", file_name="file.yml")
    assert(loader.file_name == "file.yml")

    # Test of constructor has attribute 'vault_secrets'
    assert(hasattr(loader, 'vault_secrets'))
    assert(loader.vault_secrets is None)
    loader = AnsibleLoader("", vault_secrets="secret")
    assert(loader.vault_secrets == "secret")

# Generated at 2022-06-13 07:43:13.191053
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    if HAS_LIBYAML:
        assert hasattr(AnsibleLoader, '__init__'), "has no method __init__"
        assert hasattr(AnsibleLoader, 'check_node'), "has no method check_node"
        assert hasattr(AnsibleLoader, 'construct_document'), "has no method construct_document"
        assert hasattr(AnsibleLoader, 'construct_mapping'), "has no method construct_mapping"
        assert hasattr(AnsibleLoader, 'construct_object'), "has no method construct_object"
        assert hasattr(AnsibleLoader, 'construct_scalar'), "has no method construct_scalar"
        assert hasattr(AnsibleLoader, 'construct_yaml_int'), "has no method construct_yaml_int"

# Generated at 2022-06-13 07:43:28.090048
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.vars.unsafe_proxy import wrap_var

    data = AnsibleLoader(dict(key="value")).get_single_data()
    assert data['key'] == 'value'
    assert wrap_var(data) == wrap_var(data)

    data = AnsibleLoader(list()).get_single_data()
    assert data == []
    assert wrap_var(data) == wrap_var(data)

    data = AnsibleLoader(None).get_single_data()
    assert data is None
    assert wrap_var(data) == wrap_var(data)

    data = AnsibleLoader('string').get_single_data()
    assert data == 'string'
    assert wrap_var(data) == wrap_var(data)


# Generated at 2022-06-13 07:43:37.796882
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode

    stream = AnsibleUnicode('{ "a": "b" }')
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data == {u"a": u"b"}

    # pylint: disable=anomalous-backslash-in-string
    stream = AnsibleUnicode('[\"a\", \"b\"]')
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data == [u"a", u"b"]

    stream = AnsibleUnicode('[\"a\", \"b\"]')
    loader = AnsibleLoader(stream)
    data

# Generated at 2022-06-13 07:43:41.908635
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (3, 0):
        stream = '{ foo: 1, bar: { baz: string literal } }'
        loader = AnsibleLoader(stream, vault_secrets=[])
        data = loader.get_single_data()
        assert 'bar' in data
        assert data['bar']['baz'] == u'string literal'

# Generated at 2022-06-13 07:43:51.632317
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Test AnsibleLoader class with yaml and data
    '''
    # pylint: disable=import-error,no-name-in-module
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = AnsibleLoader("""
        - hosts: localhost
          tasks:
            - shell: echo "hello"
              when: not "{{ example_param }}"
        """).get_single_data()

    assert isinstance(data[0]['tasks'][0]['when'], AnsibleUnicode)

# Generated at 2022-06-13 07:43:53.833382
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Just make sure the class can be instanciated
    AnsibleLoader('', None).get_single_data()

# Generated at 2022-06-13 07:44:05.416444
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    vault_data = None
    fake_loader = AnsibleLoader(vault_data)
    # test if ansible_loader is an instance of AnsibleLoader
    assert isinstance(fake_loader, AnsibleLoader)
    fake_loader.file_name = '~/file_name'
    # test if file_name is in fact '~/file_name'
    assert fake_loader.file_name == '~/file_name'
    # test if vault_secrets is a instance of VaultLib
    assert isinstance(fake_loader.vault_secrets, VaultLib)
    result_

# Generated at 2022-06-13 07:44:43.677992
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultAes256

    # TODO: Write this once this is a proper class

    pass


# Generated at 2022-06-13 07:44:45.116196
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader({})  # pylint: disable=no-value-for-parameter

# Generated at 2022-06-13 07:44:46.104037
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:44:48.117974
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO
    AnsibleLoader(StringIO('---\n- ansible'))  # make sure it doesn't throw an exception

# Generated at 2022-06-13 07:44:59.398162
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys

    x = AnsibleLoader('this is a string')
    assert x.stream == 'this is a string'

    x = AnsibleLoader(u'this is a string')
    assert x.stream == 'this is a string'

    x = AnsibleLoader(10)
    assert x.stream == 10

    x = AnsibleLoader(['1', 2, 3, 4])
    assert x.stream == ['1', 2, 3, 4]

    x = AnsibleLoader({'a': 10})
    assert x.stream == {'a': 10}

    x = AnsibleLoader((10, 20, 30))
    assert x.stream == (10, 20, 30)

    class B():
        pass
    x = AnsibleLoader(B())
    assert x.stream == B()

    x = Ansible

# Generated at 2022-06-13 07:45:09.255141
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class TestAnsibleLoader():
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Parser.__init__(self, stream)  # pylint: disable=non-parent-init-called
            AnsibleConstructor.__init__(self, file_name=file_name, vault_secrets=vault_secrets)
            Resolver.__init__(self)

    import io
    import yaml
    yaml_str = """
        ---
        some_text: Hello World
    """
    stream = io.StringIO(yaml_str)
    data = yaml.load(stream, Loader=TestAnsibleLoader)
    print(data)

# Generated at 2022-06-13 07:45:11.033668
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.loader
    assert hasattr(ansible.parsing.yaml.loader, "AnsibleLoader")

# Generated at 2022-06-13 07:45:18.095495
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml

    data = """
    - name: test
      hosts: localhost
      tasks:
        - debug: msg="{{ '{{' }} lookup('dns', 'www.example.com') }}"
    """

    # fail if constructs like {{ lookup('dns', 'www.example.com') }} not evaluated in data
    assert yaml.load(data, Loader=AnsibleLoader) is not None

# Generated at 2022-06-13 07:45:19.627121
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    y = AnsibleLoader('hoge\n')
    print(y)

# Generated at 2022-06-13 07:45:20.742509
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:46:41.875015
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence
    from ansible.parsing.vault import VaultLib
    import io

    vault_secrets = {}
    vault = VaultLib(vault_secrets)

    # We want to do 'test_' prefix to test the internals, but it would be nice
    # to have the class checked.
    # FIXME: the yaml unit tests should test the Loader internals, and the
    # fix the hack above.
    stream = io.StringIO(u"---\n{foo: bar}")
    stream.name = 'ansible-yaml-test'
    loader = AnsibleLoader(stream, vault_secrets=vault_secrets)

    result = loader.get_single_data()



# Generated at 2022-06-13 07:46:50.855458
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import PY2

    if PY2:
        import StringIO as io
    else:
        import io

    stream = io.StringIO('foo: !vault |\n          $ANSIBLE_VAULT;1.2;AES256;dummyusername\n          313233343536373831323334353637383132333435363738313233343536373830\n')

    loader = AnsibleLoader(stream, 'test', [VaultSecret('AES256', 'dummyusername'), VaultSecret('AES256', 'foo')])
    loader.get_single_data()

    decrypted_data = loader.get_decrypted_

# Generated at 2022-06-13 07:47:02.464937
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.parsing.yaml.data import load
    stream = """
    test_dict:
        test_string: "{{ lookup('env','HOME') }}"
        test_int: 12
        test_var: "{{ test_var }}"
        test_dict:
            test_string: "{{ lookup('env','HOME') }}"
            test_int: 12
            test_var: "{{ test_var }}"
    """

    # Simulate the global toplevel template variables
    test_var = AnsibleUnicode('helloworld')
    stream = load(stream, dict(test_var=test_var))

    assert isinstance(stream['test_dict'], AnsibleMapping)

# Generated at 2022-06-13 07:47:04.403403
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    dumper = AnsibleLoader(None, vault_secrets=None)
    dumper.file_name = 'unittest.yaml'

# Generated at 2022-06-13 07:47:08.555715
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    string = 'foo: bar baz: qux'
    loader = AnsibleLoader(string)
    loader.get_single_data()
    foo = loader.get_single_data()['foo']
    assert foo == 'bar'
    assert isinstance(foo, AnsibleUnicode)


# Generated at 2022-06-13 07:47:10.163026
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.six import StringIO
    stream = StringIO('')
    AnsibleLoader(stream)

# Generated at 2022-06-13 07:47:16.613442
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    >>> test_AnsibleLoader()
    True
    '''

    AL = AnsibleLoader(None)
    AL.add_multi_constructor('!', None)
    AL.add_multi_constructor('!include', None)
    AL.add_multi_constructor('!include_vars', None)
    AL.add_multi_constructor('!vault', None)
    AL.add_multi_constructor('!template', None)
    assert isinstance(AL, AnsibleLoader)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:47:20.318751
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Ensure that AnsibleLoader can't be instantiated
    try:
        AnsibleLoader(None)
        assert False, "AnsibleLoader can be instantiated"
    except TypeError:
        assert True

# Generated at 2022-06-13 07:47:21.559456
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:47:23.962350
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
    - hosts: all
      gather_facts: no
      tasks:
      - name: ping
        ping:
    '''

    loader = AnsibleLoader(data)
    assert loader is not None