

# Generated at 2022-06-13 15:50:17.052540
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    finder = _AnsibleCollectionFinder([os.path.abspath('./_testdata/ansible_collections')])
    finder._install() # TODO: not the best test design

    path = os.path.abspath('./_testdata/ansible_collections/zoo/zoo1')
    se = _AnsiblePathHookFinder(finder, path).find_module('zoo1')
    assert se is not None

    path = os.path.abspath('./_testdata/ansible_collections/zoo/zoo1/plugins')
    se = _AnsiblePathHookFinder(finder, path).find_module('zoo1.plugins')
    assert se is not None


# Generated at 2022-06-13 15:50:25.652214
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    fullname = "ansible_collections.amazon.ansible_collections.amazon.ecr"
    _ansibleCollectionPkgLoaderBase = _AnsibleCollectionPkgLoaderBase(fullname)
    _ansibleCollectionPkgLoaderBase._source_code_path = None
    _ansibleCollectionPkgLoaderBase._subpackage_search_paths = ["/home/ubuntu/ansible_collections/amazon/ansible_collections/amazon/ecr/"]
    filename = _ansibleCollectionPkgLoaderBase.get_filename(fullname)
    assert filename == "/home/ubuntu/ansible_collections/amazon/ansible_collections/amazon/ecr/__synthetic__"
    fullname = "ansible_collections.amazon.ansible_collections.amazon.ecr"
    _ansibleCollectionPkg

# Generated at 2022-06-13 15:50:33.987928
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    parent = 'ansible_collections'
    path_list = ['/path/to/collection']
    base_loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections', path_list=path_list)
    assert base_loader.is_package('ansible_collections') == False
    base_loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.collection', path_list=path_list)
    assert base_loader.is_package('ansible_collections.collection') == True



# Generated at 2022-06-13 15:50:42.713988
# Unit test for constructor of class _AnsibleCollectionNSPkgLoader
def test__AnsibleCollectionNSPkgLoader():
    # a.b.c -> ['a.b.c'], a.b -> ['a.b'], a -> ['a'], , a.b.c.d -> ['a.b.c.d']
    _AnsibleCollectionNSPkgLoader('a.b.c', path_list=['/path/to/a/b/c'])
    _AnsibleCollectionNSPkgLoader('a.b', path_list=['/path/to/a/b'])
    _AnsibleCollectionNSPkgLoader('a', path_list=['/path/to/a'])
    _AnsibleCollectionNSPkgLoader('a.b.c.d', path_list=['/path/to/a/b/c/d'])

    # a.b.c -> ['a.b.c', '

# Generated at 2022-06-13 15:50:47.202113
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    package_to_load = 'ansible_collections.somens.somemod'
    try:
        pkg_loader = _AnsibleCollectionPkgLoaderBase(package_to_load, path=[])
    except ImportError:  # valid
        return
    pkg_loader._subpackage_search_paths = []
    assert pkg_loader.is_package(package_to_load) == False
    pkg_loader._subpackage_search_paths = None
    assert pkg_loader.is_package(package_to_load) == False


# Generated at 2022-06-13 15:50:53.081643
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    acr = AnsibleCollectionRef(collection_name='namespace.collectionname', subdirs=None, resource='resource', ref_type='ref_type')
    assert acr.__repr__() == "AnsibleCollectionRef(collection='namespace.collectionname', subdirs=None, resource='resource')"


# Generated at 2022-06-13 15:51:00.790505
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    import tempfile, shutil

    tmpdir = tempfile.mkdtemp()

    tmpdir_data = os.path.join(tmpdir, '__data__')
    os.makedirs(tmpdir_data)

    with open(os.path.join(tmpdir_data, 'file.txt', ), 'wb') as f:
        f.write(b"abc")

    with open(os.path.join(tmpdir_data, 'empty.txt'), 'wb') as f:
        f.write(b"")

    # Test case for get_data() for file that exists
    loader = _AnsibleCollectionPkgLoaderBase(
        'ansible_collections.my.collection',
        path_list=[tmpdir_data]
    )

