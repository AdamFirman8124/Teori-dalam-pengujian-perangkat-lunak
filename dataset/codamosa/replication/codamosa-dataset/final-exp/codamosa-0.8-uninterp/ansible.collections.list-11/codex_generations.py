

# Generated at 2022-06-12 20:53:40.788641
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    This test is for ansible-test sanity
    """
    collection = 'test.collection'
    search_paths = ['test/test-collection']
    collection_dirs = list_collection_dirs(search_paths, collection)
    for collection_dir in collection_dirs:
        assert isinstance(cur_dir, bytes)
        assert is_collection_path(cur_dir)

    # test with no collection
    collection_dirs = list_collection_dirs(search_paths, None)
    for collection_dir in collection_dirs:
        assert isinstance(cur_dir, bytes)
        assert is_collection_path(cur_dir)

# Generated at 2022-06-12 20:53:49.223739
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from shutil import rmtree

    my_tmp_paths = []
    try:
        test_paths = ['../foo', 'bar', '../bar.txt', None]
        for path in test_paths:
            my_tmp_paths.append(tempfile.mkdtemp())

        assert len(my_tmp_paths) == len(test_paths) - 1
        my_tmp_paths.extend(test_paths)

        paths = list(list_valid_collection_paths(my_tmp_paths))
        assert len(paths) == 3
        assert paths == my_tmp_paths[:3]

    finally:
        for p in my_tmp_paths:
            rmtree(p)



# Generated at 2022-06-12 20:53:57.818860
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    def filter_none_test():
        filter_none_result = list_collection_dirs(search_paths=['../test/test_collections/'], coll_filter=None)
        assert list(filter_none_result) == ['../test/test_collections/ansible_collections/test_namespace/test_collection_one/']

    def filter_none_multiple_search_paths_test():
        filter_none_result = list_collection_dirs(search_paths=['../test/test_collections/', '../test/test_collections2/'], coll_filter=None)

# Generated at 2022-06-12 20:54:03.423817
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # sanity test if this function is type compatible
    if not isinstance(list_valid_collection_paths([]), type([])):
        raise TypeError("Expected type {} but got {}".format(type([]), type(list_valid_collection_paths([]))))



# Generated at 2022-06-12 20:54:10.221099
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    test_path = os.path.dirname(__file__)

    # set sane defaults
    search_paths = [
        'foo',
        'bar',
        '',
        None,
        {},
    ]
    search_paths.extend(AnsibleCollectionConfig.collection_paths)
    search_paths.append(test_path)

    valid = list(list_valid_collection_paths(search_paths))
    assert len(valid) == 2

    for path in valid:
        assert os.path.exists(path)
        assert os.path.isdir(path)


# Generated at 2022-06-12 20:54:20.843200
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test with search_paths
    search_paths = ["/test_data/test_collections"]
    test_collections = list(list_collection_dirs(search_paths))
    assert test_collections == [b'/test_data/test_collections/ansible_collections/test_namespace/test_collection']
    # Test with collection name
    assert list(list_collection_dirs(search_paths, "test_namespace.test_collection")) == test_collections
    # Test with namespace name
    assert list(list_collection_dirs(search_paths, "test_namespace")) == test_collections
    # Test without supplied search paths
    assert list(list_collection_dirs()) == []
    # Test with non-existant path

# Generated at 2022-06-12 20:54:31.025346
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test paths in search_paths including prepended abs path
    target_search_paths = ['/etc/ansible/', os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../lib/ansible')]
    collection_dirs = list(list_collection_dirs(target_search_paths))
    assert len(collection_dirs) > 2
    assert os.path.basename(collection_dirs[0]) == 'ansible_collections'
    assert os.path.basename(collection_dirs[1]) == 'ansible_collections'

    # Test 1 collection passed on command line with prepended abs path
    collection_dirs = list(list_collection_dirs(target_search_paths,'ansible.builtin'))

# Generated at 2022-06-12 20:54:42.008742
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test paths that exist, testing only Linux paths (this test is supposed to run on Linux)
    valid_paths = [
        "/tmp/does-exist",
        "/etc/ansible/collections",
        "/etc/ansible/collections/ansible_collections",
        "/etc/ansible/testcollections",
        "/etc/ansible/testcollections/ansible_collections",
    ]

    for path in list_valid_collection_paths(valid_paths):
        assert path in valid_paths

    # test paths that do not exist, testing only Linux paths (this test is supposed to run on Linux)

# Generated at 2022-06-12 20:54:49.823565
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    print("===== Testing list_collection_dirs =====")
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    collection_path = os.path.join(base, 'testcollections')
    colls = list(list_collection_dirs([collection_path]))
    assert len(colls) == 2
    assert os.path.join(collection_path, 'ansible_collections', 'ns', 'coll1') in colls
    assert os.path.join(collection_path, 'ansible_collections', 'ns', 'coll2') in colls



# Generated at 2022-06-12 20:55:01.511986
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import shutil
    import tempfile
    import ansible.plugins
    import ansible.module_utils

    plugin_types = list(ansible.plugins.__all__)
    plugin_types.extend(['module_utils', 'module_utils/powershell'])

    # create temp collection and add to collection_paths
    coll_root = tempfile.mkdtemp()
    coll_name = 'mycoll.myname'
    coll_path = os.path.join(coll_root, 'ansible_collections', 'mycoll', 'myname')

# Generated at 2022-06-12 20:55:09.524634
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test function for list_collection_dirs

    :return:
    """
    # TODO: Implement test
    return

