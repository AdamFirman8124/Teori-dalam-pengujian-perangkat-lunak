

# Generated at 2022-06-12 20:53:42.197953
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # This test uses sample paths as well as real paths.
    # It uses the fact that collection root dir (ansible_collections) does not exist at the default config's path.

    # test with only default path
    paths = list(list_valid_collection_paths())
    assert len(paths) == 1

    # add some non-existent paths that do not exist
    paths.append("/somedir/somedirectory")
    paths.append("C:\\somedir\\somedirectory")
    paths.append("path with spaces")
    paths.append("/nonexistent/path/with/spaces")
    paths.append("C:\\nonexistent\\path\\with\\spaces")
    paths.append("/home/someuser")
    paths.append("C:\\someuser")

# Generated at 2022-06-12 20:53:51.003087
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    temp_path = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_path, 'ansible_collections'))
    os.mkdir(os.path.join(temp_path, 'ansible_collections', 'namespace'))
    os.mkdir(os.path.join(temp_path, 'ansible_collections', 'namespace', 'collection'))
    os.mkdir(os.path.join(temp_path, 'ansible_collections', 'namespace', 'collection', 'plugins'))
    os.mkdir(os.path.join(temp_path, 'ansible_collections', 'namespace', 'collection', 'plugins', 'action'))

# Generated at 2022-06-12 20:53:58.611027
# Unit test for function list_collection_dirs

# Generated at 2022-06-12 20:54:09.177587
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test case: existing valid dir
    search_paths = ["/home/ansible/collections"]
    paths = list(list_valid_collection_paths(search_paths))
    assert len(paths) == 1

    # Test case: non-existing dir
    search_paths = ["/nonexisting"]
    paths = list(list_valid_collection_paths(search_paths))
    assert len(paths) == 0

    # Test case: exists, but not a directory
    search_paths = ["/etc/fstab"]
    paths = list(list_valid_collection_paths(search_paths))
    assert len(paths) == 0

    # Test case: nowarn
    search_paths = ["/etc/hosts"]

# Generated at 2022-06-12 20:54:14.952569
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['/usr/share/ansible','/etc/ansible']
    for path in list_collection_dirs(search_paths):
        print("collection path: ", path)

# Generated at 2022-06-12 20:54:23.020088
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    found = list_valid_collection_paths(search_paths=["/foo", "/bar", "/baz"], warn=False)
    assert len(list(found)) == 3

    found = list_valid_collection_paths(search_paths=["/foo", "/bar", "/baz"], warn=True)
    assert len(list(found)) == 3

    found = list_valid_collection_paths(search_paths=["/invalid/path", "/bar", "/baz"], warn=False)
    assert len(list(found)) == 2

    found = list_valid_collection_paths(search_paths=["/invalid/path", "/bar", "/baz"], warn=True)
    assert len(list(found)) == 2

# Generated at 2022-06-12 20:54:33.815186
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import textwrap
    import tempfile
    import shutil

    import pytest

    _tempdir = tempfile.mkdtemp()
    search_paths = [
        os.path.join(os.path.dirname(__file__), 'fixtures', 'test_collections'),
        _tempdir,
    ]

    dirs = list(list_collection_dirs(search_paths=search_paths, coll_filter='mynamespace.mycollection'))
    assert len(dirs) == 1

    for d in dirs:
        assert d.endswith(b'mynamespace.mycollection')

    # test without any collections matching
    dirs = list(list_collection_dirs(search_paths=search_paths, coll_filter='no.such.collection'))

# Generated at 2022-06-12 20:54:44.913741
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test with Default
    populated = list(list_valid_collection_paths())
    assert len(populated) == 1

    # Test with single path
    populated = list(list_valid_collection_paths(['/tmp']))
    assert len(populated) == 1
    assert populated[0] == '/tmp'
    assert not os.path.exists(populated[0])

    populated = list(list_valid_collection_paths(['/tmp'], warn=True))
    assert len(populated) == 0

    # Test with multiple paths
    populated = list(list_valid_collection_paths(['/tmp', '/usr/local/share', '/usr/share']))
    assert len(populated) == 3
    assert populated[0] == '/tmp'

# Generated at 2022-06-12 20:54:48.167631
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import pytest
    from ansible.module_utils.common.collections import list_valid_collection_paths

    # expect one default path if none are given
    result = list_valid_collection_paths()
    assert len(result) == 1

    # expect two paths if one exists and one does not exist
    result = list_valid_collection_paths([os.path.abspath('.'), 'something/unknown'])
    assert len(result) == 2

