

# Generated at 2022-06-12 20:53:43.282429
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.ansible.community.tests.unit.mock.plugins.mock_plugins import list_valid_collection_paths

    paths = list(list_valid_collection_paths(search_paths=["/path/does/not/exist", "/path/does/not/exist/either"]))
    assert paths == []

    paths = list(list_valid_collection_paths(search_paths=[os.path.abspath("./")]))
    assert paths == []

    paths = list(list_valid_collection_paths(search_paths=[os.path.abspath("./ansible_collections")]))
    assert paths == ["./ansible_collections"]


# Generated at 2022-06-12 20:53:51.549456
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
    from ansible.collections import azure
    #set up search paths
    collection_search_path = [
        '/home/azure_rm_tools/.ansible/collections',
        '/home/azure_rm_tools/.ansible/plugins'
    ]
    #get a collection dir
    collections = list_collection_dirs(search_paths=collection_search_path, coll_filter=AzureRMModuleBaseExt.__module__)
    for c in collections:
        print(c)
    print(azure.__path__)
    print(AzureRMModuleBaseExt.__module__)

# Generated at 2022-06-12 20:53:58.956686
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    coll_paths = list(list_valid_collection_paths())
    assert isinstance(coll_paths, list)
    assert coll_paths != []

    coll_paths = list(list_valid_collection_paths(coll_paths))
    assert isinstance(coll_paths, list)
    assert coll_paths != []

    coll_paths = list(list_valid_collection_paths(['/noexist/foo/bar']))
    assert isinstance(coll_paths, list)
    assert coll_paths == []

    coll_paths = list(list_valid_collection_paths(['/noexist/foo/bar'], warn=True))
    assert isinstance(coll_paths, list)
    assert coll_paths == []



