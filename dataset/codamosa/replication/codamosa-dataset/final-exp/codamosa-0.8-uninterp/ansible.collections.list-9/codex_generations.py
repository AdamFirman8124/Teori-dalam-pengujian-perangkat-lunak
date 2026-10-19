

# Generated at 2022-06-12 20:53:37.811039
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert len(list(list_collection_dirs(coll_filter='ansible_collections.misc.not_a_real_collection'))) == 0
    assert len(list(list_collection_dirs(coll_filter='ansible_collections.not_a_real_namespace'))) == 0
    assert len(list(list_collection_dirs(coll_filter='not_a_real_namespace'))) == 0

# Generated at 2022-06-12 20:53:47.638386
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_paths = [
        '/tmp/ansible_collections',
        '/tmp/ansible_collections/jctanner',
        '/tmp/ansible_collections/jctanner/example',
        '/tmp/ansible_collections/jctanner/my_collection',
        '/tmp/ansible_collections/jctanner/unsupported_collection',
        '/tmp/ansible_collections/jctanner/another_collection']

    # Verify all expected collection directories returned
    for path in list_collection_dirs(collection_paths):
        assert os.path.basename(path) in [
            b'example',
            b'my_collection',
            b'another_collection']

    # Verify only the collection directory specified is returned

# Generated at 2022-06-12 20:53:54.938441
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for list_collection_dirs
    """
    from tempfile import mkdtemp
    from shutil import rmtree

    cwd = os.getcwd()

    # Setup a fake collection namespace
    coll_root = mkdtemp()
    test_namespace = 'test_namespace'
    test_collection = ['test_plugin', 'test_module']
    coll_namespace_dir = os.path.join(coll_root, test_namespace)
    coll_namespace_dir = to_bytes(coll_namespace_dir)

    os.mkdir(coll_namespace_dir)

    # Setup a fake collection
    coll_dir = os.path.join(coll_namespace_dir, test_collection[0])
    os.mkdir(coll_dir)

    os.chdir

# Generated at 2022-06-12 20:53:57.068602
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = list(list_valid_collection_paths(['/dev/null']))
    assert len(paths) == 1
    assert paths[0] == '/dev/null'

# Generated at 2022-06-12 20:54:06.654637
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # explicitly test empty
    assert list_valid_collection_paths([]) == []

    # explicitly test non-existing path
    assert list_valid_collection_paths(['/non-existing-path']) == []

    # explicitly test existing directory
    test_dir = os.path.dirname(os.path.realpath(__file__))
    assert list_valid_collection_paths([test_dir]) == [test_dir]

    # explicitly test existing file
    assert list_valid_collection_paths([__file__]) == []



# Generated at 2022-06-12 20:54:13.033290
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    print("\nGoing to test function list_valid_collection_paths()")
    # test single valid path
    valid_path = "/home/user/ansible"
    print("Test single valid path")
    print("Input : {0}".format(valid_path))
    print("OUTPUT : {0}".format(list(list_valid_collection_paths([valid_path]))))
    # test multiple valid paths
    valid_path_1 = "/home/user/ansible"
    valid_path_2 = "/home/user/ansible2"
    print("Test multiple valid paths")
    print("Input : {0} {1}".format(valid_path_1, valid_path_2))

# Generated at 2022-06-12 20:54:21.772754
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Makes sure the dir paths of the collections are returned correctly
    """

    # simple test: unencoded name
    paths = list_collection_dirs(search_paths=['test/testdata/collections'], coll_filter='amazon.aws')
    assert paths[0].endswith('test/testdata/collections/ansible_collections/amazon/aws')

    # simple test: encoded name
    paths = list_collection_dirs(search_paths=['test/testdata/collections'], coll_filter='ansible.posix')
    assert paths[0].endswith('test/testdata/collections/ansible_collections/ansible.posix')

    # simple test: unencoded name, non-existent collection

# Generated at 2022-06-12 20:54:28.419179
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(["/tmp/bad/path", "/tmp/real/path"])) == ["/tmp/real/path"]
    assert list(list_valid_collection_paths(["/tmp/bad/path", "/tmp/real/path"], warn=False)) == ["/tmp/real/path"]
    assert list(list_valid_collection_paths(["/tmp/bad/path", "/tmp/real/path"], warn=True)) == ["/tmp/real/path"]

