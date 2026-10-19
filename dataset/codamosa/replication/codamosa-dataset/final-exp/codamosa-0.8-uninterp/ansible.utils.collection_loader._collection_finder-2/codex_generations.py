

# Generated at 2022-06-13 15:50:02.609095
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    # Test for #is_package for case where module has no source code
    # assert that the method raises a ValueError exception
    #
    # test fixture values
    is_package_fullname = 'ansible_collections.ansible.com.abcd'
    with pytest.raises(ValueError) as excinfo:
        assert_AnsibleCollectionPkgLoaderBase_is_package(is_package_fullname)
    assert 'is not supported' in str(excinfo.value)

    # Test for #is_package for case where module has source code
    # assert that the method returns a boolean (True or False)
    #
    # test fixture values
    is_package_fullname = 'ansible_collections.ansible.com.abcd'

# Generated at 2022-06-13 15:50:09.019952
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    s=_AnsibleCollectionPkgLoaderBase('ansible_collections.ansible', path_list=['/tmp/collection'])
    s._source_code_path = '/tmp/collection/ansible/__init__.py'
    s._subpackage_search_paths = ['/tmp/collection/ansible/plugins/collection']
    s._package_to_load = 'ansible/plugins/collection'
    ret = s.get_data('/tmp/collection/ansible/plugins/collection/module_utils/facts/system/distribution.py')

# Generated at 2022-06-13 15:50:12.706375
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr('test.collection.module_utils.subdir.subsubdir.name', ref_type='module_utils') == AnsibleCollectionRef(collection='test.collection', subdirs='subdir.subsubdir', resource='name', ref_type='module_utils')


# Generated at 2022-06-13 15:50:21.686927
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    modules = ['ansible_collections.foo.bar.baz.quux', 'ansible_collections.foo.bar.baz.quuux', 'ansible_collections.foo.bar.baz.quuuux']

    class UnitTestAnsibleCollectionPkgLoaderBase(object):
        def __init__(self, fullname, path_list=None):
            self._fullname = fullname
            self._split_name = fullname.split('.')
            self._package_to_load = self._split_name[-1]
            self._candidate_paths = ['/' + fullname[20:].replace('.', '/')]


# Generated at 2022-06-13 15:50:34.198502
# Unit test for method find_module of class _AnsibleCollectionFinder

# Generated at 2022-06-13 15:50:37.213254
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    collection_finder = _AnsibleCollectionFinder()
    assert collection_finder is not None
# End of test__AnsibleCollectionFinder



# Generated at 2022-06-13 15:50:45.472386
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    pkg = _AnsibleCollectionPkgLoaderBase("test")

    pkg._subpackage_search_path = ["/home/test/test.py"]
    assert pkg.is_package("test") == False

    pkg._subpackage_search_path = None
    assert pkg.is_package("test") == False

    pkg._subpackage_search_path = []
    assert pkg.is_package("test") == False

    pkg._subpackage_search_path = ["/home/test"]
    assert pkg.is_package("test") == True


# Generated at 2022-06-13 15:50:56.678025
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # Test to assert if method legacy_plugin_dir_to_plugin_type() raises exception for invalid
    # legacy plugin directory names.
    with pytest.raises(ValueError):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('InvalidDirectoryName')
    # Assert if legacy plugin directory name 'action_plugins' gives plugin type as 'action'.
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    # Assert if legacy plugin directory name 'library' gives plugin type as 'modules'.
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    # Assert if legacy plugin directory name 'callback_plugins' gives plugin type as 'callback'.
    assert AnsibleCollectionRef.legacy_plugin

# Generated at 2022-06-13 15:51:09.133862
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    # settings for test
    fullname = 'tests.test_collection_loader.test__AnsibleInternalRedirectLoader_load_module'
    location_existing_file = 'test_file'
    location_non_existing_file = 'test_file_not_exists'
    location_non_file = 'test_dir'
    # create valid location
    os.mkdir(location_non_file)
    with open(location_existing_file, 'w') as fd:
        fd.write('content')
    # delete original
    if fullname in sys.modules:
        del sys.modules[fullname]
    # test
    for path_list in [[], [location_non_existing_file], [location_non_file]]:
        with pytest.raises(ImportError):
            _AnsibleInternal

