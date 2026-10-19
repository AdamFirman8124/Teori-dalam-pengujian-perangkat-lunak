

# Generated at 2022-06-12 20:53:44.394033
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    path_list = [
        'test/test_data/test_collections',
        'test/test_data/test_collections2',
    ]

    coll_list = list(list_collection_dirs(search_paths=path_list))

    assert len(coll_list) == 7
    assert 'test_collections.test_plugins' in coll_list[0]
    assert 'test_collections.test_plugins2' in coll_list[1]
    assert 'test_collections.test_modules' in coll_list[2]
    assert 'test_collections.test_modules2' in coll_list[3]
    assert 'test_collections2.test_modules' in coll_list[4]
    assert 'test_collections2.test_modules2' in coll_list[5]


# Generated at 2022-06-12 20:53:53.539478
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test function list_valid_collection_paths
    """

    # Test standard usage
    assert list(list_valid_collection_paths(search_paths=["my_subdir"])) == ["my_subdir"]

    # Test missing dir usage
    assert list(list_valid_collection_paths(search_paths=["my_subdir_missing"], warn=False)) == []

    # Test non-dir usage
    assert list(list_valid_collection_paths(search_paths=["/dev/null"], warn=False)) == []

    # Test default path usage
    assert list(list_valid_collection_paths(search_paths=None)) == AnsibleCollectionConfig.collection_paths

# Generated at 2022-06-12 20:53:59.861004
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from tempfile import mkdtemp
    from shutil import rmtree

    # create a collection path that doesn't exist
    tmpdir = mkdtemp()
    rmtree(tmpdir)
    assert None is list_valid_collection_paths([tmpdir])
    assert None is list_valid_collection_paths([tmpdir], warn=True)

    # create a collection path that exists but is not a directory
    with open(tmpdir, 'w') as f:
        f.write("foo")
    assert None is list_valid_collection_paths([tmpdir])
    assert None is list_valid_collection_paths([tmpdir], warn=True)

    # now create a directory, test that this works
    os.mkdir(tmpdir)
    assert tmpdir == list_valid_collection_paths([tmpdir]).next

# Generated at 2022-06-12 20:54:05.496058
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    collection_dir = os.path.join(current_dir, 'data', 'ansible_collections')
    coll_path = [collection_dir]
    coll_list = list_collection_dirs(search_paths=coll_path)
    assert len(coll_list) == 2

# Generated at 2022-06-12 20:54:09.033629
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [
        '/etc/ansible/ansible_collections',
        '/usr/share/ansible/ansible_collections',
    ]

    display.verbosity = 8

    for collection_dir in list_collection_dirs(search_paths=paths):
        print(collection_dir)

# Generated at 2022-06-12 20:54:12.461763
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert True

# Generated at 2022-06-12 20:54:21.123092
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # test with no search paths
    coll_paths = list_collection_dirs()
    assert len(coll_paths) > 0

    # test with multiple search paths
    coll_paths = list_collection_dirs(search_paths=['./test/data/subdir1/subsubdir1', './test/data/subdir2/subsubdir2'])
    assert len(coll_paths) == 2

    # test with invalid search path
    coll_paths = list_collection_dirs(search_paths=['/this_does_not_exist/subsubdir1', './test/data/subdir2/subsubdir2'])
    assert len(coll_paths) == 1

    # test with valid but invalid search path

# Generated at 2022-06-12 20:54:31.010922
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # given
    search_paths = [
        '/tmp/ansible_test_home/test1/ansible_collections',
        '/tmp/ansible_test_home/test2/ansible_collections',
        '/tmp/ansible_test_home/test3/ansible_collections',
    ]
    default_paths = [
        '/usr/share/ansible/collections',
        '/usr/share/ansible/collections/ansible_collections',
        '/etc/ansible/collections',
    ]

    # when
    results = list(list_valid_collection_paths(search_paths=search_paths, warn=False))

    # then
    assert results == default_paths



# Generated at 2022-06-12 20:54:33.329964
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_colls = list_collection_dirs()
    assert isinstance(test_colls, list)
    assert len(test_colls) > 0
    assert '/' in test_colls[0]

# Generated at 2022-06-12 20:54:44.072023
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.utils.path import unfrackpath
    from ansible.utils.display import Display
    from ansible.collections.ansible.community import kubernetes

    display = Display()
    path_to_kube_coll = unfrackpath(kubernetes.__file__)
    kube_path, c = os.path.split(path_to_kube_coll)
    # add the parent directory of where the kubernetes collection exists, we
    # expect this to be included in the results of the list_collection_dirs
    # call
    test_search_paths = ['.', kube_path]

    # list_collection_dirs can be called with no search paths and will fall
    # back to AnsibleCollectionConfig
    # list_collection_dirs should not return the same collection multiple times


# Generated at 2022-06-12 20:55:01.661757
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import pytest

    # note this fixture is not strict as it is only used for a
    # tempdir that is cleaned up after the test
    tmpdir = pytest.ensuretemp("test_list_collection_dirs")

    coll_root = os.path.join(tmpdir, "ansible_collections")
    os.mkdir(coll_root)

    myns = "test_namespace"
    mycoll = "test_collection"

    collpath = os.path.join(coll_root, myns, mycoll)
    os.makedirs(collpath)

    collection_paths = [coll_root]

    # Test for success
    for coll_dir in list_collection_dirs(search_paths=collection_paths):
        assert coll_dir == to

# Generated at 2022-06-12 20:55:12.736467
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader import COLLECTIONS_PATHS
    import tempfile
    import shutil
    import stat
    import os

    r_collections = {
        "mynamespace": {
            "mycollection": None,
            "other_collection": None,
        },
        "othernamespace": {
            "mycollection": None,
            "other_collection": None,
        }
    }

    r_collection_roots = {}

    tmpdir_path = tempfile.mkdtemp()
    tmpfile_path = tempfile.mktemp()


# Generated at 2022-06-12 20:55:19.277649
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_coll_path = os.path.abspath(os.path.join(__file__, '../../test/collections'))
    coll_dir_path = list(list_collection_dirs(search_paths=[test_coll_path]))
    assert len(coll_dir_path) == 3



# Generated at 2022-06-12 20:55:30.853391
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = [
        '/home/test_user/.ansible/collections',
        '/usr/share/ansible/collections',
    ]
    expected_paths = [
        '/home/test_user/.ansible/collections',
        '/usr/share/ansible/collections'
    ]

    valid_paths = list(list_valid_collection_paths(search_paths, True))
    assert expected_paths == valid_paths, 'list_valid_collection_paths should return only valid paths'

    search_paths = [
        '/home/test_user/.ansible/collections',
        '/usr/share/ansible/collections',
        '/invalid/path'
    ]

# Generated at 2022-06-12 20:55:38.809091
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import tempfile
    tempdir = tempfile.mkdtemp("", "collection_load_test")
    os.mkdir(os.path.join(tempdir, "ansible_collections"))
    os.mkdir(os.path.join(tempdir, 'a'))
    os.mkdir(os.path.join(os.path.join(tempdir, "ansible_collections"), 'a'))
    os.mkdir(os.path.join(os.path.join(os.path.join(tempdir, "ansible_collections"), "a"), "b"))
    os.mkdir(os.path.join(os.path.join(os.path.join(os.path.join(tempdir, "ansible_collections"), "a"), "b"), "plugins"))

# Generated at 2022-06-12 20:55:48.093355
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    to_check = [
        "/path1/ansible_collections/namespace/collection",
        "/path2/ansible_collections/namespace/collection",
        "/path3/ansible_collections/namespace/collection",
        "/path1/ansible_collections/other/other_collection",
        "/path2/ansible_collections/other/other_collection",
        "/path3/ansible_collections/other/other_collection",
    ]
    search_paths = [
        "/path1",
        "/path2",
        "/path3",
    ]
    coll_paths = list(list_collection_dirs(search_paths, coll_filter=None))
    assert len(coll_paths) == len(set(coll_paths))

# Generated at 2022-06-12 20:55:54.418862
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test function 'list_valid_collection_paths'
    """
    import tempfile
    import shutil
    import os

    search_paths = []
    paths = []

    test_dir = tempfile.mkdtemp()
    search_paths.append(test_dir)

    # make a file in the folder we just created
    with open(os.path.join(test_dir, "test_file.txt"), 'w') as f:
        f.write("testing")

    # make a folder that we can delete
    test_dir_2 = tempfile.mkdtemp()
    search_paths.append(test_dir_2)

    # build list of valid paths
    for path in list_valid_collection_paths(search_paths):
        paths.append(path)

    # remove

