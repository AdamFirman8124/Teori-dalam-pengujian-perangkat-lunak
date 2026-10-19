

# Generated at 2022-06-13 13:19:02.582915
# Unit test for function get_shell_plugin
def test_get_shell_plugin():
    # Test the default sh
    shell = get_shell_plugin()
    assert shell.name == "sh"

    # Test the executable to be used
    shell = get_shell_plugin(executable="/bin/bash")
    assert shell.name == "bash"
    shell = get_shell_plugin(executable="/usr/bin/sh")
    assert shell.name == "sh"
    shell = get_shell_plugin(executable="/bin/ksh")
    assert shell.name == "ksh"
    shell = get_shell_plugin(executable="/usr/bin/zsh")
    assert shell.name == "zsh"

    # Test the shell family type
    shell = get_shell_plugin(shell_type="csh")
    assert shell.name == "csh"

# Generated at 2022-06-13 13:19:06.817468
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    pattern = re.compile(r'^test_PluginLoader_get_with_context\(\)\s*-\s*(.*)$')
    # Test with collection versions.
    # Test with no collections.
    # Test with no ansible.builtin collection.
    # Test with no ansible.builtin collection and no collections.
    # Test with no ansible.builtin collection and no collections version.
    # Test with no versions and no collections version.
    # Test with no versions and no collections.
    # Test with no versions.
    # Test with no collection versions and no collections.
    # Test with no collection versions and no collections version.
    pass



# Generated at 2022-06-13 13:19:16.987499
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    from ansible.utils.collection_loader import TestJinja2Loader, TestJinja2LoaderError
    import sys
    import os

    if TestJinja2Loader.FIXTURE_PATH not in sys.path:
        sys.path.append(TestJinja2Loader.FIXTURE_PATH)


# Generated at 2022-06-13 13:19:31.056574
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    tmp_dir = tempfile.mkdtemp()
    collections_path = tmp_dir + '/ansible_namespace/my_collection/my_subcollection/plugins/my_plugin_type'
    os.makedirs(collections_path)
    plugin_path = collections_path + '/my_plugin.py'
    with open(plugin_path, 'w') as plugin:
        plugin.write('def my_plugin():\n    pass')
    with open(collections_path + '/__init__.py', 'w') as init:
        init.write('from . import my_plugin')

# Generated at 2022-06-13 13:19:38.717732
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    def invoke(loader, name, collection_list=None):
        return loader.find_plugin(name, collection_list=collection_list)

    loader = PluginLoader(package='ansible_collections.nsbl.test',
                          subdir='plugins',
                          class_name='ActionModule',
                          aliases={'val': 'val'},
                          plugin_params={})

    assert invoke(loader, 'action,foo,bar') is None
    assert invoke(loader, 'action,foo,bar.py') is None
    assert invoke(loader, 'action,foo,bar,baz') is None

    assert invoke(loader, 'action') is None
    assert invoke(loader, 'action.py') is None

    assert invoke(loader, 'foo') is None
    assert invoke(loader, 'foo.py') is None


# Generated at 2022-06-13 13:19:52.705500
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    global PLUGIN_PATH_CACHE

    args = ['foo', '_bar', 'name1', 'name2', '-b', 'argparse', 'a_module', 'a_package']
    kwargs = {'subdir': 'test_plugins'}
    p = PluginLoader.get(**kwargs)

    # test 1
    PLUGIN_PATH_CACHE = {}
    assert p.find_plugin(*args) == None
    assert set(PLUGIN_PATH_CACHE.keys()) == set(['test_plugins', 'filter_plugins'])
    assert PLUGIN_PATH_CACHE['test_plugins'] == set([])
    assert PLUGIN_PATH_CACHE['filter_plugins'] == set([])
    assert p.aliases == {}

    # test 2
    args

# Generated at 2022-06-13 13:20:02.871133
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import tempfile
    import shutil
    import ansible.plugins.action

    # We need a temporary directory to work in because we can't guarantee that the added plugin directories won't override existing plugin directories
    # Create temporary plugin directories
    tmpdir = tempfile.mkdtemp()
    tmpdir_action = tempfile.mkdtemp(dir=tmpdir)
    plugin_file = tempfile.NamedTemporaryFile(dir=tmpdir_action, prefix="action_plugin_", suffix=".py", delete=False)
    plugin_file.close()
    tmpdir_callback = tempfile.mkdtemp(dir=tmpdir)
    plugin_file = tempfile.NamedTemporaryFile(dir=tmpdir_callback, prefix="callback_plugin_", suffix=".py", delete=False)
    plugin_file.close()
    tmpdir_