# Generated at 2022-06-13 15:51:13.678180
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    SearchResult = namedtuple('SearchResult', 'module_name,module_loader')
    search_results = []

    class MyFinder:
        def find_module(self, fullname, path=None):
            search_results.append(SearchResult(module_name=fullname,module_loader='MyFinder'))
            return self

    class MyFinder2:
        def find_module(self, fullname, path=None):
            search_results.append(SearchResult(module_name=fullname,module_loader='MyFinder2'))
            return self

    module_finder = MyFinder()
    module_finder2 = MyFinder2()

# Generated at 2022-06-13 15:53:22.467735
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test a generic collection reference
    ref = AnsibleCollectionRef(
        collection_name='ns.coll',
        subdirs='subdir1.subdir2',
        resource='mymod',
        ref_type='module',
    )
    assert ref.n_python_collection_package_name == 'ansible_collections.ns.coll'
    assert ref.n_python_package_name == 'ansible_collections.ns.coll.plugins.subdir1.subdir2.module'
    assert ref.fqcr == 'ns.coll.subdir1.subdir2.mymod'
    assert ref.ref_type == 'module'
    assert ref.collection == 'ns.coll'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymod'



# Generated at 2022-06-13 15:53:25.085542
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    assert _AnsibleCollectionPkgLoaderBase().get_data('test_data/good_target_path') == b'hi\n'



# Generated at 2022-06-13 15:53:36.857543
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    # Init AnsibleCollectionRef
    test_collection_name = 'namespace.collectionname'
    test_subdirs = 'subdir1.subdir2'
    test_resource = 'mymodule'
    test_ref_type = 'module'
    test_ansible_collection_ref = AnsibleCollectionRef(test_collection_name, test_subdirs, test_resource, test_ref_type)
    # AnsibleCollectionRef.__repr__ returns a str representation of an AnsibleCollectionRef object
    assert isinstance(test_ansible_collection_ref.__repr__(), str)
    assert test_ansible_collection_ref.__repr__() == "AnsibleCollectionRef(collection='namespace.collectionname', subdirs='subdir1.subdir2', resource='mymodule')"

# Unit test

# Generated at 2022-06-13 15:53:48.447778
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    import collections
    import os
    import tempfile

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    from ansible_collections.notstdlib.moveitallout.plugins.loader import _AnsibleCollectionPkgLoaderBase
    from ansible_collections.notstdlib.moveitallout.plugins.loader import _iter_modules_impl

    # create a fake collection with a subpackage with a few modules in it, and test
    # that is_package works with a few path variations
    test_collection_name = 'test_collection_name'

# Generated at 2022-06-13 15:53:56.035531
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    try:
        AnsibleCollectionRef('mycoll.mymodule', None, 'mymodule', 'module')
    except ValueError as e:
        assert 'Invalid collection name' in to_native(e)
        pass

    try:
        AnsibleCollectionRef('myns.mycoll', 'subdir1.subdir2', 'mymodule', 'module')
    except ValueError as e:
        assert 'Invalid subdirs entry' in to_native(e)
        pass

    try:
        AnsibleCollectionRef('myns.mycoll', 'subdir1.subdir2', 'mymodule', 'doc_fragment')
    except ValueError as e:
        assert 'Invalid collection ref type' in to_native(e)
        pass


# Generated at 2022-06-13 15:54:01.900410
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    print("Testing method from_fqcr of class AnsibleCollectionRef")


# Generated at 2022-06-13 15:54:02.520639
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    pass

