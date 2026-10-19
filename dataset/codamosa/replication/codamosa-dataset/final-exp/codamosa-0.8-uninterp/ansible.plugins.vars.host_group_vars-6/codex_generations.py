

# Generated at 2022-06-13 15:17:43.693309
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from collections import namedtuple

    # Mock objects
    class MockLoader:
        def __init__(self):
            pass

        def file_name_is_valid(self, filename):
            return True

        def find_vars_files(self, path, vault_password=None, check_file_ext=True):
            return ['/data/group_vars/test_gvars', '/data/host_vars/test_hvars']

        def load_from_file(self, filepath, cache=True, unsafe=False):
            return {}

    class MockHost:
        def __init__(self):
            self.name = 'test_host'

    class MockGroup:
        def __init__(self):
            self.name = 'test_group'


# Generated at 2022-06-13 15:17:52.878816
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    #Create a Variable manager and a mock_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from collections import namedtuple
    from units.mock.loader import DictDataLoader
    v = VariableManager()
    loader = DictDataLoader({})
    v.set_inventory(InventoryManager(loader=loader, sources=[]))

    #Initalize stubs
    Group = namedtuple('Group', ['name'])
    Host = namedtuple('Host', ['name'])
    entity = Host(name="test_host")
    #Load vars
    basedir = os.path.realpath("test/units/plugins/test_host_group_vars")
   

# Generated at 2022-06-13 15:18:02.225403
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from unittest import TestCase

    class MockLoader(object):
        def __init__(self):
            self.returned_data = {}
            self.called_files = []

        def find_vars_files(self, path, entity):
            self.called_files.append([path, entity])
            return ['file1.yaml']

        def load_from_file(self, file, cache=True, unsafe=True):
            self.called_files.append(file)
            return self.returned_data

    class MockDisplay(object):
        def __init__(self):
            self.debug_calls = []

        def debug(self, msg):
            self.debug_calls.append(msg)

        def warning(self, msg):
            self.debug_calls.append(msg)

   

# Generated at 2022-06-13 15:18:08.264982
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Set up test case
    vars_module = VarsModule()
    vars_module._display = DummyDisplay()
    vars_module._options = DummyOptions()
    vars_module._basedir = '/tmp'

    loader = DummyLoader(
        '/tmp/host_vars/localhost.yml',
        'localhost',
        {'vars_host': 'localhost'}
    )

    host = Host(name='localhost')
    entities = [host]

    # Exercise the method
    data = vars_module.get_vars(loader, '/tmp', entities)

    # Evaluate results
    assert {'vars_host': 'localhost'} == data


# Generated at 2022-06-13 15:18:17.524412
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Define a fake class for simulating the Host class in the inventory file.
    class KnownHost(object):
        def __init__(self, host_name, port, ansible_host, ansible_port):
            self.name = host_name
            self.port = port
            self.vars = {}
            self.vars['ansible_host'] = ansible_host
            self.vars['ansible_port'] = ansible_port

    class TestVarsModule(VarsModule):
        def get_vars(self, loader, path, entities, cache=True):
            super(TestVarsModule, self).get_vars(loader, path, entities, cache)

    # If the host_name is not valid, the test_VarsModule_get_vars() method will raise AnsibleParserError
    #

# Generated at 2022-06-13 15:18:28.261813
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    VarsModule.REQUIRES_WHITELIST = False

    def test_data(entities, result, basedir):
        vm = VarsModule()

        class DummyLoader:
            def find_vars_files(self, opath, entity_name):
                return [os.path.join(opath, f) for f in os.listdir(opath) if f.endswith('foo1')]

            def load_from_file(self, filename, cache=True, unsafe=True):
                return {}

        assert vm.get_vars(DummyLoader(), '', entities, basedir) == result

    test_data([Host('test1')],
              {'test1': {}},
              'test_dir')


