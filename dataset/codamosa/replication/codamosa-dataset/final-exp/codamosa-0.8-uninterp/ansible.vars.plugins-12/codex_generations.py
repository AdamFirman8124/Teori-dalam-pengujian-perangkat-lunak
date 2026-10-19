

# Generated at 2022-06-13 17:28:49.949036
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class TestVarsPlugin:
        def get_vars(self, loader, path, entities, cache=True):
            return {
                'a': {
                    'b': 'c'
                }
            }

    loader = None
    plugin = TestVarsPlugin()
    path = None
    entities = []
    expected = {
        'a': {
            'b': 'c'
        }
    }
    actual = get_plugin_vars(loader, plugin, path, entities)
    assert actual == expected

# Generated at 2022-06-13 17:28:57.566719
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class fake_loader:
        class fake_plugin:
            _load_name = 'fake_plugin'
            _original_path = 'fake/path'
            def get_vars(self, loader, path, entities):
                return {'fake_plugin': True}
        fake_plugin_class = fake_plugin

    class fake_loader_2:
        class fake_plugin:
            _load_name = 'fake_plugin'
            _original_path = 'fake/path'
            def get_host_vars(self, host_name):
                return {'fake_plugin': True}
        fake_plugin_class = fake_plugin

    class fake_loader_3:
        class fake_plugin:
            _load_name = 'fake_plugin'
            _original_path = 'fake/path'

# Generated at 2022-06-13 17:29:07.633783
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader

    # C.VARIABLE_PLUGINS_ENABLED is emptied before this test.
    assert len(C.VARIABLE_PLUGINS_ENABLED) == 0

    # vars_plugin_list should be empty here.
    vars_plugin_list = list(vars_loader.all())
    assert len(vars_plugin_list) == 0

    # Append some vars plugins to vars_plugin_list.
    vars_plugin_list.append(vars_loader.get('group_vars'))
    vars_plugin_list.append(vars_loader.get('host_vars'))

    # vars_plugin_list should have the appended vars plugins.
    assert len(vars_plugin_list)

# Generated at 2022-06-13 17:29:14.056557
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_plugin = None
    test_plugin_list = [
        {'plugin': test_plugin, 'path': '', 'entities': [], 'expected': {'some_key': 'some_value'}},
        {'plugin': test_plugin, 'path': '', 'entities': [], 'expected': {'some_key': 'some_value'}},
    ]

    for test in test_plugin_list:
        actual = get_vars_from_path(test['loader'], test['path'], test['entities'], test['stage'])
        assert actual == test['expected']

# Generated at 2022-06-13 17:29:24.253641
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.vars import AutoTestVars
    from ansible.inventory.manager import InventoryManager
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'plugins', 'test_vars_plugin')
    # test vars plugin
    vars_loader.add(AutoTestVars(path))
    # set up inventory object
    inv_dir = os.path.dirname(__file__)
    inventory_path = os.path.join(inv_dir, 'vars_files/ansible.cfg')

# Generated at 2022-06-13 17:29:30.589470
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    plugin = "plugin_plugin.py"
    loader = AnsibleCollectionRef.get_plugin_loader(plugin)
    path = "/path/to/plugin"
    entity = [ {'name': 'localhost'} ]

    try:
        data = get_plugin_vars(loader, plugin, path, entity)
    except AttributeError:
        pass


# Generated at 2022-06-13 17:29:36.205612
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    class MyPlugin:
        def get_vars(self, loader, path, entities):
            return {'a': 1}

    loader = MyPlugin()
    path = '/foo/bar'
    entities = [ 'ansible', 'bad' ]
    stage = 'inventory'

    data = get_vars_from_path(loader, path, entities, stage)

    assert data == {'a': 1}


# Generated at 2022-06-13 17:29:47.716149
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    test_vars_loader = vars_loader.all()
    test_vars_loader[0]._load_name = 'makedirs'
    test_vars_loader[1]._load_name = 'os'
    test_vars_loader[2]._load_name = 'template'
    test_vars_loader[3]._load_name = 'win_environment'
    test_vars_loader[4]._load_name = 'win_file_version'
    test_vars_loader[5]._load_name = 'win_owner'
    test_vars_loader[6]._load_name = 'win_package'
    test_vars_loader[7]._load_name = 'win_ping'

