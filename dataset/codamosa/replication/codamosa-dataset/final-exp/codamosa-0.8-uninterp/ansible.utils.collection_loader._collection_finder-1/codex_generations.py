

# Generated at 2022-06-13 15:50:30.036154
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    result = _AnsibleCollectionPkgLoaderBase().get_source()
    assert result is None


# Generated at 2022-06-13 15:50:40.199469
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Test the case of toplevel_pkg not in ['ansible', 'ansible_collections']
    toplevel_pkg = 'toplevel_pkg'
    fullname = toplevel_pkg
    path = None
    acf = _AnsibleCollectionFinder()
    assert None is acf.find_module(fullname, path)

    # test the case of toplevel_pkg in ['ansible', 'ansible_collections']
    #        and part_count == 1
    toplevel_pkg = 'ansible'
    fullname = toplevel_pkg
    path = None
    assert None is acf.find_module(fullname, path)
    toplevel_pkg = 'ansible_collections'
    fullname = toplevel_pkg

# Generated at 2022-06-13 15:50:46.837843
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    from collections import namedtuple
    args = namedtuple('args', 'mock_collection_root mock_package_to_load mock_pkg_path')('test_0', 'test_1', 'test_2')
    mock_logger = MagicMock()


# Generated at 2022-06-13 15:50:49.845151
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    test_loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.test', ['/'])
    assert test_loader.is_package('ansible_collections.test.test')
    test_loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.not_package', ['/'])
    assert not test_loader.is_package('ansible_collections.test.not_package')

# Generated at 2022-06-13 15:50:54.501135
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='', path_list=[])
    from ansible.module_utils.six.moves import _imp as imp
    assert loader.get_code('') is imp.NullImporter().find_module('', None).load_module('').__code__
test__AnsibleCollectionPkgLoaderBase_get_code()



# Generated at 2022-06-13 15:51:04.885811
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # noinspection PyUnresolvedReferences
    "Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase"
    from ansible_collections.ns1.t1.plugins.module_utils import f1
    from ansible_collections.ns2.t1.plugins.module_utils import f1

    # Test path for file 1a.
    test_filename = f1.__file__
    # Test path for file 2a.
    test_filename2 = f1.__file__
    assert test_filename == test_filename2

    # Test paths for file 1b.
    test_filename = os.path.join(os.path.dirname(__file__), 'ansible_collections/ns1/t1/plugins/module_utils/f1.py')

# Generated at 2022-06-13 15:51:10.273962
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    l = _AnsibleCollectionPkgLoaderBase('a.b')
    l._subpackage_search_paths = [1]
    l._fullname = 'a.b'
    assert l.load_module('a.b') == sys.modules['a.b']



# Generated at 2022-06-13 15:51:20.966384
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    print('Called %s' % test__AnsibleCollectionPkgLoaderBase_load_module.__name__)
    test_fullname = 'ansible_collections.ns1.n2.n3'
    test_parent_fullname = 'ansible_collections.ns1.n2'
    test_package_to_load = 'n3'
    test_base_paths = '/path1/', '/path2/'
    test_code = 'z = "import_test"'
    test_code_path = '/path1/ns1/n2/n3/__init__.py'
    test_code_path_existing = '/path2/ns1/n2/n3/__init__.py'

# Generated at 2022-06-13 15:51:32.510557
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').fqcr == 'ns.coll.resource'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.resource', 'module').fqcr == 'ns.coll.subdir1.resource'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.rolename', 'role').fqcr == 'ns.coll.rolename'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.playbook_name', 'playbook').fqcr == 'ns.coll.playbook_name'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.playbook_name.yml', 'playbook').fqcr == 'ns.coll.playbook_name'

# Generated at 2022-06-13 15:51:35.674137
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    test_object = _AnsibleCollectionPkgLoaderBase('foo', 'foo.py')
    actual = test_object.__repr__()
    expected = '_AnsibleCollectionPkgLoaderBase(path=foo.py)'
    assert actual == expected, 'Expected (%s), got (%s)' % (expected, actual)



# Generated at 2022-06-13 15:52:07.941766
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert "action" == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("action_plugins")
    assert "module" == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("library")

    try:
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type("invalid_dir")
        assert False, "AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type should have failed when invalid_dir is passed"
    except ValueError:
        pass

