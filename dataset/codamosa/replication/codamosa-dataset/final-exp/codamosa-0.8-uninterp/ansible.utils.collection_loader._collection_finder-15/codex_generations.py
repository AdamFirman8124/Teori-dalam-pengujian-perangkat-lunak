

# Generated at 2022-06-13 15:50:02.688694
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    _fullname = 'ansible_collections.my.namespace'
    _redirect_module = None
    _split_name = _fullname.split('.')
    _rpart_name = _fullname.rpartition('.')
    _parent_package_name = 'ansible_collections.my'
    _package_to_load = 'namespace'

    _test_instance = _AnsibleCollectionPkgLoaderBase(_fullname, ['path/to/collections'])
    _test_instance._parent_package_name = _parent_package_name
    _test_instance._package_to_load = _package_to_load
    _test_instance._fullname = _fullname
    _test_instance._redirect_module = _redirect_module
    _test_instance._split_name = _

# Generated at 2022-06-13 15:50:09.085777
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:50:18.029676
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():

    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename.yaml')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename.yml')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.playbookname.yaml')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.playbookname.yml')


# Generated at 2022-06-13 15:50:27.680489
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    package_name = 'dummy_package'
    module_name = 'ns.collection.dummy_package'
    module_name_test = module_name.replace('.', '_')

    # setup dummy module in sys.modules
    sys.modules[module_name] = ModuleType(module_name)

    # setup dummy collection path and metadata
    collection_path = '/tmp/ansible_collections/ns/collection/dummy_package'

    # setup dummy package init code
    package_init_code = '''
print('package init code called')
'''
    os.makedirs(to_bytes(collection_path))
    init_file_path = os.path.join(collection_path, '__init__.py')

# Generated at 2022-06-13 15:50:36.453685
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('not.ansible', [])

    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.foo', [])

    try:
        _AnsibleInternalRedirectLoader('ansible.builtin.foo', [])
    except ImportError:
        pytest.fail("Not able to create instance of _AnsibleInternalRedirectLoader")

test__AnsibleInternalRedirectLoader()

# Implements the Ansible Python module import hook, which looks for imported names that match special Ansible
# module namespaces, and then delegates to _AnsibleInternalRedirectLoader and _AnsibleCollectionLoader

# Generated at 2022-06-13 15:50:39.918759
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # Path hook finder needs a creator class
    creator = _AnsibleCollectionFinder(paths=['/dummy-collections-base-path'])

    path_hook_finder = _AnsiblePathHookFinder(collection_finder=creator, pathctx='/dummy-collections-base-path/ansible_collections')
    pkg_meta_path_finder = _AnsibleCollectionRootPkgLoader(fullname='ansible_collections', path_list=['/dummy-collections-base-path'])

    assert path_hook_finder.find_module('ansible_collections') == pkg_meta_path_finder



# Generated at 2022-06-13 15:50:42.578748
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.connection import ConnectionModule
    obj = ConnectionModule()
    assert obj.get_source() != None

# Generated at 2022-06-13 15:50:48.220269
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    import ansible.module_utils.six as six
    import ansible.module_utils.basic as basic
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.basic', None)
    basic2 = loader.load_module('ansible.module_utils.basic')
    assert (basic == basic2)
    assert isinstance(basic2, type(basic))
    assert (six.PY2 is not six.PY3)



# Generated at 2022-06-13 15:50:58.063661
# Unit test for method is_valid_collection_name of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_collection_name():
    # org.namespace
    # org.name
    # org.name3.namespace2
    # org.name1.namespace1
    # org.name.namespace
    # org .name . namespace
    # org. name . namespace
    # org.name . namespace

    assert False is AnsibleCollectionRef.is_valid_collection_name('')
    assert False is AnsibleCollectionRef.is_valid_collection_name('org')
    assert False is AnsibleCollectionRef.is_valid_collection_name('org.')
    assert False is AnsibleCollectionRef.is_valid_collection_name('.namespace')
    assert False is AnsibleCollectionRef.is_valid_collection_name('org.namespace.subnamespace')

