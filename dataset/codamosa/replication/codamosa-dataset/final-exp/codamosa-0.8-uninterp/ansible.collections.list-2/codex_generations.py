

# Generated at 2022-06-12 20:53:43.282609
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Path that does not exist
    assert list(list_valid_collection_paths(search_paths=['/this/does/not/exist'], warn=True)) == []

    # Path that exists but is not a directory
    test_not_dir = os.path.join(gen_append_to_basedir(__file__, 'path/to/not/dir'))
    assert list(list_valid_collection_paths(search_paths=[test_not_dir], warn=True)) == []

    # Path that exists, is a directory and looks like a collection
    test_coll_dir = os.path.join(gen_append_to_basedir(__file__, 'path/to/valid/collection/dir'))

# Generated at 2022-06-12 20:53:46.061763
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_path = ['/home/bogus/path/to/roles', 'roles']
    list_collection_dirs(search_path)


# Generated at 2022-06-12 20:53:50.605638
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert ['my/collections/path', '/etc/ansible/collections'] == list(list_valid_collection_paths(['my/collections/path', '/etc/ansible/collections']))
    assert ['/etc/ansible/collections'] == list(list_valid_collection_paths())
    assert [] == list(list_valid_collection_paths(['my/collections/path', '/my/collections/path']))