# Generated at 2022-06-12 20:56:05.299512
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.ansible.buildah.tests.unit.compat import unittest
    import os.path
    from ansible.utils import context_objects as co

    class CollectionUtilsTestCase(unittest.TestCase):
        """Unit tests for testing the list_collection_dirs function"""

        def setUp(self):
            self.display = co.GlobalDisplay()
            self.warnings = []

            def _display_warning(msg):
                self.warnings.append(msg)

            self.display.warning = _display_warning

        def tearDown(self):
            self.warnings = []

        def test_list_collection_dirs_default(self):

            # test all collections
            colls = list_collection_dirs()

# Generated at 2022-06-12 20:56:16.855037
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from collections import namedtuple
    from ansible.module_utils.common.collections import is_collection_path

    FORCE_ANSIBLE_COLLECTIONS_PATH = os.environ.get('FORCE_ANSIBLE_COLLECTIONS_PATH')
    if FORCE_ANSIBLE_COLLECTIONS_PATH:
        # Do not test with forced path
        pass
    else:
        Collection = namedtuple('Collection', 'namespace, collection')

# Generated at 2022-06-12 20:56:20.825101
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test function list_collection_dirs
    """
    collection_dirs = list_collection_dirs(['test/utils/mock_collections'], None)
    assert len(list(collection_dirs)) == 2, "There are two collections in mock_collections"


# Generated at 2022-06-12 20:56:41.956963
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.module_utils.common._collections_compat import _collections_compat_config

    # empty collection paths returned if search_paths not set
    for path in list_valid_collection_paths():
        assert path

    # empty collection path returned if search_paths set to empty list
    for path in list_valid_collection_paths([]):
        assert path

    # warning displayed if search_path not found
    w_paths = ['this/path/does/not/exist']
    for path in list_valid_collection_paths(w_paths, warn=True):
        assert path

    # warning not displayed if search_path not found, warn=False
    for path in list_valid_collection_paths(w_paths, warn=False):
        assert path

    # warning displayed if search

# Generated at 2022-06-12 20:56:52.412217
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils._text import to_bytes, to_text

    from ansible.collections.ansible.community import math
    from ansible.collections.ansible import builtin

    search_paths = [
        to_text(math.__path__[0]),
        to_text(builtin.__path__[0])
    ]

    assert to_text(math.show('ip')) == "127.0.0.1"

    count = 0
    for ns_coll in list_collection_dirs(search_paths=search_paths):
        count += 1
        assert to_bytes('ansible_collections') in ns_coll

    # We should have found two different collections
    assert count == 2

# Generated at 2022-06-12 20:56:56.893876
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for function list_collection_dirs
    """

    import ansible.config

    coll_path = os.path.join(os.path.dirname(ansible.config.__file__), 'ansible_collections')

    coll_list = list_collection_dirs(search_paths=[coll_path])

    assert next(coll_list).endswith('ansible_collections/ansible/ansible')

    coll_list = list_collection_dirs(coll_filter='ansible.collection')

    assert next(coll_list).endswith('ansible_collections/ansible/collection')

    coll_list = list_collection_dirs(coll_filter='ansible.col')

    assert not coll_list.next()


