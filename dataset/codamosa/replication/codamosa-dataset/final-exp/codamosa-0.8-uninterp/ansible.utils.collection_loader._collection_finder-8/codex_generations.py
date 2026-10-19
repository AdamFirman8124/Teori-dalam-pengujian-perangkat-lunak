

# Generated at 2022-06-13 15:50:38.065336
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
  class TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
      self._fullname = fullname
      self._split_name = fullname.split('.')
      self._rpart_name = fullname.rpartition('.')
      self._parent_package_name = self._rpart_name[0]
      self._package_to_load = self._rpart_name[2]
      self._candidate_paths = self._get_candidate_paths(['/tmp'])
      self._subpackage_search_paths = self._get_subpackage_search_paths(self._candidate_paths)
      self._decoded_source = 'test'
      self._validate_final()

  loader = TestAnsible

# Generated at 2022-06-13 15:50:46.020366
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # Initialization of constants
    ansible_collections_fake_loader_module_path='ansible_collections/test1/test1.py'
    class_instance=_AnsibleCollectionPkgLoaderBase(ansible_collections_fake_loader_module_path, [])
    # Assertion of class method get_source
    assert ansible_collections_fake_loader_module_path==class_instance.get_source(ansible_collections_fake_loader_module_path)
test__AnsibleCollectionPkgLoaderBase_get_source()

# Generated at 2022-06-13 15:50:53.192918
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    # Create a mock package with a subpackage and a module.
    # Then create a _AnsibleCollectionPkgLoaderBase and use it to load the mock package.
    # The test ensures that the loader's is_package method returns True for the package and the subpackage,
    # but returns False for the module.
    #
    # Create a temp dir
    tempdir = os.path.join(tempfile.gettempdir(), 'ansible.test__AnsibleCollectionPkgLoaderBase_is_package')
    os.makedirs(tempdir, exist_ok=True)
    # Define a mock package
    package_name = 'ansible_collections.ns1.ns2.mock'

# Generated at 2022-06-13 15:51:00.839989
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    class DummyPkgLoader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname, path_list=None, source_code_path=None, is_package=True, subpackage_search_paths=None):
            self._source_code_path = source_code_path
            self._subpackage_search_paths = subpackage_search_paths
            self._is_package = is_package

        def is_package(self, fullname):
            return self.get_filename(fullname) is not None and self._is_package

    # ensure we return None if source_code_path and subpackage_search_paths are both False
    assert not DummyPkgLoader('foo', source_code_path=False, is_package=True, subpackage_search_paths=False).get_

# Generated at 2022-06-13 15:51:12.989819
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:51:22.393612
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    acr = AnsibleCollectionRef.from_fqcr('test.test.test_module', 'module')
    assert acr.collection == 'test.test'
    assert acr.subdirs == ''
    assert acr.ref_type == 'module'
    assert acr.resource == 'test_module'

    with pytest.raises(ValueError, match='not a valid collection reference'):
        acr = AnsibleCollectionRef.from_fqcr('test.test.test_module.py', 'module')

    acr = AnsibleCollectionRef.from_fqcr('test.test.subdir1.subdir2.test_module', 'module')
    assert acr.collection == 'test.test'
    assert acr.subdirs == 'subdir1.subdir2'

# Generated at 2022-06-13 15:51:28.181744
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.doc_fragments.beats', u'doc_fragment')
    assert AnsibleCollectionRef.try_parse_fqcr(u'myns.mycoll.myfrag', u'doc_fragment') is None

# Generated at 2022-06-13 15:51:39.240172
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    # Create a _AnsibleCollectionPkgLoaderBase object with a non-existing path
    test_loader = _AnsibleCollectionPkgLoaderBase('ansible.collections.org.ansible')
    test_loader._subpackage_search_paths = []

    # Call get_code method to test that we can handle a case where the path does not exist
    assert test_loader.get_code('ansible.collections.org.test_collections') is None

    # Create a _AnsibleCollectionPkgLoaderBase object with a valid path pointing to a python module
    test_loader._subpackage_search_paths = ['/tmp/python_code']
    test_loader._redirect_module = None
    test_loader._source_code_path = '/tmp/python_code/test_module.py'

    # Call get_

