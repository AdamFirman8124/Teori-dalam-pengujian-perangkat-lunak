

# Generated at 2022-06-13 15:50:21.231024
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # test when method ref fqcr
    # method: try_parse_fqcr
    # input: ansible_collections.community.jboss.modules.jboss_module
    # output: 
    # test source line: 49
    # test result: success
    ref = 'ansible_collections.community.jboss.modules.jboss_module'
    test_result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type=None)
    assert test_result == None

    # test when method ref fqcr
    # method: try_parse_fqcr
    # input: ansible_collections.an.sible.plugins.connecti.modules.jboss_module, module
    # output: 
    # test source line: 49
    # test result: success

# Generated at 2022-06-13 15:50:33.987506
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    #
    # I don't know how to test a method that returns a string
    #
    module_source = """
        from ansible_collections.ansible.builtin.plugins.module_utils.facts.version import META_VERSION as VERSION
        from ansible_collections.ansible.builtin.plugins.module_utils.facts.arch import META_ARCH as ARCH

        def get_package_data():
            return dict(
                version=VERSION,
                arch=ARCH,
            )
    """
    test_file_dir = os.path.dirname(__file__)
    module_dir = os.path.join(test_file_dir, 'fixtures')

# Generated at 2022-06-13 15:50:37.086849
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    loader = _AnsibleCollectionPkgLoaderBase('foo.bar')
    assert loader.is_package('foo.bar') == False



# Generated at 2022-06-13 15:50:44.011859
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    loader=_AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ns', path_list=['/home/user/ansible_collections/ns'])
    loader._source_code_path='/home/user/ansible_collections/ns/__init__.py'
    assert loader.get_source('ansible_collections.ns')==b''
    loader._source_code_path=None
    try:
        loader.get_source('ansible_collections.ns')
        assert False, 'ValueError expected'
    except (AttributeError, ValueError):
        assert True
    l=_AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ns.test_collection', path_list=['/home/user/ansible_collections/ns/test_collection'])

# Generated at 2022-06-13 15:50:45.216616
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:50:52.645829
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    def _test(source_code, expected_source_code, expected_compiled_code, **kwargs):
        loader = _AnsibleCollectionPkgLoaderBase(**kwargs)
        loader._source_code_path = '<test file>'
        loader._decoded_source = source_code
        code = loader.get_code('foo')
        assert loader._decoded_source == expected_source_code
        assert code == expected_compiled_code

    def _assert_code_object_attrs(code_obj, source_code, filename, mode):
        assert code_obj.co_argcount == 0
        assert code_obj.co_cellvars == ()
        assert code_obj.co_code == (b'|\x00\x00d\x01\x00S\x00')
        assert code

# Generated at 2022-06-13 15:50:53.668615
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    assert 1 == 1


# Generated at 2022-06-13 15:51:03.654962
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    class _test__AnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def _get_candidate_paths(self, path_list):
            return path_list

        def _get_subpackage_search_paths(self, candidate_paths):
            return [p for p in candidate_paths]

    test_path = '/foo/bar/baz/'
    test_file_1 = 'test_1.py'
    test_file_2 = 'test_2.py'
    test_data_1 = 'test_1.py content'

    with open(test_path + test_file_1, 'w') as f:
        f.write(test_data_1)


# Generated at 2022-06-13 15:51:16.083747
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test the case of a valid collection name
    assert AnsibleCollectionRef('foo.bar', 'baz.quux', 'xyzzy', 'role')
    assert AnsibleCollectionRef.is_valid_collection_name('foo.bar')
    assert AnsibleCollectionRef.is_valid_collection_name('ansible.builtin')
    assert not AnsibleCollectionRef.is_valid_collection_name('foo')
    assert not AnsibleCollectionRef.is_valid_collection_name('foo.bar.baz')

    # Test the case of an invalid collection name
    with pytest.raises(ValueError):
        AnsibleCollectionRef('foo', 'baz.quux', 'xyzzy', 'role')

    with pytest.raises(ValueError):
        AnsibleCollectionRef.is_valid_collection_name('foo')


# Generated at 2022-06-13 15:51:22.568681
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    real_ansible_collections_base_path = "dummy_ansible_collections_base_path"
    test_name = "ansible_collections.my_ns.my_coll.plugin.module"
    coll_dir = os.path.join(real_ansible_collections_base_path, "ansible_collections", "my_ns", "my_coll")
    coll_pkg_path = os.path.join(coll_dir, "plugin")

    class _TestCollectionPkgLoader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            return path_list


# Generated at 2022-06-13 15:52:24.106841
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    assert callable(_AnsibleInternalRedirectLoader.load_module)
    assert _AnsibleInternalRedirectLoader.load_module.__module__ == __name__



