

# Generated at 2022-06-13 07:38:35.718428
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # From a yaml string
    loader = AnsibleLoader('[ 1, 2, 3]')
    assert loader.get_single_data() == [1, 2, 3]
    loader = AnsibleLoader('- 1\n- 2\n- 3')
    assert loader.get_single_data() == [1, 2, 3]
    loader = AnsibleLoader('- 1\n- 2\n- 3')
    assert loader.get_single_data() == [1, 2, 3]
    loader = AnsibleLoader('- 1\n- [foo, bar]\n- 3')
    assert loader.get_single_data() == [1, ['foo', 'bar'], 3]
    loader = AnsibleLoader('- 1\n- foo: bar\n  baz: quux\n- 3')

# Generated at 2022-06-13 07:38:44.831981
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleUnicode, AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml import TLSerializer

    tl = TLSerializer()

    with open('tests/yamltests/basic.yaml') as f:
        s = f.read()
        data = AnsibleLoader(s).get_single_data()
        assert [1, 2, 3] == data
        data = tl.serialize(data)
        assert s.rstrip('\n') == data.rstrip('\n')

        data = AnsibleLoader(s).get_single_data()
        assert [1, 2, 3] == data
        data = tl.serialize(data)

# Generated at 2022-06-13 07:38:54.371473
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    """
    :rtype: object
    """
    check = AnsibleLoader(None)

# Generated at 2022-06-13 07:38:56.185978
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader([])
    assert loader is not None
    assert loader.__class__.__name__ == 'AnsibleLoader'

# Generated at 2022-06-13 07:39:07.187630
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.module_utils.common.yaml import Parser, HAS_LIBYAML
    if HAS_LIBYAML:
        from ansible.parsing.yaml.loader import AnsibleLoader
        AnsibleLoader(stream='', file_name='', vault_secrets='')
    else:
        from yaml.reader import Reader
        from yaml.scanner import Scanner
        from yaml.parser import Parser
        from yaml.composer import Composer
        from yaml.resolver import Resolver
        AnsibleLoader(stream='', file_name='', vault_secrets='')

# Generated at 2022-06-13 07:39:20.927366
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Note: this unit test should be expanded for each type of class
    #       that AnsibleLoader can construct.

    # list of class types that we can construct from a dict
    dict_types = [
        'timedelta',
        'datetime',
    ]
    yaml_loader = AnsibleLoader(file_name='myf')
    # list of class types that we can construct from a string
    str_types = [
        'md5',
    ]
    for type_name in dict_types:
        from datetime import datetime, timedelta
        import hashlib
        if type_name == 'timedelta':
            class_name = timedelta

# Generated at 2022-06-13 07:39:29.137262
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # test passing vault text to the AnsibleLoader
    try:
        from ansible.parsing.vault import VaultLib
    except ImportError:
        pass
    else:
        vault_secret = VaultLib()

# Generated at 2022-06-13 07:39:39.758808
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.data import AnsibleVaultEncryptedUnicode

    data = """
foo: [1,2,3]
bar: {x: 1, y: 2}
baz: !!ansible_vault_foo foo
"""
    loader = AnsibleLoader(data)
    d = loader.get_single_data()
    asser

# Generated at 2022-06-13 07:39:43.724982
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

if __name__ == '__main__':
    from ansible.module_utils.common._collections_compat import Mapping
    ansible_loader = AnsibleLoader("foo: bar")
    assert isinstance(ansible_loader.get_single_data(), Mapping)

# Generated at 2022-06-13 07:39:47.012337
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    string = """
        foo: bar
        baz:
          - 1
          - 2
          - 3
    """

    data = AnsibleLoader(string).get_single_data()
    assert data['baz'] == [1, 2, 3]



