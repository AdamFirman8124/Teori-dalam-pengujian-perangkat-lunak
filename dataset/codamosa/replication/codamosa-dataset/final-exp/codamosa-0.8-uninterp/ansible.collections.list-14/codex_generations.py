

# Generated at 2022-06-12 20:53:42.290007
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test case: nothing passed, should return default collection path
    test1 = None
    expected_result = AnsibleCollectionConfig.collection_paths[0]
    my_list = list(list_valid_collection_paths(test1))
    assert expected_result == my_list[0]

    # test case: bad path passed
    test2 = ["/my_path/does/not/exist"]
    expected_result = []
    my_list = list(list_valid_collection_paths(test2))
    assert expected_result == my_list

    # test case: empty path passed
    test3 = [""]
    expected_result = []
    my_list = list(list_valid_collection_paths(test3))
    assert expected_result == my_list

    # test case: bad list passed
    test4

# Generated at 2022-06-12 20:53:51.074691
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test 1:
    # This test is for checking that a search_paths, which is a list having paths of files of
    # a collection and path of a file, returns only list having paths only of directories of collection
    search_path = [
        "test/collections/ansible_collections/",
        "library/test_module.py"
    ]
    assert list_valid_collection_paths(search_path) == [
        "test/collections/ansible_collections/"
    ]
    # Test 2:
    # This test is for checking that a search_paths, which is a list having paths of non existent
    # files and directories of a collection, returns only list having paths of only directories of collection

# Generated at 2022-06-12 20:53:58.663299
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import os
    import tempfile

    # Create collection
    tmp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(tmp_dir, u'namespace1', u'collection1', u'plugins', u'modules'))
    os.makedirs(os.path.join(tmp_dir, u'namespace1', u'collection1', u'plugins', u'action_plugins'))
    os.makedirs(os.path.join(tmp_dir, u'namespace1', u'collection1', u'plugins', u'filter_plugins'))
    os.makedirs(os.path.join(tmp_dir, u'namespace1', u'collection2', u'plugins', u'modules'))

# Generated at 2022-06-12 20:54:09.212626
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import mkdtemp
    import shutil
    import os


# Generated at 2022-06-12 20:54:20.730518
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common._collections_compat import TemporaryDirectory
    from ansible.module_utils._text import to_native
    from ansible.module_utils.parsing.convert_bool import boolean

    # a temp directory to list in
    with TemporaryDirectory(prefix='ansible_test_valid_paths_') as tempdir:
        # a directory to be ignored
        os.mkdir('{0}/ignore'.format(tempdir))
        # a dir to list
        os.mkdir('{0}/list'.format(tempdir))

        # a dir to find
        found_paths = list_valid_collection_paths(search_paths=['{0}/list'.format(tempdir)])

# Generated at 2022-06-12 20:54:30.580427
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Valid paths:
    my_paths = ['/tmp', '/tmp/', '/tmp/ansible_collections']
    assert set(list_valid_collection_paths(search_paths=my_paths, warn=False)) == set(my_paths)

    # Invalid paths:
    invalid_paths = ['/tmp/not-a-path', 'invalid-path']
    assert set(list_valid_collection_paths(search_paths=invalid_paths, warn=False)) == set([])

    # No paths:
    assert set(list_valid_collection_paths(search_paths=None, warn=False)) == set(AnsibleCollectionConfig.collection_paths)

# Generated at 2022-06-12 20:54:37.148679
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.config.manager import ConfigManager
    import tempfile

    coll_path1 = tempfile.mkdtemp()
    coll_path2 = tempfile.mkdtemp()
    coll_path3 = tempfile.mkdtemp()
    coll_path4 = tempfile.mkdtemp()
    coll_path5 = tempfile.mkdtemp(prefix='/tmp/fake_missing_dir')

    collection_dir = os.path.join(coll_path1, 'ansible_collections')
    os.mkdir(collection_dir)

    collection_dir = os.path.join(coll_path2, 'ansible_collections')
    os.mkdir(collection_dir)

    collection_dir = os.path.join(coll_path3, 'some_other_name')