# Generated at 2022-06-12 20:53:58.348488
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for function list_collection_dirs
    :return: None
    """

# Generated at 2022-06-12 20:54:01.040376
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list_collection_dirs(coll_filter='test.a') != list_collection_dirs()

# Generated at 2022-06-12 20:54:03.693290
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(["foobar1234567890"])) == []
    # TODO: add additional tests

# Generated at 2022-06-12 20:54:11.519370
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()

    # create dir for collection
    coll_path = os.path.join(tmpdir, "test.test")
    os.mkdir(coll_path)

    # create dir for non-collection
    not_coll_path = os.path.join(tmpdir, "test.test2")
    os.mkdir(not_coll_path)

    # create dir for config
    config_path = os.path.join(tmpdir, "test.test3")
    os.mkdir(config_path)

    # create non-existant dir
    not_exist_path = os.path.join(tmpdir, "test.test4")

    # create not a dir

# Generated at 2022-06-12 20:54:16.767256
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    display.verbosity = 2

    test_paths = ['/file1', '/does_not_exist/file2', '/dir/file3']
    valid_paths = list(list_valid_collection_paths(test_paths))

    assert len(valid_paths) == 1
    assert '/dir' in valid_paths



# Generated at 2022-06-12 20:54:26.622609
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert len(list(list_valid_collection_paths(['/tmp']))) == 1
    assert len(list(list_valid_collection_paths(['/tmp', '/tmp']))) == 1
    assert len(list(list_valid_collection_paths(['/tmp/notarealdir']))) == 0
    assert len(list(list_valid_collection_paths(['/etc', '/tmp']))) == 1
    assert len(list(list_valid_collection_paths(['/tmp', '/etc']))) == 1

# Generated at 2022-06-12 20:54:32.848559
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test empty list
    search_paths = []
    result = list_valid_collection_paths(search_paths)
    assert(len(list(result)) > 0)

    # test one present path
    result = list_valid_collection_paths(["/tmp"])
    assert("/tmp" in result)

    # test one not present path
    result = list_valid_collection_paths(["/tmp/not-really-here"])
    assert("/tmp/not-really-here" not in list(result))

# Generated at 2022-06-12 20:54:50.538367
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    ansible_collection_dir = tempfile.mkdtemp()
    ansible_collections_1 = tempfile.mkdtemp()
    ansible_collections_2 = tempfile.mkdtemp()
    shutil.copytree(ansible_collection_dir, ansible_collections_1)
    shutil.copytree(ansible_collection_dir, ansible_collections_2)

    shutil.rmtree(ansible_collection_dir)
    os.mkdir(ansible_collection_dir)
    os.mkdir(os.path.join(ansible_collection_dir, "ansible_collections"))
    ansible_collection_dir = os.path.join(ansible_collection_dir, "ansible_collections")

    # Invalid collection directory structure


# Generated at 2022-06-12 20:54:58.709538
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    collection_paths = [
        '/usr/share/ansible/collections',
        '/opt/ansible/collections',
        '~/ansible/collections']

    valid_collection_paths = list(list_valid_collection_paths(collection_paths))
    assert valid_collection_paths == [
        '/usr/share/ansible/collections',
        '/opt/ansible/collections',
        os.path.expanduser('~/ansible/collections')
    ]

# Generated at 2022-06-12 20:55:05.957452
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible_collections.ansible.foo.bar import collection_info_noext
    from ansible_collections.ansible.foo.baz import collection_info_noext
    from ansible_collections.ansible.dummy.plugin import collection_info_noext
    from ansible_collections.ansible.dummy.collection import collection_info_noext

    collection_root = "/tmp/ansible_collections"
    collection_namespaces = {
        'ansible': {
            'foo': {
                'bar': collection_info_noext,
                'baz': collection_info_noext
            },
            'dummy': {
                'collection': collection_info_noext,
                'plugin': collection_info_noext
            }
        }
    }


# Generated at 2022-06-12 20:55:13.581704
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Tests that we get no results if a collection path doesn't exist
    results = [path for path in list_valid_collection_paths(search_paths=['/tmp/nonexistent/path/'])]
    assert len(results) == 0

    # Tests that we get a warning if a provided path doesn't exist
    results = [path for path in list_valid_collection_paths(search_paths=['/tmp/nonexistent/path/'], warn=True)]
    assert len(results) == 0

    # Tests that we get a warning if a configured path doesn't exist
    results = [path for path in list_valid_collection_paths(warn=True)]
    assert len(results) >= 0

# Generated at 2022-06-12 20:55:24.641337
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    from distutils.sysconfig import get_python_lib

    # create fake collections in temp dir and add to search_paths
    ans_cols_path = tempfile.mkdtemp()
    collection_paths = [ans_cols_path]

    fake_cols = {
        'ansible.basic_testing': ['collection_one', 'collection_two'],
        'ansible.advanced_testing': ['collection_one', 'collection_three'],
    }

    for ns_name, colls in fake_cols.items():
        ns_real_path = os.path.join(get_python_lib(), 'ansible', 'collections', ns_name)
        ns_fake_path = os.path.join(ans_cols_path, ns_name)


# Generated at 2022-06-12 20:55:27.968742
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert 'ansible_collections.ansible.builtin' in list(list_collection_dirs(search_paths=["../test/data/collections/ansible_collections"]))



# Generated at 2022-06-12 20:55:35.556068
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_paths = ['./test/units/modules/utils/fixtures/test_collection_paths', './test/units/modules/utils/fixtures/test_collection_paths_missing']
    test_coll_filter = 'test_ns.test_coll'
    dirs = list_collection_dirs(test_paths, test_coll_filter)
    for dir in dirs:
        assert os.path.isfile(os.path.join(dir, 'module_utils', 'log.py'))

# Generated at 2022-06-12 20:55:45.214352
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp()
    ansible_coll_dir = os.path.join(temp_dir, 'ansible_collections')
    os.mkdir(ansible_coll_dir)
    os.mkdir(os.path.join(ansible_coll_dir, 'my_ns'))
    os.mkdir(os.path.join(ansible_coll_dir, 'my_ns', 'my_coll'))
    os.mkdir(os.path.join(ansible_coll_dir, 'my_ns', 'my_coll', 'plugins'))
    os.mkdir(os.path.join(ansible_coll_dir, 'my_ns', 'my_coll', 'plugins', 'modules'))

# Generated at 2022-06-12 20:55:47.241978
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths()) == AnsibleCollectionConfig.collection_paths



# Generated at 2022-06-12 20:55:53.879179
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile
    import shutil

    tmp_path = tempfile.mkdtemp()
    test_ns = 'testns'
    test_coll = 'testcoll'


# Generated at 2022-06-12 20:56:11.937111
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    base_dir = tempfile.mkdtemp()

    namespace_dir = os.path.join(base_dir, "ansible_collections", "my_namespace")
    collection_dir = os.path.join(namespace_dir, "my_collection")
    os.makedirs(collection_dir)

    namespace_dir_alias = os.path.join(base_dir, "ansible_collections", "my_namespace_alias")
    collection_dir_alias = os.path.join(namespace_dir_alias, "my_collection_alias")
    os.makedirs(collection_dir_alias)

    collection_dir_dupe = os.path.join(namespace_dir_alias, "my_collection")

    # test_namespace_no_collection
    list_of_

# Generated at 2022-06-12 20:56:21.196992
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    my_cwd = os.getcwd()
    my_collection_paths = [my_cwd]
    my_collection_dirs = list(list_collection_dirs(search_paths=my_collection_paths))
    # remove the current working directory prefix
    my_collection_dirs = [os.path.relpath(coll_dir, start=my_cwd) for coll_dir in my_collection_dirs]
    assert len(my_collection_dirs) == 1, "Expected to find 1 collection directory at {}".format(my_cwd)
    assert my_collection_dirs[0] == 'ansible_collections/ansible/test_collection'

# Generated at 2022-06-12 20:56:32.054992
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    try:
        import __main__ as main  # noqa - F821
        # mock string used to test if path is warning is displayed
        if main.__file__.endswith('unit/utils/collection_loader.py'):
            warn_string = ''
        else:
            warn_string = 'The configured collection path {0} does not exist.\n'
    except:
        warn_string = ''

    # Test list that contains one non-existing path
    mylist = ['/tmp', '/usr', '/noexist']
    mylist_filtered = list(list_valid_collection_paths(mylist, warn=True))
    assert(len(mylist_filtered) == 2)
    assert(warn_string == display.warning.call_args_list[0][0][0])


# Generated at 2022-06-12 20:56:43.032782
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    tests function list_valid_collection_paths

    :return:
    """
    os.path.abspath = lambda x: x
    os.path.exists = lambda x: True
    os.path.isdir = lambda x: True
    assert list(list_valid_collection_paths(['a', 'b'])) == ['a', 'b']

    os.path.abspath = lambda x: x
    os.path.exists = lambda x: False
    os.path.isdir = lambda x: True
    assert list(list_valid_collection_paths(['a', 'b'])) == []

    os.path.abspath = lambda x: x
    os.path.exists = lambda x: False
    os.path.isdir = lambda x: False

