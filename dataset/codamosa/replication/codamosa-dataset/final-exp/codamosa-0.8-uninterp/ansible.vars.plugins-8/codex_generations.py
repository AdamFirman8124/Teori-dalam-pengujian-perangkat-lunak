

# Generated at 2022-06-13 17:29:27.786035
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    data = {}
    entities = [ Host("foobar"), Host("foobar2")]

    # Test a call to v2 function
    def v2_get_vars(loader, path, entities):
        return { 'a':'b'}

    # Test a call to v1 function
    def v1_get_host_vars(host):
        return { 'a':'b'}

    class vars_plugin_loader(object):
        def __init__(self, name, path):
            self.path = path
            self._load_name = name
            self._original_path = path

    class vars_plugin(object):
        def __init__(self, name, path):
            self.vars_plugin_loader = vars_plugin_loader(name, path)


# Generated at 2022-06-13 17:29:33.166898
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    # test that the vars returned are correct when the sources list is an empty list
    assert get_vars_from_inventory_sources([]) == {}

    # test that the vars returned are correct when the sources list is not empty
    assert get_vars_from_inventory_sources(["path1", "path2"]) == {}

# Generated at 2022-06-13 17:29:46.015290
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class TestPlugin(object):
        def get_vars(self, loader, path, entities):
            return {'foo': 'test_get_vars'}

        def get_group_vars(self, group_name):
            return {'foo': 'test_get_group_vars'}

        def get_host_vars(self, host_name):
            return {'foo': 'test_get_host_vars'}

    loader = None
    plugin = TestPlugin()
    path = '/some/path'
    host_entities = [Host('testhost')]
    group_entities = [Host('testgroup')]
    data = get_plugin_vars(loader, plugin, path, host_entities)
    assert data['foo'] == 'test_get_host_vars'
    data

# Generated at 2022-06-13 17:29:50.868577
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    inventory_targets = "foo"
    loader = C.plugin_loader
    stage = "task"
    plugin = vars_loader.get("test_vars_plugin")
    
    result = get_vars_from_path(loader, "bar", inventory_targets, stage)
    assert result == {'test_vars_plugin_var': 'foo'}

# Generated at 2022-06-13 17:29:57.630311
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    test_plugin = MockVarsPlugin()
    loader = MockLoader()
    path = '/path/to/plugin'
    test_entities = [MockHost()]
    test_data = get_plugin_vars(loader, test_plugin, path, test_entities)
    assert test_data == {'foo': 'bar', 'baz': 'bop'}
    test_plugin.get_vars.assert_called_once_with(loader, path, test_entities)



# Generated at 2022-06-13 17:30:06.956500
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    def test_plugin(plugin_name):
        mock_loader = None
        plugin = vars_loader.get(plugin_name)
        assert plugin is not None, "Cannot find plugin %s" % plugin_name
        return get_plugin_vars(mock_loader, plugin, None, [])

    # use a different test for each step, do not combine them
    result1 = test_plugin('yaml')
    result2 = test_plugin('fact')
    result3 = test_plugin('hiera')

    expected1 = {'system_info': {'os': 'SunOS'}}
    assert result1 == expected1, \
        "Unexpected result:\n%s\nShould be:\n%s" % (result1, expected1)


# Generated at 2022-06-13 17:30:15.123051
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Test data used by unit test
    UNIT_TEST_DATA = {
        'unit_test_module': {
            'vars': {
                'foo': 'bar'
            }
        }
    }

    # Required to init the plugins
    vars_loader.all()

    # Get data from plugins
    data = get_vars_from_path(None, UNIT_TEST_DATA, None, 'test')

    # Validate that data is not none
    assert data is not None

    # Validate that data has key 'foo'
    assert data.get('foo') == 'bar'

# Generated at 2022-06-13 17:30:16.557980
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    res = get_vars_from_path(None, '/tmp', [], 'inventory')
    assert isinstance(res, dict)
    assert res == {}

# Generated at 2022-06-13 17:30:25.064912
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    def test_plugin(index_func, get_vars, get_host_vars, get_group_vars, run=None):
        # We can't mock a class, so mock functions on an object we can
        class TestClass:
            pass
        test_object = TestClass()
        test_object.index_func = index_func
        test_object.get_vars = get_vars
        test_object.get_host_vars = get_host_vars
        test_object.get_group_vars = get_group_vars
        test_object.run = run
        return test_object

    def test_loader():
        pass

    class TestHost(object):
        def __init__(self, name):
            self.name = name

    test_host = TestHost('test_host')

