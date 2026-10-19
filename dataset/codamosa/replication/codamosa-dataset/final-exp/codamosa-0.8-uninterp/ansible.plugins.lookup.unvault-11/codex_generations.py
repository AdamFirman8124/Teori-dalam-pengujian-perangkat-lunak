

# Generated at 2022-06-13 14:34:28.992791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_case = unittest.TestCase()
    test_case.assertTrue(True)



# Generated at 2022-06-13 14:34:29.539324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("TEST")

# Generated at 2022-06-13 14:34:38.595313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize LookupModule and set display.verbosity to DEBUG to enable debug output in assertEquals
    display.verbosity = 4
    lookup_module = LookupModule()
    lookup_module.set_loader(None)

    # Test with invalid term
    try:
        lookup_module.run(['/invalid-file'], None)
    except AnsibleParserError as e:
        assertEquals(e.message, 'Unable to find file matching "/invalid-file" ')

    # Test with valid term
    assertEquals(lookup_module.run(['../tests/integration/targets/lookup_plugins/fake_file.txt'], None), ['fake file\n'])

# Generated at 2022-06-13 14:34:50.100475
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.parsing.vault import VaultLib

    text = VaultLib.encrypt(b'foo', password='test')
    lines = text.splitlines()
    lines = ['$ANSIBLE_VAULT;1.2;AES256;ansible', lines[0], lines[1]]
    vaulted_text = '\n'.join(lines)

    fake_file = StringIO(vaulted_text)

    lookup_plugin = LookupModule()

    terms = 'foo.yml'
    variables = {}
    kwargs = {}

    display.verbosity = 4

    assert lookup_plugin.run(terms, variables, **kwargs) == ['foo\n']

# Generated at 2022-06-13 14:34:59.632900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    fake_loader = FakeLoader()
    fake_display = FakeDisplay()
    lookup = LookupModule(loader=fake_loader, display=fake_display)
    assert sorted(lookup.run(['foo', 'bar'], variables={'files': '/path/to/files', 'bar': 'baz'})) == sorted([
        'foo\n',
        'bar\n',
    ])
    fake_display.vvvv.assert_called_with(u"Unvault lookup found /path/to/files/foo")
    fake_display.vvvv.assert_called_with(u"Unvault lookup found /path/to/files/bar")

# Generated at 2022-06-13 14:35:00.124327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:35:00.628156
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:35:08.860254
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import yaml

    # Create a unvault instance
    unvault = LookupModule()

    # Initialize 'terms' variable
    terms = ["./tests/utils/unvault/a.yml",
             "./tests/utils/unvault/b.yml",
             "./tests/utils/unvault/c.yml"]

    # Initialize 'variables' variable
    variables = None

    # Call the run method
    unvault_run = unvault.run(terms, variables)

    # Check the returned data type
    assert isinstance(unvault_run[0], str)
    assert isinstance(unvault_run[1], str)
    assert isinstance(unvault_run[2], str)

    # Check the vaulted file
    vaulted_data = yaml

# Generated at 2022-06-13 14:35:19.143748
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml import objects
    from ansible.plugins.lookup.unvault import LookupModule
    from ansible.errors import AnsibleParserError
    from ansible.utils.display import Display
    from ansible.errors import AnsibleError
    from io import StringIO
    from ansible.module_utils._text import to_bytes

    class FakeVarsModule(object):
        """
        A dummy class to use in place of VarsModule, which is not available in Ansible < 2.10
        """
        def __init__(self):
            self.vars = dict()

    class FakePlayContext(object):
        """
        A dummy class to use in place of PlayContext, which is not available in Ansible < 2.10
        """
        def __init__(self, options):
            self

