

# Generated at 2022-06-13 07:38:33.643444
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    symbols = ('!',)
    loader = AnsibleLoader('{}{}'.format(symbols[0], symbols[0]), None, None)
    loader.add_constructor(symbols, AnsibleLoader.construct_yaml_null)
    assert loader.get_single_data() is None

# Generated at 2022-06-13 07:38:43.185327
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import BytesIO

    yaml1 = b"""
---
# This is a test.
foo: {{ ansible_hostname }}
bar:
  - baz: test
...
    """
    file_name = "test_AnsibleLoader"
    vault_secrets = None

    loader = AnsibleLoader(BytesIO(yaml1), file_name, vault_secrets)
    data = loader.get_single_data()
    # print('data=%s' % data)

    assert data['foo'] == '{{ ansible_hostname }}'
    assert data['bar'][0]['baz'] == 'test'
    assert loader._file_name == file_name
    assert loader._vault_secrets == vault_secrets



# Generated at 2022-06-13 07:38:52.289026
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import YAMLError
    from ansible.plugins.loader import add_directory

    from ansible.parsing.vault import VaultLib, VaultSecret
    # Load import vault integration
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()


# Generated at 2022-06-13 07:39:00.143617
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence

    def check(data, expected_data):
        data = AnsibleLoader(data, '<string>').get_single_data()
        assert data == expected_data

    check("1", 1)
    check("001", 1)
    check("0o1", 1)
    check("0O1", 1)
    check("0x1", 1)
    check("0X1", 1)
    check("0b1", 1)
    check("0B1", 1)
    check("1.3", 1.3)
    check("true", True)
    check("false", False)
    check("null", None)
    check('"a"', AnsibleUnicode('a'))

# Generated at 2022-06-13 07:39:11.653486
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = '''
    ---
    - test: 123
    - included: test.yaml
    '''

    import io
    import warnings
    from StringIO import StringIO
    from io import BytesIO
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    # Test if subclass of AnsibleConstructor
    assert issubclass(AnsibleLoader, AnsibleConstructor)

    # Test constructor
    loader = AnsibleLoader(data)
    assert isinstance(loader, AnsibleLoader)

    # Test yaml_get classmethod
    yaml = loader.yaml_get()
    assert isinstance(yaml, AnsibleLoader)

    # Test yaml_get method
    yaml = loader.yaml_get()
    assert isinstance(yaml, AnsibleLoader)

# Generated at 2022-06-13 07:39:14.846393
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = """
        foo: [ one, two, three ]
        bar: "this is a {{ lookup('file', 'test.txt') }}"
    """
    loader = AnsibleLoader(data)
    loader.get_data()

# Generated at 2022-06-13 07:39:22.408206
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create an instance of AnsibleLoader class
    obj = AnsibleLoader("stream")
    # Call AnsibleLoader class _compose_node() method
    obj._compose_node("parent", "index")

    # Call AnsibleLoader class _construct_mapping() method
    obj._construct_mapping("node", "deep")

    # Call AnsibleLoader class construct_object() method
    obj.construct_object("node", "deep")

    # Call AnsibleLoader class construct_yaml_map() method
    obj.construct_yaml_map("node")

    # Call AnsibleLoader class construct_yaml_str() method
    obj.construct_yaml_str("node")

    # Call AnsibleLoader class construct_yaml_int() method
    obj.construct_yaml_int("node")

    # Call AnsibleLoader class

# Generated at 2022-06-13 07:39:23.137423
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' returns an initialized AnsibleLoader class '''
    return AnsibleLoader(None)

# Generated at 2022-06-13 07:39:27.542786
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.utils.yaml import from_yaml

    yaml_str = """
    - hosts: localhost
      tasks:
        - debug:
            msg: hi
        - debug:
            msg: bye
    """
    obj = from_yaml(yaml_str)
    assert len(obj) == 1
    assert obj[0]['hosts'] == 'localhost'

# Generated at 2022-06-13 07:39:32.679040
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    s = '''\
abc:
  - &a b
  - &b c
  - *a
def:
    <<: *a
'''
    loader = AnsibleLoader(s)
    loader.get_single_data()
    assert True