# Generated at 2022-06-13 15:54:09.786063
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
  assert AnsibleCollectionRef('ansible.test', None, 'fake_module', 'module') == \
         AnsibleCollectionRef('ansible.test', '', 'fake_module', 'module')
  assert not AnsibleCollectionRef.is_valid_fqcr('ns1.coll1.ns2.coll2.fake_module')
  assert AnsibleCollectionRef.is_valid_fqcr('ns1.coll1.fake_module')
  assert not AnsibleCollectionRef.is_valid_fqcr('ns1.coll1.fake_module.yaml')
  assert not AnsibleCollectionRef.is_valid_collection_name('.test')
  assert AnsibleCollectionRef.is_valid_collection_name('ansible.test')

# Generated at 2022-06-13 15:54:19.599264
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    # TODO: how to mock on_collection_load.fire?
    AnsibleCollectionConfig.on_collection_load = dict()
    # TODO: how to mock import_module('ansible')
    class _Module_object:
        def __init__(self):
            pass
        def __file__(self):
            return "ansible_path"
    import_module_var = dict()
    import_module_var['ansible'] = _Module_object() 

    # if type(import_module('ansible')).__name__ == 'module':
    #     _test_failed("test__AnsibleCollectionPkgLoader_load_module()")
    # else:
    #     _test_passed("test__AnsibleCollectionPkgLoader_

# Generated at 2022-06-13 15:54:28.278802
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # POSITIVE CASES
    # LEGACY_PLUGIN_DIR_NAME = 'action_plugins'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    # LEGACY_PLUGIN_DIR_NAME = 'become_plugins'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    # LEGACY_PLUGIN_DIR_NAME = 'cache_plugins'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    # LEGACY_PLUGIN_DIR_NAME = 'callback_plugins'

# Generated at 2022-06-13 15:55:12.906068
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    from ansible.module_utils.common.collections import _AnsibleCollectionFinder
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utilities import safe_get
    _AnsiblePathHookFinder.sys.path_hooks = []
    _AnsiblePathHookFinder._filefinder_path_hook = safe_get(_AnsiblePathHookFinder._AnsiblePathHookFinder, "_filefinder_path_hook", None)
    assert _AnsiblePathHookFinder._filefinder_path_hook is not None
    assert _AnsiblePathHookFinder.find_module("ansible_collections") is not None

# Generated at 2022-06-13 15:55:15.710248
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    obj = _AnsibleCollectionPkgLoaderBase('abc.def')
    print(obj.__repr__())



# Generated at 2022-06-13 15:55:20.668112
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    example_fqcr = 'tests.unit.test_loader.example_fqcr'
    example_ref_type = 'role'
    try_parse_fqcr_return_value = AnsibleCollectionRef.try_parse_fqcr(example_fqcr, example_ref_type)
    assert try_parse_fqcr_return_value.n_python_collection_package_name == 'ansible_collections.tests.unit.test_loader'
    assert try_parse_fqcr_return_value._fqcr == u'tests.unit.test_loader.example_fqcr'
    assert try_parse_fqcr_return_value.n_python_package_name == 'ansible_collections.tests.unit.test_loader.roles.example_fqcr'


# Unit test

# Generated at 2022-06-13 15:55:30.120039
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    # Test for valid input
    res = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
    assert res == 'action', "res: %s" % res
    res = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins')
    assert res == 'lookup', "res: %s" % res
    # Test for invalid input
    with pytest.raises(ValueError):
        res = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid')


# Generated at 2022-06-13 15:55:38.367794
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    # FQCR for a custom module
    fqcr0 = 'testing.example.jerry'
    fqcr_ref0 = AnsibleCollectionRef.try_parse_fqcr(fqcr0, 'modules')
    assert fqcr_ref0 is not None
    assert fqcr_ref0.collection == 'testing.example'
    assert fqcr_ref0.ref_type == 'modules'
    assert fqcr_ref0.resource == 'jerry'
    assert fqcr_ref0.subdirs == ''
    assert fqcr_ref0.fqcr == 'testing.example.jerry'
    assert fqcr_ref0.n_python_package_name == 'ansible_collections.testing.example.plugins.modules'
    assert fqcr_ref0.n_python

# Generated at 2022-06-13 15:55:40.387023
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    path_list = []
    redirect_loader = _AnsibleInternalRedirectLoader('ansible.module_utils.six', path_list)
    assert redirect_loader



