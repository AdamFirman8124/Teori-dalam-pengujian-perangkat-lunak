

# Generated at 2022-06-13 15:50:15.575225
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    import ansible.module_utils

    # Create a _AnsibleCollectionFinder instance
    ansible_collection_finder = _AnsibleCollectionFinder()
    assert ansible_collection_finder._ansible_pkg_path == to_native(os.path.dirname(os.path.abspath(ansible.module_utils.__file__)))
    assert ansible_collection_finder._n_configured_paths == []
    assert ansible_collection_finder._n_cached_collection_paths is None
    assert ansible_collection_finder._n_cached_collection_qualified_paths is None
    assert ansible_collection_finder._n_playbook_paths == []


# Generated at 2022-06-13 15:50:25.750045
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    finder = _AnsibleCollectionFinder()
    finder._install()
    finder.set_playbook_paths('/usr/local/lib/ansible/collections')

    pathfinder = _AnsiblePathHookFinder(finder, '/usr/local/lib/ansible/collections')
    module_loader = pathfinder.find_module('ansible.module_utils.ansible_freebsd_pkgng_utils')
    assert isinstance(module_loader, _AnsibleCollectionLoader)


# Attempts to emulate the _path_hook variant of this class, allowing us to emulate a path-based loader in meta_path
# This can be removed if we later refactor the meta_path code to directly return a loader instead of delegating to
# find_module.

# Generated at 2022-06-13 15:50:34.032342
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from ansible.module_utils.common.collections import _AnsibleCollectionFinder
    from ansible.module_utils.common.collections import _AnsibleCollectionLoader
    fullname = 'ansible_collections.ns.coll'
    path = 'path'
    collection_finder = _AnsibleCollectionFinder()
    collection_loader = _AnsibleCollectionLoader(fullname=fullname, path_list=path)
    assert collection_loader == collection_finder.find_module(fullname=fullname, path=path)


# Generated at 2022-06-13 15:50:42.774849
# Unit test for constructor of class _AnsibleCollectionRootPkgLoader
def test__AnsibleCollectionRootPkgLoader():
    l = _AnsibleCollectionRootPkgLoader('ansible_collections', path_list=['/path', '/path2'])
    assert l._fullname == 'ansible_collections'
    assert l._redirect_module is None
    assert l._split_name == ['ansible_collections']
    assert l._rpart_name == ('', '', 'ansible_collections')
    assert l._parent_package_name == ''
    assert l._package_to_load == 'ansible_collections'
    assert l._source_code_path is None
    assert l._decoded_source is None
    assert l._compiled_code is None
    assert l._candidate_paths == ['/path/ansible_collections', '/path2/ansible_collections']
    assert l._subpackage_search

# Generated at 2022-06-13 15:50:48.959139
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # Case: normal
    try_parse = AnsibleCollectionRef.try_parse_fqcr('ns1.coll1', 'module')
    assert try_parse

    # Case: ref_type is invalid
    with pytest.raises(ValueError):
        AnsibleCollectionRef.try_parse_fqcr('ns1.coll1.mod1', 'invalid')

    # Case: ref_type is not specified
    try_parse = AnsibleCollectionRef.try_parse_fqcr('ns1.coll1.mod1')
    assert try_parse

    # Case: collection name is invalid
    with pytest.raises(ValueError):
        AnsibleCollectionRef.try_parse_fqcr('ns1.coll1.1mod1')

    # Case: ref is invalid

# Generated at 2022-06-13 15:50:53.976135
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('vars_plugins') == 'vars'


# Generated at 2022-06-13 15:50:58.507985
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    init_path = '/home/init_path/__init__.py'
    loader = _AnsibleCollectionPkgLoader(None, 'my_collections', ['my_collections'])
    loader._source_code_path = init_path
    loader._redirect_module = True
    module = loader.load_module('my_collections')
    assert module == loader._redirect_module