# Generated at 2022-06-12 20:54:06.439771
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    py.test unit test cases to test the ansible.utils.collection_loader list_valid_collection_paths function
    """

    fake_paths = [
        "/no/such/path",
        "/no/such/path/foo.bar",
        "/etc/passwd",
        "/etc",
    ]

    result = list_valid_collection_paths(fake_paths)
    assert isinstance(result, list)
    assert len(result) == 0



# Generated at 2022-06-12 20:54:11.833067
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Assert that a non-existing path is filtered out
    search_paths = ["/foo/bar", "/tmp/baz"]
    assert ("/foo/bar" in list_valid_collection_paths(search_paths)) is False
    assert ("/tmp/baz" in list_valid_collection_paths(search_paths)) is False
    # Assert that a directory is not filtered out
    search_paths = ["/tmp/ansible_collections"]
    assert ("/tmp/ansible_collections" in list_valid_collection_paths(search_paths)) is True

# Generated at 2022-06-12 20:54:20.871033
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import itertools
    collection_dirs = list(list_collection_dirs(search_paths=["tests/unit/data/collections.unit"], coll_filter="namespace.collection"))
    assert len(collection_dirs) == 1
    assert all(is_collection_path(coll) for coll in collection_dirs)
    assert set(collection_dirs) == set(["tests/unit/data/collections.unit/ansible_collections/namespace/collection"])

    collection_dirs = list(list_collection_dirs(search_paths=["tests/unit/data/collections.unit"], coll_filter="namespace3.collection3"))
    assert len(collection_dirs) == 1
    assert all(is_collection_path(coll) for coll in collection_dirs)

# Generated at 2022-06-12 20:54:31.066920
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile, shutil
    from ansible.utils.collection_loader import list_collection_dirs, list_valid_collection_paths
    from ansible.utils.collection_list import list_collections

    test_collections = [
        ('namespace1.name1', 'namespace1/name1'),
        ('namespace1.name2', 'namespace1/name2'),
        ('namespace2.name1', 'namespace2/name1'),
    ]

    # Create test collection directories
    coll_root = tempfile.mkdtemp()
    for test_coll in test_collections:
        coll_path = os.path.join(coll_root, test_coll[1])
        os.makedirs(coll_path)
        AnsibleCollectionConfig.collection_paths.append(coll_path)

# Generated at 2022-06-12 20:54:42.056265
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test execution under CI
    paths = ['../fixtures/collections_paths']
    result = list(list_valid_collection_paths(search_paths=paths))
    assert result == []

    # Test list_valid_collection_paths

    paths = ['./fixtures/collections_paths']
    result = list(list_valid_collection_paths(search_paths=paths))
    assert 'ansible_collections' in result
    assert 'ansible_collections_inexact' in result
    assert 'ansible_collections_not_dir' not in result
    assert 'ansible_collections_not_dir_text' not in result
    assert 'ansible_collections_missing' not in result

    # Test list_valid_collection_paths without configured path


# Generated at 2022-06-12 20:54:51.222992
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test valid paths
    coll_paths = ['foo/bar', 'baz/qux']
    result = list(list_valid_collection_paths(coll_paths))
    assert result == coll_paths

    # test partial valid paths
    coll_paths = ['foo/bar', 'baz/qux', '/nonexistent/path']
    result = list(list_valid_collection_paths(coll_paths, warn=True))
    assert '/nonexistent/path' not in result
    assert 'foo/bar' in result
    assert 'baz/qux' in result

    # test all invalid paths
    coll_paths = ['/nonexistent/path1', '/nonexistent/path2']

# Generated at 2022-06-12 20:55:00.837397
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader import _collection_finder_class
    cf = _collection_finder_class()
    collection_paths = [cf._load_collection_v1_path()]
    collection_names = [
        'ansible_namespace.collection_name',
        'ansible_namespace.another_collection_name',
        'ansible_namespace.more_collection_names'
    ]
    test_collection_paths = list(list_collection_dirs(collection_paths))
    assert len(test_collection_paths) == len(collection_names)
    for path in test_collection_paths:
        assert os.path.basename(path) in collection_names

# Generated at 2022-06-12 20:55:16.505050
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert set(list_valid_collection_paths()) == set(AnsibleCollectionConfig.collection_paths)

    assert set(list_valid_collection_paths(['/fakepath'])) == set(AnsibleCollectionConfig.collection_paths)

    assert set(list_valid_collection_paths(['/tmp'])) == set([])

    assert set(list_valid_collection_paths(['/tmp'], warn=True)) == set([])

    assert set(list_valid_collection_paths(['/fakepath'], warn=True)) == set(AnsibleCollectionConfig.collection_paths)

    assert set(list_valid_collection_paths(['/tmp', '/fakepath'])) == set(AnsibleCollectionConfig.collection_paths)


# Generated at 2022-06-12 20:55:27.625334
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    #
    # With a temp dir
    #
    test_dir = tempfile.mkdtemp()
    #
    # Namespace 'foo' collection 'bar'
    #
    test_coll_dir = os.path.join(test_dir, 'ansible_collections', 'foo', 'bar')
    os.makedirs(test_coll_dir)
    test_coll_file = os.path.join(test_coll_dir, 'plugins', '__init__.py')
    with open(test_coll_file, 'w') as f:
        pass
    #
    # Namespace 'foo' collection 'baz'
    #
    test_coll_dir = os.path.join(test_dir, 'ansible_collections', 'foo', 'baz')
    os.m

# Generated at 2022-06-12 20:55:33.321206
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(None)
    assert list_valid_collection_paths(["/test", "/foo", "/bar", "/badpath"])
    assert list_valid_collection_paths(["/test", "/foo", "/bar", "/badpath"], warn=True)



# Generated at 2022-06-12 20:55:40.081337
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test empty search_path yields no results
    assert list(list_collection_dirs(search_paths=[])) == []

    # Test no search_path yields default
    assert len(list(list_collection_dirs(search_paths=None))) > 0

    # Test single valid search_path
    test_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    assert len(list(list_collection_dirs(search_paths=[test_path]))) == 2

    # Test include and exclude filter
    assert len(list(list_collection_dirs(search_paths=[test_path], coll_filter='foo'))) == 1

# Generated at 2022-06-12 20:55:49.101041
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    def create_test_dir(testdir, name):
        testdir_path = os.path.join(testdir, name)
        if not os.path.exists(testdir_path):
            os.makedirs(testdir_path)
        return testdir_path

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = to_bytes(tmpdir, errors='surrogate_or_strict')
        valid = create_test_dir(tmpdir, 'valid')
        file = create_test_dir(tmpdir, 'file')
        os.close(os.open(file, os.O_CREAT, 0o600))
        missing = create_test_dir(tmpdir, 'missing')
        missing_path = os.path.join(missing, 'missing_path')

# Generated at 2022-06-12 20:55:55.295162
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # TODO: this is a bad test and should be removed, but a better one needs to be written
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath

    # Default should find both collections
    dirs = list(list_collection_dirs())
    assert len(dirs) == 2
    # TODO: this isn't great, but it works for CI until we address this better
    assert all(b'test_namespace' in unfrackpath(x) for x in dirs)

    # Includes test_collection with a filter
    dirs = list(list_collection_dirs(coll_filter='test_namespace.test_collection'))
    assert len(dirs) == 1

# Generated at 2022-06-12 20:56:05.844875
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import doctest
    import os
    import tempfile
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    tmp_dir = tempfile.mkdtemp()
    # Create a nested collection directory with a __main__.py
    nested_coll_dir = os.path.join(tmp_dir, 'ansible_collections/namespace/collection/plugins/modules')
    os.makedirs(nested_coll_dir)
    open(os.path.join(nested_coll_dir, '__main__.py'), 'a').close()

    # Create a non-nested collection directory with a __main__.py
    non_nested_coll_dir = os.path.join(tmp_dir, 'ansible_collections/namespace/collection')

# Generated at 2022-06-12 20:56:17.730241
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Valid paths return unmodified
    paths = ['/path/to/mycollections']
    path_generator = list_valid_collection_paths(paths)
    assert next(path_generator) == paths[0]

    # Non-existent paths return a warning message
    # Collection root is never set in the config
    paths = ['/path/to/mycollections']
    path_generator = list_valid_collection_paths(paths, warn=True)
    assert next(path_generator) == paths[0]

    # Collection root not in config and not a directory
    paths = ['/path/to/mycollections']
    path_generator = list_valid_collection_paths(paths, warn=True)
    assert next(path_generator) == paths[0]

    # Collection root in

# Generated at 2022-06-12 20:56:22.516145
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths filters out invalid paths
    """

    assert list(list_valid_collection_paths(search_paths=["test_path"])) == ["test_path"]

    assert list(list_valid_collection_paths()) == AnsibleCollectionConfig.collection_paths

