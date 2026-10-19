

# Generated at 2022-06-13 13:42:07.867872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set the environment for testing
    term = '/path/to/dir/*.cfg'
    basedir = '/path/to/dir/'
    paths = ['/playbooks/files/fooapp']

    # Set the return data
    ret = [ '/path/to/dir/config1.cfg', '/path/to/dir/config2.cfg' ]

    # Mock the glob library
    import __builtin__
    _glob_mock = __builtin__.glob
    __builtin__.glob = lambda x: ['/path/to/dir/config1.cfg', '/path/to/dir/config2.cfg']

    # Mock the os.path library
    _path_isfile_mock = os.path.isfile
    os.path.isfile = lambda x: True

    # Run the test


# Generated at 2022-06-13 13:42:13.240369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms=['/test/test.py'], variables=dict(ansible_search_path=['./test']))
    assert result == ['./test/test.py']

    result = lookup_plugin.run(terms=['test.py'], variables=dict(ansible_search_path=['./test']))
    assert result == ['./test/test.py']

# Generated at 2022-06-13 13:42:22.823865
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, None).run(["/tmp/does_not_exist"]) == []
    assert LookupModule(None, None).run(["/etc/passwd"]) == [u'/etc/passwd']
    assert LookupModule(None, None).run(["/tmp/*"]) == []
    assert LookupModule(None, None).run(["/bin/sh"]) == [u'/bin/sh']
    assert LookupModule(None, None).run(["/bin/sh", "/etc/passwd"]) == [u'/etc/passwd', u'/bin/sh']

# Generated at 2022-06-13 13:42:30.205488
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [['/path/to/file1.txt'],['/path/to/file2.txt']]
    variables = {'ansible_search_path':['/path/to/files']}
    results = lookup.run(terms, variables)
    assert results == ['/path/to/files/file1.txt', '/path/to/files/file2.txt']

# Generated at 2022-06-13 13:42:32.471261
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(['.gitignore']) == [u'/home/ansible/.gitignore']

# Generated at 2022-06-13 13:42:37.362454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # LookupModule.run() method is protected(i.e. _run), and so cannot be tested.
    # The assert and print statement below is placed just to remind that this method is not tested.
    assert True

# Generated at 2022-06-13 13:42:48.943796
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a dummy ansible variable (path)
    ansible_Variable = {'ansible_search_path':['./a/', './b/']}
    # Create a dummy term (filename)
    term = 'random*.txt'
    # Create an instace of lookupmodule
    lookupmodule = LookupModule()
    # Mock a method to return a result
    lookupmodule.find_file_in_search_path = MagicMock(return_value=None)
    # Run the run() method ansible_Variable = {'ansible_search_path':['./a/', './b/']}
    globbed_result = lookupmodule.run(terms = [term], variables = ansible_Variable)
    # Assert the result
    assert globbed_result == []

    # Create a dummy ansible variable (path)


# Generated at 2022-06-13 13:42:51.354557
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms=['/my/path/*.txt']
    variables=None
    got = module.run(terms,variables)
    assert got == []

# Generated at 2022-06-13 13:42:59.542431
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    lm = LookupModule()
    lm.set_options({})
    terms = ['/playbooks/files/fooapp/*']
    variables = {'ansible_search_path': ['/playbooks']}
    found_paths = ['/playbooks/files']

    # mock
    glob_mock = 'glob'
    os_path_mock = 'os.path'
    lm_find_file_in_search_path_mock = 'lookup_plugin.find_file_in_search_path'

    mock_target = __import__(glob_mock)
    mock_target = getattr(mock_target, 'glob')
    mock_target = getattr(mock_target, 'glob')
    orig_glob = mock_target

    mock_

# Generated at 2022-06-13 13:43:01.899585
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['/my/path/*.txt']) == []

# Generated at 2022-06-13 13:43:10.021204
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import stat
    import tempfile
    import shutil

    # Create temporary directory and files
    test_dir = tempfile.mkdtemp()
    test_file1 = os.path.join(test_dir, 'file1.txt')
    test_file2 = os.path.join(test_dir, 'file2.txt')
    test_file3 = os.path.join(test_dir, 'file3a.txt')
    test_file4 = os.path.join(test_dir, 'file3b.txt')
    test_file5 = os.path.join(test_dir, 'file4.doc')

    # Create the files
    for test_file in [test_file1, test_file2, test_file3, test_file4, test_file5]:
        os.close