# Generated at 2022-06-12 20:55:00.957759
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # valid paths
    p1 = os.path.abspath(os.path.expanduser("~/collections"))
    assert list_valid_collection_paths([p1]) == [p1]

    p1 = os.path.abspath(os.path.expanduser("~/collections"))
    p2 = os.path.abspath(os.path.expanduser("~/collections2"))
    assert list_valid_collection_paths([p1, p2]) == [p1, p2]

    # invalid paths
    assert list(list_valid_collection_paths(['/tmp/does/not/exist'])) == []
    assert list(list_valid_collection_paths(['/etc/passwd'])) == []

    # default

# Generated at 2022-06-12 20:55:13.826770
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader_test import collection_loader_config

    coll_names = []
    for path in list_collection_dirs(collection_loader_config):
        assert os.path.exists(path)
        assert path not in coll_names
        assert os.path.isdir(path)
        assert path.endswith(b".ansible_collections")
        coll_names.append(path)

    assert b"ansible_namespace.collection_name.subcollection" in coll_names



# Generated at 2022-06-12 20:55:24.640570
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    path1 = '.'
    path2 = 'not_a_dir'
    path3 = './no_ansible_collections_dir_here'

    # test default list
    default_list = list(list_valid_collection_paths())
    assert len(default_list) == 1

    # test default list plus one new path
    default_plus_1_list = list(list_valid_collection_paths([path1]))
    assert len(default_plus_1_list) == 2

    # test empty list plus one path that does not resolve
    assert len(list(list_valid_collection_paths([path2]))) == 0

    # test empty list plus one path that resolves but does not contain valid dir
    assert len(list(list_valid_collection_paths([path3]))) == 0

    # test

# Generated at 2022-06-12 20:55:29.085300
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    my_paths = ['~/.ansible/collections', '~/.ansible/my_collections', '~/.ansible/your_collections']
    for path in list_collection_dirs(my_paths):
        print(path)

# Generated at 2022-06-12 20:55:30.903010
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    pass



# Generated at 2022-06-12 20:55:38.835006
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Standard use case
    search_paths = ['/first/path', '/second/path']
    valid_paths = list(list_valid_collection_paths(search_paths))
    assert len(valid_paths) == 2
    assert all(p in search_paths for p in valid_paths)

    # Warn if path does not exist
    invalid_search_paths = ['/bad/path', '/second/path']
    valid_paths = list(list_valid_collection_paths(invalid_search_paths, warn=True))
    assert len(valid_paths) == 1
    assert '/second/path' in valid_paths

    # Warn if path is not a directory
    file_search_path = ['/sample.txt', '/second/path']

# Generated at 2022-06-12 20:55:48.671970
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test filtering on non existent path
    actual = list(list_valid_collection_paths(search_paths=['/tmp']))
    assert actual == []

    # Test filtering on a bad path type
    actual = list(list_valid_collection_paths(search_paths=['/tmp/fake_collections']))
    assert actual == []

    # Test filtering on a valid path
    actual = list(list_valid_collection_paths(search_paths=[AnsibleCollectionConfig.collection_paths[0]]))
    assert actual[0] == AnsibleCollectionConfig.collection_paths[0]
    assert len(actual) == 1

# Generated at 2022-06-12 20:55:52.081076
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = ['../../foo', '../bar']
    expected = [os.path.abspath(os.path.join('../..', 'foo')), os.path.abspath(os.path.join('..', 'bar'))]
    actual = list_valid_collection_paths(paths)

    assert list(actual) == expected

# Generated at 2022-06-12 20:55:53.277206
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths == list_valid_collection_paths



# Generated at 2022-06-12 20:56:01.143141
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = [
        "/dev/null",
        "/tmp/ansible_collections",
        "/tmp/ansible_collections/ansible_collections",
    ]

    path_list = list(list_collection_dirs(search_paths=search_paths, coll_filter='testns.testcoll'))

    assert len(path_list) == 1
    assert path_list[0] == to_bytes("/tmp/ansible_collections/ansible_collections/testns/testcoll")

