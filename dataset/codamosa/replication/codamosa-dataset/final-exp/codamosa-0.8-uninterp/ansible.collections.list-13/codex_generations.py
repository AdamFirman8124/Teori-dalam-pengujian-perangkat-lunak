

# Generated at 2022-06-12 20:53:38.764035
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    paths = list_collection_dirs(search_paths=['.', '/tmp'], coll_filter=None)
    assert len(paths) > 0

    paths = list_collection_dirs(search_paths=['./test/unit/ansible_collections'], coll_filter='test.no_metadata')
    assert len(paths) > 0

    paths = list_collection_dirs(search_paths=['./test/unit/ansible_collections'], coll_filter='test')
    assert len(paths) == 2

# Generated at 2022-06-12 20:53:48.423367
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    test_coll = tempfile.TemporaryDirectory()
    test_coll_path = os.path.join(test_coll.name, 'test_coll.test')
    test_coll_path_parent = os.path.join(test_coll.name, 'test_coll.test', 'test')
    test_ns = tempfile.TemporaryDirectory()
    test_ns_path = os.path.join(test_ns.name, 'test_ns.test')
    test_ns_path_parent = os.path.join(test_ns.name, 'test_ns.test', 'test')

    os.makedirs(os.path.join(test_coll.name, 'test_coll.test', 'plugins', 'modules'))

# Generated at 2022-06-12 20:53:55.577965
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_paths = ["/etc/ansible/collection", "/usr/share/ansible/collections"]
    ansible_collections = list_collection_dirs(coll_paths, 'ansible.builtin')
    sub_coll_paths = list(filter(lambda x: ('ansible_collections/ansible/ansible' in x) or ('ansible_collections/ansible.builtin' in x), list(ansible_collections)))
    assert len(ansible_collections) > 1
    assert len(sub_coll_paths) == 2
    #assert sub_coll_paths[0].endswith('ansible_collections/ansible/ansible_builtin') or sub_coll_paths[1].endswith('ansible_collections/ansible/ansible_builtin')



# Generated at 2022-06-12 20:54:07.714462
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection = None
    namespace = None
    search_paths = ["/home/chandrashekar/ansible_collections/"]
    coll_filter = 'pkumar.trial'
    if coll_filter is not None:
        if '.' in coll_filter:
            try:
                (namespace, collection) = coll_filter.split('.')
                print("namespace: ", namespace)
                print("collection: ", collection)
            except ValueError:
                raise AnsibleError("Invalid collection pattern supplied: %s" % coll_filter)
        else:
            namespace = coll_filter

    collections = defaultdict(dict)

# Generated at 2022-06-12 20:54:19.606998
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import list_valid_collection_paths
    from ansible.collections.ansible.builtin import test_valid_collection_paths_data

    # Check all valid paths are recognized as valid
    for val in test_valid_collection_paths_data['valid']:
        try:
            found = list(list_valid_collection_paths([val]))
        except ValueError:
            raise AssertionError("Valid path '{0}' raised an error:{1}".format((val), ValueError))
        else:
            assert found

    # Check value error is thrown on invalid paths

# Generated at 2022-06-12 20:54:30.226743
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test no search_paths
    search_paths = None
    result = list(list_valid_collection_paths(search_paths))
    assert 'home/username/.ansible/collections' in result

    # Test with default search_paths
    search_paths = ['/home/username/.ansible/collections']
    new_paths = ['/etc/ansible/collections']
    result = list(list_valid_collection_paths(search_paths))
    assert '/home/username/.ansible/collections' in result
    assert new_paths[0] not in result
    result = list(list_valid_collection_paths(new_paths))
    assert '/home/username/.ansible/collections' not in result
    assert new_paths[0] in result

    #

# Generated at 2022-06-12 20:54:35.794428
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test list of paths with missing, existing dir, and file
    search_paths = [
        '/does/not/exist',
        'docs/examples',
        'lib/ansible/config/base.yml',
    ]

    # Expect existing path and warn for missing/file
    assert list(list_valid_collection_paths(search_paths, warn=True)) == [
        'docs/examples'
    ]

    # Expect no warnings
    assert list(list_valid_collection_paths(search_paths, warn=False)) == [
        'docs/examples'
    ]