# Generated at 2022-06-12 20:56:32.520921
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    tmp_path = '/tmp/test_ansible_collection/'
    tmp_existing_path = os.path.join(tmp_path, 'existing')
    tmp_invalid_path = os.path.join(tmp_path, 'invalid')
    tmp_not_dir_path = os.path.join(tmp_path, 'not_dir')

    os.makedirs(tmp_existing_path)
    os.makedirs(tmp_invalid_path)
    with open(tmp_not_dir_path, mode='w') as f:
        f.write("it is not a dir")

    paths = [tmp_existing_path, tmp_invalid_path, tmp_not_dir_path]

# Generated at 2022-06-12 20:56:53.287535
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test Collection directory containing collection
    collection_dir = b'.'
    mock_paths = [collection_dir]

    # Should find collection directory
    assert list(list_collection_dirs(search_paths=mock_paths)).pop() == collection_dir

    # Test Collection directory containing namespace
    namespace_dir = b'./ansible_collections'
    mock_paths = [namespace_dir]

    # Should find namespace directory
    assert list(list_collection_dirs(search_paths=mock_paths)).pop() == namespace_dir

    # Test Collection containing namespace with collection
    namespace_dir = b'./ansible_collections/demisto'
    mock_paths = [namespace_dir]

    # Should find namespace directory

# Generated at 2022-06-12 20:56:57.873491
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.ansible.builtin.tests.unit.compat import unittest
    from ansible_collections.ansible.builtin.tests.unit.compat.mock import patch, Mock, MagicMock

    # not a dir, don't warn
    class CollectionConfig:
        def __init__(self, fake_paths):
            self.collection_paths = fake_paths

    test_paths = ["/my/fake/path/1", "/my/fake/path/2"]
    fake_collection_path_list = CollectionConfig(test_paths)
    fake_path1 = "/my/fake/path/1"
    fake_path2 = "/my/fake/path/2"

    fake_paths = [fake_path1]

    # Test missing path

# Generated at 2022-06-12 20:57:01.006316
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search = [u'path/does/not/exist', u'path/is/not/a/dir']
    assert list(list_valid_collection_paths(search)) == []



