

# Generated at 2022-06-13 13:42:06.150059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    a = lookup.run(terms = ["*.yml"], inject = {
        'ansible_search_path': ['.'],
        'role_path': '.'
    } )
    assert len(a) > 0

    b = lookup.run(terms = ["*.yml"], inject = {
        'ansible_search_path': None,
        'role_path': None
    } )
    assert len(b) == 0

    c = lookup.run(terms = ["*.yml"], inject = {
        'ansible_search_path': ['.'],
        'role_path': None
    } )
    assert len(c) > 0

# Generated at 2022-06-13 13:42:15.971511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Case1:
    #Input:
    #terms(list) = ["*.txt"]
    #Output:
    #_list(list) = ["/my/path/1.txt","/my/path/2.txt","/my/path/3.txt"]

    terms = ["*.txt"]
    ret = []
    term_file = os.path.basename(terms[0])
    found_paths = []
    if term_file != terms[0]:
        found_paths.append(os.path.dirname(terms[0]))
    else:
        found_paths.append(os.getcwd())

# Generated at 2022-06-13 13:42:17.100072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:42:29.777849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test normal case

    # TODO: use Mock, not os.path.isfile
    # add some mock files in current path dir
    os.system("echo test > testfile.txt")
    os.system("echo test > testfile.log")
    os.system("mkdir -p testdir")
    os.system("echo test > testdir/testfile.conf")

    # create a LookupModule object
    lm = LookupModule()

    # no .txt file, just .log
    terms = ['testfile.txt']
    # call the run method without ansible
    # no variables, so no search_path
    results = lm.run(terms)
    # should be []
    assert not results

    # no .txt file, just .log
    terms = ['testfile.log']
    # call the run

# Generated at 2022-06-13 13:42:32.129537
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm
    terms = ["/home/foo"]
    results = lm.run(terms)
    assert(len(results) == 0)

# Generated at 2022-06-13 13:42:39.488512
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    lookup = LookupModule()
    # create temp directory
    on_disk_path = tempfile.mkdtemp(dir=os.getcwd())

    # create test files
    file_names = ['test_foo', 'test_bar', 'test_baz', 'test_foo_test']
    for f in file_names:
        full_path = os.path.join(on_disk_path, f)

        # create temporary file
        with open(full_path, "w") as fd:
            fd.write(f)

    # test three files matching pattern 'test_foo*' in directory
    pattern = "test_foo*"

# Generated at 2022-06-13 13:42:46.846804
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.fileglob import LookupModule
    lookup_plugin = LookupModule()

    # Unit test without fail
    terms = ['test_fileglob.py']
    ret = lookup_plugin.run(terms, None)
    assert ret == ['test_fileglob.py']

    # Unit test with fail
    terms = ['test_fileglob.py', 'fake_file']
    with pytest.raises(AnsibleFileNotFound):
        ret = lookup_plugin.run(terms, None)

# Generated at 2022-06-13 13:42:56.917835
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import StringIO

    lookup = LookupModule()
    fixtures = {}

    def fake_find_file_in_search_path(variables, *args, **kwargs):
        return fixtures['fake_find_file_in_search_path']

    lookup.find_file_in_search_path = fake_find_file_in_search_path
    lookup.set_options({})
    lookup.basedir = '/home/ansible'

    fixtures['fake_find_file_in_search_path'] = '/home/ansible'
    data = lookup.run(terms=[os.path.join('/home/ansible', 'test')], variables={})

# Generated at 2022-06-13 13:43:01.380962
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(["Makefile.am"], {}) == []
    assert lm.run(["*"], {}) != []
    assert lm.run(["**"], {}) != []

# Generated at 2022-06-13 13:43:06.173549
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    args = {
        "terms": [
            "/test/directory/*",
            "/test/directory2/*"
        ]
    }
    returned = lookup.run(**args)
    print(returned)
    assert returned == ["/test/directory/test.txt", "/test/directory2/test.txt"]

# Generated at 2022-06-13 13:43:08.964775
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(True)

