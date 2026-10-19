

# Generated at 2022-06-13 15:50:09.135748
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    # Create an instance of _AnsibleCollectionPkgLoaderBase
    obj = _AnsibleCollectionPkgLoaderBase('foo')

    # TODO: put more tests here
    assert True



# Generated at 2022-06-13 15:50:14.403110
# Unit test for constructor of class _AnsibleCollectionNSPkgLoader
def test__AnsibleCollectionNSPkgLoader():
    path = ["/foo/bar"]
    loader = _AnsibleCollectionNSPkgLoader("ansible_collections.abc", path)
    assert loader._package_to_load == "abc"
    assert loader._candidate_paths == ["/foo/bar/abc"]
    # test with None path
    loader = _AnsibleCollectionNSPkgLoader("ansible_collections.abc", None)
    assert loader._package_to_load == "abc"
    assert loader._candidate_paths == []
    # test with empty path
    loader = _AnsibleCollectionNSPkgLoader("ansible_collections.abc", [])
    assert loader._package_to_load == "abc"
    assert loader._candidate_paths == []


# Implements Ansible's custom namespace package support.
# The ansible

# Generated at 2022-06-13 15:50:22.750773
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    class Test_AnsibleCollectionPkgLoaderBase(UnitTestCase):
        def setUp(self):
            self.loader = _AnsibleCollectionPkgLoaderBase('dummy.module')

        def test_get_code_returns_code_from_code_file(self):
            self.loader._source_code_path = os.path.join(CODE_DATA_DIR, 'example_module.py')
            self.assertIsNotNone(self.loader.get_code('dummy.module'))

        def test_get_code_returns_None_when_no_code_file_present(self):
            self.loader._source_code_path = None
            self.assertIsNone(self.loader.get_code('dummy.module'))

    runner = TestLoader()

# Generated at 2022-06-13 15:50:35.052512
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    from ansible_collections.ansible.mazzy.plugins.modules.cmd_test import CmdTest
    from ansible_collections.ansible.mazzy.plugins.modules.cmd_test import ModuleUtils
    class Tmp_AnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, fullname, path_list=None):
            import os
            self._package_to_load = os.path.dirname(CmdTest.__file__)
            super(Tmp_AnsibleCollectionPkgLoaderBase, self).__init__(fullname, path_list)

    loader = Tmp_AnsibleCollectionPkgLoaderBase("ansible_collections.ansible.mazzy.plugins.modules")

# Generated at 2022-06-13 15:50:43.217021
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').fqcr == 'ns.coll.resource'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.sr1.resource', 'module').fqcr == 'ns.coll.sr1.resource'

    assert AnsibleCollectionRef.from_fqcr('ns.coll.resource', 'module').fqcr == 'ns.coll.resource'
    assert AnsibleCollectionRef.from_fqcr('ns.coll.sr1.resource', 'module').fqcr == 'ns.coll.sr1.resource'

    assert AnsibleCollectionRef.from_fqcr('ns.coll.playbook', 'playbook').fqcr == 'ns.coll.playbook'

# Generated at 2022-06-13 15:50:51.452204
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    foo_collection_path = '/foo/collection/init'
    source_code = "from __future__ import print_function\nprint('Hello World !')"
    source_file = tempfile.NamedTemporaryFile('w', dir=foo_collection_path)
    source_file.write(source_code)
    source_file.flush()

    loader_instance = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.foo.init', path_list=['/'])
    loader_instance._source_code_path = os.path.join(foo_collection_path, source_file.name)

    code_object = loader_instance.get_code('ansible_collections.foo.init')
    assert isinstance(code_object, types.CodeType)

# Generated at 2022-06-13 15:50:59.813004
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    import os
    import sys
    import tempfile
    import unittest

    class TestCase1(unittest.TestCase):
        def setUp(self):
            self.test_content = 'DEADBEEF'
            self.test_path = os.path.join(tempfile.gettempdir(), 'ansible_test.tmp')
            self.test_path_absolute = os.path.abspath(self.test_path)
            self.test_path_relative_root = os.path.basename(self.test_path)
            self.test_path_relative_root_no_ext = self.test_path_relative_root.rsplit('.', 1)[0]
            self.test_path_relative_root_2 = self.test_path_relative_root + '.2'
            self