# Generated at 2022-06-12 20:57:10.550731
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    search_paths = [
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'test_ansible_collections'),
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'test_sibling_collections')
    ]

    for coll_dir in list_collection_dirs(search_paths):
        assert 'ansible_collections' not in coll_dir
        assert 'ansible-test-collection' in coll_dir

    for coll_dir in list_collection_dirs(search_paths, 'community.generic'):
        assert 'community' in coll_dir
        assert 'generic' in coll_dir


# Generated at 2022-06-12 20:57:22.159730
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    test_search_paths = ['/path/to/collection/a', '/path/to/collection/b']
    all_colls = list(list_collection_dirs(search_paths=test_search_paths))
    for coll_dir in all_colls:
        assert coll_dir.startswith('/path/to/collection')
        assert 'ansible_collections' in coll_dir
        assert os.path.isdir(coll_dir)

    # filter by namespace only
    namespace_only_colls = list(list_collection_dirs(search_paths=test_search_paths, coll_filter="acme"))
    for coll_dir in namespace_only_colls:
        assert coll_dir.startswith('/path/to/collection')
        assert 'ansible_collections'

# Generated at 2022-06-12 20:57:24.937609
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_filter = None
    search_paths = None
    collection = list_collection_dirs(search_paths, coll_filter)
    assert collection is not None

# Generated at 2022-06-12 20:57:34.973224
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = ['c', 'd', 'e']
    AnsibleCollectionConfig.collection_paths.append('a')
    AnsibleCollectionConfig.collection_paths.append('b')

    # no paths specified
    assert paths == list(list_valid_collection_paths([]))
    assert paths == list(list_valid_collection_paths())

    # only default paths exist
    assert paths == list(list_valid_collection_paths([]))

    # all paths exist
    paths = ['a', 'b']
    AnsibleCollectionConfig.collection_paths = paths[:]
    assert paths == list(list_valid_collection_paths(['c', 'd', 'e']))

    # non existent path
    paths = ['b', 'c', 'd', 'e']

# Generated at 2022-06-12 20:57:37.985400
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.path import unfrackpath

    for b_coll_dir in list_collection_dirs(coll_filter='net'):
        assert to_bytes(unfrackpath('$NET_ROOT/ansible')) in b_coll_dir

# Generated at 2022-06-12 20:57:43.392591
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    correct_collections = {
        'ansible': {
            'web_infrastructure': '/some/path/ansible_collections/ansible/web_infrastructure',
            'linux': '/some/path/ansible_collections/ansible/linux'
        },
        'community': {
            'vmware': '/some/path/ansible_collections/community/vmware'
        },
        'somewhere': {
            'else': '/some/other/path/ansible_collections/somewhere/else'
        }
    }

    # No filter, all collections
    # Mock out the filesystem
    import mock

    all_collections = correct_collections
    all_collections['community']['networking'] = '/some/path/ansible_collections/community/networking'

    mock_

# Generated at 2022-06-12 20:57:48.306288
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_paths = ['foo', 'bar']
    test_collection = 'another.collection'
    expected_result = [b'foo/ansible_collections/another/collection',
                       b'bar/ansible_collections/another/collection']
    result = list(list_collection_dirs(test_paths, coll_filter=test_collection))
    assert result == expected_result

# Generated at 2022-06-12 20:58:06.292031
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    # create temp dir and some collections that can be found
    d = tempfile.mkdtemp()
    coll_find = os.path.join(d, 'ansible_collections', 'namespace', 'collection')
    os.makedirs(coll_find)
    # create a collection that should not be found
    coll_no_find = os.path.join(d, 'ansible_collections', 'namespace', 'collection_no_find')
    os.makedirs(coll_no_find)
    # also create a collection outside of a namespace
    coll_no_namespace = os.path.join(d, 'ansible_collections', 'collection_no_namespace')
    os.makedirs(coll_no_namespace)
    # Get list of collection directories
    coll_dirs

# Generated at 2022-06-12 20:58:11.112302
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    b_paths = list(list_valid_collection_paths(search_paths=None, warn=False))
    assert len(b_paths) == len(AnsibleCollectionConfig.collection_paths)

    b_paths = list(list_valid_collection_paths(search_paths=[], warn=False))
    assert len(b_paths) == len(AnsibleCollectionConfig.collection_paths)

    b_paths = list(list_valid_collection_paths(search_paths=['not-there'], warn=True))
    assert len(b_paths) == len(AnsibleCollectionConfig.collection_paths)

    b_paths = list(list_valid_collection_paths(search_paths=[__file__], warn=True))

