

# Generated at 2022-06-13 15:50:11.051760
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    import ansible_collections
    from ansible_collections.ansible.amazon.plugins.module_utils.ec2 import test
    assert _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ansible.amazon.plugins.module_utils').is_package(fullname='ansible_collections.ansible.amazon')
    assert _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ansible.amazon.plugins.module_utils').is_package(fullname='ansible_collections.ansible.amazon.plugins')
    assert not _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ansible.amazon.plugins.module_utils').is_package(fullname='ansible_collections.ansible.amazon.plugins.module_utils.ec2')

# Generated at 2022-06-13 15:50:20.566188
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # Test 1
    class TestClass1(AnsibleCollectionPackageLoader):
        pass
    class TestClass2(AnsibleCollectionPackageLoader):
        def _get_candidate_paths(self, path_list):
            return [os.path.join(p, self._package_to_load) for p in path_list]
    # Test 2
    class TestClass3(AnsibleCollectionPackageLoader):
        def load_module(self, fullname):
            class TestClass:
                pass

            return TestClass()
    class TestClass4(AnsibleCollectionPackageLoader):
        def __init__(self, fullname, path_list=None):
            pass

# Generated at 2022-06-13 15:50:26.637679
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    class __Test__AnsibleCollectionPkgLoaderBase(
            _AnsibleCollectionPkgLoaderBase
    ):
        def _synthetic_filename(self, fullname):
            return '{0}/__init__.py'.format(fullname)

    # Python 2
    if not PY3:
        assert __Test__AnsibleCollectionPkgLoaderBase('ansible_collections.foo.bar', path_list=['/usr']).get_filename('ansible_collections.foo.bar') == '/usr/foo/__init__.py'

    # Python 3

# Generated at 2022-06-13 15:50:37.863900
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    testcase = unittest.TestCase()
    # mock base class to get a usable object
    class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        _allows_package_code = True

    # create instance of base class
    mloader = MockAnsibleCollectionPkgLoaderBase('ns.pkg')
    # test case: load_module() - success
    ns = mloader.load_module('ns.pkg')
    testcase.assertEqual(ns.__package__, 'ns.pkg')
    # test case: load_module() - raise exception
    mloader._subpackage_search_paths = []
    with testcase.assertRaises(ImportError):
        ns = mloader.load_module('ns.pkg')



# Generated at 2022-06-13 15:50:48.144943
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    module_name = 'ansible.builtin.something'
    loader = _AnsibleInternalRedirectLoader(module_name, ['/fake/path/1', '/fake/path/2'])
    assert loader is not None

    assert loader._redirect is None

    module_name = 'ansible.builtin.something.else'
    loader = _AnsibleInternalRedirectLoader(module_name, ['/fake/path/1', '/fake/path/2'])
    assert loader is not None

    assert loader._redirect == 'ansible.plugins.something.else'

    module_name = 'ansible.builtin.something_else'
    loader = _AnsibleInternalRedirectLoader(module_name, ['/fake/path/1', '/fake/path/2'])
    assert loader is not None

    assert loader

# Generated at 2022-06-13 15:50:57.771656
# Unit test for method is_valid_collection_name of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_collection_name():
    # Test valid collection name
    collection = 'ansible.builtin'
    assert AnsibleCollectionRef.is_valid_collection_name(collection) is True

    # Test invalid collection name (missing dot)
    assert AnsibleCollectionRef.is_valid_collection_name('ansiblebuiltin') is False

    # Test invalid collection name (extra dot)
    assert AnsibleCollectionRef.is_valid_collection_name('ansible.builtin.something') is False

    # Test invalid collection name (keyword)
    assert AnsibleCollectionRef.is_valid_collection_name('ansible.true') is False

    # Test invalid collection name (contains special character)
    assert AnsibleCollectionRef.is_valid_collection_name('ansible.built&n') is False