# Generated at 2022-06-12 20:57:05.442348
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    ''' check if valid function is working correctly '''

    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # Test for empty list
    result = list(list_valid_collection_paths(search_paths=None))
    assert len(result) == 3
    assert len(set(result)) == 3

    # Test for single valid entry
    result = list(list_valid_collection_paths(search_paths=[os.path.join(os.path.dirname(__file__), '..', 'packaging', 'test_collections', 'ansible_collections')]))
    assert len(result) == 1
    assert len(set(result)) == 1

# Generated at 2022-06-12 20:57:13.275222
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        '../ansible_collections',
        '/invalid/path',
        os.path.join(os.path.dirname(__file__), './ansible_collections'),
        os.path.join(os.path.dirname(__file__), '..'),
    ]

    valid_paths = list_valid_collection_paths(search_paths=search_paths, warn=False)

    # get the full path for the configured ansible_collections dir
    found_path = None
    for path in valid_paths:
        if os.path.basename(path) == 'ansible_collections':
            found_path = path
            break

    # ensure it did not pick up the invalid path

# Generated at 2022-06-12 20:57:23.545403
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # empty
    assert list_valid_collection_paths() == []

    # missing dirs
    assert list_valid_collection_paths(['/foo/bar/something/']) == []

    # existing dirs
    b_test_dir = to_bytes(os.path.dirname(__file__))
    assert list_valid_collection_paths([b_test_dir]) == [b_test_dir]

    # existing dirs with paths and files
    assert list_valid_collection_paths([b_test_dir, './', './list_collections.py']) == [b_test_dir, './']

