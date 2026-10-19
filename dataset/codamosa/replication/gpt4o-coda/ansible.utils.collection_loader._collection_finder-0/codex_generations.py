

# Generated at 2024-06-01 12:14:39.499932
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():    # Test valid fully-qualified collection reference
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result is not None
    assert result.collection == 'namespace.collection'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result is not None
    assert result.collection == 'namespace.collection'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test invalid fully-qualified collection reference
    ref = 'invalid.collection'
    ref_type

# Generated at 2024-06-01 12:14:43.057849
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():    collection_finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:14:44.945008
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:14:54.006722
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible_collections.test_namespace.test_collection')

# Generated at 2024-06-01 12:14:58.552050
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():    # Valid cases
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection.resource', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection.subdir.resource', 'module') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection.resource', 'role') is not None
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection.subdir.resource', 'role') is not None

    # Invalid cases
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection', 'module') is None
    assert AnsibleCollectionRef.try_parse_fqcr('namespace.collection.', 'module') is None
    assert AnsibleCollectionRef.try_parse_fqcr('namespace..resource', 'module') is None
    assert AnsibleCollectionRef.try_parse_fqcr('.collection.resource', 'module') is None
    assert AnsibleCollectionRef

# Generated at 2024-06-01 12:15:02.312822
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:15:05.513362
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    fullname = 'ansible_collections.test_namespace.test_collection'

# Generated at 2024-06-01 12:15:08.805418
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', ['/fake/path'])
    
    # Test when fullname matches and is a package

# Generated at 2024-06-01 12:15:11.873966
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():    # Test valid fully-qualified collection reference
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test invalid fully-qualified collection reference
    ref = 'invalid.collection'
    ref_type = 'module'

# Generated at 2024-06-01 12:15:14.751181
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():    collection_finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:16:13.692485
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():    # Test valid inputs
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.modules.subdir1.subdir2'
    assert ref.fqcr == 'namespace.collection.subdir1.subdir2.mymodule'

    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.n_python_package_name == 'ansible_collections.namespace.collection.plugins.modules'
    assert ref.f

# Generated at 2024-06-01 12:16:15.002519
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:16:18.356541
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['/fake/path'])
    
    # Test case 1: fullname matches and is a package

# Generated at 2024-06-01 12:16:20.275457
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:16:24.205856
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():    # Test valid inputs
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.fqcr == 'namespace.collection.subdir1.subdir2.mymodule'
    
    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.fqcr == 'namespace.collection.mymodule'
    
    # Test invalid collection name

# Generated at 2024-06-01 12:16:27.222707
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])
    
    # Mock methods to avoid actual file system access

# Generated at 2024-06-01 12:16:30.873062
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:16:34.504789
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible_collections.test_namespace.test_collection')

# Generated at 2024-06-01 12:16:38.031636
# Unit test for constructor of class AnsibleCollectionRef
def test_AnsibleCollectionRef():    # Test valid inputs
    ref = AnsibleCollectionRef('namespace.collection', 'subdir1.subdir2', 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == 'subdir1.subdir2'
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.fqcr == 'namespace.collection.subdir1.subdir2.mymodule'

    ref = AnsibleCollectionRef('namespace.collection', None, 'mymodule', 'modules')
    assert ref.collection == 'namespace.collection'
    assert ref.subdirs == ''
    assert ref.resource == 'mymodule'
    assert ref.ref_type == 'modules'
    assert ref.fqcr == 'namespace.collection.mymodule'

    # Test invalid collection name

# Generated at 2024-06-01 12:16:43.931999
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible_collections.test_namespace.test_collection')

# Generated at 2024-06-01 12:18:01.115127
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    loader = _AnsibleInternalRedirectLoader('ansible.builtin.some_module', [])

# Generated at 2024-06-01 12:18:04.580509
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:18:09.241468
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', ['/fake/path'])
    
    # Test case 1: When fullname matches and is a package

# Generated at 2024-06-01 12:18:12.701904
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

# Generated at 2024-06-01 12:18:14.723684
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:18:17.836901
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible_collections.test_namespace.test_collection')

# Generated at 2024-06-01 12:18:21.086132
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:18:24.586556
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:18:27.610116
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:18:31.233862
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():    collection_finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:19:07.499709
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():    # Test valid fully-qualified collection reference
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.fqcr == 'namespace.collection.resource'

    # Test valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.fqcr == 'namespace.collection.subdir1.subdir2.resource'

    # Test invalid fully

# Generated at 2024-06-01 12:19:10.575839
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:19:14.221764
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:19:17.495294
# Unit test for method try_parse_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_try_parse_fqcr():    # Test with valid fully-qualified collection reference
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result is not None
    assert result.collection == 'namespace.collection'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.subdirs == ''

    # Test with valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.try_parse_fqcr(ref, ref_type)
    assert result is not None
    assert result.collection == 'namespace.collection'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.subdirs == 'subdir1.subdir2'

    # Test with invalid fully-qualified collection reference
    ref = 'invalid.collection'


# Generated at 2024-06-01 12:19:20.282651
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible.builtin', ['/fake/path'])

# Generated at 2024-06-01 12:19:24.321831
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:19:27.679833
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:19:29.690554
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection')

# Generated at 2024-06-01 12:19:33.404603
# Unit test for method find_module of class _AnsiblePathHookFinder
def test__AnsiblePathHookFinder_find_module():    collection_finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:19:36.725552
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    fullname = 'ansible_collections.test_namespace.test_collection'

# Generated at 2024-06-01 12:20:08.499741
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection')

# Generated at 2024-06-01 12:20:11.574088
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test_module', [])

# Generated at 2024-06-01 12:20:13.946530
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    fullname = 'ansible_collections.test_namespace.test_collection'

# Generated at 2024-06-01 12:20:17.246525
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['/fake/path'])

    # Test with an absolute path that exists

