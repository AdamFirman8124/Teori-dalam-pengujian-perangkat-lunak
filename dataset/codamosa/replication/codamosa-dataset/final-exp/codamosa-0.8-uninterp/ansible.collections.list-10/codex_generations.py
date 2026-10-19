

# Generated at 2022-06-12 20:53:44.358085
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()

    tmppaths = [
        tempfile.mkdtemp(dir=tmpdir),
        tempfile.mkdtemp(dir=tmpdir),
        tempfile.mkstemp(dir=tmpdir)[1],
    ]
    tmppath_str = list(map(to_bytes, tmppaths))

    paths = tmppath_str + [
        '',
        'nonexistent',
        'nonexistent/path',
        '/this/path/does/not/exist',
        'nonexistent/path/foo.tar.gz'
    ]

    expected = tmppath_str

    assert list(list_valid_collection_paths(paths)) == expected


# Generated at 2022-06-12 20:53:54.173804
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from collections import namedtuple
    from ansible.module_utils.six import iteritems

    TestCase = namedtuple('TestCase', 'search_paths coll_filter expected retval')


# Generated at 2022-06-12 20:54:06.148011
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''
    Test list_valid_collection_paths()
    '''
    from tempfile import mkdtemp
    from shutil import rmtree

    # Non-existent directory not in result
    tmp_dir = '/tmp/' + mkdtemp(prefix='ansible_')
    rmtree(tmp_dir)
    assert tmp_dir not in list(list_valid_collection_paths([tmp_dir]))

    # Non-directory not in result
    tmp_file = '/tmp/' + mkdtemp(prefix='ansible_')
    with open(tmp_file, 'a'):
        os.utime(tmp_file, None)
    assert tmp_file not in list(list_valid_collection_paths([tmp_file]))

    # Existing directory in result

# Generated at 2022-06-12 20:54:08.691749
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    for d in list_valid_collection_paths(search_paths=['/tmp', "/this/is/not/a/real/path/foo"]):
        assert '/tmp' == d



# Generated at 2022-06-12 20:54:13.414885
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert 'ansible_collections.ansible.builtin' in list_collection_dirs()

# Generated at 2022-06-12 20:54:17.437070
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # the list returned by this function should be equal to the list returned by ansible_collections.__path__
    # if the test fails, the collection-related code is likely broken
    import ansible_collections
    assert list(list_collection_dirs()) == ansible_collections.__path__

# Generated at 2022-06-12 20:54:25.739085
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    def _test_paths(coll_filter, expected):
        paths = list(list_collection_dirs(search_paths=[], coll_filter=coll_filter))
        assert paths == expected

    _test_paths('foo', [])
    _test_paths('foo.bar', [])
    _test_paths('foo.barbaz', [])
    _test_paths('foo.bar.baz', [])

# Generated at 2022-06-12 20:54:35.099321
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.hashing import md5s
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import ModuleLoader
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.basic import AnsibleModule
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group


# Generated at 2022-06-12 20:54:40.147344
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = [b'/etc', b'/usr/share/ansible', b'/tmp/foo']
    for test_path in list_valid_collection_paths(paths, warn=False):
        assert test_path in [b'/usr/share/ansible', b'/etc'], "Path should be a valid one from paths"



# Generated at 2022-06-12 20:54:50.358740
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    curdir = os.path.dirname(os.path.abspath(__file__))
    testdir = os.path.join(curdir, 'fixtures', 'test_collections')
    colls = list(list_collection_dirs(search_paths=[testdir]))
    assert len(colls) == 4
    assert os.path.join(testdir, 'ansible_collections', 'namespace', 'collection') in colls
    assert os.path.join(testdir, 'ansible_collections', 'namespace', 'collection2') in colls
    assert os.path.join(testdir, 'ansible_collections', 'namespace2', 'collection') in colls

# Generated at 2022-06-12 20:55:02.349804
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import tempfile
    import shutil
    import unittest

    class TestListCollectionDirs(unittest.TestCase):
        def test_simple(self):
            testpath = tempfile.mkdtemp()
            os.makedirs(os.path.join(testpath, 'ansible_collections', 'ns1', 'collection1'))
            os.makedirs(os.path.join(testpath, 'ansible_collections', 'ns2', 'collection2'))
            os.makedirs(os.path.join(testpath, 'ansible_collections', 'ns2', 'collection3'))

            collpath = list(list_collection_dirs([testpath], None))
            self.assertEqual(3, len(collpath))

# Generated at 2022-06-12 20:55:12.814812
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # path does not exist
    p1 = "/not/a/real/path/"
    assert list(list_valid_collection_paths([p1])) == []

    # path is not a dir
    p2 = "/etc/passwd"
    assert list(list_valid_collection_paths([p2])) == []

    # path is not a collection
    p3 = os.getcwd()
    assert list(list_valid_collection_paths([p2])) == []

    # path is a collection
    test_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
    p4 = os.path.join(test_path, 'ansible_collections', 'foo', 'bar')

# Generated at 2022-06-12 20:55:23.885804
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test the list_collection_dirs function and the output

    :return:
    """
    # Setup collection_paths and filter
    search_paths = ['test/unit/utils/list_collection_test/test_collection1',
                    'test/unit/utils/list_collection_test/test_collection2']
    coll_filter = ['collection1.collection2']

    # Test the function
    result = list_collection_dirs(search_paths, coll_filter)

    # Check the result
    result_list = list(result)
    assert len(result_list) == 1
    assert to_bytes(result_list[0]) == to_bytes('test/unit/utils/list_collection_test/test_collection1/collection1/collection2')

# Generated at 2022-06-12 20:55:35.517083
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.path import unfrackpath

    search_path_list = [os.path.join(unfrackpath(__file__), 'data', 'test_collections')]

# Generated at 2022-06-12 20:55:39.774608
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/fake/path', '/fake/path2', '/etc']) == ['/etc']
    assert list_valid_collection_paths(['/fake/path', '/fake/path2']) == []



# Generated at 2022-06-12 20:55:48.885753
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os

    real_paths = ('/opt/ansible/collections', '/etc/ansible/collections')

    test_paths = []
    test_dirs = []


# Generated at 2022-06-12 20:55:53.887462
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(['/a/b/c/d']) == []

    from tempfile import mkdtemp
    from shutil import rmtree
    tmpdir = to_bytes(mkdtemp())
    try:
        assert list_valid_collection_paths([tmpdir]) == [tmpdir]
        with open(os.path.join(tmpdir, 'file'), 'w') as f:
            f.write('')
        assert list_valid_collection_paths([tmpdir]) == []
    finally:
        rmtree(tmpdir)

# Generated at 2022-06-12 20:56:04.699171
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test for collections path validation
    :return:
    """
    from ansible.collections.ansible.test.test_utils.test_collection_loader import (
        REMOVED_PATH,
        COLLECTIONS_PATHS,
    )
    from ansible.collections.ansible.test.test_utils.test_collections import (
        DummyCollection,
    )

    valid_paths = []
    for p in list_valid_collection_paths(COLLECTIONS_PATHS, warn=False):
        valid_paths.append(p)
    assert valid_paths == [COLLECTIONS_PATHS[0], REMOVED_PATH, COLLECTIONS_PATHS[2]]


# Generated at 2022-06-12 20:56:11.039679
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import shutil
    import tempfile

    tmpdir = tempfile.mkdtemp(prefix='ansible_collections_test')
    tmpcolldir = os.path.join(tmpdir, 'ansible_collections')
    os.makedirs(tmpcolldir)

    tmpcolldir1 = os.path.join(tmpdir, 'ansible_collections1')
    os.makedirs(tmpcolldir1)

    tmpnotcolldir = os.path.join(tmpdir, 'ansible_notcollections')
    os.makedirs(tmpnotcolldir)

    tmpnotcollpath = os.path.join(tmpdir, 'notapath')
    with open(tmpnotcollpath, 'w') as f:
        f.write("Not a path")


# Generated at 2022-06-12 20:56:22.888992
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Note: This test is intended to be run either by unit/integration tests, or
    # directly by a developer. If you want to run it manually, you will need to
    # create the following paths in new temporary directories, and make sure that
    # the files do not exist:
    #     not_a_directory
    #     not_a_file
    #     directory
    #     directory/subdir_1
    #     directory/subdir_2


    # Test path cases
    valid_paths = [
        os.path.realpath('.'),
    ]

    invalid_paths = [
        os.path.realpath('not_a_directory'),
        os.path.realpath('not_a_file'),
    ]

    # Case 1: Test valid paths with no extra args

# Generated at 2022-06-12 20:56:54.632904
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test standard list of directories
    dirs = (
        '/foo/bar',
        '/bar/baz',
    )
    # Test for the filter of dirs
    filtered_dirs = list(list_valid_collection_paths(dirs))
    assert len(filtered_dirs) == len(dirs)

    # Test filter of dirs with a non-existing directory
    dirs = (
        '/foo/bar',
        '/nonexist/dir',
    )
    filtered_dirs = list(list_valid_collection_paths(dirs, True))
    assert len(filtered_dirs) == 1

    # Test filter of dirs with a directory that exists but is not a dir
    dirs = (
        '/foo/bar',
        '/tmp/file',
    )
    tmp_

# Generated at 2022-06-12 20:57:06.032213
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    :return: None
    """

    import random

    # Use a random collection path to test searching for a collection
    # the directory may not exist.  If it does, the test will pass.
    random_path = "/tmp/random_path_%s" % random.randint(10000, 99999)
    assert random_path not in list(list_collection_dirs())

    # Test listing collection directories with a non existent collection filter
    assert list(list_collection_dirs(coll_filter="michael.dehaan")) == []

    # Test listing collection directories with a valid collection filter
    assert list(list_collection_dirs(coll_filter="ansible_collections.geerlingguy.mariadb")) != []

    # Test warning about non existent collection path

# Generated at 2022-06-12 20:57:09.722052
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from inspect import isgenerator
    from ansible.module_utils.six import string_types

    assert isgenerator(list_collection_dirs())
    for x in list_collection_dirs():
        assert isinstance(x, string_types)

# Generated at 2022-06-12 20:57:21.086437
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    collection_dir = os.path.join(__location__, 'test_collections', 'ns1', 'coll1')

    # test collection lists when collection is set
    coll_dirs = list(list_collection_dirs([collection_dir], coll_filter='ns1.coll1'))
    assert len(coll_dirs) == 1
    assert coll_dirs[0].endswith(os.path.join('ns1', 'coll1'))

    # test collection lists when namespace is set
    coll_dirs = list(list_collection_dirs([collection_dir], coll_filter='ns1'))
    assert len(coll_dirs) == 1


# Generated at 2022-06-12 20:57:29.992600
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    search_paths = ["/tmp/collections/collection_one", "/tmp/collections/collection_two", "/tmp/collections/collection_three"]

    coll_filter = None
    for collection in list_collection_dirs(search_paths, coll_filter):
        print(collection)

    coll_filter = 'ansible.builtin'
    for collection in list_collection_dirs(search_paths, coll_filter):
        print(collection)

    coll_filter = 'ansible.builtin.ping'
    for collection in list_collection_dirs(search_paths, coll_filter):
        print(collection)


# Generated at 2022-06-12 20:57:38.143635
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test for the generation of valid collection paths.
    """

    # The setUp function in unit test creates a temporary directory.
    # Create a file in that directory with a random name,
    # and then make sure that we can include that file as collections path.

    display.verbosity = 3

    valid_path = "/some/random/place"
    assert valid_path not in list_valid_collection_paths()

    # If not found, warn and return valid paths anyway
    assert valid_path in list_valid_collection_paths([valid_path])

    # Test invalid path, make sure its not in list, no warning
    invalid_path = "/something/thatwont/exist"
    assert invalid_path not in list_valid_collection_paths([invalid_path])

# Generated at 2022-06-12 20:57:48.405699
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    expected_result = ['/etc/ansible/collections']
    actual_result = list(list_valid_collection_paths(search_paths=['/etc/ansible/collections']))
    assert actual_result == expected_result

    expected_result = ['/etc/ansible', '/etc/ansible/collections']
    actual_result = list(list_valid_collection_paths(search_paths=['/etc/ansible', '/etc/ansible/collections']))
    assert actual_result == expected_result

    expected_result = ['/etc/ansible/collections/ansible_collections']
    actual_result = list(list_valid_collection_paths(search_paths=['/etc/ansible/collections/ansible_collections']))
    assert actual_result == expected_

# Generated at 2022-06-12 20:57:51.654426
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_dirs = list(list_collection_dirs(search_paths=[]))
    assert test_dirs
    assert test_dirs[0].endswith("ansible_collections/ansible")

# Generated at 2022-06-12 20:58:00.878499
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test 1 - all paths now valid
    paths = ['/tmp/path1', '/tmp/path2', '/tmp/path3']

    for path in paths:
        try:
            os.mkdir(to_bytes(path, errors='surrogate_or_strict'))
        except OSError:
            pass

    good_paths = list_valid_collection_paths(paths)
    for path in good_paths:
        assert path in paths

    for path in paths:
        try:
            os.rmdir(to_bytes(path, errors='surrogate_or_strict'))
        except OSError:
            pass

    # Test 2 - path doesn't exist
    paths = ['/tmp/path1', '/tmp/path2', '/tmp/path3']
    good_

# Generated at 2022-06-12 20:58:05.475131
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [u"mypath1", u'mypath2']
    assert list(list_collection_dirs(search_paths=paths, coll_filter="namespace.collection")) == []

    assert list(list_collection_dirs(search_paths=paths, coll_filter="namespace.collection")) == []

# Generated at 2022-06-12 20:58:32.186650
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    fact = list_valid_collection_paths()
    assert isinstance(fact, list)
    assert len(fact) > 0
    # return at least one default path
    assert 'ansible_collections' in os.path.basename(fact[0])

    fact = list_valid_collection_paths(['/foo/bar/baz'])
    assert isinstance(fact, list)
    assert len(fact) == 1
    assert '/foo/bar/baz' in fact[0]

    fact = list_valid_collection_paths(['/foo/bar/baz', '/tmp'], warn=True)
    assert isinstance(fact, list)
    assert len(fact) == 1
    assert '/tmp' in fact[0]



# Generated at 2022-06-12 20:58:37.835677
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp

    # Create test directories
    tempdir = mkdtemp()
    non_dir = mkdtemp()
    os.unlink(non_dir)

    config = AnsibleCollectionConfig([
        tempdir,
        non_dir,
    ])

    paths = list(list_valid_collection_paths(config.get_collection_paths()))

    assert [tempdir] == paths

# Generated at 2022-06-12 20:58:45.048371
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    invalid_path = '/tmp/invalid_path'
    valid_path = '/tmp/valid_path'

    # test that list is subset when provided invalid path that doesn't exist
    result = list_valid_collection_paths([valid_path, invalid_path])
    assert len(result) == 1

    # test that list is subset when provided invalid path that exists but is not a directory
    with open(invalid_path, 'w') as f:
        f.write('test_file')

    result = list_valid_collection_paths([valid_path, invalid_path])
    assert len(result) == 1

    # test that list is subset when provided invalid path that exists but is not a directory
    os.mkdir(invalid_path)

    result = list_valid_collection_paths([valid_path, invalid_path])

# Generated at 2022-06-12 20:58:46.383837
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # TODO: this test needs to be expanded
    assert list_valid_collection_paths()

# Generated at 2022-06-12 20:58:57.159795
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    with patch.dict(os.environ, {'ANSIBLE_COLLECTIONS_PATHS': '/foo:/bar'}):
        result = list(list_valid_collection_paths(None))
        assert result == ['/foo', '/bar']

    with patch.dict(os.environ, {'ANSIBLE_COLLECTIONS_PATHS': '/foo:/bar:/spam'}):
        result = list(list_valid_collection_paths(None))
        assert result == ['/foo', '/bar', '/spam']


# Generated at 2022-06-12 20:59:08.860233
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    This unit test covers following cases:
     - Invalid path should be skipped
     - Missing path should be skipped unless it is default path
     - Path which is not a directory should be skipped
    :return:
    """
    import tempfile

    # create a temporary directory
    temp_dir = tempfile.mkdtemp()
    test_path = [
        temp_dir,  # valid path
        os.path.join(temp_dir, 'foo'),  # valid path
        '/invalid/path/foo',  # invalid path
        '/tmp/does-not-exist',  # missing path
        '/usr/sbin/httpd',  # path which is not a directory
    ]

    # Test case 1: Error message should be shown if path does not exists
    display.reset_verbosity_level()
    warnings = []
   

# Generated at 2022-06-12 20:59:17.581968
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test empty search_path
    search_paths = []
    paths = list_valid_collection_paths(search_paths)
    assert paths == []

    # Test valid search_path
    search_paths = [__file__]
    paths = list_valid_collection_paths(search_paths)
    assert paths == [__file__]

    # Test search_path not exists
    search_paths = ["/not/a/real/path"]
    paths = list_valid_collection_paths(search_paths)
    assert paths == []

    # Test search_path is not directory
    search_paths = ["/etc/hosts"]
    paths = list_valid_collection_paths(search_paths)
    assert paths == []



# Generated at 2022-06-12 20:59:22.574843
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['test1/ansible_collections', 'test3', 'test2/ansible_collections']
    coll_filter = None
    for collection in list_collection_dirs(search_paths, coll_filter):
        print(collection)


# Generated at 2022-06-12 20:59:23.887918
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dirs = list_collection_dirs()
    assert len(dirs) > 0

# Generated at 2022-06-12 20:59:31.727156
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    safe_mkdir = lambda x: os.makedirs(to_bytes(x, errors='surrogate_or_strict'), 0o755)
    safe_rmtree = lambda x: shutil.rmtree(to_bytes(x, errors='surrogate_or_strict'))
    safe_write_data = lambda x, y: open(to_bytes(x, errors='surrogate_or_strict'), 'w').write(to_bytes(y))

    with tempfile.TemporaryDirectory() as tempdir:
        search_path = os.path.join(tempdir, 'collection_search_path')
        safe_mkdir(search_path)
        safe_mkdir(os.path.join(search_path, 'ansible_collections'))

# Generated at 2022-06-12 21:00:08.614633
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    koll = list(list_collection_dirs(["/tmp"], 'test.testcoll'))
    assert "/tmp/ansible_collections/test/testcoll" in koll


# Generated at 2022-06-12 21:00:16.620137
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import sys
    import pytest

    if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
        from contextlib import ExitStack
    else:
        from contextlib2 import ExitStack

    from ansible.module_utils import collections_loader
    from ansible.module_utils._text import to_text

    def _test_list_valid_collection_paths(tmpdir, tmpdir_factory):

        with ExitStack() as stack:
            b_ansible_collections = to_bytes('ansible_collections', errors='surrogate_or_strict')
            b_workspace = to_bytes(tmpdir_factory.mktemp('workspace'), errors='surrogate_or_strict')

# Generated at 2022-06-12 21:00:28.803040
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for list_collection_dirs()
    """
    import os
    import shutil
    import tempfile

    def create_temp_collection(path, namespace, collection):
        """
        Create a temporary collection/namespace/plugin file
        """
        target_path = os.path.join(path, namespace, collection, 'plugins', 'action')
        os.makedirs(target_path)
        file_contents = '#'
        target_file = os.path.join(target_path, collection + '.py')
        with open(target_file, 'w') as file_obj:
            file_obj.write(file_contents)

    # Create a temporary collection path to test:
    coll_root = tempfile.mkdtemp()

# Generated at 2022-06-12 21:00:36.772124
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''Unit test for list_valid_collection_paths'''
    search_paths = [
        '/does/not/exist',
        '/etc/ansible',
        '/etc/ansible/ansible_collections',
        '/etc/ansible/ansible_collections/bad_collection',
    ]

    good_paths = [
        '/etc/ansible',
        '/etc/ansible/ansible_collections',
    ]

    valid_paths = list_valid_collection_paths(search_paths)
    for valid_path in valid_paths:
        good_paths.remove(valid_path)

    assert not good_paths