# Generated at 2022-06-12 20:58:19.239907
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Unit test setup
    import tempfile
    test_coll_dir = tempfile.mkdtemp()

    # create a fake collection directory
    ns_dir = os.path.join(test_coll_dir, 'namespace')
    os.makedirs(ns_dir)

    coll_dir = os.path.join(ns_dir, 'collection')
    os.makedirs(coll_dir)

    # file within the collection
    plug_fn = os.path.join(coll_dir, 'plugins', 'test.py')
    os.makedirs(os.path.dirname(plug_fn))
    with open(plug_fn, 'w') as f:
        f.write('test')

    ret = list(list_collection_dirs([test_coll_dir]))

# Generated at 2022-06-12 20:58:29.727756
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    # make a fake collection dir
    coltmp = tempfile.mkdtemp()
    os.mkdir(os.path.join(coltmp, 'ansible_collections'))
    os.mkdir(os.path.join(coltmp, 'ansible_collections', 'myorg'))
    os.mkdir(os.path.join(coltmp, 'ansible_collections', 'myorg', 'mycoll'))
    os.mkdir(os.path.join(coltmp, 'ansible_collections', 'myorg', 'mycoll', 'plugins'))
    os.mkdir(os.path.join(coltmp, 'ansible_collections', 'myorg', 'mycoll', 'plugins', 'modules'))

# Generated at 2022-06-12 20:58:33.608576
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import load_collections

    # skip warnings while testing
    load_collections(list_only=True, collection_paths=["/invalid_path"])

# Generated at 2022-06-12 20:58:42.613011
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test a single namespace
    coll_filter = 'system'
    collection_dirs = [x for x in list_collection_dirs(coll_filter=coll_filter)]
    assert collection_dirs

    # Test a single collection
    coll_filter = 'system.ansible'
    collection_dirs = [x for x in list_collection_dirs(coll_filter=coll_filter)]
    assert collection_dirs

    # Test a non-existant collection
    coll_filter = 'chris'
    collection_dirs = [x for x in list_collection_dirs(coll_filter=coll_filter)]
    assert not collection_dirs

    # Test all collections
    coll_filter = None
    collection_dirs = [x for x in list_collection_dirs(coll_filter=coll_filter)]
   

# Generated at 2022-06-12 20:58:49.432835
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import os
    import tempfile
    import shutil

    # remove any user config file
    config = AnsibleCollectionConfig()
    config_file = config.get_config_file_path()
    if os.path.exists(config_file):
        os.remove(config_file)
    # create a temp dir and add to user config file
    temp_dir = tempfile.mkdtemp()
    temp_dir_b = to_bytes(temp_dir)
    config.set_collection_paths([temp_dir_b])

    # create a valid coll dir
    valid_coll_dir_b = os.path.join(temp_dir_b, b'ansible_collections', b'test.test_coll')
    os.makedirs(valid_coll_dir_b)
    # create an invalid,ex

# Generated at 2022-06-12 20:58:58.550856
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    coll_dirs = list(list_collection_dirs(search_paths=["tests/units/collection/search_paths/dummy_path"],
                                          coll_filter="ns1.coll1"))
    assert len(coll_dirs) == 1
    assert coll_dirs[0] == b"tests/units/collection/search_paths/dummy_path/ansible_collections/ns1/coll1"

    coll_dirs = list(list_collection_dirs(search_paths=["tests/units/collection/search_paths/dummy_path"],
                                          coll_filter="ns1.coll2"))
    assert len(coll_dirs) == 1

# Generated at 2022-06-12 20:59:00.522822
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # TODO: unit test for function list_valid_collection_paths
    pass



# Generated at 2022-06-12 20:59:12.238560
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    search_path = [tempfile.mkdtemp()]

    coll_path = os.path.join(search_path[0], 'ansible_collections')
    os.makedirs(coll_path)

    fake_namespace = 'namespace'
    fake_colls = ['collection1', 'collection2']
    fake_coll_path = os.path.join(coll_path, fake_namespace)
    os.makedirs(fake_coll_path)