# Generated at 2022-06-13 07:40:00.792548
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnsafeText, AnsibleSequence, AnsibleMapping
    from .vault import VaultLib
    from .yaml_loader import yaml_loader
    import os

    # secret data
    secret = b'\x08\x93\xe8\xde\xbd\xa1\x03\x08\xba\xf2\x02\x9e\x97\x8f\x15\x1a\x03\xd8\xba\x2c\xa0\x6d\x6a\x1e\x7d\xc1\x87\xca\xf5\x7e\x2f'

    # init AnsibleLoader

# Generated at 2022-06-13 07:40:05.385256
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Create a new AnsibleLoader instance
    loader = AnsibleLoader(stream=None)

    # Verify that the three exported methods are found
    assert hasattr(loader, 'get_single_data')
    assert hasattr(loader, 'get_many_data')
    assert hasattr(loader, 'add_multi_mapping')

# Generated at 2022-06-13 07:40:06.791356
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    AnsibleLoader(stream=None)

# Generated at 2022-06-13 07:40:15.640930
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def _assert(incoming_data, expected_data):
        assert AnsibleLoader(incoming_data).get_single_data() == expected_data

    # Valid JSON data
    _assert(u'[1, 2]', [1, 2])
    _assert(u'{"foo": 1}', {u'foo': 1})

    # Invalid JSON data
    _assert(u'[1, 2', [1, 2])
    _assert(u'{"foo": 1', {u'foo': 1})

    # Various mappings
    _assert(u'{}', {})
    _assert(u'{"foo": "bar"}', {u'foo': u'bar'})
    _assert(u'{"foo": ["bar", "baz"]}', {u'foo': [u'bar', u'baz']})

# Generated at 2022-06-13 07:40:22.193811
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    import yaml
    from io import StringIO

    def test(s, v, exp_res):
        loader = AnsibleLoader(StringIO(s), vault_secrets=[v])
        res = list(loader.get_single_data())
        assert res == exp_res

    # Test VaultSecret
    test("vault |1234\nfoo: bar\n", VaultSecret("1234"), [{'foo': 'bar'}])

    # Test VaultLib
    vault = VaultLib("1234")

# Generated at 2022-06-13 07:40:33.313505
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultAES256EncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMap

    text = "!"
    loader = AnsibleLoader(text)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleUnsafeText)

    text = "!some_object"
    loader = AnsibleLoader(text)
    data = loader.get_single_data()
    assert isinstance(data, AnsibleUnsafeText)


# Generated at 2022-06-13 07:40:35.258497
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None, None)
    assert loader
# vim: set expandtab ts=4 sw=4:

# Generated at 2022-06-13 07:40:36.663231
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader is not None

# Generated at 2022-06-13 07:40:45.921799
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    #first make sure the class is instanciable, then move on to testing
    loader = AnsibleLoader(None)
    assert hasattr(loader, 'construct_yaml_str'), 'AnsibleLoader does not contain construct_yaml_str()'
    assert hasattr(loader, 'construct_yaml_int'), 'AnsibleLoader does not contain construct_yaml_int()'
    assert hasattr(loader, 'construct_yaml_float'), 'AnsibleLoader does not contain construct_yaml_float()'
    assert hasattr(loader, 'construct_yaml_seq'), 'AnsibleLoader does not contain construct_yaml_seq()'
    assert hasattr(loader, 'construct_yaml_map'), 'AnsibleLoader does not contain construct_yaml_map()'

# Generated at 2022-06-13 07:40:57.201685
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.errors import AnsibleParserError
    from ansible.vars.unsafe_proxy import wrap_var

    class FakeLoader(object):
        def __init__(self, file_name):
            self.file_name = file_name

    # test with vault_secrets
    loader = FakeLoader('dummy_file')
    ac = AnsibleConstructor(loader=loader, vault_secrets='secrets')
    data = ac.construct_yaml_map(node=None)
    assert isinstance(data, dict)

    # test without vault_secrets
    loader = FakeLoader('dummy_file')