# Generated at 2022-06-13 15:52:33.134449
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from ansible.utils.collection_loader import _make_collection_names
    from ansible.utils.collection_loader import _AnsibleCollectionFinder
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoader

    #_fake_package_paths = _make_collection_names(["fake_collection"])
    _fake_package_paths = _make_collection_names(["fake_collection", "fake_collection.fake_ns"])
    _fake_package_paths.extend(['/usr/bin'])
    #_test_code_paths = _make_collection_names(["fake_collection.fake_ns"])
    _test_code_paths = _make_collection_names(["fake_collection", "fake_collection.fake_ns"])
    _test_code_

# Generated at 2022-06-13 15:52:36.213542
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    assert _AnsibleCollectionPkgLoaderBase(None)._synthetic_filename(None) == '<ansible_synthetic_collection_package>'

# Generated at 2022-06-13 15:52:41.317840
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # Arrange

    class C(object):

        def fire(self, collection_name, collection_path):
            self.collection_name = collection_name
            self.collection_path = collection_path

   
    # Act
    AnsibleCollectionConfig.on_collection_load = C()
    a = _AnsibleCollectionPkgLoader(['base'], ['/ansible/collections/ansible_collections/test'], 'test', 'base')
    a.load_module('ansible.collections.ansible_collections.test.base')

    # Assert
    assert AnsibleCollectionConfig.on_collection_load.collection_name == 'ansible.collections.ansible_collections.test.base'

# Generated at 2022-06-13 15:52:49.784150
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef

# Generated at 2022-06-13 15:53:00.402104
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    my_path = os.path.dirname(os.path.realpath(__file__))
    # create new instance of class _AnsibleCollectionPkgLoaderBase
    loader = _AnsibleCollectionPkgLoaderBase("_AnsibleCollectionPkgLoaderBase", path_list=[my_path])
    assert isinstance(loader, _AnsibleCollectionPkgLoaderBase)
    # Test get_data method
    assert loader.get_data(my_path) is not None
    assert loader.get_data('/does/not/exist/') is None
    assert loader.get_data('/does/not/exist.txt') is None
    assert loader.get_data(os.path.join(my_path, 'test__AnsibleCollectionPkgLoaderBase_get_data.py')) is not None



# Generated at 2022-06-13 15:53:04.227693
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    assert isinstance(_AnsibleCollectionPkgLoaderBase._get_code, _AnsibleCollectionPkgLoaderBase)
    assert hasattr(_AnsibleCollectionPkgLoaderBase,'_get_code')
    assert callable(_AnsibleCollectionPkgLoaderBase._get_code)

# Generated at 2022-06-13 15:53:12.247006
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    # Test is a package
    pkg = 'ansible_collections.pkg'
    loader = _AnsibleCollectionPkgLoaderBase(pkg)
    assert loader.is_package(pkg)
    assert loader.is_package('ansible_collections.pkg.sub')

    # Test is not a package
    mod = 'ansible_collections.mod'
    loader = _AnsibleCollectionPkgLoaderBase(mod)
    assert not loader.is_package(mod)
    assert not loader.is_package('ansible_collections.mod.sub')


# Generated at 2022-06-13 15:53:23.523864
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible').is_package('ansible_collections.ansible.os')

    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible.os').is_package('ansible_collections.ansible')

    assert _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible', ['/foo']).is_package('ansible_collections.ansible')
    assert not _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible.os', ['/foo']).is_package('ansible_collections.ansible.os')

# Generated at 2022-06-13 15:53:29.470300
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import doctest
    from ansible.init import AnsibleCollectionConfig

    module = AnsibleCollectionConfig('test_collection', __file__)
    loader = _AnsibleCollectionPkgLoaderBase('foo.bar.baz', [
        os.path.join(module.path, 'lib'),
        os.path.join(module.path, 't')
    ])
    loader.load_module(loader._fullname)
    pass



# Generated at 2022-06-13 15:54:23.892616
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    expected = ImportError
    try:
        raised = None
        obj = _AnsibleInternalRedirectLoader('ansible','path_list')
        obj.load_module('ansible')
    except Exception as err:
        raised = err
    assert isinstance(raised, expected)


# This loader only answers for intercepted Ansible Python modules. Normal imports will fail here and be picked up later
# by our path_hook importer (which proxies the built-in import mechanisms, allowing normal caching etc to occur)

