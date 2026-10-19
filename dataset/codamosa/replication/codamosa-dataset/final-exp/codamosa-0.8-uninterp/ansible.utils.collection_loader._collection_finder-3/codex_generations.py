

# Generated at 2022-06-13 15:49:55.558660
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.six.moves.urllib.request', 'path_list')
    assert loader._redirect == 'urllib.request'


# Generated at 2022-06-13 15:50:00.066555
# Unit test for method from_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:50:02.805664
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    loader = _AnsibleInternalRedirectLoader('ansible.builtin.os_user', 'path_list')
    assert loader.load_module('ansible.builtin.os_user') == None

# Generated at 2022-06-13 15:50:04.981238
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    path = '/tmp/ansible'
    module = _AnsibleCollectionPkgLoaderBase(path, path)
    print (module.get_data('ansible/__init__.py'))


# Generated at 2022-06-13 15:50:15.878389
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    class TestedFinder:
        def find_module(self, fullname, path=None):
            raise AssertionError('should not totally fail')

    cf = TestedFinder()

    t = _AnsiblePathHookFinder(cf, '/foo')
    assert t.find_module('bar')  # no path specified should use the fallback
    assert t.find_module('bar', path=['/bar'])  # path specified should use the fallback
    assert t.find_module('ansible_collections')

    # assert that the finder is passed the fallback path even when specific path is specified
    # our meta-path fake finder should still be consulted
    assert cf.find_module('ansible_collections.foo', path=['/bar'])

# Generated at 2022-06-13 15:50:26.136037
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    from ansible.errors import AnsibleError

    # test valid import_redirection
    x = AnsibleCollectionRef('random.nonsense', '', '', 'module')
    if x.collection == 'random.nonsense':
        raise AnsibleError('class AnsibleCollectionRef constructor failed for valid collection name')

    if x.ref_type != 'module':
        raise AnsibleError('class AnsibleCollectionRef constructor failed for valid ref_type')

    if x.n_python_collection_package_name != 'ansible_collections.random.nonsense':
        raise AnsibleError('class AnsibleCollectionRef constructor failed for valid n_python_collection_package_name')


# Generated at 2022-06-13 15:50:31.979206
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    from ansible_collections.ansible.builtin.plugins.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.builtin.plugins.action.network import action_plugins
    import sys
    module = sys.modules['ansible_collections.ansible.builtin.plugins.action.network']
    assert type(module) == ModuleType
    sys.modules.pop('ansible_collections.ansible.builtin')
    sys.modules.pop('ansible_collections')
    sys.modules.pop('ansible')
    module = import_module('ansible_collections.ansible.builtin.plugins.action.network')
    assert type(module) == ModuleType

# Generated at 2022-06-13 15:50:41.287414
# Unit test for constructor of class _AnsibleCollectionNSPkgLoader
def test__AnsibleCollectionNSPkgLoader():
    # We no longer support Python 2 so we just test the Python 3 case
    assert len(_AnsibleCollectionNSPkgLoader('ansible_collections.mycol.mypkg', path_list=['/path/to/col'])._subpackage_search_paths) == 1
    try:
        _AnsibleCollectionNSPkgLoader('ansible_collections.mycol', path_list=['/path/to/col'])
        assert False
    except ImportError:
        pass
    try:
        _AnsibleCollectionNSPkgLoader('ansible.mypkg', path_list=['/path/to/col'])
        assert False
    except ImportError:
        pass

# Generated at 2022-06-13 15:50:47.079375
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    caller = os.path.dirname(__file__)
    test_module = "ansible_collections.test_ns.basic_plugin"
    test_module_plugin = "ansible_collections.test_ns.basic_plugin.plugin"

    test_loader = _AnsibleCollectionPkgLoaderBase(test_module, [caller])
    test_loader_plugin = _AnsibleCollectionPkgLoaderBase(test_module_plugin, [caller])

    assert test_loader.is_package('ansible_collections.test_ns.basic_plugin') is True
    assert test_loader_plugin.is_package('ansible_collections.test_ns.basic_plugin.plugin') is False



# Generated at 2022-06-13 15:50:48.258905
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    # TODO(retr0h): Implement
    pass