# Generated at 2022-06-13 15:18:33.003328
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    module = VarsModule()
    assert module.get_vars(None, None, []) == {}
    assert module.get_vars(None, None, [1]) == {}
    assert module.get_vars(None, None, ['test_host']) == {}

# Generated at 2022-06-13 15:18:41.821125
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
    For testing purposes, the class has to be instantiated without the
    configuration argument, which is necessary when using it as a vars plugin.
    '''

    basedir = os.path.join(os.path.dirname(__file__), 'test_data', 'vars_plugin')

    vars_modules = VarsModule(c=None, basedir=basedir)

    test_hosts = ['test-host']
    test_groups = ['test-group']

    for test_host in test_hosts:
        host = Host(name=test_host)
        vars_modules.get_vars(loader=None, path='/tmp/', entities=host, cache=False)
        assert test_host in FOUND


# Generated at 2022-06-13 15:18:44.676125
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars_module = VarsModule()
    data_1 = {'test_key_1': 'test_value_1'}
    return_value = vars_module.get_vars("", "", [Host("test_1"), Host("test_2")])
    assert return_value == data_1

# Generated at 2022-06-13 15:18:54.725706
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """Unit testing for VarsModule._get_vars"""

    from ansible.constants import __version__ as VERSION
    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import vars_loader

    # Obtain data
    data = {'host_vars': {}, 'group_vars': {}}
    data['host_vars']['blah.test1'] = {'test1':'test1'}
    data['host_vars']['blah.test2'] = {'test2':'test2'}
    data['host_vars']['blah.test3'] = {'test3':'test3'}
    data['group_vars']['all'] = {'test4':'test4'}

    # Mock loader
   

# Generated at 2022-06-13 15:18:59.486324
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    assert False, "Test not implemented"

# Generated at 2022-06-13 15:19:09.442167
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    class DummyHost:
        def __init__(self):
            self.name = 'foo'

    class DummyGroup:
        def __init__(self):
            self.name = 'bar'

    class DummyOptions:
        whitelist_external_plugins = []

    class DummyDisplay:
        verbosity = 0

        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

    class DummyVaultSecretStub:
        def __init__(self, password):
            pass

        def decrypt(self, encrypted_data):
            return encrypted_data

    class DummyVaultAESWithFernet:
        def __init__(self, password):
            pass

        def decrypt(self, encrypted_data):
            import fernet
            return fernet.Fern

# Generated at 2022-06-13 15:19:09.929699
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    pass

# Generated at 2022-06-13 15:19:20.522122
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """
    Test function get_vars of class VarsModule
    """
    VarsModule._display = mock.MagicMock()
    VarsModule._vault = mock.MagicMock()
    VarsModule._get_file_vault_secret = mock.MagicMock()

    # First test case : when entities is not a list
    vars_module = VarsModule()
    loader = _loader()
    path = "test_dir/test_dir1"
    entities = "test_entity"
    cache = True

    with pytest.raises(AnsibleParserError):
        vars_module.get_vars(loader, path, entities, cache)
    VarsModule._vault.assert_not_called()
    VarsModule._get_file_vault_secret.assert_not_called()



# Generated at 2022-06-13 15:19:28.016168
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader
    module = VarsModule()
    loader = vars_loader.get("file")

    class TestHost(Host):
        def __init__(self, hostname):
            self.name = hostname

    data = module.get_vars(loader, '', TestHost('hostname'))
    assert data == {}

    data = module.get_vars(loader, '', TestHost('hostname'), cache=False)
    assert data == {}

    class TestGroup(Group):
        def __init__(self, groupname):
            self.name = groupname

    data = module.get_vars(loader, '', TestGroup('groupname'))
    assert data == {}


# Generated at 2022-06-13 15:19:33.639233
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    path = '.'
    loader = 'AnsibleFileLoader()'
    entities = Group('name')
    cache = True
    # test with Group entities
    assert VarsModule.get_vars(VarsModule(), loader, path, entities, cache) == {}
    # test with Host entities
    host = Host(name='hostname')
    assert VarsModule.get_vars(VarsModule(), loader, path, host, cache) == {}

# Generated at 2022-06-13 15:19:42.036985
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.vault import VaultLib
    from ansible.vars import VariableManager

    from ansible.plugins.loader import vars_loader

    class DummyVaultSecret:
        def __init__(self, password):
            self.password = password
            self.id = None

    class DummyDataLoader:
        def __init__(self):
            self.paths = []

        def set_basedir(self, basedir):
            self.basedir = basedir

        def add_path(self, path):
            self.paths.append(path)

        def get_basedir(self):
            return self.basedir

        def path_exists(self, path):
            return True

       

# Generated at 2022-06-13 15:19:48.017010
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
   Method VarsModule.get_vars is called when an inventory source is parsed
    '''
    module = VarsModule()
    h = Host("localhost")
    module.get_vars(None, None, h)
    module.get_vars(None, None, [h])