# Generated at 2022-06-13 17:29:53.666554
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars.plugin import VarsBasePlugin
    from ansible.vars.manager import VariableManager

    # Create test plugin
    class VarsPlugin(VarsBasePlugin):
        class VarsModule:
            def get_vars(self, loader, path, entities):
                return {'a': 'b'}


    # Create test loader object
    class FakeVarsLoader:
        def __init__(self, return_object):
            self.return_object = return_object

        def get(self, name, *args, **kwargs):
            return self.return_object

    # Create test entity object
    class FakeVarsEntity(object):
        def __init__(self, name):
            self.name = name

    # Create test data
    fake_vars_entity = FakeVarsEntity

# Generated at 2022-06-13 17:29:58.224314
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import plugin_loader


    data = {}
    plugin = plugin_loader.get('yaml')
    loader = None
    path = '/some/path'
    entities = ['john']

    if plugin is None:
        raise AnsibleError("Invalid vars plugin %s from" % (plugin._load_name))

    data = get_plugin_vars(loader, plugin, path, entities)

# Generated at 2022-06-13 17:30:03.616518
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:30:07.623373
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = {}
    path = './test/test_vars_plugin.py'
    host = Host(name='localhost')
    entities = [host]
    test_data = get_vars_from_path(loader, path, entities, 'inventory')
    assert test_data['foo'] == 'bar'
    assert test_data['baz'] == 'qux'

# Generated at 2022-06-13 17:30:18.083816
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.vars_plugins.yaml import VarsModule as VarsModule_yaml
    from ansible.vars.vars_plugins.vault import VarsModule as VarsModule_vault

    class DummyVarsModule(object):
        def get_vars(self, loader, path, entities):
            return {'dummy': 'vars'}

    class DummyVarsModule_raise(object):
        def get_vars(self, loader, path, entities):
            raise AttributeError

    class DummyVarsModule_raise_no_call(object):
        pass

    class DummyVarsModule_raise_call(object):
        def get_vars(self, loader, path, entities):
            raise AttributeError

   

# Generated at 2022-06-13 17:30:24.599752
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=None, host_list='/dev/null')
    sources = ['/etc/ansible/hosts', '/etc/ansible/group_vars']
    entities = [Database('db'), WebServer('web')]
    stage = 'inventory'
    data = get_vars_from_inventory_sources(loader, sources, entities, stage)
    assert(data)

# Generated at 2022-06-13 17:30:35.751785
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugins
    test_dict = {
        'vars_plugins.test': {
            'get_vars': {
                'path': 'test/data/test_vars_plugins/vars_plugin_test/',
                'entities': [],
                'expected': {
                    'all': {
                        'test_var': "var 1"
                    }
                }
            }
        },
        'vars_plugins.test2': {
            'get_host_vars': {
                'host': 'localhost',
                'expected': {
                    'localhost': {
                        'test_var': "var 2"
                    }
                }
            }
        }
    }

# Generated at 2022-06-13 17:30:43.804539
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory import Inventory

    i = Inventory(loader=None, variable_manager=None, host_list="localhost")

    loader = i._loader
    entities = i.entries
    stage = 'inventory'

    data = get_vars_from_path(loader, 'tests/vars_plugins', entities, stage)

    assert data == {u'a': 1, u'b': 2, u'c': 3, u'd': 4, u'z': 26, u'x': 24, u'y': 25, u'hostvars_test': u"ok"}

# Generated at 2022-06-13 17:30:44.376107
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:30:51.536883
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    class MockPlugin:
        def get_vars(self, loader, path, entities):
            return {"a": 1, "b": 2}

    class MockPlugin2:
        def get_group_vars(self, group):
            return {"c": 3, "d": 4}

    class MockPlugin3:
        def get_host_vars(self, host):
            return {"e": 5, "f": 6}

    class MockPlugin4:
        def get_vars(self, loader, path, entities):
            return {"g": 7, "h": 8}

    class MockLoader:
        def __init__(self, data):
            self.data = data

    class MockHost:
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 17:30:59.183453
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible.plugins.loader
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.plugins.dynamic_inventory import InventoryScript

    # load the data from the dynamic inventory plugin
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=None,
                          source="../../contrib/inventory/test/test.dyn")
    # retrieve all hostnames from the inventory for testing
    hostnames = [h.name for h in inventory.get_hosts(recurse=True)]
    # get the host objects for the hosts
    hosts = [inventory.get_host(h) for h in hostnames]
    # create an InventoryScript object

