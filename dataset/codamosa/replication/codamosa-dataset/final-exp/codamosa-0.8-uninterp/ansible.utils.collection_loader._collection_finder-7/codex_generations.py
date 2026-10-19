

# Generated at 2022-06-13 15:50:25.981702
# Unit test for constructor of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase():
    path_list = ["/etc/ansible"]
    acp = _AnsibleCollectionPkgLoaderBase("ansible_collections.example", path_list)
    assert acp._fullname == "ansible_collections.example"
    assert acp._split_name == ["ansible_collections", "example"]
    assert acp._rpart_name[0] == "ansible_collections"
    assert acp._rpart_name[1] == "."
    assert acp._rpart_name[2] == "example"
    assert acp._parent_package_name == "ansible_collections"
    assert acp._package_to_load == "example"
    assert acp._source_code_path is None
    assert acp._decoded_source is None
    assert acp._compiled_

# Generated at 2022-06-13 15:50:30.076906
# Unit test for constructor of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader():
    loader = _AnsibleCollectionPkgLoader(None, 'ansible_collections.Foo.Bar.Baz')
    loader._validate_final()
    assert loader._split_name == ['ansible_collections', 'Foo', 'Bar', 'Baz']
    assert loader._package_to_load == 'Bar'
    assert loader._candidate_paths == [os.path.join(p, 'Bar') for p in AnsibleCollectionConfig.get_collection_paths()]


# Generated at 2022-06-13 15:50:32.940287
# Unit test for constructor of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoader('cked', None, None)
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoader('cked.collections', None, None)
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoader('cked.collections.cked.cked.cked', None, None)


# Generated at 2022-06-13 15:50:33.824353
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    assert False, 'Not implemented'



# Generated at 2022-06-13 15:50:39.279702
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    fullname = 'package'
    path_list=['ansible_collections']
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    assert repr(loader) == '_AnsibleCollectionPkgLoaderBase(path=None)'
    fullname = 'ansible_collections.package'
    path_list=['ansible_collections']
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    assert repr(loader) == '_AnsibleCollectionPkgLoaderBase(path=None)'



# Generated at 2022-06-13 15:50:46.256651
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    loader = _AnsibleCollectionPkgLoader(None, 'ansible_collections.test_collection.a_plugin', None)

    loader.get_source(loader._fullname)

    loader.load_module(loader._fullname)


# test the load_module method of the ancestors of _AnsibleCollectionPkgLoader
test__AnsibleCollectionPkgLoader_load_module()

# The loader class for the custom namespace package support
NAMESPACE_PACKAGE_LOADER_CLASS = _AnsibleCollectionNSPkgLoader



# Generated at 2022-06-13 15:50:48.810445
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # TODO: verify various cases
    pass



# Generated at 2022-06-13 15:50:53.430451
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    l = _AnsibleCollectionPkgLoaderBase('my.package', path_list=['/my/path'])
    assert repr(l) == '_AnsibleCollectionPkgLoaderBase(path=/my/path/package)'
    l = _AnsibleCollectionPkgLoaderBase('my.package', path_list=['/my/path'])
    l._subpackage_search_paths = None
    assert repr(l) == '_AnsibleCollectionPkgLoaderBase(path=/my/path/package.py)'



# Generated at 2022-06-13 15:51:03.476482
# Unit test for constructor of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase():
    class test_AnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            assert self._fullname == 'ansible.test_ns'
            assert self._split_name == ['ansible', 'test_ns']
            assert self._rpart_name == ('ansible', '.', 'test_ns')
            assert self._parent_package_name == 'ansible'
            assert self._package_to_load == 'test_ns'