# Generated at 2022-06-13 13:20:09.479748
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    # NOTE: this test does not validate the output is correct, just that it executes without failures.
    from ansible.plugins.loader import al, Jinja2Loader
    from ansible.plugins.loader.filter_loader import FilterPluginLoader
    from ansible.plugins.loader.test_loader import TestPluginLoader
    from ansible.plugins.loader.module_loader import ActionModuleLoader
    from ansible.plugins.loader.module_loader import ConnectionModuleLoader
    from ansible.plugins.loader.module_loader import BecomeModuleLoader
    from ansible.plugins.loader.module_loader import CLIModuleLoader
    from ansible.plugins.loader.module_loader import CacheModuleLoader
    from ansible.plugins.loader.module_loader import LookupModuleLoader
    from ansible.plugins.loader.module_loader import VarsModuleLoader

# Generated at 2022-06-13 13:20:14.665929
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    name = 'foo'
    collection_list = None
    plugin_load_context = PluginLoadContext({}, [], None)

    instance = PluginLoader('ansible.plugins.action', 'ActionModule')
    result = instance.__contains__(name, collection_list)

    assert result is False

# Generated at 2022-06-13 13:20:22.053489
# Unit test for method find_plugin of class PluginLoader

# Generated at 2022-06-13 13:21:08.234295
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    import ansible.modules.not_a_real_collection as fakecol

    # We need to create a plugin loader that can load the fake collection
    test_finder = PluginLoader('', 'ansible.plugins.not_a_real_collection', 'NotARealCollectionModule')
    fakecol_path = os.path.dirname(fakecol.__file__)
    test_finder.add_directory(fakecol_path)


# Generated at 2022-06-13 13:21:12.292998
# Unit test for method all of class Jinja2Loader
def test_Jinja2Loader_all():
    # NOTE: This was test for above method. It should be merged into the general unit test for the
    # plugin loader after the issue of collection plugin lookup is addressed
    with pytest.raises(AnsibleError):
        j2 = Jinja2Loader(collection_list=None)
        assert j2.all() is not None

    mock_ansible_module_plugins = [
        'test_plugin_1.py',
        'test_plugin_2.py',
        'test_plugin_3.py',
        'test_plugin_4.py'
    ]

    with pytest.raises(AnsibleError):
        j2 = Jinja2Loader(collection_list=None)
        assert j2.all() is not None

    j2 = Jinja2Loader(collection_list=None)


# Generated at 2022-06-13 13:21:21.034743
# Unit test for method find_plugin_with_context of class PluginLoader
def test_PluginLoader_find_plugin_with_context():
    '''
    PluginLoader: find_plugin_with_context()
    '''
    name = 'testplugin'
    suffix = 'test'
    collection_list = ['test_col']
    class_name = 'TestPlugin'
    base_class = 'BasePlugin'
    packages = ['ansible.plugins.test_load_context', 'ansible_collections.test_col.plugins.test_load_context']
    package = 'ansible.plugins.test_load_context'
    package_dir = os.path.dirname(__file__)
    search_paths = ['test_load_context']
    config_section = 'testplugin'
    config_class = 'ConfigClass'
    config_defaults = 'defaults'
    aliases = {}
    subdir = 'test_load_context'
    directories

# Generated at 2022-06-13 13:21:30.826814
# Unit test for function add_dirs_to_loader
def test_add_dirs_to_loader():
    assert add_dirs_to_loader(which_loader='shell', paths='/') == ('shell_loader', ['/'])
    assert add_dirs_to_loader(which_loader='module', paths=['/', '/module']) == ('module_loader', ['/', '/module'])
    assert add_dirs_to_loader(which_loader='cache', paths=['/', '/module']) == ('cache_loader', ['/', '/module'])
    assert add_dirs_to_loader(which_loader='action', paths=['/', '/item']) == ('action_loader', ['/', '/item'])
    assert add_dirs_to_loader(which_loader='lookup', paths=['/', '/var']) == ('lookup_loader', ['/', '/var'])
    assert add_dir

