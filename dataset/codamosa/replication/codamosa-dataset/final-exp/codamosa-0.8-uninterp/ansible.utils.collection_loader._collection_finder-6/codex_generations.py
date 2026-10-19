

# Generated at 2022-06-13 15:49:50.315187
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ref = AnsibleCollectionRef.from_fqcr(u'namespace.collection.subdir1.subdir2.testmodule', u'action')
    assert ref.collection == u'namespace.collection'
    assert ref.subdirs == u'subdir1.subdir2'
    assert ref.resource == u'testmodule'
    assert ref.ref_type == u'action'
    assert ref.n_python_collection_package_name == u'ansible_collections.namespace.collection'
    assert ref.n_python_package_name == u'ansible_collections.namespace.collection.plugins.subdir1.subdir2.action.testmodule'
    assert ref.fqcr == u'namespace.collection.subdir1.subdir2.testmodule'


# Generated at 2022-06-13 15:50:02.738316
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    class Test_AnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        # Overriding the __init__ method with a new one
        def __init__(self, fullname, path_list=None):
            super(Test_AnsibleCollectionPkgLoaderBase, self).__init__(fullname, path_list)

        # Overriding the _get_candidate_paths method of _AnsibleCollectionPkgLoaderBase
        def _get_candidate_paths(self, path_list):
            return [os.path.join(p, self._package_to_load) for p in path_list]

        # Overriding the _get_subpackage_search_paths method of _AnsibleCollectionPkgLoaderBase

# Generated at 2022-06-13 15:50:09.136401
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    with pytest.raises(ValueError) as err:
        AnsibleCollectionRef("", "", "", "")
    assert 'arguments.collection_name' in str(err)

    with pytest.raises(ValueError) as err:
        AnsibleCollectionRef("foo", "", "", "")
    assert 'arguments.collection_name' in str(err)

    with pytest.raises(ValueError) as err:
        AnsibleCollectionRef("foo.bar", "", "", "non_existent")
    assert 'arguments.ref_type' in str(err)

    with pytest.raises(ValueError) as err:
        AnsibleCollectionRef("foo.bar", "asdf.askdjf.asdf", "test", "role")

# Generated at 2022-06-13 15:50:19.193601
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():

    test_cases = [
        {
            'desc': '__init__.py exists',
            'path': '/a/b/c/__init__.py',
            'expected': '',
        },
        {
            'desc': '__init__.py does not exist',
            'path': '/a/b/c/__init__.py',
            'expected': None,
        },
    ]

    class CollectionPkgLoader(object):
        def __init__(self, paths=None):
            self._subpackage_search_paths = paths

    pkg_loader = CollectionPkgLoader(['/a/b'])

    for test_case in test_cases:
        assert pkg_loader.get_data(test_case['path']) is test_case['expected'], '{0} failed'.format

# Generated at 2022-06-13 15:50:25.926459
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    assert load_module(
        fullname='ansible.plugins.strategy.linear.api',
        path_list='/Users/zhengbofan/PycharmProjects/ansible/ansible-base/ansible/',
        group_id='com.ansible.builtin:runtime',
        collection_version='1.0.0-0'
    )



# Generated at 2022-06-13 15:50:37.720442
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
  import os
  import tempfile
  import shutil
  import inspect
  import sys

  # Create a temporary directory
  tmpdir = tempfile.mkdtemp()

  # create the following layout:
  #   .
  #   |tmpdir
  #   |
  #   |__ansible_collections
  #   |  |__example_collection
  #   |     |__targets
  #   |        |__plugins
  #   |        |__module_utils
  #   |        |__doc_fragments
  #   |        |__molecule
  #   |           |__default
  #   |              |__INSTALL_REQUIREMENTS.txt
  #   |              |__test.py
  #   |           |__tests
  #   |              |__test_test.