# Generated at 2022-06-13 15:51:11.873987
# Unit test for method from_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:51:14.224152
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    assert _AnsiblePathHookFinder(None, 'fake').find_module('ansible_collections.ns.coll.module') is not None
    # TODO: more cases


# Implements the root ansible_collections package; the top-level package for all collections, but does not contain
# anything itself.

# Generated at 2022-06-13 15:51:20.960370
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    pkgloader = _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ns.module')
    pkgloader._subpackage_search_paths = ['/path/to/ansible_collections/ns/module']
    expected_data = b'content\n'
    assert pkgloader.get_data('/path/to/ansible_collections/ns/module/file.py') == expected_data
    assert pkgloader.get_data('/path/to/ansible_collections/ns/module/__init__.py') == expected_data
    assert pkgloader.get_data('/path/to/ansible_collections/ns/module/file.py') != b''

# Generated at 2022-06-13 15:51:50.530957
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    parent_name = 'dummy_parent'
    sub_mod_names = ['sub_mod_1', 'sub_mod_2']
    sub_pkg_names = ['sub_pkg_1', 'sub_pkg_2']
    names = sub_mod_names + sub_pkg_names

    class _Loader(_AnsibleCollectionPkgLoaderBase):
        def _validate_args(self):
            pass

        def _get_subpackage_search_paths(self, candidate_paths):
            return os.path.join(candidate_paths[0], self._split_name[1])

    loader = _Loader(parent_name)
    for p in names:
        os.makedirs(os.path.join(loader._subpackage_search_paths, p))

# Generated at 2022-06-13 15:52:02.795367
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():

    config_path_list = '~/configured_path/collections'
    playbook_path_list = ['~/playbook_path1/collections', '~/playbook_path2/collections', '~/playbook_path3/collections']

    # mock the finder class
    from unittest.mock import Mock
    _ansible_collection_path_hook_mock = Mock()
    setattr(_AnsibleCollectionFinder, '_ansible_collection_path_hook', _ansible_collection_path_hook_mock)
    _AnsibleCollectionFinder._n_cached_collection_paths = playbook_path_list + config_path_list
    _AnsibleCollectionFinder._n_configured_paths = [config_path_list]
    _AnsibleCollectionFinder

# Generated at 2022-06-13 15:52:11.455552
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    import os

    import sys

    import types
    import pytest
    from unittest.mock import MagicMock, Mock, call, patch
    from ._collection_loader import _AnsibleCollectionFinder

    # ensure _remove() doesn't fail in the happy path
    _AnsibleCollectionFinder._remove()

    _AnsibleCollectionFinder.__name__ = '_AnsibleCollectionFinder'
    with patch('{0}.sys.path_hooks'.format(__name__), new=[]), patch('{0}.sys.meta_path'.format(__name__), new=[]):
        acf = _AnsibleCollectionFinder()

        # mocked to prevent attempts to import real modules
        acf.find_module = Mock(name='find_module')
        assert acf.find_module.__qualname

# Generated at 2022-06-13 15:52:15.442438
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

    with pytest.raises(ValueError):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('non_existing_plugins')


# Generated at 2022-06-13 15:52:23.482573
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    objs_path = "./targets/objs"
    module_file_path = "./targets/objs/module_file.py"
    module_file_path_2 = "./targets/objs/collections/list_integers/module_file.py"
    module_file_path_3 = "./targets/objs/collections/dict_integers/module_file.py"
    module_file_path_4 = "./targets/objs/collections/int_integers/module_file.py"
    module_file_path_5 = "./targets/objs/collections/nested_integers/module_file.py"
    package_path = "./targets/objs/package"

# Generated at 2022-06-13 15:52:32.704798
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():
    # Usage of with requires Python 2.7 or higher
    with tempfile.NamedTemporaryFile() as f:
        fake_module_path = f.name
        fake_module_name = os.path.basename(f.name)
        # For Python3 is better to use the first line
        # fake_module_name = os.path.basename(f.name).split('.')[0]
        fake_module_name, ext = os.path.splitext(fake_module_name)
        loader = _AnsibleCollectionPkgLoaderBase(fake_module_name)
        loader._source_code_path = fake_module_path
        ret = loader.get_filename(fake_module_name)
        assert ret == fake_module_path

    with tempfile.TemporaryDirectory() as d:
        fake_package

