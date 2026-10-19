

# Generated at 2022-06-13 13:42:04.297282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    mod = lookup_loader.get('fileglob', class_only=True)
    assert mod.run(['~/*'], variables={'ansible_env':{'HOME': '/root'}}, wantlist=True) == ['/root/.bash_history', '/root/.bash_logout', '/root/.bash_profile', '/root/.bashrc', '/root/.cache', '/root/.config', '/root/.gemrc', '/root/.inputrc', '/root/.local', '/root/.profile', '/root/.ssh', '/root/.bash_logout']

# Generated at 2022-06-13 13:42:09.151371
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    print(module.run([u'*.py'], {u'ansible_search_path': [u'/root/ansible']}, {u'wantlist': True}))

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:42:12.972224
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    path = "./test_lookup/fileglob"
    term = "*"
    term_file = os.path.basename(term)

    lookup = LookupModule()
    result = lookup.run([term])

    file_list = os.listdir(path)

    for filename in file_list:
        assert os.path.join(path, filename) in result

# Generated at 2022-06-13 13:42:17.827333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit tests for method run of class LookupModule"""
    lookup = LookupModule()
    result = lookup.run(['Playbook_test_1.txt'], {'ansible_facts': {'search_path': '/tmp'}})
    assert result == []

# Generated at 2022-06-13 13:42:30.227764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The test case below asserts only the correct behaviour,i.e., the expected results are returned
    # by the method run() of class LookupModule.
    # It does not provide a complete test of all behaviours required by the specification of that method.
    #
    # The test case below requires a directory 'tests/unit/lookup_plugins/fileglob/data'
    # to exist in the directory where the test is run.
    import sys
    import os
    import unittest
    import shutil
    import tempfile
    import ansible.utils.path
    import ansible.module_utils._text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
   

# Generated at 2022-06-13 13:42:31.138352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 13:42:36.425876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()
    try:
        test_lookup.run(["/test/files/*.yaml"],
                        variables={
                            "ansible_search_path": ['/test/files']
                        },
                        wantlist=True)
    except AnsibleFileNotFound:
        pass
    else:
        assert False, "No error was raised when a search path was not present in the args, yet the search path was in the variable ansible_search_path."

# Generated at 2022-06-13 13:42:41.651991
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    result = lookup_module.run(terms= ['README.md'], variables= {'ansible_search_path': ['test_data/test_fileglob']})
    assert result == ['test_data/test_fileglob/README.md']

# Generated at 2022-06-13 13:42:50.138345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    arg1 = ['testfile']
    arg2 = {'ansible_search_path': [os.getcwd()]}
    arg3 = {'wantlist': False}
    arg4 = None

    # create temporary file
    with open('testfile', 'w') as f:
        pass

    # create instance of class LookupModule
    lm = LookupModule()

    # get path list
    path_list = lm.run(arg1, arg2, **arg3)

    # check result
    assert len(path_list) == 1

    # delete temporary file
    os.remove('testfile')

# Generated at 2022-06-13 13:42:55.261646
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test Class Instantiation
    module = LookupModule()
    # Test Method: run
    test_terms = ['./test_data/fileglob1.txt', './test_data/fileglob2.txt']
    result = module.run(test_terms)
    assert result == [u'./test_data/fileglob1.txt', u'./test_data/fileglob2.txt']

# Generated at 2022-06-13 13:43:04.480810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule
    test_object = LookupModule()
    
    # Define "terms"
    terms = [
        '/my/path/*.txt',
        'fooapp/*'
    ]

    # Define "variables"
    variables = [
        'ansible_search_path',
        'ansible_playbook_python',
        'ansible_playbook_dir'
    ]

    # Invoke lookup module
    test_object.run(terms, variables)