# Generated at 2022-06-13 15:50:44.892969
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    fqcr_none = AnsibleCollectionRef.try_parse_fqcr(None, None)
    fqcr_empty = AnsibleCollectionRef.try_parse_fqcr('', '')
    fqcr_0 = AnsibleCollectionRef.try_parse_fqcr('a.b.c', '')
    fqcr_1 = AnsibleCollectionRef.try_parse_fqcr('a.b.c', 'd')
    fqcr_2 = AnsibleCollectionRef.try_parse_fqcr(u'a.b', u'c')
    assert fqcr_none is None, 'should be none'
    assert fqcr_empty is None, 'should be none'
    assert fqcr_0 is None, 'should be none'

# Generated at 2022-06-13 15:50:56.194709
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module(): # pylint: disable=too-many-locals,too-many-statements,too-many-branches
    # Make sure we have a path for collections on disk.
    temp_dir = tempfile.mkdtemp()
    ansible_collections_dir = os.path.join(temp_dir, 'ansible_collections')
    os.makedirs(ansible_collections_dir)
    test_ansible_collections_dir = os.path.join(ansible_collections_dir, 'test')
    os.makedirs(test_ansible_collections_dir)
    test_ansible_collection_dir = os.path.join(test_ansible_collections_dir, 'test_collection')
    os.makedirs(test_ansible_collection_dir)

    # Add it to the

# Generated at 2022-06-13 15:50:59.489204
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    inst = _AnsibleCollectionPkgLoaderBase("fullname")
    with pytest.raises(Exception):
        inst.__repr__()



# Generated at 2022-06-13 15:51:11.416343
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Tests for parsing a reference that includes subdirs and resource type
    anr = AnsibleCollectionRef.from_fqcr('ns.coll.subdir1.subdir2.subdir3.modulename', 'module')
    assert anr.collection == u'ns.coll'
    assert anr.subdirs == u'subdir1.subdir2.subdir3'
    assert anr.resource == u'modulename'
    assert anr.fqcr == u'ns.coll.subdir1.subdir2.subdir3.modulename'
    #assert anr.n_python_package_name == u'ansible_collections.ns.coll.plugins.subdir1.subdir2.subdir3.module'

    # Tests for parsing a reference that includes subdirs and resource type
   

# Generated at 2022-06-13 15:52:07.468007
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    valid_ref = 'test.col.role.test_role'
    assert AnsibleCollectionRef.is_valid_fqcr(valid_ref) == True, "test_AnsibleCollectionRef_is_valid_fqcr:{0} failed ".format(valid_ref)

    valid_ref = 'test.col.role.test_role.yml'
    assert AnsibleCollectionRef.is_valid_fqcr(valid_ref) == True, "test_AnsibleCollectionRef_is_valid_fqcr:{0} failed ".format(valid_ref)

    valid_ref = 'test.col.role.test_role.yaml'

# Generated at 2022-06-13 15:52:16.461135
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    fail_msg = "Expected an exception of type "
    assert_msg = "Expected: {0} \n Got: {1}"
    assert_value_msg = "The value of [{0}]: expected: {1}, got: {2}"

    test_path_list_1 = ["/this/is/the/first/path", "/this/is/the/second/path"]
    test_path_list_2 = ["/this/is/the/second/path", "/this/is/the/third/path"]
    test_path_list_3 = ["/this/is/the/fourth/path", "/this/is/the/fifth/path"]
    test_path_list_4 = ["/this/is/the/sixth/path", "/this/is/the/seventh/path"]

    test_full

# Generated at 2022-06-13 15:52:22.630312
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ansible_collection_ref = AnsibleCollectionRef.from_fqcr('ns.coll.resources','module')

# Generated at 2022-06-13 15:52:32.392201
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    results = {}
    results['ok'] = [
        # from module
        AnsibleCollectionRef.try_parse_fqcr('test1.test2.test3', 'module'),
        # from module_utils
        AnsibleCollectionRef.try_parse_fqcr('test1.test2.test3', 'module_utils'),
        # from role
        AnsibleCollectionRef.try_parse_fqcr('test1.test2.test3', 'role'),
        # external role (not supported yet)
        AnsibleCollectionRef.try_parse_fqcr('test1.test2', 'role'),
        # from filter
        AnsibleCollectionRef.try_parse_fqcr('test1.test2.test3', 'filter'),
    ]