# Generated at 2024-06-01 12:20:25.320109
# Unit test for method is_valid_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_is_valid_fqcr():    assert AnsibleCollectionRef.is_valid_fqcr('namespace.collection.resource') == True

# Generated at 2024-06-01 12:20:31.771720
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['/fake/path'])
    
    # Test with an absolute path that exists

# Generated at 2024-06-01 12:20:33.308937
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:20:37.191701
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])

# Generated at 2024-06-01 12:20:41.499457
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.testmod', path_list=['/fake/path'])

# Generated at 2024-06-01 12:20:43.904080
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])
    
    # Mock methods to avoid actual file system operations

# Generated at 2024-06-01 12:21:10.828004
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test_module', [])

# Generated at 2024-06-01 12:21:12.341410
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:21:16.451418
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])
    
    # Test case 1: Source code is already decoded

# Generated at 2024-06-01 12:21:19.917335
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():    # Test valid fully-qualified collection reference with no subdirs
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.fqcr == ref

    # Test valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'
    assert result.fqcr == ref

    # Test valid fully-qualified collection reference for a role
   

# Generated at 2024-06-01 12:21:21.908352
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])
    
    # Mock methods to avoid actual file system operations

# Generated at 2024-06-01 12:21:25.065685
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['/fake/path'])

    # Test with an absolute path that exists

# Generated at 2024-06-01 12:21:28.882603
# Unit test for method is_package of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_is_package():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.testpkg', path_list=['/fake/path'])

# Generated at 2024-06-01 12:21:32.062201
# Unit test for method from_fqcr of class AnsibleCollectionRef
def test_AnsibleCollectionRef_from_fqcr():    # Test valid fully-qualified collection reference
    ref = 'namespace.collection.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == ''
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test valid fully-qualified collection reference with subdirs
    ref = 'namespace.collection.subdir1.subdir2.resource'
    ref_type = 'module'
    result = AnsibleCollectionRef.from_fqcr(ref, ref_type)
    assert result.collection == 'namespace.collection'
    assert result.subdirs == 'subdir1.subdir2'
    assert result.resource == 'resource'
    assert result.ref_type == 'module'

    # Test invalid fully-qualified collection reference
    ref = 'invalid.collection'
    ref_type = 'module'

# Generated at 2024-06-01 12:21:34.230109
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test_module', [])

# Generated at 2024-06-01 12:21:37.558640
# Unit test for method legacy_plugin_dir_to_plugin_type of class AnsibleCollectionRef
def test_AnsibleCollectionRef_legacy_plugin_dir_to_plugin_type():    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

# Generated at 2024-06-01 12:22:17.008246
# Unit test for method get_filename of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_filename():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', ['/fake/path'])
    
    # Test when fullname matches and is a package

# Generated at 2024-06-01 12:22:21.268106
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    loader = _AnsibleInternalRedirectLoader('ansible.builtin.test_module', [])

# Generated at 2024-06-01 12:22:24.743481
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    fullname = 'ansible_collections.test_namespace.test_collection'

# Generated at 2024-06-01 12:22:29.518654
# Unit test for method load_module of class _AnsibleCollectionPkgLoader
def test__AnsibleCollectionPkgLoader_load_module():    loader = _AnsibleCollectionPkgLoader('ansible_collections.test_namespace.test_collection')

# Generated at 2024-06-01 12:22:32.472723
# Unit test for method load_module of class _AnsibleInternalRedirectLoader
def test__AnsibleInternalRedirectLoader_load_module():    fullname = 'ansible.builtin.test_module'

# Generated at 2024-06-01 12:22:34.557663
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:22:37.353122
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    fullname = 'ansible_collections.test_namespace.test_collection'

# Generated at 2024-06-01 12:22:40.077102
# Unit test for method get_source of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_source():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection', path_list=['/fake/path'])

# Generated at 2024-06-01 12:22:41.231873
# Unit test for method __repr__ of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase___repr__():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:22:43.023877
# Unit test for method get_code of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_code():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])
    
    # Mock methods to avoid actual file system operations

# Generated at 2024-06-01 12:23:09.618578
# Unit test for method get_data of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_get_data():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['/fake/path'])

    # Test with a valid file path

# Generated at 2024-06-01 12:23:12.863729
# Unit test for method iter_modules of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_iter_modules():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=['/fake/path'])

# Generated at 2024-06-01 12:23:14.808410
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_collection')

# Generated at 2024-06-01 12:23:18.203374
# Unit test for method load_module of class _AnsibleCollectionPkgLoaderBase
def test__AnsibleCollectionPkgLoaderBase_load_module():    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test_namespace.test_collection', ['/fake/path'])
    
    # Mocking methods and attributes

# Generated at 2024-06-01 12:23:21.255435
# Unit test for method find_module of class _AnsibleCollectionFinder
def test__AnsibleCollectionFinder_find_module():    finder = _AnsibleCollectionFinder(paths=['/fake/path'])