# Generated at 2022-06-13 15:52:44.649332
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
  from __main__ import _AnsibleCollectionPkgLoaderBase
  from __main__ import _iter_modules_impl

  _loader = _AnsibleCollectionPkgLoaderBase('', '')
  _loader._fullname = ''
  _loader._redirect_module = None
  _loader._split_name = ''
  _loader._rpart_name = ''
  _loader._parent_package_name = ''
  _loader._package_to_load = ''
  _loader._source_code_path = ''
  _loader._decoded_source = ''
  _loader._compiled_code = ''

  _loader._module_file_from_path = _module_file_from_path
  _loader.get_filename = get_filename
  _loader.get_code = get_code
  _loader.iter = iter


# Generated at 2022-06-13 15:52:51.277688
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    test_module_name = 'ansible_collections.myns.mycoll.plugins.module_utils.foo'
    test_module_path = '/some/path/here'
    loader = _AnsibleCollectionPkgLoaderBase(test_module_name, path_list=[test_module_path])
    expected_return = '_AnsibleCollectionPkgLoaderBase(path=%s)' % test_module_path
    assert loader.__repr__() == expected_return



# Generated at 2022-06-13 15:52:54.629230
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    sys.path.append(os.path.dirname(__file__) + '/fixtures/ansible_collections/ns_pkg/')
    with _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.ns_pkg.ns_f0') as loader_base:
        loader_base.load_module()

# Generated at 2022-06-13 15:52:59.183258
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('modules') == 'module'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'module'


# Generated at 2022-06-13 15:54:00.277719
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    p = _AnsibleCollectionPkgLoader(None, 'ansible.collections.ansible_collections', 'ansible_collections')
    p.load_module('ansible.collections.ansible_collections')

# Generated at 2022-06-13 15:54:05.521616
# Unit test for method is_valid_collection_name of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_collection_name():
    assert AnsibleCollectionRef.is_valid_collection_name(None) == False
    assert AnsibleCollectionRef.is_valid_collection_name('') == False
    assert AnsibleCollectionRef.is_valid_collection_name('spam') == False
    assert AnsibleCollectionRef.is_valid_collection_name('spam.eggs') == True
    assert AnsibleCollectionRef.is_valid_collection_name('spam.eggs.green') == False



# Generated at 2022-06-13 15:54:14.041654
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    base = _AnsibleCollectionPkgLoaderBase('test', None)
    assert base.get_data('/a/file/that/does/not/exist') is None
    assert base.get_data('/a/file/that/does/not/exist2') is None
    assert base.get_data('/a/file/that/does/not/exist3') is None
    assert base.get_data('/a/file/that/does/not/exist4') is None

# Generated at 2022-06-13 15:54:25.770669
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    import tempfile
    import shutil
    import sys
    import io

    # set up temp dir
    temp_dir = tempfile.mkdtemp()
    subpackage = os.path.join(temp_dir, '__test_pkg__')
    package_init = os.path.join(subpackage, '__init__.py')
    module = os.path.join(temp_dir, '__test_mod__.py')
    # create subpackage, module
    os.mkdir(to_bytes(subpackage))
    open(to_bytes(package_init), 'w').close()
    open(to_bytes(module), 'w').close()

    loader = _AnsibleCollectionPkgLoaderBase('collection.__test_pkg__', path_list=[temp_dir])

    # get_data finds things we expect


# Generated at 2022-06-13 15:54:36.603656
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # Find the env var in a cross platform fashion
    import os
    import yaml
    import sys
    env_var = os.environ.get('ANSIBLE_COLLECTIONS_PATHS')
    # Get the path to the collection
    collection_path = None
    for path in env_var.split(os.pathsep):
        if 'ansible_collections/ansible' in path:
            if 'ansible.windows' in path:
                collection_path = path
            elif 'ansible.netcommon' in path:
                collection_path = path
            elif 'ansible.module_utils.common.network' in path:
                collection_path = path
    # Get the path to the module
    module_path = ''