# Generated at 2022-06-13 15:55:50.829923
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    '''
    _AnsibleCollectionPkgLoaderBase: Test load_module.
    '''
    # fullname will be equal to 'ansible_collections.test_collection.test_package.test_module'
    collection_name = 'test_collection'
    package_name = 'test_package'
    module_name = 'test_module'

    # create a collection
    collection_loader, collection_path = _AnsibleCollectionFinder._create_collection(collection_name)

    # load the package
    package_loader, package_path = _AnsibleCollectionFinder._create_collection_package(collection_path, collection_name, package_name)

    # load the module

# Generated at 2022-06-13 15:56:00.721041
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    try:
        import_module('ansible.module_utils.ansible_sphinx')
    except:
        # running as part of ansible-test, no need to test ansible_internal_redirect
        return

    loader = _AnsibleCollectionFinder()
    loader._n_configured_paths = ['lib']
    loader._install()

    # test ansible_internal_redirect
    ansible_module_utils = import_module('ansible.module_utils')
    assert hasattr(ansible_module_utils, 'ansible_sphinx')
    assert ansible_module_utils.ansible_sphinx.__name__ == 'ansible_collections.ansible.community.plugins.modules.module_utils.ansible_sphinx'
    assert ansible_module_utils.ansible_

# Generated at 2022-06-13 15:56:03.957395
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.yaml_utils', None)
    loader.load_module('ansible.module_utils.yaml_utils')


# helper function to get the appropriate loader for a given import request

# Generated at 2022-06-13 15:56:13.879575
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    file_finder = '_AnsibleCollectionPkgLoaderBase'
    fullname = 'ansible_collections.samples.test'
    filename = '_AnsibleCollectionPkgLoaderBase'
    source_code_path = '_AnsibleCollectionPkgLoaderBase'
    subpackage_search_paths = '_AnsibleCollectionPkgLoaderBase'
    module_attrs = {'__loader__': '__loader__', '__file__': '__file__'}
    code_obj = '_AnsibleCollectionPkgLoaderBase'
    # Case 1- check the filename when subpackage_search_paths is not None
    _AnsibleCollectionPkgLoaderBase._subpackage_search_paths = subpackage_search_paths

# Generated at 2022-06-13 15:56:40.569728
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # noinspection PyCallingNonCallable
    AnsibleCollectionRef(collection_name='namespace.collectionname', subdirs='subdir1.subdir2', resource='resource_name', ref_type='module')

    try:
        # noinspection PyCallingNonCallable
        # bad namespace
        AnsibleCollectionRef(collection_name='namespace.collectionname', subdirs='subdir1.subdir2', resource='resource_name', ref_type='module')
        raise AssertionError('AnsibleCollectionRef constructor failed to fail on bad namespace')
    except ValueError:
        pass


# Generated at 2022-06-13 15:56:46.492552
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr("ns.coll.subdir1.subdir2.resource")
    assert AnsibleCollectionRef.is_valid_fqcr("ns.coll.resource")
    assert AnsibleCollectionRef.is_valid_fqcr("ns.coll.resource.yml")
    assert AnsibleCollectionRef.is_valid_fqcr("ns.coll.resource.yml", "playbook")
    assert not AnsibleCollectionRef.is_valid_fqcr("ns.coll.")
    assert not AnsibleCollectionRef.is_valid_fqcr("ns.coll.subdir1.")
    assert not AnsibleCollectionRef.is_valid_fqcr("ns.coll.subdir1.subdir2.")

# Generated at 2022-06-13 15:56:58.075364
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    class SampleLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self): pass  # don't bother the base class with our data
        def _get_candidate_paths(self, path_list): return path_list  # normal CWD behavior
        def _get_subpackage_search_paths(self, candidate_paths): return candidate_paths  # normal dir/filesource behavior
        def _validate_final(self): pass  # don't bother the base class with our data
        def is_package(self, fullname): return self._package_to_load == 'package'  # assume container is a dir, not a module
        def _synthetic_filename(self, fullname): return '__synthetic_filename__'  # don't bother the base class with our data