# Generated at 2022-06-13 15:51:10.485811
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ansible_collection_ref = AnsibleCollectionRef('namespace.collectionname', None, 'resource', 'module')
    assert ansible_collection_ref.collection == 'namespace.collectionname'
    assert ansible_collection_ref.subdirs == ''
    assert ansible_collection_ref.resource == 'resource'
    assert ansible_collection_ref.ref_type == 'module'
    assert ansible_collection_ref.n_python_collection_package_name == 'ansible_collections.namespace.collectionname'
    assert ansible_collection_ref.n_python_package_name == 'ansible_collections.namespace.collectionname.plugins.module'
    assert ansible_collection_ref.fqcr == 'namespace.collectionname.resource'


# Generated at 2022-06-13 15:51:18.816779
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    with tempfile.TemporaryDirectory() as test_dir:
        test_file = os.path.join(test_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test_data')

        loader = AnsibleCollectionPkgLoader(None, [])
        result = loader.get_data(test_file)
        assert result == b'test_data'

        result = loader.get_data(test_file + '_not_existing')
        assert result is None



# Generated at 2022-06-13 15:51:25.768009
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # Setup test environment (Fixture)
    test_object = AnsibleCollectionRef("", "", "", "")

    input_ref = "foo.bar"
    input_ref_type = "action"

    test_object.try_parse_fqcr(input_ref, input_ref_type)

    assert True


# Generated at 2022-06-13 15:52:10.578114
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    mock_fullname = 'ansible.collections.ansible.plugins.module_utils.logstash'
    mock_subpackage_search_paths = None
    mock_source_code_path = None

    ldr = _AnsibleCollectionPkgLoaderBase(mock_fullname)
    ldr._subpackage_search_paths = mock_subpackage_search_paths
    ldr._source_code_path = mock_source_code_path

    actual__is_package_output = ldr.is_package('ansible.collections.ansible.plugins.module_utils.logstash')
    assert actual__is_package_output == False



# Generated at 2022-06-13 15:52:19.570060
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    mock_data = {}
    # Inspecting _AnsibleCollectionPkgLoaderBase.get_data method type
    assert isinstance(_AnsibleCollectionPkgLoaderBase.get_data, types.MethodType)
    # Inspecting _AnsibleCollectionPkgLoaderBase.get_data method return type
    assert isinstance(_AnsibleCollectionPkgLoaderBase.get_data(None, None), bytes)
    # Inspecting _AnsibleCollectionPkgLoaderBase.get_data method exception type
    # Testing _AnsibleCollectionPkgLoaderBase.get_data method with source code path
    collection_list = [Path('/usr/share/ansible_collections/ansible/test')]
    loader = _AnsibleCollectionPkgLoaderBase('ansible.test', path_list=collection_list)
    assert loader.get_

# Generated at 2022-06-13 15:52:30.074303
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:52:36.567054
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('httpapi_plugins') == 'httpapi'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('inventory_plugins') == 'inventory'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:52:46.649305
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoaderBase

    loader = _AnsibleCollectionPkgLoaderBase('ns.subpackage', ['my/path'])
    loader._subpackage_search_paths = ['my/path']
    assert loader.is_package('ns.subpackage')

    loader = _AnsibleCollectionPkgLoaderBase('ns.subpackage', ['my/path'])
    loader._source_code_path = 'my/path/subpackage.py'
    assert not loader.is_package('ns.subpackage')

    loader = _AnsibleCollectionPkgLoaderBase('ns.subpackage', ['my/path'])
    loader._redirect_module = 'a'
    assert not loader.is_package('ns.subpackage')



# Generated at 2022-06-13 15:52:51.638933
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll', 'module') == None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'role') == None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'module') == AnsibleCollectionRef('ns.coll', '', 'resource', 'module')
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir1.subdir2.resource', 'module') == AnsibleCollectionRef('ns.coll', 'subdir1.subdir2', 'resource', 'module')
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.rolename', 'role') == AnsibleCollectionRef('ns.coll', '', 'rolename', 'role')
   

# Generated at 2022-06-13 15:52:56.217345
# Unit test for method is_valid_collection_name of class AnsibleCollectionRef

# Generated at 2022-06-13 15:53:03.844025
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    '''
    Unit tests for find_module method of class _AnsibleCollectionFinder
    '''
    # Test if exception is raised when path is not provided for
    # a subpackage but trying to find it (issue #67944).
    # Create _AnsibleCollectionFinder object
    c1 = _AnsibleCollectionFinder()
    # Test if exception is raised
    with pytest.raises(ValueError) as error:
        c1.find_module('ansible.plugins.action')
    # Assert if exception is raised
    assert 'path must be specified' in to_text(error.value)

    # Test if error is raised and none is returned when top level package
    # to the module is not ansible or ansible_collections (issue #67944).
    # Create _AnsibleCollectionFinder object
   

# Generated at 2022-06-13 15:53:16.329544
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():

    from importlib import import_module

    from ansible.import_plugins.module_utils.basic import AnsibleModule

    from ansible.utils.collection_loader import _AnsibleInternalRedirectLoader, _get_collection_metadata, _nested_dict_get

    _get_collection_metadata = lambda collection_name: {'import_redirection':{
        'ansible.builtin.posix.pwd':{'redirect':'ansible.module_utils.basic.pwd'}}}[collection_name]
    _nested_dict_get = lambda d, keys: d['import_redirection'][keys[1]]

    redirect = _AnsibleInternalRedirectLoader(fullname='ansible.builtin.posix.pwd', path_list=[])


# Generated at 2022-06-13 15:53:17.021097
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    pass

# Generated at 2022-06-13 15:53:53.015354
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr(u'a.b.c.d', u'module').fqcr == u'a.b.c.d'
    assert AnsibleCollectionRef.from_fqcr(u'a.b.c.d.e', u'module').fqcr == u'a.b.c.d.e'
    assert AnsibleCollectionRef.from_fqcr(u'a.b.c.d.e', u'module').n_python_package_name == 'ansible_collections.a.b.plugins.c.d'
    assert AnsibleCollectionRef.from_fqcr(u'a.b.c.d.e', u'module').n_python_collection_package_name == 'ansible_collections.a.b'
   

# Generated at 2022-06-13 15:54:01.711751
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    module_name = os.path.join(os.path.dirname(__file__), 'mock_loader_source.py')
    with open(module_name, 'rb') as f:
        module_source = f.read()
    with open(module_name, 'r') as f:
        module_source_utf8 = f.read()
    loader = _AnsibleCollectionPkgLoaderBase(__name__)
    loader._source_code_path = module_name
    assert loader.get_source(__name__) == module_source_utf8
    assert loader._decoded_source == module_source_utf8



# Generated at 2022-06-13 15:54:08.539019
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from ansible import __version__
    from ansible.utils.unsafe_proxy import wrap_var

    # Construct an instance of _AnsibleInternalRedirectLoader
    airdl_instance = _AnsibleInternalRedirectLoader('ansible', None)

    # Test load_module method
    assert airdl_instance.load_module('copy') is not None
    assert airdl_instance.load_module('template') is not None
    assert airdl_instance.load_module('ansible', None) is not None
    assert airdl_instance.load_module('__version__') is wrap_var(__version__)


# FIXME: this is not a real importer, and we can't safely cache in sys.modules

# Generated at 2022-06-13 15:54:19.035426
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr(u'ns.mycoll', u'module').fqcr == u'ns.mycoll'
    assert AnsibleCollectionRef.from_fqcr(u'ns.mycoll.subdir1.subdir2', u'module').fqcr == u'ns.mycoll.subdir1.subdir2'
    assert AnsibleCollectionRef.from_fqcr(u'ns.mycoll.myrole', u'role').fqcr == u'ns.mycoll.myrole'
    assert AnsibleCollectionRef.from_fqcr(u'ns.mycoll.myrole.yaml', u'role').fqcr == u'ns.mycoll.myrole.yaml'

# Generated at 2022-06-13 15:54:21.672724
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    assert AnsibleCollectionRef("ansible.builtin", "subdir1.subdir2", "mymodule", "module").__repr__() == "AnsibleCollectionRef(collection='ansible.builtin', subdirs='subdir1.subdir2', resource='mymodule')"



# Generated at 2022-06-13 15:54:25.636527
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    assert(_AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ansible_namespace.my_collection.my_module',
                                                path_list=['/path/to/module/dir']).get_filename('ansible_collections.ansible_namespace.my_collection.my_module') == '/path/to/module/dir/my_module.py')