# Generated at 2022-06-13 07:39:37.146038
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test the AnsibleLoader constructor that actually needs parameters
    with pytest.raises(TypeError):
        AnsibleLoader()

# Generated at 2022-06-13 07:39:38.256292
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    object = AnsibleLoader(None)
    assert object

# Generated at 2022-06-13 07:39:44.313600
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    dummy_data = (
        "{a: b}",
        "{a: '{{foo}}'}",
        "{a: '{{foo.bar}}'}",
        "{a: '{{foo.bar.baz}}'}",
        "{a: '{{foo.bar.baz.boo}}'}",
    )
    for data in dummy_data:
        loader = AnsibleLoader(data)
        loader.get_single_data()

# Generated at 2022-06-13 07:39:50.442830
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence

    ds = '{"foo": "bar"}'
    d = AnsibleLoader(ds).get_single_data()
    assert isinstance(d, dict), "AnsibleLoader must return a dict instance"
    assert d.get('foo') == 'bar', "AnsibleLoader must return correct values"

    ds = '[1,2,3]'
    d = AnsibleLoader(ds).get_single_data()
    assert isinstance(d, AnsibleSequence), "AnsibleLoader must return a AnsibleSequence instance"

    ds = 'bar'
    d = AnsibleLoader(ds).get_single_data()

# Generated at 2022-06-13 07:40:01.528426
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    import yaml

    class TestAnsibleLoader(unittest.TestCase):
        def assert_constructor(self, data, expected):
            # Helper to test AnsibleConstructor.construct_mapping
            stream = yaml.compose(data)
            loader = AnsibleLoader(stream)
            self.assertEqual(loader.get_data(), expected)

        def test_constructor(self):
            self.assert_constructor({'foo': 'bar'}, [{'foo': 'bar'}])

# Generated at 2022-06-13 07:40:02.493671
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass


# Generated at 2022-06-13 07:40:12.869292
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    class TestAnsibleLoader(AnsibleLoader):
        def load(self):
            return self.get_node()
    secret = "The answer is 42"

# Generated at 2022-06-13 07:40:18.828607
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO

    stream = "---\n- hosts: localhost\n"
    stream = StringIO(stream)
    loader = AnsibleLoader(stream)
    list(loader) # force the parser to produce events
    assert list == loader.compose_document()



# Generated at 2022-06-13 07:40:22.383359
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import load

    data = load('[foo,bar]')
    assert data == ["foo", "bar"]


# Generated at 2022-06-13 07:40:33.361236
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:40:45.171450
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    old_vault_secrets = {
        'secret1': 'key1',
    }
    new_vault_secrets = {
        'secret2': 'key2',
    }
    file_name = 'ansible/test/data/ansible_loader_test'

    # Test with vault_secrets = None
    ansible_loader = AnsibleLoader(open(file_name, 'r'), file_name=file_name)
    assert ansible_loader.vault_secrets == {}

    # Test with vault_secrets = old_vault_secrets
    ansible_loader = AnsibleLoader(open(file_name, 'r'), file_name=file_name, vault_secrets=old_vault_secrets)
    assert ansible_loader.vault_secrets == old_vault_

# Generated at 2022-06-13 07:40:48.458610
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader, AnsibleLoader)


# Generated at 2022-06-13 07:40:54.920475
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    import io

    # AnsibleLoader.__init__() called with empty stream
    # Test that it doesn't throw an exception and that the correct type of object is returned
    test_obj = AnsibleLoader(io.BytesIO(""))
    assert type(test_obj) == AnsibleLoader

    test_obj = AnsibleLoader('[1, 2, 3]')
    assert test_obj.get_single_data() == [1, 2, 3]

# Generated at 2022-06-13 07:41:07.686949
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault_secrets = ['secret1', 'secret2']
    file_name = 'unused_file_name'
    loader = AnsibleLoader('thetext: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          62656466616437623762613661396163636633366636633638633962633464346533646630633464\n          35393262613661376333623831316662303933373061653237666362643939643033376337666666\n          64396465663534303733316364626336316337376538363537\n          ', file_name, vault_secrets)