# Generated at 2022-06-13 15:57:02.038222
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    loader = _AnsibleInternalRedirectLoader('ansible.builtin.unarchive', None)
    assert loader._redirect == 'ansible.module_utils.archive.unarchive'


# TODO: add unit tests

# Generated at 2022-06-13 15:57:13.264512
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    paths = ['/tmp/ansible/collections']
    def test_paths(paths, expected):
        finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=True)
        assert finder._n_configured_paths == expected
        assert finder._n_cached_collection_paths is None
        assert finder._n_cached_collection_qualified_paths is None
        # Expecting a list of length 2 because scan_sys_paths=True and sys.path contains one item
        assert len(finder._n_collection_paths) == 2
        assert finder._n_playbook_paths == []
        assert finder._n_configured_paths[0] in finder._n_collection_paths
        assert finder._n_collection_path

# Generated at 2022-06-13 15:57:20.243297
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():

  # #############
  # #############
  # #############
  # create instance of class to be tested
  class_to_test = _AnsibleInternalRedirectLoader

  # #############
  # #############
  # #############
  # call_#1

  # set up parameters
  fullname = 'ansible.module_utils.common.collections'
  path_list = []

  # create instance of class to be tested
  class_instance = class_to_test(fullname, path_list)

  # call method
  method_test = 'load_module'
  assert(hasattr(class_instance, method_test))
  assert(callable(getattr(class_instance, method_test)))
  method_result = getattr(class_instance, method_test)(fullname)

 

# Generated at 2022-06-13 15:57:25.949329
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import tempfile
    from shutil import rmtree
    import types

    # mock some yaml_dict for test purpose
    yaml_dict = {'uri': 'tar+http://test_collection.tar.gz'}

    # Test case 1: prefix is 'ansible_collections' and fullname is 'ansible_collections.test_ns'
    path = tempfile.mkdtemp()
    fullname = 'ansible_collections.test_ns'
    prefix = 'ansible_collections'
    collection_finder = _AnsibleCollectionFinder(paths=[path])
    ansible_path_hook_finder = _AnsiblePathHookFinder(collection_finder, path)
    # Mock for the test purpose

# Generated at 2022-06-13 15:57:31.688818
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from ansible.module_utils.parsing.convert_bool import boolean
    import sre_constants  # noqa
    import sre_parse  # noqa
    import re  # noqa
    import os  # noqa
    import tempfile  # noqa
    import os.path as osp  # noqa
    import sys  # noqa
    import os.path as osp  # noqa
    import sys  # noqa
    import types  # noqa
    import os  # noqa
    import zipfile  # noqa
    import tempfile  # noqa
    import ansible.module_utils.six.moves.urllib.parse as urlparse  # noqa
    import sre_constants  # noqa
    import sre_parse  # noqa
    import re  #

# Generated at 2022-06-13 15:57:32.272836
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # TODO: not implemented
    return



# Generated at 2022-06-13 15:57:38.212858
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    acr = AnsibleCollectionRef.is_valid_fqcr
    assert acr('namespace.collection.resource_name')
    assert acr('ns.coll.subdir1.subdir2.resource_name')
    assert acr('namespace.collection.playbook.yml')
    assert acr('namespace.collection.playbook.yaml')
    assert acr('namespace.collection.playbook.json')
    assert acr('namespace.collection.playbook.jpg')
    assert acr('namespace.collection.playbook.md')
    assert not acr('ns')
    assert not acr('ns.coll')
    assert not acr('.coll.adjaiia')
    assert not acr('ns.coll.')
    assert not acr('ns.coll.')
    assert not acr