# Generated at 2022-06-13 15:19:58.564636
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    entities = []
    entity = Host("test", port=None)
    entities.append(entity)
    entity = Host("/test", port=None)
    entities.append(entity)
    entity = Group("test", port=None)
    entities.append(entity)
    entity = Group("/test", port=None)
    entities.append(entity)
    host_vars = {}
    host_vars["test"] = {}
    host_vars["test"]["a"] = "b"
    group_vars = {}
    group_vars["test"] = {}
    group_vars["test"]["a"] = "b"
    from ansible.parsing.dataloader import DataLoader
    dataloader = DataLoader()
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 15:20:07.610708
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Create a moke ansible.plugins.loader.VarsModule object
    mock_VarsModule = VarsModule()
    mock_VarsModule.get_vars = VarsModule.get_vars
    mock_VarsModule._display = type('', (), dict(debug=print))
    mock_VarsModule._basedir = "./test/host_group_vars"
    # Create a moke ansible.parsing.loader.DataLoader object

# Generated at 2022-06-13 15:20:18.973070
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible_collections.ansible.community.plugins.module_utils.common.collections_loader import AnsibleCollectionLoader
    import ansible.plugins.inventory.script as script

    data = """
        [all]
        foo
    """

    # create the class object
    obj = VarsModule()

    # We are just testing the method get_vars
    # So method get_vars needs a class object of type BaseInventoryPlugin
    # class BaseInventoryPlugin will be instantiated using the code
    # cls = BaseInventoryPlugin.load(class_name, path, config, base_vars )
    # This will return the class object if class_name=script._loaders[0]
    # path=None
    # config=None
    # base_vars=None
    # The above will create a class object

# Generated at 2022-06-13 15:20:26.866354
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # arrange
    text = '---\ntest: 1\n'
    loader = AnsibleLoader(text)
    path = '/Users/chg/ansible/ansible/lib/ansible/plugins/vars/host_group_vars.py'
    entities = [Host(name='hostname')]
    cache = True

    # act
    vars = VarsModule().get_vars(loader, path, entities, cache)

    # assert
    assert vars['test'] == 1

# Generated at 2022-06-13 15:20:31.686896
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Arrange
    entity_name = 'test_entity_1'
    group_vars_dir_name = 'group_vars'
    host_vars_dir_name = 'host_vars'
    plugin_dir = __file__[:__file__.rfind('/')]
    plugin_basedir = to_bytes(plugin_dir[:plugin_dir.rfind('/')])
    test_file_1_content = b'---\nplugin_test_var_1: test_value_1'
    test_file_2_content = b'---\nplugin_test_var_2: test_value_2'


# Generated at 2022-06-13 15:20:42.418257
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    v = VarsModule()
    host = Host(name='localhost')
    loader = DictDataLoader()
    # Good data
    path = 'fixtures/groupvars'
    host.vars = v.get_vars(loader, path, host)
    assert host.vars == {'tomcat_port': 8080, 'tomcat_ssl_port': 8443, 'tomcat_ajp_port': 8009}
    # No data
    path = 'fixtures/empty'
    host.vars = v.get_vars(loader, path, host)
    assert host.vars == {}
    # No such dir
    path = 'fixtures/nosuchdir'
    host.vars = v.get_vars(loader, path, host)
    assert host.vars == {}
    # Not