# Generated at 2022-06-12 20:55:11.766863
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    invalid_paths = ['', 'foo', 'foo.bar', '/dev/null']
    assert list_valid_collection_paths(search_paths=invalid_paths) == []

# Generated at 2022-06-12 20:55:17.858033
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # test filter by namespace and collection
    colls = list(list_collection_dirs(coll_filter='myns.mycoll'))
    assert(len(colls) == 1)

    # test filter by namespace
    colls = list(list_collection_dirs(coll_filter='myns'))
    assert(len(colls) == 3)

    # test no filter
    colls = list(list_collection_dirs())
    assert(len(colls) == 4)

    # test invalid filter
    colls = list(list_collection_dirs(coll_filter='myns.mycoll.mycoll2'))
    assert(len(colls) == 0)

    # test empty paths
    colls = list(list_collection_dirs([]))
    assert(len(colls) == 4)

# Generated at 2022-06-12 20:55:28.985119
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # empty list of paths, should return default
    search_paths=[]
    assert len(list(list_valid_collection_paths(search_paths=search_paths))) == 1

    # non-existent path, should only return defaults
    search_paths=['/dev/null']
    assert len(list(list_valid_collection_paths(search_paths=search_paths))) == 1

    # missing path with warn=True, warning should be displayed
    search_paths=['/dev/null']
    try:
        result = list(list_valid_collection_paths(search_paths=search_paths, warn=True))
    except AnsibleError:
        pass

    # existing path should be included in results
    search_paths = ['/usr']

# Generated at 2022-06-12 20:55:38.209618
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    sd = tempfile.mkdtemp()

# Generated at 2022-06-12 20:55:43.469265
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    collection_paths = [
        '/tmp/playbooks',
        '/tmp/playbooks2',
        '~/playbooks3',
        '/tmp/playbooks4',
    ]
    assert list_valid_collection_paths(collection_paths) == []

    os.makedirs('/tmp/playbooks4')
    assert list_valid_collection_paths(collection_paths) == ['/tmp/playbooks4']