# Generated at 2022-06-13 15:52:44.572302
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from ansible.utils.collection_loader import AnsibleCollectionReference
    from ansible.utils.collection_loader import AnsibleCollectionRequirement
    from ansible.utils.collection_loader import AnsibleCollectionVersion
    # test an example collection (libcloud)
    def mock_method(fullname):
        if fullname == 'ansible_collections.libcloud.plugins.modules.libcloud_loadbalancer':
            return ('/tmp/ansible_collections/ansible_collections/libcloud/plugins/modules/libcloud_loadbalancer.py', True, None)
        if fullname == 'ansible_collections.libcloud.plugins.modules.libcloud_compute':
            return ('/tmp/ansible_collections/ansible_collections/libcloud/plugins/modules/libcloud_compute.py', True, None)

# Generated at 2022-06-13 15:52:54.153532
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    from ansible_collections.notstdlib.moveitallout.tests.units.mock.loader import MockModuleSpec

    # Scenario 1: no package/module code exists
    sut = _AnsibleCollectionPkgLoaderBase('notstdlib.moveitallout.plugins.test', [])
    sut._subpackage_search_paths = None
    sut._source_code_path = None
    res = sut.get_filename(sut._fullname)
    assert res is None

    # Scenario 2: package has subpackages but no code (eg, a synthetic __init__.py)
    sut = _AnsibleCollectionPkgLoaderBase('notstdlib.moveitallout.plugins.test', [])

# Generated at 2022-06-13 15:52:58.102967
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    import collections.abc
    import ansible_collections
    import ansible_collections.notarealnamespace
    import ansible_collections.test
    import ansible_collections.test.testcoll
    import ansible_collections.test.testcoll.plugins.modules
    import ansible_collections.test.testcoll.plugins.modules.test_module
    import ansible_collections.test.testcoll.plugins.modules.test_module_one
    import ansible_collections.test.testcoll.plugins.modules.test_module_two
    import ansible_collections.test.testcoll.plugins.modules.test_module_one_two
    import ansible_collections.test.testcoll.plugins.modules.test_module_two_two
    import ansible_collections.test.testcoll.plugins

# Generated at 2022-06-13 15:53:07.552038
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    class _AnsibleCollectionPkgLoaderBaseSubClass(_AnsibleCollectionPkgLoaderBase):
        def get_data(self, path):
            return super(_AnsibleCollectionPkgLoaderBaseSubClass, self).get_data(path)
    path = os.path.dirname(os.path.dirname(__file__))
    loader = _AnsibleCollectionPkgLoaderBaseSubClass('', [path])
    data = loader.get_data('/test/unit/ansible_collections/test/plugins/modules/test_ping.py')
    assert data.decode('utf-8').startswith('#!/usr/bin/python')
    # This should not fail (should not raise ValueError)

# Generated at 2022-06-13 15:53:20.370163
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # setup test
    ref = u'ns.coll.something'
    ref_type = u'action'
    # perform test
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    # assert result
    assert result.n_python_package_name == u'ansible_collections.ns.coll.plugins.action'
    assert result.n_python_collection_package_name == u'ansible_collections.ns.coll'
    assert result.fqcr == u'ns.coll.something'
    assert result.collection == u'ns.coll'
    assert result.resource == u'something'
    assert result.ref_type == u'action'
    assert result.subdirs == u''
    # setup test