# Generated at 2022-06-12 21:00:42.374014
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [
        '/etc/ansible/collections',
        '/usr/share/ansible/collections',
        '/usr/local/share/ansible/collections',
    ]

    for path in paths:
        assert list_collection_dirs(search_paths=[path])

    assert list_collection_dirs(coll_filter='namespace')
    assert list_collection_dirs(coll_filter='namespace.collection')



# Generated at 2022-06-12 21:00:52.223116
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        './test/units/module_utils/ansible_test/_data/collection_loader',
        './test/units/module_utils/ansible_test/_data/collection_loader/namespace/collection',
        './test/units/module_utils/ansible_test/_data/collection_loader/namespace/collection/plugins/module_utils',
        './test/units/module_utils/ansible_test/_data/collection_loader/namespace/collection/plugins/modules'
    ]

    for path in list_valid_collection_paths(search_paths):
        assert os.path.exists(to_bytes(path))
        assert os.path.isdir(to_bytes(path))


# Generated at 2022-06-12 21:00:53.408615
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    for path in list_collection_dirs():
        assert isinstance(path, bytes)

# Generated at 2022-06-12 21:01:01.031831
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """Test for list_valid_collection_paths function"""

    test_search_paths = [u'~/my_collection_path', u'/etc/ansible/collections']
    result_paths = list(list_valid_collection_paths(search_paths=test_search_paths))
    assert result_paths == [u'/etc/ansible/collections'], \
        "Result paths should have contained just one path"