# Generated at 2022-06-13 15:51:07.437274
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():
    loader = _AnsibleCollectionLoader('foo.bar.baz', ['/fake/path'])
    assert loader._collection_search_paths == ['/fake/path'], 'Constructor did not set _collection_search_paths properly'
    assert loader._split_name == ['foo', 'bar', 'baz'], 'Constructor did not set _split_name properly'
    assert loader._package_to_load == 'baz', 'Constructor did not set _package_to_load properly'
    assert loader._fullname == 'foo.bar.baz', 'Constructor did not set _fullname properly'


# Generated at 2022-06-13 15:51:12.719083
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():

    test_file = '/test'
    loader = _AnsibleCollectionPkgLoaderBase('', [test_file])
    with patch.object(loader, 'get_data', return_value='foobar'):
        assert loader.get_data(test_file) == 'foobar'



# Generated at 2022-06-13 15:51:19.544839
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    import ansible.utils.collection_loader as collection_loader
    
    # initialize attribute _meta_yml_to_dict
    collection_loader._meta_yml_to_dict = lambda x, y: {}
    
    def test_load_module(routing_meta_path, expected_result):
        import ansible.utils.collection_loader as collection_loader
        loader = collection_loader._AnsibleCollectionPkgLoader(fullname='ansible.collections.ns1.pkg1',
                                                         path=[routing_meta_path],
                                                         package_to_load='pkg1')
        module = loader.load_module('ansible.collections.ns1.pkg1')
        assert module._collection_meta == expected_result
        assert module.__loader__._collection_meta == expected_result

# Generated at 2022-06-13 15:51:25.795031
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():

    if not os.path.isfile("./loader.py"):
        print("write_collection: file not found ./loader.py")
        assert(False)


    fullname = "ansible.collections.test.test.test"
    loader = _AnsibleCollectionLoader(fullname)
    assert(loader._testname == 'test')
    assert(loader._split_name == ['ansible', 'collections', 'test', 'test', 'test'])

    # The variable _ansible_collection_paths is a global variable
    # So, we need to setup a global variable before calling code
    # This is the reason why we call import_module()
    if '_ansible_collection_paths' not in globals():
        globals()['_ansible_collection_paths'] = []

# Generated at 2022-06-13 15:52:33.532570
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:52:40.892485
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    import os
    import sys

    import ansible

    ansible_import_path = os.path.dirname(ansible.__path__[0])
    collection_finder = _AnsibleCollectionFinder(paths=sys.path)
    path_hook = collection_finder._ansible_collection_path_hook(ansible_import_path)
    assert path_hook is not None, "_ansible_collection_path_hook returned None"



# Generated at 2022-06-13 15:52:41.463565
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    pass


# Generated at 2022-06-13 15:52:49.906401
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    def get_filename_mocks(self, fullname):
        filename = '/path/to/synthetic'
        return filename

    def mock_is_package(fullname):
        return True

    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.acme.awesome_col')
    fullname = 'ansible_collections.acme.awesome_col'
    loader._is_package = mock.Mock(side_effect=mock_is_package)
    loader.get_filename = get_filename_mocks
    assert loader.get_filename(fullname) == '/path/to/synthetic'

    def get_filename_mocks(self, fullname):
        filename = '/path/to/sources'
        return filename

    loader = _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:53:00.476988
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # Note: Implementing unit tests for individual methods of class loader is non-trivial, and probably should be reconsidered at some point.
    # However, we're currently using the loader mechanism to make some important decisions that affect which namespaces
    # certain Ansible modules will be loaded into, so we do have a few tests here.
    import sys
    from ansible.utils.path import unfrackpath
    test_data_dir = unfrackpath(os.path.join(os.path.dirname(__file__), 'testdata'))

    _old_modules = sys.modules.copy()

# Generated at 2022-06-13 15:53:04.911304
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    module = new_module_named('ansible_collections.ansible.test')
    module.__loader__ = _AnsibleCollectionPkgLoaderBase('ansible_collections.ansible.test')
    assert module.__loader__
    assert module.__loader__.__class__.__name__ == '_AnsibleCollectionPkgLoaderBase'