# Generated at 2022-06-12 20:54:46.850485
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # no path and no config
    x = list(list_valid_collection_paths([]))
    assert len(x) == 0

    # not found in default
    x = list(list_valid_collection_paths(["/tmp"]))
    assert len(x) == 0

    # found in default and user override
    x = list(list_valid_collection_paths(["/etc/ansible", "/tmp"]))
    assert len(x) == 1, x

    # found in default and user override
    x = list(list_valid_collection_paths(["/etc/ansible", "/usr/share/ansible"]))

    assert len(x) == 2
    assert "/etc/ansible" in x
    assert "/usr/share/ansible" in x



# Generated at 2022-06-12 20:54:54.399166
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader import list_collection_dirs

    search_paths = [
        "/path/that/does/not/exist",
        "/some/file/that/is/not/a/dir",
    ]

    # collection_dirs will be empty
    collection_dirs = list(list_collection_dirs(search_paths))
    assert len(collection_dirs) == 0

    # Test with existing search paths

    search_paths = [
        "/etc/ansible/collections",
        "/usr/share/ansible/collections",
    ]

    # collection_dirs will be empty
    collection_dirs = list(list_collection_dirs(search_paths))

# Generated at 2022-06-12 20:55:03.200006
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    old_val = AnsibleCollectionConfig.collection_paths
    AnsibleCollectionConfig.collection_paths = []

    # Test with no collection filter, which returns all collections
    paths = list(list_collection_dirs())

    for path in old_val:
        if not os.path.exists(path):
            # This can happen during a development run of the collection unit tests
            print('Skipping non-existent path %s' % path)
            continue
        if not os.path.isdir(path):
            print('Skipping non-directory path %s' % path)
            continue
        path = os.path.join(path, 'ansible_collections')
        if os.path.exists(path) and os.path.isdir(path):
            paths.append(path)


# Generated at 2022-06-12 20:55:15.663541
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths()) == []
    assert list(list_valid_collection_paths(search_paths=[b"/etc/ansible/foo"])) == [b"/etc/ansible/foo"]

    # /etc does not exist, so no collections are yielded
    assert list(list_valid_collection_paths(search_paths=[b"/etc"])) == []

    # Both paths exist, but one is a file and not a directory
    assert list(list_valid_collection_paths(search_paths=[b"/etc", b"/etc/ansible"])) == [b"/etc"]

# Generated at 2022-06-12 20:55:20.953047
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import ansible
    coll_path = os.path.join(os.path.dirname(ansible.__file__), 'collections')
    if os.path.exists(coll_path):
        coll_dirs = list(list_collection_dirs(coll_path))
        assert len(coll_dirs) == 0



# Generated at 2022-06-12 20:55:23.367600
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert '' in set(list_valid_collection_paths())
    assert list_valid_collection_paths(['not_here']) == []
    assert list_valid_collection_paths(['not_here'], warn=True) == []
    assert list_valid_collection_paths([__file__]) != []

# Generated at 2022-06-12 20:55:35.167145
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.collection_loader import list_valid_collection_paths
    import os

    # Gather current values
    cur_ansible_collections_paths = AnsibleCollectionConfig.collection_paths
    cur_ansible_roles_paths = AnsibleCollectionConfig.role_paths

    # Test only absolute paths
    assert list(list_valid_collection_paths(['/tmp'])) == ['/tmp']

    # Test only roles paths
    assert list(list_valid_collection_paths(['/etc/ansible/roles'])) == []

    # Test only non existing paths
    assert list(list_valid_collection_paths(['/tmpp'])) == []

    # Test only existing collections paths

# Generated at 2022-06-12 20:55:44.238890
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    assert not list(list_collection_dirs(['../test/test_collections/invalid']))

    assert not list(list_collection_dirs(['../test/test_collections/invalid'], 'test.test_plugins'))

    assert list(list_collection_dirs(['../test/test_collections'], 'test.test_plugins'))

    assert list(list_collection_dirs(['../test/test_collections'], 'test.test_plugins'))

    assert list(list_collection_dirs(['../test/test_collections'], 'test'))

    assert list(list_collection_dirs(['../test/test_collections']))