# Generated at 2022-06-12 20:55:49.572456
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Verify the function list_collection_dirs return the collection paths responding to the namespace, collection name
    and search_paths.
    """
    coll_paths = list_collection_dirs(search_paths=["./plugins/collections"],
                                      coll_filter="namespace.collection_name")
    expected_coll_paths = ['tests/unit/module_utils/test_collection_loader/plugins/collections/namespace/collection_name']
    assert list(coll_paths) == expected_coll_paths



# Generated at 2022-06-12 20:55:55.508009
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = []
    search_paths.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib', 'ansible', 'collections', 'test_collections'))
    search_paths.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib', 'ansible', 'collections', 'non_existing'))
    search_paths.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib', 'ansible', 'collections', 'invalid_directory'))

# Generated at 2022-06-12 20:56:01.968517
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """ Unit test for function list_valid_collection_paths """
    assert list(list_valid_collection_paths()) == []
    assert list(list_valid_collection_paths(search_paths=['/usr/share/ansible/collections', '/some/path/does/not/exist'])) == \
           ['/usr/share/ansible/collections']



# Generated at 2022-06-12 20:56:08.187439
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    valid_paths = ['foo', 'bar']
    assert list_valid_collection_paths(valid_paths, warn=False) == valid_paths
    assert list_valid_collection_paths(valid_paths, warn=True) == valid_paths

    invalid_paths = ['foo', 'dne', 'not_a_directory']
    assert list(list_valid_collection_paths(invalid_paths, warn=False)) == ['foo']
    assert list(list_valid_collection_paths(invalid_paths, warn=True)) == ['foo']



# Generated at 2022-06-12 20:56:23.232582
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths(['/tmp', '/tmp/doesnotexist', '/tmp/1/2/3', '/tmp/1'])) == ['/tmp/1']
    assert list(list_valid_collection_paths(['/tmp', '/tmp/doesnotexist', '/tmp/1/2/3', '/tmp/1', '/tmp'])) == ['/tmp/1', '/tmp']

# Generated at 2022-06-12 20:56:33.044034
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.copy import ActionModule as CopyActionModule
    from ansible.plugins.action.lineinfile import ActionModule as LineinfileActionModule

    with_cache = defaultdict(dict)
    for coll_dir in list_collection_dirs(coll_filter='ansible_collections.notepad.plugins.modules.action'):
        os.environ['ANSIBLE_COLLECTIONS_PATHS'] = coll_dir
        loader = AnsibleCollectionConfig()

        module_list = loader.get_action_plugins()

        # only these 2 modules should be in this collection as it is a subset of the action module collection
        assert module_list == [CopyActionModule, LineinfileActionModule]
        assert loader.get_action_plugins() is module_list

    #

# Generated at 2022-06-12 20:56:43.271477
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Unit test for list_collection_dirs
    """
    fake_base_path = "/tmp/ansible/ansible_collections"
    fake_collections = [
        "ns1.coll1",
        "ns1.coll2",
        "ns2.coll1",
        "ns2.coll2"
    ]

    import shutil
    import tempfile
    from os.path import join

    # Create fake namespace and collection directories
    base_path = tempfile.mkdtemp(prefix="ansible-test-")
    for coll in fake_collections:
        path = join(base_path, coll)
        os.makedirs(path)

    # Make sure there is nothing at the top level that would interfere
    shutil.move(base_path, '/tmp/')
    os.maked