# Generated at 2022-06-13 15:53:09.980680
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    ref = AnsibleCollectionRef('namespace.collection_name', subdirs='somemodule', resource='module_name', ref_type='module')
    result = repr(ref)
    assert result == "AnsibleCollectionRef(collection='namespace.collection_name', subdirs='somemodule', resource='module_name')"



# Generated at 2022-06-13 15:53:15.851241
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    assert AnsibleCollectionRef('ns.coll', u'subdir1.subdir2', 'resource', 'module') == \
           AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.subdir2.resource', 'module')


# Generated at 2022-06-13 15:53:21.471377
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    obj = AnsibleCollectionRef(to_text('foo.bar'), to_text(u'subdir1.subdir2'), to_text('baz'), 'role')
    assert obj.__repr__() == 'AnsibleCollectionRef(collection=u\'foo.bar\', subdirs=u\'subdir1.subdir2\', resource=u\'baz\')'



# Generated at 2022-06-13 15:53:23.080521
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    _AnsibleCollectionFinder()



# Generated at 2022-06-13 15:54:02.484639
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    class Mock_module:
        pass
    class Mock_sys:
        class modules:
            pass
    mock_module = Mock_module()
    mock_sys = Mock_sys()
    mock_sys.modules = Mock_sys.modules()

    builtin_meta = {
        "import_redirection": {
            "ansible.module_utils.basic": {"redirect": "ansible.builtin.module_utils.basic"},
            "ansible.module_utils.mouse": {"redirect": "ansible.builtin.module_utils.mouse"}
        }
    }
    def _get_collection_metadata(collection_name):
        return builtin_meta


# Generated at 2022-06-13 15:54:07.827329
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    from ansible_collections.ansible.builtin import test_utils
    for obj in test_utils.find_object('AnsibleCollectionRef', 'from_fqcr', '#FQCR_TEST'):
        fqcr, ref_type, expected, hint = obj.args
        expected = expected.replace('%type%', ref_type)
        result = AnsibleCollectionRef.from_fqcr(fqcr, ref_type)
        assert result == eval(expected), hint


# Generated at 2022-06-13 15:54:18.796516
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ref_type = 'module'
    collection_name = 'ansible.test_collection'
    subdirs = 'subdir1.subdir2'
    resource = 'test_plugin'
    fqcr = 'ansible.test_collection.subdir1.subdir2.test_plugin'

    ref = AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

    assert ref.n_python_collection_package_name == 'ansible_collections.ansible.test_collection'
    assert ref.n_python_package_name == 'ansible_collections.ansible.test_collection.plugins.subdir1.subdir2.module'
    assert ref.collection == 'ansible.test_collection'
    assert ref.subdirs == 'subdir1.subdir2'

# Generated at 2022-06-13 15:54:28.710436
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    from ansible.utils.collection_loader import AnsibleCollectionRef
    test_1 = 'lookup_plugins'
    test_1_expected_result = 'lookup'
    test_2 = 'action_plugins'
    test_2_expected_result = 'action'
    test_3 = 'test_plugins'
    test_3_expected_result = 'test'
    test_4 = 'modules'  # is not a valid collection directory name
    test_5 = 'library'
    test_5_expected_result = 'modules'
    test_6 = 'ansible.module_utils'
    test_6_expected_result = 'module_utils'
    test_7 = 'library.module_utils'
    test_7_expected_result = 'module_utils'

# Generated at 2022-06-13 15:54:32.883483
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    assert AnsibleCollectionRef(u'namespace.colname', u'subdir1.subdir2', u'modulename', u'module') == eval(repr(AnsibleCollectionRef(u'namespace.colname', u'subdir1.subdir2', u'modulename', u'module')))

# Generated at 2022-06-13 15:54:40.321166
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # test_action_to_action_plugin
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

    # test_action_plugin_to_action
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action') == 'action'

    # test_callback_to_callback_plugin
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'

    # test_filter_to_filter_plugin
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'

    # test_lookup_to_lookup_plugin