# Generated at 2022-06-12 20:59:29.901000
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = [os.path.expanduser("~"), '/non/existent', "folder=with_invalid_name"]
    paths_filtered = list_valid_collection_paths(search_paths=paths, warn=False)
    assert not paths_filtered, \
        "paths filtered should be empty list when all paths are invalid"
    paths_filtered = list_valid_collection_paths(search_paths=paths, warn=True)
    assert not paths_filtered, \
        "paths filtered should be empty list when all paths are invalid"

# Generated at 2022-06-12 20:59:33.569027
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['/nonexistent/path', '/etc/ansible/collections']

    valid_paths = list(list_valid_collection_paths(search_paths))

    assert '/etc/ansible/collections' in valid_paths
    assert len(valid_paths) == 1



# Generated at 2022-06-12 20:59:38.091221
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert len(list(list_collection_dirs())) > 0
    assert not list_collection_dirs(search_paths=["/tmp"])
    assert len(list(list_collection_dirs(search_paths=["/tmp", "/"]))) > 0
    assert not list_collection_dirs(coll_filter="ns.coll")

# Generated at 2022-06-12 20:59:40.935510
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    list_paths = list(list_valid_collection_paths(['/tmp/not_here',
                                                   '/tmp',
                                                   'no_exists'],
                                                   warn=False))

    assert list_paths == ['/tmp']



# Generated at 2022-06-12 20:59:47.976864
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test against source repo
    collection_paths = ['test/units/data/collections1', 'test/units/data/collections2', 'test/units/data/collections3']
    collection_dirs = list_collection_dirs(search_paths=collection_paths)
    assert collection_dirs

    # Test against galaxy
    collection_dirs = list_collection_dirs()
    assert collection_dirs

    # Test against specific collection
    collection_dirs = list_collection_dirs(coll_filter='ansible_namespace.collection2')
    assert len(list(collection_dirs)) == 1

    # Test against specific collection, with namespaces
    collection_dirs = list_collection_dirs(coll_filter='ansible_namespace.collection3')

# Generated at 2022-06-12 20:59:52.500294
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Ensure test invokes previous implementation while under Ansible 2.9
    orig_list_valid_collection_paths = list_valid_collection_paths
    try:
        list_valid_collection_paths = AnsibleCollectionConfig.list_valid_collection_paths
        assert list_collection_dirs([os.path.join(os.path.dirname(__file__), '../data/collection_path')])
    finally:
        list_valid_collection_paths = orig_list_valid_collection_paths

# Generated at 2022-06-12 21:00:02.898255
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile
    from shutil import rmtree
    from json import load

    tmpdir = tempfile.mkdtemp()
    os.mkdir(to_bytes(os.path.join(tmpdir, 'ansible_collections', 'test.test')))

    paths = [os.path.join(tmpdir, 'ansible_collections')]
    paths.extend(AnsibleCollectionConfig.collection_paths)

    # with namespace, but no collection
    collection_dirs = list(list_collection_dirs(paths, 'test'))
    assert len(collection_dirs) == 1
    assert collection_dirs[0].endswith('/ansible_collections/test/test')

    # with namespace.collection

# Generated at 2022-06-12 21:00:12.168197
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    expected_collection_roots = ['/usr/share/ansible/ansible_collections',
                                 '/etc/ansible/ansible_collections']

    assert list_collection_dirs(search_paths=['/usr/share/ansible', '/etc/ansible'])

    with pytest.raises(AnsibleError) as error, pytest.raises(AnsibleError) as error2:
        list_collection_dirs(coll_filter='ynos.l3')

    assert "Invalid collection pattern supplied" in str(error)
    assert "Invalid collection pattern supplied" in str(error2)

# Generated at 2022-06-12 21:00:18.304398
# Unit test for function list_collection_dirs

# Generated at 2022-06-12 21:00:22.533198
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Setup: Create the needed test data
    collection_dirs = list_collection_dirs(search_paths=['test/test_data'])
    assert 'test.test_data_one' in str(collection_dirs)
    assert 'test.test_data_two' in str(collection_dirs)