# Generated at 2022-06-13 07:41:03.495417
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:41:16.723907
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:41:28.961434
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    loader = dl.load_from_file("../files/ansible_alias.yaml")
    assert loader.get_single_data() == {u'key': u'value'}
    loader = dl.load_from_file("../files/ansible_builtin.yaml")
    assert loader.get_single_data() == {u'key': u'value'}
    loader = dl.load_from_file("../files/ansible_datetime.yaml")
    assert loader.get_single_data() == {u'key': u'value'}
    loader = dl.load_from_file("../files/ansible_int.yaml")
    assert loader.get_single_data()

# Generated at 2022-06-13 07:41:37.715460
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    class Foo:
        x = 4

    from yaml import dump, load, MappingNode
    from ansible.parsing.yaml.constructor import from_yaml
    #from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    data = dict(
        an_int=5,
        a_float=3.15,
        binary_data=b'\x00\xfF',
        foo=Foo(),
    )

    my_dumper = AnsibleDumper()
    data_dump = dump(data, Dumper=my_dumper)
    print(data_dump)

# Generated at 2022-06-13 07:41:44.715438
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from collections import namedtuple
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from io import StringIO

    # Fake environment
    DummyEnv = namedtuple('Env', ['vault_secret', 'vault_password_file'])
    FakeEnv = DummyEnv(None, None)

    # Fake secret
    vault_secret = VaultLib('secret')
    vault_secret.load_secret('secret')

    # Test constructor

# Generated at 2022-06-13 07:41:46.779541
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ansible_loader = AnsibleLoader(None)
    assert type(ansible_loader) is AnsibleLoader

# Generated at 2022-06-13 07:41:48.832644
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO
    data = StringIO.StringIO("---\n- test data\n...")
    loader = AnsibleLoader(data)
    assert loader.construct_yaml_map() == "- test data"

# Generated at 2022-06-13 07:41:56.855241
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import ansible.constants
    import ansible.vars.manager
    import ansible.parsing.yaml.objects
    import ansible.utils.unsafe_proxy

    ansible.constants.DEFAULT_INVENTORY = 'inventory'
    ansible.constants.DEFAULT_VAULT_IDENTITY_LIST = ['vault_identity']
    ansible.vars.manager.VaultLib = 'vault_lib'
    ansible.parsing.yaml.objects.AnsibleBaseYAMLObject = 'AnsibleBaseYAMLObject'
    ansible.utils.unsafe_proxy.AnsibleUnsafeText = 'AnsibleUnsafeText'

    ans = AnsibleLoader('stream')

    assert ans.stream == 'stream'

# Generated at 2022-06-13 07:42:05.914421
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Basic test for Ansible constructor
    import sys, os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from ansible.parsing.yaml.loader import AnsibleLoader

    test_data = """
    a: b
    c: b
    d: b
    e: b
    f: b
    g: b
    """

    test_data_result = {
        'a': 'b',
        'c': 'b',
        'd': 'b',
        'e': 'b',
        'f': 'b',
        'g': 'b',
    }


# Generated at 2022-06-13 07:42:08.573569
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    yaml_str = """
    - hosts: localhost
      connection: local
      tasks:
      - name: AnsibleLoader unit test
        ping:
    """

    data = yaml.load(yaml_str, Loader=AnsibleLoader)
    assert data is not None

# Generated at 2022-06-13 07:42:22.842249
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():  # pylint: disable=too-many-locals
    import io
    with io.BytesIO(b'{"foo":"bar"}') as f:
        loader = AnsibleLoader(f)
        data = loader.get_single_data()
        assert data == {u'foo': u'bar'}

# Generated at 2022-06-13 07:42:37.985363
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.module_utils.common.yaml import Parser
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from yaml.parser import Parser as yParser
    from yaml.composer import Composer
    from yaml.resolver import Resolver

    if HAS_LIBYAML:
        assert issubclass(AnsibleLoader, Parser)
    else:
        assert issubclass(AnsibleLoader, Reader)
        assert issubclass(AnsibleLoader, Scanner)
        assert issubclass(AnsibleLoader, yParser)
        assert issubclass(AnsibleLoader, Composer)

    assert issubclass(AnsibleLoader, AnsibleConstructor)
   

