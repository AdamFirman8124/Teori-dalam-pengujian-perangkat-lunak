

# Generated at 2022-06-13 14:34:31.398033
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test run method of LookupModule
    """
    # TODO: Use temporary files in tests
    lookup_module = LookupModule()
    lookup_module.set_options(direct={})

    print("%s" % lookup_module.run(['test-fixtures/file.txt']))
    print("%s" % lookup_module.run(['test-fixtures/file2.txt']))

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:34:33.964819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["/etc/foo.txt"]
    lookup_module = LookupModule()
    assert lookup_module.run(terms) == ["foo.txt\n"]

# Generated at 2022-06-13 14:34:39.476403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    script_loader = DictLoader({
        "test_file.txt": "# contents of test_file.txt",
        "test_file2.txt": "# contents of test_file2.txt",
        })
    import collections
    display = collections.namedtuple('Display', ['debug'])
    lookup = LookupModule(loader=script_loader, display=display)
    result = lookup.run(['test_file.txt'])
    assert result == ['# contents of test_file.txt']
    result = lookup.run(['test_file.txt', 'test_file2.txt'])
    result.sort()
    assert result == ['# contents of test_file.txt', '# contents of test_file2.txt']

# Generated at 2022-06-13 14:34:48.532268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup class instance
    lookup = LookupModule()
    lookup.set_options()
    lookup._display = Display()
    lookup._display.verbosity = 3

    # Test with non-existing file
    lookupfile = lookup.run(["/etc/non-existing.file"])[0]
    assert lookupfile is None

    # Test with existing file
    lookupfile = lookup.run(["/etc/hosts"])[0]
    assert lookupfile.startswith("127.0.0.1")
    assert lookupfile.endswith("localhost\n")

# Generated at 2022-06-13 14:34:51.286325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("====No tests implemented yet===")

if __name__ == '__main__':
    print("====No code to test here====")

# Generated at 2022-06-13 14:35:00.477576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # prep for ansible-test network-integration tests
    import os
    import shutil

    test_dir = os.path.dirname(__file__) or '.'
    data_dir = os.path.join(test_dir, '..', '..', 'unit/data')
    adhoc_data_dir = os.path.join(data_dir, 'adhoc')
    shutil.copy(os.path.join(adhoc_data_dir, 'vault_password.txt'), data_dir)

    unvault = LookupModule()
    unvault.console = Display()

    # test unvaulting a file

# Generated at 2022-06-13 14:35:04.299335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    terms = [u'/tmp/ansible_test/file']
    assert m.run(terms) == [u'hello world\n'], "Unable to retrieve data from unvaulted file"

# Generated at 2022-06-13 14:35:16.242421
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for method run of class LookupModule
    # File /etc/file1.txt exists, unvaulted
    # File /etc/file2.txt exists, vaulted
    # File /etc/nonexistent.txt doesn't exist

    class mock_loader:

        def get_real_file(self, lookupfile, decrypt=True):
            if 'file1.txt' in lookupfile:
                return lookupfile

            if 'file2.txt' in lookupfile:
                return lookupfile

            return None

    class mock_display:

        def debug(self, msg=''):
            pass

        def vvvv(self, msg=''):
            pass

    rootdir = os.path.dirname(os.path.dirname(__file__))

    # Create contents of files
    file1 = os.path

# Generated at 2022-06-13 14:35:28.057037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_loader = DummyLoader({'unvault_test/secret_file.txt': 'secret'})
    test_lookup = LookupModule(loader=test_loader)
    # file is found and decrypted
    assert test_lookup.run(['unvault_test/secret_file.txt']) == ['secret']
    # file is not found
    with pytest.raises(AnsibleParserError) as e:
        test_lookup.run(['unvault_test/not_existing_file.txt'])
    assert 'Unable to find file matching' in str(e)
    # file is found but not decrypted
    test_loader.decrypt_result = False

# Generated at 2022-06-13 14:35:34.917015
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create an instance of the class being tested
    module = LookupModule()
    # create a mock class that has similar methods and attributes as the class being tested
    class MockVarsModule(object):
        def set_options(self, var_options, direct):
            pass
        def find_file_in_search_path(self, variables, directories, filename):
            return True
    # associates the mock class with the class being tested
    module._vars = MockVarsModule()
    # replaces the class being tested with a mock class
    class MockLoaderModule(object):
        def get_real_file(self, lookupfile, decrypt):
            return True
        def path_dwim(self, basedir, relpath):
            return True
    module.set_loader(MockLoaderModule())
    # creates a mock class that has similar methods

# Generated at 2022-06-13 14:35:45.501934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # file exist
    terms = ['/tmp/unvault_file.txt']
    expected = [b'This is unvault file.']
    assert(LookupModule().run(terms) == expected)

    # file does not exist
    terms = ['/tmp/unvault_file_does_not_exist.txt']
    try:
        LookupModule().run(terms)
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 14:35:47.704104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([u'password', u'postgres']) == [u'f00b4r', u'barfoo']

# Generated at 2022-06-13 14:36:00.770962
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:36:12.934648
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for AnsibleParserError exception
    lookup_module = LookupModule()
    terms = '/test/test/test'
    try:
        lookup_module.run(terms)
        assert False
    except AnsibleParserError:
        assert True
    # Test for expected value
    lookup_module = LookupModule()
    terms = ['/etc/ansible/ansible.cfg']
    variables={'lookup_file_search_path':['files']}
    actual_return= lookup_module.run(terms, variables)

# Generated at 2022-06-13 14:36:19.575025
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    assert lookupModule.run(['/path/to/the/file'], [], {}) == []
    assert lookupModule.run(['/path/to/the/file'], [], {'ansible_vault_password_file': '/path/to/the/vault_password_file'}) == []

# Generated at 2022-06-13 14:36:26.699549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Creating a LookupModule object with a single term string
    lookup_plugin = LookupModule()
    lookup_plugin.set_options(direct={'_original_file': '/playbooks/foo.yaml'})
    try:
        lookup_plugin.run(['/this/file/does/not/exist'])
        assert False, "Expected an exception"
    except AnsibleParserError:
        assert True, "No exception was thrown"

# Generated at 2022-06-13 14:36:41.014143
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    terms_expected_return = {
        "/etc/passwd": "root:x:0:0:root:/root:/bin/bash\n"
                       "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n"
                       "bin:x:2:2:bin:/bin:/usr/sbin/nologin\n"
                       "sys:x:3:3:sys:/dev:/usr/sbin/nologin\n"
                       "sync:x:4:65534:sync:/bin:/bin/sync\n",
    }

    for term, expected_return in terms_expected_return.items():
        module = LookupModule()
        results = module.run([term])
        assert results

# Generated at 2022-06-13 14:36:53.327776
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class TestVarsModule:
        def __init__(self, inventory):
            self._inventory = inventory

        def run(self, terms=None, variables=None, **kwargs):
            return dict(hostvars=dict((h.name, dict(ansible_host=h.name)) for h in self._inventory.hosts))

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['../../tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
   

# Generated at 2022-06-13 14:37:05.652733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    unvault_test_path = './test/'
    unvault_file = 'unvault.yml'
    file_path = unvault_test_path + unvault_file

    from contextlib import contextmanager
    from .fixtures.lookup import MockLoader
    from ansible.parsing.vault import VaultLib

    @contextmanager
    def run_lookup(
        terms=None,
        variables=None,
        loader=None,
        **kwargs
    ):
        if loader is None:
            loader = MockLoader({
                unvault_test_path+unvault_file: VaultLib().encrypt(
                    variable="fake_variable",
                    value="fake_value"
                )
            })

        lookup_instance = LookupModule(loader=loader)
        yield lookup

# Generated at 2022-06-13 14:37:09.187538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_class = LookupModule()
    with pytest.raises(AnsibleParserError):
        my_class.run(['/etc/foo.txt'])

# Generated at 2022-06-13 14:37:23.736920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    with open('/tmp/ansible_test_unvault_temp_file', 'w') as f:
        f.write('test data')
    assert lookup_instance.run(['/tmp/ansible_test_unvault_temp_file']) == ['test data\n']

# Generated at 2022-06-13 14:37:30.144217
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mock_self = Mock(name='mock_self')
    terms = ['lookup1.txt', 'lookup2.txt']

    expected_result = [u'lookup1 text', u'lookup2 text']

    with patch.object(LookupModule, 'run', return_value=expected_result) as mock_LookupModule_run:
        assert LookupModule.run(mock_self, terms) == expected_result
        mock_LookupModule_run.assert_called_once_with(mock_self, terms)

# Generated at 2022-06-13 14:37:36.118624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests for module run for file unvaulting
    contents = "test content"
    temp_file = open("/tmp/test.txt", "wb")
    temp_file.truncate(0)
    temp_file.write(contents)
    temp_file.close()
    os.system("ansible-vault encrypt /tmp/test.txt --output /tmp/encrypted.txt")
    lookup_module = LookupModule()
    unvault_content = lookup_module.run(["/tmp/encrypted.txt"])
    assert unvault_content == [contents]

# Generated at 2022-06-13 14:37:41.239177
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options=None, direct={})
    assert l.run(['/etc/passwd'], variables={}, **{}) == [to_text(b"root:x:0:0:root:/root:/bin/bash\n")]

# Generated at 2022-06-13 14:37:50.432689
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.hashing import md5s
    from ansible.utils.path import unfrackpath

    # Normal use
    ts = "Normal use (unvaulted)"
    lookup = LookupModule()
    lookup.set_loader(None)
    lookup.set_basedir(None)

    test_file_contents_b = b"some text\n"
    test_file_contents_u = to_text(test_file_contents_b)

    test_file_rel_path = 'test_file.txt'
    test_file_abs_path = unfrackpath(u'/tmp/%s' % test_file_rel_path)


# Generated at 2022-06-13 14:37:58.633568
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module._loader.get_search_paths = lambda: ['/some/path']
    # test file not found
    terms = ['/etc/foo.txt']
    variables = {}
    try:
        lookup_module.run(terms, variables=variables)
        assert False
    except AnsibleParserError:
        pass
    # test file found
    lookup_module._loader.get_real_file = lambda *args: '/some/path/foo.txt'

# Generated at 2022-06-13 14:38:08.065914
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader({})
    lookup_module.set_env({})

    # Test empty terms
    error = "Expected failure on empty terms."
    try:
        lookup_module.run([], {}, **{})
        assert False, error
    except AnsibleParserError as e:
        assert str(e) == 'Empty lookup term.', error

    # Test search path without valid file
    expected_file_name = "foo.txt"
    expected_lookup_term = "/etc/foo.txt"
    expected_error = "Unable to find file matching '{}'.".format(expected_lookup_term)


# Generated at 2022-06-13 14:38:09.027270
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule().run()

# Generated at 2022-06-13 14:38:17.982293
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_args = {}
    lookup_args['terms'] = ['unvault.txt']
    lookup_args['variables'] = {'_filesdir': '/tmp/lookup_plugin_test/files'}
    result = lookup_module.run(**lookup_args)
    assert result == [b'{"secret": "this is my secret"}']

    lookup_args['variables'] = {'_filesdir': '/tmp/lookup_plugin_test/files'}
    lookup_args['_filesdir'] = '/tmp/lookup_plugin_test/files'
    result = lookup_module.run(**lookup_args)
    assert result == [b'{"secret": "this is my secret"}']

    lookup_args['terms'] = ['unvault-2.txt']

# Generated at 2022-06-13 14:38:23.407595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # testing with a regular file
    lookup_module = LookupModule()
    lookup_module.set_loader({'_basedir': '/path/to/', '_files': [('/path/to/test.txt', 'test.txt')]})
    result = lookup_module.run(['test.txt'])
    assert result == ['123\n']

    # testing with a vaulted file
    lookup_module = LookupModule()
    lookup_module.set_loader({'_basedir': '/path/to/', '_files': [('/path/to/.ansible/vault/test.txt.vault', 'test.txt')]})
    result = lookup_module.run(['test.txt'])
    assert result == ['123\n']


# Generated at 2022-06-13 14:38:43.055298
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    assert lookup_module.run([], {}) == []

    assert lookup_module.run(['foo'], {})

# Generated at 2022-06-13 14:38:49.768795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {
        'role_path': [],
        'playbook_dir': u'/playbook',
        'ansible_search_path': [u'/playbook/roles/test-role/tasks', u'/playbook/tasks']
    }
    lookup_module = LookupModule()
    lookup_module.set_loader('test_loader')
    lookup_module.set_options(var_options=variables)
    terms = [u'test.yaml']
    result = lookup_module.run(terms, variables)
    assert result[0] == u"hello, unvault"

# Generated at 2022-06-13 14:38:55.610744
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create object of LookupModule
    lookup_module_obj = LookupModule()

    # create text file 
    text_file = open("/tmp/asdf.txt", "w") 
    text_file.write("LookupModule") 
    text_file.close() 

    # call run method of LookupModule class 
    result = lookup_module_obj.run(['asdf.txt']) 
    assert result == ['LookupModule\n']

# Generated at 2022-06-13 14:39:03.294058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    unit test for method run of class LookupModule
    '''
    module = LookupModule()

    # test 1 : term is a valid file and there is no error in decryption
    terms = ['/etc/ansible/roles/test/files1/lookup_fixtures/lookup_file.txt']
    ret = module.run(terms, variables=None, **None)
    assert (ret == ['this is test file for lookup.\n'])

    # test 2 : term is invalid file path
    terms = ['../lookup_fixtures/lookup_file.txt']
    ret = module.run(terms, variables=None, **None)
    assert (ret == [])

    # test 3 : term is valid file path but unable to decrypt

# Generated at 2022-06-13 14:39:13.091090
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO

    class Options(object):
        def __init__(self, **kwargs):
            for option in kwargs:
                setattr(self, option, kwargs[option])

    class FakeIO(object):
        def __init__(self):
            self.filedata = {}

        def isfile(self, path):
            return path in self.filedata

        def open_file(self, path):
            return StringIO(self.filedata[path])

        def write_file(self, path, data):
            self.filedata[path] = data

        def remove_file(self, path):
            del self.filedata[path]


# Generated at 2022-06-13 14:39:16.696877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run("foo") == ["foo"]
    assert LookupModule().run("foo", {}, var="bar") == ["foo"]
    assert LookupModule().run("foo", {}, var="bar", var2="foo") == ["foo"]

# Generated at 2022-06-13 14:39:26.724426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    path = os.path.dirname(os.path.realpath(__file__))
    lookup_context = magic()
    lookup_context.run_command = lambda x, y: {'rc': 1, 'stderr': 'error message', 'stdout': 'output', 'stdin': 'stdin'}
    lookup_context.get_real_file = lambda x, y: path + "/vault_lookup_test.txt"
    lookup_context.vault_password_file = None
    lookup_context.playbook_dir = os.getcwd()
    lookup_context.private_data_files = []
    lookup_context.template = None
    lookup_context.module_name = 'ansible'
    lookup_context.module_args = 'ansible'

# Generated at 2022-06-13 14:39:28.981714
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['/path/to/file']
    assert lookup.run(terms=terms, variables={}) == ['/path/to/file']

# Generated at 2022-06-13 14:39:36.365042
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockLoader:

        def get_real_file(self, *args, **kwargs):
            return "filename"

    display = Display()
    display.debug = lambda x: None

    a = LookupModule()
    a.display = display
    a._loader = MockLoader()

    b = a.run(terms=["/etc/foo.txt"], decrypt=True, templar=None, all_vars={}, variables={}, **kwargs)

    assert b[0] == u"filename"

# Generated at 2022-06-13 14:39:41.391200
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeContext():
        def __init__(self):
            self.args = ['a', 'b']
            self.kwargs = {'c': 'd'}

    # Failed in locating an existing file in lookup path
    lookup_module = LookupModule()
    lookup_module.set_loader({'get_real_file': lambda *args, **kwargs: None})
    assert lookup_module.run(terms=['/etc/foo.txt'], variables={'ansible_env': {'PATH': '/foo/path'}}) == []

    # Succeed in locating an existing file in lookup path

# Generated at 2022-06-13 14:39:59.943323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Test LookupModule.run")

if __name__ == "__main__":
    print("Test LookupModule")
    test_LookupModule_run()

# Generated at 2022-06-13 14:40:02.681288
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['not_exist']) == []
    assert lookup_plugin.run(['not_exist'])[0] == ""

# Generated at 2022-06-13 14:40:04.060752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(["test1.txt"]) == ["test1"]

# Generated at 2022-06-13 14:40:06.953798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_path = '/etc/foo.txt'
    test_file = LookupModule()
    test_data = to_text(test_file.run(test_path, 1))

    assert test_data is not None
    assert test_data == "bar"

# Generated at 2022-06-13 14:40:18.335899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import shutil
    import yaml
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import ImmutableDict

    # cleanup tmpdir
    def cleanup():
        shutil.rmtree(test_dir)

    # initialize test environment
    test_dir = tempfile.mkdtemp()
    lookupfile = os.path.join(test_dir, 'foo.yml')
    f = open(lookupfile, 'wb')
    f.write(to_bytes("""
    - bad: foo
    - bad2: foo
    - good: bar
    """))
    f.close()
    cleanup()

    # test not decrypted file
    test = LookupModule()
    test.set_

# Generated at 2022-06-13 14:40:26.753770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    class MockVariableManager():
        def __init__(self):
            self.vars = {}
    class MockOptions():
        def __init__(self):
            self.var_options = {}
            self.direct = {}
    definition = {
        '_loader': None,
        '_templar': None,
        '_variables': MockVariableManager(),
        '_options': MockOptions(),
        'basedir': None,
        '_use_cache': True,
        '_cache': {}
    }
    lookup.__dict__.update(definition)
    terms = ['/etc/foo.txt']
    kwargs = {}
    ret = lookup.run(terms, **kwargs)
    assert len(ret) == 1
    assert type(ret) == list

# Generated at 2022-06-13 14:40:37.320081
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:40:38.267854
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:40:41.673045
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with unicode path
    results = LookupModule().run(["tests/test_data/ansible_test.txt"])
    assert len(results) == 1
    assert isinstance(results[0], unicode)
    assert results[0] == u'This is my ansible test file.\n'

# Generated at 2022-06-13 14:40:48.966605
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test module init
    lm = LookupModule()
    assert lm != None
    assert isinstance(lm, LookupModule)

    # Test module run
    v = {
        'vault_password_files': [
            '~/.vault_pass.txt'
        ]
    }
    ret = lm.run(
        [
            'password.txt'
        ],
        variables=v
    )

    assert isinstance(ret, list)
    assert len(ret) == 1
    assert ret[0] == 'MySecretPassword'


# Generated at 2022-06-13 14:41:24.826307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Implement unit test
    pass


# Generated at 2022-06-13 14:41:29.077387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.loader import LookupModule

    terms = ['/etc/foo.txt']

    lu = LookupModule()
    with pytest.raises(AnsibleParserError):
        lu.run(terms)

# Generated at 2022-06-13 14:41:40.154697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    lookup = LookupModule()

    loader = DataLoader()
    variable_manager = VariableManager()

    #term(s) with which LookupModule.run is called
    term = "/path/to/file"
    terms = [term]

    #variables passed to LookupModule.run
    variables = OrderedDict()

    #Mocking the Search path of LookupModule.run
    lookup._loader = loader
    loader.set_basedir('/path/to/file')
    loader._search_paths = ["/path/to/file"]

    #Mocking the find_file_in_search_path

# Generated at 2022-06-13 14:41:46.000833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.debug = True
    lookup = LookupModule()
    lookup.set_options({})
    lookup.set_context('test')
    lookup.run(['unvault_test.yml'])
    lookup.run(['does/not/exist'])

# Generated at 2022-06-13 14:41:56.848070
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case when the file does not have vault/encrypted content
    lookup_obj = LookupModule()
    basedir = os.path.dirname(__file__)
    lookupfile = os.path.join(basedir,'data/plugins/lookup/unvault_test.txt')
    lookupfile = lookupfile.replace('\\', '/')
    lookup_obj._loader._searchpath = ['/home/ansible/unittest_files']
    lookup_obj._datastore = {'_original_file': '/home/ansible/unittest_files/unvault_test.txt', '_original_basedir': '/home/ansible/unittest_files'}
    lookup_obj._basedir = '/home/ansible/unittest_files'

# Generated at 2022-06-13 14:42:06.829891
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Simple test: parameters without vault
    variables = dict(
        ansible_vault_password_file="",
        )
    terms = [
        './test_data/unvault_simple.txt',
    ]
    args = dict(
        variables = variables,
        )

    unvault = LookupModule(**args)
    results = unvault.run(terms)
    assert len(results) == 1
    assert results[0] == "My unvaulted text file\n"

    # Test: parameters with vault
    variables = dict(
        ansible_vault_password_file="",
        )
    terms = [
        './test_data/unvault_vault.txt',
    ]
    args = dict(
        variables = variables,
        )

    unvault = Look

# Generated at 2022-06-13 14:42:07.338691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:42:14.721206
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    b_contents = b"foo: bar"
    module_loader = Mock()
    module_loader.get_real_file.return_value = "/tmp/foo"
    lookup_module = LookupModule(loader=module_loader)
    lookup_module.find_file_in_search_path = Mock(return_value="/tmp/foo")
    with patch('ansible.plugins.lookup.unvault.open', mock_open(read_data=b_contents)):
        assert lookup_module.run(["content.yml"]) == ["foo: bar"]



# Generated at 2022-06-13 14:42:17.112227
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    terms = ['/tmp/foo1.txt', '/tmp/foo2.txt']

    ret = lookup.run(terms)

    assert ret == ['foo1\n', 'foo2\n']



# Generated at 2022-06-13 14:42:21.139663
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_loader(MockLoader())
    assert len(lookup.run(['/etc/foo.txt', '/etc/bar.txt'])) == 2


# Generated at 2022-06-13 14:44:02.748096
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.unvault import LookupModule
    l = LookupModule()
    l.set_options({'__file__': '/etc/ansible/group_vars/all_unencrypted.yml'})
    assert l.run(['/etc/ansible/group_vars/all_unencrypted.yml']) == ['---\nunencrypted_var: this is not encrypted\n']

# Generated at 2022-06-13 14:44:13.509132
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # get base class for testing class LookupModule:
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.plugins.lookup import LookupBase

    # class to be unit tested
    lookup_module = lookup_loader.get('unvault', class_only=True)

    # reference lookup class (base class)
    lookup_base = LookupBase

    # unit test with empty lookup name
    # method run() needs at least one 'term'
    # unit test will exit with an error (AnsibleParserError)
    terms = []
    var_options = None
    kwargs = {}
    lookup_module.run(terms, var_options, **kwargs)

    # second unit test with non empty lookup name
    # unit test will

# Generated at 2022-06-13 14:44:18.782985
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.hashing import checksum_s
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.lookup.unvault import LookupModule
    from ansible.plugins.lookup import LookupBase
    import os
    import shutil
    import tempfile
    import pytest

# Generated at 2022-06-13 14:44:19.333784
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:44:29.173763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method run of class LookupModule

    '''
    display_obj = Display()
    lookup_obj = LookupModule()
    mocker_ansible = mocker.patch('ansible.plugins.lookup.LookupModule.set_options')
    mocker_ansible.return_value = None
    mocker_ansible1 = mocker.patch('ansible.plugins.lookup.LookupBase.find_file_in_search_path')
    mocker_ansible1.return_value = 'test_file'
    mocker_ansible2 = mocker.patch('ansible.plugins.lookup.LookupModule._loader.get_real_file')
    mocker_ansible2.return_value = 'test_decrypted_file'