# Generated at 2022-06-13 07:41:10.893936
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = dict(
        hash_behaviour='merge',
        list_behaviour='unique',
        string_behaviour='strip',
    )
    loader = AnsibleLoader(data, file_name='ansible-data-loaded')

    assert isinstance(loader, AnsibleLoader)

# Generated at 2022-06-13 07:41:18.408637
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import load
    from yaml.composer import ComposerError
    from yaml.parser import ParserError
    from yaml.scanner import ScannerError

    # Test user-defined tags
    assert load("!include_dir_listing /my/files") == {'include_dir_listing': '/my/files'}
    assert load("!include_vars /my/files") == {'include_vars': '/my/files'}

# Generated at 2022-06-13 07:41:19.653023
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:41:24.160194
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    test_data = b'[{u"foo": u"bar"}]'
    assert AnsibleLoader(test_data).get_single_data() == [
        AnsibleUnicode({u'foo': u'bar'})]

# Generated at 2022-06-13 07:41:33.023200
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor, list_from_yaml, dict_from_yaml, get_name
    from ansible.module_utils.common.yaml import AnsibleLoader
    from ansible.utils.unicode import to_unicode
    import re

    # Unit test for method get_name
    def test_get_name():
        n = get_name("---\n- hosts: all")
        assert n is None

        n = get_name("---\n- hosts: all\n  vars: {foo: bar}")
        assert n is None

        n = get_name("---\n- hosts: all\n  name: foo")
        assert n == "foo"


# Generated at 2022-06-13 07:41:33.916265
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:41:50.025940
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    This is a unit test for class AnsibleLoader
    """

    from ansible.parsing.yaml.objects import AnsibleUnicode

    input_data = '''
    - name: unittest
      shell: echo "{{__AnsibleUnicode__}}"
      args:
        chdir: /home/foo/bar
        executable: /bin/bash
    '''

    data = AnsibleLoader(input_data, file_name='unitTest').get_single_data()
    assert data == [{'name': 'unittest', 'args': {'executable': '/bin/bash', 'chdir': '/home/foo/bar'}, 'shell': 'echo "{{__AnsibleUnicode__}}"'}]
    data = AnsibleLoader(input_data).get_single_data()

# Generated at 2022-06-13 07:41:51.610882
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    yaml.load(stream=None, Loader=AnsibleLoader, file_name=__file__)

# Generated at 2022-06-13 07:42:01.098526
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    >>> import ansible.parsing.yaml.loader
    >>> AnsibleLoader = ansible.parsing.yaml.loader.AnsibleLoader
    >>> stream = '''
    ... ---
    ... - hosts: test
    ...   vars:
    ...     http_port: 80
    ...     max_clients: 200
    ... '''
    >>> loader = AnsibleLoader(stream)
    >>> data = loader.get_single_data()
    >>> type(data) == list
    True
    >>> data[0]['hosts']
    'test'
    >>> type(data[0]['vars']) == dict
    True
    """


# Generated at 2022-06-13 07:42:08.485887
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    txt = '''
        ---
        foo: bar
        baz:
          - 1
          - 2
          - 3
        ...
    '''

    loader = AnsibleLoader(txt)
    data = loader.get_single_data()

    assert data == dict(foo='bar',
                        baz=[1, 2, 3])

    txt = '''
        ---
        foo: bar
        baz:
          - 1
          -
            a: 1
            b: 2
          - 3
        ...
    '''
    loader = AnsibleLoader(txt)
    data = loader.get_single_data()


# Generated at 2022-06-13 07:42:10.003639
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = list(Parser, Scanner, Composer, AnsibleConstructor, Resolver)
    assert AnsibleLoader(stream).__class__.__name__ == 'AnsibleLoader'

# Generated at 2022-06-13 07:42:11.547246
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert(True)

# Generated at 2022-06-13 07:42:12.348583
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader(None, None)