# Generated at 2022-06-12 20:56:53.650589
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test returns subsets of original list
    :return:
    """

    search_paths = [
        'does_not_exist',
        '/tmp',
        '/tmp/ansible_collections',
        '/etc/ansible',
        '/usr/share/ansible'
    ]

    search_path_list = list_valid_collection_paths(search_paths, warn=True)

    assert len(list(search_path_list)) == 4
    assert '/tmp' in search_path_list
    assert '/tmp/ansible_collections' in search_path_list
    assert '/etc/ansible' in search_path_list
    assert '/usr/share/ansible' in search_path_list
    assert 'does_not_exist' not in search_path_list

# Generated at 2022-06-12 20:57:05.623380
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list(list_collection_dirs(['/a/b/c/d'])) == []
    # now set a mock up in place
    import sys
    import tempfile
    sys.modules['ansible'] = tempfile
    ansible = sys.modules['ansible']
    ansible.display = tempfile
    ansible.display.warning = lambda x: None
    import os
    t = tempfile.mkdtemp()
    t2 = tempfile.mkdtemp(dir=t)
    assert list(list_collection_dirs([t])) == []
    coll = tempfile.mkdtemp(dir=t2)
    os.mkdir(os.path.join(coll, 'test'))
    os.mkdir(os.path.join(coll, 'tests'))

# Generated at 2022-06-12 20:57:08.781662
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/invalid1', '/invalid2']
    paths = list(list_valid_collection_paths(search_paths))
    assert len(paths) == 0

# Generated at 2022-06-12 20:57:19.706183
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_paths = ["/foo/bar/baz", "/asdf/jkl;/fdsa", "foobar", "fdsa", "", "/foo/bar;/baz/asdf/jkl"]
    valid_paths = list(list_valid_collection_paths(test_paths))
    assert len(valid_paths) == 3
    assert "/asdf/jkl;/fdsa" in valid_paths
    assert "/foo/bar/baz" in valid_paths
    assert os.path.join(os.path.expanduser("~"), "ansible/collections") in valid_paths


# Generated at 2022-06-12 20:57:26.874165
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    test for function list_collection_dirs
    :return: None
    """
    coll_dir = './test/unit/fixtures/ansible_collections'
    assert next(list_collection_dirs([coll_dir]), None) is not None
    assert next(list_collection_dirs([]), None) is None
    assert next(list_collection_dirs([coll_dir], 'notexist'), None) is None
    assert next(list_collection_dirs([coll_dir], 'notexist.notexistcoll'), None) is None
    assert next(list_collection_dirs([coll_dir], 'notexist.notexistcoll:notexistmodule'), None) is None

# Generated at 2022-06-12 20:57:36.707885
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_coll_name = 'mycollection'
    test_path = '/tmp/test_list_collection_dirs'

    # Create a collection dir named "mycollection" beneath the specified test path
    os.makedirs(os.path.join(test_path, 'ansible_collections/', 'fake_namespace/' + test_coll_name))

    coll_dirs = list(list_collection_dirs(search_paths=[test_path]))

    # The collection directory should exist within the results
    assert os.path.exists(coll_dirs[0])

    # The collection directory should be a child of the specified test path
    assert os.path.commonprefix([test_path]) == test_path

    # Clean up