# Generated at 2022-06-12 20:54:36.189293
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    bad_paths = ('/usr/bin/python3', '/etc/passwd', 'DISPLAY = foo')

    for i in bad_paths:
        res = list_valid_collection_paths([i])
        assert res is None

    with tempfile.NamedTemporaryFile(prefix='ansible_collections_', suffix='_dir') as tmpdir:
        res = list_valid_collection_paths([tmpdir.name])
        assert res is None

    with tempfile.NamedTemporaryFile(prefix='ansible_collections_', suffix='.py') as tmpfile:
        res = list_valid_collection_paths([tmpfile.name])
        assert res is None

    # _list_collection_dirs is already unit tested, so if it returns a generator, this takes that as good


# Generated at 2022-06-12 20:54:47.228126
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.release import __version__
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    a1 = AnsibleCollectionConfig(search_paths=["/coll1"], collection_list=[])
    assert set(list_valid_collection_paths(search_paths=["/coll1"], warn=True)) == {"/coll1"}

    a2 = AnsibleCollectionConfig(search_paths=["/coll1", "/coll2", "/coll3", "/coll4"], collection_list=[])
    assert set(list_valid_collection_paths(search_paths=["/coll1", "/coll2", "/coll3", "/coll4"], warn=True)) == {"/coll1", "/coll2", "/coll3", "/coll4"}


# Generated at 2022-06-12 20:55:02.655683
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from shutil import rmtree
    from tempfile import mkdtemp
    import os

    test_dir = mkdtemp(prefix='ansible-test-collections')


# Generated at 2022-06-12 20:55:12.928368
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    good_1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    good_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    good_3 = os.path.dirname(os.path.abspath(__file__))
    good_4 = os.path.abspath(__file__)
    bad_1 = os.path.abspath(__file__) + '.bogus'
    bad_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library')
    bad_3 = os.path.join(os.path.abspath(__file__), 'library')


# Generated at 2022-06-12 20:55:21.086857
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test defaults
    result = list(list_valid_collection_paths(None))
    assert result

    # test relative paths based on default
    result = list(list_valid_collection_paths(["library", "filter_plugins"]))
    assert result

    # test additional paths
    result = list(list_valid_collection_paths(["/etc/ansible/collections", "/usr/share/ansible/collections", "roles", "plugins"]))
    assert result


# Generated at 2022-06-12 20:55:25.965626
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # search_paths can be any string list of paths
    search_paths = ['path1', 'path2']
    # get the subset of valid paths
    results = list(list_valid_collection_paths(search_paths))
    # compare the results with the original list to see which were filtered out
    assert search_paths == results



# Generated at 2022-06-12 20:55:32.740430
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_paths = list_valid_collection_paths(
        search_paths=['/dev/null', '/etc', '/usr/share/ansible'],
        warn=True
    )
    assert next(test_paths) == '/usr/share/ansible'
    with pytest.raises(StopIteration):
        next(test_paths)



# Generated at 2022-06-12 20:55:39.787706
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """test for valid collection paths"""
    assert list_valid_collection_paths(['foo']) == []
    assert list_valid_collection_paths(['foo', 'bar']) == []
    assert list_valid_collection_paths(['/usr/share']) == ['/usr/share']
    assert list_valid_collection_paths(['/usr/share/ansible_collections']) == ['/usr/share/ansible_collections']
    assert list_valid_collection_paths(['/usr/share/ansible_collections/', '/usr/share']) == ['/usr/share/ansible_collections/', '/usr/share']

# Generated at 2022-06-12 20:55:48.884347
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import os
    import pytest

    # if no collection paths then set to default
    search_paths = []
    coll_paths = list_valid_collection_paths(search_paths, warn=False)
    assert coll_paths == AnsibleCollectionConfig.collection_paths

    # check that collection paths works if valid paths are passed in
    coll_dir = tempfile.mkdtemp(prefix="ansible_collections_dir_")
    coll_dir1 = tempfile.mkdtemp(prefix="ansible_collections_dir_")
    search_paths = [coll_dir, coll_dir1, '/bad/path/not/existent', '/tmp']

    coll_paths = list_valid_collection_paths(search_paths, warn=False)