# Tests for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:52:17.431958
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():  # noqa: E302
    import os
    import sys
    import tempfile

    def mktmpdir(name, parents=False):
        if parents:
            return tempfile.mkdtemp(prefix=name + '_', dir=sys.path[0])
        else:
            return tempfile.mkdtemp(prefix=name + '_')

    def mktmpfile(name, mode=None, contents=''):
        fd, p = tempfile.mkstemp(prefix=name + '_', text=True)
        try:
            if mode:
                os.fchmod(fd, mode)

            if contents:
                os.write(fd, to_bytes(contents, nonstring='passthru'))

            return p
        finally:
            os.close(fd)

    tmpdir = mkt

# Generated at 2022-06-13 15:52:22.919016
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    import sys
    import ansible.utils.collection_loader as cl
    fullname = 'ansible.module_utils.network.common.utils'
    ext_path = ''
    __loader__ = cl._AnsibleInternalRedirectLoader(fullname, ext_path)
    module_from_redirect = __loader__.load_module(fullname)
    assert sys.modules[fullname] == module_from_redirect
    assert module_from_redirect.__file__ == '/usr/local/lib/python2.7/dist-packages/ansible/module_utils/network/common/utils.py'

# Generated at 2022-06-13 15:52:25.981857
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    ref = AnsibleCollectionRef(collection_name='mycollection', subdirs=None, resource='testmodule', ref_type='module')
    assert ref.__repr__() == "AnsibleCollectionRef(collection='mycollection', subdirs=None, resource='testmodule')"



# Generated at 2022-06-13 15:52:31.384387
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ns.package')
    loader._source_code_path = '/path/to/source/code/ansible_collections/ns/package/foo.py'
    loader._subpackage_search_paths = ['/path/to/source/code/ansible_collections/ns/package']

    assert loader.get_data('foo.py') == b'', 'get_data must return the correct file content'
    assert loader.get_data('bar.py') is None, 'get_data must return none when the file does not exist'
    assert loader.get_data('baz') is None, 'get_data must return none when the path is not a file'


# Generated at 2022-06-13 15:52:33.676198
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    assert True



# Generated at 2022-06-13 15:52:44.976303
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import pytest
    from ansible.module_utils._text import to_text
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.common._collections_compat import Mapping
    import os
    import pkgutil

    if PY3:
        from importlib._bootstrap_external import FileFinder
        # This method is not called directly during test. But, it is used during test indirectly.
        # So, this method is tested here along with the method 'find_module' for class _AnsiblePathHookFinder.
        def test__get_filefinder_path_hook(monkeypatch):
            _filefinder_path_hook = _AnsiblePathHookFinder._get_filefinder_path_hook()

# Generated at 2022-06-13 15:52:54.184228
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    # test an empty package
    tmpscriptdir = tempfile.mkdtemp()
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.foo.bar', [tmpscriptdir])
    assert loader.iter_modules('') == []

    # test a non-empty package
    subpackage_dir = os.path.join(tmpscriptdir, 'baz')
    os.makedirs(subpackage_dir)
    with open(os.path.join(subpackage_dir, '__init__.py'), 'wb'):
        pass

    assert loader.iter_modules('') == ['baz']

    # test a subpackage with a prefix
    assert loader.iter_modules('ba') == ['baz']

    # test an empty subpackage

# Generated at 2022-06-13 15:53:02.686690
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # FQCR test with 'module'
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir1.subdir2.resource', 'module')
    # FQCR test with non-'module'
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.rolename', 'role')
    # FQCR test with 'module'
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir1.subdir2.resource', 'module')
    # FQCR test with 'module' that has extension
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir1.subdir2.resource.yml', 'module')
    # FQCR test with 'playbook' that has extension

# Generated at 2022-06-13 15:53:08.349070
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name='test.module', path=packaging.provider.PathMetadata('/path/to/files/base'))

    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase._module_file_from_path(leaf_name='test.module', path='../..')
# Tests for method get_filename of class _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:53:37.316071
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testres')
    assert AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testres', 'module')
    assert AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testres', 'role')
    assert not AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testres', 'action')
    assert AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testres', 'test')
    assert AnsibleCollectionRef.is_valid_fqcr('ansible_test.testcoll.testdir.testres')

