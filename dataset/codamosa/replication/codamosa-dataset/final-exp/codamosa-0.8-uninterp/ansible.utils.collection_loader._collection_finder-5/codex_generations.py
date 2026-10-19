

# Generated at 2022-06-13 15:50:30.171436
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    """
    Test ansible.module_utils._collection_loader._AnsibleCollectionFinder.find_module()
    """
    module_args = dict(
        fullname='tests',
        path=None,
    )
    # TODO: implement this test
    # ansible.module_utils._collection_loader._AnsibleCollectionFinder.find_module(module_args)



# Generated at 2022-06-13 15:50:38.383599
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():
    module_name = 'ansible_collections.ns.module_a'
    module_path = [
        os.path.join(FIXTURE_PATH, 'collections', 'ns', 'module_a'),
        os.path.join(FIXTURE_PATH, 'collection1', 'ns', 'module_a')
    ]
    loader = _AnsibleCollectionPkgLoaderBase(module_name, path_list=module_path)
    assert ('module_a' in [x[1] for x in loader.iter_modules(prefix='ansible_collections')])
    assert ('module_b' not in [x[1] for x in loader.iter_modules(prefix='ansible_collections')])

# Generated at 2022-06-13 15:50:47.986538
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    # test with no path
    loader = _AnsibleCollectionPkgLoaderBase('foo')
    assert repr(loader) == '_AnsibleCollectionPkgLoaderBase(path=None)'

    # test with a single path
    loader = _AnsibleCollectionPkgLoaderBase('foo', ['some_path'])
    assert repr(loader) == "_AnsibleCollectionPkgLoaderBase(path=['some_path'])"

    # test with multiple paths
    loader = _AnsibleCollectionPkgLoaderBase('foo', ['some_path', 'other_path'])
    assert repr(loader) == "_AnsibleCollectionPkgLoaderBase(path=['some_path', 'other_path'])"

test__AnsibleCollectionPkgLoaderBase___repr__()



# Generated at 2022-06-13 15:50:58.034295
# Unit test for constructor of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder():
    import sys
    import tests
    import os

    fixture = os.path.join(os.path.dirname(tests.__file__), 'fixtures/test/ansible_collections/test_empty_module')
    assert os.path.isdir(fixture)

    _AnsiblePathHookFinder._remove()

    finder = _AnsibleCollectionFinder(paths=[fixture])

    assert finder._n_collection_paths == [fixture]

    finder._install()

    # identify the path hook
    path_hook = [ph for ph in sys.path_hooks if 'AnsiblePathHook' in repr(ph)]
    assert len(path_hook) == 1

    path_hook = path_hook[0]

    path_finder = path_hook(fixture)

# Generated at 2022-06-13 15:51:10.331747
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef

# Generated at 2022-06-13 15:51:16.681715
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    import ansible_collections.ns1.a1

    assert isinstance(ansible_collections.ns1.a1._loading_pkg_loader, _AnsibleCollectionPkgLoaderBase)
    code = ansible_collections.ns1.a1._loading_pkg_loader.get_code('ansible_collections.ns1.a1')
    from ansible_collections.ns1.a1 import _symbols
    assert isinstance(code, types.CodeType)
    exec(code, _symbols)
    assert _symbols['a1']
    assert _symbols['_a1']
    assert _symbols['_a1_a']
    assert _symbols['_a1_b']

    # Missing package module

# Generated at 2022-06-13 15:51:21.983143
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    class _AnsibleInternalRedirectLoaderNoRedirect(object):
        def __init__(self, fullname, path_list):
            self._redirect = None
            self._fullname = fullname
            self._path_list = path_list

        def load_module(self, fullname):
            raise ValueError('no redirect found for {0}'.format(self._fullname))

    no_redirect = _AnsibleInternalRedirectLoaderNoRedirect('test_import_redirect', ['/fake'])
    assert_raises(ValueError, no_redirect.load_module, 'test_import_redirect')


# Generated at 2022-06-13 15:51:32.605289
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():

    class _AnsibleCollectionPkgLoaderBase_Test(_AnsibleCollectionPkgLoaderBase):
        def _get_candidate_paths(self, path_list):
            return path_list

    coll_pkg_loader_base = _AnsibleCollectionPkgLoaderBase_Test('test_ns')

    # Test null case (fullname is not right). It will raise error.
    try:
        coll_pkg_loader_base.get_filename('test_ns1')
    except ValueError:
        pass

    # Test package case.
    coll_pkg_loader_base._subpackage_search_paths = ['/foo', '/bar']
    assert coll_pkg_loader_base.get_filename('test_ns') == '/foo/__synthetic__'
    coll_pkg_loader_base._subpackage_search_

# Generated at 2022-06-13 15:51:37.090378
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    import ansible.utils.collection_loader

    # set _meta_yml_to_dict to a dummy function for test
    ansible.utils.collection_loader._meta_yml_to_dict = lambda x, y: None

    # test with _collection_meta is None 
    t = _AnsibleCollectionPkgLoader(package_to_load='test', base_path='/test/')
    t.load_module('ansible.test')


