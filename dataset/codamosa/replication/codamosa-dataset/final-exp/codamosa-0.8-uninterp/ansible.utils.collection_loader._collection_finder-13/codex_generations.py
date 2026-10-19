

# Generated at 2022-06-13 15:49:55.638018
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # A simple test for the method load_module of class _AnsibleInternalRedirectLoader
    # Initialize first mock_fullname which is the fullname of the module
    mock_fullname = 'ansible.plugins.connection.local'
    # Initialize second mock_path_list which is the path_list of the module
    mock_path_list = []
    # Initialize the mock _AnsibleInternalRedirectLoader object
    mock_AnsibleInternalRedirectLoader_obj = _AnsibleInternalRedirectLoader(mock_fullname, mock_path_list)
    # Test the load_module method using the module name ansible.plugins.connection.local
    res = mock_AnsibleInternalRedirectLoader_obj.load_module(mock_fullname)
    # Assert that the result must be ansible.plugins.loader

# Generated at 2022-06-13 15:50:03.895428
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') is 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') is 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') is 'module_utils'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') is 'modules'

    with pytest.raises(ValueError):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('not_a_plugin')


# Generated at 2022-06-13 15:50:15.154597
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
   # test with invalid collection reference
   assert AnsibleCollectionRef.try_parse_fqcr('my.collection.my-role', 'role') == None
   # test with valid collection reference and valid plugin type
   assert AnsibleCollectionRef.try_parse_fqcr('my.collection.my_role', 'role') != None
   # test with valid collection reference and invalid plugin type
   assert AnsibleCollectionRef.try_parse_fqcr('my.collection.my_role', 'hell') == None
   # test with valid collection reference and empty plugin type
   assert AnsibleCollectionRef.try_parse_fqcr('my.collection.my_role', '') == None
   # test with collection reference with extra colons after the plugin type

# Generated at 2022-06-13 15:50:23.294544
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():
    # Test question:
    #  - why do we need to mock the base class loader?
    #    - because parent class of _AnsibleCollectionLoader imports ansible.__init__, which in turn imports
    #      ansible.utils.collection_loader which then calls the base class init.
    #    - because we need to mock the call to the base class loader, we need to mock the _AnsibleCollectionLoader
    #      class itself.

    # mocking _AnsibleCollectionPkgLoaderBase
    # - because it imports ansible.__init__, which in turn imports ansible.utils.collection_loader which then
    #   calls the base class init.
    patcher = patch('ansible.utils.collection_loader._AnsibleCollectionPkgLoaderBase.__init__')
    mock_base_class_init = patcher.start()

# Generated at 2022-06-13 15:50:35.714498
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Testing is_valid_fqcr')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.subdir2.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename')

    # not FQCRs
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll')
    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1')
    assert not AnsibleCollectionRef.is_valid_f

# Generated at 2022-06-13 15:50:39.506015
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    # Test for case where the fqcr is a string
    assert AnsibleCollectionRef.is_valid_fqcr(ref='namespace.collection') is True

    # Test for case where the fqcr is not a string
    assert AnsibleCollectionRef.is_valid_fqcr(ref=100) is False


# Generated at 2022-06-13 15:50:46.429114
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.subdir1.resource')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename', 'role')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename.yml', 'role')
    assert AnsibleCollectionRef.is_valid_fqcr('ns.coll.rolename.yaml', 'role')

    assert not AnsibleCollectionRef.is_valid_fqcr('ns.coll.resource.ext')

# Generated at 2022-06-13 15:50:53.489899
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    TEST_MODULE_NAME = "ansible_collections.acme.foobar"

    # These unit tests only work in Python 3.
    if not (sys.version_info[0] >= 3):
        # py2exit() will just raise SystemExit (a subclass of Exception) if called in python2
        pytest.skip("This code is only supported in Python 3.")

    # Make sure the ansible_collections python path is setup for the test
    PATH_TO_TEST_MODULE = os.path.join(C.COLLECTIONS_PATHS[0], "acme/foobar/__init__.py")
    expectedResult = "{0}(path='{1}')".format(_AnsibleCollectionPkgLoaderBase.__name__, PATH_TO_TEST_MODULE)

    # Test loading the module using a

# Generated at 2022-06-13 15:50:57.206939
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test.testns')
    loader._subpackage_search_paths = ['/path/to/foo']
    loader._source_code_path = '/path/to/foo/bar.py'
    loader.get_data('/path/to/foo/baz.py')



