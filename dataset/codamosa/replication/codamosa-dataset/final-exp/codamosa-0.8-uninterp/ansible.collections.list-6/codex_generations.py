

# Generated at 2022-06-12 20:53:43.063523
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils._text import to_text

    def mpath(*parts):
        return to_text(os.path.join(*map(to_bytes, parts)))

    import tempfile
    test_dir = tempfile.mkdtemp()
    test_paths = [
        mpath(test_dir, 'not_a_dir'),
        mpath(test_dir, 'dir'),
        mpath(test_dir, 'not_a_dir_either'),
    ]

    os.makedirs(test_paths[1])
    os.makedirs(test_paths[2])

    # Test that we can pass in a list of collection paths and get
    # the valid path back out
    valid_paths = list(list_valid_collection_paths(test_paths))


# Generated at 2022-06-12 20:53:51.654372
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Test the return of collection directories
    :return: None
    """

    import tempfile
    import shutil

    # create a temp directory
    tmpdir = tempfile.mkdtemp()

    # create a subdirectory with a collection
    collection = 'mycoll'
    collection_dir = os.path.join(tmpdir, 'ansible_collections', 'my_namespace', collection)
    os.makedirs(collection_dir)
    os.makedirs(os.path.join(collection_dir, 'plugins'))
    os.makedirs(os.path.join(collection_dir, 'plugins', 'modules'))
    os.makedirs(os.path.join(collection_dir, 'plugins', 'action_plugins'))

# Generated at 2022-06-12 20:53:55.347631
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dirs = list(list_collection_dirs(search_paths=["test/units/fixtures/collection_loader/search_paths"], coll_filter="mynamespace.mycollection1"))
    assert dirs[0] == b"/for/realz/mynamespace/mycollection1"

# Generated at 2022-06-12 20:54:07.433176
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import random
    import string


    col_path = 'ansible_collections'
    paths = []

    with tempfile.TemporaryDirectory() as td:
        for i in range(20):
            path = os.path.join(td, ''.join(random.choice(string.ascii_lowercase) for _ in range(10)))
            paths.append(path)
            os.mkdir(path)

        # Add real collections path to list
        if os.path.exists(col_path) and os.path.isdir(col_path):
            paths.append(col_path)

        # Create some fake collections dirs and a few real ones

# Generated at 2022-06-12 20:54:07.769638
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    pass

# Generated at 2022-06-12 20:54:19.711697
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import mkdtemp
    from shutil import rmtree

    def make_tree(base, path_parts, coll_filter=None):
        os.makedirs(os.path.join(base, *path_parts))

    def test_coll_dirs(base, exp_dirs, coll_filter=None, search_paths=None):
        dirs = list(list_collection_dirs(search_paths=search_paths, coll_filter=coll_filter))
        assert sorted(dirs) == sorted([os.path.join(base, *x) for x in exp_dirs])

    tmp_dir = mkdtemp()

# Generated at 2022-06-12 20:54:30.543025
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths()) == ['/usr/share/ansible/collections',
                                                   '/etc/ansible/collections']

    assert list(list_valid_collection_paths(['/etc/ansible/collections'])) == \
           ['/etc/ansible/collections']

    assert list(list_valid_collection_paths(['/etc/ansible/collections',
                                             '/not/real/path'])) == \
           ['/etc/ansible/collections']

    assert list(list_valid_collection_paths(['/etc/ansible/collections',
                                             '/not/real/path',
                                             '/another/fake/path'],
                                            warn=True)) == \
           ['/etc/ansible/collections']

   

# Generated at 2022-06-12 20:54:35.013026
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.testns.testcoll import plugins

    display.verbosity = 4
    assert '/any/path/does/not/exist' in list_valid_collection_paths(['/any/path/does/not/exist'])
    assert '/etc/ansible' not in list_valid_collection_paths(['/etc/ansible'])
    assert os.path.dirname(plugins.__file__) in list_valid_collection_paths()

# Generated at 2022-06-12 20:54:46.332027
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # None case, should return default
    assert list_valid_collection_paths() == AnsibleCollectionConfig.collection_paths, \
        "List Valid Collection Paths returned incorrect paths with no arguments"

    # empty list test
    assert list_valid_collection_paths([]) == AnsibleCollectionConfig.collection_paths, \
        "List Valid Collections returned incorrect paths with an empty list"

    # Single item list test
    assert list_valid_collection_paths(['tests/data/collections/ns1.coll1/']) == ['tests/data/collections/ns1.coll1/'], \
        "List Valid Collections returned incorrect path with a single-item list"

    # Multiple item list test, should return all items in the list

# Generated at 2022-06-12 20:54:47.399193
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_root = list_collection_dirs()
    for coll in collection_root:
        print(coll)
#test_list_collection_dirs()

# Generated at 2022-06-12 20:55:04.056959
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    from ansible.collections.ansible.plugins.action.builtin import BuiltinActionModule
    from ansible.collections.ansible.plugins.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 20:55:13.187025
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.collections.config import get_default_collection_paths
    search_paths = [
        '/bad/path/is/bad',
        '/bad/path/is/bad/but/exists',
        '/bad/path/is/bad/but/exists/ansible_collections',
        '/etc/ansible/collections',
        '/etc/ansible/ansible_collections',
    ]
    default_paths = get_default_collection_paths()
    # add default paths
    search_paths.extend(default_paths)
    result = list(list_valid_collection_paths(search_paths, warn=False))
    assert default_paths == result


# Generated at 2022-06-12 20:55:24.318462
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    tmpdir2 = os.path.join(tmpdir, 'tmp2')
    tmpdir3 = os.path.join(tmpdir, 'tmp3')
    tmpdir4 = os.path.join(tmpdir, 'tmp4')
    tmpdir5 = os.path.join(tmpdir, 'tmp5')
    b_tmpdir2 = to_bytes(tmpdir2)
    b_tmpdir3 = to_bytes(tmpdir3)
    b_tmpdir4 = to_bytes(tmpdir4)
    b_tmpdir5 = to_bytes(tmpdir5)
    os.mkdir(b_tmpdir2)
    os.mkdir(b_tmpdir3)

# Generated at 2022-06-12 20:55:35.821247
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves import builtins
    from ansible_collections.ansible.builtin.plugins.module_utils.basic import AnsibleModule
    import ansible.utils.collection_loader

    # Use the basic module_utils; it doesn't depend on anything
    module = AnsibleModule(argument_spec={})

    # Make sure we are in a good state to start
    collection_paths = [path for path in ansible.utils.collection_loader.list_valid_collection_paths()]
    assert collection_paths == AnsibleCollectionConfig.collection_paths

    # Test that we can add a valid collection path
    path = os.path.join(os.path.dirname(builtins.__file__), 'ansible_collections')

# Generated at 2022-06-12 20:55:45.252385
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Create a mock file system
    env = {}
    def fs(path):
        return path in env
    def mkdir(path):
        env[path] = True
    def rmdir(path):
        try:
            del env[path]
        except KeyError:
            pass

    # Test for empty collection paths
    assert list(list_valid_collection_paths([], warn=True)) == []

    # Test for non existent collection paths
    assert list(list_valid_collection_paths(['/foo/bar'], warn=True)) == []

    # Test for non directory collection paths
    mkdir('/tmp')
    env['/tmp/somefile'] = True
    assert list(list_valid_collection_paths(['/tmp/somefile'], warn=True)) == []

# Generated at 2022-06-12 20:55:53.222264
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Create fake search paths and collections
    fake_path = '/tmp/fake_collections'
    os.mkdir(fake_path)
    fake_ns_dir = os.path.join(fake_path, 'ns1')
    os.mkdir(fake_ns_dir)
    fake_coll_dir = os.path.join(fake_ns_dir, 'coll1')
    os.mkdir(fake_coll_dir)

    # List all collections
    coll_dirs = list_collection_dirs([fake_path])
    for coll in coll_dirs:
        assert os.path.exists(coll)

    # List a specific collection
    coll_dirs = list_collection_dirs([fake_path], 'ns1.coll1')
    for coll in coll_dirs:
        assert os.path

# Generated at 2022-06-12 20:55:59.897716
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader._collection_finder import list_valid_collection_paths

    # check that the function returns a generator
    assert hasattr(list_valid_collection_paths(), '__iter__')
    # check that the function returns AnsibleCollectionConfig.collection_paths
    # as the first element
    assert isinstance(list_valid_collection_paths(warn=False).next(), str)


# Generated at 2022-06-12 20:56:08.318986
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    non_existent = '/tmp/does_not_exist'
    existent = '/etc/ansible'
    exists_not_dir = '/etc/passwd'
    good = '/path/to/collection'

    # NOTE: If running this test as root, correct path may be /etc/sudoers, not /etc/passwd
    if not os.path.isfile(existent):
        existent = os.path.dirname(existent)

    # real directory that exists, should return same
    assert list(list_valid_collection_paths([existent, non_existent])) == [existent]

    # real file that exists, should not return
    assert list(list_valid_collection_paths([existent, exists_not_dir])) == [existent]

    # non-existent file, should not be returned

# Generated at 2022-06-12 20:56:20.183669
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    mysearch_paths = [
        '/tmp/path1',
        '/tmp/path2',
        '/tmp/path3',
    ]

    for i, item in enumerate(mysearch_paths):
        os.makedirs(item)

    for i, item in enumerate(list_collection_dirs(search_paths=mysearch_paths)):
        assert item == None

    # Test Search Paths
    # /tmp/path1
    #     /ansible_collections
    #         /namespace1
    #             /collection1
    #         /namespace2
    #             /collection2
    # /tmp/path2
    #     /ansible_collections
    #         /namespace3
    #             /collection3
    # /tmp/path3
    #     /ansible

# Generated at 2022-06-12 20:56:22.316657
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # TODO: find a way to unit test this

    pass

# Generated at 2022-06-12 20:56:43.273283
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_dir = os.path.join(os.path.dirname(__file__), 'unit_tests', 'collections')
    list_coll_dirs = list(list_collection_dirs([coll_dir]))
    assert len(list_coll_dirs) == 5
    assert os.path.join(coll_dir, 'ansible_collections', 'ns1', 'coll1') in list_coll_dirs
    assert os.path.join(coll_dir, 'ansible_collections', 'ns1', 'coll2') in list_coll_dirs
    assert os.path.join(coll_dir, 'ansible_collections', 'ns1', 'coll3') in list_coll_dirs

# Generated at 2022-06-12 20:56:49.882995
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ansible_release
    import ansible.utils.path

    paths = ansible.module_utils.ansible_release._find_collection_paths()

    dirs = list_valid_collection_paths(paths)
    assert len(dirs) > 0
    assert ansible.utils.path.accelerate_module_cache_dir() in dirs

# Generated at 2022-06-12 20:56:55.162445
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Check function list_collection_dirs

    This can only be tested using existing collections.
    :return: None
    """
    # pylint: disable=unused-variable

    coll_dir = list(list_collection_dirs())
    assert isinstance(coll_dir, list)

    assert len(coll_dir) > 0
    for mypath in coll_dir:
        assert os.path.exists(mypath)
        assert os.path.isdir(mypath)