# Generated at 2022-06-13 07:42:13.253820
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader('')

# Generated at 2022-06-13 07:42:14.713208
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Just create an instance to get 100% coverage
    AnsibleLoader(None)



# Generated at 2022-06-13 07:42:19.922452
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    sys.modules['_yaml'] = sys.modules['yaml']
    from ansible.parsing.dataloader import DataLoader
    ldr = DataLoader()
    res = ldr.load_from_file('../../../test/support/yaml/constructor.yml')
    assert res['map']['key2']['key2.1'][0] == 1
    assert res['map']['key2']['key2.1'][1] == 2
    assert res['map']['key2']['key2.1'][2] == 3


# Generated at 2022-06-13 07:42:36.793507
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # yaml.load() requires an io.TextIOBase object as param.
    # io.StringIO() is used to create a io.TextIOBase object from a string
    from io import StringIO
    from ansible.module_utils.common import AnsibleModule

    class FakeModuleMock(object):
        def __init__(self):
            self.params = dict()

        def fail_json(self, *args, **kwargs):
            raise Exception("Failed!")

    def test_top_level_tags():
        stream = StringIO("!top_level_tag{with_param: a_value}\n")
        loader = AnsibleLoader(stream)
        top_level_tag = loader.get_single_data()
        assert(top_level_tag["with_param"] == "a_value")


# Generated at 2022-06-13 07:42:38.193934
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader



# Generated at 2022-06-13 07:42:38.989426
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:42:49.540903
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml = """
        - name: test1
          description: test2
          site: valu3
          modules:
            - name: module1
              description: module2
              site: module3
    """
    loader = AnsibleLoader(yaml)
    data = loader.get_data()

    assert data is not None
    assert len(data) == 1
    assert data[0]['name'] == 'test1'
    assert data[0]['description'] == 'test2'
    assert data[0]['site'] == 'valu3'

    assert data[0]['modules'] is not None
    assert len(data[0]['modules']) == 1
    assert data[0]['modules'][0]['name'] == 'module1'
    assert data[0]['modules'][0]['description']

# Generated at 2022-06-13 07:42:54.956810
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.constructor import ConstructorError

    try:
        AnsibleLoader(None)
    except TypeError:
        pass
    else:
        raise AssertionError("Failed to raise TypeError when stream is None")

    try:
        AnsibleLoader(b'').get_single_data()
    except ConstructorError:
        pass
    else:
        raise AssertionError("Failed to raise ConstructorError on empty input")

# Generated at 2022-06-13 07:43:02.777657
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, None)
    assert loader.file_name is None
    assert loader.vault_secrets is None
    loader = AnsibleLoader(None, "my_file_name")
    assert loader.file_name == "my_file_name"
    loader = AnsibleLoader(None, "my_file_name", ["secret1", "secret2"])
    assert loader.file_name == "my_file_name"


# Generated at 2022-06-13 07:43:11.237624
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence, AnsibleVaultEncryptedUnicode
    loader = AnsibleLoader('', file_name='test')

    assert isinstance(loader.construct_yaml_str('test'), AnsibleUnicode)
    assert isinstance(loader.construct_yaml_map({}), AnsibleMapping)
    assert isinstance(loader.construct_yaml_seq([]), AnsibleSequence)

# Generated at 2022-06-13 07:43:24.994747
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_data = '''
    ---
    # This is a valid YAML document
    data1:
        - item1
        - item2
        - item3
    data2:
        key1: value1
        key2: value2
        key3: value3
    '''

    l = AnsibleLoader(test_data, file_name='test_loader.yml')

    # See https://pyyaml.org/wiki/PyYAMLDocumentation for details on what this
    # should return
    assert l.get_single_data() == dict(data1=['item1', 'item2', 'item3'], data2=dict(key1='value1', key2='value2', key3='value3'))

# Generated at 2022-06-13 07:43:25.702118
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert True

# Generated at 2022-06-13 07:43:26.376107
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader

# Generated at 2022-06-13 07:43:43.867554
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader()