# Generated at 2022-06-13 15:51:49.843402
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    for plugin_type, plugin_dir_name in [
        ('cache', 'cache'),
        ('callback', 'callback'),
        ('console', 'console_scripts'),
        ('doc_fragment', 'doc_fragments'),
        ('filter', 'filter_plugins'),
        ('inventory', 'inventory'),
        ('lookup', 'lookup'),
        ('module_utils', 'module_utils'),
        ('modules', 'library'),
        ('netconf', 'netconf'),
        ('role', 'roles'),
        ('shell', 'shell_plugins'),
        ('terminal', 'terminal_plugins'),
        ('test', 'test'),
        ('vars', 'vars_plugins'),
    ]:
        ansible_fqcr_dict={}
        ansible_fqcr_dict['namespace'] = ['ansible']

# Generated at 2022-06-13 15:51:54.628704
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():
    loader = _AnsibleCollectionLoader('test.test.test', ['/test/test/test'])
    assert loader._AnsibleCollectionLoader__subpackage_search_paths == ['/test/test/test']
    loader = _AnsibleCollectionLoader('test.test.test', ['/test/test/test'], allows_package_code=False)
    assert loader._AnsibleCollectionLoader__subpackage_search_paths == ['/test/test/test']
    assert loader._AnsibleCollectionLoader__allows_package_code == False


# Generated at 2022-06-13 15:52:23.054626
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # initialize a module ansible.utils.collection_loader with initialized attributes:
    # _meta_yml_to_dict
    # b_routing_meta_path
    # module
    # _meta_yml_to_dict, b_routing_meta_path

    # init test values
    fullname = 'test_fullname'
    #test_answer = __AnsibleCollectionPkgLoader_load_module(fullname)

    ansible_utils_collection_loader = import_module('ansible.utils.collection_loader')

    #initialize _meta_yml_to_dict
    import ansible.parsing.yaml.loader
    _meta_yml_to_dict_func = ansible_utils_collection_loader._meta_yml_to_dict
    _meta_yml_to_dict

# Generated at 2022-06-13 15:52:24.834493
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    assert _AnsibleCollectionPkgLoaderBase().get_filename('ansible_collections.foo') == '<ansible_synthetic_collection_package>'

# Generated at 2022-06-13 15:52:33.590666
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # expected successful parses
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module')
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').collection == 'ns.coll'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').subdirs == ''
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').resource == 'resource'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').ref_type == 'module'

    # expected errors
    with raises(ValueError):
        AnsibleCollectionRef.from_fqcr('ns.coll.resource.ext', 'module')
    with raises(ValueError):
        AnsibleCollectionRef.from_

# Generated at 2022-06-13 15:52:44.940121
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import unittest
    import mock
    import tempfile
    import os
    import shutil
    import json

    class AnsibleSyntheticPackageLoaderMock(mock.Mock):
        def get_source(self, fullname):
            return None
        def get_code(self, fullname):
            return None
        def get_filename(self, fullname):
            return '<ansible_synthetic_test_package>'

    # Mock out external path
    class FakePath(object):
        def __init__(self, b_path, dirs=[], files=[]):
            self._b_path = b_path
            self._dirs = dirs
            self._files = files
        def isdir(self, path):
            return path in self._dirs

# Generated at 2022-06-13 15:52:50.278485
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    expected_collection = 'acme.remotebedrock'
    expected_subdirs = 'modules.network.cdp'
    expected_resource = 'cdp_neighbors'
    expected_ref_type = 'module'
    expected_fqcr = expected_collection + '.' + expected_subdirs + '.' + expected_resource
    actual = AnsibleCollectionRef.from_fqcr(expected_fqcr, expected_ref_type)
    actual_fqcr = actual.fqcr
    assert actual_fqcr == expected_fqcr

    expected_collection = 'acme.remotebedrock'
    expected_subdirs = ''
    expected_resource = 'cdp_neighbors'
    expected_ref_type = 'module'
    expected_fqcr = expected_collection + '.' + expected

