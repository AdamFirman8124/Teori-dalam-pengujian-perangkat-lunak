

# Generated at 2022-06-13 15:50:19.114412
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    m=_AnsibleCollectionPkgLoaderBase('./ansible_collections/ns/collection/plugins/modules')
    m._source_code_path = './ansible_collections/ns/collection/plugins/modules.py'
    m._fullname = 'ns.collection.plugins.modules'
    m._parent_package_name = 'ns.collection.plugins'
    m._package_to_load = 'modules'
    m._get_candidate_paths([p for p in sys.path if 'ansible_collections' in p])
    m._validate_final()
    m._decoded_source = 'def main(): "do nothing"'
    m.get_data(m._source_code_path)

# Generated at 2022-06-13 15:50:27.870384
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Make sure __init__ raises exceptions when passed invalid arguments
    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace.', 'subdir', 'mymodule', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace.collection', 'sub dir', 'mymodule', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace..collection', '', 'mymodule', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef('1namespace.collection', '', 'mymodule', 'module')

    with pytest.raises(ValueError):
        AnsibleCollectionRef('namespace.1collection', '', 'mymodule', 'module')

    with pytest.raises(ValueError):
        Ansible

# Generated at 2022-06-13 15:50:39.094898
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    class DummyLoader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            # fake candidate paths that have an __init__.py file at the root level
            return [to_native(path_list[0] + '/ansible_collections/test_ns/test_coll')]

        def _get_subpackage_search_paths(self, candidate_paths):
            # filter candidate paths for existence (NB: silently ignoring package init code and same-named modules)
            return [p for p in candidate_paths if os.path.isdir(to_bytes(p))]


# Generated at 2022-06-13 15:50:48.622527
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # For python 2.7, add alias StringIO to io.StringIO
    try:
        import StringIO
    except ImportError:
        pass

    import sys
    import unittest
    from unittest.mock import patch
    from io import StringIO

    # import io.StringIO as StringIO
    # from io import BytesIO

# Generated at 2022-06-13 15:50:54.928270
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible.module_utils.foo", path_list=["/path/to/module_utils"])
    loader.get_code("ansible.module_utils.foo")
    import os.path
    with mock.patch.object(os.path, 'dirname', return_value='/path/to/module_utils'):
        loader.get_code("ansible.module_utils.foo")


# Generated at 2022-06-13 15:51:05.542106
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # Simple role test
    ref = AnsibleCollectionRef.from_fqcr('ansible.test.test_role', 'role')
    assert ref.collection == 'ansible.test'
    assert ref.subdirs == ''
    assert ref.resource == 'test_role'
    assert ref.ref_type == 'role'

    # Simple module test
    ref = AnsibleCollectionRef.from_fqcr('ansible.test.test_module', 'module')
    assert ref.collection == 'ansible.test'
    assert ref.subdirs == ''
    assert ref.resource == 'test_module'
    assert ref.ref_type == 'module'

    # Subdirs test

# Generated at 2022-06-13 15:51:18.377474
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    from ansible_collections.testns.testcoll.plugins.filter import testfilter

    test_collection_ref = AnsibleCollectionRef.from_fqcr('testns.testcoll.plugins.filter.testfilter', 'filter')

    assert test_collection_ref.collection == 'testns.testcoll'
    assert test_collection_ref.plugin_type == 'filter'
    assert test_collection_ref.plugin_name == 'filter'
    assert test_collection_ref.resource == 'testfilter'
    assert test_collection_ref.fqcr == 'testns.testcoll.plugins.filter.testfilter'
    assert test_collection_ref.fq_name == 'testns.testcoll'

# Generated at 2022-06-13 15:51:31.133679
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    output = tempfile.mkdtemp(prefix='ansible_')
    output_collection = os.path.join(output, 'ansible_collections')
    os.makedirs(output_collection)
    open(os.path.join(output_collection, 'ansible_collections', 'test_module.py'), 'w').close()
    open(os.path.join(output_collection, 'collection1', 'module1.py'), 'w').close()
    open(os.path.join(output_collection, 'collection1', '__init__.py'), 'w').close()
    open(os.path.join(output_collection, 'collection2', 'module2.py'), 'w').close()
    open(os.path.join(output_collection, 'collection2', '__init__.py'), 'w').close