# Generated at 2022-06-12 20:56:08.618305
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_dirs = [ '/dev', '/tmp', '/this/path/does/not/exist', '/etc' ]
    test_dir_results = list(list_valid_collection_paths(search_paths=test_dirs, warn=True))

    # This assumes the test suite has been run with the WD at the root of the git repo.
    assert '/etc' in test_dir_results
    assert '/tmp' in test_dir_results
    assert '/dev' not in test_dir_results
    assert '/this/path/does/not/exist' not in test_dir_results
    assert '/ansible_collections' in test_dir_results
    assert '/__not_a_path__' not in test_dir_results



# Generated at 2022-06-12 20:56:30.356872
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Test with a non-failing collection, expect one result."""
    coll_dirs = list(list_collection_dirs(['test/units/module_utils/collection_loader'], coll_filter='my.collection'))
    assert len(coll_dirs) == 1, 'Should be one result, but was %d' % len(coll_dirs)

    # test with a non-existing collection path
    coll_dirs = list(list_collection_dirs(['test/units/module_utils/collection_loader'],
                                          coll_filter='non.existingcollection'))
    assert len(coll_dirs) == 0, 'Should be no results, but was %d' % len(coll_dirs)

    # test with a non-existing search path

# Generated at 2022-06-12 20:56:41.918943
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from collections import defaultdict, namedtuple
    from ansible.utils.path import unfrackpath, makedirs_safe

    # Create example collections
    def _coll(ns, coll):
        return unfrackpath("/tmp/ansible_collections/{}/{}/".format(ns, coll))

    Coll = namedtuple("Coll", ['namespace', 'collection'])
    test_colls = [
        Coll("a", "b"),
        Coll("a", "c"),
        Coll("a", "d"),
        Coll("e", "d"),
    ]
    for coll in test_colls:
        coll_path = _coll(coll.namespace, coll.collection)
        makedirs_safe(coll_path)

    def _test_coll_paths(coll_spec, expected):
        coll

# Generated at 2022-06-12 20:56:47.121292
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_path = [b'/nonexistantdir', b'/nonexistantdir2', b'/etc/ansible']

    print()
    for p in list_valid_collection_paths(search_path, warn=True):
        print("%s" % p)



# Generated at 2022-06-12 20:56:55.860537
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    import tempfile
    import shutil
    import os

    # create empty temp dir
    temp_dir = tempfile.mkdtemp()
    assert os.path.isdir(temp_dir)

    # create collection in temp dir
    test_coll_path = os.path.join(temp_dir, 'test_collection')
    assert not os.path.exists(test_coll_path)
    assert not os.path.exists(test_coll_path+'.tar.gz')

    os.makedirs(os.path.join(test_coll_path, 'plugins', 'modules'))
    assert os.path.isdir(test_coll_path)

# Generated at 2022-06-12 20:56:58.501950
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test no config
    found = list(list_valid_collection_paths())
    assert len(found) == 1

    # Test specific paths
    found = list(list_valid_collection_paths(['/foo', '/bar']))
    assert len(found) == 1



# Generated at 2022-06-12 20:57:08.001147
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import ansible_collections

    test_search_path = '/no/such/path/foo/bar'
    test_collection_paths = [os.path.join(tempfile.gettempdir(), 'collections')]

    coll_root = os.path.join(test_collection_paths[0], 'ansible_collections')
    os.makedirs(coll_root)
    ns_dir = os.path.join(coll_root, 'namespace')
    os.makedirs(ns_dir)

    # This one will not be returned because it has no __init__.py
    no_init_dir = os.path.join(ns_dir, 'nocollection')
    os.makedirs(no_init_dir)


# Generated at 2022-06-12 20:57:17.414835
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        '/not/a/path',
        '/dev/null'
    ]

    paths = list(list_valid_collection_paths(search_paths=search_paths))

    assert len(paths) == 2

    search_paths = [
        '/',
        '/dev'
    ]

    paths = list(list_valid_collection_paths(search_paths=search_paths))

    assert len(paths) == 2

    search_paths = [
        '/dev/null',
        '/dev'
    ]

    paths = list(list_valid_collection_paths(search_paths=search_paths))

    assert len(paths) == 2

    search_paths = [
        '/dev/null',
        '/dev/null'
    ]

# Generated at 2022-06-12 20:57:29.690621
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys

    def root_path():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

    search_paths = [
        # this library
        os.path.join(root_path(), 'lib', 'ansible', 'collections', 'ansible_collections'),
        # collections test folder
        os.path.join(root_path(), 'test', 'units', 'lib'),
        # this library but in the form of a collection
        os.path.join(root_path(), 'lib', 'ansible_collections', 'ansible', 'collections', 'test_collections'),
    ] + sys.path

    colls = list(list_collection_dirs(search_paths))
    assert 2 == len(colls)

# Generated at 2022-06-12 20:57:36.550881
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import list_collection_dirs

    coll_dirs = list_collection_dirs()
    assert coll_dirs is not None
    assert len(coll_dirs) > 0

    # make sure a missing path fails
    coll_dirs_2 = list_collection_dirs(("/this/path/doesnt/exist"))
    assert coll_dirs_2 == []

    # make sure non-directory paths fail
    coll_dirs_2 = list_collection_dirs(("/etc/hosts"))
    assert coll_dirs_2 == []



# Generated at 2022-06-12 20:57:37.932885
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths(["doesnotexists", "/tmp", "/tmp/doesnotexist"])) == list(["/tmp"])

# Generated at 2022-06-12 20:57:58.132991
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert(list(set(list_collection_dirs(coll_filter="test_namespace.test_collection"))) ==
           list(set(["/Users/user/projects/ansible/test/units/lib/ansible/config/data/ansible_collections/"
                    "test_namespace/test_collection"])))
    assert(list(set(list_collection_dirs(coll_filter="test_namespace"))) ==
           list(set(["/Users/user/projects/ansible/test/units/lib/ansible/config/data/ansible_collections/"
                    "test_namespace/test_collection"])))

# Generated at 2022-06-12 20:58:08.200116
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    cwd = os.getcwd()
    search_paths = [
        './', # Test that it should be fine, even if it does not exist
        './does_not_exist', # Test that it should be fine, even if it does not exist
        os.path.join(cwd, 'does_not_exist'), # Test that it should be fine, even if it does not exist
        '/etc', # Test that it should be fine, even if it is not a directory
    ]

    valid_paths = list(list_valid_collection_paths(search_paths))

    assert len(valid_paths) == 1
    assert valid_paths[0] == os.path.join(cwd, 'does_not_exist')


# Generated at 2022-06-12 20:58:11.068063
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths()
    assert list_valid_collection_paths(search_paths=['tests/data/collections'])


# Generated at 2022-06-12 20:58:19.211821
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # list_collection_dirs: name, path, namespace, collection
    tests = []

    # simple root-level collection
    tests.append(('ns1.coll1', 'ns1.coll1', 'ns1', 'coll1'))
    tests.append(('ns1.coll2', 'ns1.coll2', 'ns1', 'coll2'))

    # sub-namespace collection
    tests.append(('ns1.colls.coll1', 'ns1/colls/coll1', 'ns1.colls', 'coll1'))
    tests.append(('ns1.colls.coll2', 'ns1/colls/coll2', 'ns1.colls', 'coll2'))

    # multiple root namespace

# Generated at 2022-06-12 20:58:24.218829
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Unit test
    """
    search_paths = [
        "/fake/path",
        "/fake/path/2",
    ]
    assert list(list_valid_collection_paths(search_paths)) == ['/fake/path', '/fake/path/2']