# Generated at 2022-06-12 20:55:55.204624
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp
    from shutil import rmtree
    import sys
    import os

    tmp_dir = mkdtemp(prefix='ansible_collections_test_')
    search_paths = [tmp_dir, 'boguspath']
    for path in search_paths:
        assert path in list_valid_collection_paths(search_paths)

    # setup test collection
    ns_dir = os.path.join(tmp_dir, 'ansible_namespace')
    coll_dir = os.path.join(tmp_dir, 'ansible_namespace.collection')
    os.mkdir(ns_dir)
    os.mkdir(coll_dir)

    assert ns_dir in list_valid_collection_paths(search_paths)
    assert coll_dir in list_

# Generated at 2022-06-12 20:56:05.806323
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import pytest
    import tempfile
    import shutil

    def create_collections(tmpdir):
        """ create the following collections and return the collection root

            collections
            |- test1
            |  |- collection1
            |  |- collection2
            |- test2
            |  |- collection1
            |  |- collection2
        """

        os.makedirs(os.path.join(tmpdir, "test1", "collection1"))
        os.makedirs(os.path.join(tmpdir, "test1", "collection2"))
        os.makedirs(os.path.join(tmpdir, "test2", "collection1"))
        os.makedirs(os.path.join(tmpdir, "test2", "collection2"))
        return tmpdir


# Generated at 2022-06-12 20:56:10.044706
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """

    :return:
    """
    test_paths = ['bogus', '/etc', '~/ansible']
    v_paths = list(list_valid_collection_paths(test_paths))
    assert v_paths == ['/etc']

# Generated at 2022-06-12 20:56:20.462744
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test with existing directory
    search_paths = ["/tmp"]
    expected_result = ["/tmp"]
    result = list(list_valid_collection_paths(search_paths=search_paths))
    assert result == expected_result, "expected %s, got %s" % (expected_result, result)

    # Test with non existing directory
    search_paths = ["/non/existing/path"]
    result = list(list_valid_collection_paths(search_paths=search_paths))
    assert result == [], "expected empty list, got %s" % result

    # Test with existing file
    search_paths = ["/etc/fstab"]
    result = list(list_valid_collection_paths(search_paths=search_paths))

# Generated at 2022-06-12 20:56:25.325186
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_coll_paths = ['/dev/null', '/not/a/dir', '/tmp']

    results = list_valid_collection_paths(test_coll_paths, True)
    assert list(results) == []

# Generated at 2022-06-12 20:56:33.824207
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Unit test for function list_valid_collection_paths
    """

    import tempfile

    # test that existing paths are returned
    dummy_collections_path = tempfile.mkdtemp(prefix='ansible_collections_')
    existing_paths = list_valid_collection_paths([dummy_collections_path])
    assert next(existing_paths) == dummy_collections_path

    # test that non existing paths are not returned
    os.rmdir(dummy_collections_path)
    no_paths = list_valid_collection_paths([dummy_collections_path])
    assert list(no_paths) == []

    # test that non existing paths are not returned
    os.mkdir(dummy_collections_path)

# Generated at 2022-06-12 20:56:37.616919
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    print('test_list_collection_dirs')
    list_of_collections = list_collection_dirs(["./tests"], "test_nsp")
    for col in list_of_collections:
        print('col: {0}'.format(col))

# Generated at 2022-06-12 20:56:48.582307
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil

    # Test with empty search paths
    search_paths = []
    assert list(list_valid_collection_paths(search_paths)) == []

    # Test with non-existing path
    search_paths.append('/some/non-existing/path')
    assert list(list_valid_collection_paths(search_paths)) == []

    # Test with existing path that is not a directory
    with tempfile.NamedTemporaryFile() as tf:
        search_paths.append(tf.name)
        assert list(list_valid_collection_paths(search_paths)) == []

    # Test with existing path that is not a collection directory
    with tempfile.TemporaryDirectory() as td:
        search_paths.append(td)

# Generated at 2022-06-12 20:56:55.458076
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    with test_collection_root() as root:
        # Single valid dir
        paths = [os.path.join(root, 'test')]
        results = list(list_valid_collection_paths(search_paths=paths))
        assert len(results) == 1
        assert results[0] == paths[0]

        # Single invalid dir
        paths = [os.path.join(root, 'invalid')]
        results = list(list_valid_collection_paths(search_paths=paths, warn=False))
        assert len(results) == 0

        # Multiple valid dirs
        subdir = os.path.join(root, 'collections')
        os.mkdir(subdir)
        paths = [root, subdir]

# Generated at 2022-06-12 20:57:06.335210
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Ensure that the list of collection directories is filtered correctly
    """
    valid_collections = []
    collection_paths = [
        '../lib/ansible/modules/network/f5',
        '../lib/ansible/modules/utilities/logic/',
        '../lib/ansible/modules/utilities/',
        '../lib/ansible/modules/storage/netapp',
        '../lib/ansible/modules/notification/hipchat',
        '../lib/ansible/modules/notification/',
        '../lib/ansible/modules/cloud/amazon',
        '../lib/ansible/modules/cloud/',
        '../',
    ]
    print('\nList collection directories with default arguments')