# Generated at 2022-06-13 15:51:03.322253
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    from ansible_collections.ansible.builtin.plugins.module_utils.facts import (
        default_fact_collection_path)
    module_utils_path = os.path.join(default_fact_collection_path, 'ansible_collections',
                                     'ansible', 'builtin', 'plugins', 'module_utils')

    module_utils_path = os.path.abspath(module_utils_path)
    assert os.path.isdir(module_utils_path)

    with open(os.path.join(module_utils_path, 'facts.py')) as fp:
        expected = fp.read()

    class A(object):
        def get_data(self, path):
            return path

    a = A()

# Generated at 2022-06-13 15:52:00.425740
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ref_type = 'module'
    ref = AnsibleCollectionRef('namespace.collection', None, 'resource', ref_type)
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'resource'
    assert ref.ref_type == 'module'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.module'
    assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collection'
    assert ref.fqcr == 'namespace.collection.resource'

    ref_type = 'role'
    ref = AnsibleCollectionRef('namespace.collection', None, 'resource', ref_type)
    assert ref.collection == 'namespace.collection'

# Generated at 2022-06-13 15:52:09.376236
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    acr_str_isvalid = ['ns.coll.subdir1.subdir2.resource',
                       'ns0.coll0.subdir1.subdir2.resource0',
                       'ns.coll.resource',
                       'ns0.coll0.resource0',
                       'ns.coll.rolename',
                       'ns0.coll0.rolename0',
                       'ns.coll.playbookname',
                       'ns0.coll0.playbookname0',
                       'ns.coll.playbookname.yml',
                       'ns0.coll0.playbookname0.yml',
                       'ns.coll.playbookname.yaml',
                       'ns0.coll0.playbookname0.yaml']

# Generated at 2022-06-13 15:52:15.998146
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    assert AnsibleCollectionRef('ns.coll', None, 'resource', 'role')
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'role')
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'role')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource', 'role')
    assert AnsibleCollectionRef.is_valid_collection_name('ns.coll')
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'module'


# Generated at 2022-06-13 15:52:23.932667
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    class test__AnsibleCollectionPkgLoaderBase_get_data_AnsibleCollectionPkgLoader(
            _AnsibleCollectionPkgLoaderBase):
        def __init__(self):
            # must be initialized with fullname and candidate_paths
            _AnsibleCollectionPkgLoaderBase.__init__(self, fullname='ansible_collections.ns.module', path_list=['/tmp'])

    # init
    loader = test__AnsibleCollectionPkgLoaderBase_get_data_AnsibleCollectionPkgLoader()
    path = '/tmp/module.py'
    # test
    assert loader.get_data(path) is None
    # prepare
    open(path, 'w').close()
    # test
    assert loader.get_data(path) == b''

    # prepare
    path

# Generated at 2022-06-13 15:52:28.560021
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    obj = AnsibleCollectionRef('ABC.XYZ','','','role')
    wanted = "AnsibleCollectionRef(collection='ABC.XYZ', subdirs='', resource='')"
    actual = obj.__repr__()
    assert actual == wanted, 'actual: %s !=Wanted: %s' % (actual, wanted)

# Generated at 2022-06-13 15:52:35.668061
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    class TestData:
        def __init__(self, test, result, returned_value):
            self.test = test
            self.result = result
            self.returned_value = returned_value

    # Arrange

# Generated at 2022-06-13 15:52:43.422030
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'module'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'


# Generated at 2022-06-13 15:52:53.031037
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import os
    # NOTE: we only patch what we need since the method under test calls into other
    # modules which we don't want to mock.
    @contextmanager
    def _patched_pkgutil_iter_modules(prefix):
        with mock.patch('ansible.utils.plugin_docs.pkgutil.iter_modules') as pkgutil_iter_modules_mock:
            yield pkgutil_iter_modules_mock