# Generated at 2022-06-12 20:55:52.206905
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Valid directories
    valid_paths = ['/tmp', '/etc/ansible/']

    for path in valid_paths:
        assert list(list_valid_collection_paths([path])) == [path]

    # Non existing directory
    invalid_path = "/I/do/not/exist"
    assert list(list_valid_collection_paths([invalid_path])) == []

    message = "The configured collection path {0}, exists, but it is not a directory.".format(invalid_path)
    with pytest.raises(AnsibleError, match=message):
        list(list_valid_collection_paths([invalid_path], True))

    # Not a directory
    invalid_path = '/tmp/file'

# Generated at 2022-06-12 20:56:02.684294
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.utils.path import get_distribution_path
    if get_distribution_path():
        # We are running from source, so the config path is probably not valid for testing
        # unless the user has run ansible-galaxy collection install
        return

    # Test path that doesn't exist
    colls = list_valid_collection_paths(search_paths=['/tmp/doesnotexist'], warn=False)
    assert(list(colls) == [])

    # Test path that isn't a directory
    colls = list_valid_collection_paths(search_paths=['/etc/ansible/ansible.cfg'], warn=False)
    assert(list(colls) == [])

    # Test valid path

# Generated at 2022-06-12 20:56:07.580105
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths(["/fake/dir"])) == []

    assert list(list_valid_collection_paths(["/etc"])) == []

    assert list(list_valid_collection_paths(["/usr/bin"])) == []

    assert list(list_valid_collection_paths(["/usr"])) == []

    assert list(list_valid_collection_paths(["/"])) == []



# Generated at 2022-06-12 20:56:14.968850
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths())
    assert list(list_valid_collection_paths(search_paths=[]))
    assert list(list_valid_collection_paths(search_paths=['/does/not/exist']))
    assert list(list_valid_collection_paths(search_paths=['']))
    assert list(list_valid_collection_paths(search_paths=['/']))

# Generated at 2022-06-12 20:56:26.319260
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    list_collection_dirs function unit tests
    """
    import tempfile
    from ansible.module_utils._text import to_text
    from ansible.utils.collection_loader import _collection_set_paths

    expected = []

    # create directories for tests
    with tempfile.TemporaryDirectory() as temp_dir:

        # load default collection_paths for tests
        _collection_set_paths(reset=True)

        test_paths = [
            os.path.join(temp_dir, 'ansible_collections'),
            os.path.join(temp_dir, 'collections'),
        ]

        # reset paths
        _collection_set_paths(reset=True)

        # test passing a non-existent dir

# Generated at 2022-06-12 20:56:37.728685
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils.common.collections import list_collection_dirs

    display.warning = lambda x: x
    display.display = lambda x: x

    assert len(list(list_collection_dirs())) > 0

    assert len(list(list_collection_dirs(search_paths=['../test/fixtures/collection_loader/imported']))) == 1

# Generated at 2022-06-12 20:56:48.728024
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil


# Generated at 2022-06-12 20:56:52.872282
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    path = '/tmp/no_such_path'
    paths = [path, '/tmp/', 'no_such_path', None]
    valid_paths = list(list_valid_collection_paths(paths, warn=True))
    assert len(valid_paths) == 1
    assert valid_paths[0] == '/tmp/'

# Generated at 2022-06-12 20:56:59.095256
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = []

    # should return default search_path without errors
    search_paths = list_valid_collection_paths(search_paths)
    assert isinstance(search_paths, list)

    # Test for non existing search_path
    search_paths = ["/blah/blah"]
    search_paths = list_valid_collection_paths(search_paths, warn=True)
    assert isinstance(search_paths, list)
    assert len(search_paths) == 0

    # Test for search_path which is a file
    search_paths = ["/etc/hosts"]
    search_paths = list_valid_collection_paths(search_paths, warn=True)
    assert isinstance(search_paths, list)

# Generated at 2022-06-12 20:57:08.444696
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.plugins import (
        action_loader,
        cache_loader,
        callback_loader,
        connection_loader,
        lookup_loader,
        module_loader,
    )

    loader, namespaces = module_loader

    all_collections = list_collection_dirs()
    all_namespaces = list(namespaces)

    for coll_path in all_collections:
        coll_name = os.path.basename(coll_path)
        ns_name = os.path.basename(os.path.dirname(coll_path))

        assert coll_name in loader._plugin_path_cache[coll_path]
        assert ns_name == loader._get_ns_from_path(coll_name, coll_path)

    assert all_namespaces == list(loader._get_collection_namespaces())

# Generated at 2022-06-12 20:57:09.216689
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # TODO
    pass


# Generated at 2022-06-12 20:57:14.130921
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_paths = ['/tmp/doesnotexist', '../relative/doesnotexist', './relativecwd/doesnotexist', '/tmp/doesnotexist2']

    for path in list_valid_collection_paths(test_paths):
        assert path == '/tmp/doesnotexist2'

    try:
        next(list_valid_collection_paths())
    except StopIteration:
        pass
    except Exception as ex:
        assert False, 'Unexpected exception: %s' % ex

# Generated at 2022-06-12 20:57:24.590536
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.ansible_release import __version__

    MODULE_ARGS = dict(
        collection_paths=['./ansible_collections', '/does/not/exist', '/tmp'],
    )

    module = AnsibleModule(
        argument_spec=MODULE_ARGS,
        supports_check_mode=True,
    )

    paths = list_valid_collection_paths(module.params['collection_paths'])
    assert len(paths) == 2
    assert './ansible_collections' in paths
    assert '/tmp' in paths


# Generated at 2022-06-12 20:57:34.673624
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for function list_collection_dirs
    """
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.system import get_platform_facts
    from ansible.module_utils.facts.virtual.base import Virtual, VirtualCollector

    facts = get_platform_facts(
        (Virtual, VirtualCollector),
        {}
    )

    # FIXME: use a temp dir instead of a system path
    search_paths = ['~/.ansible/collections/ansible_collections/']
    coll_dirs = []

    # list all collection directories
    for coll_dir in list_collection_dirs(search_paths):
        coll_dirs.append(to_text(coll_dir, errors='surrogate_or_strict'))



