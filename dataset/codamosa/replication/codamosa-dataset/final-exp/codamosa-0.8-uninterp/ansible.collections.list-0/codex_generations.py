

# Generated at 2022-06-12 20:53:43.405563
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    coll_paths = ['/tmp/c1', '/tmp/c2']

    coll_paths = list_valid_collection_paths(coll_paths, warn=False)
    assert len(coll_paths) == 0

    # return value depends on where this test is run, but it should not be empty
    coll_paths = list_valid_collection_paths(None, warn=False)
    assert len(coll_paths) > 0

    # filters
    coll_paths = list(list_collection_dirs(None, None))
    assert len(coll_paths) > 0

    # specific namespace
    coll_paths = list(list_collection_dirs(None, 'foo'))
    assert len(coll_paths) > 0

    # specific collection

# Generated at 2022-06-12 20:53:45.857016
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert(set(list_collection_dirs([])) == {b'ansible_collections/ansible/unittest_collections_loader'})

# Generated at 2022-06-12 20:53:55.347754
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    ''' Test that list_collection_dir returns a sorted list of valid
    collection paths'''

    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    from ansible.module_utils._text import to_text

    coll_dirs = list_collection_dirs(search_paths=['/tmp/ansible_collections'])
    assert coll_dirs is None, 'Empty collection directory list returned'

    coll_dirs = list_collection_dirs(search_paths=None)
    assert coll_dirs is None, 'Empty collection directory list returned'

    coll_dirs = list(list_collection_dirs(search_paths=[AnsibleCollectionConfig.collections_paths[0]]))
   

# Generated at 2022-06-12 20:54:07.432496
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Create temp dir
    tmp_dir = './test_path'
    os.mkdir(tmp_dir)
    # Create a config file
    coll_config_file = './test_path/test.yml'
    with open(coll_config_file, 'w') as f:
        f.write('collections_paths:\n - {0}'.format(tmp_dir))

    # Test that the temp directory has been filtered out
    paths = ['./test_path']
    assert list_collection_dirs(paths) == []

    # Test if the config file with the temp directory was filtered out
    paths = [coll_config_file]
    assert list_collection_dirs(paths) == []

    # Test if an existing dir is not filtered out

# Generated at 2022-06-12 20:54:17.263192
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import mock
    import tempfile
    paths = [
        str(tempfile.mkdtemp()),
        tempfile.mkstemp()[1],
        tempfile.mkstemp()[1],
        str(tempfile.mkdtemp()),
        str(tempfile.mkdtemp())
    ]

    valid_paths = list(list_valid_collection_paths(paths))
    assert len(valid_paths) == 3
    assert paths[0] in valid_paths
    assert paths[3] in valid_paths
    assert paths[4] in valid_paths



# Generated at 2022-06-12 20:54:28.867829
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    search_paths = [tempfile.mkdtemp()]
    os.mkdir(os.path.join(to_bytes(search_paths[0], errors='surrogate_or_strict'), b'ansible_collections'))
    os.mkdir(os.path.join(to_bytes(search_paths[0], errors='surrogate_or_strict'), b'ansible.builtin'))
    os.mkdir(os.path.join(to_bytes(search_paths[0], errors='surrogate_or_strict'), b'ansible_collections', b'ansible.builtin'))

    # Test invalid collection

# Generated at 2022-06-12 20:54:35.882646
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # make sure we don't find any collections
    assert list(list_collection_dirs(search_paths=[os.path.join(os.path.dirname(__file__), 'data', 'test_list_collection_dirs')])) == []
    # make sure we actually find our collection
    collection_paths = list(list_collection_dirs(search_paths=[os.path.join(os.path.dirname(__file__), 'data', 'test_list_collection_dirs', 'ansible_collections')]))
    assert len(collection_paths) == 1
    assert os.path.basename(collection_paths[0]) == 'dummy_collection'

# Generated at 2022-06-12 20:54:39.503285
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert '/does/not/exist' in list_valid_collection_paths(['/does/not/exist'])
    assert '/etc/ansible' in list_valid_collection_paths(['/etc/ansible'])