# Generated at 2022-06-13 15:20:51.919623
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    plugin = VarsModule(play_context=play_context, inventory=inventory, variable_manager=variable_manager)
    plugin._display.verbosity = 0
    
    res = plugin.get_vars(loader, '', 'localhost')
    assert res
    assert res['groups']['all'][0] == 'localhost'

# Generated at 2022-06-13 15:21:00.434522
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader

    if PY3:
        unicode = str

    loader = DataLoader()
    variables = VarsModule()
    variables._basedir = u'.'
    base_dir = to_bytes(unicode(u'.'))
    fake_host = type('object', (object,), dict(name='testhost'))
    fake_group = type('object', (object,), dict(name='testgroup'))
    fake_host_entity = fake_host()
    fake_group_entity = fake_group()

    assert variables.get_vars(loader, base_dir, entities=fake_host_entity) == {}

# Generated at 2022-06-13 15:21:09.125123
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """
    Test method get_vars of class VarsModule.
    """
    # Create test context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import vars_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    # Create host with name
    test_host = Host(name="test_host")
    test_group = Group(name="test_group")
    # Create inventory with test host
    inventory = InventoryManager(loader=DataLoader(), sources=None)
    inventory.hosts = [test_host]
    inventory.groups = [test_group]
    # Create plugin

# Generated at 2022-06-13 15:21:16.529908
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    fake_loader = "fake_loader"
    fake_path = "/fake/path"
    fake_entities = []
    v = VarsModule()
    r = v.get_vars(fake_loader, fake_path, fake_entities)
    assert r == {}
    fake_entities = [Host('localhost', 'localhost', vars={'ansible_connection': 'local'})]
    r = v.get_vars(fake_loader, fake_path, fake_entities)
    assert r == {}

# Generated at 2022-06-13 15:21:25.363390
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    #
    # TESTS
    #
    # Load an empty inventory and check the vars are loaded in the right places
    host = Host("testhost", groups=["testgroup"])
    group = Group("testgroup")

    test_module = VarsModule()
    test_module.get_vars(None, "", host)
    test_module.get_vars(None, "", group)

    # TODO: Fix this
    # # Load an inventory with a vars file in host_vars/ in the same directory as the inventory
    # test_env = EnvironmentVars()
    # test_module = VarsModule()
    # test_module.get_vars(None, "./test/unit/inventory/host_vars/", host)

    # # Load an inventory with a vars file in group_v

# Generated at 2022-06-13 15:21:29.406164
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """
    :return:
    """
    # Initialization
    # Setup test environment
    # Test get_vars of VarsModule
    # Clean up test environment
    # Verify results

    # Initialization
    # Setup test environment
    # Test get_vars of VarsModule
    # Clean up test environment
    # Verify results

# Generated at 2022-06-13 15:21:48.928932
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.vault import VaultLib

    vault_pass = "MyVaultPassword"
    vault_secret = VaultLib(vault_pass)

    # host-specific vars
    host_vars_file_path = "tests/vars_plugins/test_0_host_vars/host_vars/test_0_host_vars.yml"
    host_vars = {"test_0_host_var": "host var value"}
    host_vars_file_content = vault_secret.encrypt(host_vars)
    host_vars_file = StringIO(host_vars_file_content)
   

# Generated at 2022-06-13 15:21:56.389241
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import VaultLib

    vault_pass = 'test'
    vault = VaultLib([('default', vault_pass)])

    groupvars_dir = 'test/group_vars/'
    hostvars_dir = 'test/host_vars/'
    basedir = '.'
    # create group_vars/ dir
    os.makedirs(os.path.join(basedir, groupvars_dir))
    # create host_vars/ dir
    os.makedirs(os.path.join(basedir, hostvars_dir))
    # create group_vars/vault/ dir

