

# Generated at 2022-06-12 20:53:39.995523
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_search_paths = ["/etc/ansible/collections/ansible_collections", "/etc/ansible/collections/ansible", "~/.ansible/collections/ansible", "~/.ansible/collections/ansible_collections"]

    for i in list_collection_dirs(search_paths=test_search_paths, coll_filter=None):
        print(i)

# Generated at 2022-06-12 20:53:45.219337
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ["/tmp/foo", "/tmp/bar"]
    assert len(list(list_valid_collection_paths(search_paths=search_paths))) == 0
    search_paths = ["/usr/share/"]
    assert len(list(list_valid_collection_paths(search_paths=search_paths))) == 1

# Generated at 2022-06-12 20:53:52.902834
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile

    with tempfile.TemporaryDirectory() as search_path:
        # Create structure in the temporary search_path:
        # search_path/ansible_collections
        #                  /ansible/my_collection
        #                  /ansible/my_other_collection
        #                  /ansible/my_third_collection
        #                  /my/my_other_collection
        #                  /my/my_third_collection
        #                  /my_third_collection

        coll_root = tempfile.mkdtemp(prefix=search_path + '/')
        coll_ns_dir = tempfile.mkdtemp(prefix=coll_root + '/')
        tempfile.mkdtemp(prefix=coll_ns_dir + '/')
        tempfile.mkdtemp(prefix=coll_ns_dir + '/')
        temp

# Generated at 2022-06-12 20:53:59.554936
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    (valid, invalid, invalid_type) = [[], [], []]

    for path in ['/foo', 'bar', '/var/lib/ansible/tmp', os.path.expanduser('~/.ansible/collections'), '/etc/ansible/collections']:
        if not os.path.exists(to_bytes(path)):
            continue

        if not os.path.isdir(to_bytes(path)):
            invalid_type.append(path)
            continue

        valid.append(path)

    assert not invalid_type

    for path in ['/foo', 'bar', '/var/lib/ansible/tmp']:
        if os.path.exists(to_bytes(path)) and os.path.isdir(to_bytes(path)):
            invalid.append(path)


# Generated at 2022-06-12 20:54:09.589013
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import tempfile
    from ansible_collections.ansible.community.tests.unit.compat import unittest

    class TestListCollectionDirs(unittest.TestCase):
        def setUp(self):
            self.dir = tempfile.mkdtemp()
            collection_dirs = ["ansible_collections/ansible1",
                               "ansible_collections/ansible2/namespace"]
            for cd in collection_dirs:
                os.makedirs(os.path.join(self.dir, cd), exist_ok=True)

        def tearDown(self):
            import shutil
            shutil.rmtree(self.dir)

        def test_list_collections(self):
            coll_dirs = list(list_collection_dirs([self.dir]))

# Generated at 2022-06-12 20:54:20.752802
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = [
        os.path.abspath(__file__),
        os.path.join('.', 'ansible_collections'),
        os.path.join('..', 'ansible_collections'),
        os.path.join('..', '..', 'ansible_collections'),
        os.path.join('..', '..', '..'),
        os.path.join('..', '..', '..', '..'),
        '~/my_collection',
        '/tmp/ansible_collections',
        '/tmp',
        '/tmp/Foo',
        '/tmp/Foo/Bar',
        '/tmp/Foo/Bar/non-existent'
    ]

    valid_paths = list(list_valid_collection_paths(search_paths=paths))

    assert os.path

# Generated at 2022-06-12 20:54:31.485863
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """
    Use case 1: With a single collection directory, we want to find all collections
    and all namespaces in that directory.

    Use case 2: With a single collection directory, we want to find a single
    collection and the namespace it belongs to.

    Use case 3: With a single collection directory, we want to find a single
    namespace and all collection in that namespace.

    Use case 4: With multiple collection directories, we want to find a single
    namespace and all collections in that namespace
    """