# Generated at 2022-06-13 15:51:15.737786
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    invalid_collections = [
        '',
        '.foo',
        'foo.',
        'foo',
        'foo.bar.baz.quux.quaz',
        'foo.bar.baz.quux.quaz.quox',
        'foo-bar.baz.quux',
        'foo.bar-baz.quux',
        'foo.bar.baz-quux',
    ]

    for invalid_collection in invalid_collections:
        with pytest.raises(ValueError):
            AnsibleCollectionRef(invalid_collection, None, 'mymodule', 'module')

    valid_collections = [
        ('foo.bar', 'mymodule', 'module', 'foo.bar.mymodule'),
    ]

    for valid_collection in valid_collections:
        assert Ansible

# Generated at 2022-06-13 15:51:50.940879
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    data = [
        ('one', False),
        ('one.two', False),
        ('one.two.three', True),
        ('one.two.three.four', True),
        ('one.two.three.four.five', True),
        ('one.two.three.four.five.six', True),
        ('one.two.three.four.five.six.seven', True),
        ('one.two.three.four/five', False),
        ('one/two.three.four', False),
        ('one.two.three.four/five', False),
        ('one.two.three.four.five/', False),
        ('one.two.three.four/five.six', False),
    ]

    for (collection_name, expected) in data:
        assert AnsibleCollectionRef.is_valid_

# Generated at 2022-06-13 15:52:03.784653
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    from shutil import rmtree
    from tempfile import gettempdir
    # TEMP_DIR will be used to create a fake collection for testing purposes
    TEMP_DIR = os.path.join(gettempdir(), 'collection_loader_test')
    # TEMP_FILE will be used for storing a fake module file
    TEMP_FILE = os.path.join(TEMP_DIR, 'ansible_collections', 'fake_namespace', 'fake_collection', 'tasks', 'main.py')
    # Create the fake collection folder
    os.makedirs(os.path.join(TEMP_DIR, 'ansible_collections', 'fake_namespace', 'fake_collection', 'tasks'))
    # Create the fake module file
    with open(TEMP_FILE, 'w') as f:
        f.write

# Generated at 2022-06-13 15:52:11.624274
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    from packaging.version import Version
    from pkg_resources import parse_version
    tests = []

    # Test 1. path=None
    try:
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection.test_ns')
        loader.get_data(None)
    except ValueError:
        tests.append(True)
    else:
        tests.append(False)
    # Test 2. path='/path/to/mod.py'
    try:
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection.test_ns')
        loader.get_data('/path/to/mod.py')
    except ValueError:
        tests.append(True)
    else:
        tests.append(False)
    # Test 3. path

# Generated at 2022-06-13 15:52:18.915085
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # filename is not set
    acplb_no_filename = _AnsibleCollectionPkgLoaderBase('ansible_collections.my.package')
    # filename set to fake file
    acplb_filename = _AnsibleCollectionPkgLoaderBase('ansible_collections.my.package')
    acplb_filename._source_code_path = '/path/to/fake/file.py'
    # filename set to empty string
    acplb_filename_empty = _AnsibleCollectionPkgLoaderBase('ansible_collections.my.package')
    acplb_filename_empty._source_code_path = ''

    # setup test parameters
    names, paths, no_paths = setup_parameters()

    # Test empty filename and not a package

# Generated at 2022-06-13 15:52:29.594820
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    assert AnsibleCollectionRef.is_valid_fqcr(u'ns.coll.resource') == True
    assert AnsibleCollectionRef.is_valid_fqcr(u'ns.coll.subdir.resource') == True
    assert AnsibleCollectionRef.is_valid_fqcr(u'ns.coll.subdir.subdir.resource') == True
    assert AnsibleCollectionRef.is_valid_fqcr(u'resource') == False
    assert AnsibleCollectionRef.is_valid_fqcr(u'ns.coll.subdir.subdir.res#source') == False
    assert AnsibleCollectionRef.is_valid_fqcr(u'ns.coll.subdir.subdir..resource') == False