# Generated at 2022-06-13 15:22:03.491372
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    loader_mock = MagicMock()
    loader_mock.find_vars_files.return_value = ['host_vars/host1.yml', 'host_vars/host2.yml']
    plugin = VarsModule(basedir[0])
    plugin.get_vars(loader_mock, '', entities)
    assert loader_mock.find_vars_files.called

# Generated at 2022-06-13 15:22:06.712530
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule() 
    host = Host()
    host.name = "test"
    path = "/path/to/inventory"
    entities = [host]
    assert plugin.get_vars(None, path, entities) == {}

# Generated at 2022-06-13 15:22:11.260540
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Arrange
    basedir = os.getcwd()
    entities = [Host("test.test")]
    VarsModule.stage = 'first'

    # Act
    instance = VarsModule()
    result = instance.get_vars(None, basedir, entities, False)

    # Assert
    assert result == {'test.test': {'var1': 'var1'}}

# Generated at 2022-06-13 15:22:14.055345
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    loader = FakeDataLoader()
    path = b'/non/existent'
    plugin_name = 'host_group_vars'
    vars_mgr = VarsModule()
    vars_mgr.get_vars(loader, path, [], cache=True)
    assert len(FOUND.keys()) > 0
    assert plugin_name in FOUND.keys()[0]
    for key in FOUND:
        assert key == FOUND.keys()[0]



# Generated at 2022-06-13 15:22:22.265132
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # create a mocked ansible.inventory.host.Host object
    class MockHost(Host):
        def __init__(self, name):
            self.name = name

    # create a mocked ansible.inventory.group.Group object
    class MockGroup(Group):
        def __init__(self, name):
            self.name = name

    # create a mocked ansible.plugins.loader.VarsModule object
    class MockLoader(object):

        def find_vars_files(self, path, entities):
            return ['%s/%s.yml' % (path, entity)
                    for entity in entities if entity == 'mock_host']

        def load_from_file(self, found, cache=True, unsafe=True):
            return {'mock_host_var': 1}

    # create a mocked ansible

# Generated at 2022-06-13 15:22:24.581905
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader
    m = VarsModule()
    data = m.get_vars(vars_loader, '', [Host(name='test1')])
    assert 'test1' in data
    assert data['test1'] == 'test2'



# Generated at 2022-06-13 15:22:34.201292
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    def _mock_display(msg, *args, **kwargs):
        assert msg

    def mock_Host(name):
        host = Host(name)
        # The _options dict is MagicMock because the version of mock installed on EL6 doesn't have a
        # spec_set attribute (not sure why)
        type(host)._options = MagicMock(return_value=MagicMock(spec_set=dict))
        return host

    def _mock_entity(name, cls, return_value=None):
        entity = cls(name)
        type(entity)._options = MagicMock(return_value=MagicMock(spec_set=dict))
        return entity


# Generated at 2022-06-13 15:22:40.508563
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Setup test
    data = "Some string data"
    loader = {
        'load_from_file': lambda x, cache, unsafe: data
    }

    host_name = 'test'
    host = {
        'name': host_name,
        'get_groups': lambda: []
    }

    entities = [host]

    # Setup inventory dir
    C.DEFAULT_HOST_LIST = './test/integration/inventory'

    # Get vars
    vars_plugin = VarsModule()
    result = vars_plugin.get_vars(loader, '', entities)

    # Assert
    assert result == {host_name: data}, 'Wrong host vars were parsed'


# Generated at 2022-06-13 15:22:59.914839
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    import os
    import sys
    import unittest

    class MockHost():
        name = "host1"

    class MockGroup():
        name = "group1"

    class MockLoader():
        def __init__(self, tmp_folder):
            self.tmp_folder = tmp_folder

        def find_vars_files(self, basedir, entity_name):
            if entity_name == "host1" or entity_name == "group1":
                return ["project1_host_group_vars_host1.yml", "project1_host_group_vars_group1.yml"]
            elif entity_name == "host2" or entity_name == "group2":
                return []
            else:
                return []