# Generated at 2022-06-13 15:51:12.946751
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    obj = _AnsibleCollectionPkgLoaderBase("ansible_collections.foo.bar")
    sub_paths = ['__init__.py', 'b.py', 'b', 'c.py']
    prefix = None

    # Normal case
    actual1 = obj._get_subpackage_search_paths(sub_paths)
    expect1 = [sub_paths[2], sub_paths[3]]
    assert actual1 == expect1

    # Normal case
    actual2 = obj.iter_modules(prefix)
    expect2 = [sub_paths[1][:-3], sub_paths[2], sub_paths[3][:-3]]
    assert actual2 == expect2


# NB: this is a no-op, since our loader implementation doesn't need to do anything special on creation. It's only


# Generated at 2022-06-13 15:51:19.765983
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    import json
    import tempfile

    fullname = 'ansible_collections.ns.name'
    path_list = [
        os.path.join(tempfile.gettempdir(), 'ansible_collections/ns/name'),
        os.path.join(tempfile.gettempdir(), 'ansible_collections/ns/name/__synthetic__'),
        os.path.join(tempfile.gettempdir(), 'ansible_collections/ns/name/__init__.py'),
    ]
    # Generate source code used in the compilation of the module
    source_code = '\n'.join(['def fn():', '    pass'])
    decoded_source = source_code.encode('utf-8')

# Generated at 2022-06-13 15:51:20.425622
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
  pass


# Generated at 2022-06-13 15:51:54.029083
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    filename = os.path.join(os.path.dirname(__file__), 'collection_loader.py')
    with open(filename, 'rb') as fd:
        collection_module_code = fd.read()
    code_obj = compile(source=collection_module_code, filename='<string>', mode='exec', flags=0, dont_inherit=True)
    module_attrs = dict(
        __loader__=None,
        __file__='<string>',
        __package__='ansible',
        _meta_yml_to_dict=None,
    )
    module = None
    with _AnsibleCollectionPkgLoader._new_or_existing_module('ansible.collection', **module_attrs) as module:
        # execute the module's code in its namespace
        code_

# Generated at 2022-06-13 15:52:05.775368
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    os.chdir(current_directory)
    test_loader = _AnsibleCollectionPkgLoader(package_to_load='ansible', package_to_scan='collectionstest')
    test_loader_with_parameter = _AnsibleCollectionPkgLoader(package_to_load='ansible', package_to_scan='collectionstest', path=[])
    test_loader_with_sub_package = _AnsibleCollectionPkgLoader(package_to_load='test', package_to_scan='collectionstest', path=[])
    test_loader_with_sub_sub_package = _AnsibleCollectionPkgLoader(package_to_load='test', package_to_scan='sub_sub_package', path=[])

    test_module = test_loader.load_module('ansible')
    assert(test_module)

# Generated at 2022-06-13 15:52:12.784753
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    import ansible.utils.collection_loader
    import ansible.module_utils
    import ansible.modules
    ansible.utils.collection_loader._meta_yml_to_dict = None

    collection_pkg_loader = _AnsibleCollectionPkgLoader('ansible.collections.my_namespace.my_collection', 'module_utils')

    with pytest.raises(ValueError) as load_module_exception:
        collection_pkg_loader.load_module('ansible.collections.my_namespace.my_collection')
    msg = 'ansible.utils.collection_loader._meta_yml_to_dict is not set'
    assert str(load_module_exception.value) == msg

    import ansible_collections.my_namespace.my_collection.module_utils.module_utils



# Generated at 2022-06-13 15:52:19.498559
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # Create value for fullname
    fullname = 'ansible_collections.ansible.test'
    file_name = '__init__.py'
    file_path = '/home/test/test.py'
    # Create value for module_attrs
    module_attrs = {
        '__loader__': 'test',
        '__file__'  : file_path,
        '__package__': 'ansible_collections.ansible'
    }
    # Create value for source_code

# Generated at 2022-06-13 15:52:29.988797
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.resource.yml')
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.resource.yaml')
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.subdir1.resource')
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.resource_with_underscores')
    assert AnsibleCollectionRef.is_valid_fqcr(u'test.coll.resource_with_underscores.yml')