# Generated at 2022-06-13 15:52:56.556258
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    try:
        loader.load_module('ansible_collections.somens')
        assert(False)
    except Exception as e:
        assert(e.args == ('this loader can only load packages from the ansible_collections package, not ansible_collections.somens',))


# Generated at 2022-06-13 15:53:02.509263
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    import sys
    import pdb
    import tempfile
    from unittest.mock import patch
    from unittest.mock import MagicMock

    result = pdb.runcall(lambda x: x, 'foo')

    print('get_code')

    # test get_code() on a module
    with tempfile.TemporaryDirectory(prefix='ansible_collections_test') as test_dir:
        source_path = os.path.join(test_dir, '__init__.py')
        with open(source_path, 'w') as f:
            f.write('def foo():\n    print("bar")\n')
        loader = _AnsibleCollectionPkgLoaderBase('ansible.collections.foo', path_list=[test_dir])

# Generated at 2022-06-13 15:53:05.597826
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():

    # Note: this function is not automatically generated by testinfra

    # TODO: check that returned value is a string
    # TODO: check that returned value is the expected string
    # TODO: add other test cases
    pass

# Generated at 2022-06-13 15:53:10.476809
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
  import sys
  import types
  import os
  import os.path
  # Create the module object.
  name = 'ansible_collections.collection_name.module_name'
  module = types.ModuleType('module_name')
  # Put it in sys.modules so the next import statement will use that module.
  sys.modules[name] = module
  # Import the module.
  exec ('import ansible_collections.collection_name.module_name\n')
  ret = module
  assert ret == 'module_name'


# Generated at 2022-06-13 15:53:22.539847
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ref = AnsibleCollectionRef.from_fqcr('ns.coll.resource', ref_type='module')
    assert ref.collection == 'ns.coll'
    assert ref.subdirs == ''
    assert ref.resource == 'resource'
    assert ref.ref_type == 'module'

    ref = AnsibleCollectionRef.from_fqcr('ns.coll.subdir.resource', ref_type='module')
    assert ref.collection == 'ns.coll'
    assert ref.subdirs == 'subdir'
    assert ref.resource == 'resource'
    assert ref.ref_type == 'module'

    ref = AnsibleCollectionRef.from_fqcr('ns.coll.role', ref_type='role')
    assert ref.collection == 'ns.coll'
    assert ref.subdirs == ''

# Generated at 2022-06-13 15:54:00.320144
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    """Unit test for method load_module of class _AnsibleCollectionPkgLoader"""

    class MockAnsibleCollectionConfig(object):
        class MockEvent(object):
            def fire(self, **kwargs):
                pass

        on_collection_load = MockEvent()

    mock_MockAnsibleCollectionConfig_class = mocker.patch('ansible.utils.collection_loader.AnsibleCollectionConfig', new=MockAnsibleCollectionConfig)

    mock_import_module = mocker.patch('ansible.utils.collection_loader.import_module')

    mock_meta_yml_to_dict = mocker.patch('ansible.utils.collection_loader.MetaYmlParser._meta_yml_to_dict')

    mock_ns_name = 'my.namespace'

# Generated at 2022-06-13 15:54:01.200153
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    assert True


_collection_pkg_loader_cache = {}



# Generated at 2022-06-13 15:54:09.322978
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    def _test_iter_modules(test_path, test_prefix, ansible_collection):
        test_loader = _AnsibleCollectionPkgLoaderBase(fullname=ansible_collection, path_list=[test_path])
        module_generator = test_loader.iter_modules(test_prefix)
        module_list = [module for module in module_generator]  # exercise the generator
        return module_list

    test_path = os.path.join(os.path.dirname(__file__), 'data', 'packageloader_integration_tests')
    test_prefix = 'ansible_collections.fortinet.fortinet'
    module_list = _test_iter_modules(test_path, test_prefix, test_prefix)


# Generated at 2022-06-13 15:54:13.908780
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='test', path_list=['/'])
    assert None == loader.get_data('__init__.py')
    assert None == loader.get_data(None)
    assert '' == loader.get_data('/__init__.py')