# Generated at 2022-06-13 15:23:09.437586
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import mock
    import os.path
    import ansible.plugins.vars.host_group_vars

    class MockModule(object):
        def __init__(self):
            self.params = [{'var1': 'value1', 'var2': 'value2'}, {'var2': 'value2override'}, {'var3': 'value3'}]
            self.args = ['test', 'test']

    loader = mock.MagicMock()
    path = os.path.split(os.path.realpath(__file__))[0]
    #default test inventory
    inventory = os.path.join(path, 'hosts')
    #current unittest file
    loader.get_basedir.return_value = path
    #find_plugin_vars_files mock
    loader.find_

# Generated at 2022-06-13 15:23:18.197331
# Unit test for method get_vars of class VarsModule

# Generated at 2022-06-13 15:23:26.129197
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    print("\n" + "Module " + __name__ + " unit test" + "\n")

    import sys
    import inspect

    import ansible.utils.vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    class Object(object):

        def __init__(self, d):
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                   setattr(self, a, [Object(x) if isinstance(x, dict) else x for x in b])
                else:
                   setattr(self, a, Object(b) if isinstance(b, dict) else b)


# Generated at 2022-06-13 15:23:33.467982
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    test_plugin_instance = VarsModule()
    test_loader_instance = MockLoader()
    test_path = '/path/to/inventory'
    test_entities = [MockHost()]
    test_cache = False
    FOUND.clear()
    test_plugin_instance.get_vars(test_loader_instance, test_path, test_entities, test_cache)


# mock class allowing to test get_vars method of class VarsModule

# Generated at 2022-06-13 15:23:39.417583
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 15:23:49.743676
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # use a real file/dir tree (rather than mocking)
    # TODO: test alternative basedir
    basedir = os.path.join(C.DEFAULT_LOCAL_TMP, 'ansible_vars_plugin_test')
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    os.mkdir(os.path.join(basedir, 'group_vars'))
    os.mkdir(os.path.join(basedir, 'host_vars'))
    vars_file = os.path.join(basedir, 'group_vars', 'somegroup')
    with open(vars_file, 'wt') as f:
        f.write('groupvar: 42\n')

# Generated at 2022-06-13 15:23:59.033283
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.vars.host_group_vars import VarsModule
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.parsing.dataloader import DataLoader
    add_all_plugin_dirs()
    add_all_plugin_dirs(C.DEFAULT_INVENTORY_PLUGIN_PATH, C.DEFAULT_INVENTORY_PLUGIN_PATH)
    loader = DataLoader()
    vm = VarsModule()
    
    host_entity = Host("host_name", groups=["host_group"])
    group_entity = Group("group_name")
    host_data = vm.get_vars(loader, "", host_entity)

# Generated at 2022-06-13 15:24:03.342406
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.vars.host_group_vars

    class Entity():
        def __init__(self,name):
            self.name = name

    loader = ansible.plugins.vars.host_group_vars.VarsModule()
    # Test 1
    entities = Entity('localhost')
    retval = loader.get_vars(loader, '/path', entities)
    assert retval == {}, "Invalid return value of method get_vars"

# Generated at 2022-06-13 15:24:10.378676
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    module = VarsModule()

# Generated at 2022-06-13 15:24:41.705302
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    data = {}
    _basedir = os.path.join(os.path.dirname(__file__), 'data')
    loader = MockLoader()
    vars_module = VarsModule()

    # load vars
    b_opath = os.path.realpath(to_bytes(_basedir))
    opath = to_text(b_opath)
    found_files = []
    key = '%s.%s' % ('test_host', opath)
    if 'host_vars' in os.path.join(b_opath, 'host_vars'):
        found_files = loader.find_vars_files(os.path.join(opath, 'host_vars'), 'test_host')
        FOUND[key] = found_files
    for found in found_files:
        new_

