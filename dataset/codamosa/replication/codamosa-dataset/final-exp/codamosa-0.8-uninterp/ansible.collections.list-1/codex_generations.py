

# Generated at 2022-06-12 20:53:43.238910
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    collection_path = os.path.join(tempfile.gettempdir(), 'ansible_collections')

    def assert_collections(coll_spec, expected_namespaces, expected_collections):
        found_namespaces = []
        found_collections = []

        for path in list_collection_dirs([collection_path], coll_filter=coll_spec):
            parts = path.split(os.path.sep)
            found_namespaces.append(parts[-2])
            found_collections.append(parts[-1])

        assert sorted(found_namespaces) == sorted(expected_namespaces)
        assert sorted(found_collections) == sorted(expected_collections)

    # only one collection, no namespace

# Generated at 2022-06-12 20:53:49.485914
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    mypath = '/home/username/collections/'
    # Note: The path exist - but it's not a directory, so it should not return
    non_dir_path = '/etc/hosts'
    # Note: The path doesn't exist and it should not return
    non_existing_path = '/home/username/Collections/'

    search_paths = [non_existing_path, non_dir_path, mypath]
    assert list(list_valid_collection_paths(search_paths)) == [mypath]


# Generated at 2022-06-12 20:53:56.811168
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit tests for function list_collection_dirs
    """

    import ansible.constants as C

    def fqdn_coll(namespace, collection):
        return os.path.join(C.DEFAULT_COLLECTIONS_PATH, namespace, collection)

    assert list_collection_dirs(['/abc'], coll_filter='myns.mycoll') == \
        [to_bytes(fqdn_coll('myns', 'mycoll'))]

    assert list_collection_dirs(['/abc'], coll_filter='myns') == \
        [to_bytes(fqdn_coll('myns', 'mycoll'))]

    assert list_collection_dirs(['/abc']) == \
        [to_bytes(fqdn_coll('myns', 'mycoll'))]

# Generated at 2022-06-12 20:54:05.038479
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = [
        '/does/not/exist',
        '/dev/null',
        '/etc',
        '/tmp/'
    ]
    assert(list(list_valid_collection_paths(search_paths=paths)) == ['/etc', '/tmp/'])
    assert(list(list_valid_collection_paths(search_paths=paths, warn=True)) == ['/etc', '/tmp/'])



# Generated at 2022-06-12 20:54:07.062384
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['./foo', './bar'])) == ['./foo', './bar']



# Generated at 2022-06-12 20:54:08.882999
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_path = list_valid_collection_paths(['.'])
    assert list(valid_path) == ['.']


# Generated at 2022-06-12 20:54:18.927196
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import os

    tempdir = tempfile.mkdtemp()
    os.makedirs(os.path.join(tempdir, 'ansible_collections'))

    def _assert_tempdir_in_results():
        results = list(list_valid_collection_paths([tempdir]))
        assert results == [tempdir]

    _assert_tempdir_in_results()
    # ensure order is maintained
    _assert_tempdir_in_results()

    os.rmdir(os.path.join(tempdir, 'ansible_collections'))



# Generated at 2022-06-12 20:54:29.154481
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import tempfile
    import shutil
    import pytest

    # Create collection directories
    root_dir = tempfile.mkdtemp()
    coll_dir = os.path.join(root_dir, 'ansible_collections')
    os.mkdir(coll_dir)
    os.mkdir(os.path.join(coll_dir, 'fibonacci'))
    os.mkdir(os.path.join(coll_dir, 'fibonacci', 'numbers'))
    os.mkdir(os.path.join(coll_dir, 'fibonacci', 'numbers2'))
    os.mkdir(os.path.join(coll_dir, 'fibonacci', 'numbers3'))

# Generated at 2022-06-12 20:54:40.237582
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    data_dir = os.path.join(os.path.dirname(__file__), 'unit_data')

    collection_dirs = list(list_collection_dirs([os.path.join(data_dir, 'collections')]))
    assert len(collection_dirs) == 6
    assert os.path.basename(collection_dirs[0]) == 'ns1.coll1'
    assert os.path.basename(collection_dirs[1]) == 'ns1.coll2'
    assert os.path.basename(collection_dirs[2]) == 'ns1.coll3'
    assert os.path.basename(collection_dirs[3]) == 'ns1.coll4'
    assert os.path.basename(collection_dirs[4]) == 'ns2.coll5'

# Generated at 2022-06-12 20:54:50.396833
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    result = list(list_collection_dirs(search_paths=["test_list_collection_dirs/path1",
                                                     "test_list_collection_dirs/path2"],
                                       coll_filter="namespace1.collection1"))
    assert result == ["test_list_collection_dirs/path1/ansible_collections/namespace1/collection1"]

    result = list(list_collection_dirs(search_paths=["test_list_collection_dirs/path1",
                                                     "test_list_collection_dirs/path2"],
                                       coll_filter="namespace2"))

# Generated at 2022-06-12 20:55:03.105927
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = [
        "/fred",
        "/barney",
        "/wilma"
    ]

    if os.path.exists("/wnp"):
        paths.append("/wnp")

    new_paths = list(list_valid_collection_paths(paths))

    assert len(new_paths) == 0 or new_paths[-1].endswith("ansible_collections")

    new_paths = list(list_valid_collection_paths(paths, warn=True))

    assert len(new_paths) == 0 or new_paths[-1].endswith("ansible_collections")

# Generated at 2022-06-12 20:55:13.077647
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    if not os.path.exists('./lib/ansible/test_data/test_collections'):
        os.mkdir('./lib/ansible/test_data/test_collections')

    # test with wildcard
    assert list(list_valid_collection_paths(['/tmp/*'])) == []
    assert list(list_valid_collection_paths(['/tmp/*', './lib/ansible/test_data'])) == ['./lib/ansible/test_data']
    assert list(list_valid_collection_paths(['/tmp/*', './lib/ansible/test_data/*'])) == []

    # test with non-existing paths

# Generated at 2022-06-12 20:55:17.755726
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_paths = ['/path/to/one', '/path/to/two']
    coll_dirs = list_collection_dirs(collection_paths, 'namespace.collection')
    assert coll_dirs



# Generated at 2022-06-12 20:55:23.413041
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys
    test_path = os.path.dirname(__file__)
    test_lib_path = os.path.join(test_path, 'units')
    sys.path.append(test_lib_path)
    from test_collection_loader import CollectionLoaderTestCase

    test_group = CollectionLoaderTestCase('test_list_collection_dirs')
    test_group.setup_fixures()
    for coll_dir in list_collection_dirs(test_group.fixture_paths):
        assert coll_dir in test_group.fixture_coll_dirs
    test_group.teardown_fixures()

# Generated at 2022-06-12 20:55:32.446719
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.test.test_mock.mock import patch

    test_paths = (
        'abc/def',
        'abc/def/ghi',
        'jkl/mno/pqr',
    )

    with patch('ansible.collections.collection_loader.AnsibleCollectionConfig') as mock_config:
        mock_config.collection_paths = test_paths

        test_results = list(list_valid_collection_paths())
        assert test_results == test_paths



# Generated at 2022-06-12 20:55:39.623445
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.collections import mock_list_collection_dirs_1, mock_list_collection_dirs_2

    def test_collection_dirs_assertion_1():
        list_collection_dirs(search_paths=['/foo/bar'])

    mock_unfrackpath_noop(globals())
    mock_list_collection_dirs_1(globals())

    try:
        test_collection_dirs_assertion_1()
    except Exception as ex:
        assert str(ex) == 'bad list_collection_dirs_1'

    mock_list_collection_dirs_2(globals())

# Generated at 2022-06-12 20:55:44.321999
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # mock out config loading, since this is tested elsewhere
    class FakeConfig(object):
        collections_paths = ['a', 'b']

    original_config = AnsibleCollectionConfig
    AnsibleCollectionConfig = FakeConfig

    assert list(list_valid_collection_paths(['c', 'd'])) == ['c', 'd']

    # reset the config
    AnsibleCollectionConfig = original_config

# Generated at 2022-06-12 20:55:52.314745
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['/some/arbitrary/path', '/another/path']

    # Test both unicode and str search paths
    valid_paths = list(list_valid_collection_paths(search_paths, warn=False))
    assert isinstance(valid_paths, list)
    assert len(valid_paths) == 2
    assert valid_paths == search_paths

    # Test bytes search paths
    valid_paths = list(list_valid_collection_paths([to_bytes(x) for x in search_paths], warn=False))
    assert isinstance(valid_paths, list)
    assert len(valid_paths) == 2
    assert valid_paths == search_paths

# Generated at 2022-06-12 20:56:02.812277
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # No search_path
    search_paths = []
    assert list(list_valid_collection_paths(search_paths)) == []
    assert list(list_valid_collection_paths(search_paths, True)) == []
    # List of valid paths
    search_paths = ["/usr/share/ansible/collections", "~/share/ansible/collections"]
    assert list(list_valid_collection_paths(search_paths)) == search_paths
    assert list(list_valid_collection_paths(search_paths, True)) == search_paths
    # List of valid paths and invalid paths

# Generated at 2022-06-12 20:56:09.789076
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        '/usr/share/ansible',
        '/usr/share/ansible_collections',
        '/tmp/does/not/exist',
        '/tmp/is_file',
        '/tmp/ok.dir',
    ]

    os.makedirs('/tmp/ok.dir')
    open('/tmp/is_file', 'a').close()

    results = list(list_valid_collection_paths(search_paths, warn=True))

    assert '/usr/share/ansible' in results
    assert '/usr/share/ansible_collections' in results
    assert '/tmp/ok.dir' in results
    assert '/tmp/does/not/exist' not in results
    assert '/tmp/is_file' not in results

# Generated at 2022-06-12 20:56:20.779332
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    result = list(list_valid_collection_paths(search_paths=['/tmp/does/not/exist', '/tmp']))
    assert len(result) == 1

# Generated at 2022-06-12 20:56:31.834996
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    from shutil import rmtree
    from ansible.config.manager import ConfigManager
    from ansible.config.data import ConfigObj
    coll_root = os.path.join(tempfile.mkdtemp(), 'ansible_collections')

    for ns in ('foo', 'bar'):
        os.mkdir(os.path.join(coll_root, ns))
        for coll in ('baz', 'bum'):
            coll_dir = os.path.join(coll_root, ns, coll)
            os.mkdir(coll_dir)
            open(os.path.join(coll_dir, '__init__.py'), 'w').close()

# Generated at 2022-06-12 20:56:42.784172
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    coll_loader = AnsibleCollectionConfig()
    coll_loader.load()
    coll_paths = coll_loader.collection_paths
    valid_coll_paths = list(list_valid_collection_paths())

    # show results
    display.display("Valid collection paths:")
    display.display(valid_coll_paths)
    display.display("Configured collection paths:")
    display.display(coll_paths)

    # compare
    errors = False
    if sorted(valid_coll_paths) != sorted(coll_paths):
        errors = True
        display.error("ERROR: test_list_valid_collection_paths failed to verify valid paths")

    # test with missing dir
    search_paths = coll_paths.copy()
    search_paths.append('/tmp/foo')


# Generated at 2022-06-12 20:56:50.197533
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Make sure we are getting valid paths
    """

    coll_paths = [
        "/tmp",
        os.path.dirname(os.path.abspath(__file__)),
        "/usr/share/ansible/ansible_collections"
    ]

    valid_paths = list(list_valid_collection_paths(search_paths=coll_paths, warn=False))

    assert valid_paths == [coll_paths[1]]