# Generated at 2022-06-12 20:57:30.673326
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    config_paths = ['/foo', '/bar', '/baz']
    non_existing_paths = ['/does_not/exist']
    file_paths = ['/etc', '/usr/bin']
    paths = config_paths + non_existing_paths + file_paths
    valid_paths = config_paths + file_paths
    result = list(list_valid_collection_paths(paths))
    assert set(result) == set(valid_paths)


# Generated at 2022-06-12 20:57:38.822134
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.plugins.loader import collection_loader

    collection_loader._cache = None  # clear cache

    import tempfile
    import shutil

    c_paths = []

    c_paths.append(os.getcwd())
    c_paths.append('/path/to/nowhere')
    c_paths.append(tempfile.mkdtemp())
    c_paths.append(tempfile.mkdtemp())

    os.makedirs(os.path.join(c_paths[2], 'ansible_collections'))
    os.makedirs(os.path.join(c_paths[3], 'ansible_collections', 'ns1'))

# Generated at 2022-06-12 20:57:49.204098
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test if the function lists the collections from the configured paths
    collection_list_1 = list(list_collection_dirs())

    b_collection_list_1 = []
    for collection in collection_list_1:
        b_collection_list_1.append(to_bytes(collection))

    # Test if the function lists the collections from a custom path
    collection_list_2 = list(list_collection_dirs(['/tmp']))

    b_collection_list_2 = []
    for collection in collection_list_2:
        b_collection_list_2.append(to_bytes(collection))

    # Test if the function lists the collection from multiple custom paths
    collection_list_3 = list(list_collection_dirs(['/tmp', '/home']))

    b_collection_list_3 = []

# Generated at 2022-06-12 20:57:58.050169
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/tmp', '/tmp/foo', '/tmp/bar']) == ['/tmp', '/tmp/foo', '/tmp/bar']
    # remove not existing paths
    assert list_valid_collection_paths(['/tmp', '/tmp/foo', '/tmp/bar']) == ['/tmp']
    # not existing path, with warn
    assert list_valid_collection_paths(['/tmp', '/tmp/foo', '/tmp/bar'], True) == []
    # path is not a directory, with warn
    assert list_valid_collection_paths(['/tmp', '/tmp/foo', '/tmp/bar'], True) == []