# Generated at 2022-06-12 20:54:42.579872
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Testcase1: search_paths = None, warn = False
    assert list_valid_collection_paths() == list(AnsibleCollectionConfig.collection_paths)
    # Testcase2: search_paths = ['non_existent_path'], warn = True
    assert list(list_valid_collection_paths(['non_existent_path'], warn=True)) == []
    # Testcase3: search_paths = ['non_existent_path'], warn = False
    assert list(list_valid_collection_paths(['non_existent_path'])) == []
    # Testcase4: search_paths = ['non_directory_file'], warn = True
    assert list(list_valid_collection_paths(['non_directory_file'], warn=True)) == []
    # Testcase5: search

# Generated at 2022-06-12 20:54:51.503993
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile
    import os
    import os.path

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 20:55:01.940960
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import mkdtemp
    from shutil import rmtree

    d = mkdtemp()

# Generated at 2022-06-12 20:55:13.640729
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert set(list_valid_collection_paths(search_paths=["/dev/null"])) == set(["/dev/null"])
    assert set(list_valid_collection_paths(search_paths=["/dev/null"], warn=True)) == set(["/dev/null"])



# Generated at 2022-06-12 20:55:24.642774
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp/fake_collections', '/tmp/fake_collections_2',
                    '/tmp/fake_collections_3', '/tmp/fake_collections_4']
    valid_search_paths = dict()

    # create fake directories
    os.makedirs('/tmp/fake_collections')
    os.makedirs('/tmp/fake_collections_2')
    os.makedirs('/tmp/fake_collections_4')

    for path in list_valid_collection_paths(search_paths=search_paths):
        valid_search_paths[path] = True

    # check if paths are present
    assert '/tmp/fake_collections' in valid_search_paths
    assert '/tmp/fake_collections_2' in valid_search_paths

# Generated at 2022-06-12 20:55:33.052554
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collections = list_collection_dirs(search_paths=["../test/units/collection_loader/data/collections"])
    assert collections is not None
    assert len(collections) == 6
    assert 'ntp.date' in collections
    assert 'test.mycoll' in collections
    assert 'ansible_collections.test.mycoll' in collections
    assert 'test.dupecoll' in collections
    assert 'test.dupecoll_masked' in collections
    assert 'ntp.time' in collections

# Generated at 2022-06-12 20:55:38.750633
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    pathlist = ['.', '/dir1', '/dir2']
    assert list(list_collection_dirs(search_paths=pathlist)) == []

    pathlist = ['../', '/dir1', '/dir2']
    assert list(list_collection_dirs(search_paths=pathlist)) == []

    pathlist = ['../foo']
    assert list(list_collection_dirs(search_paths=pathlist)) == []

    pathlist = ['../foo']
    assert list(list_collection_dirs(search_paths=pathlist, coll_filter='namespace.collection')) == []

# Generated at 2022-06-12 20:55:42.939343
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.ansible.builtin import utils

    collection_list = utils.list_collection_dirs()
    print(collection_list)

    collection_list = utils.list_collection_dirs(['/tmp/myfake/collections'], coll_filter='myns.mycoll')
    print(collection_list)

# Generated at 2022-06-12 20:55:51.738996
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # returns valid local collections for the filter
    test_local_colls = list_collection_dirs(coll_filter='namespace.collection')

    # returns valid system collections for the filter
    test_system_colls = list_collection_dirs(search_paths='/usr/share/ansible/collections', coll_filter='namespace.collection')

    # returns valid local and system collections for the filter
    test_local_and_system_colls = list_collection_dirs(search_paths=['/usr/share/ansible/collections', './collection_root'], coll_filter='namespace.collection')

    # raises error if filter is invalid
    test_coll_filter = list_collection_dirs(coll_filter='invalid')

    # returns all valid local collections
    test_all_local_colls