# Generated at 2022-06-13 15:52:35.630758
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # Generate a Validator object and validate parameters
    #auto_validate_parameters(loader._AnsibleCollectionPkgLoaderBase.get_source, ['self', 'fullname'])

    # Test section
    raise Exception('Method test__AnsibleCollectionPkgLoaderBase_get_source() not implemented')


# Generated at 2022-06-13 15:52:46.096200
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    test_data_base_path = "tests/unittests/collection_pkg_loader/data/"
    test_data_path = os.path.join(test_data_base_path, "test_iter_modules_pkg")
    test_data_path_2 = os.path.join(test_data_base_path, "test_iter_modules_pkg_2")
    test_data_path_3 = os.path.join(test_data_base_path, "test_iter_modules_pkg_3")
    test_data_path_4 = os.path.join(test_data_base_path, "test_iter_modules_pkg_4")
    test_data_path_5 = os.path.join(test_data_base_path, "test_iter_modules_pkg_5")

    # setup

# Generated at 2022-06-13 15:52:51.251821
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:52:52.810805
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    assert callable(_AnsibleCollectionPkgLoaderBase.__repr__)



# Generated at 2022-06-13 15:53:01.892325
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    test1 = AnsibleCollectionRef.from_fqcr("ns.coll.resource", "module")
    assert test1.collection == "ns.coll"
    assert test1.subdirs == ""
    assert test1.resource == "resource"
    assert test1.n_python_package_name == "ansible_collections.ns.coll.plugins.module"
    assert test1.n_python_collection_package_name == "ansible_collections.ns.coll"
    assert test1.fqcr == "ns.coll.resource"

    test2 = AnsibleCollectionRef.from_fqcr("ns.coll.subdir.resource", "module")
    assert test2.collection == "ns.coll"
    assert test2.subdirs == "subdir"
    assert test2.resource == "resource"


# Generated at 2022-06-13 15:53:55.367564
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():

    collection_pkg_loader_base = _AnsibleCollectionPkgLoaderBase('ansible_collections.ns.pkg')
    assert collection_pkg_loader_base.__repr__() == '_AnsibleCollectionPkgLoaderBase(path=None)'

    with pytest.raises(AttributeError):
        _AnsibleCollectionPkgLoaderBase()



# Generated at 2022-06-13 15:54:05.195719
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from importlib import machinery
    import tempfile
    from ansible_collections.ansible.tests.unit.plugintest.playbooks import test_playbooks
    from ansible_collections.ansible.tests.unit.plugintest.plugins.modules import test_modules
    from ansible_collections.ansible.tests.unit.plugintest.plugins.module_utils import test_module_utils

    # Create a temporary directory to hold the playbook and collection directory.
    d = tempfile.TemporaryDirectory()

    # Create a playbook directory to hold the test collection.
    playbook_path = os.path.join(d.name, 'playbooks')
    os.mkdir(playbook_path)

    # Create a collection directory to hold the test collection.

# Generated at 2022-06-13 15:54:11.865654
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    '''
    :return:
    '''
    res = _AnsibleCollectionFinder().find_module('Inventory', '/root/ansible')
    assert res is None
    res = _AnsibleCollectionFinder().find_module('ansible', '/root/ansible')
    assert res is not None
    res = _AnsibleCollectionFinder().find_module('ansible', None)
    assert res is not None
    res = _AnsibleCollectionFinder().find_module('ansible.ansible', '/root/ansible')
    assert res is not None
    res = _AnsibleCollectionFinder().find_module('ansible.ansible', None)
    assert res is not None
    res = _AnsibleCollectionFinder().find_module('ansible_collections', '/root/ansible')
   

# Generated at 2022-06-13 15:54:20.435388
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import os.path
    import stat
    import unittest
    import tempfile
    from shutil import rmtree
    from tempfile import mkdtemp
    import errno

    class _AnsibleCollectionPkgLoaderBaseTest(unittest.TestCase):
        def test__get_data(self):
            root_dir = to_bytes(mkdtemp())
            self.addCleanup(rmtree, to_native(root_dir))

            # create a package
            pkgdir = os.path.join(root_dir, b'ansible_collections', b'ansible', b'collections', b'foo', b'bar')
            os.makedirs(pkgdir)

            # create a file
            data = b'hello from ansible.collections.foo.bar.__init__'
            target