# Generated at 2022-06-12 21:00:49.314976
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test for a list of valid collection paths, with a warning on non-existant paths
    """
    coll_paths = [
        u'/',
        '/doesnotexist',
        '/etc/ansible/',
        '/usr/share/ansible/',
        u'',
        'asdf',
        '/dev/null',
        'https://foo.example.com/my/path/',
        ]
    result = list_valid_collection_paths(coll_paths, warn=True)
    assert('/usr/share/ansible/' in result)
    assert('/etc/ansible/' in result)
    assert('/' in result)
    assert('/dev/null' not in result)
    assert('asdf' not in result)

# Generated at 2022-06-12 21:00:54.436427
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import ansible.constants as C
    ansible_path = C.DEFAULT_COLLECTIONS_PATHS[0]
    assert '/ansible_collections' in ansible_path

    a = list_collection_dirs()
    path = a.__next__()
    assert 'ansible_collections' in path
    assert 'ansible.builtin' in path
    assert 'lookup' in path

# Generated at 2022-06-12 21:01:06.233986
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    b_collection_root = to_bytes(tempfile.mkdtemp(prefix='coll-test-dir'))

    # Some test collections
    os.mkdir(os.path.join(b_collection_root, b'namespace1'))
    os.mkdir(os.path.join(b_collection_root, b'namespace1', b'collection1'))
    f = open(os.path.join(b_collection_root, b'namespace1', b'collection1', b'meta', b'main.yml'), 'w')
    f.write('galaxy_info:\n  namespace: namespace1\n  name: collection1\n  version: 0.1.0\n')
    f.close()

# Generated at 2022-06-12 21:01:14.378688
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test on non existing path
    assert list(list_valid_collection_paths(['/tmp/does_not_exist'])) == []

    # test on file
    tmp_file = "/tmp/ansibler_test_file"
    open(tmp_file, 'a').close()
    assert list(list_valid_collection_paths([tmp_file])) == []

    # test on existing directory
    tmp_dir = "/tmp/ansibler_test_dir"
    os.mkdir(tmp_dir)
    assert list(list_valid_collection_paths([tmp_dir])) == [tmp_dir]

    # clean up
    os.remove(tmp_file)
    os.rmdir(tmp_dir)

# Generated at 2022-06-12 21:01:24.611851
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import pytest
    import tempfile
    import shutil
    import os
    import stat

    # Create temporary directory and Ansible collection within it
    tmp_test_dir = tempfile.mkdtemp(prefix="ansible-test-collections-")
    test_coll_dir = os.path.join(tmp_test_dir, 'ansible_collections', 'jimbob', 'foo')
    os.makedirs(test_coll_dir)
    # Create a file to confirm the directory is a valid Ansible collection
    with open(os.path.join(test_coll_dir, 'metadata.json'), 'w') as f:
        f.write('{}')

    # Create config in temporary directory which includes above existing collection
    coll_config = os.path.join(tmp_test_dir, 'ansible.cfg')

# Generated at 2022-06-12 21:01:27.397505
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/tmp'])

# Generated at 2022-06-12 21:01:34.162769
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.display import Display

    # pylint: disable=invalid-name
    a = AnsibleCollectionConfig()
    d = Display()
    a.set_config_data({
        'collections_paths': ['foo', '/bar'],
    })
    # pylint: enable=invalid-name

    # collection_dirs_1
    assert list(list_collection_dirs()) == []

    # collection_dirs_2
    assert list(list_collection_dirs(search_paths=[])) == []

    # collection_dirs_3
    assert list(list_collection_dirs(search_paths=a.collection_paths)) == []

    # collection_dirs_4

# Generated at 2022-06-12 21:01:42.898533
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_paths = ['./test_data/empty',
                  './test_data/library_collections',
                  './test_data/module_collections',
                  './test_data/mixed_collections']

    display.verbosity = 4

    # test without namespace/collection filter
    colls = list(list_collection_dirs(search_paths=test_paths))
    assert len(colls) == 6

    # test with namespace filter
    colls = list(list_collection_dirs(search_paths=test_paths, coll_filter='.*demo.*'))
    assert len(colls) == 3

    # test with collection filter

# Generated at 2022-06-12 21:01:54.590254
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_paths = list_valid_collection_paths(search_paths=['/tmp', '/dev'])
    assert '/tmp' in valid_paths
    assert '/dev' not in valid_paths
    assert '/etc' not in valid_paths
    assert 'etc' not in valid_paths
    valid_paths = list_valid_collection_paths(search_paths=[])
    assert '/usr/share/ansible/collections' in valid_paths
    assert '/etc/ansible/collections' in valid_paths
    assert '/etc' not in valid_paths
    assert 'etc' not in valid_paths



# Generated at 2022-06-12 21:02:04.394154
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    dirs = list_collection_dirs('test/units/files/collection_finder/namespace_invalid', coll_filter=None)
    assert len(dirs) == 0

    dirs = list_collection_dirs('test/units/files/collection_finder/namespace_invalid', coll_filter='namespace.name')
    assert len(dirs) == 0

    dirs = list_collection_dirs('test/units/files/collection_finder/namespace_invalid', coll_filter='missing_namespace')
    assert len(dirs) == 0

    dirs = list_collection_dirs('test/units/files/collection_finder/namespace_invalid', coll_filter='missing_namespace.missing_collection')
    assert len(dirs) == 0

    dirs = list_collection_dirs

# Generated at 2022-06-12 21:02:41.008121
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['/foo/bar/baz', '/bar/moo/mar', '/baz/moo/maz']
    expected_paths = search_paths + AnsibleCollectionConfig.collection_paths

    paths = list_valid_collection_paths(search_paths)

    for path in paths:
        assert path in expected_paths

# Generated at 2022-06-12 21:02:45.263174
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves import builtins

    builtins.__dict__['_'] = lambda x: x

    path_to_test = ["/tmp/foo/bar", "/tmp/foo/baz"]
    paths = list_valid_collection_paths(path_to_test, warn=True)
    assert paths != []
    assert list(paths) == path_to_test
    assert "The configured collection path /tmp/foo/bar, exists, but it is not a directory." in display.display

# Generated at 2022-06-12 21:02:55.818039
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    This is an integration test which hits the filesystem to verify actual directories
    are returned by the function.  It is an integration test because there is no other
    way to test the function at this time.

    This test assumes the test-collection is installed into the ansible_collections path
    and can be found.  This test also assumes that the ansible_collections path if from
    the AnsibleCollectionConfig.collection_paths
    """
    collection_dirs = list(list_collection_dirs())

    # We will assume for this test that it will find at least one collection
    assert len(collection_dirs) > 0

    # We have to assume for this test the test-collection is installed.  We will check
    # that we can find the test-collection by looking for the file test_collection/plugins/action/test_action.py