# Generated at 2022-06-12 20:57:38.285587
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    coll = "myns.mycoll"
    coll_dir = None
    for c_dir in list_collection_dirs([], coll_filter=coll):
        coll_dir = c_dir
        assert os.path.isdir(c_dir)
        assert os.path.basename(c_dir) == coll
        break

    assert coll_dir == list_collection_dirs([], coll_filter=coll)[0]

# Generated at 2022-06-12 20:57:47.165734
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert next(list_collection_dirs(['test/unit/utils/collection_loader/test_data/collection_path/ansible_collections'])) == b'test/unit/utils/collection_loader/test_data/collection_path/ansible_collections/test_namespace/test_collection'



# Generated at 2022-06-12 20:57:57.635443
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test case with invalid search_paths
    search_paths = ['/test', '/test1', '/test2']
    ret_list = list_valid_collection_paths(search_paths, warn=False)
    assert ret_list == []

    # Test case with valid search_paths
    search_paths = [os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'units', 'modules',
                                 'test_ansible_module_template.py')]
    ret_list = list_valid_collection_paths(search_paths, warn=False)

# Generated at 2022-06-12 20:58:08.170798
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.collections.ansible.plugins.module_utils import collection_loader, ansible_utils
    test_paths = ['/dne', '/not/a/directory', '/dev/null']
    test_collection_root = '/tmp/ansible_collections'
    test_collections = ['jctanner.test', 'jctanner.test_no_plugins']
    # touch a file to test filtering of files
    with open(os.path.join(test_collection_root, 'jctanner.test'), 'w') as f:
        f.write('')

    for coll in test_collections:
        ansible_utils.create_collection(coll, test_collection_root, '.')

    # Test with search paths not found
    valid_paths = list_valid_collection_paths