# Generated at 2022-06-12 20:55:56.754755
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection = 'test_namespace.test_collection'
    namespace = 'test_namespace'

    coll_dir = None
    for coll_dir in list_collection_dirs(coll_filter=collection):
        pass
    assert coll_dir is not None

    coll_dir = None
    for coll_dir in list_collection_dirs(coll_filter=namespace):
        pass
    assert coll_dir is not None

# Generated at 2022-06-12 20:56:00.860273
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import pytest

    search_paths = list_valid_collection_paths(warn=False)

    for path in search_paths:
        dirs = list(list_collection_dirs(path))
        assert isinstance(dirs, list)

# Generated at 2022-06-12 20:56:05.881616
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    expected = list_valid_collection_paths()
    test_list = ['/does/not/exist', "~/path/that/does/not/exist", "/etc/ansible", "/tmp", "/tmp/ansible_collections/ansible_namespace/mycoll/plugins/module_utils"]
    result = list_valid_collection_paths(test_list)
    assert len(result) == len(expected)


# Generated at 2022-06-12 20:56:16.701019
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    list_collection_dirs(['/tmp/fakepath', '/tmp/fakepath2'], 'ansible_collections.foo')
    search_paths = list_valid_collection_paths(['/tmp/fakepath', '/tmp/fakepath2'])
    assert search_paths == []
    list_collection_dirs([], 'ansible_collections.foo')
    valid_paths = list(list_valid_collection_paths([], True))
    assert '/home/myusername/.ansible/collections' in valid_paths
    assert '/usr/share/ansible/collections' in valid_paths
    assert '/usr/local/share/ansible/collections' in valid_paths

# Generated at 2022-06-12 20:56:31.187846
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ["/valid/path", "/path/does/not/exist", "/is/not/a/directory"]
    expected = ["/valid/path", os.getenv('ANSIBLE_COLLECTIONS_PATHS')]
    result = list_valid_collection_paths(search_paths)
    assert sorted(expected) == sorted(list(result))

# Generated at 2022-06-12 20:56:42.371759
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # Pass non existing path and a valid path
    search_paths = ['/string/path/that/does/not/exist', '/usr/share/ansible']

    coll_paths = list(list_valid_collection_paths(search_paths))

    assert len(coll_paths) == 1, \
        "One path from the search_path should be returned."
    assert coll_paths[0] == '/usr/share/ansible', \
        "The path /usr/share/ansible should be returned."

    # Pass an non existent path followed by a valid path
    search_paths = ['/string/path/that/does/not/exist', '/usr/share/ansible']

    coll_paths = list(list_valid_collection_paths(search_paths))


# Generated at 2022-06-12 20:56:53.287687
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    from ansible.utils.collection_loader import get_collection_files
    from ansible.module_utils._text import to_text
    import tempfile
    import shutil

    dir_path = tempfile.mkdtemp()
    collec_path = dir_path + '/ansible_collections'

    os.mkdir(collec_path)
    os.mkdir(collec_path + '/namespace1')
    os.mkdir(collec_path + '/namespace2')
    os.mkdir(collec_path + '/namespace1/collection1')
    os.mkdir(collec_path + '/namespace1/collection2')
    os.mkdir(collec_path + '/namespace1/collection3')

# Generated at 2022-06-12 20:56:57.889336
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    # search_paths is None
    assert len(list(list_valid_collection_paths())) == 1
    assert len(list(list_valid_collection_paths(search_paths=None))) == 1
    assert len(list(list_valid_collection_paths(search_paths=[], warn=True))) == 1

    # search_paths is empty list
    assert len(list(list_valid_collection_paths(search_paths=[]))) == 1
    assert len(list(list_valid_collection_paths(search_paths=[], warn=True))) == 1

    # search_paths is missing
    search_paths=['/foo/bar/acme']
    assert len(list(list_valid_collection_paths(search_paths=search_paths))) == 0