# Generated at 2022-06-13 13:21:41.574052
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    from ansible.module_utils._text import to_bytes

    # FIXME: a lot of these tests should not be asserting on the full plugin_resolved_path
    # we should be asserting on the expected FQCR or FQP instead in most cases

    # Test with name = init: search_path = ['\tests\units\module_utils\legacy\plugins']: expected = '\tests\units\module_utils\legacy\plugins\__init__.py'
    plugin_loader = PluginLoader('module_utils', 'ansible.module_utils.module_common', '', '', '', '__init__')
    (r_plugin_name, r_plugin_path, r_found_in_cache) = plugin_loader.find_plugin('init', collection_list=['ansible.module_utils.legacy.plugins'])

# Generated at 2022-06-13 13:21:45.649414
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    loader = PluginLoader('ansible.plugins.test.test_plugin_loader.test_plugins', 'TestPlugin')
    # Test working case
    found_plugin = loader.find_plugin('test')
    assert found_plugin, "Test plugin not found"
    assert found_plugin.endswith(os.path.join('test_plugins', 'test.py')), "Found plugin %s does not appear to be correct, should end with 'test_plugins/test.py'" % found_plugin
    # Test case with an import
    found_plugin = loader.find_plugin('test', class_only=True)
    assert found_plugin, "Test plugin not found"

# Generated at 2022-06-13 13:21:54.552131
# Unit test for method find_plugin_with_context of class PluginLoader

# Generated at 2022-06-13 13:21:55.774342
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    plugin_loader = PluginLoader('somepath', 'some_package', 'some_base')
    assert not ('some_name' in plugin_loader)



# Generated at 2022-06-13 13:21:57.806460
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    pass



# Generated at 2022-06-13 13:22:08.538688
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    plugin_loader = PluginLoader(package='thing', class_name='Thing', configurable=True, min_subdir_count=2)
    # this is testing for a bug where decorated methods were not being
    # called when used with get_with_context.

    def decorator(func):
        def new_func(*args, **kwargs):
            return func(*args, **kwargs)
        return new_func

    class Thing(object):
        def hello(self, value=None):
            return 'hello'

        @decorator
        def world(self, value=None):
            return 'world'

    plugin_loader._module_cache['/tmp/fake_path'] = Thing()

    # First check for the bug
    plugin_load_context = plugin_loader.get_with_context('Thing')
    assert plugin

# Generated at 2022-06-13 13:23:02.472184
# Unit test for method add_directory of class PluginLoader
def test_PluginLoader_add_directory():

    filename1 = '/home/username/ansible/plugins/inventory/host1.py'
    filename2 = '/home/username/ansible/plugins/inventory/host2.py'

    # Test if the list is empty
    loader = PluginLoader('test', 'plugin_type', '')
    test = loader.get_all_plugin_loaders()
    assert test == {}, 'Test 1 Failed!'

    # Test if the directory is None
    loader = PluginLoader('test', 'plugin_type', None)
    test = loader.get_all_plugin_loaders()
    assert test == {}, 'Test 2 Failed!'

    # Test if the directories are added
    loader = PluginLoader('test', 'plugin_type', '')
    loader.add_directory(filename1)
    loader.add_directory(filename2)
    test = loader

# Generated at 2022-06-13 13:23:03.655491
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    assert False # TODO: implement your test here


# Generated at 2022-06-13 13:23:12.603797
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text, to_native
    from ansible.utils.path import unfrackpath, makedirs_safe
    from ansible.plugins.loader import fragments_loader as fragments_loader_class
    import tempfile

    # Make a temporary directory and add it to the start of sys.path so we can
    # import our sample plugin
    tmp_path = to_text(tempfile.mkdtemp())
    makedirs_safe(tmp_path)
    sys.path.insert(0, unfrackpath(tmp_path))

    # We don't want to import the top-level 'fragments' module which is the
    # default namespace for fragment plugins, so set the plugin class to
    # import a submodule instead