# Generated at 2022-06-12 20:54:43.551918
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['/tmp'])) == ['/tmp']
    assert list(list_valid_collection_paths(['/tmp', '/usr/share/ansible/collections'])) == \
        ['/tmp', '/usr/share/ansible/collections']
    assert list(list_valid_collection_paths(['/tmp', '/usr/share/ansible/collections'])) == \
        ['/tmp', '/usr/share/ansible/collections']
    assert list(list_valid_collection_paths(['/tmp', '/usr/share/ansible/collections',
                                             '/usr/share/ansible_collections'])) == \
        ['/tmp', '/usr/share/ansible/collections', '/usr/share/ansible_collections']

# Generated at 2022-06-12 20:54:50.712066
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test default config
    paths = list_valid_collection_paths()
    default_paths = AnsibleCollectionConfig.collection_paths
    assert len(default_paths) == len(paths)
    for path in paths:
        assert path in default_paths

    # add a bad path and test again
    paths.append('/nonexistent')
    paths = list_valid_collection_paths(paths, warn=True)
    assert len(paths) < len(default_paths)
    for path in paths:
        assert path in default_paths


# Generated at 2022-06-12 20:55:01.661139
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # make sure we can set it and it is returned
    assert list(list_valid_collection_paths(search_paths=["/my/path"])) == ["/my/path"]

    # test default paths
    defaults = ["/etc/ansible/collections", "~/.ansible/collections"]
    assert sorted(list(list_valid_collection_paths())) == sorted(defaults)

    # test duplicates
    stored_config = AnsibleCollectionConfig._search_paths
    try:
        AnsibleCollectionConfig._search_paths = ["/my/path", "/my/path", "/my/path"]
        assert [p for p in list_valid_collection_paths()] == ["/my/path"]
    finally:
        AnsibleCollectionConfig._search_paths = stored_config

# Generated at 2022-06-12 20:55:16.727220
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    fake_path = '/home/user/foo'
    fake_paths = ['/home/user/foo', '/home/user/bar']
    assert list(list_valid_collection_paths()) == list(list_valid_collection_paths())
    assert list(list_valid_collection_paths(search_paths=fake_path)) == list(list_valid_collection_paths(search_paths=fake_path))
    assert list(list_valid_collection_paths(search_paths=fake_paths)) == list(list_valid_collection_paths(search_paths=fake_paths))
    assert list(list_valid_collection_paths()) != list(list_valid_collection_paths(search_paths=fake_path))
    assert list(list_valid_collection_paths())

# Generated at 2022-06-12 20:55:27.766745
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os
    import sys


# Generated at 2022-06-12 20:55:37.915560
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import os
    from shutil import rmtree


# Generated at 2022-06-12 20:55:40.056753
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import pytest
    with pytest.raises(AnsibleError):
        list_collection_dirs(coll_filter='invalid_collection.name')

# Generated at 2022-06-12 20:55:49.066388
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.all.plugins.module_utils.common.parameters import ParameterFinder
    from ansible.module_utils._text import to_text, to_bytes
    # Make sure the collection is in the search path
    p = ParameterFinder.load_config_files()
    p.search_paths.append(to_bytes("/tmp/ansible_collections", errors='surrogate_or_strict'))
    # Create dirs
    os.makedirs("/tmp/ansible_collections/my_namespace/my_collection")
    # Create init
    open("/tmp/ansible_collections/my_namespace/my_collection/__init__.py", 'a').close()
    # Validate collection dir

# Generated at 2022-06-12 20:55:55.088223
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = ['/path/does/not/exist', '/path/isnt/a/dir', '/tmp', '/usr']
    display.verbosity = 3

    config_paths = AnsibleCollectionConfig.collection_paths

    # /path/does/not/exist, /path/isnt/a/dir should not be returned
    # /tmp and /usr should be returned
    filtered = list(list_valid_collection_paths(paths))
    assert isinstance(filtered, list)
    assert len(filtered) == 2
    assert '/tmp' in filtered
    assert '/usr' in filtered

    # the default paths should be returned
    filtered = list(list_valid_collection_paths())
    assert isinstance(filtered, list)
    assert len(filtered) == len(config_paths)