# Generated at 2022-06-12 20:58:35.272021
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # ./ansible/test/units/modules/utils/test_collections_loader.py
    assert(len(list(list_valid_collection_paths())) == 1)
    assert(len(list(list_valid_collection_paths(search_paths=[u'%%']))) == 0)
    assert(len(list(list_valid_collection_paths(search_paths=[u'/tmp']))) == 1)
    assert(len(list(list_valid_collection_paths
                    (search_paths=[u'/tmp', u'%%', u'../', u'../collection_loader']))) == 1)
    assert(len(list(list_valid_collection_paths(search_paths=[u'..']))) == 0)
    # ./ansible/test/units/module_utils/basic.py


# Generated at 2022-06-12 20:58:43.464957
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ["/data/home/darryl/ansible_collections_test/ns1/coll1/plugins/collection_test",
                    "/data/home/darryl/ansible_collections_test/ns2"]

    coll_dirs = list_collection_dirs(search_paths, "ns1.coll1")
    coll_dirs = list(coll_dirs)
    assert len(coll_dirs) == 1
    assert b"coll1" in coll_dirs[0]

    coll_dirs = list_collection_dirs(search_paths, "ns1.coll2")
    coll_dirs = list(coll_dirs)
    assert len(coll_dirs) == 1
    assert b"coll2" in coll_dirs[0]

    coll_dir