# Generated at 2022-06-12 20:58:39.312618
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test valid collection paths
    test_search_paths = [
        'a_valid_path',
        'another_valid_path',
    ]
    expected_res = ['a_valid_path', 'another_valid_path']
    results = list(list_valid_collection_paths(test_search_paths))
    assert sorted(expected_res) == sorted(results)

    test_search_paths = [
        'a_valid_path',
        'another_valid_path',
        'a_non_existent_path',
        'another_non_existent_path',
    ]
    expected_res = ['a_valid_path', 'another_valid_path']
    results = list(list_valid_collection_paths(test_search_paths))
    assert sorted(expected_res) == sorted

# Generated at 2022-06-12 20:58:46.743761
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    dummy_path = os.path.join(os.getcwd(), 'test', 'unit', 'ansible_collections')

    test_paths = AnsibleCollectionConfig(loader=DataLoader()).collection_paths

    for path in list_collection_dirs(search_paths=test_paths + [dummy_path]):
        assert path.startswith(dummy_path)

# Generated at 2022-06-12 20:58:51.128484
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common.collections import list_valid_collection_paths
    assert list(list_valid_collection_paths(['/tmp'])) == ['/tmp']
    assert list(list_valid_collection_paths()) == AnsibleCollectionConfig.collection_paths

# Generated at 2022-06-12 20:58:58.907531
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    invalid_paths = [
        'invalid-path',  # invalid path
        AnsibleVaultEncryptedUnicode(''),  # invalid/secured path
        'localhost:'  # invalid secure path
    ]

    paths = list_valid_collection_paths(invalid_paths, warn=True)
    assert len(list(paths)) == len(list(list_valid_collection_paths()))

    paths = list_valid_collection_paths(invalid_paths, warn=False)
    assert len(list(paths)) == len(list(list_valid_collection_paths()))

# Generated at 2022-06-12 20:59:10.947215
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test with empty path list
    assert [] == list(list_valid_collection_paths())

    # test with default
    default = (['/usr/share/ansible/collections', '/home/redhat/.ansible/collections'])
    assert len(default) == len(list(list_valid_collection_paths()))

    # test that non-existent path doesn't break
    assert [] == list(list_valid_collection_paths(search_paths=['/foo/bar']))

    # test one valid path
    assert ['/foo/bar'] == list(list_valid_collection_paths(search_paths=['/foo/bar']))

    # test one non-existent path

# Generated at 2022-06-12 20:59:18.894045
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    temp_dir = tempfile.TemporaryDirectory()

    # create a collection root at temp_dir
    b_coll_root = os.path.join(temp_dir.name, b'ansible_collections')
    os.mkdir(b_coll_root)

    # create a namespace at collection root
    b_namespace_dir = os.path.join(b_coll_root, b'namespace')
    os.mkdir(b_namespace_dir)

    # create a collection under namespace
    b_coll_dir = os.path.join(b_namespace_dir, b'collectionA')
    os.mkdir(b_coll_dir)

    # create another collection under namespace
    b_coll_dir = os.path.join(b_namespace_dir, b'collectionB')

# Generated at 2022-06-12 20:59:28.742120
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile
    import shutil

    dirs = []
    dirs.append(tempfile.mkdtemp())
    dirs.append(tempfile.mkdtemp())
    dirs.append(tempfile.mkdtemp())

    AnsibleCollectionConfig.load()

    # test only good paths are returned
    assert set(dirs) == set(list_valid_collection_paths(dirs))

    # add a few non-existent and non-directory paths to the mix
    dirs.append(tempfile.mktemp())
    dirs.append(tempfile.mktemp())

    assert set(dirs[:-2]) == set(list_valid_collection_paths(dirs))

    # also test handling of default collection paths

# Generated at 2022-06-12 20:59:32.563024
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
  # test valid_search_paths with default paths
  with open('/tmp/a.txt') as f:
      assert list_valid_collection_paths(search_paths=list()) == list(ansible_collections.ansible_collections)