# Generated at 2022-06-12 20:57:09.966256
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ["/random/path/does/not/exist","/etc/ansible/collections/ansible_collections/ns/coll"]
    assert list(list_valid_collection_paths(search_paths)) == ["/etc/ansible/collections/ansible_collections/ns/coll"]


# Generated at 2022-06-12 20:57:13.508406
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['./test/sanity/code/ansible_collections', './test/units/modules/test_collections/fake_collections']
    coll_dirs = list(list_collection_dirs(search_paths))
    assert len(coll_dirs) == 2


# Generated at 2022-06-12 20:57:25.896529
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test empty list
    assert list(list_valid_collection_paths([])) == []

    # Test single non-existing dir
    assert list(list_valid_collection_paths(["/foo/bar/baz"])) == []

    # Test mix of existing and non-existing dirs
    assert list(list_valid_collection_paths(["tests", "/foo/bar/baz"])) == ["tests"]

    # Test a non-existing dir mixed with another existing dir
    assert list(list_valid_collection_paths(["tests", "/foo/bar/baz"])) == ["tests"]

    # Test a non-existing dir mixed with another existing dir
    assert list(list_valid_collection_paths(["tests", "/foo/bar/baz"])) == ["tests"]

    # Test a non-existing dir mixed

# Generated at 2022-06-12 20:57:40.709211
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader import collection_loader
    import tempfile
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # set to True for debugging
    DEBUG = False

    # only run this test when we are able to create a temp dir to work in
    if os.path.exists(tempfile.gettempdir()):
        tempdir = tempfile.mkdtemp()

        if DEBUG:
            print('Created tempdir %s' % tempdir)

        # create fake collections

# Generated at 2022-06-12 20:57:45.241844
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    search_paths = ['/foo/bar', tempfile.gettempdir(), '/tmp/baz']
    search_paths = list(list_valid_collection_paths(search_paths))
    assert search_paths[0] == tempfile.gettempdir()

# Generated at 2022-06-12 20:57:55.858218
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.release import __version__

    # this test is hacky, we need to do something with the collection dirs to put them in the C.COLLECTION_DIRS cache so
    # that ansible.module_utils.ansible_collections.ansible.module_utils.foo._load_module_spec can find them

    import six
    import sys
    import json

    from ansible.module_utils.basic import AnsibleModule

    test_module = 'test_collection.test_namespace.foobar_test'
    test_module_path = os.path.join(os.getcwd(), 'test/units/module_utils/test_collections/test_namespace/plugins/modules/foobar_test.py')
    retval = AnsibleModule(argument_spec={}, supports_check_mode=True).run