# Generated at 2022-06-13 13:43:16.645639
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_fileglob = LookupModule()
    # Test case 1:
    # Return files matching given term
    term = ['*.txt']
    result = lookup_fileglob.run(terms=term, variables={
        'ansible_basedir': os.path.join(os.path.dirname(__file__), 'test_data'),
        'ansible_search_path': [
            os.path.join(os.path.dirname(__file__), 'test_data'),
        ]
    })
    assert result == [
        'test_data/test_fileglob.txt'
    ]

    # Test case 2:
    # Return files matching given term
    # for provided path in relative to ansible_basedir
    term = ['test_1/*.txt']

# Generated at 2022-06-13 13:43:17.381057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:43:27.439391
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    class Object(object):
        pass
    variable = Object()
    variable.get_basedir = lambda self: './test/test_files/'
    variable.find_file_in_search_path = lambda self, variables, path, name: './test/test_files/'
    variable.ansible_search_path = ['./test/test_files/']
    terms = ['1.txt']
    ret = lookup_module.run(terms, variable)
    assert ret == ['./test/test_files/1.txt']
    terms = ['*.txt']
    ret = lookup_module.run(terms, variable)

# Generated at 2022-06-13 13:43:39.025888
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Declare test terms and variables
    terms = [ "/my/*path/*.txt" ]
    variables = { "ansible_search_path": "./.test_lookup_plugins" }

    # Create a LookupModule object
    lookup = LookupModule()

    # Perform unit test for method run of class LookupModule
    result = lookup.run(terms, variables)

    # Assert results match expectation
    assert result[0] == "./.test_lookup_plugins/my/path/foo.txt"

    # Bad Terms
    terms = [ "/my/*path/*.txt", None ]
    result = lookup.run(terms, variables)
    assert result[0] == "./.test_lookup_plugins/my/path/foo.txt"
    assert result[1] == None

    # Check with bad path

# Generated at 2022-06-13 13:43:40.907884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansibleLookupModule = LookupModule()
    ansibleLookupModule.run('/my/path/*.txt')
    print('test')

# Generated at 2022-06-13 13:43:48.677109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Run the test process for class LookupModule.run
    '''
    fileglob = LookupModule()
    # Load with unix directory separator
    windows_separator_paths = [
        u'c:/path/to/file.txt'
    ]
    paths = fileglob.run(windows_separator_paths, variables = None, wantlist = False)
    assert paths, 'paths should not be empty'
    assert paths[0] == windows_separator_paths[0], "paths should be {}, but it is {}".format(windows_separator_paths[0], paths[0])

    # Load with windows directory separator
    windows_separator_paths = [
        u'c:\\path\\to\\file.txt'
    ]
    paths = fileglob

# Generated at 2022-06-13 13:43:58.833557
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of TestClass. This will be passed to the method testMethod as the first argument 'self'
    # 'test' is not a standard python id. It is used to differentiate the 'testMethod' and 'assertEqual' method names
    test = LookupModule()

    # Use the assertEqual method to verify that the expected and actual values are equal
    # retrieve method names from the instance 'test'
    test.assertEqual(test.get_basedir({}), './')
    test.assertEqual(test.find_file_in_search_path(None, 'files', './file.py'), './file.py')

    # Verify case where file not found

# Generated at 2022-06-13 13:44:05.004190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # h = Hello()
    lookup = LookupModule()
    terms = ['/my/path/*.txt', '/my/*.txt']
    variables = {
        'ansible_search_path': ['/my/path'],
    }
    assert lookup.run(terms, variables) == [
        '/my/path/test.txt', '/my/path/test2.txt'
    ]

# Generated at 2022-06-13 13:44:06.397718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    assert sys.version_info[0] == 3

# Generated at 2022-06-13 13:44:15.467824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''using a fake file system in memory'''
    import pytest
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible import context


# Generated at 2022-06-13 13:44:25.831744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.fileglob import LookupModule
    import os
    import tempfile
    import shutil
    import pytest

    dirname = tempfile.mkdtemp()
    shutil.rmtree(dirname, ignore_errors=True)


# Generated at 2022-06-13 13:44:36.526312
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = __import__('ansible.plugins.lookup.fileglob', fromlist=["LookupModule"]).LookupModule()

    assert lookup_module.run(["invalid_dir/aasdf.txt"], variables={'ansible_search_path': ['']}) == []
    assert lookup_module.run(["plugins/test/data/aasdf.txt"], variables={'ansible_search_path': ['']}) == ["plugins/test/data/aasdf.txt"]
    assert lookup_module.run(["invalid_dir/aasdf.txt"], variables={'ansible_search_path': [''], 'myvar': 'plugins/test/data/aasdf.txt'}) == []