# Generated at 2022-06-13 15:51:39.062740
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    collection_name = 'namespace.collectionname'
    subdirs = 'subdir1.subdir2.subdir3'
    resource = 'resource_name'

    test_obj = AnsibleCollectionRef(collection_name, subdirs, resource, 'module')

    expected_result = 'AnsibleCollectionRef(collection=\'namespace.collectionname\', subdirs=\'subdir1.subdir2.subdir3\', resource=\'resource_name\')'
    result = test_obj.__repr__()

    assert result == expected_result


# Generated at 2022-06-13 15:51:45.539601
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader("ansible_collections.namespace.collection.name", path=['/test_path'])
    assert loader.load_module("ansible_collections.namespace.collection.name") is None
    loader = _AnsibleCollectionPkgLoader("ansible_collections.namespace.collection.name", path=['/test_path'])
    loader._validate_final = lambda: None
    assert loader.load_module("ansible_collections.namespace.collection.name") is None
    loader = _AnsibleCollectionPkgLoader("ansible_collections.namespace.collection.name", path=['/test_path'])
    loader._split_name = ["ansible_collections", "namespace", "collection"]
    loader._validate_final = lambda: None


# Generated at 2022-06-13 15:52:22.540087
# Unit test for constructor of class _AnsibleCollectionRootPkgLoader
def test__AnsibleCollectionRootPkgLoader():
    # Test with valid parameter
    try:
        x = _AnsibleCollectionRootPkgLoader('ansible_collections', ['/usr/lib/python3.7/site-packages'])
        assert True
    except Exception:
        assert False

    # Test with invalid parameter
    try:
        x = _AnsibleCollectionRootPkgLoader('ansible_collections.mycollection', ['/usr/lib/python3.7/site-packages'])
        assert False
    except Exception:
        assert True


# Generated at 2022-06-13 15:52:31.731918
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    # self._decoded_source = None
    # self._source_code_path = None
    loader = _AnsibleCollectionPkgLoaderBase('./ansible/plugins')
    assert loader.get_source(loader._fullname) is None
    # self._decoded_source = "abc"
    loader = _AnsibleCollectionPkgLoaderBase('./ansible/plugins', ['some_path'])
    assert loader.get_source(loader._fullname) == 'abc'
    # self._source_code_path = 'some_path'
    loader = _AnsibleCollectionPkgLoaderBase('./ansible/plugins', ['some_path'])
    assert loader.get_source(loader._fullname) == 'abc'

# Generated at 2022-06-13 15:52:44.499496
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import re
    import traceback
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO

    import pytest
    from ansible.module_utils._text import to_bytes

    def setup_loader_module(loader, module_name, module_code):
        loader._path_list = ['/mock/package']
        loader._fullname = module_name
        loader._split_name = module_name.split('.')
        loader._rpart_name = module_name.rpartition('.')
        loader._parent_package_name = loader._rpart_name[0]
        loader._package_to_load = loader._rpart_name[2]

# Generated at 2022-06-13 15:52:54.185067
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # create a temporary collection
    collection_info = MOCK_COLLECTION_INFO.copy()
    collection_info['namespace'] = 'whatever'
    collection_info['name'] = 'foobarbaz'
    collection_metadata = mock_collection(collection_info)

    # create a temporary loader
    class MockCollLoader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            return path_list

        def _get_subpackage_search_paths(self, candidate_paths):
            return candidate_paths

        def _validate_final(self):
            pass


# Generated at 2022-06-13 15:52:59.418657
# Unit test for constructor of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase():
    class MyPkgLoader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_candidate_paths(self, path_list):
            return path_list

        def _get_subpackage_search_paths(self, candidate_paths):
            return candidate_paths

        def _validate_final(self):
            pass

    class MyMockModule(ModuleType):
        pass

    # mock out _new_or_existing_module for testability
    @contextmanager
    def my_new_or_existing_module(name, **kwargs):
        module = MyMockModule(name)
        for attr, value in kwargs.items():
            setattr(module, attr, value)
        yield module

    MyPkgLoader._new