# Generated at 2022-06-13 15:54:36.529422
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # Positive testing:
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir

# Generated at 2022-06-13 15:54:47.319871
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.somens")
    loader._redirect_module = object()
    loader.load_module("ansible_collections.somens")
    assert sys.modules["ansible_collections.somens"] == loader._redirect_module

    # Load module successfully
    assert sys.modules.pop("ansible_collections.somens", None) is None
    assert "ansible_collections.somens" not in sys.modules
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.somens")
    loader._subpackage_search_paths = []
    loader._source_code_path = None

# Generated at 2022-06-13 15:54:58.384109
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # This is a unit test for method get_source of class
    # _AnsibleCollectionPkgLoaderBase. These tests use the module
    # ansible_collections.test.test_collections.test_ns.sub1.subsub1
    # as a sample.
    loader = _AnsibleCollectionPkgLoaderBase.__new__(_AnsibleCollectionPkgLoaderBase)

    # Setup some values for the loader
    loader._fullname = 'ansible_collections.test.test_collections.test_ns.sub1.subsub1'
    loader._redirect_module = None

    loader._split_name = 'ansible_collections.test.test_collections.test_ns.sub1.subsub1'.split('.')

# Generated at 2022-06-13 15:55:10.571749
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import pytest
    from pathlib import Path
    import collections
    import ansible

    # Create a mock for class _AnsiblePathHookFinder
    mock_collection_finder = _AnsibleCollectionFinder()
    # test path
    mock_path = Path(__file__).parent.joinpath('ansible_collections/test_namespace/test_collection')
    mock_fullname = 'ansible_collections.test_namespace.test_collection.plugins.module_utils.test_module'
    mock_fullname_no_coll = 'ansible_collections.test_namespace.plugins.module_utils.test_module'
    mock_fullname_no_coll_no_nsp = 'ansible_collections.plugins.module_utils.test_module'

    # Test case 1: the full module

