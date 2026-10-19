

# Generated at 2022-06-12 20:53:39.131410
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from ansible_collections.notstdlib.moveitallout.tests.units.module_utils.collection_loader_common import MockModuleUtils
    test = MockModuleUtils()

    assert os.path.exists(list(list_valid_collection_paths([]))[0]) is True

# Generated at 2022-06-12 20:53:48.694518
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # should return default paths from config if none are passed
    assert len(list(list_valid_collection_paths())) == 2

    # try with empty list
    assert len(list(list_valid_collection_paths([]))) == 2

    # a list that contains non-existing path
    with Display():
        assert len(list(list_valid_collection_paths([os.path.join('non-existing-path', 'ansible_collections')]))) == 2

    # a list that contains existing non-dir
    with Display():
        assert len(list(list_valid_collection_paths([__file__]))) == 2

    # a list that contains all existing paths

# Generated at 2022-06-12 20:53:53.211393
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['/tmp'])) == ['/tmp']
    with os.path.expanduser('~/.ansible/collections'):
        assert list(list_valid_collection_paths()) == list(AnsibleCollectionConfig.collection_paths)

# Generated at 2022-06-12 20:54:04.713576
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test with no search_paths provided
    assert list(list_valid_collection_paths()) == list(AnsibleCollectionConfig.collection_paths)

    # Test with a mix of search_paths that do and don't exist
    search_paths = [
        '/tmp/does/not/exist',
        '/usr/share/ansible/collections',
        '/usr/share/ansible/does/not/exist'
    ]

    assert ['/usr/share/ansible/collections'] == list(list_valid_collection_paths(search_paths))

    # Test with a search_paths that exists but is not a directory

# Generated at 2022-06-12 20:54:12.092220
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    # Test that it doesn't return bad paths
    with_bad_paths = list()
    with_bad_paths.extend(AnsibleCollectionConfig.collection_paths)
    with_bad_paths.append("/this_path_should_definitely_not_exist")
    with_bad_paths.append("/this_path_should_definitely_not_exist_at_all")

    # The last path should be fine, because it's the default
    with_bad_paths.append("/usr/share/ansible/")

    res = list_valid_collection_paths(search_paths=with_bad_paths)
    assert len(list(res)) == 1

    # Test that it doesn't return bad paths
    tmpdir = tempfile.mkdtemp()
   