# Generated at 2022-06-13 13:43:09.819452
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, {}).run(["*"]) == []
    assert LookupModule(None, {}).run(["foobar"]) == []
    assert LookupModule(None, {}).run(["/etc"]) == []
    assert sorted(LookupModule(None, {}).run(["*.txt"])) == ['.gitignore.txt', 'ansible-hacking.txt', 'requirements.txt', 'config.ini.txt']
    assert sorted(LookupModule(None, {}).run(["README.rst"])) == ['README.rst']
    assert sorted(LookupModule(None, {}).run(["*.ini.txt"])) == ['config.ini.txt']

# Generated at 2022-06-13 13:43:17.055756
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Path of the file "test2.txt" is the same as the current python file
    # This is not used in the test

    # Path of the file "test1.txt" is the same as the parent of the python file
    path_of_test1_txt = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    path_of_test1_txt += os.path.sep + "test1.txt"

    # Create the file "test1.txt"
    with open(path_of_test1_txt, "w") as f:
        f.write("test1")

    # Perform test
    expected = [path_of_test1_txt]
    lookup = LookupModule()
    result = lookup.run(['test*.txt'])

    # Check result

# Generated at 2022-06-13 13:43:27.241702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # glob.glob is mocked out so that method call returns ['file1.txt', 'file2.txt', 'file3.txt']
    def mock_glob(path):
        # don't mock the other method calls
        return ['file1.txt', 'file2.txt', 'file3.txt']

    # os.path is mocked out so that the only method call being mocked is os.path.isfile
    # instead of os.path.isfile returning a boolean value, it returns an integer value
    # as a boolean value would be sufficient to determine if the test case passed or failed
    def mock_isfile(path):
        return 1

    # Initializing LookupModule class
    lookup_module = LookupModule()

    # mocked out glob module
    lookup_module.glob = mock_glob

    # mocked out os.path module

# Generated at 2022-06-13 13:43:38.887906
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # testing the results of lm.run with fileglob.
    test_terms = ['test*.txt']
    mock_filename = 'test file'
    mock_basedir = '/home/tmp/'

    # mocking glob.glob to return a mock_filename
    class MockGlob:
        def glob(globPath):
            return [mock_filename.encode("utf-8")]

    # mocking LookupBase to return a mock_basedir
    class MockLookupBase:
        def get_basedir(self, variables):
            return mock_basedir

        def find_file_in_search_path(self, variables, dirname, path):
            return None

    # mocking os to return a mock_filename

# Generated at 2022-06-13 13:43:47.096314
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:43:57.813780
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options:
        def __init__(self, verbosity=0, connection='', remote_tmp='/tmp', private_key_file=None,
                     timeout=10, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None,
                     scp_extra_args=None, become=False, become_method=None, become_user=None, check=False,
                     diff=False):
            self.verbosity = verbosity
            self.connection = connection
            self.remote_tmp = remote_tmp
            self.private_key_file = private_key_file
            self.timeout = timeout
            self.ssh_common_args = ssh_common_args or ''
            self.ssh_extra_args = ssh_extra_args or ''
            self.sftp_extra_args

# Generated at 2022-06-13 13:44:08.221448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Dummy variables.
    # FIXME: should probably be a dumper for variables
    variables = {
        'ansible_search_path': [
            '/etc',
            '/usr/share'
        ]
    }

    # Test if find_file_in_search_path() can find a valid path.
    # First, a file present in the search path.
    lu = LookupModule()
    path = lu.find_file_in_search_path(variables, 'files', 'test')

    assert path == '/usr/share/test'

    # Next, a file not present in the search path.
    path = lu.find_file_in_search_path(variables, 'files', 'inexistent_file')

    assert path is None

    # Test if run() can find all expected paths.


# Generated at 2022-06-13 13:44:16.487665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    dr = "/home/mraj/ansible_test/test_modules/ansible/module_utils"
    os.environ['ANSIBLE_MODULE_UTILS'] = dr
    # print(os.environ['ANSIBLE_MODULE_UTILS'])
    lm = LookupModule()
    terms = ["./test_module.py", "./test_module.py"]
    # print(lm.run(terms))
    assert(lm.run(terms) == [dr + "/test_module.py", dr + "/test_module.py"])