# Generated at 2022-06-13 07:42:42.842751
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from io import StringIO
    from yaml import dump
    stream = StringIO(u'{z: !zap {a: 1, b: 2}}')
    loader = AnsibleLoader(stream)
    assert isinstance(loader.get_single_data(), AnsibleMapping)
    assert isinstance(loader.get_single_data()[u'z'], AnsibleMapping)
    assert loader.get_single_data()[u'z'][u'a'] == 1
    assert loader.get_single_data()[u'z'][u'b'] == 2

# Generated at 2022-06-13 07:42:53.786510
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.vars.unsafe_proxy import wrap_var


# Generated at 2022-06-13 07:42:54.779715
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    print(AnsibleLoader)

# Generated at 2022-06-13 07:43:06.727203
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os,sys
    import yaml
    from ansible.module_utils.common.yaml import HAS_LIBYAML

    #####################
    # HAS_LIBYAML = False
    #
    # def init(self, stream, file_name=None, vault_secrets=None):
    #     yaml.Reader.__init__(self, stream)
    #     yaml.Scanner.__init__(self)
    #     yaml.Parser.__init__(self)
    #     yaml.Composer.__init__(self)
    #     AnsibleConstructor.__init__(self, file_name=file_name, vault_secrets=vault_secrets)
    #     yaml.Resolver.__init__(self)
    #
    #####################
    #

# Generated at 2022-06-13 07:43:17.458682
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' Unit test for constructor of class AnsibleLoader'''
    from ansible.module_utils.common.yaml import load
    from ansible.module_utils._text import to_unicode
    from ansible.module_utils.common.collections import is_sequence

    vault_secrets = {'my_vault_secret': 'my_vault_secret_value'}
    file_name = './tests/test_data/test_constructor.yml'
    file_name = to_unicode(file_name)

    with open(file_name, 'r') as f:
        data = load(f, Loader=AnsibleLoader, vault_secrets=vault_secrets, file_name=file_name)

    assert data['var1'] == 'var1'

# Generated at 2022-06-13 07:43:19.727029
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream=None, file_name=None, vault_secrets=None)

    # test __init__ method
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Parser)

# Generated at 2022-06-13 07:43:22.263263
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream='a')
    assert loader.stream == 'a'
    assert loader.file_name is None
    loader = AnsibleLoader(stream='b', file_name='c')
    assert loader.stream == 'b'
    assert loader.file_name == 'c'

# Generated at 2022-06-13 07:43:26.374772
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    d = "---\n" + "foo: !file { filename: /etc/hosts }\n"
    data = AnsibleLoader(d, file_name='/foo').get_single_data()
    assert data['foo'].filename == '/etc/hosts'

# Generated at 2022-06-13 07:43:49.204738
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
     AnsibleLoader

if __name__ == "__main__":
    test_AnsibleLoader()

# Generated at 2022-06-13 07:43:50.627283
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader



# Generated at 2022-06-13 07:43:58.661038
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (3,):
        import io
        stream = io.StringIO()
    else:
        import StringIO
        stream = StringIO.StringIO()

    loader = AnsibleLoader(stream)
    assert loader.stream == stream, 'Failed to initialize stream in AnsibleLoader'
    assert loader.file_name is None, 'Failed to initialize file_name in AnsibleLoader'
    assert loader.vault_secrets is None, 'Failed to initialize vault_secrets in AnsibleLoader'
    assert loader.document is None, 'Failed to initialize document in AnsibleLoader'
    assert loader.documents is None, 'Failed to initialize documents in AnsibleLoader'

# Generated at 2022-06-13 07:43:59.317337
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:44:07.691572
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    import io

    example = """
    - hosts: all
      gather_facts: no
    """

    stream = io.StringIO(example)
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()

    assert isinstance(data, list)
    assert len(data) == 1

    play = data[0]
    assert isinstance(play, AnsibleMapping)
    assert play['hosts'] == 'all'
    assert play['gather_facts'] == 'no'

