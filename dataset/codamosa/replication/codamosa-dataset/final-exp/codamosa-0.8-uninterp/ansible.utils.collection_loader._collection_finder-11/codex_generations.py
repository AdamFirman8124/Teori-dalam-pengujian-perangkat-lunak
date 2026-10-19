

# Generated at 2022-06-13 15:51:03.834115
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    _AnsibleInternalRedirectLoader('ansible.plugins.inventory.foo', None)


# Generated at 2022-06-13 15:51:16.250181
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import os
    import sys
    import pkgutil
    import importlib
    import ansible_galaxy
    import ansible.module_utils
    import ansible.module_utils.urls

    # create a package loader and get source
    # get_source() of loader is going to get the source code of a module
    # that's not a package, in a collection

    # create package loader
    is_top_level = 'ansible' not in sys.modules
    # get module from path
    collection_module = pkgutil.get_loader('ansible.module_utils.urls')
    # verify module
    assert(collection_module is not None)
    # get module path
    module_path = collection_module.get_filename('ansible.module_utils.urls')
    # verify module path

# Generated at 2022-06-13 15:51:18.249653
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    """Test case for '__repr__' of class 'AnsibleCollectionRef'."""
    ansible_collection_ref = AnsibleCollectionRef("collection", "", "mymodule", "module")
    assert repr(ansible_collection_ref) == "AnsibleCollectionRef(collection='collection', subdirs='', resource='mymodule')"


# Generated at 2022-06-13 15:51:19.507096
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    pass


# Generated at 2022-06-13 15:51:28.480305
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # __init__()
    full_name = 'ansible_collections.test.test_plugins'
    path_list = ['/usr/share/ansible/collections']
    loader = _AnsibleCollectionPkgLoaderBase(
        fullname=full_name,
        path_list=path_list,
    )
    # get_filename()
    result = loader.get_filename(full_name)
    # assert
    assert type(result) is str



# Generated at 2022-06-13 15:51:35.600787
# Unit test for constructor of class _AnsibleCollectionRootPkgLoader
def test__AnsibleCollectionRootPkgLoader():
    try:
        _AnsibleCollectionRootPkgLoader(fullname='foo', path_list=[b'/tmp'])
    except ImportError:
        return
    assert False

    try:
        _AnsibleCollectionRootPkgLoader(fullname='ansible_collections.foo', path_list=[b'/tmp'])
    except ImportError:
        return
    assert False

    _AnsibleCollectionRootPkgLoader(fullname='ansible_collections', path_list=[b'/tmp'])
    return



# Generated at 2022-06-13 15:51:36.025708
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    pass

# Generated at 2022-06-13 15:51:47.475196
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # Prepare a loader
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.mynamespace.mycollection.mymodule', ['/path/to/a/collection/file'])
    assert 'ansible_collections.mynamespace.mycollection.mymodule' == loader._fullname
    assert 'ansible_collections' == loader._split_name[0]
    assert 'mynamespace' == loader._split_name[1]
    assert 'mycollection' == loader._split_name[2]
    assert 'mymodule' == loader._split_name[3]
    assert 'ansible_collections.mynamespace.mycollection' == loader._parent_package_name
    assert 'mymodule' == loader._package_to_load
    assert ['/path/to/a/collection/file/mymodule']

# Generated at 2022-06-13 15:51:58.344823
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():

    # Monkey patch load_module to avoid exception/output of real code in load_module
    # This also allows testing of code not executed during regular program execution
    class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
        def load_module(self, fullname):

            module = super(MockAnsibleCollectionPkgLoader, self).load_module(fullname)

            # ===================
            # Code to be unit tested
            module._collection_meta = {'a': 1}
            import ansible

            if 'ansible.builtin' == '.'.join(self._split_name[1:3]):
                ansible_pkg_path = os.path.dirname(ansible.__file__)

# Generated at 2022-06-13 15:52:01.598702
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    loader = _AnsibleCollectionPkgLoaderBase('test', path_list=['/test'])
    loader.get_data('/test/test')




# Generated at 2022-06-13 15:52:33.384557
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from ansible.utils.collection_loader import _AnsibleCollectionFinder
    from ansible.parsing.utils.import_module import import_module
    import os
    import tempfile
    try:
        path_tmp = tempfile.mkdtemp()
        with open(os.path.join(path_tmp, '__init__.py'), 'w') as fp:
            fp.write("""#!/usr/bin/python
import os
import tempfile
""")
        os.chmod(os.path.join(path_tmp, '__init__.py'), 0o755)
        sys.path.append(path_tmp)
        assert None ==  import_module(path_tmp)
    finally:
        sys.path.remove(path_tmp)