# Implements implicit module loading based on a toplevel package's __path__

# Generated at 2022-06-13 15:51:42.091402
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():
    paths = [os.path.join(ans_collec_path, 'ns1', 'coll1')]
    # _AnsibleCollectionFinder(paths, scan_sys_paths=False)
    assert _AnsibleCollectionFinder(paths, scan_sys_paths=False)



# Generated at 2022-06-13 15:52:31.692295
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.test.test', ['/test/test/test'])

    class TestModule:
        def __init__(self):
            self.a = 1
            self.b = 'asdf'
            self.c = {}

    module = loader.load_module('ansible_collections.test.test.test')

    assert module.__loader__ == loader
    assert module.__file__ == '/test/test/test/__init__.py'
    assert module.__package__ == 'ansible_collections.test.test.test'


# Generated at 2022-06-13 15:52:44.494648
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():
    import unittest
    import tempfile
    import shutil
    import sys
    import os
    from ansible.module_utils.six import PY2

    # FIXME: put this in a better place
    class _MockModuleUtilsMetaYaml(object):
        def __init__(self):
            self.contents = {}
            self.file_name = None
            self.depth = 0

        def load(self, file_name):
            self.file_name = file_name

        def get(self, key, *args, **kwargs):
            return self.contents.get(key, *args, **kwargs)

        def __contains__(self, key):
            return key in self.contents

        def __enter__(self):
            self.depth += 1
            return self


# Generated at 2022-06-13 15:52:54.119821
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    # Testing an instance method with path parameter
    o = _AnsibleCollectionPkgLoaderBase('ansible.test', ['/usr/lib/python2.7/dist-packages/ansible'])
    o.get_source = lambda x: "Testing an instance method with path parameter"
    o.get_code = lambda x: "Testing an instance method with path parameter"
    o.is_package = lambda x: False
    o._source_code_path = "/usr/lib/python2.7/dist-packages/ansible/test/__init__.py"
    assert(str(o) == "{0}(path='/usr/lib/python2.7/dist-packages/ansible/test/__init__.py')".format(o.__class__.__name__))
    o = _AnsibleCollectionPkgLoader

# Generated at 2022-06-13 15:52:56.551021
# Unit test for constructor of class _AnsibleCollectionRootPkgLoader
def test__AnsibleCollectionRootPkgLoader():
    with pytest.raises(ImportError):
        _AnsibleCollectionRootPkgLoader('ansible_collections.foo')



# Generated at 2022-06-13 15:53:04.071812
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():
    assert AnsibleCollectionRef("ns.coll", "subdir1.subdir2", "resourcename", "module")
    assert AnsibleCollectionRef("ns.coll", None, "resourcename", "module")
    assert AnsibleCollectionRef("ns.coll", None, "resourcename", "role")
    assert AnsibleCollectionRef("ns.coll", "subdir1.subdir2", "resourcename", "role")
    assert AnsibleCollectionRef("ns.coll", None, "resourcename", "action")
    assert AnsibleCollectionRef("ns.coll", None, "resourcename", "playbook")
    assert AnsibleCollectionRef("ns.coll", "subdir1.subdir2", "resourcename", "playbook")

    with pytest.raises(ValueError):
        assert Ans

# Generated at 2022-06-13 15:53:05.023672
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    pass


# Generated at 2022-06-13 15:53:08.747804
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    test_instance = _AnsibleCollectionPkgLoaderBase("ansible_collections.test_collection")
    result = test_instance.is_package("ansible_collections.test_collection")
    assert result == True



# Generated at 2022-06-13 15:53:21.317733
# Unit test for constructor of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader():
    # successful redirect
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.basic', [])
    assert loader._redirect == 'ansible_collections.ansible.builtin.module_utils.basic'

    # successful module
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.urls', [])
    assert loader._redirect == 'ansible.module_utils.urls'

    # module that doesn't exist in builtin
    loader = _AnsibleInternalRedirectLoader('ansible.module_utils.nope', [])
    assert not loader._redirect

    # not a toplevel package under ansible
    loader = _AnsibleInternalRedirectLoader('ansible.foo.bar.baz', [])
    assert not loader._redirect

    # not a to

# Generated at 2022-06-13 15:53:27.344879
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    # Create a dict of arguments
    args = {}
    args['collection_finder'] = None
    args['pathctx'] = None
    # Construct a new instance of the class
    obj = _AnsiblePathHookFinder(**args)
    # Return the result of the function call
    return obj.find_module(
        fullname=None,
        path=None,
    )