# Generated at 2022-06-13 15:54:25.727149
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # These tests are run in the context of a pkg_resource import hook, so they will try to use the
    # pkg_resources.get_distribution code to load things. This code is not present on Python 3.7 and
    # later, and either a pkg_resources scatter-gather or the Python 3.7.2+ importlib.metadata API's
    # is used. This means that these tests fail if you run them in the context of a Python 3.7 or later
    # process, so we will skip them if that is the case.
    if PY2 or sys.version_info[1] < 7:
        # create an empty test collection and loader
        with tempfile.TemporaryDirectory() as td:
            fake_collection_path = os.path.join(td, 'ansible_collections', 'collection_one')
            os

# Generated at 2022-06-13 15:54:33.101841
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    import test.unit.test_loader
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.mycollection.myns', [test.unit.test_loader.DATA_PATH])
    modules = set([m[1] for m in loader.iter_modules(prefix='ansible_collections.mycollection.myns.mypkg')])
    assert(modules == set(['mypkg.a', 'mypkg.b', 'mypkg.c']))



# Generated at 2022-06-13 15:54:40.444429
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    """
    Test for AnsibleCollectionRef.is_valid_fqcr
    :return:
    """
    assert AnsibleCollectionRef.is_valid_fqcr('foo') == True
    assert AnsibleCollectionRef.is_valid_fqcr('foo.bar') == True
    assert AnsibleCollectionRef.is_valid_fqcr('foo.bar.baz') == True
    assert AnsibleCollectionRef.is_valid_fqcr('foo.bar.baz.qux') == True
    assert AnsibleCollectionRef.is_valid_fqcr('foo.bar.baz.qux.quux') == True
    assert AnsibleCollectionRef.is_valid_fqcr(u'foo.bar') == True

# Generated at 2022-06-13 15:54:47.654508
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    print('AnsibleCollectionRef.is_valid_fqcr()\n')

    print(AnsibleCollectionRef.VALID_REF_TYPES)

    print(AnsibleCollectionRef.is_valid_fqcr('ansible.builtin.action.ping', 'action'))
    print(AnsibleCollectionRef.is_valid_fqcr('ansible.builtin.action.ping', 'action'))
    print(AnsibleCollectionRef.is_valid_fqcr('ansible.builtin.action.mymodule', 'action'))
    print(AnsibleCollectionRef.is_valid_fqcr('ansible.builtin.action.mymodule', 'module'))


# Generated at 2022-06-13 15:54:58.508228
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():  # pylint:disable=missing-docstring,invalid-name
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils._text import to_bytes
    from io import StringIO
    from importlib import util
    from tempfile import TemporaryDirectory
    import shutil
    import types
    import sys

    # Module to load
    module_name = 'test_package.test_module'

    assert AnsibleCollectionConfig.collection_finder is not None

    # Get module loader.
    module_spec = util.find_spec(module_name)
    assert module_spec is not None

    module_loader = module_spec.loader

    assert module_loader is not None

    # Create temporary package directories.
    temporary_directory_path = None

# Generated at 2022-06-13 15:55:01.843344
# Unit test for constructor of class _AnsibleCollectionNSPkgLoader
def test__AnsibleCollectionNSPkgLoader():
    try:
        loader = _AnsibleCollectionNSPkgLoader('fail')
        assert False, "This code is unreachable"
    except ImportError:
        loader = None

    loader = _AnsibleCollectionNSPkgLoader('')
    assert loader

    loader = _AnsibleCollectionNSPkgLoader('ansible_collections.hello')
    assert loader

    try:
        loader = _AnsibleCollectionNSPkgLoader('ansible_collections.hello.hello')
        assert False, "This code is unreachable"
    except ImportError:
        loader = None



# Generated at 2022-06-13 15:56:00.318058
# Unit test for method is_valid_collection_name of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_collection_name():
    # test invalid names
    invalid_names = [
        "",  # empty string
        ".",  # single dot
        "..",  # double dot
        "ansible.module_utils.",  # trailing dot
        "ansible.module_utils",  # trailing
        "ansible.module..utils",  # double dots
        "ansible.module.utils.test",  # multiple segments
        "ansible.module_utils.test",  # not a valid Python name
    ]
    for name in invalid_names:
        assert not AnsibleCollectionRef.is_valid_collection_name(name)

    # test valid names
    valid_names = [
        "ansible.module_utils",
    ]
    for name in valid_names:
        assert AnsibleCollectionRef.is_valid_collection_name(name)