# Generated at 2022-06-12 20:56:46.739323
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/invalid/path', '/tmp', '/bin']
    assert len(list(list_valid_collection_paths(search_paths))) == 2


# Generated at 2022-06-12 20:56:55.682474
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Create a collection directory tree and test against it
    # We do not have a mock filesystem available yet.
    import tempfile
    base_temp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(base_temp_dir, 'ansible_collections'))
    os.mkdir(os.path.join(base_temp_dir, 'ansible_collections', b'mycollection'))
    os.mkdir(os.path.join(base_temp_dir, 'ansible_collections', b'mycollection', b'mycollection'))
    os.mkdir(os.path.join(base_temp_dir, 'ansible_collections', b'mycollection', b'mycollection', b'plugins'))

# Generated at 2022-06-12 20:56:59.499076
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert to_bytes('/root/test') in list_valid_collection_paths([to_bytes('/root/test')])



# Generated at 2022-06-12 20:57:08.111416
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [
        '/home/someuser/mycolls',
        '/home/someuser/mycolls/namespace1',
        '/home/someuser/mycolls/namespace2',
    ]
    itr = list_collection_dirs(paths)
    assert next(itr) == '/home/someuser/mycolls/namespace1'
    assert next(itr) == '/home/someuser/mycolls/namespace2'
    assert next(itr) == '/home/someuser/mycolls/namespace1'
    assert next(itr) == '/home/someuser/mycolls/namespace2'
    with pytest.raises(StopIteration):
        next(itr)