# Generated at 2022-06-13 17:31:05.034328
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    category = 'all'

    # Define a fake inventory source which will be used as source of variable
    fake_inventory_source = 'inventories/inventory_source'

    # Create fake dummy data in file system so that we can test
    # We create a file named as fake inventory source
    with open(fake_inventory_source, 'w') as f:
        f.write("[web]\nlocalhost ansible_connection=local")
    # We create a path for the variable file
    path_to_var_file = os.path.join(os.path.dirname(fake_inventory_source), 'group_vars', 'all')
    # We create a variable file for all variables

# Generated at 2022-06-13 17:31:19.115095
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    inventory_data = [
        u"all:",
        u"  vars:",
        u"    group_var: group_var_value",
        u"",
        u"group:",
        u"  vars:",
        u"    group_var2: group_var2_value",
        u"",
        u"host:",
        u"  vars:",
        u"    host_var: host_var_value",
        u"    host_var2: host_var2_value",
    ]

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host


# Generated at 2022-06-13 17:31:26.806989
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import mock
    import os

    inv_loader = mock.Mock()
    plugin = mock.Mock()
    entities = [mock.Mock()]
    plugin._load_name='test_plugin'
    plugin._original_path='test_path'
    C.VARIABLE_PLUGINS_ENABLED=['test_plugin']
    with mock.patch('ansible.plugins.loader.vars_loader.all') as vars_loader_all:
        with mock.patch('ansible.plugins.loader.vars_loader.get') as vars_loader_get:
            vars_loader_all.return_value=[plugin]
            vars_loader_get.return_value=plugin

# Generated at 2022-06-13 17:31:37.272995
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host

    loader = DataLoader()

    # Get plugin vars for single host and group
    host = Host('hostname', {})
    group = Host('groupname', {})
    path_host = '/path/to/host'
    path_group = '/path/to/group'

    vars_host = {
        'valid_host_vars_key_1': 'valid_host_vars_value_1',
        'valid_host_vars_key_2': 'valid_host_vars_value_2',
    }

# Generated at 2022-06-13 17:31:38.083425
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:31:46.149156
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import vars_plugin

    class vars_plugin_test(vars_plugin):

        class TestException(Exception):
            pass

        def __init__(self):
            super(vars_plugin_test, self).__init__()

        def get_vars(self, loader, path, entities, cache=True):
            return {'test_get_vars_check': True}

        def get_group_vars(self, group):
            return {'test_get_group_vars_check': True}

        def get_host_vars(self, host):
            return {'test_get_host_vars_check': True}

        def raise_exception(self):
            raise self.TestException

    test_instance = vars_plugin_test()


# Generated at 2022-06-13 17:31:46.614801
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:31:56.746262
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # filename is path to an invalid inventory, but we don't care
    # since this test just tests getting vars from a path
    inv_mgr = InventoryManager(loader, ['contrib/inventory/test_inventory.yml'])
    inv_mgr.parse_sources()
    vars_from_path = get_vars_from_path(loader, 'contrib/inventory/test_inventory.yml', inv_mgr.hosts.values(), 'inventory')
    assert vars_from_path == {}

# Generated at 2022-06-13 17:32:06.035762
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory import Inventory
    from ansible.plugins.loader import vars_loader

    # Test vars plugin
    class TestVarsPlugin:
        """
        Test vars plugin that supports both v2 and v1 API
        """
        class VarsModule(object):
            def __init__(self, datadir=None):
                self.datadir = datadir

            def get_vars(self, path, entities):
                if self.datadir is not None:
                    return {'test_vars_plugin_key': self.datadir}
                else:
                    return {'test_vars_plugin_key': path}

        class VarsModuleV1(object):
            def __init__(self, datadir=None):
                self.datadir = datadir


# Generated at 2022-06-13 17:32:08.861468
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader_mock = None
    path_mock = None
    entities_mock = None
    stage_mock = None
    data = get_vars_from_path(loader_mock, path_mock, entities_mock, stage_mock)
    assert data
    assert isinstance(data, dict)


# Generated at 2022-06-13 17:32:12.848437
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.loader import vars_loader

    data = {}
    loader = None
    path = "/home/user/ansible/playbooks"
    entities = []
    stage = None
    data = get_vars_from_path(loader, path, entities, stage)
    print(data)