# Generated at 2022-06-12 20:57:07.590550
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    try:
        from unittest import mock
    except ImportError:
        import mock

    search_path = tempfile.mkdtemp(prefix='ansible_collections.test_list_collection_dirs')
    curdir = os.path.dirname(os.path.abspath(__file__))
    # create a collection for testing
    os.mkdir(os.path.join(search_path, 'ansible_collections', 'testcoll.testnamespace'))
    os.mkdir(os.path.join(search_path, 'ansible_collections', 'othercoll.othernamespace'))
    # create a non-collection directory with the same name
    os.mkdir(os.path.join(search_path, 'ansible_collections', 'badcoll'))
    #

# Generated at 2022-06-12 20:57:12.692187
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    coll_dirs = list(list_collection_dirs(["/tmp/ansible_collections"], "namespace.collection"))
    assert len(coll_dirs) == 1
    coll_dirs = list(list_collection_dirs(["/tmp/ansible_collections"], "namespace"))
    assert len(coll_dirs) == 2
    coll_dirs = list(list_collection_dirs(["/tmp/ansible_collections"]))
    assert len(coll_dirs) == 3

# Generated at 2022-06-12 20:57:23.706469
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    from ansible.module_utils.common.collections import ansible_collections_paths

    # test invalid and missing paths
    assert list_valid_collection_paths(["/a/bb"]) == []
    assert list_valid_collection_paths(["/a/bb", "/a/c_bb"]) == []
    assert list_valid_collection_paths(["/a/bb", "/a/c_bb"]) == []

    # test if default path included
    assert list_valid_collection_paths(None) == ansible_collections_paths

    # test some valid
    assert list_valid_collection_paths(["/", "/a"]) == ["/", "/a"]

# Generated at 2022-06-12 20:57:29.643476
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['not-exists', '/tmp', '/tmp/foo']

    correct_paths = []
    for path in search_paths:
        if os.path.exists(path):
            correct_paths.append(path)

    found_paths = list_valid_collection_paths(search_paths)
    assert found_paths == correct_paths