# Generated at 2022-06-12 20:57:17.542872
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-12 20:57:29.780359
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    This tests with collections in both the common 'ansible_collections' directory
    as well as in the 'collection' directory.
    """
    collection_roots = [
        'test/units/module_utils/collection_loader/test_data/ansible_collections',
        'test/units/module_utils/collection_loader/test_data/collection',
    ]

    # test with an empty filter (return everything)
    collection_dirs = list_collection_dirs(collection_roots)
    collected_dirs = [dir for dir in collection_dirs]
    assert len(collected_dirs) == 2

    # test with a simple filter (return everything)
    collection_dirs = list_collection_dirs(collection_roots, 'example')

# Generated at 2022-06-12 20:57:47.772351
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from test.utils import temp_dir, remove_tmp_dir
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins

    test_name = 'test_list_valid_collection_paths'
    test_path = os.path.join(temp_dir, test_name)
    test_subpath_1 = os.path.join(test_path, 'subpath1')
    test_subpath_2 = os.path.join(test_path, 'subpath2')

    # Test that the function warns when a configured collection path does not exist
    def mock_warning(string, *args, **kwargs):
        raise AssertionError("Unexpected call to display.warning: %s" % string)


# Generated at 2022-06-12 20:57:58.177924
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test the default
    assert list(list_valid_collection_paths())

    assert list(list_valid_collection_paths(['/non/existing/path'])) == []

    assert list(list_valid_collection_paths(['/non/existing/path'], warn=True)) == []
    assert list(list_valid_collection_paths(['/etc/passwd'])) == []
    assert list(list_valid_collection_paths(['/etc/passwd'], warn=True)) == []
    assert list(list_valid_collection_paths(['/usr/bin'])) == []
    assert list(list_valid_collection_paths(['/usr/bin'], warn=True)) == []

    assert list(list_valid_collection_paths(['/bin'])) == ['/bin']

# Generated at 2022-06-12 20:58:08.199008
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''Ensure collection_paths are filtered properly'''
    from ansible.module_utils.common.collections import list_valid_collection_paths
    from ansible.utils.path import unfrackpath

    results = list(list_valid_collection_paths())

    assert results is not None
    assert len(results) > 0

    # add some paths and check them
    from ansible.module_utils.common.collections import AnsibleCollectionConfig
    b_path = to_bytes(unfrackpath(__file__), errors='surrogate_or_strict')
    b_base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(b_path))))

# Generated at 2022-06-12 20:58:12.480079
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_collection_paths = list(list_valid_collection_paths(['/foo/bar','/good/path/here']))
    assert '/foo/bar' not in valid_collection_paths
    assert '/good/path/here' in valid_collection_paths


# Generated at 2022-06-12 20:58:15.421086
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths([
        'does_not_exist',
        '/path/to/somewhere',
        '/does/not/exist',
    ])) == ['/path/to/somewhere']

# Generated at 2022-06-12 20:58:21.462590
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_dirs = list_collection_dirs()

    assert(isinstance(coll_dirs, list))
    assert(len(coll_dirs) > 0)
    assert(coll_dirs[0].endswith('ansible_collections/ansible/netcommon'))

# Generated at 2022-06-12 20:58:22.432995
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list_collection_dirs() != []

# Generated at 2022-06-12 20:58:33.273860
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    non_existing_search_paths = [
        '/a/random/test/path',
        '/a/relative/../test/path'
    ]

    valid_search_paths = [
        'a/relative/path',
        '/a/absolute/path'
    ]

    bad_search_paths = [
        'a/relative/file.txt',
        '/a/absolute/file.txt'
    ]

    for path in list_valid_collection_paths(non_existing_search_paths, warn=True):
        assert False, "Should not have returned a valid path for a non-existing path: {0}".format(path)

    for path in list_valid_collection_paths(valid_search_paths):
        assert path in valid_search_paths


# Generated at 2022-06-12 20:58:42.347727
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collections = list_collection_dirs(["tests/data/collections"])
    # print(list(collections))
    assert list(collections) == [
        b'tests/data/collections/ansible_collections/namespace/collection',
        b'tests/data/collections/ansible_collections/namespace/collection2'
    ]

    collections = list_collection_dirs(["tests/data/collections"], "namespace.collection2")
    # print(list(collections))
    assert list(collections) == [
        b'tests/data/collections/ansible_collections/namespace/collection2'
    ]

    collections = list_collection_dirs(["tests/data/collections"], "namespace.collection")
    # print(list(collections))

# Generated at 2022-06-12 20:58:49.315837
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    path_cwd = os.getcwd()
    path_tmp = '/tmp/ansible_collections'
    path_nonexistent = '/tmp/foo/bar'

    os.makedirs(path_tmp)

    # test default config
    list_valid_collection_paths()

    # test with none existing dir
    assert list_valid_collection_paths([path_tmp, path_nonexistent]) == [path_tmp]

    # test with none existing dir and skip warning
    assert list_valid_collection_paths([path_tmp, path_nonexistent], warn=False) == [path_tmp]

    # test with existing current working dir
    assert list_valid_collection_paths([path_tmp, path_cwd]) == [path_tmp, path_cwd]

    # test with non dir


# Generated at 2022-06-12 20:59:08.858133
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test for valid directory path in supplied list
    test_paths = ['/tmp']
    expected_paths = iter(['/tmp'])
    assert all(a == b for a, b in
               zip(list_valid_collection_paths(search_paths=test_paths), expected_paths))

    # Test for valid directory path in default config
    test_paths = ['/tmp']
    expected_paths = iter(['/tmp'])
    assert all(a == b for a, b in
               zip(list_valid_collection_paths(search_paths=test_paths), expected_paths))

    # Test for multiple valid directory paths
    test_paths = ['/tmp', '/tmp']
    expected_paths = iter(['/tmp', '/tmp'])

# Generated at 2022-06-12 20:59:16.759362
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test filter of invalid paths
    :return: None
    """

    test_paths = [
        "/foo/bar",
        "/etc",
        "/does/not/exist",
        "not/a/path"
    ]

    # FIXME: test should be skipped on Windows for now.
    import platform
    if platform.system() == 'Windows':
        return

    for path in list_valid_collection_paths(test_paths, True):
        assert os.path.exists(path)
        assert os.path.isdir(path)