# Generated at 2022-06-12 20:56:05.180331
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible_collections.testns.mycoll.tests.unit.compat.mock import patch
    import os

    def mock_list_valid_collection_paths(search_paths=None, warn=False):
        print("Mock list_valid_collection_paths")
        return [os.path.join(os.getcwd(), 'testi_data')]

    with patch('ansible.module_utils.ansible_collections.ansible.dist.collection_loader.list_valid_collection_paths', side_effect=mock_list_valid_collection_paths):
        for coll_dir in list_collection_dirs(search_paths=None, coll_filter=None):
            print(coll_dir)

# Generated at 2022-06-12 20:56:16.701781
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    cur_dir = os.getcwd()
    coll_dir = os.path.join(cur_dir, 'ansible_collections/testcoll/test_collection/')
    fake_coll_dir = os.path.join(cur_dir, 'ansible_collections/testcoll/fake_collection/')
    dup_coll_dir = os.path.join(cur_dir, 'ansible_collections/testcoll/dup_collection/')
    invalid_coll_dir = os.path.join(cur_dir, 'ansible_collections/testcoll/invalid_collection/')

    search_paths = [coll_dir, fake_coll_dir, dup_coll_dir]
    coll_filter = 'testcoll.test_collection'


# Generated at 2022-06-12 20:56:28.268325
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for function list_collection_dirs
    """

    # Create a dummy collection for the test
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    tmpcoll = os.path.join(tmpdir, 'ansible_collections')
    tmpnamespace = os.path.join(tmpcoll, 'ns')
    tmpcollec = os.path.join(tmpnamespace, 'coll')
    os.makedirs(tmpnamespace)
    os.makedirs(tmpcollec)

    # Testing all the collections in default path
    b_collections = list(list_collection_dirs())
    assert len(b_collections) > 0
    # Testing a specific collection in the default path

# Generated at 2022-06-12 20:56:40.296383
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from ansible.config.manager import ConfigManager
    from ansible.config.collection_config import AnsibleCollectionConfig
    from ansible.collections import deps

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 20:56:50.061848
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    expected_paths = [os.path.join(os.getcwd(), "ansible_collections")]
    assert list(list_valid_collection_paths()) == expected_paths
    assert list(list_valid_collection_paths(['/ansible_collections'])) == ['/ansible_collections']

# Generated at 2022-06-12 20:56:54.339531
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(search_paths=[])  # empty input returns default
    assert list_valid_collection_paths(search_paths=["/nonexistent"])  # non-existent ignored
    assert list_valid_collection_paths(search_paths=["/etc/passwd"])  # file ignored



# Generated at 2022-06-12 20:57:05.902960
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

# Generated at 2022-06-12 20:57:10.131967
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['./ansible/test/units/module_utils/basic/',
                    './ansible/test/units/module_utils/basic/ansible_collections/foo/bar/']

    ret = list(list_valid_collection_paths(search_paths=search_paths))
    assert len(ret) == 2

# Generated at 2022-06-12 20:57:21.771740
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Function to test list_collection_dirs
    """

    assert list(list_collection_dirs(['./test/unit/ansible_collections'])) == ['./test/unit/ansible_collections/namespace/collection', './test/unit/ansible_collections/namespace2/collection2']
    assert list(list_collection_dirs(['./test/unit/ansible_collections'], 'namespace.collection')) == ['./test/unit/ansible_collections/namespace/collection']
    assert list(list_collection_dirs(['./test/unit/ansible_collections'], 'namespace2')) == ['./test/unit/ansible_collections/namespace2/collection2']

# Generated at 2022-06-12 20:57:30.933640
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test invalid collection_path
    assert to_bytes('/path/to/invalid') in list_collection_dirs(['/path/to/invalid'])

    # Test valid collection_path
    assert to_bytes('plugins/modules') in list_collection_dirs([os.path.dirname(__file__)])

    # Test collection filter
    assert to_bytes('plugins/modules') in list_collection_dirs([os.path.dirname(__file__)], 'ansible.builtin')
    assert to_bytes('plugins/modules') not in list_collection_dirs([os.path.dirname(__file__)], 'ansible.invalid')