# Generated at 2022-06-13 07:43:48.489551
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """This is a fake test to make pytest work with AnsibleLoader class """
    my_loader = AnsibleLoader(stream="/path/to/ansible/project", file_name=None, vault_secrets=None)
    assert my_loader is not None

# Generated at 2022-06-13 07:43:53.965959
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (3,):
        from io import StringIO
    else:
        from StringIO import StringIO
    stream = StringIO(u"---\nmessage: hello world")
    loader = AnsibleLoader(stream)
    d = loader.get_single_data()
    assert d['message'] == "hello world"

# Generated at 2022-06-13 07:44:00.940589
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import yaml
    from ansible.vars.unsafe_proxy import wrap_var

    def test_vault_yaml(loader, node):
        value = loader.construct_sequence(node)
        return wrap_var(value)

    yaml.add_constructor('!vault', test_vault_yaml)
    # Test !vault

# Generated at 2022-06-13 07:44:02.434408
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert 'AnsibleLoader' in globals()


# Generated at 2022-06-13 07:44:11.051310
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import sys

    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO

    # test a list
    data = StringIO("---\n- one\n- two\n- three\n")
    loader = AnsibleLoader(data)
    assert loader.get_single_data() == ['one', 'two', 'three']

    # test a dictionary
    data = StringIO("---\none: two\nthree: four")
    loader = AnsibleLoader(data)
    assert loader.get_single_data() == {'one': 'two', 'three': 'four'}

    # test an embedded dictionary
    data = StringIO("---\n- one\n- two\n- three: four\n- five: six")
    loader

# Generated at 2022-06-13 07:44:12.619103
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.parsing.yaml.loader as loader
    loader.AnsibleLoader(None)