# Generated at 2022-06-13 13:44:23.578199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    basedir = os.path.join(os.path.dirname(__file__), '..', '..')
    terms = [os.path.join(basedir, 'lib/ansible/*')]
    result = module.run(terms, {})
    assert len(result) > 1
    assert 'ansible/modules/core/system/accounts.py' in result
    assert '/ansible/modules/core/system/accounts.py' not in result

# Generated at 2022-06-13 13:44:36.712953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    results = LookupModule().run([
        'file1.txt',
        '/folder/file2.txt',
        '/folder/file3.txt',
        'file4.txt',
        '/folder/file5.txt',
        'file6.txt',
        '/folder/file7.txt'
    ], {
        'ansible_search_path': [
            '/c/folder1/',
            '/d/folder2/',
            '/e/folder3/'
        ]
    })


# Generated at 2022-06-13 13:44:48.129660
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # Test case 1: Inputs: terms = ["/test_dir/test_path1.txt"]
    # Expected: ret = ["/test_dir/test_path1.txt"]
    # assertEqual(list1, list2) compares list1 and list2
    assertEqual(["/test_dir/test_path1.txt"], lookup.run(["/test_dir/test_path1.txt"]))

    # Test case 2: Inputs: terms = ["/test_dir/test_path2.txt"]
    # Expected: ret = []
    assertEqual([], lookup.run(["/test_dir/test_path2.txt"]))

    # Test case 3: Inputs: terms = ["test_path3.txt"]
    # Expected: ret = ["test_

# Generated at 2022-06-13 13:44:48.569606
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:44:55.572387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    basedir = lookup.get_basedir({})
    terms = [os.path.join(basedir, 'LookupModule_run_file1.txt'),
             os.path.join(basedir, 'LookupModule_run_file3.txt')]
    result = lookup.run(terms, [], wantlist=True)
    assert result[0] == terms[0]
    assert result[1] == terms[1]


# Generated at 2022-06-13 13:45:05.959911
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testcase 1: Check whether return type of method run is list
    l = LookupModule()
    l.set_options({})
    result = l.run(terms=["*"], variables={})
    assert isinstance(result, list)

    # Testcase 2: Check whether return value of method run is empty list
    l = LookupModule()
    l.set_options({})
    result = l.run(terms=["*"], variables={})
    assert result == []

# Generated at 2022-06-13 13:45:17.981124
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    # ########
    # TEST 1 #
    # ########

    # Input values:
    #   - terms         : ['/testing.yml']
    #   - variables     : {
    #                        'ansible_play_hosts': '127.0.0.1',
    #                        'hostvars': {
    #                            '127.0.0.1': {"ansible_facts": "testing"}
    #                        }
    #                      }
    #   - kwargs        : {}
    # Expected output:
    #   - ret           : ['/testing.yml']

    # Mock object:

    class MockFile:
        pass

    # Code to test:

    terms = ['/testing.yml']

# Generated at 2022-06-13 13:45:29.886380
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants
    from ansible.module_utils.six import StringIO
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'item': 'localhost'}

    play_context = PlayContext()

    tmp_fd, tmp_path = tempfile.mkstemp(text=True)


# Generated at 2022-06-13 13:45:39.297479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    results = lookup.run([], dict(ansible_search_path=['./ansible/data']))
    assert results == []

    results = lookup.run(['*.txt'], dict(ansible_search_path=['./ansible/data']))
    assert len(results) == 3
    # path used by the test is different on Windows
    if os.name == 'nt':
        assert set(['./ansible/data/bar.txt', './ansible/data/foo.txt']) == set(results)
    else:
        assert set(['./ansible/data/bar.txt', './ansible/data/foo.txt', './ansible/data/test.txt']) == set(results)