# Generated at 2022-06-13 15:54:49.014361
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    test_dir = os.path.dirname(os.path.realpath(__file__)) + "/test_iter_modules/"

    # Iterate over all modules of a collection (on disk)
    pkg_loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.my_collection", [test_dir])
    modules = [m for m in pkg_loader.iter_modules("ansible_collections.my_collection")]


# Generated at 2022-06-13 15:54:59.150987
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():

    # test good collections
    # type_array = ['action', 'become', 'cache', 'callback', 'cliconf', 'connection',
    # 'doc_fragments', 'filter', 'httpapi', 'inventory', 'lookup',
    # 'module_utils', 'modules', 'netconf', 'role', 'shell', 'strategy',
    # 'terminal', 'test', 'vars', 'playbook']

    # Action
    ref = AnsibleCollectionRef.try_parse_fqcr('myfile.mymods.myactions', 'action')
    assert ref.collection == "myfile.mymods"
    assert ref.subdirs == ""
    assert ref.resource == "myactions"
    assert ref.ref_type == "action"


# Generated at 2022-06-13 15:55:11.199838
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from _collections_loader_test_case import _CollectionsLoaderTestCase
    ns_name = 'ansible_collections_testnamespace'
    coll_name = 'testcollection'
    coll_path = os.path.join(os.getcwd(), 'test_collections', 'testnamespace', 'testcollection')
    coll_path = os.path.normpath(coll_path)
    coll_pkg_path = os.path.join(coll_path, 'plugins')
    playbook_path = os.path.normpath(os.path.join(coll_path, 'playbooks'))
    os.environ['ANSIBLE_NOCOLLECT_PATH'] = coll_path
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ':'.join([coll_path, playbook_path])

   

# Generated at 2022-06-13 15:55:21.822813
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    class _TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionsPathHookFinder.TestAnsibleCollectionFinder, _AnsibleCollectionPkgLoaderBase):
        pass
    p = os.path.join(C.DEFAULT_LOCAL_TMP, 'test__AnsibleCollectionPkgLoaderBase_iter_modules_0')
    os.makedirs(p)
    loader = _TestAnsibleCollectionPkgLoaderBase('ansible_collections.test', p)
    result = loader.iter_modules('test')
    assert next(result) == ('test', False)
    with open(os.path.join(p, '__init__.py'), 'w+') as f:
        f.write('#')

# Generated at 2022-06-13 15:55:59.825183
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # check with fqcr and ref_type arguments
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').n_python_package_name == 'ansible_collections.ns.coll.plugins.module'
    # check with fqcr and ref_type arguments, giving subdir
    assert AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.resource', 'module').n_python_package_name == 'ansible_collections.ns.coll.plugins.subdir1.module'
    # check with fqcr and ref_type arguments, ref_type is role
    assert AnsibleCollectionRef.from_fqcr('ns.coll.role', 'role').n_python_package_name == 'ansible_collections.ns.coll.roles.role'
    # check

# Generated at 2022-06-13 15:56:03.341519
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    fullname = "ansible.test"
    path_list = ["path1","path2","path3"]
    instance = _AnsibleInternalRedirectLoader(fullname, path_list)
    assert hasattr(instance, '_redirect') == False
    assert instance.load_module("abc") == None
    
    

# Generated at 2022-06-13 15:56:10.971946
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
  prefix = "ansible_collections."
  name = "jdauphant.nginx"
  fullname = "ansible_collections.jdauphant.nginx"
  path = ""
  namespace = "jdauphant"
  collection = "nginx"
  github_path = path+"/ansible_collections/jdauphant/nginx/"

  sys.modules['ansible_collections.jdauphant.nginx'] = ModuleType(fullname)
  col_loader = AnsibleCollectionPackageLoader(prefix, path)
  mod = col_loader.load_module(fullname)
  assert mod.__package__ == fullname
  assert mod.__file__ == github_path+"__init__.py"
  assert mod.__name__ == fullname