# Generated at 2022-06-12 21:01:04.978636
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Basic test for list_collection_dirs function
    """
    collection_dir = list_collection_dirs()

    # We should at least get one collection in the root of the collections path list
    assert collection_dir is not None
    assert len(collection_dir) != 0

# Generated at 2022-06-12 21:01:12.140289
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test list_collection_dirs function.
    To be used as a pytest fixture.
    """
    import pytest

    coll_filter = 'test_namespace.test_collection'
    collection_dirs = list_collection_dirs(coll_filter=coll_filter)

    try:
        assert len(collection_dirs) == 1
        test_coll_dir = next(collection_dirs)
        assert test_coll_dir.endswith("ansible_collections/test_namespace/test_collection")
    except StopIteration:
        pytest.fail("No collections found with filter '%s'" % coll_filter)

# Generated at 2022-06-12 21:02:26.759608
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    results = list_collection_dirs()
    assert len(results) == 1
    result = next(results)
    assert result.endswith('ansible_collections/ansible/__init__.py')

    test_coll = 'testcol.testing'
    results = list_collection_dirs(coll_filter=test_coll)
    assert len(results) == 1
    result = next(results)
    assert result.endswith('testcol/testing/__init__.py')

    test_ns = 'testcol'
    results = list_collection_dirs(coll_filter=test_ns)
    assert len(results) == 2