# Generated at 2022-06-12 20:58:17.444419
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # create temporary collection
    temp_dir = tempfile.mkdtemp()
    ns1_path = os.path.join(temp_dir, 'ansible_collections', 'ns1')
    coll1_path = os.path.join(ns1_path, 'coll1')
    module1_path = os.path.join(coll1_path, 'plugins', 'modules')
    coll2_path = os.path.join(ns1_path, 'coll2')
    module2_path = os.path.join(coll2_path, 'plugins', 'modules')
    os.makedirs(module1_path)
    os.makedirs(module2_path)
    # create file in collection directory to ensure it is skipped

# Generated at 2022-06-12 20:58:23.079892
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    d = tempfile.mkdtemp()
    try:
        paths = list(list_valid_collection_paths([d]))
        assert d in paths
    finally:
        import shutil
        shutil.rmtree(d)

# Generated at 2022-06-12 20:58:33.691325
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_dirs = list(list_collection_dirs(search_paths=['fixtures'], coll_filter="foo.bar"))
    assert len(collection_dirs) == 1
    collection_dir = collection_dirs[0]
    assert to_bytes(collection_dir).endswith(to_bytes('foo/bar'))
    assert os.path.exists(collection_dir)
    assert os.path.isdir(collection_dir)

    collection_dirs = list(list_collection_dirs(search_paths=['fixtures'], coll_filter="foo"))
    assert len(collection_dirs) == 2

# Generated at 2022-06-12 20:58:42.646758
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    real_paths = [
        '/home/someuser/ansible_collections',
        '/someother/path/ansible_collections',
        '/someother/path/ansible_collections/namespace',
        '/someother/path/ansible_collections/namespace',
        '/someother/path/ansible_collections/namespace/collection',
        '/someother/path/ansible_collections/namespace/collection/plugins',
    ]
    real_paths_dupe = list(real_paths)

# Generated at 2022-06-12 20:58:52.705750
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    my_search_path = []

# Generated at 2022-06-12 20:59:00.055499
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from distutils.version import LooseVersion

    # Test for collection namespaces, collections and paths
    for coll_path in list_collection_dirs(coll_filter=None):
        assert coll_path is not None

    # Test for a specific collection and path
    for coll_path in list_collection_dirs(coll_filter='ansible_namespace.collection1'):
        assert coll_path is not None
        assert coll_path.endswith('ansible_collections/ansible_namespace/collection1')

    # Test for a specific namespace and collections
    for coll_path in list_collection_dirs(coll_filter='ansible_namespace'):
        assert coll_path is not None
        assert coll_path.end

# Generated at 2022-06-12 20:59:11.779439
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    #
    # Test when no search path is passed
    #
    got_collections = list(list_collection_dirs())
    # Expected collection directories
    coll_dirs = [
        {
            'ansible.builtin': os.path.join(os.path.dirname(__file__), '../..', 'ansible_collections', 'ansible', 'builtin'),
            'ansible.netcommon': os.path.join(os.path.dirname(__file__), '../..', 'ansible_collections', 'ansible', 'netcommon'),
        },

    ]

    # Check if collection directories are present in list passed
    for coll_dir in coll_dirs:
        assert got_collections in coll_dir

    #
    # Test when local collection search path is passed
    #
   

# Generated at 2022-06-12 20:59:28.341257
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    coll_dir = os.path.join(coll_dir, 'test', 'unit', 'modules',
                            'network', 'fortios', 'collection')
    os.makedirs(coll_dir)
    coll_file = open(os.path.join(coll_dir, 'ansible_collections'), 'w')
    coll_file.write('# test')
    coll_file.close()
    coll_file = open(os.path.join(coll_dir, 'ansible_namespace'), 'w')
    coll_file.write('test')
    coll_file.close()

# Generated at 2022-06-12 20:59:31.767023
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_paths = ['/path/one', '/path/two', '/path/three']

    results = list(list_valid_collection_paths(test_paths, warn=False))

    assert results == test_paths

# Generated at 2022-06-12 20:59:39.285925
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import stat


# Generated at 2022-06-12 20:59:43.839420
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.collections.ansible.plugins.loader import _get_all_plugin_paths

    # test no search_paths or config
    res = list(list_valid_collection_paths(None))
    assert res == []

    # pass a search path
    res = list(list_valid_collection_paths(['/foo/bar/baz']))
    assert res == ['/foo/bar/baz']

    # pass a search paths
    res = list(list_valid_collection_paths(['/foo/bar/baz', '/this/that']))
    assert res == ['/foo/bar/baz', '/this/that']

    # set search paths in config
    cur_paths = _get_all_plugin_paths()