# Generated at 2022-06-13 15:53:36.755804
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():
    some_module = ModuleType('some_module')
    class _ACPLBMock(object):
        def __init__(self, _fullname, subpackage_search_paths=None):
            self._fullname = _fullname
            self._subpackage_search_paths = subpackage_search_paths

    m1 = _ACPLBMock(some_module.__name__)
    m2 = _ACPLBMock(some_module.__name__, [])
    m3 = _ACPLBMock(some_module.__name__, ['something_that_exists'])
    m4 = _ACPLBMock('not_the_right_module.name')

    # test that is_package correctly handles a module that is not a package

# Generated at 2022-06-13 15:55:12.196965
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir.resource', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.role', 'role') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.playbook', 'playbook') is not None

    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.resource') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.subdir.resource') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('ns.coll.role', 'role') is not None
   

# Generated at 2022-06-13 15:55:22.706553
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():
    import sys
    import tempfile
    import shutil
    import types
    import unittest

    class BasicTestCase(unittest.TestCase):
        def setUp(self):
            # create a temporary directory for the collection
            self.src_dir = tempfile.mkdtemp()
            # create the collection package
            self.pkg_dir = os.path.join(self.src_dir, 'ansible_collections', 'test_ns', 'test_coll')
            os.makedirs(self.pkg_dir)

            self.pkg_module_path = os.path.join(self.pkg_dir, 'test_pkg.py')
            with open(to_bytes(self.pkg_module_path), 'wb') as f:
                f.write(b"print('Hello')\n")


# Generated at 2022-06-13 15:55:35.172181
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():
    # importing the module
    import os
    import sys
    import inspect
    import shutil
    import tempfile
    import importlib
    import ansible_collections.test.mazer.zip_it.plugins.modules.zip_it as tm1
    import ansible_collections.test.mazer_empty.collection as tm2
    import ansible_collections.test.mazer_with_init.collection as tm3
    import ansible_collections.test.mazer_with_init_2.collection as tm4

    try:
        from importlib.util import source_from_cache
    except ImportError:
        from importlib import util
        source_from_cache = util.source_from_cache


# Generated at 2022-06-13 15:55:41.745254
# Unit test for constructor of class AnsibleCollectionRef

# Generated at 2022-06-13 15:55:48.726502
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():
    # AnsibleFileFinder.__repr__
    path = "/usr/lib/python/site-packages/ansible/plugin_utils/httpget"
    af = _AnsibleCollectionPkgLoaderBase(path)
    af_repr = af.__repr__()
    if '<ansible_synthetic_collection_package>' in af_repr:
        print('PASS1')
    else:
        print('FAIL1')

# Generated at 2022-06-13 15:56:00.389494
# Unit test for method __repr__ of class AnsibleCollectionRef

# Generated at 2022-06-13 15:56:09.085144
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():
    test_object = _AnsibleCollectionPkgLoader(['test_ns', 'test_coll', 'test_module'], '/test/path/module_file', '/test/path/module_file')

    with pytest.raises(ValueError):
        test_object.load_module(['test_ns', 'test_coll', 'test_module'])

    with pytest.raises(ValueError):
        test_object.load_module(['test_ns', 'test_coll', 'test_module'])

    with pytest.raises(ValueError):
        test_object.load_module(['test_ns', 'test_coll', 'test_module'])


# Generated at 2022-06-13 15:56:20.740808
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():
    assert AnsibleCollectionRef.from_fqcr("ns.coll.mod", ref_type="module") == AnsibleCollectionRef(collection_name="ns.coll", subdirs="", resource="mod", ref_type="module")
    assert AnsibleCollectionRef.from_fqcr("ns.coll.subdir1.subdir2.mod", ref_type="module") == AnsibleCollectionRef(collection_name="ns.coll", subdirs="subdir1.subdir2", resource="mod", ref_type="module")
    assert AnsibleCollectionRef.from_fqcr("ns.coll.rolename", ref_type="role") == AnsibleCollectionRef(collection_name="ns.coll", subdirs="", resource="rolename", ref_type="role")

# Generated at 2022-06-13 15:56:29.393033
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():
    from pathlib import Path
    from ansible.module_utils.common._collections_compat import (
        log_deprecated,
        PathCollectionFinder,
    )
    from ansible.module_utils.common._collections_loader import (
        _AnsibleCollectionPkgLoaderBase,
    )
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    from collections import namedtuple
    import sys
    import pytest
    from types import ModuleType
    import inspect

    # Get the path to the ansible_collections directory
    ansible_collections_path = Path(__file__).parent
    collection_root = ansible_collections

# Generated at 2022-06-13 15:56:38.987110
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():
    import os
    import sys
    import tempfile

    def _make_collection_pkg(collection_name, pkg_name='test_package'):
        '''
        Make a collection module and its package.

        :param str collection_name: The collection name
        :param str pkg_name: The name of the package module
        :return: The path to the collection package directory
        :rtype: str
        '''
        # Create a collection
        collection_dir = tempfile.mkdtemp()
        collection_path = os.path.join(collection_dir, 'ansible_collections', collection_name)
        os.makedirs(collection_path)

        # Create a package in the *-*-* format