# Generated at 2022-06-13 17:32:25.758462
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    from ansible.plugins import vars_loader
    vars_plugin_list = list(vars_loader.all())
    test_plugin = vars_plugin_list[0]
    test_plugin.get_vars = lambda x, y, z: {'test': "test_value"}
    test_data = get_vars_from_path(None, None, None, None)
    assert test_data == {'test': "test_value"}

# Generated at 2022-06-13 17:32:36.637667
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    def test_vars_get_vars(self, items):
        return {'test': 1}

    def test_vars_get_group_vars(self, items):
        return {'test_group': 1}

    def test_vars_get_host_vars(self, items):
        return {'test_host': 1}

    test_vars = type('TestVars', (object, ),
                     {'get_vars': test_vars_get_vars,
                      'get_host_vars': test_vars_get_host_vars,
                      'get_group_vars': test_vars_get_group_vars})

    loader = None
    path = 'test/path'
    entities = [Host('localhost')]

    data = get_plugin_vars

# Generated at 2022-06-13 17:32:37.953915
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass

# Generated at 2022-06-13 17:32:43.154971
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    '''
    Unit test for function get_vars_from_path
    :return:
    '''
    from ansible.parsing.yaml import objects

    result = get_vars_from_path(None, '/tmp/test', None, None)
    assert result == objects.AnsibleVars()

    class MockLoader:
        def get(self, _):
            return None

    loader = MockLoader()

    result = get_vars_from_path(loader, '/tmp/test', None, None)
    assert result == objects.AnsibleVars()



# Generated at 2022-06-13 17:32:52.563448
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = 'test'
    path = 'hosts/host_vars/local'
    entities = ["test_entity"]
    stage = 'inventory'

    # test: valid plugin
    plugin = 'ansible.plugins.vars.host_vars.HostVars'

    # test: get_host_vars
    class MockedHostVars(object):
        def get_host_vars(self, host):
            return {host: {'key': 'value'}}

    # test: get_group_vars
    class MockedGroupVars(object):
        def get_group_vars(self, group):
            return {group: {'key': 'value'}}

    vars_plugin_list = list(vars_loader.all())

# Generated at 2022-06-13 17:33:02.390499
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import json

    CWD = os.path.dirname(os.path.realpath(__file__))
    os.environ['ANSIBLE_CONFIG'] = os.path.join(CWD, 'test_config', 'ansible.cfg')
    from ansible.plugins.loader import vars_loader

    vars_plugin_list = list(vars_loader.all())
    for plugin in vars_plugin_list:
        if plugin._load_name not in C.VARIABLE_PLUGINS_ENABLED and getattr(plugin, 'REQUIRES_WHITELIST', False):
            # 2.x plugins shipped with ansible should require whitelisting, older or non shipped should load automatically
            continue

# Generated at 2022-06-13 17:33:03.477366
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # Note: This function is tested in test_plugin_loader
    pass

# Generated at 2022-06-13 17:33:12.187020
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 17:33:18.064648
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugins.vars import vars_plugins
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.utils.vars import combine_vars
    import os


# Generated at 2022-06-13 17:33:30.338047
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    cnstr = PlayContext()
    varmgr = VariableManager(loader=None, inventory=None, variable_manager=None, loader_cache=None, cnstr=cnstr)

    # Make sure that the get_vars_from_path() is working
    assert get_vars_from_path(varmgr.loader, './ansible/plugins/vars', None, None)

    var1 = get_vars_from_path(varmgr, './ansible/plugins/vars', None, None)

# Generated at 2022-06-13 17:33:44.905787
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import test_vars_plugin

    loader = C.DEFAULT_LOADER_CLASS()
    plugin = test_vars_plugin.TestVarsPlugin()
    path = '/something/somewhere'
    entities = [Host('test_host'), Host('test_host2')]
    vars = get_plugin_vars(loader, plugin, path, entities)
    assert vars['foo'] == 'bar'
    assert vars['bar'] == 'foo'

# Generated at 2022-06-13 17:33:51.126291
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = "/root/ansible_test/inventory/test_hosts"
    entities = [Host(name='test_host')]
    stage = 'task'
    plugin_list = vars_loader.all()
    plugin_name_list = C.VARIABLE_PLUGINS_ENABLED
    plugin_name_list_len = len(C.VARIABLE_PLUGINS_ENABLED)
    plugin_list_len = len(plugin_list)
    for i in range (plugin_list_len):
        plugin = plugin_list[i]