# Generated at 2022-06-13 15:51:24.413796
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six.moves import BuiltinModule
    from ansible.module_utils.six.moves import reload_module
    from ansible.module_utils.six.moves import UserDict
    from ansible.module_utils.six.moves import UserList
    from ansible.module_utils.six.moves import UserString
    import collections
    import json
    import re
    import sys
    import types
    import unittest

    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.acme.foobar', path_list=[os.path.join(os.path.dirname(__file__), 'fixtures/ansible_collections/acme/foobar')])
    loader.load_module

# Generated at 2022-06-13 15:51:31.172723
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.basic', None)
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.cloud.openstack.os_security_group', None)
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.cloud.openstack.openstack', None)
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.cloud.openstack.os_server', None)
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.cloud.openstack.os_user', None)
    t = _AnsibleInternalRedirectLoader('ansible.module_utils.distro.rhel', None)

# Generated at 2022-06-13 15:51:35.762689
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    test_legacy_plugin_dir_name = "unit_test"
    test_plugin_type = "unit"
    assert test_plugin_type in AnsibleCollectionRef.VALID_REF_TYPES
    assert test_plugin_type == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(test_legacy_plugin_dir_name)
    assert "lib" == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("library")


# Generated at 2022-06-13 15:51:39.408818
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.basic', None)
    assert loader._redirect == 'ansible_collections.ansible.builtin.module_utils.basic'



# Generated at 2022-06-13 15:51:49.998394
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    def test__AnsibleInternalRedirectLoader_load_module_helper(redirect, fullname):
        loader = _AnsibleInternalRedirectLoader(fullname, None)
        loader._redirect = redirect

        try:
            loader.load_module(fullname)
        except Exception as ex:
            raise ValueError(to_native(ex))

    # Arrange
    fullname = 'ansible.builtin.test'

    # Act
    test__AnsibleInternalRedirectLoader_load_module_helper('ansible.test', fullname)

    # Assert
    # see no exception


# discovers the real location of a module, deals with redirection and core/collection module spliting
# implementation detail: for modules under the top-level "ansible" package (and all of its collections),
# fullname should always be

# Generated at 2022-06-13 15:52:02.039116
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    def test__AnsibleCollectionPkgLoaderBase_get_source_impl(module_source_bytes, want_source_bytes):
        module_source_path = write_temp_file(module_source_bytes, suffix='.py')

        # Arrange
        loader = _AnsibleCollectionPkgLoaderBase('')
        loader._source_code_path = module_source_path

        # Act
        got_source_bytes = loader.get_source('')

        # Assert
        assert got_source_bytes == want_source_bytes
        # Clean up
        os.remove(module_source_path)

    test__AnsibleCollectionPkgLoaderBase_get_source_impl(
        b'# source code byte string',
        b'# source code byte string'
    )

# Generated at 2022-06-13 15:52:10.360070
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    test_data_path = 'test_data_get_data'
    test_file_name = 'test_file'
    test_data = 'This is test data.'
    with open(test_file_name, 'w') as file:
        file.write(test_data)
    import shutil
    shutil.copy(test_file_name, test_data_path)
    with open(os.path.join(test_data_path, test_file_name), 'r') as file:
        assert _AnsibleCollectionPkgLoaderBase.get_data(os.path.join(test_data_path, test_file_name)) == test_data
    shutil.rmtree(test_data_path)
    os.remove(test_file_name)

# Generated at 2022-06-13 15:52:17.757689
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    from ansible.utils.collection_loader import AnsibleCollectionRef

    with pytest.raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ansible.builtin.ping', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ansible.builtin.ping', 'role')

    with pytest.raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ansible.builtin.notarealmodule', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ansible.builtin', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ansible', 'module')


# Generated at 2022-06-13 15:52:23.833188
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    @contextmanager
    def _new_or_existing_module(name, **kwargs):
        module = ModuleType(name)
        sys.modules[name] = module
        for attr, value in kwargs.items():
            setattr(module, attr, value)
        yield module

    obj = _AnsibleCollectionPkgLoaderBase('ansible_collections.ns.pack.mod')

    obj.load_module = lambda fullname: None
    obj.is_package = lambda fullname: False
    obj.get_source = lambda fullname: None
    obj.get_data = lambda path: None
    obj._decoded_source = None
    obj._compiled_code = None


# Generated at 2022-06-13 15:52:29.504877
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    class TestMetadata:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs

    metadata = TestMetadata(
        name=u'collection_name',
        namespace=u'namespace',
    )
    acr = AnsibleCollectionRef(metadata.namespace, metadata.name, subdirs=None, resource=u'foo', ref_type=u'role')