# Generated at 2022-06-12 20:57:46.880321
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test that the function returns existing paths and filters out non-existent paths
    """
    import tempfile
    import shutil
    from os.path import abspath, isdir, join

    valid_paths = []
    invalid_paths = []
    for i in range(1,4):
        valid_path = tempfile.mkdtemp()
        valid_paths.append(valid_path)
        valid_paths.append(abspath(valid_path))
        invalid_path = join(abspath(valid_path), 'nonexistent')
        invalid_paths.append(invalid_path)
        invalid_paths.append(abspath(invalid_path))

    valid_paths_all = list(valid_paths)

# Generated at 2022-06-12 20:58:18.973841
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ["tests/data/collections/ansible_collections"]
    collection_dirs = list_collection_dirs(search_paths)
    assert len(list(collection_dirs)) == 1

    collection_dirs = list_collection_dirs()
    assert len(list(collection_dirs)) == 1

    collection_dirs = list_collection_dirs(search_paths, 'namespace1.collection')
    assert len(list(collection_dirs)) == 1

    collection_dirs = list_collection_dirs(search_paths, 'namespace1')
    assert len(list(collection_dirs)) == 1

    collection_dirs = list_collection_dirs(search_paths, 'invalidcollection')
    assert len(list(collection_dirs)) == 0

   

# Generated at 2022-06-12 20:58:24.045076
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert sorted(list_valid_collection_paths()) == list_valid_collection_paths(['/usr/share/ansible/collections']) == \
        list_valid_collection_paths(['/usr/share/ansible/collections', '/foo/bar'])



# Generated at 2022-06-12 20:58:27.670068
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # test list of non-existing paths
    expected_result = set()
    expected_result.update([
        '/etc/ansible/foo',
    ])

    actual_result = list_valid_collection_paths(expected_result)

    assert not actual_result



# Generated at 2022-06-12 20:58:32.187317
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/blah/does/not/exist/', '~/does/not/exist/either']
    # make sure the list validator does not die
    for path in list_valid_collection_paths(search_paths):
        assert False

# Generated at 2022-06-12 20:58:39.195522
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import sys
    import os
    scripts_path = os.path.dirname(__file__)
    sys.path.insert(0, os.path.abspath(scripts_path + '/../../..'))
    from lib.collection_loader import list_collection_dirs

    with open(os.environ['ANSIBLE_CONFIG'], 'r') as f:
        for directory in list_collection_dirs(['/home/mhhoban/ansible_collections/ansible_collections']):
            print(directory)

# Generated at 2022-06-12 20:58:47.626001
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ["/Users/me/ansible/ansible_collections",
                    "~/other_path",
                    "~/my_collections/ansible_collections"]
    collection_dirs = [x for x in list_collection_dirs(search_paths=search_paths, coll_filter=None)]
    collection_dirs_with_collection = [x for x in list_collection_dirs(search_paths=search_paths, coll_filter='my_namespace.my_collection')]
    assert len(collection_dirs) == 1
    assert len(collection_dirs_with_collection) == 1


# Generated at 2022-06-12 20:58:51.893231
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    path = [os.path.join(os.environ['ANSIBLE_COLLECTIONS_PATH'])]
    for coll_dir in list_collection_dirs(search_paths=path):
        # TODO: add valid assertions
        assert isinstance(coll_dir, bytes)

# Generated at 2022-06-12 20:58:59.752919
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = [
        os.path.join(os.path.dirname(__file__), 'data', 'collection_loader', 'non_collection_dir'),
        os.path.join(os.path.dirname(__file__), 'data', 'collection_loader', 'non_existing_dir'),
        os.path.join(os.path.dirname(__file__), 'data', 'collection_loader', 'ansible_collections'),
    ]

    try:
        # the dir is not a collection path: it does not contain any collections
        for p in list_valid_collection_paths(search_paths=search_paths, warn=True):
            raise AssertionError("{0}: is not a valid collection path".format(p))
    except AnsibleError:
        pass

    # returns all valid

# Generated at 2022-06-12 20:59:03.561618
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = ['a/b', 'c/d', 'e/f']
    expected = ['a/b', 'c/d', 'e/f']
    assert list_valid_collection_paths(paths) == expected

# Generated at 2022-06-12 20:59:14.330999
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    expected_colls = {
        'ns1': {
            'coll1': '/tmp/ansible_collections/ns1/coll1',
            'coll2': '/tmp/ansible_collections/ns1/coll2'
        },
        'ns2': {
            'coll1': '/tmp/ansible_collections/ns2/coll1',
            'coll2': '/tmp/ansible_collections/ns2/coll2'
        },
        'ns3': {
            'coll1': '/tmp/ansible_collections/ns3/coll1',
            'coll2': '/tmp/ansible_collections/ns3/coll2'
        }
    }

    namespace = None
    collection = None
    search_path = ['/tmp']

    result = []


# Generated at 2022-06-12 20:59:58.527875
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert set(list_valid_collection_paths([os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures/functional/test_utils_collection/nonexistent_path")])) == \
           {os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures/functional/test_utils_collection/nonexistent_path")}



# Generated at 2022-06-12 21:00:05.594815
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_path = '/tmp/valid_path'
    b_test_path = to_bytes(test_path)

    if os.path.exists(b_test_path):
        os.rmdir(b_test_path)
    os.mkdir(b_test_path)

    path_list = list_collection_dirs(search_paths=[test_path], coll_filter='test_namespace.test_collection')
    assert path_list == []

    os.rmdir(b_test_path)

# Generated at 2022-06-12 21:00:14.232501
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.display import Display

    display = Display()

    path = '/root/collections'
    search_paths = [path]

    path_exists = True
    path_is_a_dir = True

    if path_exists:
        if path_is_a_dir:
            for path in list_valid_collection_paths(search_paths):
                display.display(path)
        else:
            display.warning("The configured collection path {0}, exists, but it is not a directory.".format(path))
    else:
        display.warning("The configured collection path {0} does not exist.".format(path))

# Generated at 2022-06-12 21:00:19.314843
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test specific cases by mocking os.path and os.listdir with custom data
    import unittest.mock as mock
    import os.path as os_path

    with mock.patch("ansible.utils.collection_loader.list_valid_collection_paths.os.path") as mock_os_path,\
            mock.patch("ansible.utils.collection_loader.list_valid_collection_paths.list_collection_dirs") as list_collection_dirs:
        # test 1. empty list
        mock_os_path.exists.return_value = False
        mock_os_path.isdir.return_value = False
        result = list(list_valid_collection_paths())
        assert len(result) == 2
        assert result == ['/my/custom/path', '/my/other/path']

# Generated at 2022-06-12 21:00:30.476763
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert set(list_collection_dirs(['../test/units/fixtures/collection_root_valid', '../test/units/fixtures/bad_collection_root_1'])) == set([
        b'../test/units/fixtures/collection_root_valid/ansible_collections/testns1/testcoll1',
        b'../test/units/fixtures/collection_root_valid/ansible_collections/testns2/testcoll2',
    ])

    assert set(list_collection_dirs(['../test/units/fixtures/collection_root_valid'], 'testns1.testcoll1')) == set([
        b'../test/units/fixtures/collection_root_valid/ansible_collections/testns1/testcoll1',
    ])

    # bad_collection_root_

# Generated at 2022-06-12 21:00:31.932433
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['./collection-artifact'])) == ['./collection-artifact']

# Generated at 2022-06-12 21:00:37.304917
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # TODO: update this test to use the test data framework
    valid_collections = [
        ("ansible_collections/awk/logan", "awk", "logan"),
        ("ansible_collections/awx/awx", "awx", "awx"),
        ("ansible_collections/ansible_collections/ansible_collections", "ansible_collections", "ansible_collections"),
    ]
    invalid_collections = [
        "playbooks.yml",
        "playbooks.yaml",
        "not_a_valid_collection",
        "ansible_collections/no_namespace",
    ]

    # test collection root
    coll_root = os.path.join(os.path.dirname(__file__), '..')

    coll_dirs = set()

# Generated at 2022-06-12 21:00:42.101461
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = [
        '/foo/bar',
        '/baz/bar',
        'not_exists',
        'test_file'
    ]

    configs = list_valid_collection_paths(search_paths, warn=False)
    assert len(configs) == 2
    assert '/foo/bar' in configs
    assert '/baz/bar' in configs

# Generated at 2022-06-12 21:00:52.226956
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    tmp_base = '/tmp/test_list_valid_collection_paths'
    tmp = {
        'exist': os.path.join(tmp_base, 'exist'),
        'noexist': os.path.join(tmp_base, 'noexist'),
        'file': os.path.join(tmp_base, 'file'),
        'notdir': os.path.join(tmp_base, 'notdir'),
    }


# Generated at 2022-06-12 21:01:03.835965
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Filter non-existing paths and default path
    for path in list_collection_dirs(search_paths=["./not_exists", "/usr/share/ansible"]):
        assert path
        assert path.startswith("/usr/share/ansible")

    # Find path for default collection (should be in default paths)
    for path in list_collection_dirs(coll_filter="ansible_collections.community.general"):
        assert path
        assert path.startswith("/usr/share/ansible/ansible_collections")
        assert b"community" in path
        assert b"general" in path
        break

    # No collection found as it is not in default paths
    assert not list(list_collection_dirs(coll_filter="foobar_namespace.foobar_collection"))

    # Names

# Generated at 2022-06-12 21:02:29.878006
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile
    from ansible.utils.collection_loader import get_collection_paths
    from ansible.module_utils._text import to_bytes

    test_coll_root = tempfile.mkdtemp()

# Generated at 2022-06-12 21:02:34.470633
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert(isinstance(list_valid_collection_paths(), list))
    assert(isinstance(list_valid_collection_paths(search_paths=['/tmp/files']), list))

# Generated at 2022-06-12 21:02:43.258627
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # test 1
    result = list(list_collection_dirs(['../../../../test/sanity/code/unit/data/collection_config/one_collection_path']))
    assert len(result) == 1
    assert result[0] == b'../../../../test/sanity/code/unit/data/collection_config/one_collection_path/ansible_collections/namspace/collection'

    # test 2
    result = list(list_collection_dirs(['../../../../test/sanity/code/unit/data/collection_config/two_collection_paths']))
    assert len(result) == 2

# Generated at 2022-06-12 21:02:49.911920
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible.utils.path import unfrackpath

    # a directory with a subdirectory named "ansible_collections" should be valid
    assert unfrackpath(os.path.join(os.path.dirname(__file__), '../../..')) in list_valid_collection_paths()

    # a directory with no subdirectory named "ansible_collections" should be invalid
    assert not os.path.dirname(__file__) in list_valid_collection_paths()

# Generated at 2022-06-12 21:02:58.967498
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections import example
    from ansible.module_utils.six.moves.builtins import input

    def load_collections(search_paths, warn=False):

        # Note: this function alters AnsibleCollectionConfig class attributes

        display.debug("Search paths we have: {0}".format(search_paths))

        if search_paths is None:
            search_paths = []

        conf = AnsibleCollectionConfig(search_paths=search_paths)
        AnsibleCollectionConfig.config = conf
        AnsibleCollectionConfig.collection_paths = search_paths
        paths = list(list_valid_collection_paths(search_paths, warn))

        return paths

    test_args = []

# Generated at 2022-06-12 21:03:08.598134
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Test valid and invalid search_paths
    search_paths = ['/this/is/an/invalid/path']
    result = list_valid_collection_paths(search_paths, warn=False)
    for x in result:
        assert x in AnsibleCollectionConfig.collection_paths

    search_paths.extend(AnsibleCollectionConfig.collection_paths)
    result = list_valid_collection_paths(search_paths, warn=False)

    for x in result:
        assert os.path.exists(x) and os.path.isdir(x)



# Generated at 2022-06-12 21:03:19.057465
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.module_utils.common.collections import list_collection_dirs

    # Create temp directories
    from tempfile import mkdtemp
    d = mkdtemp()
    d1 = mkdtemp(dir=d)
    d2 = mkdtemp(dir=d)
    d3 = mkdtemp(dir=d)

    # Create test namespaces
    os.mkdir(os.path.join(d1, 'ansible_collections', 'ns1'))
    os.mkdir(os.path.join(d1, 'ansible_collections', 'ns2'))
    os.mkdir(os.path.join(d2, 'ansible_collections', 'ns2'))

    # Create test collections

# Generated at 2022-06-12 21:03:25.445673
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection_paths = ["../../../test/units/lib/ansible_test/_data/collections/ansible_collections/test_namespace/test_collection1",
                        "../../../test/units/lib/ansible_test/_data/collections/ansible_collections/test_namespace/test_collection2",
                        "../../../test/units/lib/ansible_test/_data/collections/ansible_collections/test_namespace2/test_collection3"]