# Generated at 2022-06-13 15:53:07.137180
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    for ref_type in ['action', 'become', 'cache', 'callback', 'cliconf', 'connection', 'doc_fragments', 'filter', 'httpapi', 'inventory', 'lookup', 'module_utils', 'modules', 'netconf', 'role', 'shell', 'strategy', 'terminal', 'test', 'vars', 'playbook']:
        ref = AnsibleCollectionRef('namespace.collname', None, 'resource', ref_type)
        assert ref.collection == 'namespace.collname'
        assert ref.subdirs == ''
        assert ref.resource == 'resource'
        assert ref.ref_type == ref_type
        assert ref.n_python_collection_package_name == 'ansible_collections.namespace.collname'

# Generated at 2022-06-13 15:53:20.282420
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    F_path = tempfile.mkdtemp()
    F_module_path = '{0}/{1}'.format(F_path, 'test_module.py')
    with open(F_module_path, 'w+') as F_module:
        F_module.writelines(['from ansible.module_utils.basic import AnsibleModule'])

    F_module_name = 'test_module'
    F_module = AnsibleCollectionLoader(path=F_path)
    F_module_code = F_module.load_module(F_module_name)
    F_module_code_path = F_module_code.__file__
    # Check that the file name of module code is the same as the file name of testing module
    if F_module_code_path != F_module_path:
        raise

# Generated at 2022-06-13 15:53:26.906823
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import os
    import imp
    import inspect
    import unittest
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoaderBase
    from ansible.utils.collection_loader import _AnsibleCollectionPkgLoader
    from ansible.utils.collection_loader import _AnsibleCollectionNSLoader
    class Test_AnsibleCollectionPkgLoaderBase_get_source(unittest.TestCase):
        def test__get_source(self):
            ansible_collections_path = [os.path.join(os.path.dirname(inspect.getfile(imp)), '..', '..', '..', '..', 'test', 'ansible_collections')]

# Generated at 2022-06-13 15:53:34.655560
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    import collections
    loader = _AnsibleCollectionPkgLoaderBase('ansible.test', path_list=['/usr/share/ansible_collections/ansible/test'])
    assert list(loader.iter_modules('notaprefix')) == collections.OrderedDict()
    assert list(loader.iter_modules('ansible.test')) == collections.OrderedDict([('ansible.test.foo', None)])
    assert list(loader.iter_modules('')) == collections.OrderedDict([('ansible.test.foo', None)])



# Generated at 2022-06-13 15:53:41.601329
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    import os
    import os.path
    import sys
    sys.meta_path=[]
    sys.path_hooks=[]
    sys.path_importer_cache={}
    finder = _AnsibleCollectionFinder()
    finder._remove()
    sys.meta_path.insert(0, finder)
    sys.path_hooks.insert(0, finder._ansible_collection_path_hook)
    class AnsibleCollectionConfig:
        collection_finder=None
    ansible_collection_config = AnsibleCollectionConfig()
    ansible_collection_config.collection_finder = finder
    assert finder.find_module('ansible.builtin') == None
    assert finder.find_module('ansible.module_utils.common.removed') == None
    assert finder.find_module

# Generated at 2022-06-13 15:54:19.001757
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Create a mock object for module_utils and test class
    class Test_loader:
        pass

    loader = Test_loader()
    # Create a mock object for module_utils and test class
    class Test_path:
        pass

    path = Test_path()
    # Create a mock object for module_utils and test class
    class Test_sys:
        pass

    sys = Test_sys()
    # Create a mock object for module_utils and test class
    class Test_fullname:
        pass

    fullname = Test_fullname()
    # Check for the case, when module name is ansible.module_utils.basic
    result = loader.find_module(path, fullname)
    assert result is not None

    # Check for the case, when module name is ansible_collections.module_utils.basic

# Generated at 2022-06-13 15:54:28.850888
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycollection', 'role') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycoll', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycoll.doc_fragments', 'doc_fragments') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycoll.foo.bar', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycoll.foo.bar.mymodule', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('collection.mycoll.foo.bar.doc_fragments', 'doc_fragments') is not None