# Generated at 2022-06-13 13:45:46.478037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup mock
    term = '/my/path/*.txt'
    variables = None
    test_obj = LookupModule()
    test_obj.find_file_in_search_path = lambda variables, dir_name, file_name: '/my/path'

    # Execute method under test
    result = test_obj.run(terms=term, variables=variables)

    # Assert expected result
    assert result is not None
    assert result == []


# Generated at 2022-06-13 13:45:56.082693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    assert ['foo'] == l.run(['test'], {'_ansible_file_name': '/some/path/test.yml', '_ansible_search_path': ['/some/path']})
    assert ['foo', 'bar'] == l.run(['test', 'test2'], {'_ansible_file_name': '/some/path/test.yml', '_ansible_search_path': ['/some/path']})

# Generated at 2022-06-13 13:46:03.070711
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(['/my/path/license.txt']) == ['/my/path/license.txt']

# Generated at 2022-06-13 13:46:10.980151
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_terms = ['./test_file*']
    results = lookup_module.run(test_terms, variables=dict(ansible_basedir=test_dir))
    assert results == ['%s/test_file1' % test_dir, '%s/test_file2' % test_dir]

# Generated at 2022-06-13 13:46:20.792218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import __version__ as ansible_version
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.plugins.lookup.fileglob import _compat_kwargs

    # setup standard patching for test fixtures
    module_utils_path = 'ansible.module_utils.parsing.plugin_docs.'
    if PY2:
        module_utils_mock_spec = (module_utils_path + 'AnsibleModule')
    else:
        module_utils_mock_spec = (module_utils_path + 'AnsibleModule.__new__')
    if PY3:
        import builtins

# Generated at 2022-06-13 13:46:28.035507
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with dir and file name
    file_path1 = "/my/path/file.txt"
    ret1 =  LookupModule().run(terms=[file_path1])
    assert ret1 == ["/my/path/file.txt"]

    # test with only file name
    file_name = "file.txt"
    terms = [file_name]
    ret =  LookupModule().run(terms=terms)
    assert "/my/path/file.txt" in ret

# Generated at 2022-06-13 13:46:35.492724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    basedir = os.path.realpath(os.path.dirname(__file__))
    terms = ["*.txt"]
    variables = { 'ansible_search_path': [
        "/etc",
        os.path.join(basedir, "files"),
    ]}

    # When
    lm = LookupModule()
    ret = lm.run(terms, variables=variables)

    # Then
    assert(ret)
    assert(len(ret) > 0)

    # Given
    terms = ["*.tcf"]
    variables = { 'ansible_search_path': [
        "/etc",
        os.path.join(basedir, "files"),
    ]}

    # When
    lm = LookupModule()

# Generated at 2022-06-13 13:46:47.418616
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def mock_get_basedir(variables):
        # Return nothing as we don't need it
        return

    lookup_obj = LookupModule()
    lookup_obj.get_basedir = mock_get_basedir

    # Mock glob.glob function
    old_glob_function = glob.glob
    def mock_glob_function(*args, **kwargs):
        arg1 = args[0]
        if arg1 == b'/playbooks/files/fooapp/*':
            return [b'/playbooks/files/fooapp/foo1', b'/playbooks/files/fooapp/foo2']
        elif arg1 == b'/my/path/*.txt':
            return [b'/my/path/file1.txt', b'/my/path/file2.txt']
        else:
            NotImplemented

# Generated at 2022-06-13 13:46:58.694542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    from os.path import isdir, isfile, join
    from shutil import rmtree
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ansible_search_path': tempfile.gettempdir()}

    lookup_plugin = LookupModule()

    test_dir = join(tempfile.gettempdir(), 'lookup_dir')
    prefix_dir = join(test_dir, 'prefix_dir')
    sub_dir = join(test_dir, 'sub_dir')

    try:
        rmtree(test_dir)
    except:
        pass