if __name__ == "__main__":
    test_list_valid_collection_paths()

# Generated at 2022-06-12 20:59:27.622374
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # A collection path
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = 'foo'
    pathlist = list(list_valid_collection_paths())
    assert len(pathlist) == 1
    assert pathlist[0] == os.path.join(os.path.expanduser('~'), 'foo')

    # A collection path with environment variables
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = '$HOME'
    pathlist = list(list_valid_collection_paths())
    assert len(pathlist) == 1
    assert pathlist[0] == os.path.join(os.path.expanduser('~'))

    # A collection paths with environment variables
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = '$HOME:foo'

# Generated at 2022-06-12 20:59:36.591318
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test function list_collection_dirs
    """
    # Get the dirname of this file
    # Add the path to the ansible_collections dir under the current directory
    # and the ansible_collections dir in the parent directory to the search paths
    # Then check to see if the list_collection_dirs() function returns only
    # the ansible_collections dir in the parent directory.
    cur_dir = os.path.dirname(__file__)
    ansible_collections_dir = os.path.join(cur_dir, 'ansible_collections')
    parent_dir = os.path.join(cur_dir, '..')
    parent_ansible_collections_dir = os.path.join(parent_dir, 'ansible_collections')


# Generated at 2022-06-12 20:59:47.458055
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_roots = []
    new_coll_root = os.path.join(os.path.dirname(__file__), "../../test/sanity/collection/ansible_collections")
    coll_roots.append(new_coll_root)
    coll_roots.extend(AnsibleCollectionConfig.collection_paths)
    coll_roots = list_valid_collection_paths(coll_roots)

    b_coll_roots = []
    for coll_root in coll_roots:
        b_coll_roots.append(os.path.join(to_bytes(coll_root), b'ansible_collections'))

    collected_collections = []
    for b_coll_root in b_coll_roots:
        collections = os.listdir(b_coll_root)

# Generated at 2022-06-12 20:59:57.822429
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import os
    import tempfile

    search_path = ['/does_not/exist', '/etc/ansible/does_not/exist/neither']

    # Create a tempfile and directory
    # Give the directory the same name as the tempfile
    tmpfile = tempfile.mkstemp()[1]
    tmpdir = tmpfile
    os.makedirs(tmpdir)

    # Expected to be returned
    search_path.append(tmpfile)
    search_path.append(tmpdir)

    # Expected to not be returned
    search_path.append('/etc/ansible/does_not_exist')

    # Remove the tempfile, leaving the directo

# Generated at 2022-06-12 21:00:09.038366
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Check if list_valid_collection_paths returns a generator
    assert isinstance(list_valid_collection_paths(), type(iter('')))
    # Check that a warning is displayed, if search_path does not exist
    assert list_valid_collection_paths(search_paths=['/path/does/not/exist'], warn=True) is not None
    # Check that a warning is not displayed, if search_path does not exist
    assert list_valid_collection_paths(search_paths=['/path/does/not/exist'], warn=False) is not None
    # Check if list_valid_collection_paths returns list of collection-paths if no search_path is set
    assert list_valid_collection_paths(search_paths=None) is not None
    # Check if list_valid_

# Generated at 2022-06-12 21:00:14.339614
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    coll_paths = ['/foo', '/does/not/exist', '/usr', '/usr/does/not/exist']
    found_paths = list(list_valid_collection_paths(coll_paths))
    assert len(found_paths) == 2
    assert found_paths[0] == '/foo'
    assert found_paths[1] == '/usr'
    assert len(list(list_valid_collection_paths())) == 0



# Generated at 2022-06-12 21:00:25.803077
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for function list_collection_dirs
    :return:
    """

    import tempfile
    import shutil
    import stat

    search_paths = []
    tmp_path = tempfile.mkdtemp()
    search_paths.append(tmp_path)
    coll_path = os.path.join(tmp_path, "ansible_collections", "test")