# Generated at 2022-06-12 20:59:39.576890
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    #  empty list
    assert list(list_valid_collection_paths()) == []

    # nonexistent path
    assert list(list_valid_collection_paths(search_paths=['/tmp/i-do-not-exist'])) == []

    # path to non-dir
    with open('/tmp/test_not_dir', 'w') as handle:
        handle.write('test')
    assert list(list_valid_collection_paths(search_paths=['/tmp/test_not_dir'])) == []

    # path to directory
    os.mkdir('/tmp/test_dir')
    assert list(list_valid_collection_paths(search_paths=['/tmp/test_dir'])) == ['/tmp/test_dir']

# Generated at 2022-06-12 20:59:49.557807
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # construct test collections dir
    import tempfile
    import shutil
    test_root = tempfile.mkdtemp()

    def create_collection(root, collection_path):
        # set to lower case as some distros mount tmp filesystems case insensitive
        collection_path = collection_path.lower()
        b_test_root = to_bytes(root, errors='surrogate_or_strict')
        b_path = to_bytes(os.path.sep.join(collection_path.split('.')), errors='surrogate_or_strict')

        b_collection_dir = os.path.join(b_test_root, b_path)
        os.makedirs(b_collection_dir)
        return b_collection_dir

    # fake collections

# Generated at 2022-06-12 21:00:28.522991
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_list = ['.']
    assert len(list(list_valid_collection_paths(valid_list))) > 0
    invalid_list = ['']
    assert len(list(list_valid_collection_paths(invalid_list))) == 0
    valid_invalid_list = ['.', '']
    assert len(list(list_valid_collection_paths(valid_invalid_list))) > 0


# Generated at 2022-06-12 21:00:38.412389
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    DISPLAY_PATH = 'ansible.test.collection'
    COLLECTION_PATH = 'ansible_collections/ansible/test/collection'
    COLLECTED_PATH = 'ansible_collections/ansible/test/collected/collection'

    def assertDisplayPath(p, dp):
        assert to_bytes(dp) == list_collection_dirs(p).next()

    def assertPath(p, cp):
        paths = list(list_collection_dirs(p))
        assert len(paths) == 1, "Expected only 1 path but found %s" % len(paths)
        assert to_bytes(cp).endswith(paths[0])

    assertPath(['/not_a/path', '/not_a/path2'], COLLECTION_PATH)

# Generated at 2022-06-12 21:00:49.233118
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test that the collection paths are correctly detected
    """

    coll_paths = list_valid_collection_paths()
    assert len(coll_paths) == 3

    # just one directory configured
    coll_paths = list_valid_collection_paths(['/tmp'])
    assert len(coll_paths) == 1

    # add a non-existant directory
    coll_paths = list_valid_collection_paths(['/tmp', '/non_existant_path'])
    assert len(coll_paths) == 1

    # add a non-directory
    coll_paths = list_valid_collection_paths(['/tmp', '/etc/fstab'])
    assert len(coll_paths) == 1

    # add an existing directory
    coll_paths = list_valid_

# Generated at 2022-06-12 21:01:00.104800
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    #Test 1: None search_paths, should pass
    assert list(list_valid_collection_paths())

    #Test 2: Empty path, should not pass
    assert not list(list_valid_collection_paths([""]))

    #Test 3: Non-existing search_paths, should not pass
    assert not list(list_valid_collection_paths(["/non-existing/path"]))

    #Test 4: Valid search_path, should pass
    assert list(list_valid_collection_paths(["./ansible_collections"]))

    #Test 5: Valid search_path as root, should pass
    with open('collection_loader/__init__.py', 'r') as fp:
        assert list(list_valid_collection_paths(["/"]))

# Generated at 2022-06-12 21:01:09.811335
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import ansible.module_utils._text

    coll_root = tempfile.mkdtemp()


# Generated at 2022-06-12 21:01:21.642266
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths in util.py
    """
    # No args
    path_list = list(list_valid_collection_paths())
    assert len(path_list) == 1
    assert path_list[0] == AnsibleCollectionConfig.default_collection_path

    # Cleared args
    path_list.clear()
    for path in path_list:
        assert path not in list_valid_collection_paths(search_paths=path_list)

    # Test list_valid_collection_paths() with default
    path_list.clear()
    path_list.append(AnsibleCollectionConfig.default_collection_path)
    for path in path_list:
        assert path in list_valid_collection_paths()