# Generated at 2022-06-13 13:47:07.564026
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock class for LookupBase
    class LookupBaseMock():

        def get_basedir(self, variables=None):
            return os.path.dirname(__file__)

        def find_file_in_search_path(self, variables, paths, dirname):
            return os.path.abspath(dirname)

    ret = []
    terms = ['/test_dir/*.txt', '/test_dir/*.tmp']
    variables = None
    kwargs = {}

    lookupModule = LookupModule()
    lookupModule.set_loader(LookupBaseMock())
    returned_ret = lookupModule.run(terms, variables, **kwargs)

    assert returned_ret == ret

# Generated at 2022-06-13 13:47:17.002363
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class DummyVars():
        ansible_search_path = []

    mock_self = DummyVars()
    mock_self.runner = DummyVars()
    mock_self.runner.config = DummyVars()
    mock_self.runner.config.basedir = '/some/basedir'
    mock_self.get_basedir = lambda v: '/some/basedir'

    mock_self.find_file_in_search_path = lambda v, dname, fname: None
    result = LookupModule.run(mock_self, terms=['foo'], variables=None)
    assert result == []

    mock_self.find_file_in_search_path = lambda v, dname, fname: '/some/basedir/foo'

# Generated at 2022-06-13 13:47:26.630193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class UnitTestLookupModule(LookupModule):
        def __init__(self, basedir=None, **kwargs):
            self.basedir = basedir
        def get_basedir(self, variables):
            return self.basedir

    module = UnitTestLookupModule(basedir='/home/username/playbooks')

    # Testing regular lookup
    terms = ['/home/username/playbooks/files/fooapp/bar']
    results = module.run(terms=terms, variables=None)
    assert results == ['/home/username/playbooks/files/fooapp/bar']

    # Testing lookup with a pattern
    terms = ['/home/username/playbooks/files/fooapp/*']
    results = module.run(terms=terms, variables=None)

# Generated at 2022-06-13 13:47:44.202996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    p = LookupModule()
    terms = ['/home/ec2-user/test.txt', 'test.py']
    variables = {'ansible_search_path': ['/home/ec2-user'], 'ansible_playbook_dir': '/etc/ansible'}
    assert p.run(terms, variables) == ['/home/ec2-user/test.txt']

# Generated at 2022-06-13 13:47:50.203438
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """This function is to test run method of class LookupModule
    """
    # create an instance of LookupModule class
    lookup_module_obj = LookupModule()
    args = ["testlookupfile","testlookupfile1"]
    ret=lookup_module_obj.run(args)
    # check if the function returns list
    if type(ret) is list:
        assert True
    else:
        assert False

# Generated at 2022-06-13 13:47:59.385987
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test that fileglob will match files contained in one or more sub directories
    lm = LookupModule()
    assert '/test/test/test' in lm.run(['./test/test/test'])
    assert '/test/test/test' in lm.run(['test/test/test'])
    assert '/test/test' in lm.run(['test/test'])

    # test that fileglob will not match directories
    assert 'test/test' not in lm.run(['test/test'])

    # test that fileglob will match relative paths
    assert 'test/test/test' in lm.run(['./test/test/test'])

    # test that fileglob will match files conatined in one or more parent directories

# Generated at 2022-06-13 13:48:09.378665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    dwimmed_path = '/playbooks/files/fooapp/*'
    term_file = 'foo'
    # Test with a valid dwimmed path. This test should return only 'term_file'
    l = LookupModule()
    l.get_basedir = lambda x: dwimmed_path
    assert l.run([term_file]) == [term_file]
    # Test with an invalid dwimmed path. This test should return 'Nothing'.
    l.get_basedir = lambda x: ''
    assert l.run([term_file]) == []