# Generated at 2022-06-12 20:54:49.861852
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_path = os.path.join(os.getcwd(), 'test', 'units', 'utils', 'mock_collections')
    all_colls = ['/tmp/test/units/utils/mock_collections/ansible_collections/my_namespace/my_collection1',
                 '/tmp/test/units/utils/mock_collections/ansible_collections/my_namespace/my_collection2']

    try:
        # Test with invalid search_path
        search_paths = ['tests/units/utils/mock_collections']
        assert list(list_collection_dirs(search_paths)) == []
    except FileNotFoundError:
        pass


# Generated at 2022-06-12 20:54:59.237217
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test vars
    search_paths = ['/tmp/junk', '/tmp/junk/subdir', '/tmp']

    # test no search paths provided
    assert list(list_valid_collection_paths([])) == []

    # test that existing paths are returned
    assert list(list_valid_collection_paths(search_paths, warn=True)) == ['/tmp']

    # test that non-existent paths are excluded
    assert list(list_valid_collection_paths(search_paths, warn=True)) == ['/tmp']



# Generated at 2022-06-12 20:55:14.504046
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import shutil
    import tempfile
    tdir = tempfile.mkdtemp()

# Generated at 2022-06-12 20:55:23.333891
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible import context
    import tempfile
    path = tempfile.mkdtemp()
    path1 = tempfile.mkdtemp()
    coll_base = list_valid_collection_paths([path])
    assert path in coll_base
    coll_base = list_valid_collection_paths([path], warn=True)
    assert path in coll_base
    try:
        context.CLIARGS = {'collections_paths': [path1]}
        coll_base = list_valid_collection_paths(None)
        assert path1 in coll_base
        assert path in coll_base
    finally:
        context.CLIARGS = {}

# Generated at 2022-06-12 20:55:35.127697
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp
    from shutil import rmtree
    from ansible.collections import list_valid_collection_paths
    from ansible.module_utils._text import to_bytes

    tmp_path1 = mkdtemp()
    tmp_path2 = mkdtemp()
    tmp_path3 = mkdtemp()
    tmp_path4 = mkdtemp()
    tmp_path5 = mkdtemp()
    tmp_path6 = mkdtemp()
    tmp_path7 = mkdtemp()

    search_paths = [tmp_path1, tmp_path2, tmp_path3]
    path_list = list(list_valid_collection_paths(search_paths))

    assert len(path_list) == 3
    assert to_bytes(tmp_path1) in path_list


# Generated at 2022-06-12 20:55:38.191995
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list_collection_dirs()
    assert list_collection_dirs(coll_filter='ansible.builtin')


# Generated at 2022-06-12 20:55:47.567303
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Tries to find collection paths given relative and absolute directories
    """
    search_paths = [
        'tests/collections/testcollections',
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'collections', 'testcollections')
    ]

    found_directories = list_collection_dirs(search_paths, "namespace1.collection1")

    for path in found_directories:
        assert os.path.exists(path)
        assert os.path.isdir(path)
        assert os.path.basename(path) == "collection1"
        assert os.path.basename(os.path.dirname(path)) == "namespace1"

# Generated at 2022-06-12 20:55:51.356595
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = list(list_valid_collection_paths(search_paths=['/path/that/does/not/exist']))
    assert paths == []

    paths = list(list_valid_collection_paths(search_paths=['/usr']))
    assert paths == []

    paths = list(list_valid_collection_paths(search_paths=['/tmp']))
    assert paths == []

# Generated at 2022-06-12 20:55:58.874428
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # invalid, warning expected
    assert list(list_valid_collection_paths(search_paths=['/fake/path'], warn=True)) == []

    # valid
    MY_DIR = os.path.dirname(os.path.abspath(__file__))
    MY_DIR_PATH = os.path.join(MY_DIR, ".").replace("\\", "/")
    assert list(list_valid_collection_paths(search_paths=[MY_DIR_PATH])) == [MY_DIR_PATH]



# Generated at 2022-06-12 20:56:07.682132
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths()
    """
    # Test when no search path provided
    assert list_valid_collection_paths(warn=True)

    # Test with search_path which does not exist
    search_paths = ['non-existing-path']
    valids = list(list_valid_collection_paths(search_paths))
    assert len(valids) == 0

    # Test with search_path which is file
    with open('/tmp/test_ansible_collection_paths_test.txt', 'w') as f:
        f.write('test')
    search_paths = ['/tmp/test_ansible_collection_paths_test.txt']
    valids = list(list_valid_collection_paths(search_paths))