# Generated at 2022-06-13 15:53:02.024764
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Test for method find_module of class _AnsibleCollectionFinder
    class _MockAnsiblePathHookFinder:
        def __init__(self, finder, path):
            pass

    class _MockAnsibleInternalRedirectLoader:
        def __init__(self, fullname, path_list):
            pass

    class _MockAnsibleCollectionNSPkgLoader:
        def __init__(self, fullname, path_list):
            pass

    class _MockAnsibleCollectionPkgLoader:
        def __init__(self, fullname, path_list):
            pass

    class _MockAnsibleCollectionLoader:
        def __init__(self, fullname, path_list):
            pass


# Generated at 2022-06-13 15:53:11.260254
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # Add a fake module to the list of modules
    ansible_fake_module = types.ModuleType('ansible.collections.mycollection')
    sys.modules[ansible_fake_module.__name__] = ansible_fake_module
    fake_loader = _AnsibleInternalRedirectLoader('ansible.collections.mycollection', [])
    fake_loader._redirect = ansible_fake_module.__name__
    fake_loader.load_module('ansible.collections.mycollection')
    assert sys.modules[ansible_fake_module.__name__] == ansible_fake_module
    assert sys.modules['ansible.collections.mycollection'] == ansible_fake_module
    # Remove the module from the list of modules
    del sys.modules[ansible_fake_module.__name__]

# Generated at 2022-06-13 15:54:18.672997
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens',
                                             path_list=['/path/somewhere', '/path/elsewhere']
    )
    assert not loader.is_package('ansible_collections.somens')
    assert loader.is_package('ansible_collections.somens.other')



# Generated at 2022-06-13 15:54:28.602687
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # Arrange
    # Act
    # Assert
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.my_collection.mymodule', 'module').fqcr == 'namespace.my_collection.mymodule'
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.my_collection.subdir.subsubdir.playbook', 'playbook').fqcr == 'namespace.my_collection.subdir.subsubdir.playbook'
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.my_collection.subdir.subsubdir.mymodule', 'module').fqcr == 'namespace.my_collection.subdir.subsubdir.mymodule'

# Generated at 2022-06-13 15:54:37.448553
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    # Test 1. ansible.__init__ will not be redirected
    airdl = _AnsibleInternalRedirectLoader('ansible.__init__',[])
    assert airdl._redirect is None

    # Test 2. ansible.module_utils.basic will not be redirected
    airdl = _AnsibleInternalRedirectLoader('ansible.module_utils.basic',[])
    assert airdl._redirect is None

    # Test 3. ansible.module_utils.connection will be redirected to ansible.builtin.module_utils.connection
    airdl = _AnsibleInternalRedirectLoader('ansible.module_utils.connection',[])
    assert airdl._redirect == 'ansible.builtin.module_utils.connection'


# Generated at 2022-06-13 15:54:43.029849
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').n_python_package_name == 'ansible_collections.ns.coll.plugins.module'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.resource', 'module').n_python_package_name == 'ansible_collections.ns.coll.plugins.subdir1.module'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.rolename', 'role').n_python_package_name == 'ansible_collections.ns.coll.roles.rolename'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.filtername', 'filter').n_python_package_name == 'ansible_collections.ns.coll.plugins.filter'

# Generated at 2022-06-13 15:54:48.980301
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader(['ansible_collections','community','general','plugins','modules','ping','ping.py'],
                                         'ansible_collections.community.general.plugins.modules.ping')
    module = loader.load_module()

# This class supports the ansible_collections namespace package. It implements the load_module and iter_modules
# methods.
# TODO: implement find_module

# Generated at 2022-06-13 15:54:51.304413
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    assert _AnsibleCollectionPkgLoaderBase.get_code('') == _AnsibleCollectionPkgLoaderBase()