# Generated at 2022-06-12 20:58:03.121362
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_coll_paths = [
        os.path.join(os.path.dirname(__file__), 'data/collections'),
    ]

    # Test empty coll_filter
    result_list = list(list_collection_dirs(search_paths=test_coll_paths))
    assert result_list == [
        b'ansible.builtin',
        b'ansible.module_utils',
        b'ns_a.coll_a',
        b'ns_a.coll_b',
        b'ns_a.coll_c',
        b'ns_b.coll_a',
        b'ns_b.coll_b',
        b'ns_b.coll_c'
    ]

    # Test with a namespace

# Generated at 2022-06-12 20:58:09.458003
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = [
        "~/fakeroot/ansible_test/test_collections",
        "~/fakeroot/ansible_test/test_collections2",
        "~/fakeroot/fake_ansible_test"]
    b_search_paths = [to_bytes(p) for p in search_paths]
    valid_paths = list(list_valid_collection_paths(b_search_paths, warn=False))

    assert b_search_paths[0] in valid_paths
    assert b_search_paths[1] in valid_paths
    assert len(valid_paths) == 2



# Generated at 2022-06-12 20:58:18.327833
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.path import unfrackpath

    def normalize_paths(path):
        return [unfrackpath(x) for x in path]

    def compare_path(test_paths, orig_paths):
        assert len(test_paths) == len(orig_paths),\
            "%s Original Collection Path(s) Found."\
            "  %s Test Path(s) Found." % (len(orig_paths), len(test_paths))

        for i in orig_paths:
            assert i in test_paths, \
                "Failed to find original collection path %s" % i


# Generated at 2022-06-12 20:58:29.371774
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test for Listing all collections
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    my_file = os.path.join(cur_dir, 'my_collection_path')
    if os.path.exists(my_file):
        os.remove(my_file)

    if os.path.exists(my_file):
        os.remove(my_file)
    if os.path.exists(my_file + '1'):
        os.remove(my_file + '1')

    all_collections = list(list_collection_dirs(search_paths=[my_file], coll_filter=None))

    # Test for Listing a specific collection
    collection_filter = 'namespace1.collection1'

# Generated at 2022-06-12 20:58:37.965747
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [
        'test/unit/utils/collection_loader/test_collection_path_1',
        'test/unit/utils/collection_loader/test_collection_path_2',
    ]
    collection_dir = 'test_collection_dir_1'
    collection_dirs = set(list_collection_dirs(paths, coll_filter=collection_dir))
    assert collection_dirs == {u'test/unit/utils/collection_loader/test_collection_path_1/ansible_collections/test1/test_collection_dir_1'}



# Generated at 2022-06-12 20:58:45.128540
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test list_collection_dirs
    """
    import tempfile
    import shutil
    test_dir = tempfile.mkdtemp()


# Generated at 2022-06-12 20:58:56.869839
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    all_collections = ['namespace.collection', 'namespace.other_collection', 'other_namespace.collection', 'other_namespace.other_collection']

    search_paths = ['/collection_search_path1', '/collection_search_path2']

    # Don't use list_collection_dirs, use os.listdir to compare expected results
    # with actual results to avoid recursion of this function
    # (i.e. do: if os.path.basename(path) != 'ansible_collections': path = os.path.join(path, 'ansible_collections'))
    expected_dirs = []
    for path in search_paths:
        for collection in all_collections:
            expected_dirs.append(os.path.join(path, 'ansible_collections', collection))

   

# Generated at 2022-06-12 20:59:12.279803
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for list_collection_dirs
    """
    # Arrange
    mock_paths = ['/test/path', '/second/test/path']

    # Action
    # Assert
    assert mock_paths == list(list_collection_dirs(mock_paths))

# Generated at 2022-06-12 20:59:19.636960
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common._collections_compat import Path

    test_paths = {
        'ansible_collections': ['/home/user/.ansible/collections', '/etc/ansible/collections', '/usr/share/ansible/collections'],
        'custom_collections': ['/home/user/.ansible/custom_collections', '/etc/ansible/custom_collections', '/usr/share/ansible/custom_collections'],
    }
    for (coll_type, default_paths) in test_paths.items():
        # test with empty list
        search_paths = []
        assert list(list_valid_collection_paths(search_paths)) == default_paths

        # test with good paths
        search_paths = default_paths

