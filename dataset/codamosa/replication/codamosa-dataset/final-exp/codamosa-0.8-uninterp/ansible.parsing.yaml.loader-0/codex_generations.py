

# Generated at 2022-06-13 07:38:38.645042
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Construct AnsibleLoader object
    loader = AnsibleLoader(stream=None)

    # Check attributes of class AnsibleLoader

    assert hasattr(loader, 'file_name')
    assert hasattr(loader, 'stream')
    # On Ansible 2.8 file_vars is not present
    assert hasattr(loader, 'file_vars') or loader.__class__.__name__ == 'AnsibleLoader_2_8'
    assert hasattr(loader, 'vault_secrets')

# Generated at 2022-06-13 07:38:39.564193
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    return AnsibleLoader('test string')

# Generated at 2022-06-13 07:38:41.376038
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    # Class AnsibleLoader has attribute name
    assert hasattr(AnsibleLoader, 'name')

# Generated at 2022-06-13 07:38:45.442306
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    loader = AnsibleLoader(None)
    assert isinstance(loader.construct_yaml_str(None), AnsibleUnicode)
    loader = AnsibleLoader(None, file_name='filename')
    assert isinstance(loader.file_name, AnsibleUnicode)



# Generated at 2022-06-13 07:38:54.894868
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Generated at 2022-06-13 07:38:57.040953
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Ensure that AnsibleLoader returns the class hierarchy of its parent
    '''
    assert AnsibleLoader.__bases__ == (Parser, AnsibleConstructor, Resolver)

# Generated at 2022-06-13 07:39:00.182566
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    loader = AnsibleLoader(b'---\n- foo: bar')

    data = loader.get_single_data()
    assert isinstance(data[0]['foo'], AnsibleUnicode)
    assert data[0]['foo'] == u'bar'

# Generated at 2022-06-13 07:39:02.307458
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader
    assert AnsibleConstructor

# Generated at 2022-06-13 07:39:06.565851
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = 'foo: bar\n'
    stream += 'baz: 123\n'
    a = AnsibleLoader(stream)
    assert isinstance(a, AnsibleLoader)
    assert a.get_single_data() == {'foo': 'bar', 'baz': 123}

# Generated at 2022-06-13 07:39:20.461712
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

#   Load the yaml files
    path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                        '../../test/units/constructor/data/yaml_files/')

# Generated at 2022-06-13 07:39:22.921589
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:39:30.094654
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

# Generated at 2022-06-13 07:39:42.076780
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import random, string, sys

    # Create random name of file
    fileName = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    # Create random content of file
    fileContent = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))

    # Create random vault secret
    vaultSecret = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    # Create file
    with open(fileName, 'w') as file:
        file.write(fileContent)

    file_name, ext = os.path.splitext(file)

    # Use AnsibleLoader to load content of file in an object
    loader = AnsibleLoader(fileName)


# Generated at 2022-06-13 07:39:50.300913
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.module_utils.common.yaml import HAS_LIBYAML
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from yaml.resolver import Resolver

    expected_repr = "<AnsibleLoader repr() not implemented>"

    stream = "---"
    file_name = None
    vault_secrets = None
    loader = AnsibleLoader(stream, file_name=file_name, vault_secrets=vault_secrets)

    assert loader.stream == stream
    assert loader.file_name == file_name
    assert loader.vault_secrets == vault_secrets

    assert loader.__repr__() == expected_repr
    assert loader.__str__() == expected_repr

    assert isinstance(loader, Resolver)

# Generated at 2022-06-13 07:39:55.969089
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info >= (2, 7):
        from tests.support.unit.test_yaml_loader import TestYAMLLoader
        return TestYAMLLoader.check_yaml_class(AnsibleLoader, 'ansible')

if __name__ == "__main__":
    print(test_AnsibleLoader())

# Generated at 2022-06-13 07:40:00.881511
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    output = AnsibleLoader(b"---\n- hosts: localhost").get_single_data()
    assert output == {u'hosts': u'localhost'}
    assert isinstance(output['hosts'], AnsibleUnicode)



# Generated at 2022-06-13 07:40:11.840678
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=R0914
    import datetime
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    class TestVaultSecret(VaultSecret):
        def __init__(self, password, file_name=None, vault_id=None):
            super(TestVaultSecret, self).__init__(password, file_name, vault_id)
            self.password = password
            self.file_name = file_name
            self.vault_id = vault_id
        def __eq__(self, other):
            return self.__class__ == other.__class__ and self.__dict__ == other.__dict__

    # Test

# Generated at 2022-06-13 07:40:23.720384
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader(): # pylint: disable=too-many-locals
    import os
    import sys
    import tempfile
    import shutil
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.vault import VaultLib

    this_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(this_dir, 'loader_tests')


# Generated at 2022-06-13 07:40:31.554773
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None)  # type: ignore
    AnsibleLoader(None, file_name='foo')  # type: ignore
    AnsibleLoader(None, file_name='foo', vault_secrets=['foo'])  # type: ignore

    # The type of vault_secrets param is a list of strings
    AnsibleLoader(None, file_name='foo', vault_secrets=[[]])  # type: ignore  # pylint: disable=bad-continuation  # noqa

    # Pylint wrongly detects YAML as JSON, so we override its complains here
    AnsibleLoader(None, file_name='foo', vault_secrets=[{}])  # type: ignore  # pylint: disable=bad-continuation  # noqa

# Generated at 2022-06-13 07:40:36.811285
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from yaml import load
    import os

    dirname = os.path.dirname(__file__)
    module = os.path.normpath(os.path.join(dirname, '../../module_utils/facts/system/distribution.py'))
    with open(module, 'r') as stream:
        code = load(stream, AnsibleLoader)

# Generated at 2022-06-13 07:40:41.974218
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None

# Generated at 2022-06-13 07:40:47.608529
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    """ This is a test to confirm the constructor of AnsibleLoader works as expected """
    # If the user does not have libyaml, then the AnsibleLoader class should be just a normal Loader, not
    # a combination of all the other Loader classes.
    if HAS_LIBYAML:
        assert issubclass(AnsibleLoader, Parser)
    else:
        assert not issubclass(AnsibleLoader, Parser)
    assert issubclass(AnsibleLoader, AnsibleConstructor)
    assert issubclass(AnsibleLoader, Resolver)

# Generated at 2022-06-13 07:40:49.900973
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    test_stream = '''
    {% set test = "TEST" %}
    foo:
    - bar:
      - baz:
        - name: fail
        - {{ test }}
    '''
    loader = AnsibleLoader(test_stream)
    for i in loader:
        print(i)

# Generated at 2022-06-13 07:40:58.977777
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # pylint: disable=unused-variable
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements

    import os
    import tempfile
    import textwrap
    import shutil
    import json
    import pytest
    from tempfile import NamedTemporaryFile
    from collections import OrderedDict
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    from ansible.parsing.yaml.dumper import AnsibleDumper

    from ansible.parsing import vault

    if HAS_LIBYAML:
        yaml = pytest.importors

# Generated at 2022-06-13 07:41:04.146158
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert hasattr(AnsibleLoader, 'add_constructor')
    assert hasattr(AnsibleLoader, 'add_multi_constructor')

    loader = AnsibleLoader(b'ok: [localhost]')
    assert hasattr(loader, 'get_single_data')

# Generated at 2022-06-13 07:41:12.711694
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    '''
    Make sure AnsibleLoader is testing all its methods.
    '''
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib

    vault_secrets = [('default', VaultLib({}))]
    test_data = AnsibleBaseYAMLObject(test_data=AnsibleUnsafeText('blah', vault_secrets=vault_secrets))

    # base_data is an AnsibleBaseYAMLObject and is expected to be returned by
    # AnsibleConstructor.construct_yaml_map.
    base_data = {'test': test_data}

# Generated at 2022-06-13 07:41:23.218403
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    source = '''
        ---
        - hosts: all
          # a comment
          tasks:
          - name: test
            action: foo
            args:
              - biz=baz
          - name: Include a role
            include_role: "foo/bar"
          - include: "bar/foo"
    '''
    # '?', ':', '-', ',' and '[' are used to indicate keys
    # '&', '*', '#' and '!' are used to tag nodes
    source_with_tags = """
    ---
    - hosts: all
      tags: ['debug:var=app1']
      tasks:
      - name: test
        action: foo
        args:
          - biz=baz
    """
    # We don't need to test that it has the right

# Generated at 2022-06-13 07:41:24.507795
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


__all__ = ['AnsibleLoader']

# Generated at 2022-06-13 07:41:29.548637
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info[0] < 3:
        stream = u'{ foo: bar }'
    else:
        stream = '{ foo: bar }'
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    print(data)
    assert data == {'foo': 'bar'}

if __name__ == '__main__':
    test_AnsibleLoader()

# Generated at 2022-06-13 07:41:35.214498
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import StringIO
    yamlloader_string = StringIO.StringIO("""
    ---
    - !!python/object:__main__.MyClass
      foo: 1
      bar: 2
    """)
    yamlloader = AnsibleLoader(yamlloader_string)
    yamlloader.get_single_data()
    # print yamlloader.get_single_data()

# Generated at 2022-06-13 07:41:48.375752
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import sys
    if sys.version_info[0] > 2:
        from io import StringIO
    else:
        from StringIO import StringIO
    try:
        AnsibleLoader(StringIO('---'))
    except TypeError:
        assert False, "TypeError raised unexpectedly"
    else:
        assert True

# Generated at 2022-06-13 07:41:48.987374
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:41:52.074781
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    ldr = AnsibleLoader('---\nfoo: bar')
    assert ldr.get_single_data() == AnsibleUnicode('bar')

# Generated at 2022-06-13 07:42:00.916362
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Try loading a list and make sure ContentError is raised when there are
    # non-hash elements in the list
    stream = open('../../test/units/parsing/yaml/files/dict_only.yml')
    loader = AnsibleLoader(stream)

    try:
        loader.get_single_data()
        assert False, 'Expected exception but did not see one'  # pylint: disable=redundant-unittest-assert
    except Exception as e:  # pylint: disable=broad-except
        assert isinstance(e, Exception)
        assert e.__class__.__name__ == 'ContentError'


# Generated at 2022-06-13 07:42:08.342719
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    src = """- hosts: test-servers
      pre_tasks:
        - name: test play with vault
          action: command echo {{vault_test_password}}""".splitlines()

    import io
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    vault_secret = "secret"
    loader = AnsibleLoader(io.StringIO("\n".join(src)), vault_secrets=[
        ("vault_test_password", vault_secret)])
    data = loader.get_single_data()

    assert data["hosts"] == "test-servers"
    assert data["pre_tasks"][0]["name"] == "test play with vault"


# Generated at 2022-06-13 07:42:15.083280
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert isinstance(loader.add_constructor('!include', AnsibleConstructor.include), AnsibleConstructor.include)
    assert isinstance(loader.add_constructor('!include_vars', AnsibleConstructor.include_vars), AnsibleConstructor.include_vars)
    assert isinstance(loader.add_constructor('!vault', AnsibleConstructor.vault_secrets), AnsibleConstructor.vault_secrets)
    assert isinstance(loader.add_constructor('!template', AnsibleConstructor.template), AnsibleConstructor.template)

# Generated at 2022-06-13 07:42:18.258342
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Initialization of arguments
    stream = None
    file_name = None
    vault_secrets = None

    # Initialization of class AnsibleLoader
    obj = AnsibleLoader()


# Generated at 2022-06-13 07:42:26.380123
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import yaml
    from io import StringIO
    from ansible.parsing.yaml.loader import AnsibleLoader

# Generated at 2022-06-13 07:42:35.914145
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data1 = """
        - hosts: all
          vars:
            http_port: 80
            max_clients: 200
            var1:
              key1: value1
              key2: value2
          roles:
          - common
          - webservers
    """
    data2 = """
    - name: 'Playbook task test'
      hosts: all
      remote_user: root
      tasks:
      - name: 'Make a test file'
        tempfile:
          state: file
          dest: /tmp/testfile.txt
          mode: 0644
          is_tmp: yes
        register: testfile_output
      - name: 'Show results'
        debug:
          var: testfile_output
    """
    loader = AnsibleLoader(None)

# Generated at 2022-06-13 07:42:36.314040
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:43:01.166958
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    strings = [
        "---\n",
        "# comment\n",
        "hello: 1\n",
        "world: 2\n",
        "# another comment\n",
        "\n",
        "goodbye: 3\n",
    ]
    stream = io.StringIO("".join(strings))
    loader = AnsibleLoader(stream)
    data = loader.get_single_data()
    assert data
    assert data['world'] == 2
    assert data['goodbye'] == 3
    assert loader.compose_document()

# Generated at 2022-06-13 07:43:10.436174
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:43:11.371842
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader

# Generated at 2022-06-13 07:43:20.311314
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    yaml_str = """
        - hosts: localhost
          tasks:
            - name: write a message
              debug: msg="Hello, world!"
    """
    loader = AnsibleLoader(yaml_str)
    for data in loader:
        assert data
        assert 'playbook' not in data
        assert data['hosts'] == 'localhost'
        assert data['tasks'] == [{'name': 'write a message', 'debug': {'msg': 'Hello, world!'}}]

# Generated at 2022-06-13 07:43:21.135527
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    pass

# Generated at 2022-06-13 07:43:27.804313
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    file_name = "test_file_name"
    vault_secrets = "test_vault_secrets"
    al = AnsibleLoader(file_name=file_name, vault_secrets=vault_secrets)
    assert al.file_name == file_name
    assert al.vault_secrets == vault_secrets

# Generated at 2022-06-13 07:43:37.604114
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import io
    import unittest
    import sys

    class TestAnsibleLoader(unittest.TestCase):
        '''
        Covers the functionality of the AnsibleLoader class
        '''
        def __init__(self, *args, **kwargs):
            super(TestAnsibleLoader, self).__init__(*args, **kwargs)
            self.test_file = '''
            ---
            foo: {{ bar }}
            ...'''
            self.test_file_utf_8 = '''
            ---
            foo: ümlauts
            ...'''

        def test_ansible_loader_construction(self):
            '''
            Ensures that we can create an AnsibleLoader instance
            '''
            if sys.version_info[0] < 3:
                stream = io.Bytes

# Generated at 2022-06-13 07:43:39.179387
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import yaml
    AnsibleLoader(yaml.reader.Reader(''))  # Constructor should not raise exception

# Generated at 2022-06-13 07:43:42.923484
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # init
    loader = AnsibleLoader(None)

    # Asserts
    assert(loader.file_name is None)
    assert(loader.vault_secrets is None)

# Generated at 2022-06-13 07:43:48.303818
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():

    AnsibleLoader(file_name="test_AnsibleLoader")
    AnsibleLoader(vault_secrets="test_AnsibleLoader")
    AnsibleLoader(file_name="test_AnsibleLoader", vault_secrets="test_AnsibleLoader")

# Generated at 2022-06-13 07:44:24.583406
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    stream = "--- {}\n"
    loader = AnsibleLoader(stream)
    ansible_obj = loader.get_single_data()
    assert isinstance(ansible_obj, dict)

# Generated at 2022-06-13 07:44:25.480476
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(stream="test_stream")

# Generated at 2022-06-13 07:44:36.752676
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    def _test_AnsibleLoader1():
        contents = """
        - hosts: all
          gather_facts: False
        """
        data = AnsibleLoader(contents).get_single_data()
        assert data == {
            "hosts": "all",
            "gather_facts": False
        }, data

    def _test_AnsibleLoader2():
        contents = """
        - hosts: all
          gather_facts: False
        """
        data = AnsibleLoader(contents, file_name='foo.yml').get_single_data()
        assert data == {
            "hosts": "all",
            "gather_facts": False,
            "_ansible_file_name": 'foo.yml'
        }, data

    _test_AnsibleLoader1()
    _test_Ans

# Generated at 2022-06-13 07:44:43.419837
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    yaml_data = AnsibleUnicode(u'\u041b\u0438\u0441\u0442\u043e: \u043f\u0430\u0440\u043e\u043b\u044c')
    assert AnsibleLoader(yaml_data).get_single_data() == dict(
        Листо=u'пароль')

# Generated at 2022-06-13 07:44:44.628670
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Check if AnsibleLoader can be instantiated
    assert AnsibleLoader

# Generated at 2022-06-13 07:44:45.906497
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader


# Generated at 2022-06-13 07:44:46.815537
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    AnsibleLoader(None, None, None)

# Generated at 2022-06-13 07:44:48.470344
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader("foo")
    result = loader.get_single_data()
    assert result == "foo"

# Generated at 2022-06-13 07:44:51.469492
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    data = '''
---
foo bar
'''

    assert AnsibleLoader(data).get_single_data() == {'foo': 'bar'}

# Generated at 2022-06-13 07:45:01.146053
# Unit test for constructor of class AnsibleLoader

# Generated at 2022-06-13 07:46:20.772001
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # fail constructor
    try:
        a = AnsibleLoader()
    except:
        pass
    # error init function
    try:
        a = AnsibleLoader(1, 2, 3)
    except:
        pass

    # simple test
    stream = Parser.from_yaml_string('[1, 2, 3]')
    b = AnsibleLoader(stream)
    assert(b)


if __name__ == "__main__":
    import pytest
    pytest.main([os.path.join(os.path.dirname(__file__), "test_yaml.py")])

# Generated at 2022-06-13 07:46:21.633110
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    assert AnsibleLoader is not None



# Generated at 2022-06-13 07:46:23.199353
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # TODO
    # c = AnsibleLoader()
    pass

# Generated at 2022-06-13 07:46:33.524775
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    import os
    import tempfile
    import shutil
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedString

    tmpdir = tempfile.mkdtemp(dir=os.getcwd())
    filename = os.path.join(tmpdir, "test_AnsibleLoader.yml")

    # Write a test file

# Generated at 2022-06-13 07:46:37.329220
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from StringIO import StringIO
    stream = StringIO(u'\n'.join([u'---',
                                  u'foo:',
                                  u'  bar: 1',
                                  u'  baz: 2']))
    loader = AnsibleLoader(stream)
    loader.get_single_data()

# Generated at 2022-06-13 07:46:39.766881
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    ''' AnsibleLoader() should pass with no errors '''
    pass

# Generated at 2022-06-13 07:46:49.947985
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    # Test for class AnsibleLoader (subclass of Parser)
    from ansible.parsing.yaml.loader import AnsibleLoader
    from yaml import dump
    from collections import namedtuple


    class SampleLoader(AnsibleLoader):
        pass


    # Test for class SampleLoader (subclass of AnsibleLoader)
    class A(object):
        def __init__(self):
            self.a = 1


    class B(object):
        def __init__(self):
            self.b = 2


    # test constructor with class
    sample_data = dump({"A": A, "B": B})
    result = SampleLoader(sample_data).get_single_data()
    assert result == {"A": A, "B": B}

    # test constructor with namedtuple
    NamedTuple

# Generated at 2022-06-13 07:46:58.394714
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    from ansible.parsing.yaml.literals import LiteralUnicode, LiteralInt
    loader = AnsibleLoader(None)
    literal = LiteralUnicode('test')
    assert loader.construct_yaml_str(None, literal) == literal.value
    literal = LiteralInt('123')
    assert loader.construct_yaml_int(None, literal) == literal.value
    literal = LiteralInt('-123')
    assert loader.construct_yaml_int(None, literal) == literal.value

# Generated at 2022-06-13 07:46:59.375485
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(None)
    assert loader

# Generated at 2022-06-13 07:47:05.337530
# Unit test for constructor of class AnsibleLoader
def test_AnsibleLoader():
    loader = AnsibleLoader(stream=None, file_name=None, vault_secrets=None)
    assert isinstance(loader, Reader)
    if HAS_LIBYAML:
        assert isinstance(loader, Parser)
    else:
        assert isinstance(loader, Scanner)
        assert isinstance(loader, Parser)
        assert isinstance(loader, Composer)
    assert isinstance(loader, AnsibleConstructor)
    assert isinstance(loader, Resolver)