# Generated at 2022-06-13 13:48:19.370773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Create an empty ansible module for testing
    class Options:
        _terms = ['test']
        wantlist = False
    from ansible.utils.display import Display
    class AnsibleModule:
        def __init__(self):
            self.options = Options()
            self.params = {'_raw_params': 'test'}
            self.display = Display()
    amodule = AnsibleModule()
    import os
    import tempfile
    #Create a temporary directory for testing
    test_dir = tempfile.mkdtemp()
    #Create a temporary file for testing
    test_file = tempfile.NamedTemporaryFile(dir=test_dir)
    #Add file name to term

# Generated at 2022-06-13 13:48:27.325344
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Python < 2.7.3 returns an empty string in os.path.abspath('.')
    basedir = os.path.normpath(os.path.abspath('.'))
    lookup = LookupModule()
    result = lookup.run(['./test/test_lookup_plugins/txt'], {'ansible_search_path': [basedir, './test/test_lookup_plugins']})
    assert result == [os.path.join(basedir, "test", "test_lookup_plugins", "txt")]

# Generated at 2022-06-13 13:48:32.158618
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    test_arr = ["/tmp/file"]
    ret = l.run(test_arr, {})
    assert len(ret) == 0

    test_arr = ["/tmp/*"]
    ret = l.run(test_arr, {})
    assert len(ret) == 0

# Generated at 2022-06-13 13:48:37.432938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()

    assert test.run(['./test/data/*']) == ['./test/data/example.cfg', './test/data/example1.cfg']
    assert test.run(['./test/data/*.cfg']) == ['./test/data/example.cfg', './test/data/example1.cfg']

# Generated at 2022-06-13 13:48:39.550623
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['my_file.py']
    ret = lookup.run(terms)
    print(ret)

# Generated at 2022-06-13 13:48:47.467541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import glob
    import stat

    test_path = os.getcwd()
    test_filedir = os.path.join(test_path, 'LookupPlugins')
    test_zipfile = os.path.join(test_filedir, 'ExamplePlugins.zip')

    # If a zipfile exists, then remove it
    if os.path.exists(test_zipfile):
        os.chmod(test_zipfile, stat.S_IWUSR)
        os.unlink(test_zipfile)

    # Test the run method of class LookupModule
    lm = LookupModule()
    test_terms = ['ExamplePlugins.zip']
    test_variables = {'ansible_search_path': [test_filedir]}

# Generated at 2022-06-13 13:49:22.445234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["*.ini", "*.conf"], {}, wantlist=True) == []
    import tempfile
    dirname = tempfile.mkdtemp(prefix="ansible-test-fileglob")
    items = ["foo.ini", "bar.conf", "baz.bin", "etc.conf"]
    for item in items:
        open(os.path.join(dirname, item), "w").close()
    assert sorted(LookupModule().run([os.path.join(dirname, "*.conf")], {}, wantlist=True)) == \
            sorted([os.path.join(dirname, "bar.conf"), os.path.join(dirname, "etc.conf")])

# Generated at 2022-06-13 13:49:33.343381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Method run of class LookupModule can be tested using the following terms and variables
    terms = [
        "/etc/passwd"
    ]

    variables = {
        "ansible_search_path": [
            "/home/ansible/playbook/roles/lookup/files"
        ]
    }

    assert lookup.run(terms, variables) == ["/home/ansible/playbook/roles/lookup/files/etc/passwd"]

    # Method run of class LookupModule can be tested using the following terms and variables
    terms = [
        "*.txt"
    ]

    variables = {
        "ansible_search_path": [
            "/home/ansible/playbook/roles/lookup/files"
        ]
    }


# Generated at 2022-06-13 13:49:44.148230
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = LookupModule().run(["*.yaml"])
    # EXPECTED TO FIND FILES IN /TEST DIRECTORY WITH EXTENSION yaml
    assert len(ret) == 10, "Expected 10 files with extension yaml in /test directory"

# Generated at 2022-06-13 13:49:50.067908
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    targets = [ '/some/dir/file1.txt', '/some/dir/file2.txt', '/some/dir/file3.txt' ]
    for target in targets:
        open(target, 'w').close()
    results = module.run(terms=["/some/dir/*.txt"])
    # Remove test files
    for target in targets:
        os.remove(target)

    assert len(results) == 3