# Generated at 2022-06-13 15:56:22.528778
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.subdir2.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll1.coll2.subdir1.resource')

    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.subdir2.subdir3.resource')
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.subdir2.subdir3.subdir4.resource')

# Generated at 2022-06-13 15:56:27.659745
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    loader = _AnsibleCollectionPkgLoaderBase('ansible.collections.ansible-collections.org', path_list=['/ansible/collections/ansible-collections/org'])
    assert loader.load_module(loader._fullname) == loader.load_module(loader._fullname)
    assert loader.load_module(loader._fullname) == loader.load_module(loader._fullname)

# Generated at 2022-06-13 15:56:38.393760
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    for input_args, expected_output in [
        ([], ValueError),
        (['test1.py'], None),
        (['/not/a/file'], None),
        (['/not/a/file/test1.py'], None),
        (['/tmp/test1.py'], None),
        (['/tmp/__init__.py'], ''),
        (['__init__.py'], None),
        (['__init__.py', '/tmp'], None),
        (['__init__.py', '/tmp/'], ''),
        (['/tmp/foo/__init__.py'], ''),
        (['foo/__init__.py', '/tmp'], ''),
    ]:

        fd = open('/tmp/test1.py', 'w')


# Generated at 2022-06-13 15:56:39.255552
# Unit test for constructor of class _AnsibleCollectionRootPkgLoader
def test__AnsibleCollectionRootPkgLoader():
    cl = _AnsibleCollectionRootPkgLoader('ansible_collections')
    assert cl


# Generated at 2022-06-13 15:56:43.983943
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
   # Load fixture
   fixture = loadfixture('test__AnsibleCollectionPkgLoaderBase_get_source')

   # Load AnsibleCollectionPkgLoaderBase instance
   testinstance = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections", path_list=fixture[0])

   # Run the method and validate the result
   assert testinstance.get_source(fullname="ansible_collections") == fixture[1]


# Generated at 2022-06-13 15:56:55.473388
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    """ test__AnsibleCollectionPkgLoaderBase_load_module """
    from collections import namedtuple
    from ansible.utils.display import Display

    # before import ansible we need to redirect output, because ansible
    # imports logging and it will be configured as soon as we trigger an
    # import of ansible
    fake_display = Display()
    fake_display.display = lambda *args, **kwargs: None
    Display.verbosity = 4

    # we need to patch the display class before we start the import of
    # ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.basic

# Generated at 2022-06-13 15:57:07.014238
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    assert u'ansible.builtin.get_url' == AnsibleCollectionRef(u'ansible.builtin', None, u'get_url', u'module').fqcr

    # Test constructor with valid namespace and collection name
    assert u'namespace.collectionname' == AnsibleCollectionRef(u'namespace.collectionname', None, u'dummy_resource', u'dummy_ref_type').fqcr

    # Test constructor with invalid namespace and collection name
    bad_namespace = u'namespace_collectionname'
    with pytest.raises(ValueError) as excinfo:
        AnsibleCollectionRef(bad_namespace, None, u'dummy_resource', u'dummy_ref_type')

# Generated at 2022-06-13 15:57:34.488178
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # TODO: return the correct module instead of the collection_loader
    loader = _AnsibleCollectionPkgLoader('ansible.foo', ['foo', 'bar'], None)
    assert isinstance(loader.load_module('ansible.foo'), _AnsibleCollectionPkgLoader)



# Generated at 2022-06-13 15:57:37.579401
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import tempfile
    import os

    class _TestLoader(_AnsibleCollectionPkgLoaderBase):
        pass

    # module code to import (ensure we don't match any Python implicit modules)