# Generated at 2022-06-13 15:52:41.368229
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    class test_module(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass
        def _get_candidate_paths(self, path_list):
            return path_list
        def _get_subpackage_search_paths(self, candidate_paths):
            return candidate_paths
        def _validate_final(self):
            pass
    script_path = os.path.dirname(os.path.realpath(__file__))
    path_list = [os.path.join(script_path, 'test/test_module.py')]
    test_loader = test_module('test_module', path_list)
    test_loader.get_source('test_module')



# Generated at 2022-06-13 15:52:49.826175
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # from_fqcr needs a ref_type to parse
    acr = AnsibleCollectionRef.from_fqcr(u"foo.bar.baz", u"module")
    assert acr.subdirs == u""
    assert acr.fqcr == u"foo.bar.baz"
    assert acr.collection == u"foo.bar"
    assert acr.resource == u"baz"
    assert acr.ref_type == u"module"
    assert acr.n_python_package_name == u"ansible_collections.foo.bar.plugins.module"
    assert acr.n_python_collection_package_name == u"ansible_collections.foo.bar"

    # with a subdir

# Generated at 2022-06-13 15:53:00.402955
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    import sys
    import types
    import unittest
    import unittest.mock as mock
    def _get_results(path_list):
        builtin_meta = {
            'import_redirection': {
                'ansible.module_utils.selinux': {'redirect': 'ansible.builtin.selinux'},
            }
        }
        with mock.patch.object(sys, 'modules', {}):
            with mock.patch.object(ansible.utils.collection_loader.builtin, '_get_collection_metadata', return_value=builtin_meta), \
                    mock.patch.object(ansible.utils.collection_loader, 'import_module', return_value=ansible.builtin.selinux) as mock_import_module:
                loader = ansible.utils.collection_

# Generated at 2022-06-13 15:53:08.747864
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:53:21.318044
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    """Test find_module method of class _AnsibleCollectionFinder"""
    def _find_module(name, path=None):
        """Test _AnsibleCollectionFinder.find_module()"""
        finder = _AnsibleCollectionFinder()
        return finder.find_module(name, path)

    assert _find_module('ansible')
    assert _find_module('ansible.module_utils.basic')
    assert _find_module('ansible_collections', ['/tmp/collections'])
    assert _find_module('ansible_collections.ansible')
    assert _find_module('ansible_collections.ansible.common')
    assert _find_module('ansible_collections.ansible.common.my_module')

# Generated at 2022-06-13 15:54:19.680094
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
  assert AnsibleCollectionRef.from_fqcr(ref="ansible.builtin.file", ref_type="module") == AnsibleCollectionRef(collection_name='ansible.builtin', subdirs='', resource='file', ref_type='module')
  assert AnsibleCollectionRef.from_fqcr(ref="ansible.builtin.copy", ref_type="module") == AnsibleCollectionRef(collection_name='ansible.builtin', subdirs='', resource='copy', ref_type='module')
  assert AnsibleCollectionRef.from_fqcr(ref="ansible.builtin.win_copy", ref_type="module") == AnsibleCollectionRef(collection_name='ansible.builtin', subdirs='win', resource='copy', ref_type='module')

# Generated at 2022-06-13 15:54:23.752356
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    import sys
    import six
    loader=_AnsibleCollectionPkgLoaderBase(None, None)
    expected = '_AnsibleCollectionPkgLoaderBase(path=None)'
    actual = loader.__repr__()
    assert actual == expected



# Generated at 2022-06-13 15:54:32.643070
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    contents = [os.path.join('', 'ansible_collections', 'ns_coll')]
    for content in contents:
        path_list = [content]
        finder = _AnsiblePathHookFinder(os.path.join('', 'ansible_collections'), None).find_module('ns_coll', path_list)
        loader = finder.load_module('ns_coll')
        assert loader._fullname == 'ns_coll'
        assert loader.get_filename('ns_coll') == os.path.join('', 'ansible_collections', 'ns_coll', '__synthetic__')

    contents = [os.path.join('', 'ansible_collections', 'ns_coll', 'foo')]
    for content in contents:
        path_list = [content]
        finder

# Generated at 2022-06-13 15:54:40.165155
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    if not PY3:
        return (True, 'skipping ansible.module_utils.six.PY3 check')

    # tests:
    # pkg vs module (source on disk vs not)
    # byte string vs unicode source
    # empty package init
    # empty package init vs directory vs missing file
    # code w/o __file__ (module w/o path)

    from ansible.module_utils import six
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common.collections import _AnsibleCollectionPkgLoaderBase
    from ansible.module_utils.common.collections import FileFinder


# Generated at 2022-06-13 15:54:43.100006
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    suite = unittest.TestSuite()
    suite.addTest(Test__AnsibleCollectionPkgLoaderBase_get_source('test_get_source'))
    return suite


# Generated at 2022-06-13 15:54:53.697005
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    import copy
    import sys
    import types
    import collections

    mock_sys_modules = dict(sys.modules)

    class MockImportModule:
        def __init__(self):
            self.args = None
            self.kwargs = None

        def __call__(self, *args, **kwargs):
            self.args = copy.deepcopy(args)
            self.kwargs = copy.deepcopy(kwargs)
            return args[0]

        def reset(self):
            self.args = None
            self.kwargs = None

    mock_import_module = MockImportModule()

    class MockRuntimeYML:
        def __init__(self):
            self.yml = None


# Generated at 2022-06-13 15:55:02.371775
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    try:
        # We need an exception for this test
        from ansible_collections.ansible_collections import exception
    except:
        print("SKIP: ansible requires exception from ansible_collections.ansible_collections")
        return
    try:
        # We need a  for this test
        from ansible_collections.ansible_collections import collection_loader
        from ansible_collections.ansible_collections import collection_finder
    except:
        print("SKIP: ansible requires collection_loader and collection_finder from ansible_collections.ansible_collections")
        return

    pattern = None
    namespace = 'ansible_collections'
    finder = collection_finder.AnsibleCollectionFinder(namespace, pattern)
    loader = collection_loader.AnsibleCollectionLoader([])

# Generated at 2022-06-13 15:55:08.683550
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    from ansible_collections.foo.bar.plugins.module_utils import bar_utils
    from ansible_collections.foo.bar.plugins.modules import bar_module
    from ansible_collections.foo.bar.plugins.test.modules import test_bar_module

    # test basic ref
    ref = AnsibleCollectionRef.from_fqcr('foo.bar.resource', 'module')
    assert ref.n_python_collection_package_name == 'ansible_collections.foo.bar'
    assert ref.n_python_package_name == 'ansible_collections.foo.bar.plugins.modules.resource'
    assert ref.fqcr == 'foo.bar.resource'

    # test python package
    assert ref.n_python_collection_package_name == 'ansible_collections.foo.bar'

# Generated at 2022-06-13 15:55:10.688798
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    leg_dir_name = 'action_plugins'
    plugin_type = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(leg_dir_name)
    assert plugin_type == 'action'


# Generated at 2022-06-13 15:55:14.550576
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    tester = _AnsibleCollectionPkgLoaderBase('ansible_collections.ns.package.module')
    assert tester.is_package('ansible_collections.ns.package') is True

# Generated at 2022-06-13 15:55:46.653540
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    loader = _AnsibleInternalRedirectLoader('ansible.plugins.action.archive', ["/path/to/archive"])

    assert loader is not None, 'Loader is None.'

#
# Internal functions including helper methods for _AnsibleCollectionLoader
#


# Generated at 2022-06-13 15:55:51.113572
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('become_plugins') == 'become'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cache_plugins') == 'cache'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('callback_plugins') == 'callback'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('cliconf_plugins') == 'cliconf'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('connection_plugins') == 'connection'

    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type

# Generated at 2022-06-13 15:55:59.519563
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    load_module = _AnsibleCollectionPkgLoader(fullname='synthetic.package.name', loader=object).load_module
    # Call load_module and check that it is raising ImportError
    # since there is no attribute '_meta_yml_to_dict' in ansible.utils.collection_loader
    try:
        load_module(fullname='synthetic.package.name')
    except ImportError:
        pass
    except Exception as ex:
        raise AssertionError(
            'load_module raised wrong exception type. Expected "ImportError", got "{0}"'.format(type(ex).__name__)
        )



# Generated at 2022-06-13 15:56:07.939952
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    # Testing method ansible_collections.ansible.builtin.plugins.action.from_fqcr of class AnsibleCollectionRef
    # test with dummy ref_type and ref that are valid
    ref_type = 'module'
    ref = 'ansible.builtin.git'
    ansible_collections.ansible.builtin.plugins.action.AnsibleCollectionRef.from_fqcr(ref, ref_type)
    # test with dummy ref_type and ref that are invalid
    ref_type = 'module'
    ref = 'ansible.builtin.'
    with pytest.raises(ValueError):
        ansible_collections.ansible.builtin.plugins.action.AnsibleCollectionRef.from_fqcr(ref, ref_type)
    # test with dummy ref_type and ref that are invalid

# Generated at 2022-06-13 15:56:19.695433
# Unit test for constructor of class AnsibleCollectionRef

# Generated at 2022-06-13 15:56:28.633346
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    ref = AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'module')
    assert ref.fqcr == 'ns.coll.resource'
    assert ref.n_python_package_name == 'ansible_collections.ns.coll.plugins.module'
    assert ref.collection == 'ns.coll'
    assert ref.ref_type == 'module'
    assert ref.resource == 'resource'
    assert ref.subdirs == ''

    ref = AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'role')
    assert ref.fqcr == 'ns.coll.resource'
    assert ref.n_python_package_name == 'ansible_collections.ns.coll.roles.resource'
    assert ref.collection == 'ns.coll'