# Generated at 2022-06-13 13:44:43.398301
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import unittest
    import shutil
    import tempfile
    from ansible.errors import AnsibleFileNotFound
    from ansible.plugins.lookup import LookupModule

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            # Make a temporary directory, and write files therein
            self.dir = tempfile.mkdtemp(dir=os.getcwd())
            results = ['1.txt', '2.txt', '3.txt']
            self.results = []
            for r in results:
                self.results.append(os.path.join(self.dir, r))
                with open(os.path.join(self.dir, r), 'wb') as f:
                    f.write(b'foo')

# Generated at 2022-06-13 13:44:50.614766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    import ansible.constants as C

    DATA_DIR = os.environ['A_TEST_DATA_DIR']
    fixtures_path = os.path.join(DATA_DIR, 'fixtures')
    TEST_DIRECTORY = os.path.join(fixtures_path, 'test_file_lookup_plugin')
    assert os.path.isdir(TEST_DIRECTORY)

    options = {"verbosity": 0, "inventory": InventoryManager(loader=DataLoader(), sources=[fixtures_path + "/hosts"])}

# Generated at 2022-06-13 13:44:52.821290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['*.txt'], inject={'ansible_search_path' : ['.']}) == ["test_file.txt"]

# Generated at 2022-06-13 13:45:02.353570
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 13:45:15.297229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __main__
    __main__.file_name="LookupModule_run.py"
    __main__.__file__="LookupModule_run.py"
    lookup = LookupModule()
    lookup.set_options({})

    # Non-relative path
    ret = lookup.run(["/etc/asdf.conf"], {"ansible_search_path": [ "/etc" ]})
    assert ret == ["/etc/asdf.conf"]

    # Relative path
    ret = lookup.run(["etc/asdf.conf"], {"ansible_search_path": [ "/foo" ]})
    assert ret == ["/foo/etc/asdf.conf"]

    # Non-existent relative path

# Generated at 2022-06-13 13:45:20.972918
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/my/path/*.txt', '*.txt']
    # terms = ['/my/path/*.txt']
    results = []
    lookup_instance = LookupModule()
    results.extend(lookup_instance.run(terms))
    return results

# Generated at 2022-06-13 13:45:24.540318
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    x = lu.run(['version.ini'],{})
    assert len(x)>0
    assert 'version.ini' in x[0]

# Generated at 2022-06-13 13:45:40.451359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Verifies correct results for specific input.
    lookup = LookupModule()

    # Test path with a single directory.
    paths = ['tests/static/', 'tests']
    results = lookup.run(paths, dict())
    assert results == ["tests/static/play_hosts"]

    # Test path with a mix of directories and files.
    paths = ['tests/static', 'tests/static/play_hosts']
    results = lookup.run(paths, dict())
    assert results == ["tests/static/play_hosts"]

    # Test path with a file and directory that has no glob match.
    paths = ['tests/static', 'tests/static/doesntexist']
    results = lookup.run(paths, dict())
    assert results == []

# Generated at 2022-06-13 13:45:51.763233
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, None, None).run(["./file_with_spaces.txt", "./file_without_spaces.txt"], {'role_path': ['../']}) == ["../files/file_with_spaces.txt", "../files/file_without_spaces.txt"]
    assert LookupModule(None, None, None).run(["file_with_spaces.txt", "file_without_spaces.txt"], {'role_path': ['../']}) == ["../files/file_with_spaces.txt", "../files/file_without_spaces.txt"]

# Generated at 2022-06-13 13:45:57.386013
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = ['/etc/hosts*']
    variables = None

    ret = lm.run(terms, variables)

    assert ret[0] == '/etc/hosts'
    assert len(ret) == 1

# Generated at 2022-06-13 13:46:03.340023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # we need to fake a class for the module import
    class FakeVarsModule():
        def __init__(self):
            self.ansible_search_path = ['tests/unit']
            self.ansible_basedir = os.path.dirname(__file__)

    lookup_module = LookupModule()
    result = lookup_module.run(['*.py'], variables=FakeVarsModule())
    assert result == ['__init__.py', 'test_lookup_fileglob.py'], result

# Generated at 2022-06-13 13:46:08.506832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([]) == []
    assert lookup_module.run('non_matching_baby') == []

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 13:46:13.096632
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    search_path = (
        "{0}/tests/test_utils/roles/test_collections/ansible_collections/nsantos/t_collection/tasks/files".format(os.getcwd())
    )
    lookup_module.run([search_path])

# Generated at 2022-06-13 13:46:16.798170
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup = lookup_loader.get('fileglob')
    assert lookup.run(['./test/test_fileglob.py']) == ['./test/test_fileglob.py']

# Generated at 2022-06-13 13:46:24.854794
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a dict to use as variables
    test_var = dict()
    # Create a copy of LookupModule and pass variables to it
    test_lookup = LookupModule()
    test_lookup.set_options(variables=test_var)
    # Create a path to a directory containing files that match the wildcard *
    test_term = '/tmp/test_fileglob/*'
    # Run the run method using the created path
    result = test_lookup.run(terms=[test_term])
    # Assert that the result of the run method is 
    # a list with 1 or more items
    assert(len(result) >= 1)

# Generated at 2022-06-13 13:46:32.019617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First test
    l = LookupModule()
    test_terms = ["/my/path/*.txt"]
    expected_result = ['test.txt']
    result = l.run(test_terms)

    # check result
    assert result == expected_result

    # Second test
    l = LookupModule()
    test_terms = ["/my/path/*.txt"]
    expected_result = ['test.txt']
    result = l.run(test_terms)

    # check result
    assert result == expected_result

# Generated at 2022-06-13 13:46:46.147796
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TEST CASE 1: List files matching a given pattern on dir
    module = LookupModule()
    result = module.run(
        [
            'Test/data/fileglob/input/*.*',
        ],
        dict(),
    )
    assert(
        result ==
        [
            'Test/data/fileglob/input/file1.txt',
            'Test/data/fileglob/input/file2.txt',
        ]
    )

    # TEST CASE 2: List files matching a given pattern on dir and subdir
    module = LookupModule()
    result = module.run(
        [
            'Test/data/fileglob/input/**/*.txt',
        ],
        dict(),
    )