# Generated at 2022-06-12 20:57:06.199639
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    collect_dirs = list(list_collection_dirs(search_paths=['/tmp/collections']))
    assert collect_dirs == []

    collect_dirs = list(list_collection_dirs(search_paths=[os.path.dirname(__file__)]))
    assert len(collect_dirs) > 0
    for cdir in collect_dirs:
        assert os.path.exists(cdir)
        assert os.path.isdir(cdir)

    # filter by collection only
    collect_dirs = list(list_collection_dirs(search_paths=[os.path.dirname(__file__)], coll_filter='mycoll'))
    assert len(collect_dirs) == 1
    for cdir in collect_dirs:
        assert os.path.exists

# Generated at 2022-06-12 20:57:13.960998
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Make sure that the list of paths being passed through list_valid_collection_paths is
    being filtered correctly.
    """
    from tempfile import mkdtemp
    from shutil import rmtree

    import os

    path1 = os.path.realpath(os.path.join(mkdtemp(), 'ansible_collections'))
    path2 = os.path.realpath(os.path.join(mkdtemp(), 'ansible_collections'))

    assert os.path.exists(path1) and os.path.isdir(path1)
    assert os.path.exists(path2) and os.path.isdir(path2)

    res1 = list_valid_collection_paths([path1, path2])
    assert list(res1) == [path1, path2]



# Generated at 2022-06-12 20:57:20.771756
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    ansible_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ansible')
    list_collection_dirs([ansible_path])
    list_collection_dirs([ansible_path], 'ansible.builtin')
    list_collection_dirs([ansible_path], 'ansible.builtin.test')

# Generated at 2022-06-12 20:57:31.604566
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from ansible.module_utils.common.files import mk_boolean

    # Setup paths we expect
    EXPECTED_COLLECTION_PATHS = [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))]

    # Validate expected paths
    assert list(list_valid_collection_paths()) == EXPECTED_COLLECTION_PATHS, 'incorrect path returned'

    # Validate passing the paths we expect return the exact same paths
    assert list(list_valid_collection_paths(EXPECTED_COLLECTION_PATHS)) == EXPECTED_COLLECTION_PATHS, 'expected paths and passed paths should be the same'

    # Create a temp directory to test
    temp_directory

# Generated at 2022-06-12 20:57:39.349201
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import random
    import string
    import os

    # pass in a temp dir for our test colls
    test_coll_dir = os.path.join(os.path.dirname(__file__), 'test_collections')

    # create a random collection name and load it into our test dir
    rnd_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    test_coll = '%s.%s' % ('ansible_collections', rnd_name)
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = test_coll_dir
    os.system('ansible-galaxy collection init %s' % test_coll)

    # verify we can load collection from a dir not in $ANSIBLE_COLLECTIONS_

# Generated at 2022-06-12 20:57:46.348802
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    pathlist = list(list_valid_collection_paths([]))
    expected_pathlist = [os.path.join(os.path.expanduser('~'),
                                      'ansible_collections')]
    assert pathlist == expected_pathlist

    pathlist = list(list_valid_collection_paths(['/some/collection/path', '/non-existent/path']))
    expected_pathlist = ['/some/collection/path']
    assert pathlist == expected_pathlist



# Generated at 2022-06-12 20:57:56.856281
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """Test the list_valid_collection_paths function."""

    search_paths = []
    search_paths.append('/tmp')
    search_paths.append('/tmp/does_not_exist')
    search_paths.append('/tmp/ansible_collections')
    search_paths.append('/tmp/ansible_collections/test')
    search_paths.append('/tmp/ansible_collections/test/test')
    search_paths.append('/tmp/ansible_collections/test/test/test')

    # should return only existing directories
    assert list(list_valid_collection_paths(search_paths)) == ['/tmp', '/tmp/ansible_collections']

    # should return single path for Ansible Collection

# Generated at 2022-06-12 20:58:29.451885
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test 1 - use default search path, check that we find all installed collections

    # first get a list of all the installed collections
    expected = [x for x in list_valid_collection_paths()]

    # now get a list of all installed collections
    # we expect this list to be a superset of the collection search path list
    # check we find all valid
    found_colls = list(list_collection_dirs())

    assert len(found_colls) > len(expected)

    # iterate through all found collections
    for coll_dir in found_colls:
        # check it is installed
        assert os.path.exists(coll_dir)

    # Test 2 - ensure that a specific collection can be found in any search path
    # We know google.cloud is installed as we tested that in the previous test
    found_coll

# Generated at 2022-06-12 20:58:39.989550
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.utils.path import get_distribution_path
    from ansible.module_utils.six import PY3

    collections_paths = [get_distribution_path(runtime_data_context=dict(collection_paths=[]))]
    collection = 'ansible_collections.test.test_collection'
    coll_paths = list_collection_dirs(search_paths=collections_paths, coll_filter=collection)

    if PY3:
        expected = [b'/usr/share/ansible_collections/ansible_collections/test/test_collection']
    else:
        expected = [b'/usr/share/ansible_collections/test/test_collection']

    assert list(coll_paths) == expected

# Generated at 2022-06-12 20:58:48.550062
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    mycoll = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'integration', 'targets', 'collections')
    assert list_collection_dirs(search_paths=[mycoll, ], coll_filter="redhat.molecule") == [os.path.join(mycoll, "redhat/molecule")]
    assert list_collection_dirs(search_paths=[mycoll, ], coll_filter="redhat") == [os.path.join(mycoll, "redhat/molecule")]
    assert list_collection_dirs(search_paths=[mycoll, ], coll_filter="redhat.something") == [os.path.join(mycoll, "redhat/molecule")]
    assert list_collection_dir

# Generated at 2022-06-12 20:58:58.036343
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    tmpdir = tempfile.mkdtemp(prefix='ansible_test_collections_')
    display.vvv("Temporary Collection Directory: {0}".format(tmpdir))

    # valid collections
    collection1 = os.path.join(
        tmpdir,
        'ansible_collections',
        'mynamespace',
        'mycollection1',
    )
    os.makedirs(collection1)

    collection2 = os.path.join(
        tmpdir,
        'ansible_collections',
        'mynamespace',
        'mycollection2',
    )
    os.makedirs(collection2)


# Generated at 2022-06-12 20:59:03.845125
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ["~/mypath/ansible_collections", "~/.ansible/collections", "/usr/share/ansible/collections"]
    valid_search_paths = list(list_valid_collection_paths(search_paths))

    for path in valid_search_paths:
        assert path.endswith('collections')

# Generated at 2022-06-12 20:59:14.604744
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = [u'./tests/data/bogus_collection_path', u'./tests/data/ansible_collections/awesome_ns1']
    coll_filter = None
    colls = list(list_collection_dirs(search_paths, coll_filter))
    assert len(colls) == 1
    assert u'awesome_collection' in os.path.basename(colls[0])

    coll_filter = u'awesome_ns1.awesome_collection'
    colls = list(list_collection_dirs(search_paths, coll_filter))
    assert len(colls) == 1
    assert u'awesome_collection' in os.path.basename(colls[0])

    coll_filter = u'awesome_ns1.'
    colls = list

# Generated at 2022-06-12 20:59:24.843374
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''Test list_valid_collection_paths'''

    import tempfile

    nb_test_paths = 10
    test_paths = []
    # create temporary directories
    for _ in range(nb_test_paths):
        test_paths.append(tempfile.mkdtemp())

    # add a non-directory path
    with tempfile.NamedTemporaryFile() as test_file:
        test_paths.append(test_file.name)

    # add a non-existing paths
    test_paths.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'INVALID_PATH'))

    # add a duplicate
    test_paths.append(test_paths[0])

    # remove one of the directories
    test_

# Generated at 2022-06-12 20:59:27.615281
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Should not raise an error
    list(list_collection_dirs(coll_filter='foo.bar'))

# Generated at 2022-06-12 20:59:36.589209
# Unit test for function list_collection_dirs

# Generated at 2022-06-12 20:59:44.259192
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    tmp_dir = to_bytes(tempfile.gettempdir())

    # valid collection for test
    test_good_collections_dir = os.path.join(tmp_dir, b'test_good_collections')
    os.makedirs(test_good_collections_dir)
    test_good_collection_dir = os.path.join(test_good_collections_dir, b'test', b'good_collection')
    os.makedirs(test_good_collection_dir)
    open(os.path.join(test_good_collection_dir, b'MANIFEST.json'), 'w').close()

    # valid collection for test, but no manifest

# Generated at 2022-06-12 21:00:35.274111
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():  # pylint: disable=W0212
    current_dir = os.getcwd()

    # Create directory (if not exists) for unit test
    if not os.path.exists('./test_list_valid_collection_paths'):
        os.makedirs('./test_list_valid_collection_paths')

    os.chdir('./test_list_valid_collection_paths')

    if not os.path.exists('./test_list_valid_collection_paths_dummy_file'):
        with open('./test_list_valid_collection_paths_dummy_file', 'a'):
            os.utime('./test_list_valid_collection_paths_dummy_file', None)

    # Test when search_paths param is not set


# Generated at 2022-06-12 21:00:38.268071
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    display.deprecated("function list_valid_collection_paths")

# Generated at 2022-06-12 21:00:42.221948
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert len(list(list_valid_collection_paths())) > 0
    assert len(list(list_valid_collection_paths(search_paths=[]))) > 0
    assert len(list(list_valid_collection_paths(search_paths=[os.path.join(os.getcwd(), 'testlib')]))) == 1

# Generated at 2022-06-12 21:00:52.350551
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    bases = ["/usr/share/ansible", "/non/existent", "~/ansible"]

    # Start with an empty config, test that defaults are returned
    paths = []
    results = list_valid_collection_paths(paths)
    assert len(list(results)) == len(AnsibleCollectionConfig.collection_paths)

    # Remove duplicates, test that there is one for each provided path
    paths = list(set(bases))
    results = list_valid_collection_paths(paths)
    assert len(list(results)) == len(paths)
    for p in results:
        assert p in paths

    # Add some path back in and test that the same number is returned
    paths = list(set(bases)) + bases
    results = list_valid_collection_paths(paths)
   

# Generated at 2022-06-12 21:01:04.021334
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    search_path = [os.path.dirname(os.path.abspath(__file__)) + '/test_collections/collection_list_dirs']

    collection_paths = list_collection_dirs(search_path)

# Generated at 2022-06-12 21:01:12.501391
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    from ansible.utils.path import makedirs_safe

    test_ns = 'test_namespace'
    test_coll = 'test_collection'
    t_path = tempfile.mkdtemp()

    # test listing collections with no collections present
    assert not list(list_collection_dirs([t_path]))

    # test listing all collections
    test_coll_path = os.path.join(t_path, test_ns, test_coll)
    makedirs_safe(test_coll_path)
    assert list(list_collection_dirs([t_path])) == [test_coll_path]

    # test listing specific collection
    test_coll2 = 'test_collection2'

# Generated at 2022-06-12 21:01:21.829416
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test to check the list_collection_dirs function.
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(dir_path, '../../test/ansible_collections/test_collections/')
    collection_paths = [dir_path]
    coll_filter = "test_collections.test"
    collection_dirs = list_collection_dirs(collection_paths, coll_filter)

    for collection_dir in collection_dirs:
        assert collection_dir == b"../../test/ansible_collections/test_collections/test_collections/test/test"

# Generated at 2022-06-12 21:01:31.220289
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    #
    # Test search paths
    #

    # Get default config from class
    test_search_paths = AnsibleCollectionConfig.collection_paths[:]

    # Get valid search paths for list_collection_dirs()
    test_search_paths = list(list_valid_collection_paths(test_search_paths))

    # Create fake search paths
    test_search_paths.append('/invalid/path')
    test_search_paths.append('/another/invalid/path')

    # Filter out invalid search paths
    test_search_paths = list(list_valid_collection_paths(test_search_paths, warn=True))

    # There should be no invalid search paths
    assert ['/invalid/path', '/another/invalid/path'] != test_search_paths



# Generated at 2022-06-12 21:01:37.298271
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Display function is mocked out to not use Display.display on test call
    # the results of the function call are the only thing compared in testing
    # this function.
    display.display = lambda x, y: x
    mycoll = list(list_collection_dirs(coll_filter='t_ansible_collections.my_collection'))
    assert mycoll == [b'/tmp/my_collections/ansible_collections/t_ansible_collections/my_collection']

# Generated at 2022-06-12 21:01:43.148609
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    '''
    Return paths for the specific collections found in passed or configured search paths
    :param search_paths: list of text-string paths, if none load default config
    :param coll_filter: limit collections to just the specific namespace or collection, if None all are returned
    :return: list of collection directory paths
    '''
    
    # Test case1: search_paths = None
    assert list_collection_dirs() == []

    # Test case2: coll_filter = 'ns.collection'
    assert list_collection_dirs(coll_filter='namspace.collection') == []
    


# Generated at 2022-06-12 21:03:16.202786
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys
    import ansible_collections
    import ansible_collections.test.test_files
    import tempfile
    import shutil
    import importlib
    import os

    def _create_test_collections():
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()

        # Create ansible collection directory
        b_coll_dir = os.path.join(temp_dir, to_bytes('ansible_collections'))
        os.makedirs(b_coll_dir)

        # Create test collections
        b_namespace_dir = os.path.join(b_coll_dir, to_bytes('my_namespace'))
        os.makedirs(b_namespace_dir)


# Generated at 2022-06-12 21:03:23.972117
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    b_tmp_collection1 = to_bytes('@test_tmp_coll1')
    b_tmp_collection2 = to_bytes('@test_tmp_coll2')
    b_tmp_collection3 = to_bytes('@test_tmp_coll3')
    b_tmp_collection4 = to_bytes('@test_tmp_coll4')

    path_list = [b_tmp_collection1, b_tmp_collection2, b_tmp_collection3, b_tmp_collection4]