# Generated at 2022-06-13 15:52:41.562710
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    my_loader = _AnsibleInternalRedirectLoader('ansible.module_utils.module_runner', [])
    # FIXME: use some other way to import module runner
    mod = my_loader.load_module('ansible.module_utils.module_runner')
    assert mod

# implements the path_hook() importer protocol function. Registers a custom finder and loader for ansible_collections,
# and adds the custom finder to sys.meta_path to catch all ansible_collections imports.

# Generated at 2022-06-13 15:52:42.326002
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    finder = _AnsibleCollectionFinder()
    assert finder is not None



# Generated at 2022-06-13 15:52:44.465907
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    test_data = {
        '__init__.py': '''
#!/usr/bin/python
fruits = "Apple"
''',
        '__synthetic__': '''
#!/usr/bin/python
fruits = "Apple"
'''
    }

    not_executable_test_d

# Generated at 2022-06-13 15:52:49.070709
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():

    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.module_utils.foo', None)

    # NOTE: we don't have a mock of the builtin metadata here, so we'll receive
    # ImportError when it calls _get_collection_metadata for 'ansible.builtin'
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.builtin.foo', None)


# Implements the import hook for collection-qualified imports.
# see https://www.python.org/dev/peps/pep-0302/#id3 for the expected API.
# PEP 302 says the importer must be a class so we make it a class even though its not a very complicated object
# Also, we make the importer a "factory" that returns a new

# Generated at 2022-06-13 15:52:59.759529
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    # test _AnsiblePathHookFinder.__init__
    def _test_init(path_hook_finder, pathctx): # type: (_AnsiblePathHookFinder, str) -> None
        assert path_hook_finder._pathctx == os.path.normpath(pathctx)
    _test_init(_AnsiblePathHookFinder(_AnsibleCollectionFinder(), 'a/b/c'), 'a/b/c')
    _test_init(_AnsiblePathHookFinder(_AnsibleCollectionFinder(), 'a/b/c/'), 'a/b/c')
    _test_init(_AnsiblePathHookFinder(_AnsibleCollectionFinder(), 'a/b/c\\'), 'a/b/c')


# Implements a path based importer for ansible

# Generated at 2022-06-13 15:53:07.906131
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'module'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('modules') == 'module'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') == 'module_utils'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'

# Generated at 2022-06-13 15:53:20.725864
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # For the sake of unit test, we use an Ansible module full name
    # and a invalid module full name
    ans_fullname = 'ansible.utils.unsafe_proxy'
    invalid_fullname = 'ansible.utils.invalid_unsafe_proxy'
    collection_paths = [os.path.join(os.path.dirname(os.path.abspath(__file__))),
                        os.path.join(os.path.dirname(os.path.abspath(__file__)), '.tox/py36')]
    collection_finder = _AnsibleCollectionFinder(collection_paths)
    collection_finder._install()
    # Test for the an Ansible module full name

# Generated at 2022-06-13 15:53:22.242928
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    loader = _AnsibleCollectionPkgLoaderBase('')
    print ('loader:', loader)



# Generated at 2022-06-13 15:53:28.942946
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    collection_name = 'Collection'
    subdirs = 'subdir1'
    resource = 'resource'
    ref_type = 'module'

    test_object = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

    expected_result = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

    result = test_object.__repr__()
    assert result == expected_result



# Generated at 2022-06-13 15:54:25.179008
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    """
    Ensure that load_module of class _AnsibleInternalRedirectLoader works as expected
    """
    # function to test import_module and sys.modules, in order to avoid changing it.
    def import_module(name):
        # Check if name is already in sys.modules, if not then raise an exception
        if name in sys.modules:
            return sys.modules[name]
        else:
            raise ModuleNotFoundError
    # function to test nested_dict_get by splitting the name.
    def _nested_dict_get(dict_value, key_list):
        if not isinstance(key_list, list):
            raise TypeError('type must be list')
        if not key_list:
            raise ValueError('key_list must not be empty')