# Generated at 2022-06-13 15:54:32.745625
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    import tempfile
    import shutil
    import os

    def test_temp_directory():
        """Creates a temp directory, returns the absolute path and deletes on exit.

        :rtype: str
        """
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    try:
        from importlib import util as importlib_util
    except ImportError:
        from importlib import find_loader as importlib_util

    def test_c_extension_module(temp_dir):
        """Creates a C extension in temp directory, ensures Python finds it, but skips over it in iter_modules.

        :param str temp_dir:
        """
        # TEST__AnsibleCollectionPkgLoaderBase_iter_modules c_extension_module
       

# Generated at 2022-06-13 15:54:40.243547
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from ansible.module_utils.six.moves import reload_module
    from ansible.utils.collection_loader._pkg_util_finder import _AnsiblePathHookFinder
    from ansible.utils.collection_loader._pkg_util_loader import _AnsibleCollectionPkgLoaderBase
    from ansible.utils.collection_loader._pkg_util_finder import _AnsibleCollectionFinder
    from ansible.utils.collection_loader._pkg_util_loader import _AnsibleCollectionPkgLoader
    from ansible.utils.collection_loader._pkg_util_loader import _AnsibleVersionedCollectionPkgLoader
    from ansible.utils.collection_loader._pkg_util_path import _AnsibleCollectionPathEntry
    # unittest code
    
    #Test for _AnsibleCollectionPkgLoaderBase


# Generated at 2022-06-13 15:54:43.489529
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    target = _AnsibleCollectionPkgLoaderBase('ansible_collections.my_namespace.my_collection')
    assert target.get_code('ansible_collections.my_namespace.my_collection') is None


# Generated at 2022-06-13 15:54:54.342228
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    assert _AnsibleCollectionFinder().find_module("ansible_collections.foo.bar") == _AnsibleCollectionLoader
    assert _AnsibleCollectionFinder().find_module("ansible_collections") == _AnsibleCollectionRootPkgLoader
    assert _AnsibleCollectionFinder().find_module("ansible_collections.foo") == _AnsibleCollectionNSPkgLoader
    assert _AnsibleCollectionFinder().find_module("ansible_collections.foo.bar.baz") == _AnsibleCollectionLoader
    assert _AnsibleCollectionFinder().find_module("ansible.config.loader") == _AnsibleInternalRedirectLoader
    assert _AnsibleCollectionFinder().find_module("ansible.test") == _AnsibleInternalRedirectLoader
    assert _AnsibleCollectionF

# Generated at 2022-06-13 15:55:02.743408
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    """
    Test _AnsibleCollectionPkgLoaderBase.get_code()

    This method is used by the importers to get the code object of a module.
    The code is compiled by get_code and later executed by load_module.
    The code object is also needed by getattr or dir.
    """
    _tempdir = tempfile.mkdtemp()
    code_object = None

# Generated at 2022-06-13 15:55:08.981746
# Unit test for method from_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:55:10.338107
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    import ansible_collections.ansible.foo
    assert isinstance(ansible_collections.ansible.foo, ModuleType)



# Generated at 2022-06-13 15:55:21.357328
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    import tempfile
    import shutil
    import textwrap

    # define directory tree to set up finder (these paths should be relative to the collection root, i.e.
    # collection_to_create)

# Generated at 2022-06-13 15:55:22.250235
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
# TODO:
    pass



# Generated at 2022-06-13 15:58:48.777277
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # This is a normal module
    r = AnsibleCollectionRef.from_fqcr('galaxy.author.module_name', 'module')
    assert r.collection == 'galaxy.author'
    assert r.resource == 'module_name'
    assert r.subdirs == ''
    assert r.ref_type == 'module'
    assert r.fqcr == 'galaxy.author.module_name'

    # This is a module inside a subdir
    r = AnsibleCollectionRef.from_fqcr('galaxy.author.subdir1.module_name', 'module')
    assert r.collection == 'galaxy.author'
    assert r.resource == 'module_name'
    assert r.subdirs == 'subdir1'
    assert r.ref_type == 'module'
    assert r.f

# Generated at 2022-06-13 15:58:58.957407
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    TEST_DATA = [
        ('action_plugins', 'action'),
        ('callback_plugins', 'callback'),
        ('connection_plugins', 'connection'),
        ('filter_plugins', 'filter'),
        ('inventory_plugins', 'inventory'),
        ('lookup_plugins', 'lookup'),
        ('library', 'modules'),
        ('test_plugins', 'test'),
        ('vars_plugins', 'vars'),
    ]
    for legacy_plugin_dir_name, plugin_type in TEST_DATA:
        assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(legacy_plugin_dir_name) == plugin_type, \
            "AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type() failed to convert legacy_plugin_dir_name=%s to plugin_type=%s"