# Generated at 2022-06-13 13:23:25.619493
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    '''test_PluginLoader_all'''

    # PluginLoader, plugin_package, name, class_name, basedir, module_name=None, package=None, config_base=None, collection_list=None, base_class=None, subdir=None, aliases=None
    # Create an instance of PluginLoader
    # PluginLoader.get(name, *args, **kwargs)

    PL = PluginLoader('deprecated_action_plugin', 'deprecated_action_plugin', 'deprecated actions',
                      os.path.join(os.path.expanduser('~'), 'ansible/ansible/plugins/deprecated_action_plugin'),
                      package='ansible.plugins.deprecated_action_plugin')
    PL.all()
# exit(0)


# Generated at 2022-06-13 13:23:26.417200
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    assert True



# Generated at 2022-06-13 13:23:40.701959
# Unit test for method get_with_context of class PluginLoader
def test_PluginLoader_get_with_context():
    """
    Test PluginLoader._get_with_context
    """

    class TestPlugin(object):
        pass

    # Test loading from a single directory
    pl = PluginLoader('unit_test', 'ansible.unit_test', 'TestPlugin', 'test')
    pl._add_directory(os.path.join(os.path.dirname(__file__), 'test_plugins'))

    # Test loading a plugin that does not exist
    assert pl.get_with_context('fake').object is None
    assert pl.get_with_context('fake').resolved is False

    # Test loading a plugin that is a partial import
    assert pl.get_with_context('partialimport.py').object is None
    assert pl.get_with_context('partialimport.py').resolved is True

    # Test loading a plugin that imports correctly


# Generated at 2022-06-13 13:23:47.085395
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.plugins import AnsiblePluginWrapper, filter_loader, test_loader
    from ansible.plugins.loader import Jinja2Loader
    from ansible.playbook.play_context import PlayContext

    # Invalid name (Not CollectionRef)
    try:
        filter_loader.get("foo")
        raise AssertionError("Failed to raise AnsibleError with invalid name")
    except AnsibleError:
        pass
    try:
        test_loader.get("foo")
        raise AssertionError("Failed to raise AnsibleError with invalid name")
    except AnsibleError:
        pass

    # invalid name (not CollectionRef)

# Generated at 2022-06-13 13:23:55.999685
# Unit test for method find_plugin of class Jinja2Loader
def test_Jinja2Loader_find_plugin():
    tmpdir = tempfile.mkdtemp()
    name = os.path.join(tmpdir, 'filterfile.py')

    with open(name, 'w+') as f:
        f.write("""def myfilter(s):
    return 'filtered'
""")

    try:
        p = Jinja2Loader('ansible.plugins.filter', 'FilterModule', 'filter_plugins', package_subdir='filter_plugins').find_plugin('filterfile', collection_list=[])
        assert p == name
    finally:
        shutil.rmtree(tmpdir)


# Generated at 2022-06-13 13:24:05.361169
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    _temp_dir = tempfile.mkdtemp()
    _temp_dir_name = os.path.basename(_temp_dir)

    # test duplicate plugin
    _plugin_1_dir = os.path.join(_temp_dir, 'plugins', 'lookup', 'plugin1')
    os.makedirs(_plugin_1_dir)
    with open(os.path.join(_plugin_1_dir, '__init__.py'), 'w') as f:
        f.write('from ansible.plugins.lookup import LookupBase\n'
                'class LookupModule(LookupBase):\n'
                '    def run(self, *args, **kwargs):\n'
                '        pass\n')

# Generated at 2022-06-13 13:24:16.259812
# Unit test for method all of class PluginLoader
def test_PluginLoader_all():
    def mockreturn(self,*args,**kwargs):
        if len(args) == 0 and len(kwargs) == 0:
            return None
        elif args == ('foo','bar','baz','qux','quux',) and kwargs == {'corge':'grault','garply':'waldo'}:
            return None
        else:
            raise AssertionError('unexpected call to PluginLoader.get')
    import __main__
    import sys
    import imp
    import os
    import glob
    import collections
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    from ansible.utils.display import Display
    # setup test
    display = Display()
    # create test module