# Generated at 2022-06-13 15:56:09.077594
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    class TestLoader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname, path_list=None):
            self._source_code_path = None
            super(TestLoader, self).__init__(fullname, path_list=path_list)

    test_loader = TestLoader('ansible_collections.fake_ns.fake_coll.fake_pkg')
    assert test_loader._rpart_name[2] == 'fake_pkg'
    assert test_loader._parent_package_name == 'ansible_collections.fake_ns.fake_coll'
    assert test_loader._split_name == ['ansible_collections', 'fake_ns', 'fake_coll', 'fake_pkg']
    assert test_loader.get_source(test_loader._fullname) is None
    assert test

# Generated at 2022-06-13 15:56:18.792880
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # is the exception ValueError correctly raised?
    # mocked object, we only want to test if the method is correctly catching the exception
    collection_finder_mock = MagicMock()
    # mocked object, we only want to test if the method is correctly catching the exception
    pathctx_mock = MagicMock()
    collection_finder_mock.find_module.return_value = None
    path_hook_finder = _AnsiblePathHookFinder(collection_finder_mock, pathctx_mock)
    with pytest.raises(ValueError):
        path_hook_finder.find_module('ansible', path=None)



# Generated at 2022-06-13 15:56:23.781585
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:56:28.973582
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    path_list = ["/tmp/ansible_collections/ansible_collections/my_namespace/my_collection"]
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.my_namespace.my_collection", path_list=path_list)
    result = loader.is_package("ansible_collections.my_namespace.my_collection")
    assert result is True, "_AnsibleCollectionPkgLoaderBase_is_package failed"

# Generated at 2022-06-13 15:56:38.875613
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # Path to the collection
    collection_path = "/tmp"
    # Available package in the collection's source path
    package = "test_package"
    # Packages under the package
    sub_packages = ["sub_package_1","sub_package_2"]
    # Current package path
    current_package_path = os.path.join(collection_path, package)
    # Subpackages paths
    sub_packages_paths = [os.path.join(current_package_path,sp) for sp in sub_packages]
    # Prepare the test scenario
    # Collection path, valid package
    os.mkdir(collection_path)
    os.mkdir(current_package_path)
    # Package's subpackages

# Generated at 2022-06-13 15:56:44.854703
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    paths = ['tests/fixtures/collections']

    loader = _AnsibleCollectionFinder(paths)

    result = loader.find_module('ansible_collections.somens')
    assert result.__class__.__name__ == '_AnsibleCollectionNSPkgLoader'

    result = loader.find_module('ansible_collections.somens.somecollection')
    assert result.__class__.__name__ == '_AnsibleCollectionPkgLoader'

    result = loader.find_module('ansible_collections.somens.somecollection.plugins.modules.some_collection_module')
    assert result.__class__.__name__ == '_AnsibleCollectionLoader'


# Generated at 2022-06-13 15:56:51.626594
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():

    file_content = 'Hello World!'

    def get_data(self, path):
        if path == '/file_path':
            return file_content
        else:
            return None

    with patch.object(_AnsibleCollectionPkgLoaderBase, 'get_data', side_effect=get_data):
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.col_name', path_list=['/path'])
        assert loader.get_data("/file_path") == file_content



# Generated at 2022-06-13 15:56:56.303103
# Unit test for method from_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:57:03.627750
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    """Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase"""

    # We should not be able to load a module from a path that does not exist
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase.load_module('ansible.test', path=['/path/does/not/exist'])

    # If a module is already in sys.modules, then it should just be aliased
    fullname = 'ansible_collections.ansible.test'
    # We cannot create a new module object here, because "module" refers to this module, which is already in sys.modules
    module = sys.modules[fullname]

    ldr = _AnsibleCollectionPkgLoaderBase(fullname, path=['/path/does/not/exist'])
    ldr_red