# Generated at 2022-06-12 21:02:28.379045
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    for coll_dir in list_collection_dirs():
        print(coll_dir)

# Generated at 2022-06-12 21:02:37.079858
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert all(list(list_valid_collection_paths(search_paths=["foo"])) == ["foo"])
    assert all(list(list_valid_collection_paths(search_paths=["foo", "bar"])) == ["foo", "bar"])
    assert all(list(list_valid_collection_paths()) == AnsibleCollectionConfig.collection_paths)



# Generated at 2022-06-12 21:02:44.278058
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp
    from shutil import rmtree
    from ansible.collections.ansible.plugins.modules.test_collection.my_test_collection.plugins.modules.test_collection_module import Test
    temp_directory = mkdtemp()

# Generated at 2022-06-12 21:02:46.122611
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths([__file__])) == [__file__]

# Generated at 2022-06-12 21:02:56.535283
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Check that the search paths are filtered correctly
    assert list(list_valid_collection_paths([])) == AnsibleCollectionConfig.collection_paths

    # Check that the default paths are not repeated
    assert len(list(list_valid_collection_paths())) == len(AnsibleCollectionConfig.collection_paths)

    # Check that extra non existing paths are filtered out
    assert list(list_valid_collection_paths(['/not/real/path'])) == AnsibleCollectionConfig.collection_paths

    # Check that existing paths are not filtered out
    assert list(list_valid_collection_paths(['/'])) == ['/'] + AnsibleCollectionConfig.collection_paths

    # Check that existing paths are not filtered out and extra paths are dropped