# Generated at 2022-06-13 15:53:48.932645
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # given
    test_get_data_inputs = {
        '/path/file1.txt': {
            'content': 'file1',
            'expectation': 'file1',
        },
        '/path/file2.txt': {
            'content': 'file2',
            'expectation': 'file2',
        },
        '/path/__init__.py': {
            'content': 'file3',
            'expectation': '',
        },
    }
    test_get_data_files = {}
    for data_input in test_get_data_inputs.values():
        test_get_data_files[data_input['content']] = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 15:54:00.714437
# Unit test for constructor of class AnsibleCollectionRef

# Generated at 2022-06-13 15:54:05.289023
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    """
    Test method __repr__ of class AnsibleCollectionRef
    """
    ansible_collection_ref = AnsibleCollectionRef('collection_name', 'subdirs', 'resource', 'ref_type')
    assert repr(ansible_collection_ref) == 'AnsibleCollectionRef(collection=\'collection_name\', subdirs=\'subdirs\', resource=\'resource\')'


# Generated at 2022-06-13 15:54:16.886858
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # test_loader is an instance of class _AnsibleCollectionPkgLoaderBase
    test_loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible.some_ns', path_list=['/path/to/parent'])
    test_loader._source_code_path = '/path/to/parent/some_ns/foo.py'
    assert test_loader.get_filename('ansible_collections.ansible.some_ns') == test_loader._source_code_path
    # if the module does not exist and is a package
    test_loader._source_code_path = None
    test_loader._subpackage_search_paths = ['/path/to/parent/some_ns/subpackage']

# Generated at 2022-06-13 15:54:27.380904
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    '''
    This test is called by pytest to verify that method load_module of class _AnsibleInternalRedirectLoader
    works as expected.
    :return: None
    '''
    col_name = 'ansible.builtin'
    col_pkg_path = 'lib/ansible/collections/ansible/builtin'

    fullname = 'ansible.module_utils.common.dict'

    # Redirect import of ansible.module_utils to ansible.builtin.module_utils
    # Prepare the fake package
    sys.modules[fullname] = None
    fake_module = types.ModuleType(fullname)
    sys.modules[fullname] = fake_module
    # Prepare the fake path_hook in sys.meta_path
    fake_path_hook = MagicMock()
    sys.meta_

# Generated at 2022-06-13 15:54:37.383630
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # Make sure that get_data returns the right error if path is None
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase().get_data(None)
    # Make sure that get_data returns the right error if path is empty string
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase().get_data('')
    # Make sure that get_data returns the right error if path is relative
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase().get_data('collections/fake_collection/fake_namespace/fake_name')
    # Make sure that get_data returns the right error if path does not exist

# Generated at 2022-06-13 15:54:43.141634
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    class FakeFindLoader_Loader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, *args, **kwargs):
            super(FakeFindLoader_Loader, self).__init__(*args, **kwargs)

    loader = FakeFindLoader_Loader(fullname='ansible_collections.testns.foo', path_list=[])
    assert loader.get_code('foo') == None


# Generated at 2022-06-13 15:54:48.709283
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    testref = AnsibleCollectionRef(u'my.collection', None, u'mymodule', u'module')
    if testref.collection != u'my.collection' or testref.subdirs != None or testref.resource != u'mymodule' or testref.ref_type != u'module':
        raise AssertionError('test_AnsibleCollectionRef constructor failed')


# Generated at 2022-06-13 15:54:58.877700
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    # Test with collection, subdirs and resource
    ref = AnsibleCollectionRef(collection_name='ns.name', subdirs='dir1.dir2', resource='name', ref_type='module')
    expected = 'AnsibleCollectionRef(collection=\'ns.name\', subdirs=\'dir1.dir2\', resource=\'name\')'
    assert ref.__repr__() == expected

    # Test with empty collection, subdirs and resource
    ref = AnsibleCollectionRef(collection_name='', subdirs='', resource='', ref_type='module')
    expected = 'AnsibleCollectionRef(collection=\'\', subdirs=\'\', resource=\'\')'
    assert ref.__repr__() == expected

    # Test with no collection, no subdirs and resource
    ref = Ans

# Generated at 2022-06-13 15:56:57.526838
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import sys
    import ansible_collections.ansible.test

    assert 'ansible_collections.ansible.test' in sys.modules

    assert 'ansible_collections.ansible.test.plugins.module_utils.module_utils_logger' in sys.modules
    assert 'ansible.utils.module_docs' in sys.modules
    assert 'ansible_collections.ansible' in sys.modules

    del sys.modules['ansible_collections.ansible.test']
    del sys.modules['ansible_collections.ansible.test.plugins.module_utils.module_utils_logger']
    del sys.modules['ansible.utils.module_docs']
    del sys.modules['ansible_collections.ansible']