# Generated at 2022-06-13 13:50:06.330297
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    def get_basedir_mock(self, variables):
        return '.'

    def find_file_in_search_path_mock(self, variables, directory, filename):
        return os.path.join('.', directory, filename)

    class AnsibleFileNotFoundMock(AnsibleFileNotFound):
        """
        Class AnsibleFileNotFoundMock for mocking AnsibleFileNotFound
        """
        pass

    class LookupModuleMock(LookupBase):
        """
        Class LookupModuleMock for mocking LookupModule
        """
        def get_basedir(self, variables):
            return get_basedir_mock(self, variables)


# Generated at 2022-06-13 13:50:18.644756
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    path_to_src_file = os.path.join(os.path.dirname(__file__), '../lookup_plugins/fileglob.py')

# Generated at 2022-06-13 13:50:25.953418
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of class
    lookup_module = LookupModule()
    # Create test variables
    variables = {
        'ansible_search_path': [
            "ansible/test/unittests/test_files/roles/fileglob_role/files",
            "ansible/test/unittests/test_files/roles/fileglob_role",
            "ansible/test/unittests/test_files"
        ]
    }
    # Create test terms
    terms = [
        'test1.txt',
        'test2.txt',
        'test3.txt',
        'inner_dir/inner_file1.txt',
        'inner_dir/inner_file2.txt'
    ]
    # Run method run with terms and variables
    list_of_files = lookup_module

# Generated at 2022-06-13 13:50:32.945391
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests if the following case is propery handled. If a file
    # is not found, then return empty list.
    l = LookupModule()
    l.get_basedir = lambda x: ''
    assert l.run(['unexsisting_file'], {}) == []

    # Tests if the following case is propery handled. If a file
    # is found, then return path to file.
    l = LookupModule()
    l.get_basedir = lambda x: ''
    assert l.run(['README.rst'], {}) == [u'README.rst']

# Generated at 2022-06-13 13:50:36.892455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run([ 'src/sample-*.txt' ], variables=dict( ansible_search_path=[ '/home/foo' ]))
    assert result == [ '/home/foo/src/sample-test.txt' ]

# Generated at 2022-06-13 13:50:48.848549
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    global_args = dict(
        _ansible_search_paths='[["playbooks/files", "playbooks/vars"]]',
        _ansible_no_log='False'
    )
    # init LookupBase
    lookupBase = LookupBase()
    
    # init LookupModule
    lookupModule = LookupModule()

    # setup test terms
    terms = ['/my/path/*.txt', '*.txt']

    # run test
    assert lookupModule.run(terms, global_args) == ['playbooks/files/foo.txt']
    assert lookupModule.run(terms, global_args, wantlist=True) == ['playbooks/files/foo.txt']

# Generated at 2022-06-13 13:51:47.491557
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible import context
    import ansible.constants as C
    context.CLIARGS = {}
    context.CLIARGS['module_path'] = None
    context.CLIARGS['tree'] = None
    context.CLIARGS['roles_path'] = None
    context.CLIARGS['inventory'] = None
    context.CLIARGS['syntax'] = None
    context.CLIARGS['connection'] = None
    context.CLIARGS['forks'] = None
    context.CLIARGS

# Generated at 2022-06-13 13:52:00.662497
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Assume we have a file named 'foo' in directory '.temp/files/'
    test = LookupModule()
    test.set_options(wantlist=True, _terms=["/home/user/.temp/files/foo"])
    test_run = test.run(terms=["foo"], variables={'hostvars':{'group1':["host"]}})
    assert test_run == [u'/home/user/.temp/files/foo']

    # Assume we do not have a file named 'foo' in directory '.temp/files_none/'
    test = LookupModule()
    test.set_options(wantlist=True, _terms=["home/user/.temp/files_none/foo"])