# Generated at 2022-06-13 17:34:01.209123
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    mock_vars_loader = FakeVarsLoader({'fake': FakeVarsPlugin, 'fake_host': FakeHostVarsPlugin, 'fake_group': FakeGroupVarsPlugin})
    with mock_vars_loader.mock_plugin('fake') as plugin:
        plugin._return_value = {'key': 1}
        assert get_vars_from_path(None, 'path', [], 'inventory') == {'key': 1}

    with mock_vars_loader.mock_plugin('fake_host') as plugin:
        plugin._return_value = {'key': 1}
        assert get_vars_from_path(None, 'path', [Host('test')], 'inventory') == {'key': 1}
        plugin._return_value = {'key': 2}
        assert get_vars_from_

# Generated at 2022-06-13 17:34:12.090122
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # To run this unit test, change the line above to:
    #   if False:
    from ansible.module_utils.six.moves.urllib.parse import quote
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    # Hack a plugin into the loader that returns a magic name
    #
    # This is the simplest vars plugin possible
    from ansible.plugins.vars import BaseVarsPlugin
    class MyMagicPlugin(BaseVarsPlugin):
        pass

    # Make sure the plugin is enabled
    C.VARIABLE_PLUGINS_ENABLED = [quote(MyMagicPlugin.__name__, safe='')]

    # Create a loader to get the plugin
    loader = None
   

# Generated at 2022-06-13 17:34:20.959689
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    def fake_plugin():

        class _plugin(object):

            def __init__(self):
                self._loaded = True
                self._original_path = 'foo'
                self._load_name = 'bar'

            def get_vars(self, loader, path, entities):
                return {'foo': path}

        return _plugin()

    from ansible.plugins.loader import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    im = InventoryManager(loader, 'hosts', [], False)
    play = Play()
    play.hosts = 'all'
    vars_plugin = fake_plugin()
    vars_loader._shared_loader_obj.module_finder.add_plugin(vars_plugin)
    assert get_vars_

# Generated at 2022-06-13 17:34:21.481090
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    pass



# Generated at 2022-06-13 17:34:27.393516
# Unit test for function get_vars_from_path
def test_get_vars_from_path():

    class DummyVarsModule():
        def __init__(self, name):
            self._name = name
        def get_vars(self, loader, path, entities):
            return {'var' + self._name: path}

    from ansible.plugins.loader import path_dwim, plugin_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    all_var_plugins = [DummyVarsModule('1'), DummyVarsModule('2')]

    def get_vars_plugin(self, name):
        for plugin in all_var_plugins:
            if plugin._name == name:
                return plugin


# Generated at 2022-06-13 17:34:35.990904
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    loader = None
    sources = [
        '../../../contrib/inventory/foo.file.ini',
        '../../../contrib/inventory/bar.ini',
        '../../../contrib/inventory/baz.yaml',
        '../../../contrib/inventory/bar.yaml',
        '../../../contrib/inventory/bar.yml',
        '../../../contrib/inventory/not_a_dir',
    ]
    hosts = [
        Host('host1'),
        Host('host2'),
        Host('host3'),
        Host('host4'),
        Host('host5'),
        Host('host6'),
        Host('host7'),
        Host('host8'),
    ]
    stage = 'task'

# Generated at 2022-06-13 17:34:41.451306
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())
    plugin_name = vars_plugin_list[0]._load_name
    plugin = vars_plugin_list[0]
    data = get_plugin_vars("loader", plugin, "/home/", "entities")
    assert data is not None

# Generated at 2022-06-13 17:34:44.417646
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = MockVarsPlugins()
    path = "test_path"
    entities = []
    stage = "test_stage"

    assert get_vars_from_path(loader, path, entities, stage) == {}


# Generated at 2022-06-13 17:35:06.094572
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    vars_plugin_list = list(vars_loader.all())
    vars_plugin_list.append(vars_plugin_list[0])
    vars_loader.all_plugins = vars_plugin_list
    vars_loader._all = [vars_loader.all_plugins[0]._load_name, vars_loader.all_plugins[1]._load_name]
    data = get_vars_from_path(None, None, None, None)
    assert isinstance(data, dict)