# Generated at 2022-06-12 20:56:19.378906
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import pathlib
    import tempfile
    import pytest
    from ansible.errors import AnsibleError

    ######################
    TEST_ANSIBLE_COLLECTION_ROOT = pathlib.Path(tempfile.mkdtemp())
    ######################

    TEST_NAMESPACES = ['myns', 'myotherns']
    TEST_COLLECTIONS = ['mycoll', 'myothercoll']

    # create a fake collection structure
    def _mk_coll(nscoll, coll):
        coll_dir = os.path.join(TEST_ANSIBLE_COLLECTION_ROOT, nscoll)
        os.mkdir(coll_dir)
        # create a fake galaxy.yml file, but with only the collection name in it, since
        # we need to know that to construct the path to the collection, but

# Generated at 2022-06-12 20:56:28.710559
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.collections.collection_finder import list_valid_collection_paths

    # Test False for missing or invalid paths
    assert list_valid_collection_paths(['/tmp/not_a_dir/dir_does_not_exist']) == []
    assert list_valid_collection_paths(['/tmp/file_not_dir/']) == []

    # Test True for valid path
    assert list_valid_collection_paths(['/tmp']) == ['/tmp']
    assert list_valid_collection_paths(['/tmp/']) == ['/tmp/']

# Generated at 2022-06-12 20:56:44.385527
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    d1 = "/tmp/does_not_exist"
    d2 = "/etc/"
    d3 = "/bin"
    d4 = "/usr/share/ansible/collections"

    # test bad paths
    assert set(list_valid_collection_paths([d1, d2, d3])) == set()

    # test empty list
    assert set(list_valid_collection_paths([])) == set()

    # test single good path
    assert set(list_valid_collection_paths([d4])) == set([d4])

    # test single bad path
    assert set(list_valid_collection_paths([d1])) == set()

    # test multiple bad paths
    assert set(list_valid_collection_paths([d1, d2])) == set()

    # test good and

# Generated at 2022-06-12 20:56:54.413508
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import random
    import shutil
    import tempfile
    import unittest

    class TestListCollections(unittest.TestCase):

        def setUp(self):
            self.coll_root_path = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.coll_root_path, ignore_errors=True)

        def test_empty_coll_path(self):
            coll_dirs = list(list_collection_dirs([self.coll_root_path]))
            self.assertEquals(len(coll_dirs), 0)

        def test_invalid_coll_dir(self):
            os.makedirs(os.path.join(self.coll_root_path, "ansible_collections/invalid/test"))
            coll_dirs

# Generated at 2022-06-12 20:57:06.032034
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import json
    import sys

    b_tmpd = None

# Generated at 2022-06-12 20:57:15.945777
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # use default config, two paths returned
    valid_paths = list(list_valid_collection_paths(search_paths=None, warn=False))
    assert isinstance(valid_paths, list)
    assert len(valid_paths) >= 2

    # should be able to use relative paths
    x = "tests/resources"
    valid_paths = list(list_valid_collection_paths([x], warn=False))
    assert len(valid_paths) == 1
    assert valid_paths[0] == x

    # invalid path should return empty list
    valid_paths = list(list_valid_collection_paths(["/tmp/does/not/exist"], warn=False))
    assert isinstance(valid_paths, list)
    assert len(valid_paths) == 0

    #

# Generated at 2022-06-12 20:57:27.378339
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils.ansible_release import __version__
    from ansible.collections.ansible.fortios.plugins.module_utils.fortios import __version__ as fortios_ver
    import ansible_collections.ansible.fortios.plugins.module_utils.fortios
    import ansible_collections.ansible.netcommon.plugins.module_utils.network
    import ansible_collections.cisco.ios.plugins.module_utils.network
    import ansible_collections.fortinet.fortios.plugins.module_utils.fortios
    import ansible_collections.netcommon.plugins.module_utils.network

    assert to_bytes(__version__) in ansible_collections.ansible.fortios.plugins.module_utils.fortios.__file__
    assert to_bytes