# Generated at 2022-06-12 21:03:04.156406
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test that the list iterator handles duplicate or invalid paths
    :return:
    """

    # test empty list
    assert {} == dict(list_valid_collection_paths(['not_found']))

    # test default collection paths
    assert {'/etc/ansible/collections'} == set(list_valid_collection_paths())

    # test duplicates
    assert {'/etc/ansible/collections'} == set(list_valid_collection_paths(['/etc/ansible/collections', '/etc/ansible/collections']))

# Generated at 2022-06-12 21:03:16.073768
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import pytest
    from ansible.collections.ansible.community.plugins.module_utils.common.collection_loader import list_collection_dirs

    from tempfile import mkdtemp

    from shutil import rmtree

    # Make a temp directory of temporary directories
    temp_dir = mkdtemp()

    # Make a collection path
    coll_dir = "{}/ansible_collections/namespace/collection/docs".format(temp_dir)
    os.makedirs(coll_dir)
    # Get the path of the collection
    collection_dir = list(list_collection_dirs([temp_dir]))

    # check that the above path is returned
    assert collection_dir == [b'/tmp/tmp1p45lkzr/ansible_collections/namespace/collection']

    # cleanup
    r

# Generated at 2022-06-12 21:03:23.657951
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.constants import DEFAULT_COLLECTIONS_PATHS
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 0
    
    import sys

    if sys.platform != 'win32':
        search_paths = ['~/.ansible/collections']
    else:
        search_paths = ['c:\\collections']

    search_paths.extend(DEFAULT_COLLECTIONS_PATHS)
    coll_filter = 'ansible.builtin'
    coll_dirs = list(list_collection_dirs(search_paths, coll_filter))
    assert len(coll_dirs) == 2

if __name__ == '__main__':
    test_list_collection_dirs()

# Generated at 2022-06-12 21:03:32.101488
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Run unit test for list_valid_collection_paths
    """

    from ansible.utils.collection_loader import list_valid_collection_paths

    test_paths = [
        '/path/does/not/exist',
        '/path/is/not/directory',
        '/path/is/a/valid/collection',
        '/path/is/a/valid/collection'
    ]

    mock_isdir = [False, True, True, False]

    mock_exists = [False, True, True, False]

    mock_config = [True, True, False, False]

    def mock_file_exists(path):
        if path == to_bytes('/path/is/a/valid/collection'):
            return True
        return False