# Generated at 2022-06-12 20:56:56.799567
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import sys
    import ansible_collections

    import tempfile
    import shutil
    import os

    import collections

    TEST_COLLECTIONS = collections.defaultdict(dict)
    TEST_COLLECTIONS['namespace1']['collection1'] = 'test/test_collections/namespace1/collection1'
    TEST_COLLECTIONS['namespace1']['collection2'] = 'test/test_collections/namespace1/collection2'
    TEST_COLLECTIONS['namespace2']['collection1'] = 'test/test_collections/namespace2/collection1'
    TEST_COLLECTIONS['namespace2']['collection2'] = 'test/test_collections/namespace2/collection2'

# Generated at 2022-06-12 20:56:58.770834
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(search_paths=[os.getcwd()])) == [os.getcwd()]
    assert list(list_valid_collection_paths(search_paths=['/non/existing/path'])) == []


# Generated at 2022-06-12 20:57:08.188382
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    # Setup two namespaces
    test_namespace_1 = 'my_namespace_1'
    test_namespace_2 = 'my_namespace_2'

    # Create a working directory
    test_dir = tempfile.mkdtemp()

    # Create a collections directory as a subdirectory of the working directory
    collections_dir = os.path.join(test_dir, 'ansible_collections')
    os.mkdir(collections_dir)

    # Create a namespace directory under the collections directory
    namespace_dir_1 = os.path.join(collections_dir, test_namespace_1)
    os.mkdir(namespace_dir_1)

    # Create a collection directory under the namespace directory