# Generated at 2022-06-13 15:55:45.256786
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    '''Unit tests for the find_module method of the _AnsibleCollectionFinder class'''
    import os
    import sys

    # Prepare test data for normal case
    expected_class = "_AnsibleCollectionFinder" # the expected class returned by find_module()
    expected_value_fullname = "ansible_collections.testns.testcoll.testmodule"
    expected_value_path = [] # this value is not used by the find_module() method
    expected_return_value = expected_class

    os.environ['ANSIBLE_COLLECTIONS_PATH'] = '/home/ansible/ansible_collections:/home/ansible/ansible_collections_extra'
    collection_finder = _AnsibleCollectionFinder()

# Generated at 2022-06-13 15:55:46.630537
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('not.ansible', None)



# Generated at 2022-06-13 15:55:51.278288
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    import mock

    with mock.patch.object(_AnsibleCollectionPkgLoaderBase, 'get_source') as mock_get_source, \
         mock.patch('ansible_collections.ansible.plugins.module_utils.common.compile') as mock_compile:
        mock_source = 'test source code'
        mock_get_source.return_value = mock_source
        mock_compiled = b'test compiled code'
        mock_compile.return_value = mock_compiled
        _A = _AnsibleCollectionPkgLoaderBase('test.name', None)
        _A._fullname = 'test.name'
        _A._source_code_path = 'test_source_code_path'
        _A._compiled_code = None