# Generated at 2022-06-12 20:59:46.977296
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections import init_collection_paths
    
    init_collection_paths()
    
    l = list_collection_dirs()
    assert l is not None
    
    l = list_collection_dirs(['/usr/bin'], 'community.general')
    assert l is not None

# Generated at 2022-06-12 20:59:58.201211
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.display import Display
    import tempfile
    from shutil import rmtree

    display = Display()
    temp_dir = tempfile.mkdtemp()
    temp_dir2 = tempfile.mkdtemp()
    temp_dir3 = tempfile.mkdtemp()
    temp_dir4 = tempfile.mkdtemp()

    # config is empty list
    assert list(list_valid_collection_paths(search_paths=[])) == []

    # search_paths has non-existing dir
    search_paths = [temp_dir, "nadir"]
    assert list(list_valid_collection_paths(search_paths=search_paths)) == [temp_dir]

    # search_paths has existing file

# Generated at 2022-06-12 21:00:00.364309
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    module_paths = ['/etc/collections']
    paths = list(list_valid_collection_paths(module_paths))
    assert module_paths == paths



# Generated at 2022-06-12 21:00:11.643704
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Verify that list_collection_dirs will return collections found in the
    collection search paths, or when passed a path it will return the
    collections, or when passed a collection it will return the collection.
    """
    from ansible.utils.collection_loader import list_collection_dirs

    collections = list_collection_dirs()
    assert collections is not None

    collections = list_collection_dirs(['.'])
    assert collections is not None
    assert len(list(collections)) > 0

    collections = list_collection_dirs(['.'], coll_filter='test_namespace2.test_coll')
    assert collections is not None
    assert len(list(collections)) == 1
    coll = list(collections)[0]
    assert coll.endswith("test_namespace2/test_coll")




# Generated at 2022-06-12 21:00:22.867586
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Prepare test dir structure
    test_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    test_search_paths = ['%s/test/unit/data/test_collections/' % test_dir]

    # namespace and collection provided
    assert list(list_collection_dirs(test_search_paths, coll_filter='ns1.coll1')) == \
        [b'%s/test/unit/data/test_collections/ansible_collections/ns1/coll1' % test_dir]

    # just namespace provided

# Generated at 2022-06-12 21:00:29.407528
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.utils.collection_loader import get_collection_config_files
    from ansible.utils.path import unfrackpath

    collection_configs = get_collection_config_files(unfrackpath("$HOME"))

    for cfg in collection_configs:
        for path in cfg.get_collection_paths():
            assert os.path.isdir(to_bytes(path))



# Generated at 2022-06-12 21:00:45.469473
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    class FakeDisplay(object):
        def __init__(self):
            self.warnings = []

        def warning(self, msg):
            self.warnings.append(msg)

    import tempfile
    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-12 21:00:50.345000
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp', '/root', '/doesnotexist']
    valid_collection_paths = list(list_valid_collection_paths(search_paths, warn=True))
    assert '/tmp' in valid_collection_paths
    assert '/root' in valid_collection_paths
    assert '/doesnotexist' not in valid_collection_paths

# Generated at 2022-06-12 21:01:00.501799
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.release import __version__ as ansible_version
    from os.path import join, dirname

    here = dirname(dirname(dirname(dirname(dirname(dirname(dirname(dirname(dirname(__file__)))))))))
    test_collections_dir = join(here, 'test', 'support', 'test_collections')
    dirs = list_collection_dirs([test_collections_dir])
    assert len(dirs) == 8

    dirs = list_collection_dirs([test_collections_dir], 'namespace2.collection2_2')
    # One namespace and one collection
    assert len(dirs) == 1



# Generated at 2022-06-12 21:01:10.093675
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # !/usr/bin/env python3
    """unit test for list_collection_dirs function"""

    import os
    import tempfile
    import shutil
    from ansible.module_utils.common.collections import list_collection_dirs

    # create temp dir and add valid collection
    tmpdir = tempfile.mkdtemp()
    os.makedirs(os.path.join(tmpdir, 'ansible_collections/namespace1/collection1'))

    searchpath = [tmpdir]

    # Test to find collection in search_path
    assert list(list_collection_dirs(searchpath, 'namespace1.collection1')) == \
        [os.path.abspath(os.path.join(tmpdir, 'ansible_collections/namespace1/collection1'))]

    #

# Generated at 2022-06-12 21:01:17.866340
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert 0 == len(list(list_valid_collection_paths([])))

    assert 4 == len(list(list_valid_collection_paths(search_paths=['/tmp', '/tmp/foo/bar', 'tests/unit/module_utils/test_collections'])))
    assert 2 == len(list(list_valid_collection_paths(search_paths=['tests/unit/module_utils/test_collections', '/tmp', '/tmp/foo/bar'])))



# Generated at 2022-06-12 21:01:27.516437
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    unit test to verify list_collection_dirs

    1. return all collections, even if they are dupes
    2. return only a specific collection
    3. return only a specific namespace
    4. return only a specific namespace and collection
    """

    colls = list(list_collection_dirs())

    # 1 - return all collections
    assert len(colls) > 0

    # 2 - return only a specific collection
    colls = list(list_collection_dirs(coll_filter="ansible_collections.community.general"))
    assert len(colls) == 1
    assert colls[0].endswith("/ansible_collections/community/general")

    # 3 - return only a specific namespace
    colls = list(list_collection_dirs(coll_filter="community"))