# Generated at 2022-06-13 15:57:47.975156
# Unit test for constructor of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase():
    col_loader_base = _AnsibleCollectionPkgLoaderBase('ansible_collections.test1.test2')
    assert col_loader_base._fullname == 'ansible_collections.test1.test2'
    assert col_loader_base._redirect_module is None
    assert col_loader_base._split_name == ['ansible_collections', 'test1', 'test2']
    assert col_loader_base._rpart_name == ('ansible_collections.test1', '.', 'test2')
    assert col_loader_base._parent_package_name == 'ansible_collections.test1'
    assert col_loader_base._package_to_load == 'test2'
    assert col_loader_base._source_code_path is None
    assert col_loader_base._decoded

# Generated at 2022-06-13 15:57:52.751660
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # Case 1: Positive Case
    acr = AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.subdir2.resource', 'module')
    assert acr.collection == 'ns.coll'
    assert acr.subdirs == 'subdir1.subdir2'
    assert acr.resource == 'resource'
    assert acr.ref_type == 'module'

    # Case 2: Positive Case
    acr = AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module')
    assert acr.collection == 'ns.coll'
    assert acr.subdirs == ''
    assert acr.resource == 'resource'
    assert acr.ref_type == 'module'

    # Case 3: Positive Case
    acr = AnsibleCollectionRef.from_fq

# Generated at 2022-06-13 15:57:59.321029
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somesubns')
    # import os
    # test_code_obj = compile(source="print('Hello, World!')", filename=os.path.abspath('./test_code.py'), mode='exec', flags=0, dont_inherit=True)
    test_code_obj = compile(source="pass", filename='<string>', mode='exec', flags=0, dont_inherit=True)
    loader._compiled_code = test_code_obj
    assert test_code_obj == loader.get_code('ansible_collections.somens.somesubns')

# Generated at 2022-06-13 15:58:10.585234
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # m = mock.MagicMock()
    m = {};
    m.__loader__ = None
    m.__file__ = "/home/travis/build/ansible/ansible/lib/ansible/module_utils/six/__init__.py"
    m.__package__ = "ansible_collections.ansible.builtin.plugins"

    class _AnsibleCollectionPkgLoaderBaseMock(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            pass

        def _get_subpackage_search_paths(self, candidate_paths):
            pass

        def _validate_final(self):
            pass


# Generated at 2022-06-13 15:58:17.203011
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    #
    # Test for #29553 - Fix package variant of galaxy collection loader's load_module to support __path__ (potential)
    #
    class TestPhonyPkgLoader(ansible_collections.import_plugins.loader._AnsibleCollectionPkgLoaderBase):
        def __init__(self):
            self.test_result = None
            self._subpackage_search_paths = ['/tmp/foo']
            self._fullname = 'ansible_collections.foo.bar'
            self._source_code_path = '/tmp/foo/__init__.py'
            self._redirect_module = None
            self._split_name = self._fullname.split('.')
            self._rpart_name = self._fullname.rpartition('.')
            self._parent_package_name = self._

# Generated at 2022-06-13 15:58:27.217290
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename', 'role')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.playbookname.yaml', 'playbook')

    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource.py')
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource.txt')
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource.yml')

# Generated at 2022-06-13 15:58:37.366533
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    cpl = _AnsibleCollectionPkgLoaderBase('foo')
    assert cpl.get_source('foo') is None
    # test get_source where we have a source code path but source is not yet loaded
    cpl._source_code_path = '/foo/bar'
    with mock.patch.object(cpl, 'get_data') as fake_get_data:
        fake_get_data.return_value = 'source code'
        assert cpl.get_source('foo') == 'source code'
        assert cpl._decoded_source == 'source code'
        fake_get_data.assert_called_once_with('/foo/bar')

    # test get_source where it's already cached
    res = cpl.get_source('foo')
    assert cpl._decoded_source == 'source code'

# Generated at 2022-06-13 15:58:41.649617
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    # Test case data
    fullname = "ansible_collections.test_collection.test_sub_collection.test_sub_sub_collection"
    cls = _AnsibleCollectionPkgLoaderBase(fullname)
    fullname = "ansible_collections.test_collection.test_sub_collection.test_sub_sub_collection"

    # Execution
    is_package = cls.is_package(fullname)

    # Verification
    assert is_package == False