# Generated at 2022-06-13 14:35:30.220479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Check that we can read a file's decrypted content.

    Method LookupModule.run() is supposed to read a file containing
    encryped content and return it decrypted.  This test checks that
    it works as expected.  It also checks that an exception is
    generated when a nonexistent file is requested.

    """
    import tempfile
    from ansible.plugins.lookup.unvault import LookupModule
    lookup = LookupModule()
    lookup.set_options(direct={})

# Generated at 2022-06-13 14:35:36.313837
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    d = {}
    # Action
    result = LookupModule().run(term=None, variables=d, **kwargs)
    # Assert
    assert result is None or len(result) == 0

# Generated at 2022-06-13 14:35:47.321264
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves.mock import patch, MagicMock
    import shutil

    class TestLookupModule(LookupModule):
        def __init__(self):
            self._loader = MagicMock()

        def find_file_in_search_path(self, variables, file_type, file_name):
            return file_name

    # Test case 1, file exists and is unvaulted
    test_module = TestLookupModule()
    result1 = test_module.run(['./test/unvault_test_case1.txt'], variables={})
    assert result1 == [u'1\n2\n3\n']

    # Test case 2, file does not exist
    test_module = TestLookupModule()

# Generated at 2022-06-13 14:36:00.414309
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = LookupModule()

    # Required:
    #  - term argument to search

# Generated at 2022-06-13 14:36:07.374134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: not testing encrypted file(s)
    from ansible.errors import AnsibleParserError
    from ansible.parsing.plugin_docs import get_lookup_docs
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.loader import lookup_loader, fragment_loader
    from ansible.utils.display import Display
    display = Display()
    utils.plugins.finder.find_plugins()

    # valid, encrypted file(s)
    terms = [
        {'foo.txt': '/usr/local/share/ansible/lookuptest/foo.txt'}
    ]
    variables = {
        'ansible_search_paths': ['files']
    }
    lookup = LookupModule()
    result = {'foo.txt': 'foo'}

# Generated at 2022-06-13 14:36:13.825673
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup_module = LookupModule()

    open('/tmp/test.txt', 'w').write('Hello World')

    with pytest.raises(AnsibleParserError):
        lookup_module.run(terms=['/tmp/nothere.txt'])

    assert lookup_module.run(['/tmp/test.txt']) == ['Hello World']
    assert lookup_module.run(['/tmp/test.txt', '/tmp/test.txt']) == ['Hello World', 'Hello World']

# Generated at 2022-06-13 14:36:19.830641
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    L = LookupModule()

    # no files to read
    assert L.run(['']) == []

    # one file to read
    assert L.run(['/a/b/c']) is not []

    # two files to read
    assert L.run(['/a/b/c', '/a/b/c']) is not []

# Generated at 2022-06-13 14:36:28.603546
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_bytes
    import tempfile
    import os

    (fd, fname) = tempfile.mkstemp()
    os.close(fd)

    testText = "test"
    testBytes = to_bytes(testText)
    with open(fname, "wb") as f:
        f.write(testBytes)
    lookup = LookupModule()
    terms = [fname]
    results = lookup.run(terms, variables=None, **{})

    assert results[0] == testText
    os.remove(fname)


# Generated at 2022-06-13 14:36:35.657560
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    # generate test file
    fh = open("/tmp/test-unvault.txt", "w")
    fh.write("test")
    fh.close()

    # create lookupobj
    lookup = LookupModule()

    # run lookup
    result = lookup.run(["/tmp/test-unvault.txt"], [], None)

    # check result
    assert (result == ["test"], "unvault file content should be ['test'], not %s" % result)

    # delete test file
    os.remove("/tmp/test-unvault.txt")

# Generated at 2022-06-13 14:36:40.575481
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup_plugin = lookup_loader.get('unvault')
    assert lookup_plugin.run(['./plugins/lookup/unvault_test_file.txt']) == ['This file is used for unit testing of unvault lookup.\n']

# Generated at 2022-06-13 14:36:51.953643
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    import ansible.context
    from units.mock.loader import DictDataLoader

    unvault_terms = ["/etc/foo.txt"]
    mock_loader = DictDataLoader({
        '/etc/foo.txt': 'test\n',
    })
    ansible_vars = {
        'ansible_search_path': ['/etc']
    }
    ansible.context.CLIARGS = {'v': 1}

    loader = DataLoader()
    lookup = LookupModule()
    lookup.set_loader(mock_loader)

    assert lookup.run(unvault_terms, variables=ansible_vars) == ['test\n']

# Generated at 2022-06-13 14:37:07.678550
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=unused-argument
    # pylint: disable=random-module-class-name
    class module_args:
        files = "path to file"

    # pylint: disable=unused-variable
    # pylint: disable=random-module-class-name
    class test_LookupModule(LookupBase):
        # pylint: disable=unused-argument
        # pylint: disable=random-module-class-name
        def run(self, terms, variables=None, **kwargs):
            return [module_args.files]


# Generated at 2022-06-13 14:37:16.794774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    source = ['/etc/foo.txt']

    # On successful lookup
    # -------------------
    expected = [b'John']
    with unittest.mock.patch('ansible.plugins.lookup.unvault.LookupModule.find_file_in_search_path') as mock_find_file_in_search_path:
        mock_find_file_in_search_path.return_value = '/tmp/foo.txt'
        with unittest.mock.patch('ansible.plugins.lookup.unvault._loader.get_real_file') as mock_get_real_file:
            mock_get_real_file.return_value = './test/unvault.py'

# Generated at 2022-06-13 14:37:23.424357
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_input = {
        '_terms': [
            '/etc/foo.txt',
        ],
        '_fqcn': 'ansible.plugins.lookup.unvault',
    }

    expected_output = [u"value of foo.txt\n"]

    # Create a mock object for AnsibleOptions
    class Options:

        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = 10
            self.remote_user = 'test_remote_user'
            self.private_key_file = None
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra_args = None
            self.become = False


# Generated at 2022-06-13 14:37:26.491183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([None], None) == [None]
    assert LookupModule().run(None, None) == [None]
    assert LookupModule().run(['unvault_test'], None) == ["unvault_test\n"]

# Generated at 2022-06-13 14:37:29.673770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyFile:
        def __init__(self, text):
            self.text = text
            self.cursor = 0

        def read(self):
            if self.cursor >= len(self.text):
                return ''
            else:
                self.cursor += 1
                return self.text[cursor]

    # Setup
    lookup_module = LookupModule()
    lookup_module._loader = DummyFile('dummy_content')

    # Test
    assert lookup_module.run(['dummy_file']) == ['dummy_content']

# Generated at 2022-06-13 14:37:37.400701
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import re
    from ansible.module_utils._text import to_bytes

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_path = os.path.join(test_dir, 'unvault_lookup_tests')

    lookup_instance = LookupModule()
    lookup_instance.set_options(plugin_dirs=[test_path])

    # Valid input, 1 non vaulted file
    assert re.match('abc', lookup_instance.run(['unvault_test_non_vaulted.txt'])[0]) is not None

    # Valid input, 1 vaulted file
    assert re.match('def', lookup_instance.run(['unvault_test_vaulted.txt'])[0]) is not None

    # Valid input

# Generated at 2022-06-13 14:37:47.450031
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    display_content = ("Unvault lookup term: /etc/foo.txt\n"
                       "Unvault lookup found /etc/foo.txt\n")

    display_content_without_file = "Unvault lookup term: /etc/foo.txt\n"

    lookup_module_object = LookupModule()

    lookup_module_object.display = display

    lookup_module_object._loader = FakeVarsModule()

    assert lookup_module_object.run(['/etc/foo.txt']) == ['This is a foo.txt\n']
    assert lookup_module_object.run(['/etc/foo.txt'], variables={
        'files': '/etc/'
    }) == ['This is a foo.txt\n']

# Generated at 2022-06-13 14:37:55.059845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Instantiate a LookupModule
    lookup = LookupModule()
    
    # Declare test variables
    #test_terms = ["/etc/test_vault.txt"]
    test_terms = ["/etc/test.txt"]
    
    # Execute the 'run' method
    result = lookup.run(test_terms)
    
    # Display result
    display.vvvv(result)

# Execute the test
if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:38:03.549155
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a LookupModule object
    l = LookupModule()

    # Create a file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    f = open(current_directory + '/test_file.txt', 'w+')
    f.write('TEST FILE')
    f.close()

    # Test the LookupModule.run method on the file
    res = l.run(['/home/admin/test_file.txt'])

    # Delete the file
    os.remove(current_directory + '/test_file.txt')

    return res

# Generated at 2022-06-13 14:38:10.593113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test unvault lookup when file exists
    lookupfile_path = os.path.join(C.LOCAL_VARS_DIR, "test-unvault.yml")
    with open(lookupfile_path, 'w') as lookupfile:
        lookupfile.write("foo")
    returned_contents = module.run([lookupfile_path])
    shutil.rmtree(C.LOCAL_VARS_DIR, True)
    assert returned_contents == [u'foo']

# Generated at 2022-06-13 14:38:19.787758
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    assert lookup_obj.run([]) == []



# Generated at 2022-06-13 14:38:21.082083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Add some unit tests for the run method
    pass

# Generated at 2022-06-13 14:38:23.967731
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['/etc/myfile']
    variables = {}
    kwargs = {}

    lookup = LookupModule()

    assert not lookup.run(terms, variables, kwargs)

# Generated at 2022-06-13 14:38:35.139732
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.utils.display import Display
    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    test_loader = DataLoader()
    test_display = Display()
    test_vars = VariableManager()

    lookup_obj = LookupModule()
    lookup_obj._loader = test_loader
    lookup_obj.set_options(var_options=test_vars)

    # Lookup file
    test_lookup_file = lookup_obj.run(['test_lookup_file.txt'])
    assert test_lookup_file == [u'lookup_contents\n']

    # Lookup file with no extension

# Generated at 2022-06-13 14:38:45.963197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    lookup_module = LookupModule()
    # Ensure we can decrypt a vaulted file
    with tempfile.NamedTemporaryFile() as f:
        f.write(str.encode('test'))
        with open(f.name, 'rb') as data:
            encrypted = AnsibleVaultEncryptedUnicode.from_file(data, None)
        with open(f.name, 'wb') as outfile:
            outfile.write(encrypted.bytes_data)
        terms = [f.name]
        variables = None
        lookup_module.run(terms, variables)

    # Ensure we can decrypt a non-vaulted file

# Generated at 2022-06-13 14:38:50.164936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    mytest = LookupModule()
    mytest.set_options(direct={'_terms': ['test.txt', 'test2.txt']})
    
    assert(mytest.run(mytest._options['_terms'])) == ['test\n', 'test2\n']

# Generated at 2022-06-13 14:38:59.233874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils._text import to_bytes

    # Set vault password
    vault_secret = VaultLib(password='foo')

    # Create file and encrypt it
    file_content = '# Ansible managed\n\ntestvar=foobar'
    encrypted_file_content = vault_secret.encrypt(to_bytes(file_content))

    # Create lookup object of type unvault
    lookup_object = LookupModule()

    # Create vars object

# Generated at 2022-06-13 14:38:59.806739
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:39:06.238690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = ['testFile.yaml']
    test_variables = {'ansible_lookup_plugin_dirs': [{'module_utils/module_utils.py'}]}
    actual_result = LookupModule().run(test_terms, test_variables)
    expected_result = [b'fake_data']
    assert(actual_result == expected_result)

# Generated at 2022-06-13 14:39:11.855801
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # tests that an exception is raised when lookup fails to find the file
    terms = ['/etc/foo.txt']
    LookupModule_run(terms)
    # tests that the content of the file is returned
    #create a file with the content 'blah'
    f = open(terms[0], "w")
    f.write('blah')
    f.close()
    # read the content
    LookupModule_run(terms)


# Generated at 2022-06-13 14:39:32.476445
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ret = lookup.run(['test'])
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert isinstance(ret[0], to_text.__class__)
    assert ret[0] == '{{test}}'

# Generated at 2022-06-13 14:39:42.664323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock loader object which can be used as a class variable
    # in our mock LookupModule object
    # Unfortunately, we can't use the mock loader utility class in this
    # case because it only works with a mock action plugin, which doesn't
    # have the LookupModule class variable loader
    mock_loader = type('MockLoader', (object,), dict())

    lookup_module = type('MockLookupModule', (object,), dict())
    lookup_module._loader = mock_loader

    # Create a fake file in the same path as our mock loader
    # object with the contents we want to return from our lookup
    fake_file = '/fake/path/to/the/file.txt'
    fake_file_contents = 'Hello World'
    with open(fake_file, 'w') as f:
        f.write

# Generated at 2022-06-13 14:39:43.343913
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    assert True

# Generated at 2022-06-13 14:39:46.351315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    path = {"vars": {"ansible_basedir": '/ansible/path'}}
    terms = ["file.txt"]
    ret = module.run(terms, variables=path)
    assert ret == ['Just a test file\n'], ret

# Generated at 2022-06-13 14:39:48.792403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""
    lookup_plugin = LookupModule()
    assert lookup_plugin.run([]) == []

# Generated at 2022-06-13 14:39:58.614099
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import context, plugins

    lookup_plugin = plugins.lookup_loader.get('unvault')

    assert lookup_plugin.run(terms=['/etc/passwd'], variables={'files': []}) == ['root:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:/sbin/nologin\ndaemon:x:2:2:daemon:/sbin:/sbin/nologin\n','admin:x:1000:1000:Administrator:/home/admin:/bin/bash\n']


# Generated at 2022-06-13 14:40:00.064101
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    a = LookupModule()
    test_terms = ()

    # test None return
    assert a.run(terms=test_terms) is None

# Generated at 2022-06-13 14:40:07.469986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    from ansible.errors import AnsibleParserError
    from ansible.parsing.vault import VaultLib
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock
    from ansible_collections.notstdlib.moveitallout.plugins.lookup.unvault import LookupModule

    # Create a mocked object for the object to be tested
    # LookupModule object instantiation
    unvault_lkp = LookupModule()

    # Mock the Loader object and its method loader.get_real_file
    unvault_lkp._loader = MagicMock()

    # Create a mocked object for the loader.get_real_file method and its return_value
    unvault_lkp._loader.get_real_

# Generated at 2022-06-13 14:40:09.361364
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    pass # test_LookupModule_run

# Generated at 2022-06-13 14:40:18.758593
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup.set_loader({'_loader': {'get_real_file': lambda x: x, 'path_sep': ':', '_basedir': '.'}})
    assert lookup.run(['lookup_fixtures.yml']) == ['lookup_fixtures:\n  local:\n    hello: world\n']

    lookup.set_loader({'_loader': {'get_real_file': lambda x: x, 'path_sep': ':', '_basedir': './'}})
    assert lookup.run(['lookup_fixtures.yml']) == ['lookup_fixtures:\n  local:\n    hello: world\n']

# Generated at 2022-06-13 14:41:05.363610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    # create an instance of the class 
    lookup = LookupModule(display) 
    # create an instance of DictDataLoader 
    data_loader = DictDataLoader({}) 
    # set _loader instance attribute of lookup 
    lookup._loader = data_loader
    # call search_path
    search_path = lookup.search_path(None, None)
    # call find_file_in_search_path 
    lookupfile = lookup.find_file_in_search_path(None, 'files', 'test.txt')
    # call run method and pass lookupfile, None and None to it
    result = lookup.run(lookupfile, None, None)
    return result

# Generated at 2022-06-13 14:41:06.336046
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert LookupModule.run is not None

# Generated at 2022-06-13 14:41:09.790961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    # LookupModule.run method input parameters
    terms = ['/tmp/file1']
    variables = {}
    # LookupModule.run method expected output
    expected = b"This is file1\n"

    # Act
    obj = LookupModule()
    actual = obj.run(terms, variables)

    # Assert
    assert actual[0] == expected

# Generated at 2022-06-13 14:41:18.598405
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    filename = 'test.yml'
    vault_file = 'test.ymlvault'
    module.set_options(direct={'encrypt': 'yaml', '_enc_password': 'test'})
    with open(filename, 'w') as f:
        f.write('test')
    module._loader.set_vault_password('test')
    module._loader.encrypt_vault('test.yml', 'test.ymlvault', vault_file, 'yaml')
    compare_file = 'test.ymlvault'
    assert module.run([filename]) == module._loader.get_vaulted_files()

# Generated at 2022-06-13 14:41:29.966509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils._text import to_bytes
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    basepath = unfrackpath("$MODULE_CACHE_DIR")
    test_file = os.path.join(basepath, 'test_lookup_unvault_run_file')
    test_value = "my test string"

    # no test_file exists
    assert not os.path.isfile(test_file)
    # no file exists in tmpdir
    assert not os.path.isfile(os.path.join(tmpdir, os.path.basename(test_file)))
    # create a file with test_file in tmpdir and contain some text

# Generated at 2022-06-13 14:41:36.899911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Initialize test objects
    lookup_mod = LookupModule()
    lookup_mod.set_loader(None)

    # Initialize test variables
    terms = ["/etc/testFoo"]
    variables = dict()
    kwargs = dict()

    # Test run method
    ret = lookup_mod.run(terms, variables, **kwargs)

    # Assert expected return value
    assert ret == "testFoo"

# Generated at 2022-06-13 14:41:42.063478
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()
    assert lookup_plugin.run([]) == []
    assert lookup_plugin.run(['/etc/hosts']) == [u'127.0.0.1 localhost\n\n# The following lines are desirable for IPv6 capable hosts\n::1 ip6-localhost ip6-loopback\nfe00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters\nff02::3 ip6-allhosts\n\n']

# Generated at 2022-06-13 14:41:45.163316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod_args = {
        '_terms': ['foo.txt'],
        '_bsf_loader':
        {
            '_search_path': {
                'files': ['/etc']
            }
        }
    }
    text = 'the value of foo.txt is {{lookup(\'unvault\', \'foo.txt\')|to_string }}'
    assert mod.run(**mod_args) == ['foo']

# Generated at 2022-06-13 14:41:52.261472
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["/etc/foo.txt", "/etc/bar.txt"]
    result = lookup.run(terms)
    assert len(result) == len(terms)
    try:
        lookup.run(["/etc/no-foo.txt"])
        assert False, "Expected an AnsibleParserError exception."
    except AnsibleParserError as e:
        assert str(e).__contains__("Unable to find file matching")

# Generated at 2022-06-13 14:41:55.402532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = "test_file.txt"
    result = lookup.run(terms)

    assert(result[0] == to_text(b'Test file content\n'))

# Generated at 2022-06-13 14:43:33.882506
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TEST: Invalid path leads to AnsibleParserError
    lookup_module = LookupModule()
    lookup_module.set_options(direct={'plugin_name': 'unvault'})
    invalid_path = ['/invalid/path']
    assert lookup_module._check_for_vault(invalid_path, None) == False
    try:
        lookup_module.run(invalid_path)
        fail('Expected an AnsibleParserError')
    except AnsibleParserError as e:
        assert 'Unable to find file' in str(e)

    # TEST: Empty lookup returns empty list
    assert lookup_module.run([]) == []

    # TEST: Regular lookup not vaulted does not decrypt
    assert lookup_module.run(['test/test_unvault.py']) != []

    # TEST: Regular

# Generated at 2022-06-13 14:43:43.595349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakePlugin(object):
        def __init__(self):
            self.name = "unvault"
    class FakeVars(object):
        def __init__(self):
            self.my_vars = {'vars':{}}
    class FakeLoad(object):
        def __init__(self, vars=None):
            self.vars = vars
    class FakeLookupBase(LookupBase):
        def __init__(self, loader=None, templar=None, **kwargs):
            self.runner = FakePlugin()
            self.loader = loader
            self.templar = templar
            self.options = kwargs
    class FakeFile(object):
        def __init__(self, contents):
            self.contents = contents
            self.close = lambda: None

# Generated at 2022-06-13 14:43:44.387232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert( isinstance( LookupModule().run( ['/foo.txt'] ), list ) )

# Generated at 2022-06-13 14:43:46.139735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader()

    terms = ['test_data', 'test_data']
    ret = lookup_module.run(terms)

    assert ret == ['foobar', 'foobar']


# Generated at 2022-06-13 14:43:49.789864
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/etc/foo.txt']
    lookup_plugin = LookupModule()
    lookup_plugin.get_search_paths = lambda :['.']
    assert lookup_plugin.run(terms) == ['This is foo']


# Generated at 2022-06-13 14:44:01.702447
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Inside a TestCase class
    file = open("/ansible/test/data/lookup_plugins/files/unvault_test_file.txt", "r")
    TEST_FILE_DATA = file.read()
    file.close()

    unvault_lookup = LookupModule()
    assert TEST_FILE_DATA == unvault_lookup.run(["./test/data/lookup_plugins/files/unvault_test_file.txt"])[0]

    unvault_lookup = LookupModule()
    unvault_lookup.set_options({}, {}, {"ansible_lookup_unvault_vault_password":"unvault_lookup_test"})

# Generated at 2022-06-13 14:44:06.083483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookupModule = LookupModule()
    terms = ['/etc/foo.txt']
    variables = dict()
    kwargs = dict()
    results = test_lookupModule.run(terms, variables, **kwargs)
    assert len(results) == 1
    assert results[0] == 'hello world'

# Generated at 2022-06-13 14:44:15.730967
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    fields_lookup = {
        '_ansible_display': Display(),
        '_ansible_no_log': False,
        '_ansible_verbosity': False,
        'run_once': False,
        'play': None,
        'play_context': None,
        '_ansible_debug': False,
    }
    terms = '/some/file/location'
    variables = None
    kwargs = { '_ansible_diff': False }

    lookup = LookupModule()
    lookup.set_loader('some_loader')
    lookup.set_options(**fields_lookup)
    lookup.get_file_contents_from_file = lambda *x: 'some content'.encode()
    lookup.find_file_in_search_path = lambda *x: '/some/file/location'

# Generated at 2022-06-13 14:44:27.154199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['tests/units/lookup_plugins/test_unvault_data/unvault_file.yml']
    result = module.run(terms=terms, variables={'role_path': '',
                                                'roles_path': '/etc/ansible',})