# Generated at 2022-06-12 21:01:37.423572
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from os import mkdir, rmdir
    from shutil import rmtree

    # Create a temp directory
    temp_dir = tempfile.mkdtemp()
    # Create a temp directory to be used for collection path
    coll_dir = tempfile.mkdtemp()

    # Check output for default search path in case of empty search path list
    result = list(list_valid_collection_paths([]))
    assert result == []

    # Create a temp directory which does not exist for search path
    temp_dir_path = temp_dir + "/non_exist"
    # Check output for a search path which does not exist
    result = list(list_valid_collection_paths([temp_dir_path]))
    assert result == []

    # Create a search path which is not a directory

# Generated at 2022-06-12 21:01:48.905682
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    '''
    :return:
    '''
    from tempfile import TemporaryDirectory
    from ansible.module_utils.common.collections import AnsibleCollectionConfig

    # No search paths, give default
    result = list(list_valid_collection_paths())

    # Should have the 3 default paths
    assert len(result) == len(AnsibleCollectionConfig.collection_paths)

    # Test different paths, create temporary directory and add to search paths
    with TemporaryDirectory() as test_dir1:
        with TemporaryDirectory() as test_dir2:
            with TemporaryDirectory() as test_dir3:
                # Add bad directory to search paths as well
                with TemporaryDirectory() as test_dir4:
                    os.rmdir(test_dir4)


# Generated at 2022-06-12 21:02:00.135836
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # defaults
    default_coll_dir = AnsibleCollectionConfig.collections_paths()
    default_coll_dir_list = list(list_valid_collection_paths())
    assert default_coll_dir_list
    assert len(default_coll_dir_list) == len(default_coll_dir)

    # defaults with warning
    default_coll_dir = AnsibleCollectionConfig.collections_paths()
    default_coll_dir_list = list(list_valid_collection_paths(warn=True))
    assert default_coll_dir_list
    assert len(default_coll_dir_list) == len(default_coll_dir)

    # invalid path
    invalid_path_list = [
        '/my/path/does/not/exist',
    ]

# Generated at 2022-06-12 21:02:07.683012
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    collection_dirs = list(list_collection_dirs(coll_filter="test_collection.nested"))
    assert isinstance(collection_dirs, list), "list_collection_dirs returned something other than a list"
    assert len(collection_dirs) == 2, "expected 2 directories, got %s" % len(collection_dirs)
    assert collection_dirs[0].endswith('ansible_collections/test_collection/nested'), \
        "expected the test_collection.nested directory to be present, got %s" % collection_dirs[0]
    assert collection_dirs[1].endswith('ansible_collections/test_collection/nested'), \
        "expected the test_collection.nested directory to be present, got %s" % collection_dirs[1]

    collection_