# Generated at 2022-06-12 21:03:07.412603
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # 1. Return what should be returned
    # 1.1 Return all collections
    coll_filter = None
    colls = list_collection_dirs(coll_filter=coll_filter)
    assert len(colls) > 0
    # 1.2 Return a specific collection
    coll_filter = "ansible.builtin"
    colls = list_collection_dirs(coll_filter=coll_filter)
    assert len(colls) > 0
    # 1.3 Return a specific namespace
    coll_filter = "ansible"
    colls = list_collection_dirs(coll_filter=coll_filter)
    assert len(colls) > 0
    # 1.4 Return specific namespace and collection
    coll_filter = "ansible.builtin"

# Generated at 2022-06-12 21:03:18.034534
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # create temp dir
    import tempfile
    temp_dir = tempfile.mkdtemp()
    # remove after use
    import atexit
    atexit.register(lambda: shutil.rmtree(temp_dir))
    # create collection
    coll_dir = tempfile.mkdtemp(dir=temp_dir)
    plug_dir = tempfile.mkdtemp(dir=coll_dir)
    # create valid namespace/collection
    coll_dir = os.path.join(coll_dir, 'ansible_collections', 'test_ns', 'nested_coll')
    os.makedirs(coll_dir)
    coll_file = os.path.join(coll_dir,  'plugins', 'collection_info', 'test.json')
    with open(coll_file, 'wt') as f:
        f

# Generated at 2022-06-12 21:03:28.312156
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    fake_path = "/tmp/fake_path"
    fake_path2 = "/tmp/fake_path2"

    # search_paths not supplied
    results = list(list_valid_collection_paths())
    assert len(results) == len(AnsibleCollectionConfig.collection_paths)

    # single path search
    results = list(list_valid_collection_paths([fake_path]))
    assert len(results) == 1
    assert fake_path in results

    # multi path search
    results = list(list_valid_collection_paths([fake_path, fake_path2]))
    assert len(results) == 2
    assert fake_path in results
    assert fake_path2 in results

    # invalid path search