# Generated at 2022-06-13 07:44:08.765805
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)

# Generated at 2022-06-13 07:44:18.156211
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleUnicode

    s = u"""
    unicode_str: hello
        look:
            - a: down
            - b: up
    """

    def verify_instance(result):
        assert isinstance(result, AnsibleMapping)
        assert isinstance(result['unicode_str'], AnsibleUnicode)
        assert isinstance(result['look'], AnsibleSequence)
        assert result['unicode_str'] == u'hello'

        verify_instance(result['look'][0])

# Generated at 2022-06-13 07:44:24.880747
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
- name: install nginx
  yum: pkg=nginx state=latest
- name: start nginx
  service: name=nginx enabled=yes
'''
    loader = AnsibleLoader(stream)
    assert type(loader.get_single_data()) == list
    assert type(loader.get_single_data()[0]) == dict
    assert type(loader.get_single_data()[1]) == dict
    assert loader.get_single_data()[0]['name'] == 'install nginx'
    assert loader.get_single_data()[0]['yum']['pkg'] == 'nginx'
    assert loader.get_single_data()[0]['yum']['state'] == 'latest'

# Generated at 2022-06-13 07:44:35.840961
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import __builtin__
    if not hasattr(__builtin__, 'open'):
        from ansible.compat.six import builtins
        setattr(builtins, 'open', open)
    import datetime
    import yaml

    class Obj(object):
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    class MyYamlObject(AnsibleBaseYAMLObject):
        yaml_loader = AnsibleLoader
        yaml_tag = u'!myyamlobject'

    class MyYamlObjectWithConstructor(AnsibleBaseYAMLObject):
        yaml_loader = AnsibleLoader

# Generated at 2022-06-13 07:44:41.262122
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = '''
        ---
        - hosts: localhost
          gather_facts: false
          tasks:
            - name: value
              debug: msg="This is a test"
    '''

    loader = AnsibleLoader(yaml_str, file_name=None, vault_secrets=None)

    for item in loader:
        print(item)


# Generated at 2022-06-13 07:45:25.564170
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("hello, world")
    assert loader is not None

# Generated at 2022-06-13 07:45:26.214187
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:45:28.741480
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.constructor import AnsibleLoader
    # FIXME: Requires import from unittest
    #assert AnsibleLoader, AnsibleConstructor
    return None

# Generated at 2022-06-13 07:45:34.464045
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert hasattr(loader, 'construct_yaml_map')
    assert hasattr(loader, 'construct_yaml_str')
    assert hasattr(loader, 'vault_secrets')
    assert hasattr(loader, 'vault_secrets_filename')
    assert hasattr(loader, 'vault_secrets_file')

# Generated at 2022-06-13 07:45:40.126358
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (3, 0):
        assert b'foo' == AnsibleLoader('foo').get_single_data()
    else:
        assert 'foo' == AnsibleLoader('foo').get_single_data()
    assert [1, 2, 3] == AnsibleLoader('- 1\n- 2\n- 3').get_single_data()


# Generated at 2022-06-13 07:45:43.805378
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = """
a: 1
b: 2
"""

    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data is not None
    assert data.get('a') == 1
    assert data.get('b') == 2

# Generated at 2022-06-13 07:45:49.006403
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
    invalid:
        - string
        - 1
        - {k: 2}
        - [a, b, c]
    '''
    loader = AnsibleLoader(data)
    loader.get_single_data()

    data = '''
    invalid:
        - string
        - 1
        - {k: 2}
        - [a, b, c]
    '''
    loader = AnsibleLoader(data)
    loader.get_single_data()

# Generated at 2022-06-13 07:45:51.105397
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' Unit test for constructor of class AnsibleLoader '''
    assert AnsibleLoader(stream=None)

# Generated at 2022-06-13 07:45:51.664924
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader('')

# Generated at 2022-06-13 07:45:56.194813
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Create AnsibleLoader
    loader = AnsibleLoader("")

    # Create fake data
    data = dict(
        ansible_variable=dict(
            key1="value1",
            key2="value2",
            key3="value3",
        )
    )

    # Assert that the data is loaded correctly
    assert loader.construct_mapping(node=None, deep=True) == data