# Generated at 2022-06-13 15:57:04.383837
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    print("testing module {0}...".format(__loader__))
    with_ns = False
    # TODO: imp.reload doesn't work with relative imports, so make sure we don't have these in the import!
    # TODO: the collection loaders expect the loader to be installed on sys.meta_path so make sure that's true!
    #FIXME: put this source in an external file to ensure it's not in the same directory as the test code
    source = '''\
        import os
         
        def foo():
            return "module"
         
        def bar():
            return "module"
        '''
    #FIXME: put this source in an external file to ensure it's not in the same directory as the test code

# Generated at 2022-06-13 15:57:08.055960
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader(['ansible','builtin','module_utils'], [])
    actual = loader.load_module('ansible.builtin.module_utils')
    assert actual._collection_meta == {}

# Generated at 2022-06-13 15:57:16.542559
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # Create a mock object of a class
    from unittest.mock import Mock
    class_instance = Mock(_AnsibleCollectionPkgLoaderBase)
    # Define return values for the mock object to return when a method is called
    class_instance._subpackage_search_paths = [os.path.join(ANSIBLE_TEST_DATA_ROOT, 'collection_pkg_loader/subpkg1')]
    class_instance._fullname = "subpkg1"
    class_instance._rpart_name = ("", "subpkg1")
    class_instance._package_to_load = "subpkg1"
    class_instance._parent_package_name = ""
    # Call the method and check the returned value
    return_value = class_instance.get_data("subpkg1/subsubpkg1/test.txt")

# Generated at 2022-06-13 15:57:18.047743
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    # TODO: implement
    pass

    # Unit test for method __init__ of class _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:57:23.441321
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    # set up test invironment
    import tempfile
    import shutil
    from ansible.module_utils._text import to_bytes
    test_dir = tempfile.mkdtemp()
    test_root_dir = os.path.join(test_dir, 'ansible_collections')

# Generated at 2022-06-13 15:57:30.864319
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():

    # Handle no namespace
    assert AnsibleCollectionRef.from_fqcr('collection.resource', 'module').ref_type == u'module'
    assert AnsibleCollectionRef.from_fqcr('collection.resource', 'module').collection == u'collection'
    assert AnsibleCollectionRef.from_fqcr('collection.resource', 'module').resource == u'resource'
    assert AnsibleCollectionRef.from_fqcr('collection.resource', 'module').subdirs == u''

    # Handle namespace
    assert AnsibleCollectionRef.from_fqcr('ns.collection.resource', 'module').ref_type == u'module'
    assert AnsibleCollectionRef.from_fqcr('ns.collection.resource', 'module').collection == u'ns.collection'

# Generated at 2022-06-13 15:57:32.353433
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader('my_collection.my_namespace', 'my_plugin')
    loader.load_module('my_collection.my_namespace.my_plugin')

# Generated at 2022-06-13 15:57:37.106132
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from ansible_collections.nsbl.test.unit.plugins.loader._loader_test_lib import _TestUSPathContext
    path_list = ['/tmp']
    _test_us_path_context = _TestUSPathContext(path_list)
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.nsbl.test', path_list)
    assert(loader.load_module('ansible_collections.nsbl.test') == None)

# Generated at 2022-06-13 15:57:42.426193
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test the class loader
    ref = AnsibleCollectionRef.from_fqcr('test_namespace.test_collection.test_module', u'module')
    assert ref.collection == 'test_namespace.test_collection'
    assert ref.subdirs == ''
    assert ref.resource == 'test_module'
    assert ref.ref_type == 'module'
    assert ref.n_python_collection_package_name == 'ansible_collections.test_namespace.test_collection'
    assert ref.n_python_package_name == 'ansible_collections.test_namespace.test_collection.plugins.module'
    assert ref.fqcr == 'test_namespace.test_collection.test_module'