# Generated at 2022-06-12 20:57:38.937023
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    tpath = tempfile.mkdtemp()
    tpath1 = tempfile.mkdtemp()
    tpath2 = tempfile.mkdtemp()
    collection_test = "test1"
    collection_test1 = "test2"
    collection_test2 = "test3"
    tcollection1 = os.path.join(tpath, 'ansible_collections', collection_test, collection_test1)
    tcollection2 = os.path.join(tpath1, 'ansible_collections', collection_test, collection_test1)
    tcollection3 = os.path.join(tpath2, 'ansible_collections', collection_test, collection_test1)

# Generated at 2022-06-12 20:57:49.298915
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Unit test for function list_collection_dirs"""

    import tempfile
    import shutil
    from textwrap import dedent

    from ansible.utils.collection_loader import AnsibleCollectionLoader, import_collection_file

    test_namespace = 'test_namespace'
    test_coll1 = 'test_coll1'
    test_coll2 = 'test_coll2'
    test_collection_name1 = '%s.%s' % (test_namespace, test_coll1)
    test_collection_name2 = '%s.%s' % (test_namespace, test_coll2)
    test_collection_name3 = 'test_coll3'
    test_collection_name = 'fake_collection'
    test_plugin_type = 'fake_plugin_type'

# Generated at 2022-06-12 20:57:56.696293
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = ['/bar/foo', '/tmp/baz']
    results = list_valid_collection_paths(paths)
    assert next(results) == '/bar/foo'
    assert next(results) == '/tmp/baz'
    assert next(results, None) is None

    paths = ['/not/real', '/this/one/is/not/a/dir']
    results = list_valid_collection_paths(paths, warn=True)
    assert next(results, None) is None



# Generated at 2022-06-12 20:58:03.552114
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import shutil
    import tempfile
    import unittest

    import ansible

    ANSIBLE_BASE = os.path.dirname(ansible.__file__)

    class TestListCollectionDirs(unittest.TestCase):
        def _create_collection_dir(self, namespace, collection):
            collection_dir = os.path.join(self.coll_root, namespace, collection)
            os.makedirs(collection_dir)
            os.makedirs(os.path.join(collection_dir, 'plugins'))
            return collection_dir

        def setUp(self):
            self.coll_root = tempfile.mkdtemp()
            self._create_collection_dir('ansible_namespace', 'ansible_collection')


# Generated at 2022-06-12 20:58:17.588998
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp/path1', 'doesnt_exist', '/tmp/path2', '/tmp/path3']
    valid_paths = [path for path in list_valid_collection_paths(search_paths, warn=False)]
    
    assert sorted(search_paths) == sorted(valid_paths)

# unit test for function list_collection_dirs

# Generated at 2022-06-12 20:58:29.218895
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import list_valid_collection_paths
    from ansible.utils.display import Display
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    search_paths = list()
    search_paths.append(os.path.expanduser('~/.ansible/collections'))
    display = Display()

    # test warning
    valid_paths = list_valid_collection_paths(search_paths=search_paths, warn=True)
    assert len(valid_paths) == len(AnsibleCollectionConfig.collection_paths)

    # test without warn
    valid_paths = list_valid_collection_paths(search_paths=search_paths, warn=False)

# Generated at 2022-06-12 20:58:34.288206
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collections = list(list_collection_dirs(coll_filter='ansible_collections.amazon.aws.plugins.module_utils.ec2_vpc_net'))
    assert len(collections) == 1
    assert collections[0].endswith('ansible_collections/amazon/aws')

# Generated at 2022-06-12 20:58:38.269941
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    for collection_dir in list_collection_dirs(["/usr/share"], 'ansible_namespace.collection'):
        assert to_bytes(collection_dir) == (b"/usr/share/ansible_collections/ansible_namespace/collection")



# Generated at 2022-06-12 20:58:43.465811
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list_valid_collection_paths(search_paths=['/tmp/no_such_path']) == ()
    assert '/tmp' in list_valid_collection_paths(search_paths=['/tmp'])
    assert '/tmp' in list_valid_collection_paths(search_paths=['/tmp', '/tmp/no_such_path'])
    assert '/usr/local/share/ansible/collections' in list_valid_collection_paths(search_paths=[])



# Generated at 2022-06-12 20:58:54.255204
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # read the config from the defaults
    config = AnsibleCollectionConfig.config
    search_paths = config.get('collections', 'paths')

    # what happens when the collection path is empty
    actual = list(list_valid_collection_paths(search_paths=[]))
    assert actual == []

    # read the config from the defaults
    config = AnsibleCollectionConfig.config
    search_paths = config.get('collections', 'paths')

    # what happens when the collection path is empty
    actual = list(list_valid_collection_paths(search_paths=[]))
    assert actual == []

    # what happens when the search path exists and is a directory
    test_path = os.path.join(os.path.dirname(__file__), 'test/test_collections')
    actual

# Generated at 2022-06-12 20:59:00.676745
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    from ansible.plugins.loader import plugin_loader

    coll_test_path = os.path.join(tempfile.gettempdir(), 'test_collections')

    # create test dir
    os.mkdir(coll_test_path)

    # create collection layout in test dir
    os.mkdir(os.path.join(coll_test_path, 'ansible_collections'))
    os.mkdir(os.path.join(coll_test_path, 'ansible_collections', 'namespace'))
    os.mkdir(os.path.join(coll_test_path, 'ansible_collections', 'namespace', 'collection'))


# Generated at 2022-06-12 20:59:08.684411
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Validate that the search_paths are returned in a valid state
    :return:
    """

    from ansible.module_utils.collection_loader import get_collection_loader
    from ansible.collections import is_collection_path

    cl = get_collection_loader()
    for coll_root in cl._collection_paths:
        assert os.path.exists(coll_root)
        assert os.path.isdir(coll_root)
        assert is_collection_path(coll_root)