# Generated at 2022-06-13 15:55:00.822705
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # For now, these tests must use a copy of the module, since the module is already loaded
    # and the class variable _meta_yml_to_dict is already initialized.
    copy_of_CollectionLoader = copy.copy(CollectionLoader)

    # There is no meta/runtime.yml file
    def test_get_metadata_error():
        meta_yml_to_dict = MagicMock(
            side_effect=ValueError('msg')
        )
        loader = _AnsibleCollectionPkgLoader(
            fullname='ansible_collections.namespace.collection',
            data={
                '_meta_yml_to_dict': meta_yml_to_dict,
                'subpackage_search_paths': MagicMock(),
            }
        )

# Generated at 2022-06-13 15:55:11.084148
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    test_ansible_collection_finder = _AnsibleCollectionFinder()
    test_ansible_collection_finder._install()
    finder_result = test_ansible_collection_finder.find_module('ansible_collections.default.test_plugin')
    assert isinstance(finder_result, _AnsibleCollectionLoader)
    assert finder_result.fullname == 'ansible_collections.default.test_plugin'
    finder_result = test_ansible_collection_finder.find_module('ansible')
    assert isinstance(finder_result, _AnsibleInternalRedirectLoader)
    assert finder_result.fullname == 'ansible'
    test_ansible_collection_finder._remove()



# Generated at 2022-06-13 15:55:17.240278
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.foo')
    try:
        source = loader.get_source('ansible_collections.foo')
    except ValueError:
        assert 1
    try:
        source = loader.get_source('foo')
    except ValueError:
        assert 1
    

# Generated at 2022-06-13 15:55:27.208308
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    import types
    import collections.abc
    import io
    import io
    import os
    import os
    import sys
    # TypeError: __init__() missing 1 required positional argument: 'path_list'
    # _AnsibleInternalRedirectLoader(fullname=, path_list=)
    try:
        _AnsibleInternalRedirectLoader(fullname=0, path_list=0)
    except TypeError:
        pass
    # TypeError: __init__() missing 1 required positional argument: 'path_list'
    # _AnsibleInternalRedirectLoader(fullname=, path_list=)
    try:
        _AnsibleInternalRedirectLoader(fullname=0, path_list=0)
    except TypeError:
        pass
    # TypeError: __init__() missing 1 required positional argument:

# Generated at 2022-06-13 15:56:08.908326
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # __context__ should be empty or None
    # __file__ should be None
    # __name__ should be 'ansible_collections.unittest_ns'

    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.unittest_ns')
    loader._source_code_path = '/path/to/ansible_collections/unittest_ns/__init__.py'
    loader._subpackage_search_paths = ['/path/to/ansible_collections/unittest_ns']
    loader._decoded_source = "print('Hello world!')"
    assert 'ansible_collections.unittest_ns' == loader._parent_package_name
    assert 'method get_source of class' in repr(loader)

# Generated at 2022-06-13 15:56:20.603310
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    from ansible.utils.collection_loader._data import _meta_yml_to_dict

    # Prepare test data
    fullname = 'ansible.collections.backup'
    module = ModuleType(fullname)

    # Prepare class object
    _APL = _AnsibleCollectionPkgLoader
    _APL._meta_yml_to_dict = _meta_yml_to_dict
    a = _APL(fullname, '/home/ansible/collection_path')
    a._split_name = fullname.split('.')
    a._subpackage_search_paths = ['/home/ansible/collection_path/backup/plugins']
    a._package_to_load = 'plugins'

# Generated at 2022-06-13 15:56:29.299941
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'

    try:
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('nonexistent_type')
        assert False
    except ValueError:
        pass



# Generated at 2022-06-13 15:56:38.987941
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # test with problem: no path
    test_loader = _AnsibleCollectionPkgLoaderBase()
    with pytest.raises(ValueError) as excinfo:
        test_loader.get_source(fullname=None)
    assert 'a path must be specified' in str(excinfo)

    # test with problem: relative path
    test_loader = _AnsibleCollectionPkgLoaderBase()
    with pytest.raises(ValueError) as excinfo:
        test_loader.get_source(fullname=None)
    assert 'relative resource paths not supported' in str(excinfo)

    # test with problem: invalid file path
    test_loader = _AnsibleCollectionPkgLoaderBase()