# Generated at 2022-06-13 15:54:36.454650
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():

    acr = AnsibleCollectionRef.from_fqcr('namespace.collection.resource', ref_type='module')
    assert acr.__repr__() == 'AnsibleCollectionRef(collection=\'namespace.collection\', subdirs=\'\', resource=\'resource\')'

    acr = AnsibleCollectionRef.from_fqcr('namespace.collection.subdir1.resource', ref_type='module')
    assert acr.__repr__() == 'AnsibleCollectionRef(collection=\'namespace.collection\', subdirs=\'subdir1\', resource=\'resource\')'

    acr = AnsibleCollectionRef.from_fqcr('namespace.collection.subdir1.subdir2.resource', ref_type='module')

# Generated at 2022-06-13 15:54:46.358720
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    base_path = os.path.join(os.getcwd(), 'tests/sanity/collection/collection_fixtures/ansible_namespace/')
    base_path_other = os.path.join(os.getcwd(), 'tests/sanity/collection/collection_fixtures/namespace_other/')
    collection_finder = _AnsibleCollectionFinder(paths=[base_path, base_path_other], scan_sys_paths=False)
    ansible_path_hook_finder = _AnsiblePathHookFinder(collection_finder, pathctx=base_path)
    assert ansible_path_hook_finder.find_module('module_b')



# Generated at 2022-06-13 15:54:57.324540
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    cls = _AnsibleCollectionPkgLoaderBase
    instance = cls('ansible_collections.ns.fullname', path_list=[to_text(os.path.join(FIXTURE_DIR, 'coll1', 'ns1', 'name1'))])
    results = instance.load_module('ansible_collections.ns.fullname')
    assert isinstance(results, ModuleType)
    assert results.__name__ == 'ansible_collections.ns.fullname'
    assert results.__file__ == '/Users/ansible/ansible_test/test/units/module_utils/test_collections/fixtures/coll1/ns1/name1/__synthetic__'
    assert results.__package__ == 'ansible_collections.ns'

# Generated at 2022-06-13 15:55:09.095799
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # 1. Test a toplevel collection path
    # 1.1. Test a module that exists in the path
    # 1.2. Test a module that doesn't exist in the path
    # 2. Test a subpackage path
    # 3. Test a submodule path
    # 4. Test a non-collections path

    collection_finder = _AnsibleCollectionFinder()
    # TODO: figure out how to test this
    collection_finder.find_module('ansible')
    collection_finder.find_module('ansible.module_utils')

    # TODO: test with invalid name
    # TODO: test find_module without path
    # TODO: test find_module with empty path


# Generated at 2022-06-13 15:55:12.063543
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    fqcr = AnsibleCollectionRef('mycoll.myresource', None, 'module', 'module')
    # str(fqcr) behavior is tested elsewhere, we're only testing repr() here
    assert repr(fqcr) == "AnsibleCollectionRef(collection='mycoll.myresource', subdirs='', resource='module')"
    assert str(fqcr) == 'mycoll.myresource.module'


# Generated at 2022-06-13 15:55:19.426935
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    """Unit test for method find_module of class _AnsiblePathHookFinder"""
    # New object from _AnsiblePathHookFinder class
    testObj = _AnsiblePathHookFinder([], [])
    # Check the module finder works fine
    assert testObj.find_module('ansible') is not None
    # Check Error if invalid module
    assert testObj.find_module('wrong.module') is None


# Generated at 2022-06-13 15:55:26.402852
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import unittest
    class MyTestCase(unittest.TestCase):
        def test__AnsiblePathHookFinder_find_module(self):
            # Test that find_module loads the module
            import ansible
            import ansible.plugins
            import ansible.module_utils.srt
            import ansible.module_utils.urls
            AnsiblePathHookFinder = ansible.module_utils.collection_loader._AnsiblePathHookFinder
            collection_finder = _AnsibleCollectionFinder()
            path_context = os.path.dirname(os.path.dirname(os.path.dirname(ansible.__file__)))
            ansible_path_hook_finder = AnsiblePathHookFinder(collection_finder, path_context)
            ansible_path_hook_

# Generated at 2022-06-13 15:55:36.794360
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("action_plugins") == "action"
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("cache_plugins") == "cache"
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("callback_plugins") == "callback"
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("cliconf_plugins") == "cliconf"
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("connection_plugins") == "connection"
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("library") == "modules"

# Generated at 2022-06-13 15:55:37.911451
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    assert True

# Generated at 2022-06-13 15:56:36.798975
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    test_full_name = 'ansible.module_utils.facts.system.network'
    _AnsibleInternalRedirectLoader(test_full_name, [])