# Generated at 2022-06-12 21:01:28.120363
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_path = os.path.abspath("tests/data/collection")
    search_paths = [collection_path]

    assert list_collection_dirs(search_paths=search_paths) == []
    assert list_collection_dirs(search_paths=search_paths, coll_filter="namespace.collection") == ["/path/to/collection"]
    assert list_collection_dirs(search_paths=search_paths, coll_filter="namespace") == ["/path/to/collection"]

# Generated at 2022-06-12 21:01:29.622596
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert ('/collections' in list_valid_collection_paths())



# Generated at 2022-06-12 21:01:39.194945
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile

    test_ns = 'myns'
    test_coll = 'mycoll'
    test_coll_dir = os.path.join(test_ns, test_coll)
    test_collection_paths = [os.path.join(tempfile.gettempdir(), 'ansible-module-tests')]
    expected_collection_path = os.path.join(test_collection_paths[0], 'ansible_collections', test_ns, test_coll)
    os.makedirs(os.path.join(test_collection_paths[0], 'ansible_collections', test_ns))


# Generated at 2022-06-12 21:01:51.316327
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    def _test_list_collection_dirs(colls, search_paths, coll_filter, expected):

        path_function = lambda : list(list_collection_dirs(search_paths, coll_filter))

        # collections is None and coll_filter is None
        assert list(colls) == expected

        # collections not None and coll_filter is none
        assert list(colls) == expected

        # coll_filter is set and collections is None, empty
        assert list(colls) == expected

        # coll_filter matches
        assert _test_list_collection_dirs(colls, search_paths, "test_ns.test_coll_name", [b'/path/to/collections/test_ns/test_coll_name'])

# Generated at 2022-06-12 21:03:00.792654
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    collection_dirs = [
        'ansible_collections/mynamespace1/mycollection1',
        'ansible_collections/mynamespace1/mycollection2',
        'ansible_collections/mynamespace1/mycollection3',
        'ansible_collections/mynamespace2/mycollection1',
        'ansible_collections/mynamespace2/mycollection2',
        'ansible_collections/mynamespace2/mycollection3',
        'ansible_collections/mynamespace3/mycollection1',
        'ansible_collections/mynamespace3/mycollection2',
        'ansible_collections/mynamespace3/mycollection3',
    ]

# Generated at 2022-06-12 21:03:12.611470
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os
    import pytest

    _, tmp_path = tempfile.mkstemp()
    tmp_path = os.path.dirname(tmp_path)
    tmp_ns = "tmp.faked_ns"
    tmp_coll = "faked_coll"

    coll_root_path = os.path.join(tmp_path, "ansible_collections")
    ns_root_path = os.path.join(coll_root_path, tmp_ns)
    coll_root_path = os.path.join(ns_root_path, tmp_coll)

    os.makedirs(coll_root_path)

    collection_dirs = list(list_collection_dirs([tmp_path]))


# Generated at 2022-06-12 21:03:21.706014
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Ensure that passing in just the path works
    for path1 in list_valid_collection_paths(search_paths=["/tmp/my_collection_path"]):
        assert '/tmp/my_collection_path' in path1

    # Ensure that we do not get duplicate paths
    path_list = ["/tmp/my_collection_path", "/tmp/my_collection_path"]
    for path2 in list_valid_collection_paths(search_paths=path_list):
        path_list.remove(path2)
        assert path2 in path_list
        assert len(path_list) == 0

    # Ensure that we will warn if path doesn't exist
    path_list = ["/tmp/my_collection_path_DOES_NOT_EXIST"]

# Generated at 2022-06-12 21:03:25.556986
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    collections = list_collection_dirs(coll_filter='community.general')
    for path in collections:
        print(path)

if __name__ == '__main__':
    test_list_collection_dirs()