# Generated at 2022-06-12 20:57:15.579531
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import pytest

    def _create_file(path):
        with open(path, 'w+') as f:
            f.write('some content')

    temp_dir = tempfile.mkdtemp()
    temp_path_ansible_collection = os.path.join(temp_dir, 'ansible_collection')
    temp_path_namespace = os.path.join(temp_path_ansible_collection, 'namespace')
    temp_path_namespace_1 = os.path.join(temp_path_ansible_collection, 'namespace1')
    temp_path_namespace_2 = os.path.join(temp_path_ansible_collection, 'namespace2')

# Generated at 2022-06-12 20:57:27.090844
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test this module to be used as unit test in docker image
    :return:
    """

    # normalize paths
    search_paths = [
        '/ansible_collections/foo/bar',
        '/ansible_collections/test',
        'ansible_collections/test/foobar',
    ]

    # make sure we got the correct count of returned dirs
    assert len(list(list_collection_dirs(search_paths))) == 3

    # make sure we got the correct count of returned dirs
    assert len(list(list_collection_dirs(search_paths, 'test'))) == 1

    # make sure we got the correct count of returned dirs
    assert len(list(list_collection_dirs(search_paths, 'test.foobar'))) == 1

# Generated at 2022-06-12 20:57:36.939925
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # returns only collection dirs in list that contain ansible_collections in their path
    assert list(list_collection_dirs(["/foo", "/foo/ansible_collections", "/bar/ansible_collections/namespace/collection"])) == ['/foo/ansible_collections', '/bar/ansible_collections/namespace/collection']
    # returns only collection dirs in list that contain 'ansible_collections/namespace/collection' in their path
    assert list(list_collection_dirs(["/foo", "/foo/ansible_collections", "/bar/ansible_collections/namespace/collection"],
                                      coll_filter="namespace.collection")) == ['/bar/ansible_collections/namespace/collection']
    # returns only collection dirs in list that contain 'ansible_collections/namespace

# Generated at 2022-06-12 20:57:59.629694
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''
    test list_valid_collection_paths()
    '''
    test_valid_paths = ['/blah/yeah', '~/omg', '/wtf/bbq']
    valid_paths = list(list_valid_collection_paths(test_valid_paths))
    assert all(path in test_valid_paths for path in valid_paths)
    assert len(valid_paths) == 3


# Generated at 2022-06-12 20:58:09.191520
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.plugins.finder import find_collection_in_search_path, get_collection_variant_loadable_paths
    from ansible.collections import AnsibleCollectionLoader
    from ansible.module_utils import basic

    cl = AnsibleCollectionLoader()

    display.verbosity = 4
    display.deprecated = False

    # just make sure the collection loading works
    dirs = list(list_collection_dirs())
    assert len(dirs) >= 1
    basic.remove_tree(dirs[0])

    # just make sure the collection loader can work with these
    coll_path = find_collection_in_search_path('ansible_collections.nope')
    assert coll_path is None
    coll_path = find_collection_in_search_path('nope.nope')
    assert coll

# Generated at 2022-06-12 20:58:18.293298
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.collections import default_collection_paths, list_collections
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader import AnsibleCollectionConfigData

    config = AnsibleCollectionConfigData(
        collection_paths=[]
    )

    # Test expected search paths
    coll_paths = sorted(list(list_collection_dirs()))
    exp_coll_paths = sorted(default_collection_paths())
    if coll_paths != exp_coll_paths:
        raise AssertionError("Expected search paths: %s\nSearch paths: %s"
                             % (exp_coll_paths, coll_paths))

    # Test no non-existing search paths

# Generated at 2022-06-12 20:58:29.371167
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    collection_path = '/usr/share/ansible/collections:~/.ansible/collections'
    collection_b_path = to_bytes(collection_path, errors='surrogate_or_strict')

    # Test that legacy search path is converted to local collection path
    assert list(list_valid_collection_paths([collection_path])) == [os.path.join(x, 'ansible_collections') for x in collection_b_path.split(b':')]

    # Test that b_path is converted to local collection path
    assert list(list_valid_collection_paths([collection_b_path])) == [os.path.join(x, 'ansible_collections') for x in collection_b_path.split(b':')]

    # Test that search_paths are not modified
    assert list

# Generated at 2022-06-12 20:58:35.739005
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    mysearch_paths = []
    mysearch_paths.append('/tmp/does_not_exist')
    mysearch_paths.append('/tmp')
    mysearch_paths.append('/tmp/does_not_exist_either')

    for path in list_valid_collection_paths(mysearch_paths, warn=False):
        assert path == '/tmp'

# Generated at 2022-06-12 20:58:37.092305
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths()) != []



# Generated at 2022-06-12 20:58:42.278621
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert len(list(list_valid_collection_paths())) == 1
    assert len(list(list_valid_collection_paths(search_paths=["/notarealdir/justatest"]))) == 1
    assert len(list(list_valid_collection_paths(search_paths=["/usr/local"]))) == 1
    assert len(list(list_valid_collection_paths(search_paths=["/usr/local", "/notarealdir/justatest"]))) == 2

# Generated at 2022-06-12 20:58:44.934582
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test that a missing path is ignored
    paths = ['abc/defghi/jklm']
    assert list(list_valid_collection_paths(paths)) == []

    return True

# Generated at 2022-06-12 20:58:50.553005
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test with a non-existent search_path
    search_path = ['/tmp/invalid_non_existent_default_ansible_collections']
    result = list_valid_collection_paths(search_path)
    assert list(result) == []

    if os.path.exists('/tmp/invalid_non_existent_default_ansible_collections'):
        os.rmdir('/tmp/invalid_non_existent_default_ansible_collections')

    # Test with a short name non-existent search_path
    search_path = ['invalid_non_existent_default_ansible_collections']
    result = list_valid_collection_paths(search_path)
    assert list(result) == []

    # Test with a non-existent search_path

# Generated at 2022-06-12 20:58:59.217596
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test1_paths = ["./test1", "./test2", "./test3"]
    test2_paths = ["./test1/ansible_collections", "./test2/ansible_collections", "./test3/ansible_collections"]
    test3_paths = ["./test1/ansible_collections/", "./test2/ansible_collections/", "./test3/ansible_collections/"]
    test1_filter = "awx"
    test2_filter = "awx.awx_collection"

# Generated at 2022-06-12 20:59:39.552681
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    existing_dirs = []

    # Test with non existing dirs
    search_path = ['/no/such/dir', '/no/such/dir/either']
    result = list_valid_collection_paths(search_path)
    assert len(list(result)) == 0

    # Test with dir that is not a directory
    with open("/tmp/does_not_exist", 'a+') as f:
        search_path = [f.name]
        result = list_valid_collection_paths(search_path, False)
        assert len(list(result)) == 0

    # Test with a real existing dir and a default path
    existing_dirs.append(os.path.dirname(os.path.realpath(__file__)))
    search_path = existing_dirs
    result = list_valid_collection

# Generated at 2022-06-12 20:59:49.556862
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    '''
    Test cases, with different inputs and expected outputs.
    '''

# Generated at 2022-06-12 20:59:54.701644
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ["/tmp/collection_paths/nope", "test/test_data/test_collections/collection_paths/nope"]

    for path in list_valid_collection_paths(search_paths):
        assert os.path.exists(path)



# Generated at 2022-06-12 20:59:57.046066
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    subdirs = list_collection_dirs()
    assert subdirs is not None
    assert len(list(subdirs)) > 0


# Generated at 2022-06-12 21:00:03.859497
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Valid collection path
    search_path_list = ['/path/foo', '/path/bar']
    assert list_valid_collection_paths(search_path_list) == {'/path/foo', '/path/bar'}

    # Non existing collection path
    search_path_list = ['/baz']
    assert list_valid_collection_paths(search_path_list, warn=True) == set()

    # Collection path with non existing parent
    search_path_list = ['/does_not_exist/foo']
    assert list_valid_collection_paths(search_path_list, warn=True) == set()

# Generated at 2022-06-12 21:00:11.561564
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    with tempfile.TemporaryDirectory() as path:
        with tempfile.NamedTemporaryFile(dir=path) as d:
            search_paths = [nonexistent_path, d.name, path]
            actual = list_valid_collection_paths(search_paths)
            expected = [path]
            assert(actual == expected)


nonexistent_path = '/this/path/does/not/exist'

# Generated at 2022-06-12 21:00:17.913462
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from distutils.version import LooseVersion
    from ansible import __version__

    require_ansible_collections = LooseVersion(__version__) >= LooseVersion('2.9.0')

    test_path = os.path.join(os.path.dirname(__file__), 'unit/ansible_collections')

    # with ansible_collections
    if require_ansible_collections:
        coll_path = os.path.join(test_path, 'ansible_collections')
    else:
        coll_path = test_path

    # test with no ansible_collections

# Generated at 2022-06-12 21:00:29.801531
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert sorted(list(list_collection_dirs(
        search_paths=[os.path.join(os.path.dirname(__file__), 'fixtures')],
        coll_filter="myns1.mycoll1",
    ))) == sorted([b'/dev/null/ansible_collections/myns1/mycoll1'])

    assert sorted(list(list_collection_dirs(
        search_paths=[os.path.join(os.path.dirname(__file__), 'fixtures')],
        coll_filter="myns1",
    ))) == sorted([b'/dev/null/ansible_collections/myns1/mycoll1', b'/dev/null/ansible_collections/myns1/mycoll2'])


# Generated at 2022-06-12 21:00:35.124401
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """This function is used to test the function of
    list_collection_dirs.
    :return:
    """
    # test: return all the collections
    collections = list(list_collection_dirs())
    assert isinstance(collections, list)

    # test: return all collections of a specified namespace
    collections = list(list_collection_dirs(coll_filter='test'))
    assert isinstance(collections, list)

    # test: return a specified collection
    collections = list(list_collection_dirs(coll_filter='test.test'))
    assert isinstance(collections, list)

# Generated at 2022-06-12 21:00:38.508437
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import doctest
    failed, tests = doctest.testmod()
    assert tests > 0
    assert failed == 0

# Generated at 2022-06-12 21:01:14.561429
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils import basic

    basic._ANSIBLE_ARGS = None

    assert [] == list(list_valid_collection_paths())

    assert ['.'] == list(list_valid_collection_paths(search_paths=['.']))
    assert ['.'] == list(list_valid_collection_paths(search_paths=['.', './not-there']))
    assert ['.'] == list(list_valid_collection_paths(search_paths=['.', './not-there/path']))



# Generated at 2022-06-12 21:01:20.572773
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_paths = ['./test/data/dummy_collections_to_test_paths', './test/data/dummy_collections_to_test_paths/ansible_collections']
    coll_dirs = list(list_collection_dirs(search_paths=coll_paths))
    assert len(coll_dirs) == 2, "Failed to load all collection dirs"

# Generated at 2022-06-12 21:01:25.645719
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_search_paths = [
        'non_existing_fake_path',
        os.path.join(os.path.abc, 'non_existing_fake_path'),
        'valid_existing_path',
    ]
    test_collection_roots = list_valid_collection_paths(test_search_paths)

    for test_collection_root in test_collection_roots:
        assert test_collection_root == 'valid_existing_path'



# Generated at 2022-06-12 21:01:36.621132
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    assert set(list_collection_dirs(search_paths=['/tmp/does_not_exist'])) == set()

    assert list_collection_dirs(search_paths=['/tmp/does_not_exist'], warn=True) == []

    coll_path = '/tmp/foo'
    assert set(list_collection_dirs(search_paths=[coll_path])) == set()

    coll_path = '/tmp/foo'
    assert list_collection_dirs(search_paths=[coll_path], warn=True) == []


# Generated at 2022-06-12 21:01:38.571610
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert len(list(list_valid_collection_paths())) > 0
    assert len(list(list_valid_collection_paths(['/does/not/exist']))) == 0



# Generated at 2022-06-12 21:01:50.659804
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys
    import inspect
    test_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    test_path = os.path.join(test_path, '..', '..', '..', 'library', 'ansible', 'module_utils', 'ansible_collections')
    if test_path not in sys.path:
        sys.path.insert(0, test_path)

    from ansible_collections.notstdlib.moveitallout.tests.unit.test_utils import TestConfigReader
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.collection_loader import list_valid_collection_paths, list_collection_dirs

# Generated at 2022-06-12 21:01:58.621657
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    my_paths = []
    my_paths.append('/tmp/does-not-exist')
    my_paths.append('/usr/bin')
    my_paths.append(os.path.join(os.path.dirname(__file__), 'fixtures', 'collection_loader'))

    observed = list(list_valid_collection_paths(my_paths))
    assert observed == [os.path.join(os.path.dirname(__file__), 'fixtures', 'collection_loader')]



# Generated at 2022-06-12 21:02:02.395378
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.foo.bar.plugins.module_utils import v1

    assert v1
    assert v1.__file__ == "plugins/module_utils/v1.py"
    assert False
    #assert os.path.exists(v1.__file__)

# Generated at 2022-06-12 21:02:07.668955
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile

    collection_path_root = '/tmp'
    collection_dir = os.path.join(collection_path_root, 'ansible_collections')
    # os.makedirs(collection_dir)

    path = list_valid_collection_paths(search_paths=[collection_path_root])
    assert path == [collection_path_root]

# Generated at 2022-06-12 21:02:15.194520
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_paths = [
        '/tmp/invalid_collection_search_path',
        '/invalid/collection/search/path',
        '/etc',
        '.',
    ]

    # Warning is defined as non-zero exit code
    assert list(list_valid_collection_paths(search_paths=test_paths, warn=True)) == ['.']

    # No warning if missing
    assert list(list_valid_collection_paths(search_paths=test_paths, warn=False)) == []



# Generated at 2022-06-12 21:02:57.774633
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile
    import time

    b_test_collections_dir = to_bytes(tempfile.mkdtemp(), errors='surrogate_or_strict')
    test_collections_dir = os.path.join(b_test_collections_dir, b'ansible_collections')

    test_namespace1 = os.path.join(test_collections_dir, b'namespace1')
    os.makedirs(test_namespace1)

    test_coll1 = os.path.join(test_namespace1, b'collection1')
    os.makedirs(test_coll1)
    os.makedirs(os.path.join(test_coll1, b'plugins'))


# Generated at 2022-06-12 21:03:09.378765
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import pytest
    from ansible.cli.collection_utils import list_collection_dirs
    from ansible.utils.collection_loader import get_collections_resolver_paths
    import os
    import filecmp
    import tempfile
    import shutil

    def find_file(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def create_dir(new_dir):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

    def create_file(new_file):
        if not os.path.exists(new_file):
            open(new_file, 'a').close()

    # Setup collection structure
    tmp_collections

# Generated at 2022-06-12 21:03:19.761823
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # 1) No search_paths, get config
    default_locations = list(list_valid_collection_paths())

    # 2) List with paths that do not exist
    search_paths = ['this_does_not_exist', 'this_is_a_dir/that_does_not_exist', '/this_is_a_file']
    for path in list_valid_collection_paths(search_paths, warn=True):
        assert False, "Unexpected existing path: %s" % path

    # 3) List that contains config and paths that do not exist
    search_paths = ['this_does_not_exist', 'this_is_a_dir/that_does_not_exist', '/this_is_a_file']
    search_paths.extend(default_locations)

# Generated at 2022-06-12 21:03:27.592640
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test for no collection paths, should yield default
    assert list(list_valid_collection_paths())

    # test for a missing and existing collection path, should yield the one existing
    # test for empty string and None value
    assert list(list_valid_collection_paths(['', None, '/valid_path/', '/bad_path/']))

    # test for a missing and existing collection path, should yield the one existing
    # test for empty string only but with warning
    assert list(list_valid_collection_paths(['', '/valid_path/', '/bad_path/'], True))