# Generated at 2022-06-13 15:53:31.223876
# Unit test for constructor of class _AnsibleCollectionNSPkgLoader
def test__AnsibleCollectionNSPkgLoader():
    path_list = ['/etc/ansible/collections']
    loader = _AnsibleCollectionNSPkgLoader('ansible_collections.test_ns', path_list)
    assert loader._fullname == 'ansible_collections.test_ns'
    assert loader._split_name == ['ansible_collections', 'test_ns']
    assert loader._package_to_load == 'test_ns'
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._source_code_path == None
    if PY2:
        # Py2 iter_modules output is a generator, so convert it to a list
        assert list(loader.iter_modules(prefix='test')) == [('test_ns', True, True)]

# Generated at 2022-06-13 15:54:07.157391
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    _meta_yml_to_dict = ''

    class Ansible(object):
        @staticmethod
        def module_utils(name):
            return import_module(name)

    # Constructor of _AnsibleCollectionPkgLoader will initialize self._split_name to ['ansible_collections', 'foo', 'bar']
    _AnsibleCollectionPkgLoaderBase.__init__ = lambda obj, name, path=None: setattr(obj, '_split_name', ['ansible_collections', 'foo', 'bar'])
    _AnsibleCollectionPkgLoader.__init__ = _AnsibleCollectionPkgLoaderBase.__init__

    # load_module will load module ansible_collections.foo.bar

# Generated at 2022-06-13 15:54:18.648662
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef

# Generated at 2022-06-13 15:54:25.259623
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import tempfile
    import sys
    import os
    import shutil
    def mock_get_data(path):
        with open(path, 'rb') as fd:
            return fd.read()
    mock_loader = _AnsibleCollectionPkgLoaderBase(
        fullname='test_ansible_collections_ns.test',
        path_list=['/fake/path']
    )
    mock_loader.get_data = mock_get_data
    py_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    py_file.write('print("Hello World!")\n')
    py_file.close()

# Generated at 2022-06-13 15:54:36.454645
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # Test 1: Check if the constructor is able to parse a FQCR
    test1_input1 = 'ansible_collections.ns.coll.resource'
    test1_input2 = 'plugins.resource'
    test1_exp1 = 'ns.coll.resource'
    test1_exp2 = 'plugins.resource'
    test1 = AnsibleCollectionRef(test1_input1, None, 'resource', 'module')
    test1_mem = test1._fqcr
    assert(test1_mem == test1_exp1)

    test1_1 = AnsibleCollectionRef(test1_input2, None, 'resource', 'modules')
    test1_1_mem = test1_1._fqcr
    assert(test1_1_mem == test1_exp2)

    # Test 2: Check if

# Generated at 2022-06-13 15:54:42.299076
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    import unittest
    import sys
    import types
    from collections import namedtuple
    from ansible.utils import context_objects as co

    # BEGIN: test utility functions

    # utility function for generating a mock AnsibleCollectionConfig instance with mock methods
    def _mock_config_instance(already_loaded=None):
        m = Mock()
        m.collection_root_paths = ['/collections']
        m.collection_roots_found = True
        m.collection_roots_loaded = True
        m.already_loaded = already_loaded or ['/collections/namespace/collection']
        return m

    def _mock_collection_load_callback(collection_name, collection_path):
        call_args = getattr(_mock_collection_load_callback, 'call_args', None)

# Generated at 2022-06-13 15:54:44.332423
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1', 'mymodule', 'module')
    assert ref.__repr__() == "AnsibleCollectionRef(collection='namespace.collection', subdirs='subdir1', resource='mymodule')"



# Generated at 2022-06-13 15:54:55.657903
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    """test_ansible_collections_loader.py:test__AnsibleCollectionPkgLoaderBase_load_module"""
    import ansible_collections
    parent_package_name = ansible_collections.__name__
    package_to_load = 'somens'
    fullname = f'{parent_package_name}.{package_to_load}'
    path_list = [
        os.path.join(ansible_collections.__path__[0], package_to_load),
        os.path.join(ansible_collections.__path__[1], package_to_load)
    ]
    loader = _AnsibleCollectionPkgLoaderBase(fullname=fullname, path_list=path_list)
    loader.load_module(fullname)
    assert fullname in sys.modules