# Generated at 2022-06-12 20:59:29.134359
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    test_coll_path = tempfile.mkdtemp(prefix="ansible_collections_test_")
    os.makedirs(os.path.join(test_coll_path, "some_namespace", "some_collection"))

    assert len(list(list_collection_dirs([test_coll_path]))) == 1

    assert len(list(list_collection_dirs([test_coll_path], "some_namespace.some_collection"))) == 1

    assert len(list(list_collection_dirs([test_coll_path], "some_namespace"))) == 1

    assert len(list(list_collection_dirs([test_coll_path], "some_other_namespace"))) == 0

    assert len(list(list_collection_dirs([test_coll_path], "")))

# Generated at 2022-06-12 20:59:34.601216
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    This function tests the list_valid_collection_paths function when
    it is run in the following scenario:
    - A given valid path
    - A given invalid one
    """

    given_valid_path = 'test'
    given_invalid_path = '/test'

    results = list(list_valid_collection_paths([given_valid_path, given_invalid_path]))
    assert results == [given_valid_path]


# Generated at 2022-06-12 20:59:42.407034
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # A directory which does not exist.
    not_exists_dir = ['/not_exists_dir']

    # A directory that exists but is not readable
    not_readable_dir = ['/root']

    # A directory which does not contain "ansible_collections" directory.
    # This should not be considered as a valid collection search path.
    no_coll_dir = ['/usr']

    # A directory which contains "ansible_collections" directory.
    coll_dir = ['/usr/share']

    # A file, should not be considered as a valid search path.
    is_file = ['/bin/ls']

    # Empty lists shouldn't raise any errors.
    empty = []

    # Configured search path, that doesn't exist.

# Generated at 2022-06-12 20:59:51.851230
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test a non-existent search path
    new_path = '/path/to/ansible_collections/new_col'
    found_collections = list(list_collection_dirs(search_paths=[new_path]))
    assert not found_collections

    # Test an existing search path
    new_path = os.path.join(os.path.dirname(__file__), 'data', 'ansible_collections')
    found_collections = list(list_collection_dirs(search_paths=[new_path]))
    assert len(found_collections) == 2
    assert found_collections[0].endswith(b'new_col/new_ns/new_coll')

# Generated at 2022-06-12 21:00:02.216694
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil
    import pytest

    # create a temp directory and a collection in it
    tmp_dir = tempfile.mkdtemp()

    # create a collection dir
    collection_dir = os.path.join(tmp_dir, 'ansible_collections', 'ns1', 'collection1')
    os.makedirs(collection_dir)

    # create a file in the temp dir
    open(os.path.join(tmp_dir, 'test.txt'), 'w').close()

    # create a file in the temp dir
    open(os.path.join(tmp_dir, 'mycollection'), 'w').close()

    # create a file in the temp dir
    open(os.path.join(tmp_dir, 'mycollection.tar.gz'), 'w').close()

    # create a file

# Generated at 2022-06-12 21:00:13.374444
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile

    tst_path = tempfile.mkdtemp()

    search_paths = [
        os.path.join(tst_path, 'coll_path_1'),
        os.path.join(tst_path, 'coll_path_2'),
        os.path.join(tst_path, 'coll_path_3'),
        os.path.join(tst_path, 'coll_path_4'),
    ]

    for p in search_paths:
        os.mkdir(p)

    search_paths.append('/an_invalid_coll_path')

    coll_paths = list(list_valid_collection_paths(search_paths))

    assert(len(coll_paths) == len(search_paths) - 1)

# Generated at 2022-06-12 21:00:17.288697
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    try:
        from unittest import mock
    except ImportError:
        import mock

    search_paths = ['one', 'two', 'three', 'missing', 'four']
    final_paths = [p for p in list_valid_collection_paths(search_paths)]
    expected_paths = ['one', 'two', 'three', 'four']

    assert final_paths == expected_paths, "search_paths are not as expected"


# Generated at 2022-06-12 21:00:29.407999
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.path import unfrackpath
    import tempfile
    import shutil
    import sys
    import os

    tmpdir = tempfile.mkdtemp()
    tf_plugindir = tempfile.mkdtemp()
    tf_datadir = tempfile.mkdtemp()

    tf_playbook = tempfile.NamedTemporaryFile(mode='w+b')
    tf_playbook_path = tf_playbook.name

    collections_root = os.path.join(tmpdir, 'ansible_collections')

    ns = 'foo'
    coll1 = 'bar'
    coll2 = 'baz'
    coll3 = 'barbaz'
    coll1_dir = os.path.join(collections_root, ns, coll1)

# Generated at 2022-06-12 21:00:53.071156
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths function
    :return:
    """

    search_paths = [
        'test_collections/dummy_collections',
        'test_include_vars/subdir',
        'invalid_dir_name',
    ]
    actual_result = list_valid_collection_paths(search_paths)
    expected_result = [
        'test_collections/dummy_collections',
        'test_include_vars/subdir',
    ]

    assert list(actual_result) == expected_result