# Generated at 2022-06-12 20:54:20.895985
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test the function 'list_valid_collection_paths' in the ansible.utils.collection_loader module.
    :return: None
    """
    # Test that list_valide_collection_paths() will return only valid collection paths.
    collection_paths = [
        'ansible/test_data',  # not a dir
        'ansible/test/utils/collection_loader/data/coll_dir1',
        '/fake/coll/dir',
        'ansible/test/utils/collection_loader/data/coll_dir2'
    ]
    valid_collection_paths = list(list_valid_collection_paths(collection_paths))
    assert len(valid_collection_paths) == 3
    assert 'ansible/test_data' not in valid_collection_paths

# Generated at 2022-06-12 20:54:23.488431
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    collection = list_collection_dirs('tests/units/collection_loader/collection_paths', 'my_namespace.my_collection')
    assert len(list(collection)) == 1

# Generated at 2022-06-12 20:54:34.171088
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    # test with a non-existent path
    invalid_path = "/some/non/existent/path"
    assert list(list_valid_collection_paths([invalid_path], warn=False)) == []

    # test with a valid directory
    temp_dir = tempfile.mkdtemp()
    assert list(list_valid_collection_paths([temp_dir], warn=False)) == [temp_dir]

    # test with a file that exists
    temp_file = tempfile.mkstemp()
    os.close(temp_file[0])
    assert list(list_valid_collection_paths([temp_file[1]], warn=False)) == []

    # test with a path which is just a plain file
    file_path = tempfile.mkstemp()[1]

# Generated at 2022-06-12 20:54:43.925545
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
  invalid_paths = list(list_valid_collection_paths(['/tmp/does_not_exist']))
  assert len(invalid_paths) == 0
  assert list(list_valid_collection_paths(['/etc'])) == ['/etc']
  assert list(list_valid_collection_paths(['/usr/share/ansible'])) == ['/usr/share/ansible']
  assert list(list_valid_collection_paths(['/usr/share/ansible'])) == ['/usr/share/ansible']
  assert isinstance(list(list_valid_collection_paths(['/etc', '/usr/share/ansible'])), list)


# Generated at 2022-06-12 20:54:52.272699
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = (
        './test/units/utils/collection_loader/ansible_collections',
        './test/units/utils/collection_loader/ansible_collections2',
    )

    coll_dirs = [
        x for x in list_collection_dirs(search_paths=search_paths)
    ]
    assert len(coll_dirs) == 2, "should return all collections in all namespaces"
    assert coll_dirs[0].endswith(os.path.abspath('./test/units/utils/collection_loader/ansible_collections/namespace1/collection1')), "should return collection path with namespace"

# Generated at 2022-06-12 20:55:00.195599
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/tmp/robot', '/mnt/collection']
    val_paths = list(list_valid_collection_paths(search_paths, warn=True))
    assert val_paths == ['/mnt/collection']

# Generated at 2022-06-12 20:55:02.951356
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    assert list(list_valid_collection_paths()) == ['/Users/myuser/Library/Application Support/Ansible/collections',
                                                   '/etc/ansible/collections',
                                                   '/usr/share/ansible/collections']


# Generated at 2022-06-12 20:55:12.967657
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible_collections.all import all

    import shutil
    import tempfile
    import textwrap

    failed = False

    temp_path = tempfile.mkdtemp()

    # Make a fake ansible_collections/all/foo
    all_path = os.path.join(temp_path, 'ansible_collections', 'all')
    foo_path = os.path.join(all_path, 'foo')
    os.makedirs(foo_path)
    with open(os.path.join(foo_path, '__init__.py'), 'w') as f:
        f.write(textwrap.dedent('''
        # collection metadata content
        '''))
    ret = list_collection_dirs([temp_path])
    list_return = list(ret)

# Generated at 2022-06-12 20:55:24.318818
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Reload this module to reset the _fqcn
    importlib.reload(ansible.utils.collection_loader)

    # This test assumes the 'list_collection_dirs' function works
    # which is tested in itself (test_list_collection_dirs).
    # This 'list_valid_collection_dirs' function is a wrapper that
    # filters out non existing directories and invalid collection
    # directories, it simply calls 'list_collection_dirs' with
    # specific arguments, so we are testing that the wrapper does
    # it's job and does not impact the call to list_collection_dirs'.

    # Create test directories
    os.makedirs(os.path.join(test_data_path, 'ansible_collections', 'test_namespace_foo', 'test_collection_bar'))
    os.m

# Generated at 2022-06-12 20:55:35.822374
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import os
    import sys
    cwd = os.getcwd()
    test_path = os.path.join(cwd, 'test_list')
    c = [
        os.path.join(test_path, 'ansible_collections/c/d'),
        os.path.join(test_path, 'ansible_collections/a'),
        os.path.join(test_path, 'ansible_collections/b/a'),
        os.path.join(test_path, 'ansible_collections/b/d'),
        os.path.join(test_path, 'ansible_collections/b/c'),
    ]

    for path in c:
        if not os.path.exists(path):
            os.makedirs(path)

# Generated at 2022-06-12 20:55:39.820995
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    search_paths = []
    coll_filter = ''

    generator = list_collection_dirs(search_paths, coll_filter)
    list_result = list(generator)

    assert list_result is not None, "Expected a list result, was None"


# Generated at 2022-06-12 20:55:43.870955
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    try:
        d = './test/ansible_fake_collections'
        x = list(list_collection_dirs(search_paths=[d]))
        assert x[0] in d
    except Exception as e:
        assert False, e

# Generated at 2022-06-12 20:55:51.919170
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.plugins.loader import collection_loader
    from ansible.utils.display import Display
    display = Display()

    collection_loader._load_collections()

    # first use the cached result
    colls = list_collection_dirs()
    assert colls is not None

    found = 0
    for coll in colls:
        found += 1
        assert os.path.isdir(coll)

    display.display("Found %d collections" % found)

    assert found > 1

    # now force a reload
    collection_loader._load_collections(force_reload=True)

    # first use the cached result
    colls = list_collection_dirs()
    assert colls is not None

    found = 0
    for coll in colls:
        found += 1


# Generated at 2022-06-12 20:55:58.582643
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = u'/nonexistent/foo,/nonexistent/bar,/nonexistent/baz/'
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = to_bytes(os.environ['ANSIBLE_COLLECTIONS_PATHS'])
    assert list_valid_collection_paths() == ['/nonexistent/foo', '/nonexistent/bar', '/nonexistent/baz/']

# Generated at 2022-06-12 20:56:07.511757
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import TemporaryDirectory
    from shutil import copytree
    from tempfile import mkdtemp
    import os

    def assert_dirs_equals(dirs1, dirs2):
        dirs1 = [dir1.replace("\\", "/") for dir1 in dirs1]
        dirs2 = [dir2.replace("\\", "/") for dir2 in dirs2]
        assert len(dirs1) == len(dirs2), "First path list has different size than second"
        for dir1 in dirs1:
            assert dir1 in dirs2, "First path list contains a path missing from second"
        for dir2 in dirs2:
            assert dir2 in dirs1, "Second path list contains a path missing from first"


# Generated at 2022-06-12 20:56:16.854781
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    ansible_path = os.getcwd()
    collection_path = [ansible_path]
    collection_path.extend(AnsibleCollectionConfig.collection_paths)
    collection_dirs = list_collection_dirs(search_paths=collection_path)
    assert collection_dirs

# Generated at 2022-06-12 20:56:21.192720
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = [
        # an invalid search_path
        '~/invalid_search_path'
    ]
    result = list_valid_collection_paths(search_paths=search_paths, warn=True)
    assert len(list(result)) == 0

    list_valid_collection_paths()



# Generated at 2022-06-12 20:56:31.457324
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths
    """
    import tempfile

    from ansible.utils.display import Display

    display = Display()
    with tempfile.NamedTemporaryFile('wt') as fp:
        fp_path = fp.name
    tmp = tempfile.mkdtemp()
    try:
        for paths in [[], "/invalid/path", tmp, fp_path, [tmp, fp_path]]:
            assert list(list_valid_collection_paths(paths)) == [tmp]

    except Exception:
        raise
    finally:
        if tmp:
            os.rmdir(tmp)
        if fp_path:
            os.unlink(fp_path)