# Generated at 2022-06-13 15:54:56.613710
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    pass


# Generated at 2022-06-13 15:55:03.972844
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    _AnsibleInternalRedirectLoader('ansible.module_utils.subprocess', None)
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.builtin.module_utils.subprocess', None)
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.builtin.plugins.module_utils.subprocess', None)
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.builtin.plugins.uri.subprocess', None)
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader(None, None)

### Imp-facing entry points ###

# Generated at 2022-06-13 15:55:13.360180
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    import tempfile
    import shutil

    # create test collection directory tree
    # we need to figure out the path ourselves
    collection_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    fixture_dir = os.path.join(collection_dir, 'test_fixtures')
    tmp_dir = tempfile.mkdtemp(prefix='test_fixtures')
    test_fixture = 'test_lookup_plugin'
    # we expect the directory to be under 'test_fixtures' and to be named 'test_lookup_plugin'
    test_dir = os.path.join(tmp_dir, test_fixture)

# Generated at 2022-06-13 15:55:49.608545
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    loader = _AnsibleCollectionPkgLoaderBase("ansible_collections.some.ns", path_list=["/tmp"])
    loader._subpackage_search_paths = ["/tmp/some/ns"]
    loader._source_code_path = "/tmp/some/ns/a.py"
    loader._decoded_source = "print('hello world')"
    loader._compiled_code = compile("print('hello world')", "<string>", "exec")
    module = loader.load_module("ansible_collections.some.ns")
    assert isinstance(module, types.ModuleType)
    assert module.__name__ == "ansible_collections.some.ns"


# Generated at 2022-06-13 15:56:00.569458
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from collections import namedtuple
    from ansible import constants
    from ansible.utils.collection_loader import _meta_yml_to_dict
    from ansible.utils.collection_loader import _get_collection_metadata
    from ansible.utils.collection_loader import _AnsibleInternalRedirectLoader
    _meta_yml = 'plugin_routing:'
    _meta_yml += '  action_plugin:'
    _meta_yml += '    some_thing:'
    _meta_yml += '      redirect: not.a.real.package'
    _meta_yml = _meta_yml_to_dict(_meta_yml, ('namespace', 'collection', 'meta/runtime.yml'))
    builtin_meta = _get_collection_metadata('ansible.builtin')
    routing_entry

# Generated at 2022-06-13 15:56:09.216759
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    import os

    # Setup
    pwd = os.getcwd()
    os.chdir('test/units/module_utils/ansible_test/_data/cli_playbook_working_dir')
    collection_config = AnsibleCollectionConfig()
    collection_config._configured_collection_paths = []
    collection_config._playbook_paths = ['collections']
    collection_config.collection_finder._remove()

    # Test
    try:
        result = collection_config.collection_finder.find_module('test_internal_collection_loader.test_module')
        assert result.filename == os.sep.join(['collections', 'test', 'test_internal_collection_loader.py'])
    except ImportError:
        assert False

    # Tear Down
    os.chdir(pwd)


# Generated at 2022-06-13 15:56:19.381813
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    assert "_AnsibleCollectionPkgLoaderBase(path=None)" == _AnsibleCollectionPkgLoaderBase(fullname='_AnsibleCollectionPkgLoaderBase').__repr__()
    assert "_AnsibleCollectionPkgLoaderBase(path='/tmp')" == _AnsibleCollectionPkgLoaderBase(fullname='_AnsibleCollections',path_list=['/tmp']).__repr__()
    assert "_AnsibleCollectionPkgLoaderBase(path='/tmp')" == _AnsibleCollectionPkgLoaderBase(fullname='_AnsibleCollections',path_list=['/tmp','/tmp']).__repr__()