# Generated at 2022-06-13 15:56:01.046925
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    '''
    Test loading a package using a _AnsibleCollectionPkgLoaderBase object
    '''
    path_list = ['/tmp/path_list']
    fullname = 'ansible_collections.connor_test.c_test'
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list=path_list)

    # Get the path where the code is installed
    source_code = loader.get_source(fullname)
    if source_code is None:
        source_code = '/tmp/ansible/ansible_collections/connor_test/c_test/__init__.py'
        module_source_code = '/tmp/ansible/ansible_collections/connor_test/c_test/c_test.py'
    else:
        source_code = loader

# Generated at 2022-06-13 15:56:04.525888
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    fullname = "namespace.collection.subpackage"
    l = _AnsibleCollectionPkgLoaderBase(fullname)
    assert False == l.is_package(fullname)
    assert True  == l.is_package("namespace.collection")


# Generated at 2022-06-13 15:56:09.428041
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.ns.new_namespace")
    loader._subpackage_search_paths=[
        '/path/to/collection/new_namespace'
    ]
    loader.get_data("/path/to/collection/new_namespace/module.py")
    # TODO


# Generated at 2022-06-13 15:56:21.107025
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    l = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test-collection')
    path1 = '/tmp/test-collection1'
    path2 = '/tmp/test-collection2'
    path3 = '/tmp/test-collection3'
    path4 = '/tmp/test-collection4'
    path5 = '/tmp/test-collection5/__init__.py'
    path6 = '/tmp/test-collection6/__init__.py'
    path7 = '/tmp/test-collection7/__init__.py'
    path8 = '/tmp/test-collection8/__init__.py'
    path9 = '/tmp/test-collection9/__init__.py'
    path10 = '/tmp/test-collection10/__init__.py'

# Generated at 2022-06-13 15:56:23.900596
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    import ansible.utils.collection_loader
    ansible.utils.collection_loader._meta_yml_to_dict = meta_yml_to_dict


# handle loading of modules/packages in a collection package

# Generated at 2022-06-13 15:56:28.225186
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    test_obj = AnsibleCollectionRef(collection_name="namespace.collection", subdirs='subdir1.subdir2', resource="resource", ref_type="ref_type")
    assert repr(test_obj) == "AnsibleCollectionRef(collection='namespace.collection', subdirs='subdir1.subdir2', resource='resource')"



# Generated at 2022-06-13 15:56:38.465050
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    source_code_path = b"/home/yannick/CLionProjects/ansible_collection_loader/tests/data/ansible_collections/my_namespace/my_collection/roles"
    subpackage_search_paths = [source_code_path]
    fullname = "ansible_collections.my_namespace.my_collection.roles"
    filename = "/home/yannick/CLionProjects/ansible_collection_loader/tests/data/ansible_collections/my_namespace/my_collection/roles/__synthetic__"

# Generated at 2022-06-13 15:57:56.617425
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    import unittest

    class AnsibleCollectionRefTestCase(unittest.TestCase):
        def test_valid_collection_name(self):
            # Valid collection name
            test_name_1 = u'ns.collname'
            # Invalid collection name
            test_name_2 = u'ns.coll.name'
            # Invalid collection name
            test_name_3 = u'ns..collname'
            # Invalid collection name
            test_name_4 = u'ns.collname.'
            # Invalid collection name
            test_name_5 = u'ns.collname_'
            # Invalid collection name
            test_name_6 = u'ns.coll@name'
            self.assertTrue(AnsibleCollectionRef.is_valid_collection_name(test_name_1))

# Generated at 2022-06-13 15:58:03.014022
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    class _AnsibleCollectionPkgLoaderBase_mock(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname, path_list=None):
            super().__init__(fullname, path_list=path_list)

        def _get_candidate_paths(self, path_list):
            return path_list

        def _get_subpackage_search_paths(self, candidate_paths):
            return candidate_paths

    # test empty path
    loader = _AnsibleCollectionPkgLoaderBase_mock(fullname="ansible_collections.test.test_paths", path_list=[])
    assert loader.get_data(path="/tmp/test.py") is None

    # test missing file