# Generated at 2022-06-13 15:51:09.685048
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():

    class TestCollectionPkgLoader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            if len(self._split_name) != 3 or self._split_name[1] != 'testns':
                raise ValueError('this is a test of a particular loader config')

        def _get_candidate_paths(self, path_list):
            return [os.path.join(p, self._split_name[1]) for p in path_list]

        def _validate_final(self):
            self._source_code_path = os.path.join(self._candidate_paths[0], self._package_to_load + '.py')
            if not os.path.isfile(self._source_code_path):
                raise ImportError('source code not found')

    # pretend we

# Generated at 2022-06-13 15:52:06.643300
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from ansible.utils.collection_loader import _AnsibleCollectionFinder
    from ansible.utils.collection_loader import _AnsibleCollectionLoader
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoader
    from ansible.utils.collection_loader import _AnsibleCollectionRootPkgLoader
    from ansible.utils.collection_loader import _AnsibleCollectionNSPkgLoader
    from ansible.utils.collection_loader import _AnsibleInternalRedirectLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    finder = _AnsibleCollectionFinder(paths=['tests/units/utils/collection_loader/collections'])

    finder._install()

    # test ansible_collections.ns.coll.file

# Generated at 2022-06-13 15:52:15.915722
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    loader = _AnsibleCollectionPkgLoaderBase('foo')
    assert repr(loader) == "_AnsibleCollectionPkgLoaderBase(path=None)"

    loader = _AnsibleCollectionPkgLoaderBase('foo', path_list=[])
    assert repr(loader) == "_AnsibleCollectionPkgLoaderBase(path=None)"

    loader = _AnsibleCollectionPkgLoaderBase('foo', path_list=['/bar/baz', '/bar/qux'])
    assert repr(loader) == "_AnsibleCollectionPkgLoaderBase(path=['/bar/baz', '/bar/qux'])"

    loader = _AnsibleCollectionPkgLoaderBase('foo', path_list=['/bar/baz', '/bar/qux'])

# Generated at 2022-06-13 15:52:25.721734
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert(AnsibleCollectionRef.from_fqcr(u'collection.foo.module',
                                          u'module').collection == u'collection')
    assert(AnsibleCollectionRef.from_fqcr(u'collection.foo.module',
                                          u'module').subdirs == u'')
    assert(AnsibleCollectionRef.from_fqcr(u'collection.foo.module',
                                          u'module').resource == u'module')
    assert(AnsibleCollectionRef.from_fqcr(u'collection.foo.module',
                                          u'module').ref_type == u'module')
    assert(AnsibleCollectionRef.from_fqcr(u'collection.foo.module',
                                          u'module').collection == u'collection')

# Generated at 2022-06-13 15:52:27.007815
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    m = _AnsibleCollectionPkgLoaderBase()
    assert m.load_module.__name__ == "load_module"


# Generated at 2022-06-13 15:52:32.254764
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():

    from ansible.utils import collection_loader
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoader
    from ansible import constants as C

    # Create a local dir for testing
    temp_dir = tempfile.mkdtemp()
    local_ansible_collection = C.ANSIBLE_COLLECTIONS_PATHS[0]

    shutil.copytree(local_ansible_collection, temp_dir)

    from ansible.release import __version__
    assert __version__ != ''

    # Create a local collection to test with
    metadata_dir = os.path.join(temp_dir, 'ansible_collections', 'test', 'foo', 'meta')
    os.makedirs(metadata_dir)

# Generated at 2022-06-13 15:52:38.899955
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    from ansible import __path__ as ansible_path
    finder = _AnsiblePathHookFinder(None, ansible_path[0])
    assert finder.find_module('setup') is not None
    assert not finder.find_module('fkladjflkadjfldfjkldjlfdajfd')



# Generated at 2022-06-13 15:52:47.917305
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    """
    Test to check the object constructor, getters and setters
    """
    ansible_collection_ref_obj = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'my_resource', 'my_type')

    # Getters
    assert ansible_collection_ref_obj.collection == 'namespace.collection'
    assert ansible_collection_ref_obj.subdirs == 'subdir1.subdir2'
    assert ansible_collection_ref_obj.resource == 'my_resource'
    assert ansible_collection_ref_obj.ref_type == 'my_type'

    # Setters
    ansible_collection_ref_obj.collection = 'namespace.new_collection'

# Generated at 2022-06-13 15:52:58.773076
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ref = AnsibleCollectionRef('test_ref', 'ansible,test_ref', 'ns.coll', u'role')
    assert ref.fqcr == u'ns.coll.role.test_ref'
    assert ref.n_python_package_name == 'ansible_collections.ns.coll.roles.test_ref'
    assert ref.n_python_collection_package_name == 'ansible_collections.ns.coll'
    assert ref.collection == u'ns.coll'
    assert ref.subdirs == u''
    assert ref.ref_type == u'role'
    assert ref.resource == u'test_ref'

    ref = AnsibleCollectionRef('test_ref', 'ansible,test_ref', 'ns.coll', u'playbook')