# Generated at 2022-06-13 13:43:19.311764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests passing no terms
    lu = LookupModule()
    assert lu.run(terms=[], wantlist=True) == []

    # Tests passing different terms
    lu = LookupModule()
    assert lu.run(terms=['/my/path/*.txt'], wantlist=True) == []

    # Tests passing existing file paths
    lu = LookupModule()
    assert lu.run(terms=['README.md'], wantlist=True) == [os.path.abspath('README.md')]

# Generated at 2022-06-13 13:43:28.680518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    lookup = LookupModule()
    terms = [os.path.join(test_dir, '..', '..', '..', 'examples', 'ansible.cfg')]
    result = lookup.run(terms, variables={'role_path': [test_dir]})
    assert len(result) == 1
    assert result[0] == os.path.join(test_dir, '..', '..', '..', 'examples', 'ansible.cfg')
    terms = [os.path.join(test_dir, '..', '..', '..', 'examples', 'NOTFOUND')]

# Generated at 2022-06-13 13:43:35.993286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def mock_lookupbase_find_file_in_search_path(variables, path, path_dirname):
        return '/my/path'

    lookup = LookupModule()
    lookup.find_file_in_search_path = mock_lookupbase_find_file_in_search_path
    ret = lookup.run(['*.txt'])
    assert ret == []
    assert lookup.find_file_in_search_path.called_with(None, 'files', '')

# Generated at 2022-06-13 13:43:45.893540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for method run of class LookupModule"""
    results = ['/Users/pe/Documents/ansible/test/test_fileglob/test_data/a',
              '/Users/pe/Documents/ansible/test/test_fileglob/test_data/b',
              '/Users/pe/Documents/ansible/test/test_fileglob/test_data/c']

    # test basedir
    basedir = '/test/test_fileglob/test_data'
    cwd = os.getcwd()

# Generated at 2022-06-13 13:43:56.078218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test default behaviour
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, '..')
    path = os.path.join(path, '../examples/')
    terms = ['host_vars', 'roles']
    files = lookup_module.run(terms=terms)
    assert files == [os.path.join(path, 'example.ini')]

    # Test with wantlist=True
    wanted_list = lookup_module.run(terms=terms, wantlist=True)
    assert wanted_list == [os.path.join(path, 'example.ini')]

# Generated at 2022-06-13 13:44:07.441071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''test run method of class LookupModule'''
    f = 'lookup_plugins/fileglob.py'
    lookup = LookupModule()

    # test empty file
    assert lookup.run([f]) == [f]

    # test a file with some words
    f = 'lookup_plugins/test_lookups.py'
    assert lookup.run([f]) == [f]

    # test a pattern
    f = 'lookup_plugins/test_lookups.py*'
    assert lookup.run([f]) == ['lookup_plugins/test_lookups.py', 'lookup_plugins/test_lookups.pyc']

    # test folder
    f = 'lookup_plugins/'
    assert lookup.run([f]) == [f]

    # test pattern in folder

# Generated at 2022-06-13 13:44:12.108228
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['*', 'test/test']
    variables = {}
    assert lookup_module.run(terms, variables, wantlist=True) != []


# Generated at 2022-06-13 13:44:24.520638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert ['/foo/bar/1.txt', '/foo/bar/2.txt', '/foo/baz/1.txt'] == LookupModule(loader=None, basedir=None, runner=None).run(terms=['*.txt'], variables={
        'ansible_search_path': ['/foo/bar', '/foo/baz']
    })
    assert ['/foo/bar/1.txt'] == LookupModule(loader=None, basedir=None, runner=None).run(terms=['*.txt'], variables={
        'ansible_search_path': ['/foo/bar', '/bar/baz']
    })

# Generated at 2022-06-13 13:44:30.202023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    test.get_basedir.return_value = "/playbooks"
    test.find_file_in_search_path.return_value = "/playbooks/files"
    assert test.run(["/my/path/*.txt"], {}, {'wantlist': True}) == ['/my/path/foo.txt', '/my/path/bar.txt']