# Generated at 2022-06-13 15:56:42.451934
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test')
    loader._decoded_source = '"""\ntest\n"""'
    assert loader.get_source('ansible_collections.test') == loader._decoded_source



# Generated at 2022-06-13 15:56:47.932958
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
  # A test to find the module using the find module method
  # Create an object of the class _AnsiblePathHookFinder
  obj=_AnsiblePathHookFinder
  # Call the method find_module and pass the fullname of the module
  assert obj.find_module(self,fullname)==None
  # Call the method iter_modules and pass the prefix
  assert obj.iter_modules(self,prefix)==None
  # Call the method __repr__ and pass the two parameters
  assert obj.__repr__(self,path='self._pathctx')==None

# Generated at 2022-06-13 15:56:52.796643
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') == 'module_utils'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('modules') == 'modules'

# Generated at 2022-06-13 15:56:58.772104
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    collection_namespace = 'testns'
    collection_name = 'testcoll'
    collection_subdirs = 'testdir1.testdir2'
    collection_ref_type = 'role'
    collection_resource_name = 'testresource'
    collection_resource_path = 'testdir1/testdir2/testresource/'
    collection_path = '/path/to/collection/and/namespace'

    fqcr_with_ns = '{0}.{1}.{2}'.format(collection_namespace, collection_name, collection_resource_name)
    fqcr_without_ns = '{0}.{1}'.format(collection_name, collection_resource_name)


# Generated at 2022-06-13 15:57:03.520550
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    redirect = _AnsibleInternalRedirectLoader('ansible.stdout', [])
    assert redirect._redirect == 'builtins.print', "_AnsibleInternalRedirectLoader did not set _redirect correctly"



# Generated at 2022-06-13 15:57:13.818314
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoaderBase
    # Test for invalid arguments
    test_cases = {
        'fullname': ['ansible_collections.namespace', 'ansible_collections.namespace.collection',
        'ansible_collections.namespace.collection.subcollection', 'ansible_collections.namespace.collection.subcollection.module',
        'ansible_collections.namespace.collection.subcollection.module.submodule']
    }
    for test_case, result_list in test_cases.items():
        loader = _AnsibleCollectionPkgLoaderBase(result_list[0])
        for result in result_list:
            try:
                loader.load_module(result)
            except ValueError:
                continue

# Generated at 2022-06-13 15:57:59.254524
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    with pytest.raises(ValueError):
        redirect_test_loader = _AnsibleInternalRedirectLoader(fullname="test", path_list=None)
        redirect_test_loader.load_module(fullname="test")
    with pytest.raises(ValueError):
        redirect_test_loader = _AnsibleInternalRedirectLoader(fullname="ansible.collection.test", path_list=None)
        redirect_test_loader.load_module(fullname="ansible.collection.test")



# Generated at 2022-06-13 15:58:10.544373
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    # Case 1: import ansible.module_utils ==> success
    name = 'ansible.module_utils'
    fullname = 'ansible.module_utils'
    loader = _AnsiblePkgLoaderBase(fullname)
    assert loader.get_code(fullname)

    # Case 2: import collections.test_module ==> success
    name = 'collections.test_module'
    fullname = 'collections.test_module'
    loader = _AnsibleCollectionPkgLoaderBase(fullname)
    assert loader.get_code(fullname)

    # Case 3: import collections.test_module.role ==> success
    name = 'collections.test_module.roles'
    fullname = 'collections.test_module.roles'

# Generated at 2022-06-13 15:58:15.063976
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():

    assert list(_AnsibleCollectionPkgLoaderBase.iter_modules(None, 'ansible_collections.notadir')) == []
    # FIXME: test valid package iteration behavior? requires fake filesystem stuff
    # assert list(_AnsibleCollectionPkgLoaderBase.iter_modules(None, 'ansible_collections.pkg')) == []
    # assert list(_AnsibleCollectionPkgLoaderBase.iter_modules(None, 'ansible_collections.pkg.subpkg')) == []