# PEP302 loader to handle loading Ansible Python modules, via a small number of special redirections to the built-in
# collection (also known as the Ansible core distribution), and, when the requested module is not redirected, by
# delegating to the standard Python import system.

# Generated at 2022-06-13 15:56:45.230750
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    fqcrs = [
        u'collection',
        u'collection.resource',
        u'collection.subdir.resource',
        u'collection.subdir.subdir.resource',
        u'collection.subdir.subdir.subdir.resource',
        u'col.lection',
        u'col.lection.resource',
        u'col.lection.subdir.resource',
        u'col.lection.subdir.subdir.resource',
        u'col.lection.subdir.subdir.subdir.resource',
    ]
    for fqcr in fqcrs:
        assert AnsibleCollectionRef.is_valid_fqcr(fqcr)


# Generated at 2022-06-13 15:56:56.691693
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import ctypes, inspect
    from ansible.utils import context_objects as context

    # Find and import the C function _test_module_loaders_in_python
    # and raise an exception on failure.
    try:
        so_name = os.path.join(os.path.dirname(context._ansible_base_loader_exec_path), '_ansible_module_loaders.so')
        if not os.path.exists(so_name):
            raise ImportError('{0} is not installed, cannot load test module'.format(so_name))
        lib = ctypes.CDLL(so_name)
    except Exception:
        raise ImportError('cannot load test module')

    # Attempt to locate the function and raise an exception on failure.

# Generated at 2022-06-13 15:57:03.211829
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    loader = _AnsibleCollectionPkgLoaderBase(
        fullname='ansible_collections.test_ns.test',
        path_list=[os.path.join(os.path.dirname(__file__), 'test_data', 'collections', 'ansible_collections', 'test_ns')],
    )

    modules = {}
    for r in loader.iter_modules(prefix=''):
        modules[r[1]] = True
    assert modules == {
        'test': True,
        'test.bad': True,
        'test.good': True,
        'test.good.sub': True,
        'test.good.sub.sub2': True,
    }


# Generated at 2022-06-13 15:57:13.600380
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c', ref_type='role') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c.d') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c.d') is True
    assert AnsibleCollectionRef.is_valid_fqcr('a.b.c.d.e') is True

# Generated at 2022-06-13 15:57:20.474417
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # Unit test for method load_module of class _AnsibleInternalRedirectLoader

    # Setup variables for test
    fullname = 'ansible.module_utils.basic.AnsiColors'
    split_name = fullname.split('.')
    toplevel_pkg = split_name[0]
    module_to_load = split_name[-1]

    # Setup mocking for method import_module
    mock_mod = MagicMock()
    mock_mod.__name__ = 'ansible.module_utils.basic.ansi_colors'
    mock_mod.__path__ = ['ansible/module_utils/basic/ansi_colors.py']

# Generated at 2022-06-13 15:57:26.219175
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # Set up function
    # Setup: Generate a dummy module
    def temp_dir():
        return tempfile.mkdtemp()

    # Setup: Get the module name
    dummy_collection_dir = temp_dir()
    module_name = 'dummy_collection.dummy_module'
    module_path = os.path.join(dummy_collection_dir, 'dummy_module')

    os.makedirs(module_path)

    # Setup: Make it a package
    package_init_file_path = os.path.join(module_path, '__init__.py')
    with open(package_init_file_path, 'w') as package_init_file:
        package_init_file.write('')

    original_meta_yml_to_dict = ansible.utils.collection_loader

# Generated at 2022-06-13 15:57:30.169430
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # Arrange
    fullname = 'ansible.module_utils.ansible_test'
    path_list = ['/var/tmp/ansible/ansible-test-collection/from-ansible-test-collection/module_utils/']
    loader = _AnsibleInternalRedirectLoader(fullname, path_list)

    # Act and Assert
    with pytest.raises(ImportError):
        loader.load_module(fullname)


# Generated at 2022-06-13 15:57:32.630392
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # FIXME: how to test the ModuleType?
    pass

# Generated at 2022-06-13 15:57:39.481996
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.foo.bar.baz")
    loader._subpackage_search_paths = ['/tmp/foo', '/tmp/bar']
    loader._source_code_path = '/tmp/foo/bar/baz.py'
    assert loader.get_filename("ansible_collections.foo.bar.baz") == loader._source_code_path
    assert loader.get_filename("ansible_collections.foo.bar.baz.other") != loader._source_code_path