# Generated at 2022-06-12 20:56:37.201993
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths([])) == []
    assert list(list_valid_collection_paths(search_paths=["/tmp", "/fake"])) == ["/tmp"]
    assert list(list_valid_collection_paths(search_paths=["/tmp", "/fake"], warn=True)) == ["/tmp"]

# Generated at 2022-06-12 20:56:48.407770
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    # Test case 1: search_paths set, coll_filter None
    search_paths = ["~/.ansible/collections", "/usr/share/ansible/collections"]
    coll_filter = None
    exp_coll_dir1 = ['~/.ansible/collections/ansible_collections', '/usr/share/ansible/collections/ansible_collections']
    assert set(list_collection_dirs(search_paths, coll_filter)) == set(exp_coll_dir1)

    # Test case 2: search_paths set, coll_filter set
    search_paths = ["~/.ansible/collections", "/usr/share/ansible/collections"]
    coll_filter = "ansible.test"

# Generated at 2022-06-12 20:56:56.567893
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    empty_search_paths = []
    expected_default_paths = AnsibleCollectionConfig.collection_paths
    assert (list(list_valid_collection_paths(empty_search_paths)) == expected_default_paths), \
        'Should return the default paths without warning.'

    non_existing_paths = ['/nonexisting/path']
    assert (list(list_valid_collection_paths(non_existing_paths)) == expected_default_paths), \
        'Should not return non existing paths.'
    assert (list(list_valid_collection_paths(non_existing_paths, warn=True)) == expected_default_paths), \
        'Should warn if the search path does not exist.'

    invalid_paths = ['/bin/bash']

# Generated at 2022-06-12 20:57:03.800836
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/var/lib/awx/projects/6/example.com/collections', '/var/lib/awx/projects/6/example.com/library']

    for path in list_valid_collection_paths(search_paths):
        assert isinstance(path, str), 'should be text'
        assert os.path.exists(to_bytes(path)), "Path should exist"
        assert os.path.isdir(to_bytes(path)), "Path should be a directory"


# Generated at 2022-06-12 20:57:11.950298
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile


# Generated at 2022-06-12 20:57:20.197363
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # Test empty search path
    assert next(list_valid_collection_paths()) is not None

    # Test invalid search path
    assert next(list_valid_collection_paths(['/invalid_path'])) is not None

    # Test valid path
    assert next(list_valid_collection_paths(['/bin'])) == '/bin'

    # Test valid path with None search_paths
    assert next(list_valid_collection_paths(['/bin'])) == '/bin'

# Generated at 2022-06-12 20:57:31.149045
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    test_dir = '/tmp/fake_collections'
    search_path = [test_dir]
    this_ns = 'test_ns'
    this_coll = 'test_coll'

    # Create fake test collection
    os.makedirs(os.path.join(test_dir, 'ansible_collections', this_ns, this_coll, 'lib', 'ansible', 'modules'))

    # Verify test collection is found when searching all collections
    found_colls = list(list_collection_dirs(search_paths=search_path))
    assert len(found_colls) == 1
    assert os.path.join(test_dir, 'ansible_collections', this_ns, this_coll) in found_colls[0]

    # Verify test collection is found when searching by collection
    found_coll

# Generated at 2022-06-12 20:57:42.912171
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # setup
    search_paths = []

    # no search paths, defaults should be returned
    assert list_valid_collection_paths(search_paths)



# Generated at 2022-06-12 20:57:53.261052
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    t_paths = ["foo", "bing", "bar"]
    display.verbosity = 0
    # test all
    assert list_collection_dirs(search_paths=t_paths) is not None
    # test namespace only
    assert list_collection_dirs(search_paths=t_paths, coll_filter="neato") is not None
    # test collection only
    assert list_collection_dirs(search_paths=t_paths, coll_filter="dud.foo") is not None
    # test both
    assert list_collection_dirs(search_paths=t_paths, coll_filter="guido.col") is not None
    # test junk

# Generated at 2022-06-12 20:58:01.781551
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    with tempfile.TemporaryDirectory() as coll_root:

        coll_paths = []
        for ns_name in ['namespace1', 'namespace2']:
            b_ns_name = to_bytes(ns_name)
            b_ns_path = os.path.join(coll_root, b_ns_name)
            os.makedirs(b_ns_path)
            coll_paths.append(b_ns_path)

            for coll_name in ['coll1', 'coll2']:
                b_coll_name = to_bytes(coll_name)
                b_coll_path = os.path.join(b_ns_path, b_coll_name)
                os.makedirs(b_coll_path)


# Generated at 2022-06-12 20:58:09.576681
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """Unit test for function list_valid_collection_paths"""
    search_paths = (
        '/etc/ansible/collections',
        '/data/ansible_collections',
        '/data/ansible/collections',
        '/usr/share/ansible/collections',
        'invalid-1',
        'invalid-2',
    )

    search_path_results = (
        '/etc/ansible/collections',
        '/data/ansible_collections',
        '/data/ansible/collections',
        '/usr/share/ansible/collections',
    )

    assert list(list_valid_collection_paths(search_paths)) == list(search_path_results)