# Generated at 2022-06-13 15:54:37.897715
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    obj = AnsibleCollectionRef.from_fqcr('ns.coll1.resource', 'module')

    assert obj.collection == 'ns.coll1'
    assert obj.subdirs == ''
    assert obj.resource == 'resource'
    assert obj.ref_type == 'module'
    assert obj.n_python_package_name == 'ansible_collections.ns.coll1.plugins.module'
    assert obj.fqcr == 'ns.coll1.resource'

    obj = AnsibleCollectionRef.from_fqcr('ns.coll1.subdir1.resource', 'module')

    assert obj.collection == 'ns.coll1'
    assert obj.subdirs == 'subdir1'
    assert obj.resource == 'resource'
    assert obj.ref_type == 'module'
    assert obj.n

# Generated at 2022-06-13 15:54:42.907599
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible_test._internal.common.collections import AnsibleCollectionLoaderFixture
    from ansible_test._internal.common.diff import assert_equal
    from ansible_test._internal.sanity.config import ConfigFixtureMixin
    from ansible_test._internal.sanity.code.unit.collection_loader import _AnsibleCollectionLoaderFixture
    from ansible_test._internal.sanity.code.unit.collection_loader import _AnsibleCollectionFinderFixture
    import ansible_test
    import os

    fixture = _AnsibleCollectionFinderFixture()
    fixture.add_collection('foobar.barfoo')

    # None

# Generated at 2022-06-13 15:54:53.225474
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ref1 = AnsibleCollectionRef.from_fqcr('ns.coll.hiera', 'role')
    assert ref1.collection == 'ns.coll'
    assert ref1.ref_type == 'role'
    assert ref1.resource == 'hiera'
    assert ref1.subdirs == ''

    ref2 = AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.hiera', 'role')
    assert ref2.collection == 'ns.coll'
    assert ref2.ref_type == 'role'
    assert ref2.resource == 'hiera'
    assert ref2.subdirs == 'subdir1'

    ref3 = AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.subdir2.hiera', 'role')

# Generated at 2022-06-13 15:54:56.165887
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    # TODO: add unit test for method is_valid_fqcr of class AnsibleCollectionRef  # noqa
    raise Exception('test not implemented')

# Generated at 2022-06-13 15:55:04.157141
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:55:13.488206
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    file_finder_hook = _AnsiblePathHookFinder._get_filefinder_path_hook(None)
    # Assume the module "ansible" is installed under "/usr/lib/python3.X/site-packages"
    collection_finder = _AnsibleCollectionFinder(paths="/usr/lib/python3.X/site-packages")
    collection_finder._install()
    ansible_path_hook = _AnsiblePathHookFinder(collection_finder, "/usr/lib/python3.X/site-packages")
    # If the module "not_exists_module" doesn't exist, it should return None
    assert ansible_path_hook.find_module("not_exists_module", path="/usr/lib/python3.X/site-packages") == None
    # If the module "ans

# Generated at 2022-06-13 15:55:23.142875
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    model = AnsibleCollectionLoader()
    ansible_collection_name = "one"
    ansible_namespace = "two"
    ansible_sub = "sub"
    fullname = "ansible_collections.{0}.{1}.{2}".format(ansible_collection_name, ansible_namespace, ansible_sub)
    path_list = [os.path.join(os.path.dirname(__file__), 'data')]
    module_obj = model.load_module(fullname)
    assert module_obj.__file__.endswith(os.path.join('data', ansible_collection_name, ansible_namespace, ansible_sub, '__synthetic__'))

# Generated at 2022-06-13 15:55:25.811550
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    loader = _AnsibleInternalRedirectLoader
    assert(loader)



# Generated at 2022-06-13 15:55:53.547335
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    '''
    This function tests the method __repr__ of class _AnsibleCollectionPkgLoaderBase.
    '''
    raise NotImplementedError

# Generated at 2022-06-13 15:56:03.522089
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # set up
    fullname = 'ansible_collections.ns1.sub1'
    helper = _AnsibleCollectionPkgLoaderBase(fullname, ['/my/path1', '/my/path2'])
    def _get_candidate_paths(path_list):
        return [os.path.join(p, 'sub1') for p in path_list]
    helper._get_subpackage_search_paths = _get_candidate_paths
    helper._subpackage_search_paths = _get_candidate_paths([])

    # test: resource exists