# Generated at 2022-06-12 20:59:16.902332
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import os

    temp_path = tempfile.mkdtemp()

    assert list_valid_collection_paths([]) == list(AnsibleCollectionConfig.collection_paths)
    assert list_valid_collection_paths(['/dev/null']) == []

    os.mkdir(os.path.join(temp_path, 'foo'))

    assert list_valid_collection_paths([temp_path]) == [temp_path, ]
    assert list_valid_collection_paths([temp_path, '/dev/null']) == [temp_path, ]
    assert list_valid_collection_paths(['/dev/null', temp_path]) == [temp_path, ]

# Generated at 2022-06-12 20:59:27.708617
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile
    import shutil

    from ansible.executor.task_queue_manager import TaskQueueManager

    # We want to test this in isolation from existing config
    from ansible.collections.collection_loader import _collection_loaders
    saved_collection_loaders = dict(_collection_loaders)
    del _collection_loaders

    def cleanup_collection_loaders():
        _collection_loaders.clear()
        _collection_loaders.update(saved_collection_loaders)

    test_path = to_bytes(tempfile.mkdtemp())
    coll_path = os.path.join(test_path, b'ansible_collections')
    os.mkdir(coll_path)
    os.mkdir(os.path.join(coll_path, b'local_namespace'))
   

# Generated at 2022-06-12 20:59:53.713480
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.collections.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_loader import list_collection_dirs

    search_paths = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'collection_loader'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'ansible_collections_real'),
    ]


# Generated at 2022-06-12 21:00:02.705441
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    searchpath = ['collection1', 'collection2']
    coll = os.getenv('ANSIBLE_COLLECTIONS_PATHS')
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ':'.join(searchpath)
    try:
        cpath = list(list_collection_dirs())
        assert os.path.basename(cpath[0]) == 'ns1'
        assert os.path.basename(cpath[1]) == 'coll1'
    finally:
        if coll is None:
            del os.environ['ANSIBLE_COLLECTIONS_PATHS']
        else:
            os.environ['ANSIBLE_COLLECTIONS_PATHS'] = coll