# Generated at 2022-06-12 20:57:37.083942
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys
    import tempfile
    from shutil import rmtree
    from ansible.utils import context_objects as co

    def _test_list_collection_dirs(search_paths, coll_filter=None, expected_collections=None):
        with tempfile.TemporaryDirectory() as td:

            for path in search_paths:
                if os.path.basename(path) != 'ansible_collections':
                    path = os.path.join(path, 'ansible_collections')

                b_tmp_root = os.path.join(td, to_bytes(path))
                b_coll_root = to_bytes(os.path.join(b_tmp_root, 'ansible_collections'), errors='surrogate_or_strict')


# Generated at 2022-06-12 20:57:47.115866
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test listing valid collection paths.
    """
    # Explicitly create search_paths list object
    search_paths = ["/tmp/foo"]
    # Ensure path exists
    os.makedirs('/tmp/foo')

    # Ensure each path in search_paths is equivalent to the single path returned by
    # list_valid_collection_paths()
    assert search_paths == [path for path in list_valid_collection_paths(search_paths=search_paths)]

    # Ensure search_paths without warn=True doesn't warn
    search_paths = ["/tmp/bar"]
    list_valid_collection_paths(search_paths=search_paths)

    # Ensure search_paths with warn=True does
    search_paths = ["/tmp/bar"]

# Generated at 2022-06-12 20:57:57.592596
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test defaults
    assert list(list_valid_collection_paths(search_paths=None)) == list(AnsibleCollectionConfig.collection_paths)

    # test single valid path
    coll_paths = ['~/.ansible/collections']
    assert list(list_valid_collection_paths(search_paths=coll_paths)) == coll_paths

    # test single invalid path
    coll_paths = ['/invalid']
    assert list(list_valid_collection_paths(search_paths=coll_paths)) == []

    # test multiple paths, 1 valid
    coll_paths = ['/invalid', '~/.ansible/collections']

# Generated at 2022-06-12 20:58:08.170275
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    '''
    Basic test for function list_collection_dirs
    '''
    from ansible.config.manager import ConfigManager
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    import os

    coll_config = AnsibleCollectionConfig()
    coll_config.load()

    # test with no collection_paths defined
    search_paths = None
    coll_filter = None
    collection_dirs = list(list_collection_dirs(search_paths, coll_filter))
    assert len(collection_dirs) == 0

    # test with empty collection_paths defined
    search_paths = []
    coll_filter = None
    collection_dirs = list(list_collection_dirs(search_paths, coll_filter))
    assert len(collection_dirs) == 0

    #

# Generated at 2022-06-12 20:58:13.508773
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    expected = ['/tmp/ansible_collections', '/tmp/ansible_collections2']

    assert list_valid_collection_paths(['/some/path/that/does/not/exist', '/tmp/ansible_collections', '/tmp/ansible_collections2']) == expected

    for path in list_valid_collection_paths():
        path.startswith('/')

# Generated at 2022-06-12 20:58:32.814426
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 2

    # not run if off
    if os.environ.get('ANSIBLE_UNIT_TEST_LIST_COLLECTIONS', None) is None:
        return

    # this test should use its own private tmp dir
    tmpdir = os.environ.get('ANSIBLE_TEST_TMP', None)
    if tmpdir is None:
        raise AssertionError("tmpdir was not set")

    # create a private collection dir with a few namespaces
    colldir = os.path.join(tmpdir, 'ansible_collections')
    os.makedirs(colldir)
    os.makedirs(os.path.join(colldir, 'ns1.coll1'))

# Generated at 2022-06-12 20:58:41.793628
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    b_coll_root = to_bytes(tempfile.mkdtemp())
    b_ns = to_bytes('awesome')
    b_coll = to_bytes('test')

    start_paths = [
        b_coll_root,
        b_coll_root + b'x',
        b'invalid://path/y',
        b_coll_root + b'z/',
        b_coll_root + b'/' + b_ns + b'/' + b_coll,
    ]

    valid_paths = list_valid_collection_paths(start_paths, warn=True)
    assert len(valid_paths) == 1
    assert b_coll_root == valid_paths[0]



# Generated at 2022-06-12 20:58:44.934894
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths([os.path.dirname(__file__) + '/resources/list_valid_collection_paths_1/'])) == ['tests/resources/list_valid_collection_paths_1']

# Generated at 2022-06-12 20:58:56.607851
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    '''
    Test the list_collection_dirs function.
    '''
    assert ['galaxy-local'] == list_collection_dirs(search_paths=[os.path.join(os.path.dirname(__file__), 'fixtures', 'collection_paths')])
    assert ['galaxy-local'] == list_collection_dirs(search_paths=[os.path.join(os.path.dirname(__file__), 'fixtures', 'collection_paths', 'ansible_collections')])
    assert ['galaxy-local'] == list_collection_dirs(search_paths=[os.path.join(os.path.dirname(__file__), 'fixtures', 'collection_paths', 'ansible_collections', 'galaxy-local')])

# Generated at 2022-06-12 20:59:08.776744
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection1 = '/foo/ansible_collections/namespace1/collection1'
    collection2 = '/foo/ansible_collections/namespace1/collection2'
    collection3 = '/bar/ansible_collections/namespace2/collection1'

    for dir in [collection1, collection2, collection3]:
        os.makedirs(dir)

    assert list(list_collection_dirs(search_paths=['/foo'])) == ['namespace1/collection1', 'namespace1/collection2']

    assert list(list_collection_dirs(search_paths=['/foo', '/bar'])) == ['namespace1/collection1', 'namespace1/collection2', 'namespace2/collection1']

# Generated at 2022-06-12 20:59:17.779147
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.common.json import AnsibleJSONEncoder

    import json
    import tempfile
    import shutil

    # test with and without config file
    with tempfile.NamedTemporaryFile(delete=False) as f:
        ansible_cfg_path = f.name

    with tempfile.NamedTemporaryFile(delete=False) as f:
        config_path = f.name

    with tempfile.NamedTemporaryFile(delete=False) as f:
        coll_path = f.name

    with tempfile.NamedTemporaryFile(delete=False) as f:
        coll_path_2 = f.name


# Generated at 2022-06-12 20:59:28.440474
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil

    # test root
    # temp_root = tempfile.mkdtemp()

    # test dir inside
    # temp_1 = tempfile.mkdtemp( dir = temp_root )

    # test subdir inside
    # temp_1_1 = tempfile.mkdtemp( dir = temp_1 )

    # test file inside
    # temp_1_1_1 = tempfile.mkstemp( dir = temp_1_1 )

    # test for trailing /
    # temp_1_1_1_dir = os.path.dirname(temp_1_1_1)

    test_dir = os.path.join(os.path.dirname(__file__), 'data', 'test_list_valid_collection_paths')

# Generated at 2022-06-12 20:59:35.561157
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test the list_collection_dirs function returns the collection directories
    """

    # TODO: fix this - the docker container setup has issues with .tox/ and .cache/
    # this is more of a test for Travis and other CI systems
    # should really be testing with a directory of collections
    search_paths = [os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, 'doc', 'collections'))]
    found = [p for p in list_collection_dirs(search_paths)]

    assert len(found) == 2