# Generated at 2022-06-13 15:56:26.572752
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    reload(ansible.utils.collection_loader)
    reload(ansible.utils.module_docs_fragments)
    _AnsibleInternalRedirectLoader = ansible.utils.collection_loader._AnsibleInternalRedirectLoader

    path_list = []
    fullname = 'ansible.builtin.copy'
    _AnsibleInternalRedirectLoader = _AnsibleInternalRedirectLoader(fullname, path_list)
    _AnsibleInternalRedirectLoader.load_module(fullname)


# this loader handles plugins in the 'lib/ansible/plugins' namespace, which include lookup and connection plugins

# Generated at 2022-06-13 15:56:34.134383
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    """Unit test for method `__repr__` of class `AnsibleCollectionRef`."""
    ac = AnsibleCollectionRef(
        collection_name='ansible.builtin',
        subdirs='action',
        resource='ping',
        ref_type='plugin_type_specific'
    )
    assert repr(ac) == "AnsibleCollectionRef(collection='ansible.builtin', subdirs='action', resource='ping')"



# Generated at 2022-06-13 15:56:36.503790
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    collection_ref = AnsibleCollectionRef('a', 'b', 'c', 'd')
    assert collection_ref.__repr__() == 'AnsibleCollectionRef(collection=\'a\', subdirs=\'b\', resource=\'c\')'

# Generated at 2022-06-13 15:56:44.813050
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock, patch
    from ansible_collections.community.general.plugins.module_utils.facts import _ansible_collection_finder

    class DummyLoader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, *args, **kwargs):
            self.object = args[0]
            super(DummyLoader, self).__init__(self.object)
            self.data = kwargs

        def get_filename(self, fullname):
            return self.data['filename']


# Generated at 2022-06-13 15:56:49.080926
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    # Loader should not be called for non-ansible imports
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('not.ansible.module', '.')

    # Loader not interested for ansible imports without a corresponding redirect entry
    with pytest.raises(ImportError):
        _AnsibleInternalRedirectLoader('ansible.module', '.')

# TODO: fix this warning
warnings.warn('ansible.utils.collection_loader.get_collection_path is deprecated, please use '
              'ansible.utils.collection_loader.get_collections_paths', AnsibleDeprecationWarning)


# Generated at 2022-06-13 15:56:50.559591
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # TODO To be implemented
    pass

# Generated at 2022-06-13 15:57:29.361730
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    t = AnsibleCollectionRef.from_fqcr('ns.coll.subdir.sample', 'module')

    assert(t.collection == 'ns.coll')
    assert(t.subdirs == 'subdir')
    assert(t.resource == 'sample')
    assert(t.ref_type == 'module')
    assert(t.n_python_package_name == 'ansible_collections.ns.coll.plugins.subdir.module')
    assert(t.n_python_collection_package_name == 'ansible_collections.ns.coll')
    assert(t.fqcr == 'ns.coll.subdir.sample')


# Generated at 2022-06-13 15:57:35.581332
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    # Tests of method is_valid_fqcr:

    # Tests against strings that should be determined to be invalid collection names/references:

    # verify leading/trailing whitespace is ignored
    assert not AnsibleCollectionRef.is_valid_fqcr(' foo.bar ')

    # verify we don't allow empty strings
    assert not AnsibleCollectionRef.is_valid_fqcr('')

    # verify we don't allow strings without at least two components
    assert not AnsibleCollectionRef.is_valid_fqcr('foo')

    # verify we don't allow strings with only two components
    assert not AnsibleCollectionRef.is_valid_fqcr('foo.bar')

    # verify we require at least one dot as separator

# Generated at 2022-06-13 15:57:43.278153
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # make everything happy
    _meta_yml_to_dict = lambda x, y: {}
    AnsibleCollectionConfig.on_collection_load = SimpleNamespace()
    AnsibleCollectionConfig.on_collection_load.fire = lambda x, y: None
    # Test with empty meta
    module = _AnsibleCollectionPkgLoader(['ansible.collections', 'test', 'collection']).load_module(
        'ansible.collections.test.collection'
    )
    assert module.__path__[0] == '/nonexistent_dir'
    assert module.__file__ == '/nonexistent_dir/__synthetic__'
    assert module.__loader__ == '<ansible.collections.test.collection>'
    assert module._collection_meta == {}
    # Test with non-empty meta
   