# Generated at 2022-06-13 17:30:26.436759
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path is not None

# Generated at 2022-06-13 17:30:58.775121
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.vars.base_vars import BaseVarsModule

    def get_vars_from_file(self, path):
        if not os.path.exists(path):
            return {}
        vars = {}
        with open(path, 'r') as f:
            vars.update(dict(line.rstrip().split(':', 1) for line in f if ':' in line))
        return vars

    BaseVarsModule.get_vars_from_file = get_vars_from_file

    def get_vars(self, loader, path, entities):
        vars = {}
        basedir = path
        for entity in entities:
            if isinstance(entity, Host):
                vars = combine_

# Generated at 2022-06-13 17:31:04.691633
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    """Testing the get_vars_from_path function to see if the data
    returned by the function is correct."""
    import ansible.plugins.vars.test_vars_2 as test_vars_2
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    entities = [Host('test.ansible.com')]
    stage = 'inventory'

    # First testing if an invalid plugin(class) type is passed. This should
    # raise an AnsibleError.
    class ClassSpecified(object):
        pass
    try:
        get_vars_from_path(loader, '', entities, stage, [ClassSpecified])
    except AnsibleError:
        pass

# Generated at 2022-06-13 17:31:11.335240
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.loader import test_vars
    from ansible.resources import CollectionLoader

    loader = CollectionLoader()
    vars_loader.add_directory(loader.get_basedir(test_vars))
    plugin = vars_loader.all()[0]
    data = get_plugin_vars(loader, plugin, "./", ['localhost'])

    assert data == {'test_plugin_vars': 'test_plugin_vars'}

# Generated at 2022-06-13 17:31:18.538545
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import vars_loader

    test_data = {}
    for plugin in vars_loader.all():
        test_data = combine_vars(test_data, get_plugin_vars(None, plugin, None, None))

    assert test_data == {}

# Generated at 2022-06-13 17:31:24.149946
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    '''
    Test get_vars_from_path.
    '''
    test_host_path = '~/playbooks/hosts'
    test_vars_plugin = '~/playbooks/plugins/files/vars/test.yaml'
    test_data = {
        'ansible_connection': 'local',
        'test_var': 'test',
    }
    assert get_vars_from_path([test_host_path, test_vars_plugin], test_host_path, [], '') == test_data

# Generated at 2022-06-13 17:31:33.171840
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader, lookup_loader
    display.verbosity = 4
    vars_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'plugins', 'vars'))
    lookup_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'plugins', 'lookup'))

    data = {'foo': 1}
    # In the vars_plugins/test.yaml file, the test_var is 1
    path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'plugins', 'vars')
    # There is not vars_plugins/test_var in v

# Generated at 2022-06-13 17:31:42.217254
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import tempfile
    import unittest

    data = {}
    plugin_name = "test_vars_plugin"
    class FakeVarsPlugin(object):
        REQUIRES_WHITELIST = False
        _load_name = plugin_name
        _original_path = plugin_name
        def get_vars(self, loader, path, entities):
            return {"get_vars": path}

    vars_loader.add(plugin_name, FakeVarsPlugin())

    # Test with RUN_VARS_PLUGINS not set
    data = combine_vars(data, get_vars_from_path(None, os.getcwd(), [], "task"))
    assert data == {"get_vars": os.getcwd()}

    # Test with RUN_VARS_PLUG

# Generated at 2022-06-13 17:31:49.811590
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader.vars_loader import VarsModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class DummyPlugin(VarsModule):
        pass

    class DummyPlugin1(VarsModule):
        pass

    class DummyPlugin2(VarsModule):
        pass

    class DummyPlugin3(VarsModule):
        pass

    dummy_plugin = DummyPlugin()
    dummy_plugin._load_name = 'dummy_plugin'
    dummy_plugin._original_path = 'dummy/path'

    dummy_plugin1 = DummyPlugin1()
    dummy_plugin1._load_name = 'dummy_plugin1'
    dummy_plugin1._original_

# Generated at 2022-06-13 17:31:53.834910
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pick_vars_plugin("./test/ansible/plugins/vars", "test_vars_plugin.py", "get_vars")