# Generated at 2022-06-13 15:54:47.356229
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    source_code_path_1 = './test_elftools/__init__.py'
    source_code_path_2 = './test_elftools/elffile.py'
    source_code_path_3 = './test_elftools/elfheader.py'
    source_code_path_4 = './test_elftools/elfcore'
    source_code_path_5 = './test_elftools/version.py'
    source_code_path_6 = './test_elftools/elffile_test'
    source_code_path_7 = './test_elftools/version'
    source_code_path_8 = './test_elftools/__synthetic__'

# Generated at 2022-06-13 15:54:58.384570
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    _AnsibleCollectionFinder._remove()

    # patching the _AnsibleInternalRedirectLoader loader to raise an Exception
    def _AnsibleInternalRedirectLoader_mock(*args, **kwargs):
        raise Exception("test__AnsibleCollectionFinder_find_module")

    # patching the _AnsibleCollectionRootPkgLoader loader to raise an Exception
    def _AnsibleCollectionRootPkgLoader_mock(*args, **kwargs):
        raise Exception("test__AnsibleCollectionFinder_find_module")

    # patching the _AnsibleCollectionNSPkgLoader loader to raise an Exception
    def _AnsibleCollectionNSPkgLoader_mock(*args, **kwargs):
        raise Exception("test__AnsibleCollectionFinder_find_module")

    # patching the _Ansible

# Generated at 2022-06-13 15:55:10.572763
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves import builtins

    class Test_AnsibleCollectionPkgLoaderBase:
        def test__validate_args(self):
            with pytest.raises(ImportError):
                _AnsibleCollectionPkgLoaderBase._validate_args(None, "ansible.foo")

            with pytest.raises(ImportError):
                _AnsibleCollectionPkgLoaderBase._validate_args(None, "something_else.foo")

            with pytest.raises(ImportError):
                _AnsibleCollectionPkgLoaderBase._validate_args(None, "something_else")

            f = _AnsibleCollectionPkgLoaderBase._validate_args(None, "ansible_collections.foo")


# Generated at 2022-06-13 15:55:19.511441
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    # UUT
    loader = _AnsibleCollectionPkgLoaderBase(
        fullname='ansible_collections.test_collection.subcollection.subsubcollection',
        path_list=['/a/b/c/d', '/e/f/g/h']
    )
    loader._subpackage_search_paths = ['path1']
    loader._redirect_module = 'redirect_module'
    # test
    module = loader.load_module(fullname=loader._fullname)
    # verification
    assert sys.modules.get(loader._fullname) is module


# Generated at 2022-06-13 15:55:26.445320
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():
    '''
    This test check the get source code method of the class _AnsibleCollectionPkgLoaderBase
    :return:
    '''
    import patch
    fullname = 'ansible_collections.somens.somecollection'
    split_name = fullname.split('.')
    toplevel_pkg = split_name[0]

    path_hook = _AnsiblePathHookFinder(toplevel_pkg, None)
    path_finder = _AnsibleCollectionsPathFinder(path_hook, None)

    path = '/home/edgar/Repositories/ansible_collections/somens/somecollection/'
    loader_args = dict(fullname=fullname, path_list=[path])
    loader = _AnsibleCollectionPkgLoader(**loader_args)
    assert loader

# Generated at 2022-06-13 15:55:51.405077
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.subdir1.subdir2.resource', u'role')
    assert AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.resource', u'role')
    assert not AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.subdir1.resource', u'playbook')
    assert not AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.subdir1.subdir2.resource', u'playbook')
    assert AnsibleCollectionRef.try_parse_fqcr(u'ns.coll.subdir1.subdir2.resource_name.yml', u'playbook')

# Generated at 2022-06-13 15:56:01.110229
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    refObj = AnsibleCollectionRef('ns.coll', 'subdir1.subdir2', 'resource', 'module')
    assert (refObj.fqcr == 'ns.coll.subdir1.subdir2.resource')
    assert (refObj.n_python_collection_package_name == 'ansible_collections.ns.coll')
    assert (refObj.n_python_package_name == 'ansible_collections.ns.coll.plugins.subdir1.module')
    assert (refObj.resource == 'resource')
    assert (refObj.collection == 'ns.coll')

    refObj = AnsibleCollectionRef('ns.coll', None, 'resource', 'module')
    assert (refObj.fqcr == 'ns.coll.resource')