# Constructors for collection references

# Generated at 2022-06-13 15:53:36.299621
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    path_list = ['/Users/fengwei/python-test/test_py_loader']
    cl = _AnsibleCollectionPkgLoaderBase('test_py_loader.test', path_list)
    assert(cl.is_package('test_py_loader.test') == False)


# Generated at 2022-06-13 15:53:48.016820
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    def _AnsibleCollectionPkgLoaderBase_get_code(subpackage, package_path):
        from ansible_collections.ansible.plugins import module_utils as fnn_module_utils
        from ansible_collections.ansible.plugins.modules import fnn as fnn_module
        fnn_module_utils.__path__ = fnn_module.__path__ \
            = fnn_module.__init__.__code__.co_filename \
            = fnn_module_utils.__init__.__code__.co_filename \
            = package_path
        loader = _AnsibleCollectionPkgLoaderBase(self.fullname)
        self.assertEqual(loader.get_code(self.fullname+subpackage), None)

# Generated at 2022-06-13 15:53:49.880184
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    _AnsibleCollectionPkgLoader('../../../')


# Generated at 2022-06-13 15:54:00.975819
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # Positive test case
    fqcr = "foo.bar.baz"
    ref_type = "module"
    test_obj = AnsibleCollectionRef.from_fqcr(fqcr,ref_type)
    assert test_obj.collection == "foo.bar"
    assert test_obj.subdirs == ""
    assert test_obj.resource == "baz"
    assert test_obj.ref_type == "module"
    assert test_obj.n_python_collection_package_name == "ansible_collections.foo.bar"
    assert test_obj.n_python_package_name == "ansible_collections.foo.bar.plugins.module"
    assert test_obj.fqcr == "foo.bar.baz"

    # Negative test case

# Generated at 2022-06-13 15:54:08.482362
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    import sys
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.ansible_galaxy.collection_finder import _AnsibleCollectionFinder
    from ansible.module_utils.ansible_galaxy.path_hook import _AnsiblePathHookFinder
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.module_utils.common

    class _TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            return path_list

        def _get_subpackage_search_paths(self, candidate_paths):
            return candidate_paths



# Generated at 2022-06-13 15:54:11.606761
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    """Test for method load_module of class _AnsibleCollectionPkgLoaderBase"""
    raise NotImplementedError



# Generated at 2022-06-13 15:54:18.342616
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr('my.test.module', 'module')
    assert AnsibleCollectionRef.try_parse_fqcr('my.test.module', 'module')
    assert not AnsibleCollectionRef.try_parse_fqcr('my.test.module', 'role')
    assert not AnsibleCollectionRef.try_parse_fqcr('my.test.invalid')
    assert not AnsibleCollectionRef.try_parse_fqcr('my.test.invalid.module', 'module')


# Generated at 2022-06-13 15:54:20.594603
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    assert(_AnsibleCollectionPkgLoaderBase('').get_code == _AnsibleCollectionPkgLoaderBase.get_code)

# Generated at 2022-06-13 15:54:30.518093
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from ansible.module_utils import common

    class TestCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname, path_list=None):
            super(TestCollectionPkgLoaderBase, self).__init__(fullname, path_list)
            self._source_code_path = '<string>'

    root_package_name = 'ansible_collections'
    test_module = 'testmodule'
    module_fullname = '.'.join([root_package_name, test_module])
    test_module_file = os.path.join(os.path.dirname(common.__file__), 'module_utils/basic.py')
    assert os.path.isfile(test_module_file)

    # not a real loader, but a crude stand-in

# Generated at 2022-06-13 15:54:37.375879
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == u'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == u'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == u'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == u'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == u'filter'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('inventory_plugins') == u'inventory'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:55:34.705148
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    print("========================Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase========================")
    class MyClass(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname):
            super(MyClass, self).__init__(fullname, path_list=["/path/to/package"])
            self._subpackage_search_paths = ["/path/to/package"]
    module_loader = MyClass("ansible_collections.test.test")
    print("test for fullname: ansible_collections.test.test")
    print("test for package that does not have __init__.py")
    print("get_filename() should return string <ansible_synthetic_collection_package>")