# Generated at 2022-06-13 15:54:23.705233
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    p = _AnsibleCollectionPkgLoaderBase('ansible_collections.foo')
    assert p.__repr__() == '_AnsibleCollectionPkgLoaderBase(path=None)'



# Generated at 2022-06-13 15:54:31.184511
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    with pytest.raises(ImportError):
        loader = _AnsibleInternalRedirectLoader('toplevel', 'path')

    with pytest.raises(ImportError):
        loader = _AnsibleInternalRedirectLoader('ansible.builtin.test', 'path')

    loader = _AnsibleInternalRedirectLoader('ansible.builtin.unit', 'path')
    assert loader._redirect == "ansible.builtin._unit"

# This loader only answers for intercepted Ansible Python modules. Normal imports will fail here and be picked up later
# by our path_hook importer (which proxies the built-in import mechanisms, allowing normal caching etc to occur)

# Generated at 2022-06-13 15:54:37.002445
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():

    # init _AnsibleCollectionPkgLoader with data
    collection_name = "ansible.builtin"
    path_list = [sys.exec_prefix, os.path.join(sys.exec_prefix, 'lib')]

    loader = _AnsibleCollectionPkgLoader(collection_name, path_list)

    # mock load_module
    loader.load_module = MagicMock(name='load_module')
    module = loader.load_module(collection_name)

    # check result
    assert module is None

# Generated at 2022-06-13 15:54:47.387971
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    assert _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name='this_is_a_leaf', path='/this/is/a/path') == (None, None)
    assert _AnsibleCollectionPkgLoaderBase.get_code(fullname='this_is_a_fullname') == None
    assert _AnsibleCollectionPkgLoaderBase.get_data(path='this_is_a_path') == None
    assert _AnsibleCollectionPkgLoaderBase.get_filename(fullname='this_is_a_fullname') == None
    assert _AnsibleCollectionPkgLoaderBase.get_source(fullname='this_is_a_fullname') == None

# Generated at 2022-06-13 15:54:58.467224
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    _AnsiblePathHookFinder_find_module_opts = {
        'ansible.module_utils.basic': None,
        'ansible.module_utils.common.config': None,
        'ansible_collections.not_found.missing': None,
        'ansible_collections.not_found.missing.plugins.module_utils.basic': None,
    }
    for f_name, v in _AnsiblePathHookFinder_find_module_opts.items():
        # Setup
        collection_finder = None
        pathctx = './ansible/'

        # Test
        if not v:
            v = _AnsiblePathHookFinder(collection_finder, pathctx)
            v = v.find_module(f_name)

        # Verify
        assert v is None

# Generated at 2022-06-13 15:55:06.004698
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    '''
    Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
    '''
    # pylint: disable=unused-variable

    # FUTURE: we'd like to have a good test case for this, but the path
    # mechanism makes it hard to test this method. This is just "dim lights"
    # to remind us to look at this again.
    pass


# Generated at 2022-06-13 15:56:06.074015
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    for plugin_dir in PluginLoader.plugin_loaders:
        plugin_type = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_dir)
        assert plugin_type in AnsibleCollectionRef.VALID_REF_TYPES, '%s is not a valid collection ref_type' % plugin_type
        assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_type) == plugin_type


# Generated at 2022-06-13 15:56:09.609343
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    _AnsiblePathHookFinder.find_module("ansible.module_utils")
    _AnsiblePathHookFinder.find_module("ansible_collections.ns.coll.module_utils")


# Generated at 2022-06-13 15:56:21.284243
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # Valid collection names
    ref = AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module')
    assert ref.collection == 'ns.coll'
    assert ref.subdirs == ''
    assert ref.resource == 'resource'
    assert ref.ref_type == 'module'
    assert ref.fqcr == 'ns.coll.resource'
    assert ref.n_python_collection_package_name == 'ansible_collections.ns.coll'
    assert ref.n_python_package_name == 'ansible_collections.ns.coll.plugins.module'

    ref = AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.subdir2.resource', 'action')
    assert ref.collection == 'ns.coll'