# Generated at 2022-06-12 20:59:40.441937
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert len(list(list_collection_dirs(search_paths=["test/unit/utils/fixtures/collection_search_paths"]))) == 2
    assert len(list(list_collection_dirs(search_paths=["test/unit/utils/fixtures/collection_search_paths"],
                                         coll_filter='test_collection_1'))) == 1
    assert len(list(list_collection_dirs(search_paths=["test/unit/utils/fixtures/collection_search_paths"],
                                         coll_filter='test_namespace.test_collection_2'))) == 1

# Generated at 2022-06-12 20:59:43.758019
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths= [ '/tmp/not/a/real/path', '~/.ansible/collections']
    paths = [x for x in list_valid_collection_paths(search_paths, warn=False)]
    assert paths == ['/home/travis/.ansible/collections']

# Generated at 2022-06-12 21:00:12.007042
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import sys
    import tempfile
    import shutil

    b_path = to_bytes(tempfile.mkdtemp())
    with open(os.path.join(b_path, 'ansible.cfg'), 'w') as f:
        f.write('[defaults]\ncollections_path=%s' % b_path)

    paths = [
        tempfile.mkdtemp(),
        tempfile.mkdtemp(),
    ]

    list_p = list(list_valid_collection_paths(search_paths=paths[:]))
    assert len(list_p) == len(paths)

    list_p = list(list_valid_collection_paths(search_paths=[b_path]))
    assert len(list_p) == 1