# Generated at 2022-06-12 20:57:36.822044
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test filtering out non existing or invalid search_paths for collections
    """
    path1 = "/etc/ansible/collections"
    path2 = "/some/bogus/path"
    path3 = "/etc/ansible/collections"
    expected = [path1, path2, path3]
    expected_filtered = [path1, path3]

    list_of_paths = list_valid_collection_paths(expected, warn=True)

    assert isinstance(list_of_paths, type(expected))
    assert list(list_of_paths) == expected_filtered



# Generated at 2022-06-12 20:57:42.686775
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    paths = [
        "/my/collection/path",
        "/my/second/collection/path",
    ]
    valid_paths = []
    for path in list_valid_collection_paths(search_paths=paths, warn=True):
        valid_paths.append(path)

    assert len(paths) == len(valid_paths)
    for path in valid_paths:
        assert path in paths


# Generated at 2022-06-12 20:58:01.121979
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # create collection dirs
    collection_dir = './test_list_collection_dirs'
    os.mkdir(collection_dir)
    os.mkdir(os.path.join(collection_dir, 'ansible_collections'))
    os.mkdir(os.path.join(collection_dir, 'ansible_collections', 'namespace_0'))
    os.mkdir(os.path.join(collection_dir, 'ansible_collections', 'namespace_0', 'collection_0'))
    os.mkdir(os.path.join(collection_dir, 'ansible_collections', 'namespace_0', 'collection_1'))
    os.mkdir(os.path.join(collection_dir, 'ansible_collections', 'namespace_1'))
    os.mkdir

# Generated at 2022-06-12 20:58:07.840824
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = ['test/unit/utils/module_utils/ansible_test_collection/',
                    'test/unit/utils/module_utils/ansible_test_collection2/']
    coll_filter = 'mycollection.mynamespace'

    for coll_dir in list_collection_dirs(search_paths=search_paths, coll_filter=coll_filter):
        assert coll_dir == 'test/unit/utils/module_utils/ansible_test_collection2/mynamespace/mycollection'
        break

# Generated at 2022-06-12 20:58:16.482141
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    test_modules = [
        'ansible_collections.ansible.builtin',
        'ansible_collections.ansible.builtin.plugins',
        'ansible_collections.ansible.builtin.plugins.module',
        'ansible_collections.ansible.builtin.plugins.module.ansible_test_collection'
    ]

    test_paths = ['ansible_collections', 'ansible_collections/ansible']

    for path in test_modules:
        assert path in list(list_collection_dirs(test_paths))

    for path in test_paths:
        assert path in list(list_collection_dirs(test_paths))

# Generated at 2022-06-12 20:58:24.044877
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Find search paths from ansible config
    from ansible.config.manager import get_config_data

    search_paths=get_config_data().get('collections_paths', None)
    coll_filter=get_config_data().get('collection_name', None)

    # Lookup collection dirs
    collection_dirs = list_collection_dirs(search_paths=search_paths, coll_filter=coll_filter)

# Generated at 2022-06-12 20:58:34.692821
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os

    temp_dir = tempfile.TemporaryDirectory()
    coll_path = os.path.join(temp_dir.name, 'ansible_collections')
    os.makedirs(coll_path)

    test_coll_names = [
        "company.collection_name",
        "company.another_collection"
    ]

    for ns in test_coll_names:
        os.makedirs(os.path.join(coll_path, ns))

    # Verify we get back a collection dir for each of our test collections
    for coll_dir in list_collection_dirs([temp_dir.name]):
        assert coll_dir in [os.path.join(coll_path, x) for x in test_coll_names], "Found unexpected collection dir: %s"

# Generated at 2022-06-12 20:58:43.135675
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Collection path check_mode when search path is file
    def test_case_1():
        test_paths = ['file']
        result = list(list_valid_collection_paths(test_paths))
        assert result == []
    test_case_1()

    # Collection path check_mode when search path is directory
    def test_case_2():
        test_paths = ['dir']
        result = list(list_valid_collection_paths(test_paths))
        assert result == ['/dir/']
    test_case_2()

    # Collection path check_mode when search path is directory
    def test_case_3():
        test_paths = []
        result = list(list_valid_collection_paths(test_paths))

# Generated at 2022-06-12 20:58:47.542439
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    with open('/tmp/collections.json', 'w') as f:
        f.write("""
{
    "collections": [
        {
            "name": "namespace.collection1",
            "version": "1.2.3"
        },
        {
            "name": "namespace.collection2",
            "version": "1.2.3"
        }
    ]
}
""")

    os.mkdir('/tmp/ansible_collections/namespace')
    os.mkdir('/tmp/ansible_collections/namespace/collection1')
    os.mkdir('/tmp/ansible_collections/namespace/collection1/plugins')
    os.mkdir('/tmp/ansible_collections/namespace/collection1/plugins/actions')
    os.mkdir

# Generated at 2022-06-12 20:58:52.165459
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp/ansible_collections/', '/does/not/exist', '/usr/share/ansible']
    assert list(list_valid_collection_paths(search_paths)) == ['/tmp/ansible_collections/', '/usr/share/ansible']

# Generated at 2022-06-12 20:58:59.887169
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import sys
    import os

    coll_dir = tempfile.mkdtemp()
    # 30 different collection dirs.
    for i in range(30):
        b_coll_dir = to_bytes(os.path.join(coll_dir, "ns_%d.collection_%d" % (i, i)))
        os.mkdir(b_coll_dir)
        plugin_dir = os.path.join(b_coll_dir, 'plugins', 'action')
        os.makedirs(plugin_dir)
        with open(os.path.join(plugin_dir, '__init__.py'), 'w') as f:
            f.write('#')


# Generated at 2022-06-12 20:59:11.662532
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.collections.ansible_collections.myns.mycoll import mycoll_avars
    from ansible.collections.ansible.amazon.plugins.modules.rds import (rds_logfile_info, rds_logfile_purge)
    from ansible.collections.ansible.amazon.plugins.filter.dictquery import (dict_query)
    from ansible.plugins.action.copy import (ActionModule as CopyAction)

    # List all collections in default search paths
    result = list_collection_dirs()
    assert len(result) > 5

    # List just a specific collection
    result = list_collection_dirs(coll_filter='ansible.amazon')
    assert len(result) == 1
    assert os.path.basename(result[0]) == 'amazon'

    # List just

# Generated at 2022-06-12 20:59:37.378086
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    import os
    import pytest
    temp_dir = tempfile.gettempdir()
    collection_paths = [temp_dir]
    valid_collection_paths = list_valid_collection_paths(collection_paths)
    assert next(valid_collection_paths) == temp_dir
    with pytest.raises(StopIteration):
        next(valid_collection_paths)



# Generated at 2022-06-12 20:59:48.494853
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from ansible.collections import is_collection_search_path
    from ansible.collections import is_collection_path

    result = list(list_valid_collection_paths(search_paths=[], warn=True))
    assert result == list_valid_collection_paths()

    tmpdir = tempfile.mkdtemp()
    to_bytes(tmpdir)
    result = list(list_valid_collection_paths(search_paths=[tmpdir], warn=True))
    assert [tmpdir] == result

    not_a_col_path = os.path.join(tmpdir, "foo")
    os.mkdir(to_bytes(not_a_col_path))

# Generated at 2022-06-12 20:59:59.884394
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # basic test
    search_pathes = [os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  '../../../test/units/module_utils/ansible_test_collections/collections'))]

    path_list_sp = list(list_collection_dirs(search_pathes))

    assert len(path_list_sp) == 2, "expected 2"

    path_list_sp_coll = list(list_collection_dirs(search_pathes, 'testns.testcoll'))

    assert len(path_list_sp_coll) == 1, "expected 1"

    path_list_sp_ns = list(list_collection_dirs(search_pathes, 'testns'))


# Generated at 2022-06-12 21:00:04.911722
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    g = list_collection_dirs(coll_filter='community.general')
    ansible_collections_path = next(g)
    assert('ansible_collection_path' in ansible_collections_path)
    assert('community.general/ansible_collections/' in ansible_collections_path)
    assert('test/ansible_collections/community.general' not in ansible_collections_path)

# Generated at 2022-06-12 21:00:13.900358
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from os.path import realpath
    temp_file = tempfile.NamedTemporaryFile()
    b_temp_file = to_bytes(temp_file.name)
    paths = ['test/test', b_temp_file, 'none', temp_file.name, realpath(b_temp_file), realpath(temp_file.name)]
    for path in list_valid_collection_paths(paths, warn=True):
        assert os.path.exists(path)
        assert path in [realpath(b_temp_file), realpath(temp_file.name)]

# Generated at 2022-06-12 21:00:25.055981
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths()
    :return: list of collection directory paths
    """

    search_paths = ["/tmp/foo", "/tmp/bar"]
    paths = list(list_valid_collection_paths(search_paths))
    assert not paths

    search_paths = ["/tmp/foo", "/tmp/bar"]
    os.mkdir("/tmp/foo")
    os.mkdir("/tmp/bar")
    paths = list(list_valid_collection_paths(search_paths))
    assert not paths

    search_paths = ["/tmp/collection/foo", "/tmp/collection/bar"]
    os.makedirs("/tmp/collection/foo")
    os.makedirs("/tmp/collection/bar")