# Generated at 2022-06-12 20:58:18.326474
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Ensure that the list of valid_collection_paths is filtered properly
    :return:
    """
    import tempfile
    from shutil import rmtree
    from ansible.collections.ansible.general.tests.unit.test_utils import fixture_path

    tmp_path1 = tempfile.mkdtemp()
    print("Using temp dir1 %s" % tmp_path1)
    tmp_path2 = tempfile.mkdtemp()
    print("Using temp dir2 %s" % tmp_path2)
    b_tmp_path1 = to_bytes(tmp_path1, errors='surrogate_or_strict')
    b_tmp_path2 = to_bytes(tmp_path2, errors='surrogate_or_strict')

# Generated at 2022-06-12 20:58:27.311940
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list_valid_collection_paths(search_paths=['/dev/null'], warn=False) == []
    assert list_valid_collection_paths(search_paths=[], warn=False) == []
    assert list_valid_collection_paths(search_paths=['.'], warn=False) == ['.']
    assert list_valid_collection_paths(search_paths=['../../../../../../..'], warn=False) == []
    assert list_valid_collection_paths(search_paths=['nonexistingdir'], warn=False) == []


# Generated at 2022-06-12 20:58:38.314639
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # Test: no options set returns all collections
    coll_dirs = list(list_collection_dirs())
    assert len(coll_dirs) > 1

    # Test: passing all options returns a single collection
    coll_dirs = list(list_collection_dirs(
        search_paths=['./test/units/utils/ansible_modules_test/test_data/test_collections'],
        coll_filter='test.test_collection_bar'
    ))
    assert len(coll_dirs) == 1
    assert coll_dirs[0].endswith('test_collections/test/test_collection_bar')

    # Test: passing namespace returns all collections in that namespace

# Generated at 2022-06-12 20:58:45.125350
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    # print("\n")
    # for p in list_collection_dirs(warn=True):
    #     print(p)

    mycolls = list_collection_dirs(['/Users/alikins/ansible_collections/ansible_collections',
                                    '/Users/alikins/ansible_collections/ansible_collections/alikins'])
    # print("\n")
    # for c in mycolls:
    #     print(c)

    mycolls = list_collection_dirs(['/Users/alikins/ansible_collections/ansible_collections/alikins/azure'])
    # print("\n")
    # for c in mycolls:
    #     print(c)



# Generated at 2022-06-12 20:58:50.662771
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile

    temp = tempfile.TemporaryDirectory()

    # Create a fake collection
    ansible_collection_dir = os.path.join(temp.name, 'ansible_collections')
    os.mkdir(ansible_collection_dir)
    os.mkdir(os.path.join(ansible_collection_dir, 'fake_collection'))

    # Check if we get the fake collection back
    ret = list(list_collection_dirs([temp.name]))
    assert len(ret) == 1
    assert ret[0].endswith(os.path.join(temp.name, 'ansible_collections', 'fake_collection'))

    # Check if we get the fake collection back by limiting the filter

# Generated at 2022-06-12 20:58:53.985752
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    collections = list_collection_dirs(search_paths=['/usr/share/ansible/collections'])
    for collection in collections:
        display.warning('collection: {0}'.format(collection))

# Generated at 2022-06-12 20:59:13.723756
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert not len(list(list_valid_collection_paths(['/tmp/iamnothere/ansible_collections'])))
    assert not len(list(list_valid_collection_paths(['/tmp/iamnothere/ansible_collections'])))



# Generated at 2022-06-12 20:59:23.809722
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    from tempfile import mkdtemp
    import shutil
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import configparser

    # Create a temp collection path to test and remove it when done
    temp_collection_path = mkdtemp()
    temp_collection_path_empty = os.path.join(temp_collection_path, 'empty')
    os.makedirs(temp_collection_path_empty)

    # Create a temp file to test and remove it when done
    temp_file = mkdtemp()

    # Paths to test
    test_paths = ['not-here', temp_collection_path_empty, temp_file]

    # Test that all paths are considered invalid

# Generated at 2022-06-12 20:59:29.934000
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    ''' Ensure we are getting a subset of what we expect '''

    good_paths = ['/foo/bar', ]
    bad_paths = ['/foo/baz', '/foo/qux', ]

    valid_paths = list(list_valid_collection_paths(search_paths=good_paths + bad_paths, warn=False))
    assert good_paths == valid_paths, "Expected collection paths to be filtered correctly"

# Generated at 2022-06-12 20:59:37.621026
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile
    import os

    try:
        tmpdir = tempfile.mkdtemp()

        shutil.copytree(os.path.join(os.path.dirname(__file__), 'data', 'ansible_collections'), os.path.join(tmpdir, 'ansible_collections'))
        shutil.copytree(os.path.join(os.path.dirname(__file__), 'data', 'test_collections'), os.path.join(tmpdir, 'test_collections'))

        dir_list = list_collection_dirs([tmpdir])
        assert len(dir_list) == 2

    finally:
        # Clean up
        shutil.rmtree(tmpdir)

# Generated at 2022-06-12 20:59:45.262267
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from ansible.plugins.loader import collection_loader
    test_dir = '/tmp/list_collection_dirs_test'

    # create collection directories
    os.makedirs('/tmp/list_collection_dirs_test/namespace1.collection1')
    os.makedirs('/tmp/list_collection_dirs_test/namespace1.collection2')
    os.makedirs('/tmp/list_collection_dirs_test/namespace1.collection3')
    os.makedirs('/tmp/list_collection_dirs_test/namespace2.collection1')
    os.makedirs('/tmp/list_collection_dirs_test/namespace2.collection2')
    os.makedirs('/tmp/list_collection_dirs_test/namespace2.collection3')



# Generated at 2022-06-12 20:59:52.783500
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    """Unit test for the list_collection_dirs function"""
    import tempfile
    import shutil
    from ansible.module_utils import basic

    tmpdir = tempfile.mkdtemp()
    tmpcoll = tmpdir + "/ansible_collections"
    tmpns = tmpcoll + "/namespace"
    tmpcollpath = tmpns + "/collection"
    tmpemptycollpath = tmpns + "/emptycollection"
    tmpothercoll = tmpns + "/other_collection"
    tmpfiltercoll = tmpcoll + "/other_namespace/collection"
    tmpdupecoll = tmpns + "/dupe"
    tmpdupecoll2 = tmpcoll + "/other_namespace/dupe"
    tmpbadcoll = tmpns + "/bad"
    tmppluginpath = tmpcollpath + "/plugins/module_utils"

    os.m

# Generated at 2022-06-12 21:00:03.145798
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import shutil
    import tempfile

    for path in list_valid_collection_paths():
        if os.path.basename(path) != 'ansible_collections':
            path = os.path.join(path, 'ansible_collections')
        b_path = to_bytes(path)
        if os.path.exists(b_path):
            shutil.rmtree(b_path)

    tmpdir = tempfile.mkdtemp()

    coll1 = to_bytes(os.path.join(tmpdir, 'ansible_collections', 'ns1'))
    coll2 = to_bytes(os.path.join(tmpdir, 'ansible_collections', 'ns2', 'coll2'))

# Generated at 2022-06-12 21:00:14.231969
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    import tempfile

    # setup non-default test paths
    coll_paths = []
    for i in range(3):
        # create a temp path to test with
        coll_path = tempfile.mkdtemp("test_list_collection_dirs")
        # ansible.collection.foo -> ansible_collections.foo
        coll_name = "ansible.collection.{0}".format(i)
        # create path for collection
        coll_dir = os.path.join(coll_path, os.path.basename(coll_name))
        # create the collection directory
        os.mkdir(coll_dir)
        # add to the search_path list
        coll_paths.append(coll_path)

    # sanity check the setup
    assert len(coll_paths) == 3

    # list dirs

# Generated at 2022-06-12 21:00:19.371956
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    search_paths = ['/does/not/exist', '.']

    valid_paths = list(list_valid_collection_paths(search_paths=search_paths, warn=False))
    assert len(valid_paths) == 1 and valid_paths[0] == '.'


# Generated at 2022-06-12 21:00:21.807416
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    assert list(list_valid_collection_paths(['/foo/bar'])) == []
    assert list(list_valid_collection_paths([]))



# Generated at 2022-06-12 21:00:57.369286
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-12 21:01:00.552675
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    assert list(list_valid_collection_paths())
    assert list(list_collection_dirs())

# Generated at 2022-06-12 21:01:10.134586
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    from tempfile import TemporaryDirectory
    from shutil import copytree

    # make a collection of ansible_collections
    with TemporaryDirectory() as root1:
        copytree(os.path.join(os.path.dirname(__file__), 'data/ansible_collections'), root1)
        assert list(list_collection_dirs([root1,])) == [os.path.join(root1, 'ansible_collections', 'my', 'test_collection')]

    # make a collection of ansible_collections/ns
    with TemporaryDirectory() as root2:
        copytree(os.path.join(os.path.dirname(__file__), 'data/ansible_collections/my'), root2)

# Generated at 2022-06-12 21:01:21.741322
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths = ['/nonexistent', '/usr/local/share/ansible/collections', '/usr/share/ansible/collections']
    if os.path.exists('does_not_exist'):
        os.rmdir('does_not_exist')
    os.mkdir('does_not_exist')
    paths.append('does_not_exist')
    valid_paths = list(list_valid_collection_paths(search_paths=paths))
    assert len(valid_paths) == 3
    assert '/usr/local/share/ansible/collections' in valid_paths
    assert '/usr/share/ansible/collections' in valid_paths
    assert 'does_not_exist/ansible_collections' in valid_paths

# Generated at 2022-06-12 21:01:24.323761
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    search_paths = ['does/not/exist/', '/tmp/']

    assert {p for p in list_valid_collection_paths(search_paths)} == {'/tmp/'}

# Generated at 2022-06-12 21:01:24.894089
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    pass

# Generated at 2022-06-12 21:01:35.655010
# Unit test for function list_collection_dirs
def test_list_collection_dirs():

    fakecoll_path = os.path.join(os.path.dirname(__file__), 'data/fake_collections')
    fakecoll_paths = [os.path.abspath(fakecoll_path)]

    exp_coll_ns = {
        'my_namespace': 'fake_collections/ansible_collections/my_namespace',
        'other_namespace': 'fake_collections/ansible_collections/other_namespace',
    }

    for coll in list_collection_dirs(search_paths=fakecoll_paths):
        assert is_collection_path(coll)

# Generated at 2022-06-12 21:01:43.854893
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    test_paths = [
        "/home/username/.ansible/collections",
        "/usr/share/ansible/collections",
    ]

    test_paths_non_existing = [
        "/home/username/.ansible/collections",
        "/usr/share/ansible/collections",
        "/non/existing/path"
    ]

    # Load default config and check if configured_paths exist
    for configured_path in AnsibleCollectionConfig.collection_paths:
        found_paths = list_valid_collection_paths(search_paths=test_paths)
        for path in found_paths:
            assert to_bytes(configured_path, errors='surrogate_or_strict') in found_paths

    # Check if warning is shown if path does not exist
    found_path

# Generated at 2022-06-12 21:01:56.281616
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    import tempfile

    # setup two test directories, one non-existent and one a file
    search_paths = []
    path = tempfile.mkdtemp()
    search_paths.append(path)
    path = tempfile.mkstemp()
    search_paths.append(path[1])

    # expect only the valid directory, and no output
    assert len([x for x in list_valid_collection_paths(search_paths, warn=False)]) == 1
    assert len([x for x in list_valid_collection_paths(search_paths, warn=True)]) == 1
    assert len([x for x in list_valid_collection_paths(search_paths, warn=None)]) == 1

# Generated at 2022-06-12 21:02:06.142386
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    paths_to_test = ['fake/path/one', '/some/real/path', '/some/other/real/path']

    def mock_exists(path):
        return path in paths_to_test

    def mock_isdir(path):
        return True

    def mock_isnotdir(path):
        return False

    mock_dict = {
        'exists': mock_exists,
        'isdir': mock_isdir,
        'isnotdir': mock_isnotdir
    }

    # test including a not-found path
    import builtins
    builtins_original = builtins.__dict__
    builtins.__dict__.update(mock_dict)

    from ansible.utils.collection_loader import list_valid_collection_paths as list_valid_collection_paths_function


# Generated at 2022-06-12 21:03:11.898949
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():

    # test unconfigured paths
    assert list(list_valid_collection_paths()) == list(AnsibleCollectionConfig.collection_paths)

    # TODO: test a configured path, add a config and test that

# Generated at 2022-06-12 21:03:21.155303
# Unit test for function list_valid_collection_paths
def test_list_valid_collection_paths():
    """
    Test list_valid_collection_paths
    """

    from ansible.compat.tests import mock, unittest

    class ListValidCollectionPathsTest(unittest.TestCase):
        """
        Test list_valid_collection_paths
        """

        def setUp(self):
            self.mock_path = mock.patch("ansible.module_utils.basic.AnsibleModule.params", new_callable=dict)
            self.mock_path.start()

        def tearDown(self):
            self.mock_path.stop()

        def test_list_valid_collection_paths_none(self):
            """
            Test list_valid_collection_paths with no config
            """

            res = list(list_valid_collection_paths())
            self.assertTrue

# Generated at 2022-06-12 21:03:26.347668
# Unit test for function list_collection_dirs
def test_list_collection_dirs():
    import tempfile
    import shutil
    import os

    def _write_invalid_collection():
        # Write a single file instead of a directory
        with tempfile.NamedTemporaryFile() as test_file:
            test_collection_invalid_path = os.path.join(test_collections_path, "ansible_namespace", "test_collection_invalid")
            return test_file.name, test_collection_invalid_path

    def _write_valid_collection():
        # Create a directory for a collection
        test_collection_valid_path = os.path.join(test_collections_path, "ansible_namespace", "test_collection_valid")
        os.makedirs(test_collection_valid_path)
        return test_collection_valid_path

    # Create the main test collections directory