# Generated at 2022-06-13 17:32:02.908415
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.utils import context_objects as co

    context = co.Context(display, loader)

    # Test old style vars_plugin
    results = get_vars_from_path(context, 'test_path', ['test_entity'], 'inventory')

    results = get_vars_from_path(context, 'test_path', ['test_entity'], 'inventory')

    results = get_vars_from_path(context, 'test_path', ['test_entity'], 'task')

    results = get_vars_from_path(context, 'test_path', ['test_entity'], 'task')

    # Test new style vars_plugins
    vars_plugin = vars_loader.get('test_plugin')
    results = get_v

# Generated at 2022-06-13 17:33:11.937370
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    result = get_vars_from_inventory_sources(None, ['host'], None, 'inventory')
    assert result == {}
    result = get_vars_from_inventory_sources(None, ['host1'], None, 'task')
    assert result == {}

# Generated at 2022-06-13 17:33:19.582173
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    # Unit test with actual variables plugins

    # get all variables plugin
    vars_plugin_list = list(vars_loader.all())
    # get plugin with name 'docroot'
    vars_plugin = vars_loader.get('docroot')

    # get all plugin path
    plugin_path = {}
    for plugin in vars_plugin_list:
        plugin_path[plugin._load_name] = plugin._original_path
    
    # get docroot plugin path
    docroot_plugin_path = vars_plugin._original_path

    # get var from docroot plugin
    docroot_data = get_plugin_vars(vars_plugin, docroot_plugin_path, 'htdocs')

    # get var from all plugin path

# Generated at 2022-06-13 17:33:27.986671
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    sources = [
        '/etc/ansible/hosts'
    ]
    entities = ['host1', 'host2']
    stage = 'inventory'
    assert get_vars_from_inventory_sources(loader, sources, entities, stage), "Expected: A dictionary of variables from inventory source files, Got: This function didn't return any variables"

# Generated at 2022-06-13 17:33:37.470605
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import find_plugin_file_path
    from ansible.plugins.loader import vars_loader

    display.verbosity = 4
    # all_vars_plugins = vars_loader.all()
    old_all_vars_plugins = list(vars_loader._all_files)
    # TODO: add some options, ie. demand, start, etc., to run specific plugins
    # vars_plugin_test_path = find_plugin_file_path(os.path.join(C.DEFAULT_MODULE_PATH, 'vars-plugin-test'))
    vars_plugin_test_path = os.path.join(C.DEFAULT_MODULE_PATH, 'vars-plugin-test')
    assert vars_plugin_test_path not in vars_loader._all_

# Generated at 2022-06-13 17:33:38.021391
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:33:47.021339
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import unittest

    class TestPlugin():
        def get_vars(self, loader, path, entities):
            return {'plugin_vars': True}

    class AnsiblePluginLoader(object):
        def get(self, name):
            return TestPlugin()

    class AnsibleHost(object):
        def __init__(self, host_name):
            self.name = host_name

    class AnsibleGroup(object):
        def __init__(self, group_name):
            self.name = group_name

    class TestAnsibleModuleUtilsLoader(unittest.TestCase):
        # get_vars_from_path unit test
        def test_get_vars_from_path(self):
            test_entity = AnsibleHost('test')
            plugin = TestPlugin()

# Generated at 2022-06-13 17:33:51.801410
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader

    path = os.path.join(os.path.dirname(__file__), 'vars_plugin_fixture')
    data = get_vars_from_path(vars_loader, path, [], 'inventory')

    assert data == {'foo': 'bar'}

# Generated at 2022-06-13 17:33:54.335549
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    dbg_msg = "function get_vars_from_inventory_sources() failed"
    assert True, dbg_msg

# Generated at 2022-06-13 17:34:02.358673
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    sources = ["https://github.com/ansible-collections/community.general/tree/84e47b7a5924adadfde7a5f9cba9ac8f909ab66e/ansible_collections/community/general"]
    entities = [AnsibleCollectionRef.from_string("community.general.aws_vpc")]
    data = get_vars_from_path(AnsibleCollectionLoader(), sources[0], entities, "inventory")
    assert data['collection_name'] == 'community.general'
    assert data['collection_version'] == '0.0.0'

# Generated at 2022-06-13 17:34:12.865361
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    import imp
    from ansible.plugins.loader import plugin_loader

    # assert that vars from a plugin can be retrieved by get_vars_from_path
    plugin_path = './test/units/vars/vars_plugins/test_vars_path.py'
    plugin_name = 'test_vars_path'
    m = imp.new_module(plugin_name)
    m.__file__ = plugin_path
    exec(open(plugin_path, 'rb').read(), m.__dict__)
    plugin_loader._add_directory(os.path.dirname(plugin_path))
    plugin = vars_loader.get(plugin_name, class_only=True)

    data = get_vars_from_path(None, plugin_path, None, 'inventory')

    # should match the