# Generated at 2022-06-13 15:58:21.292545
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # pylint: disable=too-many-function-args
    def _test_get_filename(loader, expected_filename, expected_exception, exception_message):
        if expected_exception is not None:
            # TODO: check exception mentions fullname by default?
            try:
                loader.get_filename(loader._fullname)
                assert False, 'get_filename should have thrown {0} with {1}'.format(
                    expected_exception.__name__, exception_message)
            except expected_exception as e:
                assert exception_message in to_native(e)
        else:
            assert loader.get_filename(loader._fullname) == expected_filename
        return


# Generated at 2022-06-13 15:58:26.663088
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Test the case where fullname is 'ansible' and path is None
    sys.meta_path = []
    path = None
    fullname = 'ansible'
    sys.modules = {}
    collection_finder = _AnsibleCollectionFinder(paths=path)
    collection_loader = collection_finder.find_module(fullname=fullname, path=path)
    assert collection_loader.fullname == fullname
    assert collection_loader.path_list == collection_finder._n_collection_paths
    assert collection_loader.__class__.__name__ == '_AnsibleInternalRedirectLoader'
    # Test the case where fullname is 'ansible' and path is not None
    sys.meta_path = []
    path = []
    fullname = 'ansible'
    sys.modules = {}
   

# Generated at 2022-06-13 15:58:36.921904
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from ansible.utils import collection_loader

    # Test with a path_list that return no module
    path = []
    fullname = 'ansible.plugins.action.exit_json'
    _AnsibleInternalRedirectLoader_obj = collection_loader._AnsibleInternalRedirectLoader(fullname, path)
    assert _AnsibleInternalRedirectLoader_obj._redirect == 'ansible.builtin.exit_json'

    # Test with a path_list that return one module
    path = ['.']
    fullname = 'ansible.plugins.action.exit_json'
    _AnsibleInternalRedirectLoader_obj = collection_loader._AnsibleInternalRedirectLoader(fullname, path)
    assert _AnsibleInternalRedirectLoader_obj._redirect == 'ansible.builtin.exit_json'


# Generated at 2022-06-13 15:58:46.562823
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    print("Unit test for method get_filename of class _AnsibleCollectionsPkgLoaderBase...")
    print("Testing to get filename of collection namespace")
    # Create a _AnsibleCollectionPkgLoaderBase object
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections")
    # Get the filename of collection namespace, expected "__synthetic__"
    filename = loader.get_filename("ansible_collections")
    if filename == "__synthetic__":
        print("Success: ansible_collections.__synthetic__ file is created")
    else:
        print("fail: ansible_collections.__synthetic__ file is not created or not found")

    print("Testing to get filename of collection namespace")
    # Create a _AnsibleCollectionPkgLoaderBase object, the fullname is

# Generated at 2022-06-13 15:58:51.002944
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    # Test for method is_valid_fqcr(ref) of class AnsibleCollectionRef
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource', ref_type='module')
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource', ref_type='roles')



# Generated at 2022-06-13 15:59:00.513070
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():

    ## _AnsibleCollectionPkgLoaderBase.get_source(fullname)
    ## test method with the following parameters:
    ##  fullname='ansible_collections.ansible.somens.plugins.module_utils.test_utils'
    ##
    ##  path='/home/user/ansible/ansible_collections/ansible/somens/plugins/module_utils/test_utils.py'
    ##

    from ansible_collections.ansible.somens.plugins.module_utils.test_utils import _AnsibleCollectionPkgLoaderBase
    from ansible_collections.ansible.somens.plugins.module_utils.test_utils import AnsibleCollectionLoaderEntryFactory
    from ansible_collections.ansible.somens.plugins.module_utils.test_utils import to_