# Generated at 2022-06-12 21:00:18.187250
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    def _clean_path(path):
        """
        fix path differences between OSes
        """
        if path.startswith('/'):
            return path.replace('/', os.path.sep)
        return path


# Generated at 2022-06-12 21:00:22.826383
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.collections_loader import list_collection_dirs

    for (ns, colls) in iteritems(list_collection_dirs()):
        for coll in colls:
            print("%s.%s" % (ns, coll))

# Generated at 2022-06-12 21:00:32.197567
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.common.text.converters import to_bytes
    test_paths = list()
    test_paths.append(to_bytes(os.path.normpath(os.path.join(to_bytes(os.path.dirname(__file__)), b'..', b'..', b'collections', b'ansible_collections'))))
    test_paths.append(b'foo/bar/baz')
    test_paths.append(b'/foo/bar/baz')
    test_paths.append(b'/tmp/')
    list(list_valid_collection_paths(test_paths))

# Generated at 2022-06-12 21:00:36.480177
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    def mock_get_collection_paths(warn=False):
        return ['/tmp/ansible_collections/']

    coll_dict = {}

    def mock_collection_dict():
        return coll_dict

    # TODO: make a proper mock
    class AnsibleCollectionConfig:
        def __init__(self):
            self.collection_paths = ['/tmp/ansible_collections/']

    def mock__load_collections():
        return

    def mock_list_valid_collection_paths(search_paths, warn=False):
        return search_paths

    # add all the 'mock' methods we just made to the modules we are testing

# Generated at 2022-06-12 21:00:45.162706
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.module_utils._text import to_text
    from ansible.compat.tests import unittest

    class TestListValidCollectionPaths(unittest.TestCase):

        def setUp(self):
            self.test_dir = os.path.join(os.path.dirname(__file__), 'test_collections')

        def _check_path(self, paths, expected):

            expected = [to_text(i) for i in expected]
            result = list(list_valid_collection_paths(search_paths=paths))

            self.assertEqual(len(result), len(expected))
            self.assertListEqual(expected, sorted(result))

        def test_no_paths(self):

            # paths the the root path and one non-existent path
            b_root

# Generated at 2022-06-12 21:00:52.538923
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # include a default and non-existing path
    search_paths = ['/foo/bar', '/tmp/nope']
    # include a path that exists but is not a dir
    with open('/tmp/not_a_dir', 'a'):
        os.utime('/tmp/not_a_dir', None)

    assert list(set(list_valid_collection_paths(search_paths))) == set(['/tmp'])

    # include a path that exists and is a dir
    os.mkdir('/tmp/collection')

    assert list(set(list_valid_collection_paths(search_paths))) == set(['/tmp', '/tmp/collection'])

# Generated at 2022-06-12 21:00:59.336653
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    search_paths = [
        '/usr/share/ansible/collections']

    coll_paths = list(list_collection_dirs(search_paths))
    assert len(coll_paths) > 1

    coll_paths = list(list_collection_dirs(search_paths, 'ansible_collections.foo.bar'))
    assert len(coll_paths) == 1
    assert is_collection_path(coll_paths[0])

# Generated at 2022-06-12 21:01:00.350396
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # validate that list_collection_dirs returns paths
    paths = list(list_collection_dirs())
    assert paths is not None

# Generated at 2022-06-12 21:01:09.971348
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    import tempfile
    tempdirs = []
    search_paths = []


# Generated at 2022-06-12 21:01:36.664005
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import pytest
    import os


# Generated at 2022-06-12 21:01:39.875377
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dirs = list(list_collection_dirs(['/usr/share'], 'ansible_collections.testcoll'))

    assert len(dirs) == 1
    assert '/usr/share/ansible_collections/ansible_collections/testcoll' in dirs