# Generated at 2022-06-13 15:53:00.280864
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    assert False, "Fail: test__AnsibleCollectionFinder_find_module not implemented"

# Generated at 2022-06-13 15:53:04.433695
# Unit test for constructor of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader():
    for good_value in [[], ['/path/to/collection1', '/path/to/collection2'], ['/path/to/collection1'], ['/path/to/collection2']]:
        loader = _AnsibleCollectionPkgLoader(good_value)
        assert loader._candidate_paths == good_value
        assert loader._package_to_load is None
        assert loader._redirect_module is None
        assert loader._source_code_path is None
        assert loader._subpackage_search_paths is None


# Generated at 2022-06-13 15:53:41.673536
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():

    assert AnsibleCollectionRef.is_valid_fqcr("test.test") == False
    assert AnsibleCollectionRef.is_valid_fqcr("test.test.test") == True
    assert AnsibleCollectionRef.is_valid_fqcr("test.test.test.test2") == True
    assert AnsibleCollectionRef.is_valid_fqcr("test.0test.test") == True
    assert AnsibleCollectionRef.is_valid_fqcr("test.test.test.test2.test.2") == True
    assert AnsibleCollectionRef.is_valid_fqcr("test.test.test.test2.test.2", "module") == True
    assert AnsibleCollectionRef.is_valid_fqcr("test.test.test.test2.test.2", "role") == True

# Generated at 2022-06-13 15:53:51.618764
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'module_utils'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('modules') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('shell_plugins') == 'shell'
    with pytest.raises(ValueError):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('test')


# Generated at 2022-06-13 15:53:52.871427
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    assert _AnsibleCollectionPkgLoaderBase.__doc__


# Generated at 2022-06-13 15:54:03.192173
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    import unittest
    import ansible.module_utils.six.moves.builtins as builtins
    class TestAnsibleCollectionRef(unittest.TestCase):
        def setUp(self):
            self.builtin_meta = _get_collection_metadata('ansible.builtin')
        def test_from_fqcr(self):
            # Works if collection is ansible.builtin
            self.assertIsNotNone(AnsibleCollectionRef.from_fqcr("ansible.builtin.ping","module"))

            # Works if collection is not ansible.builtin
            self.assertIsNotNone(AnsibleCollectionRef.from_fqcr("ansible.netcommon.icmp_unreach_error","module"))


# Generated at 2022-06-13 15:54:08.103333
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    import ansible.utils.collection_loader
    ansible.utils.collection_loader._meta_yml_to_dict = lambda x, y: _meta_yml_to_dict(x, y)
    ansible.utils.collection_loader._get_collection_metadata = lambda x: _get_collection_metadata(x)

    # direct redirect
    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test', None)
    assert loader._redirect == 'ansible.test'

    # indirect redirect
    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test1', None)
    assert loader._redirect == 'ansible.test'

    # no redirect

# Generated at 2022-06-13 15:54:18.833880
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:54:27.217454
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # Ensure that AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type works as expected
    for directory in [u'action_plugins', u'library', u'filter_plugins', u'lookup_plugins', u'callback_plugins', u'vars_plugins',
                      u'connection_plugins']:
        plugin_type = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(directory)
        assert plugin_type in AnsibleCollectionRef.VALID_REF_TYPES, \
            u'Failed to convert legacy directory name - \'{0}\' to a legit plugin type'.format(directory)



# Generated at 2022-06-13 15:54:30.283478
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():
    loader = _AnsibleCollectionLoader('ansible.foo', ['/some/path'])
    assert loader is not None


# Generated at 2022-06-13 15:54:32.119612
# Unit test for constructor of class _AnsibleCollectionLoader
def test__AnsibleCollectionLoader():
    ac = _AnsibleCollectionLoader(fullname="_AnsibleCollectionLoader", path=[])

# Generated at 2022-06-13 15:54:39.860730
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    import sys
    import pytest

    # test with valid collection name
    result = AnsibleCollectionRef.from_fqcr(u'ns.coll.resource', u'module')
    assert result.collection == u'ns.coll'
    assert result.resource == u'resource'
    assert result.subdirs == u''
    assert result.ref_type == u'module'
    assert result.n_python_collection_package_name == u'ansible_collections.ns.coll'
    assert result.n_python_package_name == u'ansible_collections.ns.coll.plugins.module.resource'
    assert result.fqcr == u'ns.coll.resource'

    # test with invalid collection name