# Generated at 2022-06-12 21:01:04.806280
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import pytest
    import tempfile

    # Create a temporary directory for this test
    temp_dir = tempfile.mkdtemp()

    # Temporary directory should exist
    assert os.path.isdir(temp_dir)

    # Create a temporary file
    temp_file = os.path.join(temp_dir, "foo.txt")
    open(temp_file, 'w').close()

    # Temporary directory should contain one file
    assert os.listdir(temp_dir) == ["foo.txt"]

    # Temporary directory should be a valid collection path
    assert temp_dir in list_valid_collection_paths([temp_dir])

    # Temporary file should not be a valid collection path
    assert temp_file not in list_valid_collection_paths([temp_file])

    # Temporary file should be a valid collection path if it exists

# Generated at 2022-06-12 21:01:12.949314
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    def test_path_list(path_list, exp_path_list):

        ret_list = list(list_valid_collection_paths(path_list))
        assert ret_list == exp_path_list

    test_path_list(
        [
            '/bogus/path1',
            '/also/bogus',
            '/this/one/exists',
        ],
        [
            '/this/one/exists',
        ],
    )

    test_path_list(
        [
            '/bogus/path1',
            '/also/bogus',
            '/etc/ansible/test_collection',
        ],
        [
            '/etc/ansible/test_collection',
        ],
    )


# Generated at 2022-06-12 21:01:18.832130
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    try:
        import collections.abc
    except ImportError:
        import collections

    # Verify that the type returned by list_collection_dirs is a list type
    if isinstance(list_collection_dirs(), collections.abc.Iterable):
        print('The type of list_collection_dirs() is a list')
    else:
        print('The type of list_collection_dirs() is not a list')

# Generated at 2022-06-12 21:01:29.188340
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        'collection_playbook_does_not_exist',
        'collection_playbook_is_file',
        './',
        './test/test_data/collection_resources/ansible_collections/test_collection'
    ]

    for given_path in search_paths:

        b_given_path = to_bytes(given_path, errors='surrogate_or_strict')

        if given_path == './':
            result = list_valid_collection_paths([given_path])

            assert len(result) == len(search_paths) - 1

        elif os.path.exists(b_given_path) and not os.path.isdir(b_given_path):
            result = list_valid_collection_paths([given_path])

           

# Generated at 2022-06-12 21:01:38.754416
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    with open('/tmp/not-a-config', 'wb') as f:
        f.write(b'foo')

    found = [x for x in list_valid_collection_paths(search_paths=['/tmp/not-a-config'])]
    assert len(found) == 0

    found = [x for x in list_valid_collection_paths(search_paths=['/tmp/not-a-config'], warn=False)]
    assert len(found) == 0

    found = [x for x in list_valid_collection_paths(search_paths=['/tmp/not-a-config'], warn=True)]
    assert len(found) == 0


# Generated at 2022-06-12 21:01:50.788729
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil

    # Create a directory with invalid collection paths
    temp_dir = tempfile.mkdtemp()

    # Empty directory
    subdir = os.path.join(temp_dir, 'empty_dir')
    os.mkdir(subdir)

    # Non-directory
    non_dir = os.path.join(temp_dir, 'non_dir')
    with open(non_dir, 'w') as non_dir_open:
        non_dir_open.write('')

    # directory with invalid collection
    coll_dir = os.path.join(temp_dir, 'ansible_collections/invalid_namespace/invalid_coll')
    os.makedirs(coll_dir)

    # Create a directory with valid collection path
    valid_coll_dir = os.path