# Generated at 2022-06-12 21:00:13.830962
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Make sure non-existent search_paths are skipped
    with open(os.devnull, "w") as f:
        # AnsibleDisplay will be initialized from environment variables
        display.verbosity = 1
        display.display = f

        search_path = ["/no/such/path", "/another/no/such/path"]
        valid_paths = [path for path in list_valid_collection_paths(search_path, warn=True)]
        assert [] == valid_paths

        search_path = ["/foo/bar", "/fizz/buzz"]
        valid_paths = [path for path in list_valid_collection_paths(search_path, warn=True)]
        assert [] == valid_paths

        search_path = ["/etc/ansible", "/etc/ansible/ansible_collections"]

# Generated at 2022-06-12 21:00:19.190808
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import functools
    import zipfile

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a collection
    collection = "mycol"
    namespaces = ["ns1", "ns2"]
    namespace_dirs = []
    for ns in namespaces:
        namespace_dirs.append(tempfile.mkdtemp(dir=tmpdir))
        collection_dir = os.path.join(namespace_dirs[-1], collection)
        os.mkdir(collection_dir)
        open(os.path.join(collection_dir, "README.md"), "w+")

    search_path = os.path.join(tmpdir, "my_custom_path")
    os.mkdir(search_path)
    test_files

# Generated at 2022-06-12 21:00:24.623326
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['/foo/bar', '/invalid/path', '/valid/path']
    expected_paths = search_paths[2].split(os.sep)
    assert list(list_valid_collection_paths(search_paths))
    assert expected_paths in list(list_valid_collection_paths(search_paths))


# Generated at 2022-06-12 21:00:33.970024
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.utils.path import unfrackpath
    from ansible.utils.path import makedirs_safe

    b_cwd = to_bytes(os.getcwd())

    # Test empty config
    search_paths = []
    assert list(list_valid_collection_paths(search_paths)) == []

    # Test invalid path
    search_paths = [unfrackpath('/this/path/does/not/exist')]
    assert list(list_valid_collection_paths(search_paths)) == []

    # Test valid directory path
    search_paths = [unfrackpath(os.path.join(b_cwd))]
    assert list(list_valid_collection_paths(search_paths)) == [unfrackpath(b_cwd)]

    # Test valid

# Generated at 2022-06-12 21:00:44.031994
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test the list_collection_dirs function.

    This function is used to find collections on local disk.
    We want to test the following scenarios:
    1. Passing a namespace that doesn't exist.
    2. Passing a namespace that exists.
    3. Passing a collection that doesn't exist in a namespace.
    4. Passing a collection that exists.
    5. Passing an invalid collection name.
    6. Passing a collection that exists in the same namespace twice with different paths.
    """
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.match import match
    from ansible.collections.ansible.community.plugins import module_utils

    # The subdirectory we will be using for our test collections
    TEST_DIR = 'ansible_collections'

    #

# Generated at 2022-06-12 21:00:52.946019
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [
        'c1_path1',
        'c1_path2',
        'c2_path1',
        'c2_path2'
    ]
    coll_filter = "namespace1.collection1"
    namespaces_collections = {
        "namespace1": ["collection1"],
        "namespace2": ["collection2"],
        "namespace3": ["collection1", "collection2"],
    }

    collection_dirs = []
    # When filter is set.
    collection_dirs.append(list(list_collection_dirs(paths, coll_filter)))
    assert len(collection_dirs[-1]) == 4, "Expected number of collection dirs is 4"

    # When filter is not set.

# Generated at 2022-06-12 21:00:58.369780
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test for list_valid_collection_paths.
    """
    search_paths = ['/none/exist', '/etc/ansible/collections']
    coll_dirs = list_valid_collection_paths(search_paths)
    coll_dir = list(coll_dirs)[0]

    assert '/etc/ansible/collections' == coll_dir


# Generated at 2022-06-12 21:01:09.554763
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import shutil
    import tempfile

    coll_from = 'ansible_collections.test.test_collection'
    search_path = [os.path.join(os.path.dirname(__file__), coll_from.replace('.', os.path.sep))]
    failed = False


# Generated at 2022-06-12 21:01:47.408536
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths()) == AnsibleCollectionConfig.collection_paths
    assert list(list_valid_collection_paths(['/tmp/foo/bar', '/tmp/foo/baz'])) == ['/tmp/foo/bar', '/tmp/foo/baz']