# Generated at 2022-06-12 21:00:33.534180
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(["fakedir", "fakedir2"])) == [],\
        "Expected empty list for non existing paths"

    # validate correct return of valid path
    assert list(list_valid_collection_paths([os.path.dirname(__file__)])) == [os.path.dirname(__file__)],\
        "Expected single valid path in list"

    assert list(list_valid_collection_paths(["fakedir1", os.path.dirname(__file__), "fakedir2"])) == [os.path.dirname(__file__)],\
        "Expected single valid path in list"


# Generated at 2022-06-12 21:00:38.412283
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['/bad/path', '/good/path']
    expected_paths = ['/good/path']

    paths = list(list_valid_collection_paths(search_paths, warn=False))

    assert paths == expected_paths



# Generated at 2022-06-12 21:00:42.633002
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    for collection in list_collection_dirs(search_paths=['/vagrant/test/units/modules/collections/empty',
                                                         '/vagrant/test/units/modules/collections/fake'],
                                           coll_filter='ns.coll'):
        assert collection == '/vagrant/test/units/modules/collections/fake/ns/coll'

# Generated at 2022-06-12 21:00:48.363475
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    from ansible.module_utils.common.collections import AnsibleCollectionRef
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # Set up our default config in a tmp directory
    orig_config = AnsibleCollectionConfig.collection_paths
    tmpdir = tempfile.mkdtemp()

    # This is the test: it should only return the default config
    # which is the 'ansible_collections' under the python lib directory
    paths = list(list_valid_collection_paths())
    assert len(paths) == 1

    # Now set the default config to a path we know doesn't exist
    AnsibleCollectionConfig.collection_paths = ['/tmp']
    paths = list(list_valid_collection_paths())
    assert len(paths) == 0

    # Now set the