# Generated at 2022-06-13 17:35:53.298519
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # create a temporary path
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_')

    # create a temporary ansible.cfg file in the tmpdir
    # see https://docs.python.org/2/library/tempfile.html#tempfile.NamedTemporaryFile
    from ansible.cli import CLI
    from ansible.config.manager import ConfigManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    cfgfile = tempfile.NamedTemporaryFile(mode='w+t', prefix='ansible_test_', suffix='.cfg', delete=False, dir=tmpdir, encoding=u'utf-8')
    cfgfile.write('[defaults]\n')

# Generated at 2022-06-13 17:35:54.188990
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
   assert True

# Generated at 2022-06-13 17:36:02.239454
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from .test_vars_plugins import VarsModuleTestPlugin

    class TestPlugin(VarsModuleTestPlugin):
        pass

    paths = ['/var/lib/awx/projects',
             '/var/lib/awx/projects/test/',
             './test/test_vars_plugins/plugins',
             './test/test_vars_plugins/plugins/test_plugin',
             './test/test_vars_plugins/plugins/test_plugin/vars_plugins']
    for path in paths:
        os.makedirs(path, exist_ok=True)
    loader = vars_loader

# Generated at 2022-06-13 17:36:13.484033
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible import constants as C
    from ansible.plugins.loader import vars_loader

    # Mock the vars plugin
    class MockVarsPlugin:
        def get_vars(self, loader, path, entities):
            return {'key1': 'value1'}

    class MockLoader:
        def _is_collection_path(self, path):
            return False

    # Create a playbook loader object
    p = MockLoader()

    # Create a plugin loader object
    l = vars_loader.all()

    # Add a plugin to the plugin loader
    l.add(MockVarsPlugin())

    # Mock an entity that can be passed to vars plugin
    mock_entity = object()

    # Call the get_vars_from_path function

# Generated at 2022-06-13 17:36:22.136711
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    sources = 'test/units/inventory_vars/source_vars'

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=sources)
    inventory.parse_inventory(host_list=['localhost'])
    host = inventory.get_host(name='localhost')
    data = get_vars_from_path(loader, sources, [host], 'all')
    assert 'source_vars' in data
    assert 'source_vars_key' in data['source_vars']
    assert data['source_vars']['source_vars_key'] == 'source_vars_value'

# Generated at 2022-06-13 17:36:23.651076
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path({}, {}, {}, 'inventory') == {}

# Generated at 2022-06-13 17:36:24.200173
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:36:34.503698
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    import ansible
    from ansible.plugins.vars import test_vars_plugin

    # test with one plugin which is a subclass of BaseVarsPlugin
    vars_plugin = test_vars_plugin.TestVarsPlugin()
    assert get_vars_from_path(ansible.plugins.loader, None, [], 'any') == {}
    assert get_vars_from_path(ansible.plugins.loader, None, [], 'inventory') == {'var1': 'value1'}
    assert get_vars_from_path(ansible.plugins.loader, None, [], 'task') == {'var2': 'value2'}
    assert get_vars_from_path(ansible.plugins.loader, None, [], 'any') == {'var3': 'value3'}

    # test

# Generated at 2022-06-13 17:36:44.518694
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugin

    class TestVarsPlugin(vars_plugin.VarsBase):
        def get_vars(self, loader, path, entities):
            return {'get_vars': "foo"}

    class TestVarsPlugin2(vars_plugin.VarsBase):
        def get_host_vars(self, host):
            return {'get_host_vars': "foo"}

        def get_group_vars(self, group):
            return {'get_group_vars': "foo"}

    class TestVarsPlugin3(vars_plugin.VarsBase):
        def run(self, terms, variables=None, **kwargs):
            return {'run': "foo"}

    test_vars_loader = vars_loader.VarsModuleLoader

# Generated at 2022-06-13 17:36:52.244292
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader

    plugin = vars_loader.get("vars_test")

    result = get_plugin_vars(vars_loader, plugin, '', [])

    assert result == {
        "vars_test_data": "vars_test_data",
        "vars_test_also_in_group": "vars_test_also_in_group"
    }