# Generated at 2022-06-13 15:56:35.359788
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    path = './data/ansible_collections/xnetwork/cisco/plugins/modules'
    pkg = _find_pkg_relative(path=path, fullname="ansible_collections.xnetwork.cisco")
    assert(pkg is not None)
    data = pkg.get_data('library/eos_vlan.py')
    assert(data is not None)
    assert('ANSIBLE_METADATA' in data)


# Generated at 2022-06-13 15:56:43.404131
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    collection_ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'resource_name', 'module')
    assert collection_ref.is_valid_fqcr('namespace.collection.subdir1.subdir2.resource_name', 'module')
    assert not collection_ref.is_valid_fqcr('namespace.collection.subdir1.subdir2.resource_name', 'role')
    assert not collection_ref.is_valid_fqcr('namespace.collection.subdir1.subdir2.resource_name')
    assert not collection_ref.is_valid_fqcr('namespace.collection.resource_name', 'module')
    assert collection_ref.is_valid_fqcr('namespace.collection.resource_name', 'playbook')
# END - Unit test for

# Generated at 2022-06-13 15:56:46.325748
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('lookup_plugins') == 'lookup'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'


# Generated at 2022-06-13 15:56:47.807533
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    path_list = ['foo/bar/baz']
    loader = _AnsibleInternalRedirectLoader('ansible.builtin.module', path_list)
    assert loader._redirect == 'ansible.modules.module'