# Generated at 2022-06-12 21:01:23.343450
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert to_bytes("usr/local/share/ansible_collections") in list_valid_collection_paths()
    assert to_bytes("usr/share/ansible_collections") in list_valid_collection_paths()
    assert to_bytes("test_path") not in list_valid_collection_paths(search_paths=['test_path'])

# Generated at 2022-06-12 21:01:34.262103
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil

    dirs = []
    tmpdir = tempfile.mkdtemp()

    # Create a valid and invalid collection dir
    dirs.append(os.path.join(tmpdir, 'ansible_collections', 'mynamespace', 'mycoll'))
    dirs.append(os.path.join(tmpdir, 'ansible_collections', 'mynamespace2', 'mycoll2'))
    dirs.append(os.path.join(tmpdir, 'ansible_collections', 'invalid'))
    dirs.append(os.path.join(tmpdir, 'ansible_collections', 'mynamespace3', 'invalid'))
    for d in dirs:
        os.makedirs(d)

    # Test it
    results = None

# Generated at 2022-06-12 21:01:42.961584
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    path_list = ['/tmp', '/tmp2']
    result_list = list(list_valid_collection_paths(path_list))
    assert len(result_list) == 2
    assert result_list[0] == '/tmp'
    assert result_list[1] == '/tmp2'
    os.makedirs('/tmp2')
    result_list = list(list_valid_collection_paths(path_list))
    assert len(result_list) == 1
    assert result_list[0] == '/tmp2'
    os.rmdir('/tmp2')
    open('/tmp2', "w").close()
    result_list = list(list_valid_collection_paths(path_list))
    assert len(result_list) == 0
    os.remove('/tmp2')



# Generated at 2022-06-12 21:01:49.714880
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    list_valid_collection_paths(
        [
            '/does/not/exist',
            '/this/one/does',
            '/this/one/does/too',
            '/this/one/does/too/but/not/a/dir',
        ],
        warn=True
    )



# Generated at 2022-06-12 21:01:58.041219
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = []

    # Test for All
    for path in list_collection_dirs(search_paths):
        assert True

    # Test for specific collection
    for path in list_collection_dirs(search_paths, "ansible_collections.ns"):
        assert True
    # Test for invalid collection
    for path in list_collection_dirs(search_paths, "ns.coll"):
        assert False

    # Test for valid collection
    collections = list_collection_dirs(search_paths, "ns.coll")
    assert len(collections) > 0