# Generated at 2022-06-13 15:57:48.082320
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    tests = [
        ('foo.bar.baz', 'module', 'foo.bar.plugins.module.baz'),
        ('foo.bar.a/b.baz', 'module', 'foo.bar.plugins.a/b.module.baz'),
        ('foo.bar.a/b.c/d.baz', 'module', 'foo.bar.plugins.a/b.c/d.module.baz'),
        ('foo.bar.baz', 'role', 'foo.bar.roles.baz'),
        ('foo.bar.baz', 'playbook', 'foo.bar.playbooks.baz'),
    ]
    for collection, ref_type, python_package in tests:
        collection = AnsibleCollectionRef.from_fqcr(collection, ref_type)
        assert collection.n_python

# Generated at 2022-06-13 15:57:56.866300
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    # Test with a package
    package_path = 'ansible_collections.geerlingguy.pip'
    package_loader = AnsibleCollectionPackageLoader(package_path)
    code_obj = package_loader.get_code(package_path)
    assert code_obj is not None

    # Test with a module
    module_path = 'ansible_collections.geerlingguy.pip.library'
    source_code = package_loader.get_source(module_path)
    assert source_code == ''
    code_obj = package_loader.get_code(module_path)
    assert code_obj is not None

    # Test with a module which does not exist
    module_path = 'ansible_collections.geerlingguy.pip.not_exist'

# Generated at 2022-06-13 15:58:01.699218
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.ns.module')
    assert str(loader) == "_AnsibleCollectionPkgLoaderBase(path=['module'])"
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.ns.package')
    assert str(loader) == "_AnsibleCollectionPkgLoaderBase(path=['package'])"


# TODO: remove this base once all collections have been ported to use a real one

# Generated at 2022-06-13 15:58:12.347497
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr(u'ansible.builtin.testmod', u'module')
    assert AnsibleCollectionRef.from_fqcr(u'another.collection.test', u'role')
    assert AnsibleCollectionRef.from_fqcr(u'another.collection.test', u'playbook')
    assert AnsibleCollectionRef.from_fqcr(u'another.collection.subdir.test', u'module')
    assert AnsibleCollectionRef.from_fqcr(u'another.collection.subdir.subdir2.test', u'cache')

# Generated at 2022-06-13 15:58:14.458984
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # assume we have a valid collection for the purposes of testing
    ref = AnsibleCollectionRef('ns.coll', '', 'resource', 'modules')
    assert ref.collection == 'ns.coll'


# Generated at 2022-06-13 15:58:23.860401
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    with pytest.raises(ImportError, match='not interested'):
        _AnsibleInternalRedirectLoader("foo.bar", [])
    loader = _AnsibleInternalRedirectLoader("ansible.module_utils.basic", [])
    assert loader._redirect == 'ansible.module_utils.common.basic'
    with pytest.raises(ValueError, match='no redirect found for'):
        loader.load_module("ansible.module_utils.basic")

# A utility class for the ansible_collections namespace package's path_hook

# Generated at 2022-06-13 15:58:34.569010
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    acr = AnsibleCollectionRef
    assert acr.legacy_plugin_dir_to_plugin_type(u'action_plugins') == u'action'
    assert acr.legacy_plugin_dir_to_plugin_type(u'become_plugins') == u'become'
    assert acr.legacy_plugin_dir_to_plugin_type(u'cache_plugins') == u'cache'
    assert acr.legacy_plugin_dir_to_plugin_type(u'callback_plugins') == u'callback'
    assert acr.legacy_plugin_dir_to_plugin_type(u'cliconf_plugins') == u'cliconf'
    assert acr.legacy_plugin_dir_to_plugin_type(u'connection_plugins') == u'connection'
    assert acr