# Generated at 2022-06-12 21:00:34.660822
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os
    from ansible.module_utils._text import to_bytes

    temp_dir = to_bytes(tempfile.mkdtemp())
    coll_dir_name = to_bytes('ansible_collections')
    ns_dir_name = to_bytes('test_coll')
    coll_dir_name = to_bytes('test.test_coll')
    coll_dir_path = os.path.join(temp_dir, coll_dir_name, ns_dir_name, coll_dir_name)

    # os.makedirs(coll_dir_path)
    # os.makedirs(os.path.join(temp_dir, coll_dir_name, ns_dir_name))
    os.makedirs(coll_dir_path)

# Generated at 2022-06-12 21:01:00.501779
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common.collections import list_valid_collection_paths
    from ansible.module_utils.common.collections import list_collection_dirs

    # collection_paths not defined, only default
    result = list(list_valid_collection_paths())
    assert result == ['/usr/share/ansible/collections'], result

    # temp paths supplied
    result = list(list_valid_collection_paths(search_paths=['/tmp/test']))
    assert result == ['/tmp/test'], result

    # config is still loaded, so should contain both
    result = list(list_valid_collection_paths(search_paths=['/tmp/test'], warn=True))

# Generated at 2022-06-12 21:01:10.094650
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from os.path import join as pjoin

    from tempfile import mkdtemp
    from shutil import rmtree

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.ansible_release import __version__

    path = mkdtemp()

# Generated at 2022-06-12 21:01:21.742383
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_paths = [
        'collection_path1',
        'collection_path2',
        'collection_path3',
        'collection_path4',
        'collection_path5'
    ]
    namespaces = [
        'mynamespace1',
        'mynamespace2',
        'mynamespace3',
        'mynamespace4',
        'mynamespace5'
    ]
    collections = [
        'mycollection1',
        'mycollection2',
        'mycollection3',
        'mycollection4',
        'mycollection5'
    ]

    # no collection paths

# Generated at 2022-06-12 21:01:25.417362
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['/nonexistantpath', '/nonexistantpath'])) == []
    assert list(list_valid_collection_paths(['/nonexistantpath', '/tmp/'])) == ['/tmp/']
    assert list(list_valid_collection_paths(['/nonexistantpath'])) != []