# Generated at 2022-06-12 20:58:54.296708
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Set up a test config
    b_tmpdir = to_bytes(os.path.dirname(__file__))
    b_testdir = os.path.join(b_tmpdir, b'test_collection_loader')
    os.makedirs(b_testdir)
    os.makedirs(os.path.join(b_testdir, b'collections'))
    os.makedirs(os.path.join(b_testdir, b'collections', b'ansible_collections'))
    os.makedirs(os.path.join(b_testdir, b'collections', b'ansible_collections', b'test.collection'))

# Generated at 2022-06-12 20:59:00.677612
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    # create valid collection on tmpfs
    coll_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(coll_dir, "testcoll.testmod"))
    # test for valid collection in single dir
    results = list(list_collection_dirs([coll_dir], "testcoll.testmod"))
    assert results == [os.path.join(coll_dir, "testcoll.testmod")]
    # test for valid collection in no path
    results = list(list_collection_dirs([], "testcoll.testmod"))
    assert results == []
    # test for invalid collection in specified path
    results = list(list_collection_dirs([coll_dir], "doesntexist.doesntexist"))
    assert results == []
    # test for invalid collection in no path


# Generated at 2022-06-12 20:59:12.426393
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible_collections.ansible.builtin import plugins
    import ansible.module_utils.facts
    import ansible.module_utils.common
    import ansible_collections.ansible.builtin.plugins.cache

    collection_namespace = plugins.__name__.split('.', 2)[0]
    collection_name = plugins.__name__.split('.', 2)[1]

    print("Testing ansible.builtin plugins collection (%s.%s):" % (collection_namespace, collection_name))
    plugin_dirs = list_collection_dirs(coll_filter="%s.%s" % (collection_namespace, collection_name))
    assert ansible.module_utils.facts.__file__.startswith(plugin_dirs.next())
    assert ansible.module_utils.common

# Generated at 2022-06-12 20:59:28.695307
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.collections import is_collection_path

    collection_loader = AnsibleCollectionLoader()

    for coll in list_collection_dirs(search_paths=collection_loader.get_collection_paths()):
        assert is_collection_path(coll)
        assert coll.endswith(b'ansible_collections')

    assert not list(list_valid_collection_paths(warn=True))



# Generated at 2022-06-12 20:59:37.358306
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    path_prefix = tempfile.mkdtemp()
    path_list = []

    path_list.append(os.path.join(path_prefix, 'ansible_collections', 'test1', 'test2'))
    os.makedirs(path_list[0])
    path_list.append(os.path.join(path_prefix, 'ansible_collections', 'test1', 'test3'))
    os.makedirs(path_list[1])
    path_list.append(os.path.join(path_prefix, 'ansible_collections', 'test4', 'test5'))
    os.makedirs(path_list[2])

    path_list.append(os.path.join(path_prefix, 'ansible_collections', 'test1'))


# Generated at 2022-06-12 20:59:45.005057
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # create directory
    #   /tmp/list_valid_collection_paths_test
    # and /tmp/list_valid_collection_paths_test/ansible_collections/
    # and /tmp/list_valid_collection_paths_test/ansible_collections/file
    # populate /tmp/list_valid_collection_paths_test/ansible_collections/file with collection file
    # create /tmp/list_valid_collection_paths_test/file as a file

    import tempfile
    import shutil
    import atexit

    tmpdir = tempfile.mkdtemp()
    coll_dir = os.path.join(tmpdir, "ansible_collections")
    os.mkdir(coll_dir)
    coll_dir = os.path.join(coll_dir, "file")