# Generated at 2022-06-13 15:57:18.884593
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    # Ensure that only source code (i.e. not package) is loaded.
    loader = _AnsibleCollectionPkgLoaderBase(fullname='foo.bar')
    loader._source_code_path = "/path/to/source_code.py"
    assert loader.get_code(fullname='foo.bar') is not None
    loader._subpackage_search_paths = '/path/to/package'
    assert loader.get_code(fullname='foo.bar') is None



# Generated at 2022-06-13 15:57:25.234977
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    for base_path in (u'.', u'..'):
        for path in (u'', u'/', u'..'):
            for package_name in (u'__init__', u'ns', u'__init__.py', u'ns.py'):
                for fullname in (u'c.collection.ns.sub1', u'ns', u'__init__'):
                    for subpackage_path in (None, u'asdf', u'..', u'/asdf'):
                        for filename in (None, u'', u'asdf', '__init__.py'):
                            ldr = _AnsibleCollectionPkgLoaderBase(fullname, [base_path])
                            ldr._package_to_load = package_name
                            ldr._subpackage_search_paths = sub

# Generated at 2022-06-13 15:57:31.547743
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
  from types import ModuleType
  import os
  mock_factory = MockFactory()
  test_paths = [['/tmp/collection'], ['/tmp/collection', '/tmp/collection_other']]
  for test_path in test_paths:
    for exists_return in [True, False]:
      with mock_factory.create_scope(os, 'path', exists=lambda p: p == test_path[0] if exists_return else False):
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.foo', test_path)
        result = loader.is_package('ansible_collections.foo')