# Generated at 2022-06-12 21:01:36.505319
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Playbook tests for list_collection_dirs"""

    import shutil
    import tempfile
    import sys

    collection_root = tempfile.mkdtemp()


# Generated at 2022-06-12 21:01:39.316766
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_paths = [
        'test/path',
        'another/path',
    ]
    for path in list_valid_collection_paths(search_paths=test_paths, warn=False):
        assert path



# Generated at 2022-06-12 21:01:43.341972
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_path = "test/not_a_path"
    search_paths = [test_path]
    valid_paths = list(list_valid_collection_paths(search_paths, warn=False))

    # There should be no valid paths returned
    assert (len(valid_paths) == 0)



# Generated at 2022-06-12 21:01:56.489185
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test collection name
    coll_name = 'my_collection'

    # Test list collection dir
    def list_coll_dirs(coll_filter=None):
        coll_dirs = []
        for coll_dir in list_collection_dirs(coll_filter=coll_filter):
            coll_dirs.append(coll_dir)
        return coll_dirs

    # Test that we get all colections
    ns1 = 'my_namespace1'
    ns2 = 'my_namespace2'
    coll1 = 'coll1'
    coll2 = 'coll2'
    coll3 = 'coll3'
    coll4 = 'coll4'
    search_path = '/path/to/search'

# Generated at 2022-06-12 21:02:06.281134
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collections = list_collection_dirs(search_paths=['tests/unit/data/collections/ansible_collections'], coll_filter='ansible.windows')

# Generated at 2022-06-12 21:02:09.880371
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    result = list_valid_collection_paths(search_paths=['/not-exist1',
                                                       '/not-exist2',
                                                       '/etc']).__next__()
    assert result == '/etc'

# Generated at 2022-06-12 21:02:29.384241
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    expected = [os.path.join(os.path.sep, u'test', u'ansible_collections', u'ansible', u'test', u'plugins', u'module_utils')]
    result = list(list_collection_dirs([os.path.sep + u'test']))
    assert result == expected

# Generated at 2022-06-12 21:02:37.626425
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    res = list(list_collection_dirs(search_paths=['./unit_test_data/collections/path1', './unit_test_data/collections/path2']))
    assert res == ['./unit_test_data/collections/path1/ansible_collections/name1/coll1',
                   './unit_test_data/collections/path1/ansible_collections/name2/coll2']

# Generated at 2022-06-12 21:02:43.390364
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Absolute paths work
    paths = []
    path1 = '/tmp/path/one'
    path2 = '/tmp/path/two'
    paths.append(path1)
    paths.append(path2)
    for dir in list_collection_dirs(paths):
        assert dir

    # Relative paths work
    paths = []
    path1 = './path/one'
    path2 = './path/two'
    paths.append(path1)
    paths.append(path2)
    for dir in list_collection_dirs(paths):
        assert dir

# Generated at 2022-06-12 21:02:54.135609
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    from ansible.utils.collection_loader import _get_collection_dirs

    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    # Temporary directory and temporary file for tests
    tmpdir = tempfile.mkdtemp()
    f = tempfile.NamedTemporaryFile(dir=tmpdir, delete=False)
    b_tmpdir = to_bytes(tmpdir, errors='surrogate_or_strict')
    b_f = to_bytes(f.name, errors='surrogate_or_strict')

    # create a file that's not a collection directory
    touch(os.path.join(tmpdir, 'test_file.txt'))

    # create the collection directory and a file in it
    os

# Generated at 2022-06-12 21:03:05.082553
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Unit test to ensure list_valid_collection_paths returns correct paths
    """

    test_paths = [
        "/tmp",
        "/tmp/foo",
        "/tmp/foo/bar",
        "/tmp/foo/bar/baz",
    ]

    for test_path in test_paths:
        b_test_path = to_bytes(test_path, errors='surrogate_or_strict')
        os.makedirs(b_test_path)

    display.verbosity = 3
    # Test that all paths get returned with no filters
    paths = list(list_valid_collection_paths(search_paths=test_paths))

    assert len(paths) == len(test_paths)
    assert paths == test_paths

    # Test that all paths get returned with

# Generated at 2022-06-12 21:03:16.757856
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    # create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # create a subdirectory to mimic an official collection dir
    os.makedirs(os.path.join(tmpdir, 'namespace1-collection1'))
    os.makedirs(os.path.join(tmpdir, 'namespace2-collection2'))
    os.makedirs(os.path.join(tmpdir, 'namespace3-collection3'))
    # create a non-collection dir for testing purposes
    os.makedirs(os.path.join(tmpdir, 'not_a_collection'))


# Generated at 2022-06-12 21:03:24.285804
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['/path/to/custom/collections', '/path/to/custom/collections2']
    expected_collections = ['collection_one', 'collection_two']
    collection_dirs = list(list_collection_dirs(search_paths=search_paths))
    assert len(collection_dirs) == 2
    collection_names = sorted([os.path.basename(cd) for cd in collection_dirs])
    assert collection_names == expected_collections

    collection_dirs = list(list_collection_dirs(search_paths=search_paths, coll_filter='namespace.collection_one'))
    assert len(collection_dirs) == 1
    assert collection_dirs[0] == '/path/to/custom/collections/namespace/collection_one'