# Generated at 2022-06-13 17:35:07.303026
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass



# Generated at 2022-06-13 17:35:12.521115
# Unit test for function get_plugin_vars
def test_get_plugin_vars():

    class VarsPlugin(object):

        def get_vars(self, loader, path, entities):
            return {'foo': 'bar', 'baz': 'bat'}

    loader = object()
    entities = object()

    plugin = VarsPlugin()
    result = get_plugin_vars(loader, plugin, 'foo', entities)
    assert result == {'foo': 'bar', 'baz': 'bat'}



# Generated at 2022-06-13 17:35:20.610545
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import os
    import sys
    import tempfile
    import tox
    import ansible.utils.collection_loader
    import ansible.plugins.loader
    import ansible.utils.vars
    import ansible.utils.display

    sys.path.insert(0, os.path.dirname(os.path.dirname(tox.__file__)))

    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class Diplay(object):
        DEBUG = False

    ansible.utils.display.Display = Diplay

    class DummyPlugin(object):
        def __init__(self, config):
            self

# Generated at 2022-06-13 17:35:28.138271
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    import ansible_collections.sensu.sensu_go.plugins.module_utils.sensu_common
    from ansible_collections.sensu.sensu_go.plugins.module_utils.sensu_common import SensuCommon
    import ansible.plugins.loader
    from ansible.plugins.loader import vars_loader
    from ansible.vars import combine_vars
    import ansible.utils.vars
    #import ansible.plugins.vars
    #from ansible.plugins.vars import BaseVarsPlugin
    test_base_path = "/Users/leo7044/Projects/ansible-ben/test/unit/ansible/plugins/vars"

# Generated at 2022-06-13 17:35:37.721959
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.plugin.vars import BaseVarsPlugin
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.data import InventoryData
    from ansible.inventory.group import Group

    class TestVarsPlugin(BaseVarsPlugin):
        pass

    vars_loader.add(TestVarsPlugin, 'test')

    # Test hostvars
    inventory = InventoryData()
    inventory.add_host(Host(name="testhost"))
    entities = [inventory.get_host("testhost")]
    path = "path/to/dir"

    plugin = TestVarsPlugin()
    plugin.get_host_vars = lambda *args: {'host_vars_test': args}

# Generated at 2022-06-13 17:35:47.111279
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():
    import ansible.cli.playbook
    import ansible.inventory.manager

    # Setup
    opts = ansible.cli.playbook.PlaybookCLI._parse_cli_opts([])
    loader = ansible.cli.CLI.setup_loader(opts)
    inv_manager = ansible.inventory.manager.InventoryManager(loader, sources=["tests/inventory/inventory_vars_plugins"])
    inv = inv_manager.inventory

    # Test group vars
    group_vars_data = get_vars_from_inventory_sources(loader, inv_manager.sources, [inv.groups['group_for_tests']], 'inventory')
    assert group_vars_data == {'group_var': 1}

    # Test group vars with names
    group_vars_data = get

# Generated at 2022-06-13 17:35:50.239849
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    loader = None
    path = './'
    entities = None
    stage = 'task'

    vars_from_path = get_vars_from_path(loader, path, entities, stage)

    assert isinstance(vars_from_path, dict)

# Generated at 2022-06-13 17:35:51.474588
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    assert get_vars_from_path(None, '.', [], 'inventory') == {}

# Generated at 2022-06-13 17:35:51.883405
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    pass

# Generated at 2022-06-13 17:36:25.910374
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    '''
    Test function get_vars_from_path.
    This function calls get_vars()
    '''
    # TODO
    pass

# Generated at 2022-06-13 17:36:33.873762
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.config.manager import ConfigManager
    from ansible.inventory.manager import InventoryManager
    config = ConfigManager()
    inventory = InventoryManager(loader=None, sources=config.get_plugin_paths('my_test_inventory'))
    entities = inventory.get_groups_dict().keys()
    # test_vars_path is a test vars plugin
    data = get_vars_from_path(inventory.loader, "test/units/plugins/vars/test_vars_path", entities, "task")
    assert data == {'test_number': 42}