# Generated at 2022-06-13 15:55:12.144737
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    print('')
    print('****************************')
    print('Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase')
    print('****************************')
    print('')

    # class _AnsibleCollectionPkgLoaderBase:
    #     _allows_package_code = False
    #
    #     def __init__(self, fullname, path_list=None):
    #         self._fullname = fullname
    #         self._redirect_module = None
    #         self._split_name = fullname.split('.')
    #         self._rpart_name = fullname.rpartition('.')
    #         self._parent_package_name = self._rpart_name[0]  # eg ansible_collections for ansible_collections.somens, '' for

# Generated at 2022-06-13 15:55:18.787379
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    this_module = sys.modules[__name__]
    loader = _AnsibleCollectionPkgLoaderBase.__new__(_AnsibleCollectionPkgLoaderBase)
    loader.__init__(__name__, sys.path)
    assert loader.get_filename(__name__) == this_module.__file__
    assert loader.get_filename(__package__) is None


# Generated at 2022-06-13 15:55:22.961527
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    pkg_name = 'ansible_collections.namespace.collection'
    pkg_path = '/pkg/path'
    loader = _AnsibleCollectionPkgLoader(pkg_name, [pkg_path])
    # _meta_yml_to_dict is not set
    try:
        loader.load_module(pkg_name)
        assert False
    except ValueError:
        assert True
    # _meta_yml_to_dict is set
    _meta_yml_to_dict = lambda s, f: {'plugin_routing':{}}
    import ansible
    ansible_pkg_path = os.path.dirname(ansible.__file__)
    metadata_path = os.path.join(ansible_pkg_path, 'config/ansible_builtin_runtime.yml')


# Generated at 2022-06-13 15:55:35.392099
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:55:36.454024
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    assert 1==1

# Generated at 2022-06-13 15:55:48.529101
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import unittest

    import ansible_collections
    import ansible_collections.example.zoo
    
    class Test__AnsiblePathHookFinder_find_module(unittest.TestCase):
        def test__find_module_for_ansible_collections_example_zoo(self):
            self.assertEqual(ansible_collections.example.zoo.__doc__, 'This is an example collection')

    unittest.main(argv=[''], verbosity=2, exit=False)


# Implements pkgutil-style module finding on the given path list. This can be used by a loader to consult for
# sub-modules within its own package for load_module. This is not a full pkgutil implementation (eg there's no
# support for resources), and is not a full finder

# Generated at 2022-06-13 15:55:50.969264
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    pass


# Generated at 2022-06-13 15:55:56.708372
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoaderBase

    assert _AnsibleCollectionPkgLoaderBase('foo').get_filename('foo') is None, \
        "loader has no code, so get_filename should return None"

    class _TestLoaderClass(_AnsibleCollectionPkgLoaderBase):
        def get_filename(self, fullname):
            if fullname != self._fullname:
                raise ValueError('this loader cannot find files for {0}, only {1}'.format(fullname, self._fullname))
            b_path = to_bytes('/foo/bar')
            if os.path.isfile(b_path):
                return '/foo/bar'
            return None


# Generated at 2022-06-13 15:56:06.077078
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    import os
    import tempfile
    import shutil
    import os.path
    import sys

    t = tempfile.mkdtemp()

# Generated at 2022-06-13 15:56:17.713797
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from ansible.tests.unit.compat import unittest
    # load_module(self, fullname)
    tests = [
        {
            'given': {
                'fullname': 'ansible.foo'
            },
            'expect': {
                'exception': True,
                'exception_message': 'not redirected, go ask path_hook'
            }
        }
    ]
    for test in tests:
        given = test['given']
        expected = test['expect']
        with unittest.TestCase('__init__') as tc:
            loader = _AnsibleInternalRedirectLoader(given['fullname'], None)
            if expected['exception']:
                with tc.assertRaises(Exception) as cm:
                    loader.load_module(given['fullname'])
               

# Generated at 2022-06-13 15:57:00.037085
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from _collections_loader_mocks import MockAnsibleCollectionConfig, MockAnsibleModuleUtilsInternalRedirect,\
        MockAnsibleCollectionRootPkgLoader, MockAnsibleCollectionNSPkgLoader, MockAnsibleCollectionPkgLoader,\
        MockAnsibleCollectionLoader, MockSystemPaths
    from ansible.module_utils.common.text.converters import to_native, to_text, to_bytes
    from ansible.module_utils.six import string_types
    from . import to_bytes
    AnsibleCollectionConfig._collection_config = MockAnsibleCollectionConfig()
    sys.modules['ansible.module_utils.internal_redirect'] = MockAnsibleModuleUtilsInternalRedirect()

    paths = ['/etc/ansible', '/usr/share/ansible']
    ansible_