# Generated at 2022-06-12 20:59:52.760318
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test that each collection type is present in the list of known collection directories.
    """
    dirs = list(list_collection_dirs())
    assert len(set(dirs)) >= 4
    if os.path.isdir('test/integration/roles'):
        assert any(x.endswith('test/integration/roles') for x in dirs)
    assert any(x.endswith('ansible_collections/ansible/roles') for x in dirs)
    assert any(x.endswith('ansible_collections/ansible_collections/bdehaan/system') for x in dirs)
    assert any(x.endswith('ansible_collections/bdehaan/system') for x in dirs)

# Generated at 2022-06-12 21:00:00.167526
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    temp_path = "/tmp"
    default_paths = AnsibleCollectionConfig.collection_paths

    assert list(list_valid_collection_paths()) == list(default_paths)
    assert list(list_valid_collection_paths([])) == list(default_paths)
    assert list(list_valid_collection_paths([temp_path])) == [temp_path]
    assert list(list_valid_collection_paths([temp_path, None])) == [temp_path]

# Generated at 2022-06-12 21:00:09.621979
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common._collections_compat import Path
    from ansible.module_utils._text import to_text

    test_dirs = ['does_not_exist', 'does_not_exist2']
    search_paths = [Path('does_not_exist'), Path('does_not_exist2')]

    display.display = Display(verbosity=0)

    with Display.captured() as output:
        valid_search_paths = list(list_valid_collection_paths(search_paths, warn=True))

    assert len(valid_search_paths) == 0

# Generated at 2022-06-12 21:00:17.077098
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile

    test_paths = ['/tmp',
                  '/tmp/ansible_collections',
                  os.path.join(tempfile.gettempdir(), 'ansible_collections'),
                  os.path.join(tempfile.gettempdir(), 'ansible_collections', 'test_ns'),
                  os.path.join(tempfile.gettempdir(), 'ansible_collections', 'test_ns', 'test_coll')]

    # create first half of test paths
    for x in test_paths[:2]:
        try:
            os.makedirs(to_bytes(x))
        except OSError:
            pass

    # test that only half of paths are valid
    valid_paths = list_valid_collection_paths(test_paths)

# Generated at 2022-06-12 21:00:22.324912
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    expected_path = os.path.join(os.getcwd(), 'ansible_collections', 'ansible', 'collection1')
    actual_paths = list(list_collection_dirs(coll_filter='ansible.collection1'))

    assert expected_path in actual_paths



# Generated at 2022-06-12 21:00:27.586846
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    path1 = "/usr/share/ansible/collections"
    path2 = "/path/to/not_exist"
    paths = [path1, path2]

    # this still works because list_collection_dirs() filters out the non existent path
    dirs = list(list_collection_dirs(paths))

    assert dirs

# Generated at 2022-06-12 21:00:35.532020
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import StringIO
    from ansible.collection_loader.utils import list_valid_collection_paths
    from ansible.collections import COLLECTIONS_PATHS

    # Test default paths
    print(list(list_valid_collection_paths()))
    assert list(list_valid_collection_paths()) == list(COLLECTIONS_PATHS)

    # Test default paths with additional user paths
    print(list(list_valid_collection_paths(['/usr/share/ansible/collections'])))

# Generated at 2022-06-12 21:01:07.285146
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['./test/unit/files/collections/foo',
                    './test/unit/files/collections/bar',
                    './test/unit/files/collections/baz']
    collections = list(list_collection_dirs(search_paths))
    assert len(collections) == 6

    # test namespacing
    collections = list(list_collection_dirs(search_paths, 'bar'))
    assert len(collections) == 2

    # test single collection
    collections = list(list_collection_dirs(search_paths, 'baz.bak'))
    assert len(collections) == 1

    # test no search_paths
    collections = list(list_collection_dirs())
    assert len(collections) == 0


# Unit test to check

# Generated at 2022-06-12 21:01:17.268975
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    tmpdir = to_bytes(tempfile.mkdtemp())
    testdir = os.path.join(tmpdir, b'test_list_valid_collection_paths')
    os.makedirs(testdir)
    os.makedirs(os.path.join(testdir, b'ansible_collections'))
    os.makedirs(os.path.join(testdir, b'ansible_collections', b'not_a_collection'))

    paths = list(list_valid_collection_paths([testdir]))
    assert paths == [testdir]

    os.makedirs(os.path.join(testdir, b'ansible_collections', b'my_namespace'))
    paths = list(list_valid_collection_paths([testdir]))


# Generated at 2022-06-12 21:01:27.029836
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils import basic
    import os
    import six

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    # Test list_collection_dirs with no argument
    dirs = list_collection_dirs()
    for d in dirs:
        assert os.path.isdir(d)

    # Test list_collection_dirs with a single value
    dirs = list_collection_dirs(search_paths=['/tmp/test_collection'])
    for d in dirs:
        assert os.path.isdir(d)

    # Test list_collection_dirs with two values
    dirs = list_collection_dirs(search_paths=['/tmp/test_collection', '/tmp/test_collection2'])

# Generated at 2022-06-12 21:01:34.179114
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    try:
        # This will fail since the default collections path doesn't exist
        ansible_collections_path = list(list_valid_collection_paths(warn=True))
        assert ansible_collections_path == []
    except SystemExit:
        # display.warning raises SystemExit the first time it's called
        # so catch it and continue
        pass

    ansible_collections_path = list(list_valid_collection_paths([os.path.dirname(__file__)]))
    assert ansible_collections_path == [os.path.dirname(__file__)]



# Generated at 2022-06-12 21:01:42.899256
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test if list_collection_dirs returns dirs for specific collection
    """

    from ansible.utils.collection_loader import AnsibleCollectionNotFoundError
    from ansible.module_utils.common._collections_compat import to_text
    import tempfile
    import os

    tempdir = tempfile.mkdtemp()
    tempdir_ansible_collections = os.path.join(tempdir, 'ansible_collections')
    tempdir_ansible_namespace = os.path.join(tempdir, 'ansible_collections', 'ansible')
    tempdir_test_collection = os.path.join(tempdir, 'ansible_collections', 'ansible', 'test')

    os.makedirs(tempdir_test_collection)