# Generated at 2022-06-13 07:44:20.981304
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:44:26.610168
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    Testing the constructor for AnsibleLoader.  This is mainly for the
    epydoc class documentation.
    """

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    assert hasattr(AnsibleLoader, '__init__')
    assert hasattr(AnsibleLoader, 'construct_yaml_map')
    assert hasattr(AnsibleLoader, 'construct_yaml_seq')
    assert hasattr(AnsibleLoader, 'construct_mapping')
    assert hasattr(AnsibleLoader, 'construct_pairs')
    assert hasattr(AnsibleLoader, 'construct_object')
    assert hasattr(AnsibleLoader, 'construct_scalar')
    assert hasattr(AnsibleLoader, 'primitive_constructor')
    assert AnsibleLoader.y

# Generated at 2022-06-13 07:44:33.378378
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # FIXME: Once we drop Python 2 support, use `nonlocal` here.
    global_result = None
    class MyLoader(AnsibleLoader):
        def compose_node(self, parent, index):
            global global_result
            global_result = parent, index

    data = '''
        ---
        "test": test
    '''

    loader = MyLoader(data.encode('utf-8'))
    loader.get_single_data()
    assert global_result == (None, None)

# Generated at 2022-06-13 07:45:08.916043
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:45:10.434735
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader('')
    assert loader.file_name is None


# Generated at 2022-06-13 07:45:23.494116
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 07:45:26.250673
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = []
    loader = AnsibleLoader(stream)
    assert loader.file_name is None
    assert loader.vault_secrets is None

# Generated at 2022-06-13 07:45:37.367525
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    data = '''{
    "foo": [ "bar", "baz" ],
    "bam": { "baz": "bam" },
    "biz": "baz"
}
'''

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.loader import AnsibleLoader
    from yaml.constructor import ConstructorError

    dataobj = AnsibleLoader(data, file_name='<string>').get_single_data()

    assert isinstance(dataobj, dict)
    assert isinstance(dataobj, ImmutableDict)

    try:
        dataobj['bam'] = 'foo'
        assert False, 'should have thrown exception'
    except TypeError:
        pass


# Generated at 2022-06-13 07:45:39.392069
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Ensure class AnsibleLoader is instantiable
    '''
    AnsibleLoader(None)

# Generated at 2022-06-13 07:45:48.413590
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import load, dump
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    stream = u"vault_test: !vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          30326336646637333935616163613164373565383565343737316535633537396534656637303566\n          6233650a303362613731393131623462653561666332313636353933316632363361326132306538\n          633631623233370a3866643138653639343133353863663664313637333430633834356631343561\n          6432666262356133\n"


# Generated at 2022-06-13 07:45:50.564732
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, file_name=None, vault_secrets=None)
    assert loader is not None

# Generated at 2022-06-13 07:45:52.911859
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test object creation with success
    try:
        AnsibleLoader(stream=None)
    except:
        raise AssertionError('Constructor of AnsibleLoader raised an exception')

# Generated at 2022-06-13 07:46:00.387084
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    def test_contructor_arg(mocker, arg):
        # The purpose of the following test is to ensure that the constructor of
        # AnsibleConstructor is called with the correct arguments.

        # Create an instance of AnsibleConstructor.
        constructor = AnsibleConstructor()

        # The following patch ensures that the constructor of AnsibleConstructor
        # is called with the correct arguments.
        mocker.patch.object(AnsibleConstructor, '__init__', return_value=None)
        AnsibleConstructor(arg)
        AnsibleConstructor.__init__.assert_called_once_with(constructor, arg)


# Generated at 2022-06-13 07:47:16.274068
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = b'{test: yes, value: 42}'
    loader = AnsibleLoader(data)
    doc = loader.get_single_data()
    assert doc == {'test': 'yes', 'value': '42'}


# Generated at 2022-06-13 07:47:17.697611
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert HAS_LIBYAML

# Generated at 2022-06-13 07:47:19.890325
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader([], [])

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:47:25.611228
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping
    data = {'a': {'b': '1'}, 'c': ['2',{'d': '3'}]}
    yaml_data_stream = AnsibleLoader(data, file_name='memory://')
    data = yaml_data_stream.get_single_data()
    assert isinstance(data, AnsibleMapping)
    assert data.a.b == '1'
    assert data.c[0] == '2'
    assert data.c[1].d == '3'

# Generated at 2022-06-13 07:47:29.588986
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    x = AnsibleLoader("my_yaml_string", "my_file_name", ["my_secret"])
    assert x.file_name == "my_file_name"
    assert AnsibleConstructor.vault_secrets == ["my_secret"]

# Generated at 2022-06-13 07:47:37.016767
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # AnsibleLoader class is abstract and cannot be directly instantiated
    # This test will fail when a new AnsibleLoader implementation is
    # introduced in the future

    # Create an instance of the class AnsibleLoader
    loader = AnsibleLoader(None, "/path/to/yaml")

    # Check if the file_name variable is set properly
    assert loader.file_name == "/path/to/yaml"

    # Check if the vault_secrets variable is set properly
    assert loader.vault_secrets == None

# Generated at 2022-06-13 07:47:38.984769
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # test_AnsibleLoader_constructor_libyaml()
    loader = AnsibleLoader('')
    assert loader.__class__.__name__ == 'AnsibleLoader'
    assert loader.__doc__ == 'AnsibleLoader(stream, file_name=None, vault_secrets=None)'

# Generated at 2022-06-13 07:47:42.730114
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=protected-access
    assert AnsibleLoader._construct_yaml_map is AnsibleConstructor._construct_yaml_map
    assert AnsibleLoader._construct_mapping is AnsibleConstructor._construct_mapping

# Generated at 2022-06-13 07:47:45.849267
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    text = """
        ---
        "{{ 'hello' }}": world
    """
    loader = AnsibleLoader(text)
    assert loader.get_single_data() == {'hello': 'world'}

# Generated at 2022-06-13 07:47:53.890163
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from io import StringIO

    data = u'''
    - 1
    - 2
    - 3
    '''
    stream = StringIO(data)
    loader = AnsibleLoader(stream, file_name='')

    assert([1,2,3] == loader.get_single_data())

    data = u'''
    ---
    - 1
    - 2
    - 3
    '''.strip()
    stream = StringIO(data)
    loader = AnsibleLoader(stream, file_name='')

    assert({} == loader.get_single_data())