# Generated at 2022-06-12 21:01:58.629134
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    import tempfile
    import os

    if PY3:
        search_paths = ['invalid_path']
        result = list(list_valid_collection_paths(search_paths, warn=False))
        assert len(result) == 0
    else:
        search_paths = ['invalid_path1', 'invalid_path2']
        result = list(list_valid_collection_paths(search_paths, warn=False))
        assert len(result) == 0

    if PY3:
        search_paths = ['invalid_path']
        result = list(list_valid_collection_paths(search_paths, warn=True))

# Generated at 2022-06-12 21:02:02.070615
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp

    test_path = [mkdtemp(prefix='ansible_collections')]
    list(list_valid_collection_paths(search_paths=test_path))



# Generated at 2022-06-12 21:02:13.302810
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.constants import DEFAULT_COLLECTIONS_PATHS
    from ansible.module_utils._text import to_text
    import tempfile
    import shutil

    (fd, dirpath) = tempfile.mkstemp(dir=os.getcwd())

# Generated at 2022-06-12 21:02:20.829484
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.cli import CLI
    from ansible.config.manager import ConfigManager

    instances = []
    for arg in ["-c", "", "-T", "60", "all"]:
        print(arg)
        a = CLI.parse([arg], None)[0]
        print(a.__dict__)
        b = a.__class__(**a.__dict__)
        instances.append(b)

    cli = CLI(args=instances)

    config_mgr = ConfigManager()
    cli.add_playbook_parser()
    cli.add_parser()
    cli.add_base_parser()
    cli.base_parser = cli.base_parsers[0]

# Generated at 2022-06-12 21:02:25.460531
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/etc/ansible/roles', '/etc/ansible/', '/etc/ansible/roles/']
    paths = list_valid_collection_paths(search_paths)

    assert paths.next() == '/etc/ansible/roles'
    assert paths.next() == '/etc/ansible'

# Generated at 2022-06-12 21:02:33.010775
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test invalid namespace
    invalid_ns = 'invalid_namespace'
    results = list(list_collection_dirs(coll_filter=invalid_ns))
    assert len(results) == 0

    # Test invalid collection
    invalid_coll = 'invalid_namespace.invalid_collection'
    results = list(list_collection_dirs(coll_filter=invalid_coll))
    assert len(results) == 0

    # Test valid collection
    valid_coll = 'valid_namespace.valid_collection'
    results = list(list_collection_dirs(coll_filter=valid_coll))
    assert len(results) == 1

    # Test valid namespace
    valid_ns = 'valid_namespace'
    results = list(list_collection_dirs(coll_filter=valid_ns))
    assert len

# Generated at 2022-06-12 21:02:42.617648
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Create a fake collections dir and populate with known paths
    import shutil
    import tempfile
    import unittest

    test_dir = tempfile.mkdtemp()
    ansible_collections_dir = os.path.join(test_dir, "ansible_collections")
    os.mkdir(ansible_collections_dir)

    namespace_dir = os.path.join(ansible_collections_dir, 'namespace')
    os.mkdir(namespace_dir)

    os.mkdir(os.path.join(namespace_dir, 'collection'))
    os.mkdir(os.path.join(namespace_dir, 'collection2'))

    bad_namespace_dir = os.path.join(ansible_collections_dir, 'bad_namespace')
    # add a file

# Generated at 2022-06-12 21:02:53.648640
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    fixtures = os.path.join(this_dir, 'fixtures', 'list_collection_dirs')
    test_coll_root = os.path.join(fixtures, 'test_coll_root')
    coll_config = AnsibleCollectionConfig.load_from_file(os.path.join(fixtures, 'ansible.cfg'))
    coll_config.set_collection_paths([test_coll_root])
    absolute_coll_paths = list(list_collection_dirs(search_paths=[test_coll_root]))
    assert len(absolute_coll_paths) == 3, '3 collection paths found'

# Generated at 2022-06-12 21:03:04.767405
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common.collections import list_valid_collection_paths
    from ansible.module_utils._text import to_native

    # remove any existing search paths before testing
    AnsibleCollectionConfig.collection_paths = []
    valid_paths = []
    invalid_paths = []