# Generated at 2022-06-12 21:01:46.128174
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test filter of non existing or invalid search_paths for collections
    """
    # No search_paths, load default config
    search_paths = list_valid_collection_paths()
    assert search_paths is not None
    assert len(list(search_paths)) == 1

    # Check non existing search_paths
    search_paths = [u"/tmp/somewhichdoesnotexist"]
    search_paths = list_valid_collection_paths(search_paths)
    assert search_paths is not None
    assert len(list(search_paths)) == 0

    # Check valid directory as search_paths
    search_paths = ["/tmp"]
    search_paths = list_valid_collection_paths(search_paths)

# Generated at 2022-06-12 21:01:57.582895
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from os.path import expanduser, expandvars
    import shutil
    import tempfile
    import unittest


# Generated at 2022-06-12 21:02:06.843179
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    ''' test_list_collection_dirs()
    '''

    search_paths = [os.path.join(os.path.dirname(__file__), '../test/units/module_utils/ansible_collections'),
                    os.path.join(os.path.dirname(__file__), '../test/integration/test_collections'),
                    os.path.join(os.path.dirname(__file__), '../test/units/module_utils/test_plugins'),
                    os.path.join(os.path.dirname(__file__), '../test/units/plugins')]


# Generated at 2022-06-12 21:02:17.072009
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    test_path = tempfile.mkdtemp()
    # Create a test path that is a file
    file_path = tempfile.mkstemp()[1]
    paths = [test_path, file_path]

    # Paths should contain test_path and file_path
    assert(len(list(list_valid_collection_paths(search_paths=paths))) == 1)
    assert(len(list(list_valid_collection_paths(search_paths=paths, warn=True))) == 1)

    # Paths should only contain the test_path
    assert(len(list(list_valid_collection_paths(search_paths=paths, warn=False))) == 1)

# Generated at 2022-06-12 21:02:24.064018
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = [os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'integration', 'targets', 'collections')]
    dirs = list(list_collection_dirs(search_paths=paths, coll_filter="mycoll.myplugin"))
    assert dirs == [b'/home/huitseeker/ansible/test/integration/targets/collections/ansible_collections/mycoll/myplugin']

# Generated at 2022-06-12 21:02:28.869369
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert not list_valid_collection_paths(search_paths=["/not/exists"])

    assert list_valid_collection_paths(search_paths=["/usr/bin"])

    assert list_valid_collection_paths(search_paths=["/etc/ansible/ansible.cfg"])

# Generated at 2022-06-12 21:02:41.427544
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_root = '/tmp/coll_root'
    os.makedirs(os.path.join(coll_root, 'ansible_collections/test/testcoll'))
    os.makedirs(os.path.join(coll_root, 'ansible_collections/test/plugins'))
    os.makedirs(os.path.join(coll_root, 'ansible_collections/test2/testcoll'))
    os.makedirs(os.path.join(coll_root, 'ansible_collections/test2/testcoll2'))
    os.makedirs(os.path.join(coll_root, 'ansible_collections/test2/plugins'))

# Generated at 2022-06-12 21:02:46.908474
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Paths that do not exist
    paths = ['/testpath/does/not/exist',
             '/testpath/does/not/exist2',
             '/testpath/does/not/exist3']
    valid_paths = list_valid_collection_paths(search_paths=paths)
    assert not valid_paths

    # Paths that are not directories
    paths = ['/etc/hosts', '/etc/passwd', '/etc/group']
    valid_paths = list_valid_collection_paths(search_paths=paths)
    assert not valid_paths

    # Some paths that exist and are dirs
    paths = ['/usr', '/usr/bin', '/etc/ansible']
    valid_paths = list_valid_collection_paths(search_paths=paths)


# Generated at 2022-06-12 21:03:21.360307
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from .collection_loader import _get_collection_paths
    from .collection_loader import _get_collection_metadata

    # we only want to test that the function yields valid collection paths
    for collection_path in list_collection_dirs(_get_collection_paths()):
        (namespace, collection, version) = _get_collection_metadata(collection_path)
        assert namespace is not None
        assert collection is not None
        assert version is not None

# Generated at 2022-06-12 21:03:31.347495
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os

    # create collection ns1.coll1 in temporary filesystem
    temp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_dir, 'ansible_collections'))
    os.mkdir(os.path.join(temp_dir, 'ansible_collections', 'ns1'))
    os.mkdir(os.path.join(temp_dir, 'ansible_collections', 'ns1', 'coll1'))
    os.mkdir(os.path.join(temp_dir, 'ansible_collections', 'ns1', 'coll1', 'plugins'))