# Generated at 2022-06-13 15:58:11.539408
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    fqcr = u"ns.collection.resource"
    assert AnsibleCollectionRef.is_valid_fqcr(fqcr, u"module")

    fqcr = u"ns.collection.subdir.subdir.resource"
    assert AnsibleCollectionRef.is_valid_fqcr(fqcr, u"module")

    fqcr = u"ns.collection.rolename"
    assert AnsibleCollectionRef.is_valid_fqcr(fqcr, u"role")

    fqcr = u"ns.collection.subdir.subdir.rolename"
    assert AnsibleCollectionRef.is_valid_fqcr(fqcr, u"role")

    fqcr = u"ns.collection.subdir.subdir.rolename.yml"
    assert AnsibleCollectionRef.is_

# Generated at 2022-06-13 15:58:22.891226
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test ref_type is valid
    # Valid ref_type
    AnsibleCollectionRef('namespace.collection', 'subdir', 'resource', 'modules')
    # Invalid ref_type
    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace.collection', 'subdir', 'resource', 'foo')

    # Test collection_name is valid
    # Valid namespace and valid collection name
    AnsibleCollectionRef('namespace.collection', 'subdir', 'resource', 'modules')
    # Invalid namespace and valid collection name
    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace.collec tion', 'subdir', 'resource', 'modules')
    # Valid namespace and invalid collection name

# Generated at 2022-06-13 15:58:28.110304
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    from ansible.utils.collection_loader import _meta_yml_to_dict
    import_module('ansible')
    _meta_yml_to_dict = None
    c = _AnsibleCollectionPkgLoader('ns.coll', _meta_yml_to_dict)
    assert c.load_module('ns.coll') == None




# Generated at 2022-06-13 15:58:37.809633
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    collectionName = 'namespace.collection'
    subdir = 'subdir1.subdir2'
    resource = 'resource'
    ref_type = 'module'

    ansible_collection_ref = AnsibleCollectionRef(collectionName, subdir, resource, ref_type)

    assert (ansible_collection_ref.is_valid_fqcr(u'name.space.subdir1.subdir2.my_mod') == True)
    assert (ansible_collection_ref.is_valid_fqcr(u'ns.coll') == False)
    assert (ansible_collection_ref.is_valid_fqcr(u'ns.coll.subdir1.subdir2.subdir3.subdir4.subdir5.my_mod') == False)

# Generated at 2022-06-13 15:58:38.666219
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    pass

# Generated at 2022-06-13 15:58:46.084332
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    ALPLBase = _AnsibleCollectionPkgLoaderBase('')
    ALPLBase._subpackage_search_paths = []
    ALPLBase._source_code_path = '/path/to/module.py'
    assert repr(ALPLBase) == '_AnsibleCollectionPkgLoaderBase(path=/path/to/module.py)'

    ALPLBase._subpackage_search_paths = ['/path/to/subpackage']
    ALPLBase._source_code_path = ''
    assert repr(ALPLBase) == '_AnsibleCollectionPkgLoaderBase(path=[/path/to/subpackage])'



# Generated at 2022-06-13 15:58:47.671709
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    assert True, "Test if the method __repr__ of class AnsibleCollectionRef works."


# Generated at 2022-06-13 15:58:55.370400
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    ref = AnsibleCollectionRef(u'my.collection', None, u'module1', u'module')
    assert ref.collection == u'my.collection'
    assert not ref.subdirs
    assert ref.resource == u'module1'
    assert ref.ref_type == u'module'
    assert ref.fqcr == u'my.collection.module1'
    assert ref.n_python_package_name == 'ansible_collections.my.collection.plugins.modules.module1'
    assert ref.n_python_collection_package_name == 'ansible_collections.my.collection'

    ref = AnsibleCollectionRef(u'my.collection', u'subdir1.subdir2', u'module1', u'module')

# Generated at 2022-06-13 15:59:02.276784
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    true_parameters = [
        ('a.b.c', 'd', 'a.b.c'),
        ('a.b.c', 'd.e.f', 'a.b.c.d.e.f'),
        ('a.b.c', 'd.e.f.g', 'a.b.c.d.e.f.g'),
        ('a.b.c', 'd.e.f.g.h', 'a.b.c.d.e.f.g.h'),
        ('a.b.c', 'd.e.f.g.h.i', 'a.b.c.d.e.f.g.h.i'),
    ]