# Generated at 2022-06-13 15:57:39.231775
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    p = Path(__file__).parent
    pkg_name = 'namespace1'
    pkg_path = p.joinpath(pkg_name)
    loader = _AnsibleCollectionPkgLoaderBase(pkg_name, [pkg_path])
    # module
    module_name = 'module1.py'
    result = loader.get_data(path.join(pkg_path, module_name))
    print('result: {0}'.format(result))
    # package
    pkg_name_2 = 'package1'
    pkg_path_2 = p.joinpath(pkg_name_2)
    loader = _AnsibleCollectionPkgLoaderBase(pkg_name_2, [pkg_path_2])

# Generated at 2022-06-13 15:57:49.394215
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    import collections
    from ansible_collections.theforeman.foreman.plugins.module_utils.foreman_helper import _AnsibleCollectionPkgLoaderBase
    path = dirname(collections.__file__)
    loader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.theforeman.foreman', path_list=[path])
    assert loader.get_source(fullname='ansible_collections.theforeman.foreman')
    assert loader.get_source(fullname='ansible_collections.theforeman.foreman') == loader.get_source(fullname='ansible_collections.theforeman.foreman')

# Generated at 2022-06-13 15:57:54.291633
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():
    import unittest

    TEST_DATA = (
        ('ns.coll.resource', True),
        ('ns.coll.subdir1.resource', True),
        ('ns.coll.resource.file', False),
        ('ns.coll.resource.file.yml', False),
        ('ns.coll.resource.yml', True),
        ('ns.coll.rolename', True),
        ('ns.coll.playbookname.yml', True),
        ('ns.coll.playbookname.yaml', True),
        ('ns.coll.playbookname.yml.somestuff', False),
    )


# Generated at 2022-06-13 15:57:56.205886
# Unit test for constructor of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder():
    assert isinstance(_AnsibleCollectionFinder(), _AnsibleCollectionFinder)



# Generated at 2022-06-13 15:58:00.505933
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    import json
    kwargs = '{"path_list": ["/Users/aenster/Documents/ansible/collection_layout/ansible_collections/somens/somen_2"], "fullname": "ansible_collections.somens.somen_2"}'
    j = json.loads(kwargs)
    l = _AnsibleCollectionPkgLoaderBase(**j)
    # This test always fails because function is_package doesn't return anything.
    assert False

# Generated at 2022-06-13 15:58:11.771150
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    # pylint: disable=redefined-outer-name
    def assertEqual(value, expected):
        if value != expected:
            raise AssertionError('value: {0} did not match expected: {1}'.format(to_native(value), to_native(expected)))

    # empty paths are fine, they'll be filled in later
    ref = AnsibleCollectionRef(collection_name=u'ns.coll', subdirs=u'subdir1', resource=u'resource1', ref_type=u'module')
    assertEqual(ref.collection, 'ns.coll')
    assertEqual(ref.subdirs, 'subdir1')
    assertEqual(ref.resource, 'resource1')
    assertEqual(ref.ref_type, 'module')


# Generated at 2022-06-13 15:58:13.817267
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    acp = _AnsibleCollectionPkgLoader(None, None, None)
    assert acp.load_module("ansible_collections.ns1.package1") == None