# Generated at 2022-06-12 21:02:05.762988
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    fake_path = "/some/path/that/does/not/exist"
    search_paths = ['/some/path/that/does/exist', fake_path]
    valid_paths = list(list_valid_collection_paths(search_paths))
    assert len(valid_paths) == 1, "Expected 1 path got: %s" % valid_paths

    # And again, but with a warning
    valid_paths = list(list_valid_collection_paths(search_paths, warn=True))
    assert len(valid_paths) == 1, "Expected 1 path got: %s" % valid_paths

# Generated at 2022-06-12 21:02:16.797978
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/some/none/existing/path', '/some/other/path']

    result = list_valid_collection_paths(search_paths, warn=True)
    assert result == search_paths

    search_paths = ['/etc/ansible/collections']

    result = list_valid_collection_paths(search_paths, warn=True)
    assert result == search_paths

    search_paths = ['/etc/ansible/collections/ansible_collections']

    result = list_valid_collection_paths(search_paths, warn=True)
    assert result == []

    search_paths = ['/etc/ansible']

    result = list_valid_collection_paths(search_paths, warn=True)
    assert result == []

    search_

# Generated at 2022-06-12 21:02:27.480877
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    expected_paths = ['/etc/ansible/collections', '/usr/share/ansible/collections', '/usr/local/share/ansible/collections']
    actual_paths = list(list_valid_collection_paths())
    assert actual_paths == expected_paths

    expected_paths = ['/etc/ansible/collections', '/usr/share/ansible/collections', '/usr/local/share/ansible/collections',
                      '~/.ansible/collections', '/ansible/collections']
    actual_paths = list(list_valid_collection_paths(['~/.ansible/collections', '/ansible/collections']))
    assert actual_paths == expected_paths


# Generated at 2022-06-12 21:02:33.679894
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import shutil
    import tempfile

    (fd, temp_dir) = tempfile.mkstemp()
    temp_dir = temp_dir + "_dir"
    os.close(fd)
    os.mkdir(temp_dir)

    # create collection dir
    ns1_dir = os.path.join(temp_dir, "ansible_collections")
    ns1_test_dir = os.path.join(ns1_dir, "myns", "testcoll")
    os.makedirs(ns1_test_dir)

    # create collection in non-collection path
    ns2_dir = os.path.join(temp_dir, "myns", "testcoll")
    os.makedirs(ns2_dir)

    # create collection in namespace path
    ns3_dir = os.path.join

# Generated at 2022-06-12 21:02:38.536122
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    dir_list = list_collection_dirs(search_paths="../../../../ansible_collections/./../../../collection_dirs")
    for dir_name in dir_list:
        assert os.path.isdir(dir_name), "Invalid collection path: %s" % dir_name

# Generated at 2022-06-12 21:03:23.570468
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import pytest
    from ansible import context
    # test all existing path return true
    context.CLIARGS = {'collections_paths': ['/etc/ansible/hosts',],}
    search_paths = list_valid_collection_paths()
    assert next(search_paths) == '/etc/ansible/hosts'
    # test non exist file return false.
    context.CLIARGS = {'collections_paths': ['test',],}
    search_paths = list_valid_collection_paths()
    assert next(search_paths, None) is None
    # test not a directory file return false.
    context.CLIARGS = {'collections_paths': [__file__,],}
    search_paths = list_valid_collection_paths()


# Generated at 2022-06-12 21:03:29.753398
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list_valid_collection_paths(['/foo/bar', '/tmp']) == ['/foo/bar', '/tmp']
    assert list_valid_collection_paths(['/foo/bar', '/tmp']) != ['/foo/bar2', '/tmp2']
    assert list_valid_collection_paths(['/foo/bar', '/tmp']) != ['/foo/bar', '/tmp', '/tmp2']
    assert list_valid_collection_paths(['/foo/bar', '/tmp']) != ['/foo/bar', '/tmp2']