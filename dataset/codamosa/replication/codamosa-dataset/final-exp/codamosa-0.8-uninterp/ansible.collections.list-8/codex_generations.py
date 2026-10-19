

# Generated at 2022-06-12 20:53:45.481325
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible import context
    from ansible.cli import CLI
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    b_testroot = to_bytes(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    b_namespace = to_bytes('ansible_namespace')
    b_collection = to_bytes('collection1')
    b_coll_dir = os.path.join(b_testroot, b_namespace, b_collection)

# Generated at 2022-06-12 20:53:48.071828
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    expected_paths = ["./something/valid"]
    coll_paths = list_valid_collection_paths(expected_paths)
    for path in coll_paths:
        assert path in expected_paths


# Generated at 2022-06-12 20:53:55.272914
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_paths = [
        # just path
        "/a/path",
        # windows path with drive
        "c:/a/windows/path",
        # /not/a/real/path
        "/not/a/real/path",
        # relative path that doesn't exist
        "./not/a/relative/path",
    ]

    coll_paths = list(list_valid_collection_paths(search_paths=test_paths))

    assert len(test_paths) == len(coll_paths)
    assert "/a/path" in coll_paths
    assert "c:/a/windows/path" in coll_paths
    assert "./not/a/relative/path" in coll_paths
    assert "/not/a/real/path" not in coll_paths
    coll_

# Generated at 2022-06-12 20:54:07.351460
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths() with a number of found and non-found paths.
    """

    # 1) First try with a path that does not exist
    coll_paths = ["/tmp/notexist/ansible_collections"]

    res = list_valid_collection_paths(coll_paths)
    assert len(res) == 0

    # 2) Second, try with a path that exists, but it's not a directory.
    coll_paths = ["/tmp/notexist/ansible_collections", "/tmp/nodir"]

    open("/tmp/nodir", 'a').close()

    res = list_valid_collection_paths(coll_paths)
    assert len(res) == 0

    # 3) Third, try with a path that exists, and it's a directory

# Generated at 2022-06-12 20:54:18.926727
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = '/usr/share/ansible/collections:/usr/share/ansible1/collections:/usr/share/ansible2/collections:/usr/share/ansible-collections:/usr/share/ansible-collections1:/usr/share/ansible-collections2:/etc/ansible/collections'
    print("All collection paths found")
    for path in list_collection_dirs():
        print(path)

    print("All collection paths found, filtered with namespace 'azure_preview_modules'")
    for path in list_collection_dirs(coll_filter='azure_preview_modules'):
        print(path)

    print("All collection paths found, filtered with collection name 'community.azure'")

# Generated at 2022-06-12 20:54:30.317091
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils import basic

    collection_paths = [
        os.path.join(basic.modlib.BASE_MODULE_DATA_PATH, 'ansible_collections/foo_namespace'),
        os.path.join(basic.modlib.BASE_MODULE_DATA_PATH, 'ansible_collections/bar_namespace'),
    ]

    search_paths = list_collection_dirs(collection_paths)
    assert search_paths.next() == os.path.join(basic.modlib.BASE_MODULE_DATA_PATH, 'ansible_collections/foo_namespace/foo_collection/bar_plugin_type')

# Generated at 2022-06-12 20:54:33.801218
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Unit test for function list_collection_dirs"""
    path = "/etc/ansible/collections"
    path_list = [path]
    coll_list = list(list_collection_dirs(path_list))
    assert coll_list == ["/etc/ansible/collections/ansible/test"]


# Generated at 2022-06-12 20:54:39.786183
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    pathlist = [
        '/does/not/exist',
        '/etc/ansible/ansible.cfg',
        '/tmp/ansible_collections/'
    ]

    expected_paths = [
        '/tmp/ansible_collections/'
    ]

    for path in list_valid_collection_paths(pathlist, False):
        if path not in expected_paths:
            assert False



# Generated at 2022-06-12 20:54:50.898512
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    os.mkdir('./test_list_valid_collection_paths')
    os.mkdir('./test_list_valid_collection_paths/test_list_valid_collection_paths')
    os.mkdir('./test_list_valid_collection_paths/test_list_valid_collection_paths/test_list_valid_collection_paths')
    os.mkdir('./test_list_valid_collection_paths/test_list_valid_collection_paths/test_list_valid_collection_paths2')
    os.mkdir('./test_list_valid_collection_paths/test_list_valid_collection_paths2')

# Generated at 2022-06-12 20:55:01.696672
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ["/tmp/ansible_collections"]

    actual_collection_dirs = list(list_collection_dirs(search_paths, None))
    expected_collection_dirs = ["/tmp/ansible_collections/ansible/test_collection_1", "/tmp/ansible_collections/ansible/test_collection_2", "/tmp/ansible_collections/namespace/test_collection_3"]
    assert(actual_collection_dirs == expected_collection_dirs)

    actual_collection_dirs = list(list_collection_dirs(search_paths, 'namespace.test_collection_3'))
    expected_collection_dirs = ["/tmp/ansible_collections/namespace/test_collection_3"]

# Generated at 2022-06-12 20:55:15.869846
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_collection_paths = ['path', '/path', '/path/that/does/not/exist', '/path/that/does/not/exist/']
    test_collection_paths_warn = '/path/that/does/not/exist/'
    test_collection_paths_no_warn = '/path'

    collection_paths_existing = list(list_valid_collection_paths(search_paths=test_collection_paths, warn=True))

    assert collection_paths_existing[0] == test_collection_paths_no_warn
    assert collection_paths_existing[1] == test_collection_paths_no_warn


# Generated at 2022-06-12 20:55:20.475291
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/dev/null', '/tmp/nonexist', '/tmp']
    valid_paths = list(list_valid_collection_paths(search_paths, warn=True))

    assert valid_paths == ['/tmp']



# Generated at 2022-06-12 20:55:32.259849
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test default with no input
    path_list = list(list_valid_collection_paths())
    assert '/etc/ansible/collections' in path_list
    assert '~/.ansible/collections' in path_list
    assert './collections' in path_list

    # test with explicit path
    path_list = list(list_valid_collection_paths(['/tmp']))
    assert '/tmp' in path_list

    # test with explicit path and default config
    path_list = list(list_valid_collection_paths(['/tmp'], True))
    assert '/tmp' in path_list
    assert '/etc/ansible/collections' in path_list
    assert '~/.ansible/collections' in path_list
    assert './collections' in path_list

    # test

# Generated at 2022-06-12 20:55:39.550522
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.ansible.tests.unit.compat.mock import patch
    from ansible.collections.ansible.community.plugins.module_utils.ansible_modlib_lzma import (
        ZipFile,
    )
    from ansible.collections.ansible.community.plugins.module_utils.ansible_modlib_lzma import (
        LZMADecompressor,
    )


# Generated at 2022-06-12 20:55:48.698179
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import mkdtemp
    import shutil

    testdir = mkdtemp()
    testnsdir_ansible = os.path.join(testdir, 'ansible_collections', 'ansible')
    testnsdir_temp = os.path.join(testdir, 'ansible_collections', 'temp')
    os.makedirs(os.path.join(testnsdir_ansible, 'nginx'))
    os.makedirs(os.path.join(testnsdir_ansible, 'ssh'))
    os.makedirs(os.path.join(testnsdir_temp, 'nginx'))

    collection_paths = []
    collection_paths.append(testdir)


# Generated at 2022-06-12 20:55:52.080614
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test the function list_valid_collection_paths
    :return: list of collection directory paths
    """
    collection = None
    namespace = None

    collections = defaultdict(dict)
    for path in list_valid_collection_paths(search_paths=['/usr/share/ansible/collections']):
        print(path)

# Generated at 2022-06-12 20:56:02.500844
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils._text import to_bytes
    from collections import defaultdict
    os.path.isdir()
    assert list_collection_dirs(['/tmp']) == []
    os.path.isdir()
    assert list_collection_dirs(['tests']) == [b'ansible_collections/new_namespace/new_collection']
    os.path.isdir()
    assert list_collection_dirs(['tests/fixtures/test_collections']) == [b'ansible_collections/new_namespace/new_collection']
    os.path.isdir()
    assert list_collection_dirs(['tests/fixtures/test_collections/ansible_collections']) == [b'ansible_collections/new_namespace/new_collection']

# Generated at 2022-06-12 20:56:06.675180
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    collection_dir_list = []

    my_dir_list = list_collection_dirs(search_paths=[], coll_filter="test.test_collection")

    for this_dir in my_dir_list:
        collection_dir_list.append(this_dir)

    assert len(collection_dir_list) == 1
    assert collection_dir_list[0].endswith('/ansible_collections/test/test_collection')

# Generated at 2022-06-12 20:56:09.884104
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = list_valid_collection_paths(warn=False)

    assert len(search_paths) == len(AnsibleCollectionConfig.collection_paths)

# Generated at 2022-06-12 20:56:21.095216
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile

    # create temp dir
    b_tmpdir = to_bytes(tempfile.mkdtemp(prefix='collections-test'))
    os.rmdir(b_tmpdir)

    os.makedirs(os.path.join(b_tmpdir, to_bytes('ansible_collections', 'utf-8'), to_bytes('mycollection', 'utf-8')))

    os.makedirs(os.path.join(b_tmpdir, to_bytes('ansible_collections', 'utf-8'), to_bytes('test', 'utf-8')))

    test_paths = [b_tmpdir, os.path.join(b_tmpdir, to_bytes('ansible_collections', 'utf-8'))]


# Generated at 2022-06-12 20:56:33.797232
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils._text import to_text
    from ansible.collections import load_collection_filter

    all_collections = load_collection_filter(None)
    os_collections = load_collection_filter('os')
    os_redhat_collections = load_collection_filter('os.redhat')

    dirs = list(list_collection_dirs())
    assert len(dirs) == len(all_collections)

    dirs = list(list_collection_dirs(coll_filter='os'))
    assert len(dirs) == len(os_collections)

    dirs = list(list_collection_dirs(coll_filter='os.redhat'))
    assert len(dirs) == len(os_redhat_collections)

# Generated at 2022-06-12 20:56:38.915903
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dirs = list(list_collection_dirs(search_paths=['../test/data/list_collections']))
    assert len(dirs) == 3
    assert b'../test/data/list_collections/ansible_collections/namespace1/collection1' in dirs
    assert b'../test/data/list_collections/ansible_collections/namespace2/collection2' in dirs

# Generated at 2022-06-12 20:56:45.652420
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # testing with a list of paths
    p = ['/path/does/not/exist', '/etc/ansible/collections']
    result = list_valid_collection_paths(search_paths=p, warn=False)
    assert next(result) == '/etc/ansible/collections'

    # testing with the default paths
    result = list_valid_collection_paths(warn=False)
    # Checking that one of the default paths is returned (not all of them)
    assert any(p in next(result) for p in AnsibleCollectionConfig.collection_paths)

    # testing with a path that exists but is a file
    p = ['/usr/bin/python']
    result = list_valid_collection_paths(search_paths=p, warn=False)

# Generated at 2022-06-12 20:56:55.031586
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = [
        '/tmp/collections1',
        '/tmp/collections2',
        '/tmp/collections3',
        '/tmp/collections4',
        '/tmp/collections5'
    ]

    assert len(list(list_collection_dirs(search_paths))) == 0

    # create valid collection directories in the /tmp directory
    namespace = 'test'
    collection = 'foo'
    coll_filter = 'test.foo'

    # create all valid paths to test function
    os.makedirs('/tmp/collections1/ansible_collections/test/foo')
    os.makedirs('/tmp/collections2/test/foo')
    os.makedirs('/tmp/collections3/notansible_collections/test/foo')
    os.maked

# Generated at 2022-06-12 20:57:06.201448
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test the function.
    :return:
    """

    # Test with non-existing dir.
    test_path_1 = ['/tmp/doesnotexist']
    for path in list_valid_collection_paths(test_path_1, warn=True):
        print("test_path_1 found: %s" % path)

    # Test with non-existing dir.
    test_path_2 = ['/usr/local/share/ansible_collections']
    for path in list_valid_collection_paths(test_path_2, warn=True):
        print("test_path_2 found: %s" % path)

    # Test with non-existing dir.
    test_path_3 = ['doesnotexist']

# Generated at 2022-06-12 20:57:13.388231
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp/does_not_exist/', '/does/not/either', '/etc/ansible/collections', '/etc/ansible/']
    expected = ['/etc/ansible/collections', '/etc/ansible/']
    assert list(list_valid_collection_paths(search_paths)) == expected
    # Without warn, does not display warnings
    assert list(list_valid_collection_paths(search_paths, warn=False)) == expected
    # Warn shows warnings
    assert list(list_valid_collection_paths(search_paths, warn=True)) == expected



# Generated at 2022-06-12 20:57:19.746125
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    This test requires that the collection paths exist and the collections are in place
    """
    import tempfile
    import shutil

    # create paths
    tmpdir = tempfile.mkdtemp()
    tmpcolldir = os.path.join(tmpdir, 'ansible_collections')
    os.makedirs(tmpcolldir)

    # create namespace
    tmpnamespacedir = os.path.join(tmpcolldir, 'foo')
    os.makedirs(tmpnamespacedir)

    # create collection
    tmpcollectiondir = os.path.join(tmpnamespacedir, 'bar')
    os.makedirs(tmpcollectiondir)

    collection_paths = [tmpcolldir]

    # test all collections
    collection_paths = [tmpcolldir]
    coll_filter = None
    coll_path

# Generated at 2022-06-12 20:57:22.266147
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Wont be populated until AnsibleCollectionConfig is initialized :(
    search_paths = AnsibleCollectionConfig.collection_paths
    display.debug("Collection paths: %s" % search_paths)

    collections = list(list_collection_dirs(search_paths))
    display.debug("Collections: %s" % collections)

# Generated at 2022-06-12 20:57:25.370197
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dirs = list(list_collection_dirs())
    assert len(dirs) >= 2
    assert os.path.isdir(dirs[0])
    assert os.path.isdir(dirs[1])

# Generated at 2022-06-12 20:57:30.190476
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/dev/null', '/does/not/exist']) == []
    assert '/tmp' in list_valid_collection_paths(['/does/not/exist', '/tmp'])
    assert '~' in list_valid_collection_paths()



# Generated at 2022-06-12 20:57:49.784124
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    result = list_collection_dirs(coll_filter='namespace.collection_name')
    for path in result:
        assert path.endswith(b'ansible_collections/namespace/collection_name')

# Generated at 2022-06-12 20:57:59.780942
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import pytest
    from ansible.utils.collection_loader import list_valid_collection_paths
    import os

    # Check with empty search path
    assert list(list_valid_collection_paths([])) == list(AnsibleCollectionConfig.collection_paths)

    # Check with bogus path
    # since we cannot create a bogus path for unit tests, we will test if a path is not in the search path
    # this is valid test
    assert not os.path.exists('/tmp/bogus/ansible_collections')
    assert '/tmp/bogus' not in list(list_valid_collection_paths(['/tmp/bogus']))

    # Check with valid path

# Generated at 2022-06-12 20:58:04.680584
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        '/no/such/path',
        '/etc/ansible/my_collection_config.yml'
    ]

    assert list_valid_collection_paths(search_paths, warn=True) == []



# Generated at 2022-06-12 20:58:10.042496
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths([])).__len__() == AnsibleCollectionConfig.collection_paths.__len__()

    assert list(list_valid_collection_paths(['/tmp'], warn=True)).__len__() == 0

    assert list(list_valid_collection_paths(['nothing_here'], warn=True)).__len__() == 0

    assert list(list_valid_collection_paths(['/etc/passwd'], warn=True)).__len__() == 0

    assert list(list_valid_collection_paths(['/dev'], warn=True)).__len__() == 0

# Generated at 2022-06-12 20:58:18.490984
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Unit test for function `list_valid_collection_paths`
    """
    import shutil
    import tempfile
    from ansible.module_utils._text import to_text

    # Create a local temp directory
    tmp_dir = tempfile.mkdtemp()
    tmp_dir2 = os.path.join(tmp_dir, 'AnSiBlE_cOlLeCtIoNs')
    tmp_dir3 = to_text(tmp_dir, errors='surrogate_or_strict')

    # Add it to the collection paths
    search_paths = [
        tmp_dir2,
        tmp_dir3,
    ]

    # Check that the directory is properly listed
    test_paths = list_valid_collection_paths(search_paths, warn=False)
    assert tmp_dir

# Generated at 2022-06-12 20:58:29.371219
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = [
        'test/unit/roles/bar',
        'test/unit/roles/foo']
    # collection_filter == None
    collections = list_collection_dirs(search_paths)
    assert collections is not None
    assert set(collections) == set(['foo.bar', 'test.test'])
    # collection_filter == 'foo.bar'
    collections = list_collection_dirs(search_paths, 'foo.bar')
    assert collections == ['foo.bar']
    # collection_filter == 'foo'
    collections = list_collection_dirs(search_paths, 'foo')
    assert collections == ['foo.bar']
    # No valid collection path
    collections = list_collection_dirs(['foo'])
    assert collections == []

# Generated at 2022-06-12 20:58:38.995491
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    b_my_collections = to_bytes(os.path.join(os.getcwd(), 'test/unit/ansible_collections'))
    dirs = list_collection_dirs(b_my_collections)
    assert len(dirs) == 2
    assert to_bytes(os.path.join(b_my_collections, 'namespace1', 'collection1')) in dirs
    assert to_bytes(os.path.join(b_my_collections, 'namespace2', 'collection2')) in dirs
    assert to_bytes(os.path.join(b_my_collections, 'namespace3', 'collection3')) not in dirs

# Generated at 2022-06-12 20:58:44.692261
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    config = ['/existing/path', '/another/path', '/non/existing/path']
    paths = list(list_valid_collection_paths(config))
    assert '/existing/path' in paths
    assert '/another/path' in paths
    assert '/non/existing/path' not in paths



# Generated at 2022-06-12 20:58:48.444460
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    This is a test to ensure the list of valid collection paths is working as expected.
    """
    test_paths = ['/path/does/not/exist',
                  '/test/test_collections']
    search_paths = list(list_valid_collection_paths(test_paths))

    assert len(search_paths) == 1
    assert search_paths[0] == '/test/test_collections'


# Generated at 2022-06-12 20:58:51.082659
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/path/that/does/not/exist']) == []
    assert list_valid_collection_paths([]) != []

# Generated at 2022-06-12 20:59:17.416422
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test empty list
    #================
    assert list_valid_collection_paths() == AnsibleCollectionConfig.collection_paths

    # Test list with a single invalid path
    #=====================================
    assert list(list_valid_collection_paths(["/tmp/invalid_search_path"])) == []

    # Test list with a single existing path
    #======================================
    assert list(list_valid_collection_paths(["/usr/share/ansible/ansible_collections"])) == ["/usr/share/ansible/ansible_collections"]

    # Test list with a single existing path and a invalid path
    #==========================================================

# Generated at 2022-06-12 20:59:28.105115
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os

    orig_cwd = os.getcwd()

    # create tmp dir
    temp_dir = tempfile.mkdtemp()
    temp_dir = os.path.normpath(temp_dir)
    # create collection dir tree
    coll_root = os.path.join(temp_dir,"test_collection")

    coll_namespace_dir1 = os.path.join(coll_root,"test1_namespace")
    coll_namespace_dir2 = os.path.join(coll_root,"test2_namespace")

    coll1_plugin1_dir = os.path.join(coll_namespace_dir1,"test_plugin1","plugins","modules")

# Generated at 2022-06-12 20:59:31.843453
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = ["/tmp", "~/.ansible/collections"]
    for path in list_valid_collection_paths(paths):
        if path in paths:
            paths.remove(path)

    assert(len(paths) == 0)



# Generated at 2022-06-12 20:59:33.365255
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list_collection_dirs()
    assert not list_collection_dirs(coll_filter='foo')

# Generated at 2022-06-12 20:59:37.456582
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(search_paths=["/dev/null", "./tests/units/data/collection_paths", "/no/such/path"]) == ["/dev/null", "./tests/units/data/collection_paths"]

# Generated at 2022-06-12 20:59:45.085895
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Generate expected answers for list_valid_collection_paths
    :return:
    """

    # use list to capture text of what is displayed in warning
    warning = []

    display.display = lambda x: warning.append(x)
    display.warning = lambda x: warning.append(x)

    # preset defaults, so we can test warnings
    search_paths = ['/will/not/exist', '/neither/will/this']
    search_paths.extend(AnsibleCollectionConfig.collection_paths)

    # Add some data to the test paths, to make sure we don't fail on returning all paths
    os.makedirs('/valid/collections/path/ansible_collections')

# Generated at 2022-06-12 20:59:52.783992
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''
    Verify we list out valid paths for collections
    '''

    # expect three paths
    paths = list(list_valid_collection_paths(["/no/such/path/here", "/no/such/path/here2", "test/data/test_collections"]))
    assert len(paths) == 3

    # expect three paths, first time is cached, second time is from cache
    paths = list(
        list_valid_collection_paths(["/no/such/path/here", "/no/such/path/here2", "test/data/test_collections"]))
    assert len(paths) == 3

    # expect two paths
    paths = list(list_valid_collection_paths(["/no/such/path/here", "test/data/test_collections"]))

# Generated at 2022-06-12 21:00:03.146120
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # create temp dirs for this test
    for test_dir in ['a', 'b', 'c']:
        os.mkdir(test_dir)

    # create the testing files
    test_file_paths = ['abc', 'bcd', 'cde']

    for test_file in test_file_paths:
        with open(test_file, 'w') as f:
            f.write('')

    # test if search_paths set to None and warn set to false
    result_lst = list(list_valid_collection_paths(None, False))
    assert result_lst == [], result_lst

    # test if search_paths set to empty and warn set to false
    result_lst = list(list_valid_collection_paths([], False))
    assert result_lst

# Generated at 2022-06-12 21:00:14.269176
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test default path (is existing)
    search_paths = [os.path.join(os.path.dirname(__file__), '../../../collections/ansible_collections')]
    results = list(list_valid_collection_paths(search_paths))
    assert results == search_paths

    # test missing path
    results = list(list_valid_collection_paths(['/tmp/foobar123']))
    assert results == []

    # test not-a-directory path
    results = list(list_valid_collection_paths(['/tmp/test_list_valid_collection_paths']))
    assert results == []

    # test multiple paths, some missing, some not-a-directory

# Generated at 2022-06-12 21:00:25.656876
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test case 1: search_paths list is none
    search_paths = None
    path_list_strings = list(list_valid_collection_paths(search_paths))
    assert path_list_strings is not None

    # test case 2: search_paths list has one valid path string
    search_paths = ["/etc"]
    path_list_strings = list(list_valid_collection_paths(search_paths))
    assert path_list_strings is not None

    # test case 3: search_paths list has one valid path string and one invalid path string
    search_paths = ["/etc", "/etc_invalid"]
    path_list_strings = list(list_valid_collection_paths(search_paths))
    assert path_list_strings is not None



# Generated at 2022-06-12 21:01:00.552554
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test for collection name with single namespace.
    # Test for collection name with multiple namespaces.
    # Test for random collection name.
    # Test for random collection name with multiple namespaces.
    # TODO: Add unit tests for these scenarios.
    pass

# Generated at 2022-06-12 21:01:10.134534
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    x = list_collection_dirs(search_paths=['/tmp/test_path'], coll_filter='my_namespace.my_collection')
    assert list(x) == [b'/tmp/test_path/ansible_collections/my_namespace/my_collection']

    # get all collections in namespace
    x = list_collection_dirs(search_paths=['/tmp/test_path'], coll_filter='my_namespace')
    assert list(x) == [b'/tmp/test_path/ansible_collections/my_namespace/my_collection_1',
                       b'/tmp/test_path/ansible_collections/my_namespace/my_collection_2']

    # get all from group of namespaces

# Generated at 2022-06-12 21:01:12.649016
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    cur_dir = os.path.dirname(__file__)
    base_dir = os.path.join(cur_dir, 'fixtures', 'collections')
    coll_path = os.path.join(base_dir, 'collection_root')
    search_paths = [coll_path]
    coll_filter = 'namespaced.collection'
    dirs = list(list_collection_dirs(search_paths, coll_filter))
    assert len(dirs) == 1
    assert dirs[0].endswith(coll_filter)



# Generated at 2022-06-12 21:01:22.770927
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test 1, one non-existent path, one valid path
    search_paths = [
        '/var/tmp/notexist1',
        '/var/tmp/notexist2',
        '/etc/ansible/roles',
        '/var/tmp/notexist3',
    ]

    paths = list_valid_collection_paths(search_paths)

    assert len(paths) == 1
    assert paths[0] == '/etc/ansible/roles'

    # Test 2, one non-existent path, no valid paths found
    search_paths = ['/var/tmp/notexist1', '/var/tmp/notexist2']

    paths = list_valid_collection_paths(search_paths)

    assert len(paths) == 0



# Generated at 2022-06-12 21:01:34.221336
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import pytest
    from ansible.utils.display import Display
    from ansible.errors import AnsibleError

    display = Display()

    def test_load_fixtures(tmpdir):
        tmpdir = str(tmpdir)
        # create a simple structure that lists a collection directory and a non-collection directory
        os.makedirs(os.path.join(tmpdir, "ansible_collections", "test_coll", "ns_a"))
        os.makedirs(os.path.join(tmpdir, "ansible_collections", "test_coll", "ns_b"))
        os.makedirs(os.path.join(tmpdir, "non_coll_dir"))
        # list of collection directories that should be found

# Generated at 2022-06-12 21:01:34.756885
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    pass

# Generated at 2022-06-12 21:01:43.331314
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    tmp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp_dir, 'ansible_collections'))

    os.mkdir(os.path.join(tmp_dir, 'ansible_collections', 'a'))
    os.mkdir(os.path.join(tmp_dir, 'ansible_collections', 'a', 'b'))

    tmp_config_path = os.path.join(tmp_dir, 'ansible.cfg')
    with open(tmp_config_path, 'wt') as f:
        f.write("[defaults]\n")
        f.write("collections_paths=%s\n" % tmp_dir)


# Generated at 2022-06-12 21:01:56.488014
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # This is just a small sample unit test for list_collection_dirs
    # to verify it is working properly. Should be expanded to cover
    # more cases.

    # This is the directory that contains all of our test collections
    test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "test", "units",
                            "utils", "ansible_collections")

    # This is the path we expect the collections to be found at
    test_path = os.path.join(test_dir, "ansible_collections")

    # This is the default path that list_collection_dirs searches
    # We need it here so we can remove it from the path list to simulate
    # the user not specifying a custom path for list_collection_dirs
    default_path = next

# Generated at 2022-06-12 21:02:06.282478
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test the return value of list_collection_dirs for a variety of inputs
    """
    import os
    import tempfile
    import unittest

    class TestCollectionPaths(unittest.TestCase):

        def test_list_collection_dirs_single_path(self):

            def generate_collections_dir(namespace_dir, collections):

                for coll in collections:
                    collection_dir = os.path.join(namespace_dir, coll)
                    os.mkdir(collection_dir)

            tempdir = tempfile.TemporaryDirectory()


# Generated at 2022-06-12 21:02:09.457959
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    results = list(list_collection_dirs(coll_filter="ansible_collections.not_a_valid_path"))
    assert results == []



# Generated at 2022-06-12 21:02:45.479956
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # find path where collections are being run, test_utils
    test_utils_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    test_collections_path = os.path.join(test_utils_path, 'test_collections')

    # Use the test_collections dir and the valid collection paths to test listing the collection dirs

# Generated at 2022-06-12 21:02:50.939375
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """Test non-Linux paths are returned."""
    search_paths = ['/foo/bar', '/foo/bar/baz']
    result = list_valid_collection_paths(search_paths, warn=False)
    assert next(result) == '/foo/bar'
    with pytest.raises(StopIteration):
        next(result)


# Generated at 2022-06-12 21:02:59.767511
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    paths = list_collection_dirs(search_paths=["./meta/readme/test"], coll_filter="namespace.collection")
    assert paths

    paths = list_collection_dirs(search_paths=["./meta/readme/test"], coll_filter="namespace")
    assert paths

    paths = list_collection_dirs(search_paths=["./meta/readme/test"], coll_filter="bad.collection")
    assert not paths

    paths = list_collection_dirs(search_paths=["./meta/readme/test"], coll_filter="bad")
    assert not paths

    paths = list_collection_dirs(search_paths=["./meta/readme/test"])
    assert paths


# Generated at 2022-06-12 21:03:02.033434
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_paths = list_valid_collection_paths()
    assert valid_paths is not None

# Generated at 2022-06-12 21:03:13.739502
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    search_path = ['/Users/jgoerzen/playground/ansible/ansible_collections_bad_subdir',
                   '/Users/jgoerzen/playground/ansible/ansible_collections_missing_subdir',
                   '/Users/jgoerzen/playground/ansible/ansible_collections/',
                   '/Users/jgoerzen/playground/ansible/ansible_collections_bad_subdir/ansible_collections',
                   '/Users/jgoerzen/playground/ansible/ansible_collections_missing_subdir/ansible_collections',
                   '/Users/jgoerzen/playground/ansible/ansible_collections_bad_subdir/ansible_collections/'
                   ]

# Generated at 2022-06-12 21:03:17.512774
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    #  FIXME: these paths are invalid on windows
    test_search_paths = ['/usr/share/ansible/ansible_collections', '/usr/share/ansible']

    found = list(list_collection_dirs(test_search_paths))

    assert found

# Generated at 2022-06-12 21:03:24.677371
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile
    import getpass
    import sys

    temp_path = tempfile.mkdtemp(prefix="ansible_test", dir=os.getcwd())

    temp_path_ansible_collections = os.path.join(temp_path,"ansible-collections")

    namespaces = ["namespace1","namespace2"]
    collections = list()
    for namespace in namespaces:
        collections.append(["collection1","collection2"])

    for idx, namespace in enumerate(namespaces):
        os.mkdir(os.path.join(temp_path_ansible_collections, namespace))
        for collection in collections[idx]:
            os.mkdir(os.path.join(temp_path_ansible_collections, namespace, collection))

# Generated at 2022-06-12 21:03:32.881624
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # test with an empty search path
    test_coll_dirs = list_collection_dirs(search_paths=[])
    assert len(list(test_coll_dirs)) == 0

    # test with a valid search path
    test_coll_dirs = list_collection_dirs(search_paths=["../test/data/valid_collections/collections"])
    assert len(list(test_coll_dirs)) == 2
    # test with an invalid search path
    test_coll_dirs = list_collection_dirs(search_paths=["../test/data/invalid_collections/collections"])
    assert len(list(test_coll_dirs)) == 0
    # test with a valid namespace