# Generated at 2022-06-13 07:47:30.584799
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """
    AnsibleLoader Constructor will call the three parent constructors of
    this class, so effectively what we are testing here is that calling
    AnsibleLoader doesn't cause any errors
    """
    import StringIO
    # This file has been created with Ansible
    # It has no CRLF line terminators
    ansible_yml = StringIO.StringIO("""
        - name: Test the Ansible loader
          hosts: localhost
          connection: local
          tasks:
            - name: Test that AnsibleLoader doesn't blow up
              command: /bin/true
          vars:
            test_var: "Testing the vars section"
    """)
    loader = AnsibleLoader(ansible_yml)
    yaml_data = loader.get_single_data()
    assert yaml_data is not None

# Generated at 2022-06-13 07:47:38.400576
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = '''
    --- # This is a comment and not metadata
    hosts:
     - server
     - client
    vars:
     key: value
    tasks:
    - name: task1
      action: action1
    ...
    '''

    loader = AnsibleLoader(stream)
    assert loader.get_single_data() == {'hosts': ['server', 'client'], 'vars': {'key': 'value'}, 'tasks': [{'name': 'task1', 'action': 'action1'}]}

# Generated at 2022-06-13 07:47:49.069789
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from yaml.resolver import Resolver
    from yaml.composer import Composer
    from yaml.reader import Reader
    from yaml.scanner import Scanner
    from yaml.parser import Parser
    from ansible.parsing.yaml.loader import AnsibleLoader
    stream = StringIO.StringIO("---")
    reader = Reader(stream)
    scanner = Scanner(reader)
    parser = Parser(scanner)
    composer = Composer(parser)
    constructor = AnsibleConstructor()
    resolver = Resolver()
    loader = AnsibleLoader(stream)
    assert isinstance(loader, Parser)
    assert isinstance(loader, Reader)

# Generated at 2022-06-13 07:47:59.613613
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml.composer import Composer
    from yaml.scanner import Scanner
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    class AnsibleLoader_test(Scanner, Composer, AnsibleConstructor):
        def __init__(self, stream, file_name=None, vault_secrets=None):
            Scanner.__init__(self, stream)
            Composer.__init__(self)
            AnsibleConstructor.__init__(self, file_name=file_name, vault_secrets=vault_secrets)
    assert issubclass(AnsibleLoader_test, Scanner)
    assert issubclass(AnsibleLoader_test, Composer)
    assert issubclass(AnsibleLoader_test, AnsibleConstructor)

# Generated at 2022-06-13 07:48:04.725104
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    class AnsibleLoader:
        __init__(self, stream):
    '''
    # Do nothing for now
    _ = AnsibleLoader(None)

if __name__ == '__main__':
    # Unit test
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-13 07:48:13.847671
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # instantiate a loader
    loader = AnsibleLoader('')
    # check type of the ansible constructor
    assert isinstance(loader, AnsibleConstructor)
    # check the scalar string values
    for scalar in [
            None,
            123,
            'foo',
            'bar',
            '10',
            '10.5',
            '10.5.6',
            '0x10.5.6',
            '123.text',
            '123text',
            'text123',
            '123.text123',
            '.123'
    ]:
        # check the scalar string value
        assert(loader.construct_scalar(scalar) == scalar)

# Generated at 2022-06-13 07:48:16.186725
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = 'mystream'
    file_name = 'myfile'
    vault_secrets = 'vaultsecret'

    AnsibleLoader(stream, file_name, vault_secrets)

# Generated at 2022-06-13 07:48:29.268687
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_text = """
---
- hosts:
    - database
  sudo: true
  tasks:
    - name: install python2.7
      yum:
         name: python27
         state: latest
    - name: install Python MySQL client
      yum:
         name: MySQL-python
         state: latest
"""
    loader = AnsibleLoader(yaml_text)