# Generated at 2022-06-13 15:56:29.760482
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert not AnsibleCollectionRef.is_valid_fqcr(None)
    assert not AnsibleCollectionRef.is_valid_fqcr('')
    assert not AnsibleCollectionRef.is_valid_fqcr('collection')
    assert not AnsibleCollectionRef.is_valid_fqcr('collection.resource')
    assert not AnsibleCollectionRef.is_valid_fqcr('collection..resource')
    assert not AnsibleCollectionRef.is_valid_fqcr('collection.subdir.resource')

    assert AnsibleCollectionRef.is_valid_fqcr('namespace.collection.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('namespace.collection.subdir.resource')

# Generated at 2022-06-13 15:56:39.013515
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # args = [fullname]
    # kwargs = None
    # configure mock for loader
    ansible_collections_ns = setup_loader_mock('ansible_collections', 'ns')
    mock_to_setup = {'find_module': get_find_module_mock(ansible_collections_ns, 'ns.has_code_file')}
    setup_loader_mock('ansible_collections.ns.has_code_file', 'thing.py', **mock_to_setup)

    test_loader = AnsibleCollectionSyntheticModuleLoader('ansible_collections.ns.has_code_file')
    assert test_loader.load_module('ansible_collections.ns.has_code_file') == ansible_collections_ns.has_code_file

# Unit test

# Generated at 2022-06-13 15:56:46.809570
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():

    class _AnsibleSyntheticCollectionPkgLoader(_AnsibleCollectionPkgLoaderBase):
        _allows_package_code = True
        def _get_candidate_paths(self, path_list):
            return [os.path.join(p, self._package_to_load) for p in path_list]

        def _get_subpackage_search_paths(self, candidate_paths):
            return [p for p in candidate_paths if os.path.isdir(to_bytes(p))]


    class _AnsibleSyntheticCollectionPkgLoaderNoSubpackages(_AnsibleCollectionPkgLoaderBase):
        _allows_package_code = True

# Generated at 2022-06-13 15:56:51.603552
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c', 'module')
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c', 'some_random_type')
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c.d.e', 'module')
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c.d.e', 'some_random_type')
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c', 'role')
    assert None == AnsibleCollectionRef.try_parse_fqcr('a.b.c.d.e', 'role')

# Generated at 2022-06-13 15:57:01.618037
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader(['ansible', 'fakecollection', 'fakeplugin'],
                                         candidate_paths=['/path/to/ansible_collections/ansible/fakecollection/fakeplugin'])
    class FakeModule(object):
        _collection_meta = {}
    module = FakeModule()

    with mock.patch('ansible.utils.collection_loader._meta_yml_to_dict', return_value={}):
        with mock.patch('ansible.utils.collection_loader.AnsibleCollectionConfig.on_collection_load') as mock_on_collection_load:
            with mock.patch('ansible.utils.collection_loader._AnsibleCollectionPkgLoader.load_module', return_value=module):
                loader.load_module('ansible.fakecollection.fakeplugin')
               

# Generated at 2022-06-13 15:57:13.009965
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ansible_collections_paths = [os.path.join(os.path.dirname(__file__), 'data', 'collection_loader_modules')]
    os.environ[ANSIBLE_COLLECTIONS_PATHS] = ':'.join(ansible_collections_paths)
    # Test __init__
    test_inputs = {
        'collection_name': 'ansible.python_collection',
        'subdirs': '',
        'resource': 'python_module',
        'ref_type': 'module'
    }
    acr_result = AnsibleCollectionRef(**test_inputs)

# Generated at 2022-06-13 15:57:20.081493
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    expected_result_1 = ('stdlib.sys', 'stdlib.sys')
    expected_result_2 = ('ansible.utils.collection_loader', 'ansible.utils.collection_loader')

    from ansible.utils.collection_loader import get_collection_list
    from ansible.errors import AnsibleError

    _AnsibleCollectionConfig.COLLECTIONS_PATHS = []
    _AnsibleCollectionConfig.COLLECTIONS_PATHS.append(
        '/home/vcap/pcf-release-13/ansible_release-dir/src/ansible-2.10.3/test/unit/utils/collection_loader/test_data/ansible_collections/my_namespace/my_collection_1'
    )