# Generated at 2022-06-13 17:36:44.350868
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    # test for vars plugin
    import ansible.plugins.vars.vars_plugin as vars_plugin
    vars_plugin.VarsModule = vars_plugin.VarsModule

    from ansible.plugins.loader import vars_loader
    plugin = vars_loader.get('vars_plugin')

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    # test for v1 vars plugins
    class VarsV1(object):
        def __init__(self, *args, **kwargs):
            self._load_name = "vars_v1"
            self._original_path = "vars_v1"

        def get_vars(self, loader, path, entities):
            return {}

    vars_v1 = VarsV1()

# Generated at 2022-06-13 17:36:55.020451
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    display.verbosity = 4

    def plugin_mock(module_path=None):
        class vars:
            _original_path = module_path
            _load_name = 'name'
            def get_vars(self, loader, path, entities):
                return {'name': 'vars'}
        return vars

    loader = vars_loader
    loader.all = lambda: [plugin_mock('/var/lib/a/b/c')]
    path = '/var/lib/a/b/c/d'
    inventory_hosts = [Host('a')]

    assert get_vars_from_path(loader, path, inventory_hosts, '') == {'name': 'vars'}



# Generated at 2022-06-13 17:37:03.796378
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.loader import vars_loader

    plugin = vars_loader.get('yaml_file')
    plugin._load_name = 'yaml_file'
    plugin._original_path = os.path.join(os.path.dirname(__file__), '__init__.py')
    plugin.path = os.path.join(os.path.dirname(__file__), '__init__.py')
    plugin.get_vars.__func__.__code__ = os.path.join(os.path.dirname(__file__), '__init__.py').__code__
    plugin.get_group_vars.__func__.__code__ = os.path.join(os.path.dirname(__file__), '__init__.py').__code__

# Generated at 2022-06-13 17:37:09.318618
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    loader = AnsibleCollectionLoader()

    # Setup inventory and ansible.cfg
    i = InventoryManager(loader=loader, sources=['localhost,'])
    i.parse_sources()

    data = get_vars_from_path(loader, './', i.hosts.values(), 'inventory')
    # First plugin, basic_vars, will generate a dictionary with this data
    assert "ansible_play_hosts" in data and data["ansible_play_hosts"] == [u'127.0.0.1']
    data = get_vars_from_path(loader, './', i.hosts.values(), 'task')
    # Second plugin, non-task-specific, will generate empty dictionary

# Generated at 2022-06-13 17:37:15.073615
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    ''' unittest for function get_vars_from_path '''
    from ansible.plugins import vars_loader

    class TestVarPlugin:
        def get_vars(self, loader, path, entities):
            #return {'vars': 'test'}
            return {'vars': 'test'}

    test_var_plugin = TestVarPlugin()
    vars_loader._all.append(test_var_plugin)
    test_path = '/path/to/dir'
    test_entities = ('a','b','c','d')
    test_stage = 'stage'
    test_data = get_vars_from_path(None, test_path, test_entities, test_stage)

# Generated at 2022-06-13 17:37:15.901012
# Unit test for function get_vars_from_path
def test_get_vars_from_path():
    pass


# Generated at 2022-06-13 17:37:25.540171
# Unit test for function get_vars_from_inventory_sources
def test_get_vars_from_inventory_sources():

    class TestCollectionLoader(object):

        def __init__(self):
            self.collections = dict()

        def get(self, name):
            if name in self.collections:
                return self.collections[name]
            return None

        def all(self):
            return self.collections.values()

    class TestInventorySource(object):

        def __init__(self, path):
            self.path = path

        def get_host_list(self):
            if ',' in self.path:
                return self.path.split(',')
            return self.path

    class Test_Vars_Plugin_v1(object):

        def __init__(self):
            self.run = "Vars_Plugin_v1"


# Generated at 2022-06-13 17:37:33.579965
# Unit test for function get_plugin_vars
def test_get_plugin_vars():
    from ansible.plugins.vars import BaseVarsPlugin, VarsModule
    test_data_vars_path = os.path.join(os.path.dirname(__file__), 'test_data/vars')

    class testvars_BaseVarsPlugin(BaseVarsPlugin):
        def get_vars(self, loader, path, entities, cache=True):
            return {'foo': 'bar'}

    class testvars_VarsModule(VarsModule):
        def get_vars(self, loader, path, entities, cache=True):
            return {'foo': 'bar'}

    dummy_loader = type('DummyLoader', (), {})

    # BaseVarsPlugin