# Generated at 2022-06-13 15:58:12.798647
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    rfc = AnsibleCollectionRef.from_fqcr

# Generated at 2022-06-13 15:58:19.489206
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import copy
    import types
    import pkgutil
    import ansible.module_utils.six as six

    import ansible_collections.foo.bar
    from ansible_collections.foo.bar.plugins import test_module
    from ansible_collections.foo.bar.plugins.module_utils import test_module_utils
    from ansible_collections.foo.bar.plugins.module_utils import test_multi_shared_module_utils
    from ansible_collections.foo.bar.plugins.module_utils.other_tests import test_multi_shared_module_utils2
    from ansible_collections.foo.bar.plugins.module_utils.custom_collection_ns.test_nested_multi_ns_module_utils import point

    # Set up env

# Generated at 2022-06-13 15:58:28.246871
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # test for a loader with empty search paths and no source code path
    f1 = _AnsibleCollectionPkgLoaderBase(fullname='ansible.modules.test', path_list=[])
    assert f1.get_filename('ansible.modules.test') == None

    # test for a loader with search paths and no source code path
    f2 = _AnsibleCollectionPkgLoaderBase(fullname='ansible.modules.test', path_list=['/path/to/ansible', '/path/to/ansible2'])
    assert f2.get_filename('ansible.modules.test') == '<ansible_synthetic_collection_package>'
    f2._source_code_path = '/path/to/code'

# Generated at 2022-06-13 15:58:30.358294
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    # TODO: we need to write unit tests for _AnsibleInternalRedirectLoader
    assert False


# implements the actual find_module/load_module API

# Generated at 2022-06-13 15:58:37.401689
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    fake_path_list = [
        '/Users/my_user/.ansible/collections/ansible_collections/foobar/fake',
    ]
    fake_fullname = 'ansible_collections.foobar.fake'
    ansible_collections_pkg_loader = _AnsibleCollectionPkgLoaderBase(fake_fullname, fake_path_list)
    expected = '_AnsibleCollectionPkgLoaderBase(path=[\'/Users/my_user/.ansible/collections/ansible_collections/foobar/fake/fake\'])'
    assert repr(ansible_collections_pkg_loader) == expected



# Generated at 2022-06-13 15:58:43.789351
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr("ansible.builtin.ping", "module").fqcr == "ansible.builtin.ping"
    assert AnsibleCollectionRef.from_fqcr("ansible.builtin.ping", "module").n_python_collection_package_name == "ansible_collections.ansible.builtin"
    assert AnsibleCollectionRef.from_fqcr("ansible.builtin.ping", "module").n_python_package_name == "ansible_collections.ansible.builtin.plugins.modules.ping"
    assert AnsibleCollectionRef.from_fqcr("ansible_collections.ns.coll.resource", "module").fqcr == "ns.coll.resource"

# Generated at 2022-06-13 15:58:53.237050
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    import ansible.utils.collection_loader
    class _AnsibleInternalRedirectLoader:
        def __init__(self, fullname, path_list):
            pass
        def load_module(self, fullname):
            # since we're delegating to other loaders, this should only be called for internal redirects where we answered
            # find_module with this loader, in which case we'll just directly import the redirection target, insert it into
            # sys.modules under the name it was requested by, and return the original module.
            # should never see this
            import sys
            if not self._redirect:
                raise ValueError('no redirect found for {0}'.format(fullname))
            # FIXME: smuggle redirection context, provide warning/error that we tried and failed to redirect
            mod = import_module(self._redirect)

# Generated at 2022-06-13 15:58:57.284117
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    fullname='ansible.module_utils.basic'

    with pytest.raises(Exception) as execinfo:
        assert _AnsibleInternalRedirectLoader(fullname, '')