# Generated at 2022-06-13 15:24:49.902936
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''Unit test for get_vars method of VarsModule'''
    test_VarsModule = VarsModule()
    entities = [Host('test')]
    loader = BaseVarsPlugin()
    test_VarsModule.get_vars(loader, 'test_path', entities)
    assert entities == [Host('test')]
    with pytest.raises(AnsibleParserError):
        test_VarsModule.get_vars(loader, 'test_path', 'not a list')


if __name__ == '__main__':
    test_VarsModule_get_vars()

# Generated at 2022-06-13 15:24:50.510735
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    VarsModule()

# Generated at 2022-06-13 15:24:57.869256
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    ansible_vault.rekey()

    source_base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_var_plugins_data')

    host_vars_path = os.path.join(source_base_path, 'host_vars')
    group_vars_path = os.path.join(source_base_path, 'group_vars')

    secure_path = os.path.join(source_base_path, 'ansible_vault')

    # setup
    host1 = Host(name='test1')
    group1 = Group(name='group1')

    inventory = Inventory(loader=C.DEFAULT_INVENTORY_LOADER)
    inventory.add_group(group1)


# Generated at 2022-06-13 15:25:09.127902
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    import os

    basedir="test/vars-plugin/inventory/host_group_vars/test_vars_plugin"
    vars_plugin_stagedir="test/vars-plugin/inventory/host_group_vars/test_vars_plugin/stage"

    # test the get_vars method of the VarsModule class
    os.environ['ANSIBLE_VARS_PLUGIN_STAGE'] = 'stage'
    os.environ['ANSIBLE_YAML_FILENAME_EXT'] = 'json'

    # set up an inventory object
    inventory=Inventory('test/vars-plugin/inventory/host_group_vars/test_vars_plugin/hosts')

    # set up the object to test against

# Generated at 2022-06-13 15:25:19.475792
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """Check get_vars method of VarsModule plugin class"""
    import pytest
    from ansible.plugins.vars.host_group_vars import VarsModule
    basedir = "/path/to/basedir"
    # We don't mock os functions, but we test on fixture directory created
    # by makefile in this repository
    b_basedir = to_bytes(basedir, errors='surrogate_or_strict')
    os.chdir(os.path.join(b_basedir, b"plugin_tests/host_group_vars/files"))
    loader = DictDataLoader({})
    inventory = Inventory("host_vars=host_vars group_vars=group_vars")
    vm = VarsModule()
    vm._basedir = basedir
    # 1) test for host,

# Generated at 2022-06-13 15:25:21.417461
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    VarsModule().get_vars(loader, path, entities, cache=True)
    VarsModule().get_vars(loader, path, entities, cache=True)

# Generated at 2022-06-13 15:25:30.310279
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    test_data_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test/integration/vars_plugins/data/'))
    entities = []
    host = Host(name='localhost', port=22)
    entities.append(host)
    vars_module_obj = VarsModule()
    data_loader_obj = DataLoader()

    vars_manager_obj = VariableManager()
    vars_module_obj._display = lambda x: None
    vars_module_obj._basedir = to_bytes(os.path.realpath(test_data_dir))
    vars_module_

# Generated at 2022-06-13 15:25:40.497385
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    ut_host = Host('host')
    ut_group = Group('group')
    ut_basedir = os.path.join(os.getcwd(), 'inventory')
    ut_path = os.path.join(ut_basedir, 'hosts')
    ut_vars_module = VarsModule()
    ut_vars_module._basedir = ut_basedir
    ut_vars_module._display = C.display
    ut_data = ut_vars_module.get_vars(loader, ut_path, [ut_host, ut_group], cache=True)
    assert ut_data['host'] == {'host_var_group': 'host_var_group_val', 'host_var': 'host_var_val'}

# Generated at 2022-06-13 15:25:50.603663
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import pytest, json, yaml

    basedir = "./test/unit/plugins/vars/test_vars_module"
    inventory_file = os.path.join(basedir, "inventory")

# Generated at 2022-06-13 15:26:44.574750
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    class Host:
        name = ""

    class Group:
        name = ""

    class Loader:
        def __init__(self):
            self.module_vars = {}

        def get_basedir(self):
            return self._basedir

        def load_from_file(self, path, cache=True, unsafe=True):
           return

        def find_vars_files(self, path, entity):
           return

    class Display:
        def display(self, src):
            print(src)

        def verbose(self):
            return True

        def warning(self, src):
            print(src)

        def debug(self, src):
            print(src)

    class TestVarsModule(VarsModule):
        def __init__(self):
            self._loader = Loader()
            self

# Generated at 2022-06-13 15:26:47.757223
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    varsModule = VarsModule()

    assert(varsModule.get_vars(None, None, None) == {})
    assert(varsModule.get_vars(None, None, []) == {})

# Generated at 2022-06-13 15:26:55.342175
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
  # Stub variables
  loader = None
  path = "path"
  entities = [Host("localhost")]
  cache = True

  # Stub methods
  class VarsModuleMock(VarsModule):
    def __init__(self):
      self.subdir = 'host_vars'

    def get_vars(self, loader, path, entities, cache=True):
      super(VarsModuleMock, self).get_vars(loader, path, entities, cache)

  # Create mock object for VarsModule class
  varsModule = VarsModuleMock()

  # Unit test get_vars method
  varsModule.get_vars(loader, path, entities, cache)

# Generated at 2022-06-13 15:27:05.384350
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    #Override some Ansible config/env variables for this unit test
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    os.environ[C.DEFAULT_ROLES_PATH] = temp_dir.name
    os.environ[C.DEFAULT_ROLES_PATH] = to_text(os.getcwd())
    os.environ[C.DEFAULT_ROLES_PATH] = to_text('tests/test_data/roles')
    os.environ[C.DEFAULT_HOST_LIST] = to_text('tests/test_data/inventory/base')
    os.environ[C.DEFAULT_HOST_LIST] = to_text('tests/test_data/inventory/hosts')
    os.environ[C.DEFAULT_HOST_LIST]

# Generated at 2022-06-13 15:27:10.001634
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    test_entities = ['test_host1', 'test_host2']
    test_basedir = './test_dir'
    varsModule = VarsModule()
    varsModule.get_vars(None, test_basedir, test_entities)


# Generated at 2022-06-13 15:27:20.636076
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    loader =  FakeVarsLoader()
    module = VarsModule()
    module._basedir = os.path.realpath(__file__)
    path = os.path.join(module._basedir, "data_hosts_and_groups")
    cache = False

    # get_vars for host
    host = FakeHost("host1", "host_vars/host1.yaml")
    host_vars = module.get_vars(loader, path, host, cache)
    assert host_vars == {'host_var1': 'host1', 'inventory_hostname_short': 'host1', 'inventory_hostname': 'host1'}

    # get_vars for group
    group = FakeGroup("group1", "group_vars/group1.yml")
    group_vars = module

# Generated at 2022-06-13 15:27:21.611061
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    v = VarsModule()
    # What to test

    pass

# Generated at 2022-06-13 15:27:25.763009
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''Unit test for method get_vars of class VarsModule.'''
    pLoader = VarsModule()
    path = 'tests/inventory/group_vars/group1'
    groups = [Group(name='group1')]
    data = pLoader.get_vars(loader=None, path=path, entities=groups, cache=True)
    assert data == {'var1': 'p1'}

# Generated at 2022-06-13 15:27:35.279618
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock
    from ansible_collections.ansible.community.tests.unit.plugins.loader import DictDataLoader

    path = os.path.join(os.path.dirname(__file__), 'test_vars_plugin_get_vars')
    fake_basedir = os.path.join(path, 'basedir')

    fake_loader = DictDataLoader({path: {}})

    vm = VarsModule()

    # Test with a Host
    host = Host(name='testhost')
    vm.get_vars(fake_loader, path, host)