# Generated at 2022-06-13 13:24:47.154070
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    # Clear the directories for all plugin objects
    for name, obj in get_all_plugin_loaders():
        obj.directories = []
    # Add the plugin directory to all plugin objects
    plugin_path = os.path.join("/path/to/ansible", "plugins")
    add_all_plugin_dirs(plugin_path)
    # Check that the plugin_path is properly added to all plugin objects
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            assert plugin_path + "/" + obj.subdir in obj.directories, [plugin_path + "/" + obj.subdir, obj.directories]


# for backwards compatibility purposes, we expose the alias 'ModuleLoader'
# as well as the correct 'PluginLoader' name
ModuleLoader = PluginLoader



# Generated at 2022-06-13 13:24:49.757960
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    plugins = Jinja2Loader('jinja2', 'ansible.legacy')
    if 'str' not in plugins.all():
        raise AssertionError('Answer is incorrect')


# Generated at 2022-06-13 13:24:56.340881
# Unit test for method record_deprecation of class PluginLoadContext
def test_PluginLoadContext_record_deprecation():
    import tempfile, shutil
    # Create a dummy collection which has a plugin with deprecation info, then test the record_deprecation method
    tempdir = to_native(tempfile.mkdtemp())
    collection_name = 'temp_collection'
    collection_dir = os.path.join(tempdir, collection_name)
    os.makedirs(collection_dir, mode=0o755)
    plugin_dir = os.path.join(collection_dir, 'plugins', 'test_plugins')
    os.makedirs(plugin_dir, mode=0o755)
    collection_config_file = os.path.join(collection_dir, 'galaxy.yml')

# Generated at 2022-06-13 13:24:58.161305
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    # TODO: write this test
    pass

# Generated at 2022-06-13 13:25:00.721365
# Unit test for method find_plugin of class PluginLoader
def test_PluginLoader_find_plugin():
    plugin_loader = PluginLoader('myplugin', 'myplugin', 'myplugin')
    assert plugin_loader.find_plugin('') == None

# Generated at 2022-06-13 13:25:11.322785
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    import sys
    import tempfile
    test_modules = os.path.join(tempfile.mkdtemp(), 'modules')
    add_all_plugin_dirs(test_modules)
    assert test_modules not in sys.path

    lib = os.path.join(test_modules, 'library')
    os.mkdir(lib)
    add_all_plugin_dirs(test_modules)
    assert lib in sys.path
    sys.path.remove(lib)

    module_utils = os.path.join(test_modules, 'module_utils')
    os.mkdir(module_utils)
    add_all_plugin_dirs(test_modules)
    assert module_utils in sys.path
    sys.path.remove(module_utils)


# Generated at 2022-06-13 13:25:14.811455
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import PluginLoader

    # build an object for the class
    plugin_loader = PluginLoader('v1')

    # call the method under test with valid arguments
    with pytest.raises(AnsibleError):
        plugin_loader.get('module')




# Generated at 2022-06-13 13:25:18.708264
# Unit test for method __contains__ of class PluginLoader
def test_PluginLoader___contains__():
    '''
    Unit test for method __contains__ of class PluginLoader
    '''
    pass # since the method is a generator


# Generated at 2022-06-13 13:25:27.969878
# Unit test for method get of class Jinja2Loader
def test_Jinja2Loader_get():
    from ansible.plugins.loader import filter_loader, test_loader
    from ansible.utils.display import Display
    display = Display()
    # Test: with valid display, invalid name
    loader_instance = filter_loader
    name = 'foobar'
    display = display
    check_list = []
    _list = loader_instance.get(name, display)
    check_list.append(type(_list) == tuple)
    check_list.append(type(_list[0]) == None)
    check_list.append(_list[1].startswith('plugin (%s) not found in' % name))
    check_list.append('    names:')
    check_list.append('foobar')
    assert all(check_list)
    # Test: with invalid display, valid name
    loader_instance = filter_loader

# Generated at 2022-06-13 13:25:34.607869
# Unit test for function add_all_plugin_dirs
def test_add_all_plugin_dirs():
    path = os.path.dirname(__file__) + "/../../../lib/ansible/plugins/action/test_add_all_plugin_dirs_path"
    add_all_plugin_dirs(path)
    for name, obj in get_all_plugin_loaders():
        if obj.subdir:
            plugin_path = os.path.join(path, to_bytes(obj.subdir))
            if os.path.isdir(plugin_path):
                assert plugin_path in obj.get_directories()