# Generated at 2022-06-12 21:01:55.614010
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    display.verbosity = 4
    # collection paths should be returned
    search_paths = ["../../..", "../../../../"]
    paths = list(list_valid_collection_paths(search_paths))
    assert len(paths) == 2
    assert "../../.." in paths

    # missing paths should be skipped but warning should be raised
    search_paths = ["foo"]
    paths = list(list_valid_collection_paths(search_paths, warn=True))
    assert len(paths) == 0

    # non directory paths should be skipped but warning should be raised
    search_paths = ["setup.cfg"]
    paths = list(list_valid_collection_paths(search_paths, warn=True))
    assert len(paths) == 0

# Generated at 2022-06-12 21:02:05.663709
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test collection paths with filenames
    test_paths = [
        '~/my_collections',
        '/path/to/my_collections',
        'relative/path/to/my_collections',
        'my_collections',
    ]

    new_paths = list(list_collection_dirs(search_paths=test_paths))

    # Test collection paths with directory
    test_paths = [
        '~/ansible_collections',
        '/path/to/ansible_collections',
        'relative/path/to/ansible_collections',
        'ansible_collections',
    ]

    new_paths = list(list_collection_dirs(search_paths=test_paths))

    # Test collection path with directory and filter
    test_paths

# Generated at 2022-06-12 21:02:16.759119
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Should return default collection paths
    expected_result = [
        '/usr/share/ansible/collections',
        '/usr/local/share/ansible/collections',
        '~/.ansible/collections'
    ]
    actual_result = list_valid_collection_paths()
    assert isinstance(actual_result, list)
    assert len(actual_result) == 3
    assert actual_result == expected_result

    # Should return empty list, if no search paths are provided
    expected_result = []
    actual_result = list_valid_collection_paths(None)
    assert isinstance(actual_result, list)
    assert len(actual_result) == 0
    assert actual_result == expected_result

    # Should return search paths provided by user

# Generated at 2022-06-12 21:02:20.737812
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test function list_collection_dirs
    """
    assert os.path.isdir(list(list_collection_dirs(coll_filter="namespace.collection")).pop())
    assert is_collection_path(list(list_collection_dirs(coll_filter="namespace")).pop())



# Generated at 2022-06-12 21:02:30.714292
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    #returns all the valid paths
    assert list_valid_collection_paths(['../test/unit/utils/test_collections', '../test/unit/utils']) == [
        '../test/unit/utils/test_collections', '../test/unit/utils']
    #returns only the valid paths
    assert list_valid_collection_paths(
        ['../test/unit/utils/test_collections', '../test/unit/utils', '../test/unit/utils/test_collections_notexist']) == \
           ['../test/unit/utils/test_collections', '../test/unit/utils']
    #returns only the valid paths

# Generated at 2022-06-12 21:03:20.390365
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = [
        '/tmp/foo/bar/baz',
        '/tmp/foo',
        '/tmp/bad/path',
        '/tmp/file',
    ]

    valid = list(list_valid_collection_paths(paths, warn=False))
    for path in valid:
        assert os.path.exists(path)
        assert os.path.isdir(path)

    for path in paths:
        if path not in valid:
            assert not os.path.exists(path)