# Generated at 2022-06-13 15:56:06.861088
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    # data to be used as argument of function load_module
    fullname = "test_fullname"

    # creating a test object of class _AnsibleCollectionPkgLoader and calling load_module
    test_obj = _AnsibleCollectionPkgLoader(
        package_to_load=fullname,
        searching_path=[os.path.join(os.path.sep, 'etc', 'ansible', 'collections')]
    )
    assert test_obj.load_module(fullname) == None



# Generated at 2022-06-13 15:56:13.345522
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    ref_type = u'action'
    ref = u'namespace.collection.test_action'
    acr = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert acr.collection == u'namespace.collection'
    assert acr.subdirs == u''
    assert acr.resource == u'test_action'
    assert acr.ref_type == ref_type

    ref = u'namespace.collection.test_action.py'
    acr = AnsibleCollectionRef.from_fqcr(ref, u'playbook')
    assert acr.collection == u'namespace.collection'
    assert acr.subdirs == u''
    assert acr.resource == u'test_action'
    assert acr.ref_type == u'playbook'

    ref

# Generated at 2022-06-13 15:56:15.336050
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    with pytest.raises(TypeError):
        AnsibleCollectionRef.__repr__()

# Generated at 2022-06-13 15:56:26.013674
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():

    # Create instance of a class _AnsibleCollectionPkgLoader
    _ansible_collection_pkg_loader = _AnsibleCollectionPkgLoader(
        'ansible_collections.foo.bar',
        'bar', 'bar', ['col1/foo/bar', 'col2/foo/bar'],
        CollectionConfig.get_collection_config())

    # Create instance of a class ModuleType
    _module_type = ModuleType('ansible_collections.foo.bar')

    # Create instance of a class ModuleType
    def _new_or_existing_module_context():
        # Create instance of a class ModuleType
        _module_type = ModuleType('ansible_collections.foo.bar')
        return _module_type

    # Call method load_module of class _AnsibleCollectionPkgLoader

# Generated at 2022-06-13 15:56:31.683018
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    # The class catch only 'ansible' top level package
    _AnsibleInternalRedirectLoader('ansible.builtin', None)
    # Must raise exception for others
    try:
        _AnsibleInternalRedirectLoader('foo.builtin', None)
        assert False
    except ImportError:
        pass



# Generated at 2022-06-13 15:56:39.940444
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    """
    A unit test for the _AnsiblePathHookFinder module
    """
    from itertools import combinations

    test_path_hook_finder = _AnsiblePathHookFinder(
        collection_finder=None,
        pathctx='some_path',
    )
    test_path_hook_finder.find_module('some_module')
    test_path_hook_finder.iter_modules('some_prefix')
    test_path_hook_finder.__repr__()
    test_path_hook_finder._get_filefinder_path_hook()

    test_path_hook_finder._filefinder_path_hook = lambda path: 'some_content'
    test_path_hook_finder.find_module('some_module')

    test_path_hook_finder._filefinder_path_hook

# Generated at 2022-06-13 15:56:41.773061
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    ref="ns.coll.resource"
    ref_type="module"
    assert AnsibleCollectionRef.try_parse_fqcr(ref, ref_type) is not None


# Generated at 2022-06-13 15:56:47.443355
# Unit test for method load_module of class _AnsibleCollectionPkgLoader

# Generated at 2022-06-13 15:57:25.854548
# Unit test for method __repr__ of class AnsibleCollectionRef
def test_AnsibleCollectionRef___repr__():
    # Test with collection = 'namespace.collection', subdirs = 'subdir1.subdir2', resource = 'someaction'
    # This test case should work out nicely
    rc = AnsibleCollectionRef(u'namespace.collection', u'subdir1.subdir2', u'someaction', u'action')
    assert rc.__repr__() == u'AnsibleCollectionRef(collection=u\'namespace.collection\', subdirs=u\'subdir1.subdir2\', resource=u\'someaction\')'