# Generated at 2022-06-13 13:47:23.777063
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test of method run of LookupModule class.
    """
    # Create an instance of class LookupModule
    lm = LookupModule()
    # Create an instance of class PluginLoader
    pl = PluginLoader()
    # Create an instance of class LookupBase
    lb = pl.get('lookup', 'fileglob')
    # Create a variable
    variable = {'ansible_search_path': ['.']}
    # Run the method run of class LookupModule
    ret = lm.run(["test_LookupModule_run.py"], variable)
    assert ret == ['./test_LookupModule_run.py']

# Generated at 2022-06-13 13:47:25.196108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement
    return

# Generated at 2022-06-13 13:47:33.195511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test term_file != term
    term='path/to/terms/*.txt'
    ret = lookup.run([term], {'ansible_search_path':['path/to', 'path/to/terms']})
    assert ret == ['path/to/terms/test.txt']

    # Test term_file == term
    term='*.txt'
    ret = lookup.run([term], {'ansible_search_path':['path/to', 'path/to/terms']})
    assert ret == ['path/to/terms/test.txt']

# Generated at 2022-06-13 13:47:46.037877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    mock_self = type('', (), {})()
    mock_self.get_basedir = lambda variables: '/playbooks'

    # mock the glob module
    def mock_glob(path):
        if path == '/playbooks/files/fooapp/*':
            return ['/playbooks/files/fooapp/foofile1', '/playbooks/files/fooapp/foofile2']
        elif path == '/playbooks/files/README':
            return ['/playbooks/files/README']
        elif path == '/playbooks/*.txt':
            return ['/playbooks/README.txt', '/playbooks/mock_self.txt']
        elif path == '/playbooks/bad/mock_self.txt':
            return []

# Generated at 2022-06-13 13:47:57.480075
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing /playbooks/files dir
    terms = ['/playbooks/files/file1.txt', '/playbooks/files/file2.txt']
    ret = LookupModule().run(terms)
    assert(ret == ['/playbooks/files/file1.txt', '/playbooks/files/file2.txt'])

    # Testing /playbooks/files dir for *.txt pattern
    terms = ['/playbooks/files/*.txt']
    ret = LookupModule().run(terms)
    assert(ret == ['/playbooks/files/file1.txt', '/playbooks/files/file2.txt', '/playbooks/files/file3.txt'])

    # Testing /playbooks/files dir for *.md pattern
    terms = ['/playbooks/files/*.md']
    ret = LookupModule().run(terms)

# Generated at 2022-06-13 13:48:10.848878
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize the LookupModule
    lookup = LookupModule()

    # Create a Dummy class for testing
    class DummyClass(object):
        pass

    # Create a new variable object
    variables = DummyClass()

    # Create a new variable object
    basedir = '/'

    # Set default value of the variable basedir
    variables.basedir = basedir

    # Create a list of terms
    terms = ['playbooks/files/fooapp/*']

    # Run the function run of the lookup module
    res = lookup.run(terms, variables=variables, wantlist=True)

    # Check the result returned by run of the lookup module

# Generated at 2022-06-13 13:48:18.849988
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # We are using a file called "test_module.py"
    test_module_path = os.path.join(os.path.dirname(__file__), "test_module.py")
    expected_result = [test_module_path]
    result = lookup_module.run([os.path.basename(test_module_path)], variables={"ansible_search_path": [os.path.dirname(test_module_path)]})
    assert result == expected_result
    assert result == [os.path.join(os.path.dirname(__file__), "test_module.py")]

# Generated at 2022-06-13 13:48:30.437985
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Syntax : lookup.run(terms, variables=None, **kwargs)

    # empty list of terms
    result = lookup.run([])
    assert result == []

    # terms list with one path
    result = lookup.run(['/my/path/*.txt'])
    assert result == []

    f = open('/my/path/sample.txt', 'w')
    f.write('sample content')
    f.close()

    # terms list with one path
    result = lookup.run(['/my/path/*.txt'])
    assert result == ['/my/path/sample.txt']

    # no wildcard given
    result = lookup.run(['/my/path/sample.txt'])
    assert result == ['/my/path/sample.txt']

# Generated at 2022-06-13 13:48:41.265710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, ['/etc/hosts']) == ['/etc/hosts']
    assert LookupModule.run(None, ['/etc/hosts.d/hosts']) == ['/etc/hosts.d/hosts']
    assert LookupModule.run(None, ['/etc/hosts*']) == []
    assert LookupModule.run(None, ['/etc/.*']) == []
    assert LookupModule.run(None, ['/etc/hosts']) == ['/etc/hosts']
    assert LookupModule.run(None, ['/etc/hosts.d/*']) == []
    assert LookupModule.run(None, ['/etc/hosts.d/hosts']) == ['/etc/hosts.d/hosts']

# Generated at 2022-06-13 13:48:52.953729
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instance of the LookupModule class
    l = LookupModule()

    # construct a list of valid file paths
    valid_file_paths = ['/path/to/file1', '/path/to/file2', '/path/to/file3']

    # construct a list of invalid file paths
    invalid_file_paths = ['', '.', '/path/to/dir1', '/path/to/dir2/']

    # construct a list of valid file patterns
    valid_file_patterns = ['file1', 'file1*', 'file[12]*']

    # construct a list of invalid file patterns
    invalid_file_patterns = ['file*', 'file1*file2*']

    # test for all valid file patterns and all valid file paths

# Generated at 2022-06-13 13:49:18.423525
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Testing run of class LookupModule")
    assert LookupModule().run(["*.txt"], variables={"ansible_search_path": ["/tmp"]}) == []

# Generated at 2022-06-13 13:49:30.516864
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    module_args = dict(terms=['*.yml'])
    module_path_src_file = os.path.join(os.path.dirname(__file__), '..', '..', 'module_utils')
    module_path_dst_file = os.path.join(os.path.dirname(__file__), '..', '..', 'module_utils', 'module_utils')
    os.symlink(module_path_src_file, module_path_dst_file)

    def setup(tempdir):
        testdir = os.path.join(tempdir, 'tests/')
        if not os.path.exists(testdir):
            os.makedirs(testdir)

       

# Generated at 2022-06-13 13:49:40.643410
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/my/path/*.txt']
    variables = {'ansible_search_path': ['test/data']}
    assert LookupModule().run(terms, variables=variables) == [u'../test/data/my/path/bar.txt', u'../test/data/my/path/foo.txt']
    terms = ['*.txt']
    assert LookupModule().run(terms, variables=variables) == [u'../test/data/bar.txt', u'../test/data/dir/test.txt', u'../test/data/foo.txt']
    terms = ['*.tsv']
    assert LookupModule().run(terms, variables=variables) == [u'../test/data/foo.tsv']
    terms = ['non-existing-file']

# Generated at 2022-06-13 13:49:50.657811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lm = LookupModule()
    lm.set_options({'first': True})

    # Test a normal fileglob
    mock_loader = MockLoader({
        "ansible_search_path": [],
    })
    ansible_search_path = [os.path.join(os.path.dirname(__file__), 'fixtures', 'fileglob')]
    terms = [os.path.join(os.path.dirname(__file__), 'fixtures', 'fileglob', '*.txt')]
    ret = lm._run(terms, mock_loader, ansible_search_path=ansible_search_path)
    assert(len(ret) == 2)
    assert(ret[0] == 'file1.txt')

# Generated at 2022-06-13 13:50:06.552214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import shutil

    lookup = LookupModule()
    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-13 13:50:07.099260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 13:50:10.532654
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    path = "test"
    assert lookup.run([path]) == [path]

# Generated at 2022-06-13 13:50:20.935057
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    path_1 = '/path/to/file.conf'
    path_2 = '/path/to/file_2.conf'
    term = '*.conf'
    paths = ['.', '/path/to', '/path/to/']

    # GIVEN a lookup module that returns a list of paths
    lookup_module_instance = LookupModule()

    # WHEN 3 paths are found from term (path is a file)
    found_paths = lookup_module_instance._get_search_path(variables={}, basedir=paths[1], term=path_1)

    # THEN it should be 3 paths in the result
    assert len(found_paths) == 3

    # WHEN 2 paths are found from term (path is a directory)

# Generated at 2022-06-13 13:50:32.465502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleFileNotFound
    from ansible.parsing.vault import VaultLib
    test = LookupModule()

# Generated at 2022-06-13 13:50:43.218617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests that 'fileglob' returns value as expected
    # Method: run
    # Params: test_paths, test_variables, kwargs
    # Return Value: ret
    # Expected: 'fileglob' returns expected value
    # See also: LookupModule class
    # See also: https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/fileglob.py

    # basename part of the test data
    ret = []
    term_file = "test*.txt"

    # create a dummy file to use for lookup
    # to test glob return
    fh = open("/tmp/test.txt.0", "w")
    fh.close()

    fh = open("/tmp/test.txt.1", "w")
   

# Generated at 2022-06-13 13:51:32.866054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import shutil
    import sys

    # Path to directory of this file
    path = os.path.dirname(os.path.realpath(__file__))

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary python module
    module = tempfile.mkstemp('.py', 'ansible_module_')[1]
    shutil.copy(path + '/ansible_test_fileglob.py', module)

    # Add temporary directory to import path
    sys.path.append(tmpdir)

    # Import temporary python module
    from ansible_test_fileglob import LookupModule

    # Initialize LookupModule class as obj
    obj = LookupModule()

    # Create a test directory

# Generated at 2022-06-13 13:51:37.105217
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("\nUnit Test: fileglob lookup")
    test_instance = LookupModule()
    print("\nResult of fileglob lookup is: "+str(test_instance.run(['/etc/shadow'])))

if __name__ == '__main__':
    print("\nUnit Test: fileglob lookup")
    test_LookupModule_run()

# Generated at 2022-06-13 13:51:41.500017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of LookupModule to test run method
    test_class = LookupModule()
    # Test with invalid term
    result = test_class.run(['/tmp/test_file.txt'], variables=None, wantlist=True)
    assert result == []

# Generated at 2022-06-13 13:51:54.472530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    fullpath = os.path.realpath(__file__)
    dir_content = os.listdir(os.path.dirname(fullpath))
    # Test 1: Test with a valid file term
    terms = [__file__]
    result = lookup_module.run(terms, variables=None, **{})
    assert result == [to_text(fullpath, errors='surrogate_or_strict')]
    # Test 2: Test with a valid file term and wantlist=True
    terms = [__file__]
    result = lookup_module.run(terms, variables=None, **{'wantlist': True})
    assert result == [to_text(fullpath, errors='surrogate_or_strict')]
    # Test 3: Test with an invalid file term