# Generated at 2022-06-12 21:02:32.118052
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    from ansible.module_utils.six.moves.urllib.request import urlopen, URLError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, ContentTooShortError
    import tempfile
    test_dir = tempfile.mkdtemp()

    # Create a file for testing
    (fd, path) = tempfile.mkstemp()
    os.close(fd)

    # Create a directory, that doesn't exist in search_paths
    new_dir = os.path.join(test_dir, 'collections')
    os.mkdir(new_dir)
    assert os.path.exists(new_dir)

# Generated at 2022-06-12 21:02:33.269126
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    x = list(list_collection_dirs(coll_filter='test.test_collection'))
    assert len(x) == 1

# Generated at 2022-06-12 21:02:42.751476
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.collections.ansible import AnsibleCollectionConfig
    from ansible.utils.collection_loader import list_valid_collection_paths

    t_config = AnsibleCollectionConfig()

    # test with default search_paths
    search_paths = list_valid_collection_paths()
    assert len(search_paths) == len(t_config.collection_paths), "default search_paths did not match"

    # test with empty list
    search_paths = list_valid_collection_paths([])
    assert len(search_paths) == len(t_config.collection_paths), "empty search_paths did not return default"

    # random non-existent paths
    test_path = '/var/tmp/xxx-xxx-xxx-xxx'
    search_paths = list_valid_

# Generated at 2022-06-12 21:02:53.644380
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.utils.path import unfrackpath
    from ansible.utils.listify import listify_lookup_plugin_terms

    # create config object that will contain the base paths
    myconfig = AnsibleCollectionConfig()

    # create a valid collection path
    tmp = '/tmp/ansible_test_list_valid_collection_paths'
    valid_path = unfrackpath(tmp)
    os.makedirs(to_bytes(valid_path))

    # create a invalid collection path
    tmp = '/tmp/ansible_test_list_valid_collection_paths_2'
    invalid_path = unfrackpath(tmp)

    # create a valid collection path as file
    tmp = '/tmp/ansible_test_list_valid_collection_paths_3'

# Generated at 2022-06-12 21:02:57.161477
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    coll_dirs = list(list_collection_dirs())
    print(coll_dirs)

if __name__ == '__main__':
    test_list_collection_dirs()

# Generated at 2022-06-12 21:03:06.204491
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # validate list of valid paths, one invalid
    paths = ['/tmp', '/nonexisting', '/usr/share/ansible_collections']
    expected = ['/tmp', '/usr/share/ansible_collections']

    assert list(list_valid_collection_paths(paths)) == expected

    # validate empty list
    paths = []
    assert list(list_valid_collection_paths(paths)) == paths

    # validate None with defaults
    paths = None
    assert list(list_valid_collection_paths(paths)) == AnsibleCollectionConfig.collection_paths



# Generated at 2022-06-12 21:03:17.114528
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    try:
        # invalid path
        assert 'foo' not in list(list_valid_collection_paths(['foo']))
    except Exception as e:
        pass

    try:
        # invalid path
        assert '/invalid/foo/bar' not in list(list_valid_collection_paths(['/invalid/foo/bar']))
    except Exception as e:
        pass

    try:
        # invalid path
        assert 'foo' not in list(list_valid_collection_paths(['foo']))
    except Exception as e:
        pass

    # test default, since it should always exist
    assert AnsibleCollectionConfig.coll_path_default in list(list_valid_collection_paths())

    # test for optional paths

# Generated at 2022-06-12 21:03:24.484968
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    coll_path = os.path.join(os.path.dirname(__file__), '../../../')
    coll_path = os.path.abspath(coll_path)

    # Test the default case, look in the typical places with no filter
    default_dirs = list_collection_dirs()
    for d in default_dirs:
        assert d.startswith(os.path.sep + 'usr')

    # Test that we can search a path outside of the typical places
    user_dirs = list_collection_dirs(search_paths=[coll_path])
    for d in user_dirs:
        assert os.path.abspath(d).startswith(coll_path)

    # Test that we can filter the results to a specific namespace