# Generated at 2022-06-13 15:57:31.650524
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    from test.ansible_mock.utils.collection_loader import AnsibleMockCollectionConfig, AnsibleMockMetaYML

    # set class variables
    AnsibleMockCollectionConfig.COLLECTION_PATHS = [os.path.join(os.getcwd(), 'test/ansible_mock/ansible_data/collections/foo')]
    AnsibleCollectionConfig._config_object = AnsibleMockCollectionConfig()
    _meta_yml_to_dict = AnsibleMockMetaYML()._meta_yml_to_dict

    # create instance of class _AnsibleCollectionPkgLoader
    loader = _AnsibleCollectionPkgLoader(None, 'foo', None)
    assert 'foo' == loader._package_to_load
    assert ['foo'] == loader._split_name

    # create a

# Generated at 2022-06-13 15:57:39.972106
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Instance of _AnsibleCollectionFinder
    finder = _AnsibleCollectionFinder()
    # test if top-level package not equal to ansible or ansible_collections
    assert finder.find_module('foo') is None
    with pytest.raises(ValueError) as err:
        finder.find_module('ansible', path='foo')
    assert "path should not be specified for top-level packages" in str(err)
    with pytest.raises(ValueError) as err:
        finder.find_module('ansible_collections.foo')
    assert "path must be specified for subpackages" in str(err)



# Generated at 2022-06-13 15:57:50.210967
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    # Instantiate _AnsibleCollectionFinder
    ansible_collection_finder = _AnsibleCollectionFinder()

    # Test with fullname == 'ansible_collections.somens'
    fullname = 'ansible_collections.somens'
    ansible_collection_loader = ansible_collection_finder.find_module(fullname=fullname, path=None)
    print(ansible_collection_loader)

    # Test with fullname == 'ansible_collections.somens.somecoll'
    fullname = 'ansible_collections.somens.somecoll'
    ansible_collection_loader = ansible_collection_finder.find_module(fullname=fullname, path=None)
    print(ansible_collection_loader)

    # Test with fullname == 'ansible_col

# Generated at 2022-06-13 15:57:51.422841
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    #TODO: implement
    pass


# Generated at 2022-06-13 15:57:54.128697
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    obj = _AnsibleCollectionPkgLoaderBase("ansible_collections")
    output = obj.get_code("ansible_collections")
    assert output is None

# Generated at 2022-06-13 15:57:58.210448
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') == 'module_utils'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    raises(ValueError, lambda: AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('bad_type'))

# Unit tests for methods is_valid_collection_name, is_valid_fqcr and from_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:58:09.162034
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from ansible.utils.collection_loader import _AnsibleInternalRedirectLoader
    from ansible.utils.collection_loader import _get_collection_metadata
    from ansible.utils.collection_loader import _nested_dict_get
    from importlib import import_module
    from mock import patch
    from sys import modules
    with patch('ansible.utils.collection_loader._get_collection_metadata', lambda x: {"fake_collection_name": "fake_collection_path"}):
        with patch('ansible.utils.collection_loader._nested_dict_get', lambda x,y: {"fake_module": "fake_package"}):
            import_module("ansible.builtin.fake_module").__name__
            # Test passes if AssertionError is not raised

# Generated at 2022-06-13 15:58:16.347059
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    from _pytest.monkeypatch import MonkeyPatch
    from . import collection_loader
    from . import collections
    _m_load_module = _AnsibleInternalRedirectLoader
    _m_load_module.collection_loader = collections
    _m_load_module.collection_loader.collection_loader = collection_loader
    _m_load_module.collection_loader.collection_loader.redirected_package_map = {}
    monkeypatch = MonkeyPatch()

# Generated at 2022-06-13 15:58:26.807335
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():
    for legacy_plugin_dir_name in [
            'lib',
            'action_plugins',
            'cache_plugins',
            'callback_plugins',
            'cliconf_plugins',
            'connection_plugins',
            'doc_fragments',
            'filter_plugins',
            'httpapi_plugins',
            'inventory_plugins',
            'lookup_plugins',
            'module_utils',
            'modules',
            'netconf_plugins',
            'shell_plugins',
            'strategy_plugins',
            'terminal_plugins',
            'test_plugins',
            'vars_plugins',
    ]:
        plugin_type = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(legacy_plugin_dir_name)
        assert plugin_type in _PLUGIN_