# Generated at 2022-06-13 15:58:10.860770
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # Pretending that there is a redirection from 'ansible.builtin.foo' -> 'ansible.builtin.bar'
    builtin_meta = {'import_redirection': {'ansible.builtin.foo': {'redirect': 'ansible.builtin.bar'}}}

    # We create a fake collection configuration
    fake_config = AnsibleCollectionConfig()
    fake_config.namespace_packages = {'ansible.builtin': ['/some/non/existing/directory']}
    fake_config.collection_package_paths = {}

    # We create a fake _meta_yml_to_dict function.
    # This function is used to convert a YAML content to a dictionary
    def fake__meta_yml_to_dict(content, filename):
        return builtin_meta
    # We inject the

# Generated at 2022-06-13 15:58:13.221617
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert 'action' == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
    assert 'module' == AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library')


# Generated at 2022-06-13 15:58:19.872946
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    finder = _AnsibleCollectionFinder()
    finder._n_cached_collection_paths = ['/fake/path']
    fullname = 'faked_name'
    path = ['/fake/path']
    assert finder.find_module(fullname) == None
    assert finder.find_module(fullname, path) == None
    fullname = 'ansible'
    assert finder.find_module(fullname) == None
    assert finder.find_module(fullname, path) == None
    fullname = 'ansible_collections'
    assert finder.find_module(fullname) == None
    assert finder.find_module(fullname, path) == None
    fullname = 'ansible.plugins'
    assert finder.find_module(fullname) == None
   

# Generated at 2022-06-13 15:58:28.296419
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():

    import ansible.utils.collection_loader as cul

    if hasattr(cul, '_AnsibleInternalRedirectLoader') and callable(getattr(cul, '_AnsibleInternalRedirectLoader')):
        # Setup test objects and mock functions
        loader = getattr(cul, '_AnsibleInternalRedirectLoader')('ansible.plugins.test', None)
        loader._redirect = "ansible_collections.test.test_plugins.test"
        with patch('{0}.import_module'.format(BUILTINS), return_value=MagicMock()):
            with patch.object(sys, 'modules', autospec=True) as modules:
                # Invoke the load_module method
                result = loader.load_module('ansible.plugins.test')
                # Verification
                assert result == sys.modules

# Generated at 2022-06-13 15:58:34.871595
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
  def check_get_source(self):
    fullname = 'ansible_collections.internal.some_pkg'
    # if fullname != self._fullname:
    #   raise ValueError('this loader cannot load source for {0}, only {1}'.format(fullname, self._fullname))
    if not self._source_code_path:
      return None
    # FIXME: what do we want encoding/newline requirements to be?
    self._decoded_source = self.get_data(self._source_code_path)
    return self._decoded_source
  # this is how we test get_source as it's not exposed directly
  _AnsibleCollectionPkgLoaderBase.get_source = check_get_source
  # #here is where we check if we are working as intended
  # class _Ansible

# Generated at 2022-06-13 15:58:43.942292
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # - tests for finding a file in a collection
    # - tests for finding a python module in the ansible package
    # - tests for not finding a file
    # - tests for not finding a file in a collection
    # - tests for finding a file in a collection using a specified path
    # - uses both the py2 and py3 finders
    #
    # TODO:
    # - find something that's in multiple collections?
    # - find an ansible module that's been redirected?

    import pytest
    from ansible_collections.foo.bar.plugins.modules import baz

    # test finding a file in a collection
    acf = _AnsibleCollectionFinder()
    acf._install()

# Generated at 2022-06-13 15:58:52.172246
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ansible_module = AnsibleCollectionRef.from_fqcr(u'myns.mycoll.mymodule', u'module')
    assert ansible_module.collection == u'myns.mycoll'
    assert ansible_module.resource == u'mymodule'
    assert ansible_module.ref_type == u'module'

    ansible_module = AnsibleCollectionRef.from_fqcr(u'myns.mycoll.subdir1.subdir2.mymodule', u'module')
    assert ansible_module.collection == u'myns.mycoll'
    assert ansible_module.resource == u'mymodule'
    assert ansible_module.ref_type == u'module'

    # FIXME: this should not be accepted, subdirs must be properly validated
    ansible_

# Generated at 2022-06-13 15:58:59.881051
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # create a loader for a fake collection with an empty package
    fake_pkg_loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.fake_col.dummy', [b'/foo/bar/fake_col/dummy'])
    # test loading of a known file
    assert fake_pkg_loader.get_source('ansible_collections.fake_col.dummy') == ''
    # test loading of a non-existent file
    assert fake_pkg_loader.get_source('ansible_collections.fake_col.dummy.__init__') == None