# Generated at 2022-06-13 15:55:36.123884
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    assert 1==1
# ----------------------------------------------------------------------
# << Tests >> (11 of 28)

# Generated at 2022-06-13 15:55:47.493358
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    import ansible
    ansible_path = to_native(os.path.dirname(to_bytes(ansible.__file__)))
    example_paths = [os.path.join(ansible_path, '..', '..', 'collection_examples'),
                     os.path.join(ansible_path, '..', '..', 'collection_examples', 'ansible_collections')]
    collection_finder = _AnsibleCollectionFinder(paths=example_paths, scan_sys_paths=False)
    assert collection_finder._ansible_pkg_path == ansible_path
    assert collection_finder._n_configured_paths == example_paths
    assert collection_finder._n_cached_collection_paths is None
    assert collection_finder._n_cached_collection_qualified_

# Generated at 2022-06-13 15:55:59.827566
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import tempfile
    test_dir = tempfile.TemporaryDirectory()
    tmpdir = test_dir.name

    # copy source directories of ansible_collections and ansible to temporary
    # directory
    collection_dir = os.path.join(tmpdir, "ansible_collections")
    shutil.copytree(os.path.join(os.path.dirname(__file__), "..", ".."),
                    collection_dir)

    collection_finder = _AnsibleCollectionFinder([tmpdir])
    collection_finder._install()

    ansible_core_module_name = "ansible.module_utils.basic"
    ansible_core_module = collection_finder.find_module(ansible_core_module_name)

    print(ansible_core_module)
    test_dir.cleanup()

# Generated at 2022-06-13 15:56:08.580893
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():

    ci_path = os.path.realpath(__file__)
    ci_path = os.path.join(ci_path, '../../../lib/ansible/collections')
    ci_path = os.path.normpath(ci_path)

    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[ci_path])
    loader.load_module('ansible_collections.somens')

    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.subpkg', path_list=[ci_path])
    loader.load_module('ansible_collections.somens.subpkg')


# Generated at 2022-06-13 15:56:13.054099
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    print("Test __repr__")
    p = AnsibleCollectionRef('ns.coll', None, 'name', 'module')
    string = p.__repr__()
    assert string == "AnsibleCollectionRef(collection='ns.coll', subdirs=None, resource='name')"

# Generated at 2022-06-13 15:56:13.788014
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    pass

# Generated at 2022-06-13 15:56:24.926103
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test with the full variables.
    a = AnsibleCollectionRef('namespace.collectionname', 'subdir1.subdir2', 'resource', 'role')

    assert a.subdirs == 'subdir1.subdir2'
    assert a.collection == 'namespace.collectionname'
    assert a.resource == 'resource'
    assert a.ref_type == 'role'
    assert a.n_python_collection_package_name == 'ansible_collections.namespace.collectionname'
    assert a.n_python_package_name == 'ansible_collections.namespace.collectionname.roles.subdir1.subdir2.resource'
    assert a.fqcr == 'namespace.collectionname.subdir1.subdir2.resource'

    # Test with empty subdirs.

# Generated at 2022-06-13 15:56:36.296120
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from collections import namedtuple
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import ansible_collections.somens.subns.subsubns.subsubsubns
    import ansible_collections.somens.subns.subsubns.subsubsubns.subsubsubsubns
    import ansible_collections.somens.subns.subsubns.subsubsubns.subsubsubsubsubns
    import ansible_collections.somens.subns.subsubns.subsubsubns.subsubsubsubsubsubns
    import ansible_collections.somens.subns.subsubns.subsubsubns.subsubsubsubsubsubsubns

# Generated at 2022-06-13 15:56:44.606771
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:59:07.553600
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # test initialization via __init__()
    for ref_type in AnsibleCollectionRef.VALID_REF_TYPES:
        ar = AnsibleCollectionRef('my.collection', 'subdir1.subdir2', 'myresource', ref_type)
        assert(ar.fqcr == 'my.collection.subdir1.subdir2.myresource')
        assert(ar.collection == 'my.collection')
        assert(ar.subdirs == 'subdir1.subdir2')
        assert(ar.resource == 'myresource')

    # test initialization via from_fqcr()
    for ref_type in AnsibleCollectionRef.VALID_REF_TYPES:
        ar = AnsibleCollectionRef.from_fqcr('ns1.coll1.subdir1.subdir2.myresource', ref_type)