# Generated at 2022-06-12 21:02:01.158430
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = [
        'test/units/collections/list_collection_dirs/path1',
        'test/units/collections/list_collection_dirs/path2',
    ]

    for coll_path in list_collection_dirs(search_paths):
        print(coll_path)

    for coll_path in list_collection_dirs(search_paths, 'ns1'):
        print(coll_path)

    for coll_path in list_collection_dirs(search_paths, 'ns2.coll2'):
        print(coll_path)

    for coll_path in list_collection_dirs(search_paths, 'ns2.coll_bad'):
        print(coll_path)

# Generated at 2022-06-12 21:02:09.776134
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    test list_valid_collection_paths
    """
    import tempfile
    import shutil

    path_dir1 = tempfile.mkdtemp(prefix="ansible_collections_dir")
    path_dir2 = tempfile.mkdtemp(prefix="ansible_collections_dir")
    path_file = tempfile.mkstemp(prefix="ansible_collections_file")[1]
    search_paths = [path_dir1, path_dir2, path_file]

    def cleanup():

        try:
            shutil.rmtree(path_dir1)
        except OSError:
            pass

        try:
            shutil.rmtree(path_dir2)
        except OSError:
            pass


# Generated at 2022-06-12 21:02:19.189937
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    ''' list_valid_collection_paths() function generates a list of valid collection paths,
    This function generates a temp directory, puts a file and two directories in it,
    and then verifies that the function returns only the directories but not the file.
    '''
    # copy and paste syntax from python docs
    # https://docs.python.org/2/library/tempfile.html
    import tempfile
    import os
    import shutil

    path = tempfile.mkdtemp() + '/my_paths'
    os.makedirs(path)

# Generated at 2022-06-12 21:02:57.054230
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    a = list(list_valid_collection_paths())
    assert a
    b = list(list_valid_collection_paths(['/tmp']))
    assert b == ['/tmp']
    b = list(list_valid_collection_paths(['/tmp'], warn=True))
    assert b == []
    b = list(list_valid_collection_paths(['/']))
    assert b == ['/']

# Generated at 2022-06-12 21:03:08.639763
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves import builtins

    cp = []
    cp.append('/tmp/')
    cp.append('/var/tmp/')
    cp.append('/var/tmp')
    cp.append('/dev/null')
    try:
        cp.append('/')
    except:
        pass

    # builtins.open = open

    sfp = list_valid_collection_paths(cp, warn=True)

    used_paths = []
    for p in sfp:
        used_paths.append(p)

    assert '/tmp' in used_paths
    assert '/var/tmp/' in used_paths
    assert '/dev/null' not in used_paths
    assert '/' not in used_paths



# Generated at 2022-06-12 21:03:14.424956
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    d1 = tempfile.mkdtemp()
    d2 = tempfile.mkdtemp()
    test_paths = [d1, './fake/path', d2]
    result = list_valid_collection_paths(test_paths, warn=True)
    assert d1 in result
    assert d2 in result
    assert './fake/path' not in result

# Generated at 2022-06-12 21:03:20.269084
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # As we do not know how the current system is configured
    # we can only test that some subset of search paths are
    # returned as valid.
    #
    # Test search paths provided with non-empty list.
    search_paths = ['.', './', './collections', '/collections', '']
    result = list(list_valid_collection_paths(search_paths))
    assert len(result) > 0, "There should be some valid search paths."



# Generated at 2022-06-12 21:03:24.558706
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import TEST_COLLECTION_PATH_1
    from ansible.utils.collection_loader import TEST_COLLECTION_PATH_2
    expected_result = [TEST_COLLECTION_PATH_1, TEST_COLLECTION_PATH_2]
    result = list(list_valid_collection_paths([TEST_COLLECTION_PATH_1, TEST_COLLECTION_PATH_2]))
    assert result == expected_result