# Generated at 2022-06-13 15:57:12.373105
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # test for normal case
    collection_ref = AnsibleCollectionRef.try_parse_fqcr(u"ansible_test.test", u"doc_fragments")
    assert collection_ref.collection == u"ansible_test.test"
    assert collection_ref.subdirs == u""
    assert collection_ref.resource == u"test"
    assert collection_ref.ref_type == u"doc_fragments"

    # test for normal case including subdirectories
    collection_ref = AnsibleCollectionRef.try_parse_fqcr(u"ansible_test.test.subdir1", u"doc_fragments")
    assert collection_ref.collection == u"ansible_test.test"
    assert collection_ref.subdirs == u"subdir1"
    assert collection_ref.resource

# Generated at 2022-06-13 15:57:19.128621
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('filter_plugins') == 'filter'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('test_plugins') == 'test'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('some_plugins') == 'some'

# Generated at 2022-06-13 15:57:23.495807
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    pathlist = ['/home/maria/ansible_collections/alvaroaleman/product/plugins/modules']
    fullname = 'ansible_collections.alvaroaleman.product.plugins.modules.product.alvaroaleman_product'
    file_path = '/home/maria/ansible_collections/alvaroaleman/product/plugins/modules/product.py'
    code_object = _AnsibleCollectionPkgLoaderBase(fullname, path_list=pathlist).get_code(fullname)
    assert code_object is not None

# Generated at 2022-06-13 15:57:30.243986
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    print("Testing AnsibleCollectionRef")
    # test: new AnsibleCollectionRef with good input
    ref1 = AnsibleCollectionRef("my.collection", "subdir1.subdir2", "mymodule", "module")
    print("ref1 is {0}".format(ref1))
    if ref1 is None:
        print("test_AnsibleCollectionRef failed: new AnsibleCollectionRef with good input failed")
        return False

    # test: new AnsibleCollectionRef with bad input
    try:
        ref2 = AnsibleCollectionRef("my.collection.", "subdir1.subdir2.", "mymodule", "module")
    except ValueError:
        print("test_AnsibleCollectionRef pass: new AnsibleCollectionRef with bad input passed")
        pass

# Generated at 2022-06-13 15:57:40.626951
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    from unittest.mock import patch
    from unittest import TestCase
    from tests.test_utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
    from collections import namedtuple

    import tempfile
    import shutil
    import contextlib
    import os
    import stat

    # create a temporary directory
    temp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(temp_dir, 'foo'))

    # create a temporary python file (mocked as a module) in the temp directory
    temp_file = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False)
    os.chmod(temp_file.name, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
   

# Generated at 2022-06-13 15:57:42.303175
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    ac = AnsibleCollectionRef("test", None, None, None)
    assert ac.__repr__()=="AnsibleCollectionRef(collection='test', subdirs=None, resource=None)"

# Generated at 2022-06-13 15:57:52.202879
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    # Path to be used for module finding
    path = 'path-to-be-used-for-module-finding'
    # Module names to be returned by iter_modules
    module_names = ['module-names-to-be-returned-by-iter_modules']

    def _get_candidate_paths(path_list):
        # Verify path_list length is 1
        assert len(path_list) == 1
        # Verify path_list[0] is path
        assert path_list[0] == path
        # Return candidate_paths
        return ['candidate-paths']

    def _get_subpackage_search_paths(candidate_paths):
        # Verify candidate_paths length is 1
        assert len(candidate_paths) == 1
        # Verify candidate_paths[0] is '

# Generated at 2022-06-13 15:57:55.756571
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'module')

    assert ref.__repr__() == "AnsibleCollectionRef(collection='namespace.collection', subdirs='', resource='mymodule')"


# Generated at 2022-06-13 15:58:02.221542
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    from types import ClassType, ModuleType, FunctionType
    from inspect import isclass, ismodule

    def test_class(cls):
        assert isclass(cls), '{0} is a class'.format(cls)
        assert cls.__name__ in globals(), '{0} in globals'.format(cls.__name__)
        assert cls == eval(cls.__name__), '{0} == eval({1})'.format(cls, cls.__name__)

    def test_method(method):
        assert isinstance(method, FunctionType), '{0} is a method'.format(method)
        assert method.__name__ in globals(), '{0} in globals'.format(method.__name__)