# Generated at 2022-06-13 15:56:08.223976
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    '''
    Test that the __repr__ method returns the correct representation
    of class AnsibleCollectionRef
    '''
    test_collref = AnsibleCollectionRef('galaxy.ansible.collection', 'subdirs', 'module', 'module')
    assert test_collref.__repr__() == "AnsibleCollectionRef(collection='galaxy.ansible.collection', subdirs='subdirs', resource='module')"


# Generated at 2022-06-13 15:56:14.296042
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    acr = AnsibleCollectionRef('namespace.collection', None, 'resource', 'module')
    assert acr.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert acr.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'
    assert acr.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'
    assert acr.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'
    assert acr.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'
    assert acr.legacy_plugin_dir_to_plugin_type('doc_fragments') == 'doc_fragments'
    assert acr

# Generated at 2022-06-13 15:56:24.072311
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    def get_code(fullname):
        _AnsibleCollectionFinder._remove()
        af = _AnsibleCollectionFinder(paths=[' '])
        af.set_playbook_paths([' '])
        af._install()

        return af.find_module(fullname)

    assert get_code('ansible.module_utils.some_utils')
    assert get_code('ansible_collections.ns.some_coll.plugins.module_utils.some_utils')
    assert get_code('ansible_collections.ns.some_coll.plugins.modules.some_mod')
    assert get_code('ansible_collections.ns.some_coll.plugins.modules')



# Generated at 2022-06-13 15:56:35.070780
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    with mock.patch('ansible_collections.ansible.builtin.plugins.module_loader._AnsibleCollectionPkgLoaderBase._new_or_existing_module') as _new_or_existing_module, \
         mock.patch('ansible_collections.ansible.builtin.plugins.module_loader._AnsibleCollectionPkgLoaderBase.get_code') as get_code, \
         mock.patch('ansible_collections.ansible.builtin.plugins.module_loader._AnsibleCollectionPkgLoaderBase.get_filename') as get_filename:
        _new_or_existing_module.return_value.__enter__.return_value = 'entered'
        get_code.return_value = 'code'
        get_filename.return_value = 'filename'
        loader_instance = ansible_

# Generated at 2022-06-13 15:56:38.205419
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    loader = _AnsibleInternalRedirectLoader('ansible.utils.color', None)
    module = loader.load_module('ansible.utils.color')
    assert module.__name__ == 'ansible.builtin.utils.color'
# Test for method fullname of class _AnsibleInternalRedirectLoader

# Generated at 2022-06-13 15:56:45.181915
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    pkg_loader = _AnsibleCollectionPkgLoaderBase(
        fullname='ansible_collections.testns.testcoll',
        path_list=['/tmp']
    )

    assert pkg_loader.__repr__() == "_AnsibleCollectionPkgLoaderBase(path=['/tmp/testcoll'])"

    pkg_loader = _AnsibleCollectionPkgLoaderBase(
        fullname='ansible_collections.testns.testcoll',
        path_list=['/tmp']
    )

    assert pkg_loader.__repr__() == "_AnsibleCollectionPkgLoaderBase(path=['/tmp/testcoll'])"



# Generated at 2022-06-13 15:56:56.651612
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    test_cases = [
        ("/mock/path/to/mock_module.py", b'test_content'),
        ("/mock/path/to/mock_module.py", None),
        ("/mock/path/to/subpackage", "subpackage_content"),
        ("/mock/path/to/subpackage", None),
    ]

    for test_data in test_cases:
        mock_path = test_data[0]
        mock_content = test_data[1]

        class _MockLoader(_AnsibleCollectionPkgLoaderBase):
            def _validate_args(self):
                pass

            def load_module(self, fullname):
                pass

            def _get_candidate_paths(self, path_list):
                return []


# Generated at 2022-06-13 15:57:03.834414
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    with _temp_path_collection_loaders() as package_1_path, _temp_path_collection_loaders() as package_2_path:
        with open(os.path.join(package_1_path, '__init__.py'), 'wb') as f:
            f.write(b'#')
        with open(os.path.join(package_1_path, 'module_1.py'), 'wb') as f:
            f.write(b'#')
        with open(os.path.join(package_1_path, 'module_2.py'), 'wb') as f:
            f.write(b'#')
        with open(os.path.join(package_2_path, 'module_3.py'), 'wb') as f:
            f.write(b'#')

        loader