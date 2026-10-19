

# Generated at 2022-06-13 13:05:41.644395
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Create an instance of the plugin class.
    plugin = InventoryModule()

    # Create an instance of the AnsibleInventory class.
    inventory = AnsibleInventory("/fake/path", None)

    # Create an instance of the AnsibleDataLoader class.
    loader = AnsibleDataLoader()

    # Create an instance of the AnsiblePluginLoader class.
    plugin_loader = AnsiblePluginLoader()

    # Create an instance of the AnsibleDisplay class.
    display = AnsibleDisplay()

    # Create an instance of the AnsibleHost class.
    host = AnsibleHost("test_host")

    # Create an instance of the AnsibleInventoryGroup class.
    group = AnsibleInventoryGroup("test_group", None)

    # Set the class variables.
    plugin.inventory = inventory
    plugin.loader = loader
    plugin.plugin

# Generated at 2022-06-13 13:05:48.758429
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    yaml1 = InventoryModule()
    assert(yaml1.verify_file("testfile.yml"))
    assert(yaml1.verify_file("testfile.yaml"))
    assert(yaml1.verify_file("testfile.json"))
    assert(not yaml1.verify_file("testfile.txt"))

    yaml2 = InventoryModule()
    yaml2._options = {'yaml_extensions': ['.txt']}
    assert(yaml2.verify_file("testfile.txt"))
    assert(not yaml2.verify_file("testfile.yml"))


# Generated at 2022-06-13 13:05:57.453419
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    
    testobj = InventoryModule()
    
    # test 1: valid file extension
    testobj.b_set_options(dict(yaml_extensions=['.yml']))
    testobj.b_set_loader(MockLoader())
    assert testobj.verify_file('/some/path/to/a/file.yml') == True

    # test 2: invalid file extension
    testobj.b_set_options(dict(yaml_extensions=['.yml']))
    testobj.b_set_loader(MockLoader())
    assert testobj.verify_file('/some/path/to/a/file.txt') == False


# Generated at 2022-06-13 13:06:06.880896
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import yaml
    inventory_file = """
    localhost ansible_host=127.0.0.1
    """
    
    inventory_file_dict = yaml.safe_load(inventory_file)
    inventory = InventoryManager(loader=DataLoader(), sources=[inventory_file])
    inventory.add_group('all')
    src = ','.join(inventory.sources)
    plugin_options = [src]
    print(inventory)
    obj = InventoryModule()
    obj.parse(inventory, loader=DataLoader(), path=inventory_file, cache=True)
    print(inventory)
    print(inventory.groups)
    #assert inventory

# Generated at 2022-06-13 13:06:19.004802
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import inventory_loader

    DATA = {
        'all': {
            'hosts': ['test1', 'test2'],
            'vars': {},
            'children': {},
        },
    }

    loader = DataLoader()
    inv = inventory_loader.get('yaml', loader=loader)
    inv.set_options()

    # Test files with extension specified in option "yaml_extensions"
    yaml_exts = inv.get_option('yaml_extensions')
    for ext in yaml_exts:
        path = '/tmp/test_file_' + ext

# Generated at 2022-06-13 13:06:29.486122
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import sys
    import os
    import tempfile
    import shutil
    import json

    temp_directory = tempfile.mkdtemp()

# Generated at 2022-06-13 13:06:37.626531
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()
    print(inventory.verify_file('./test/test_plugins/test_inventory_plugins/yaml/test_1.yaml'))
    print(inventory.verify_file('./test/test_plugins/test_inventory_plugins/yaml/test_1.yml'))
    print(inventory.verify_file('./test/test_plugins/test_inventory_plugins/yaml/test_1.json'))
    print(inventory.verify_file('./test/test_plugins/test_inventory_plugins/yaml/test_1.txt'))

test_InventoryModule_verify_file()

# Generated at 2022-06-13 13:06:49.091001
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:07:01.465839
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import json
    from ansible.inventory.host import Host

    inv = InventoryModule()

# Generated at 2022-06-13 13:07:13.331270
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import tempfile
    import shutil
    import sys
    import io
    import os
    import io

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from lib.ansible.plugins.loader import InventoryLoader
    from lib.ansible.inventory.manager import InventoryManager
    from lib.ansible.plugins.inventory import yaml
    from lib.ansible.plugins.loader import add_all_plugin_dirs
    from lib.ansible.config.manager import ConfigManager


    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir,'test_inventorymodule_parse.yml')


# Generated at 2022-06-13 13:07:37.537892
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:07:50.803460
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    path = 'tests/modules/inventory/static/hosts.yaml'
    inventory = InventoryModule()
    inventory.parse(None, None, path)
    #print(inventory.get_hosts()[0].groups)
    assert inventory.get_hosts()[0].groups[1].name == 'first_group'
    assert inventory.get_hosts()[0].groups[1].vars['group_var'] == 'value'
    assert inventory.get_hosts()[0].groups[1].vars['group_var2'] == 'value2'
    assert inventory.get_hosts()[0].groups[1].children[0].name == 'other_group'
    assert inventory.get_hosts()[1].groups[1].name == 'other_group'

# Generated at 2022-06-13 13:07:59.603395
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """ Unit-test InventoryModule.parse() """

    # Import built-in Ansible modules in order to get the same ones
    # that Ansible uses
    import ansible.plugins.loader as plugins_loader
    import ansible.plugins.inventory.base as inventory_base
    import ansible.plugins.inventory.yaml as inventory_yaml

    # We need to initialize the loader in order to be able to import
    # the plugins
    plugins_loader.add_directory(os.path.join(os.path.dirname(__file__),
                                              os.path.pardir,
                                              os.path.pardir,
                                              'lib',
                                              'ansible',
                                              'plugins'))

    # Initialize BaseInventoryPlugin
    inventory_base.BaseInventoryPlugin()


# Generated at 2022-06-13 13:08:15.135176
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import os

    class MockInventory:

        def __init__(self):
            self.hosts = []
            self.groups = {}

        def add_host(self, host, group):
            self.hosts.append({'host': host, 'group': group})
            if group not in self.groups:
                self.groups[group] = []
            self.groups[group].append(host)

        def add_group(self, group):
            if group not in self.groups:
                self.groups[group] = []
            return group

        def add_child(self, group, sub_group):
            group = self.add_group(group)
            sub_group = self.add_group(sub_group)
            if group not in self.groups['all']:
                self.groups['all'].append

# Generated at 2022-06-13 13:08:28.001128
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.set_options()
    inv.parse(None, None, './lib/ansible/plugins/inventory/test_yaml_inventory.yaml')
    assert "test1" in inv.inventory.hosts
    assert "test1" in inv.inventory.groups["other_group"].hosts
    assert "test1" in inv.inventory.groups["last_group"].hosts
    assert "group_all_var" in inv.inventory.groups["all"].vars
    assert "group_all_var" in inv.inventory.groups["all"].vars
    assert "group_last_var" in inv.inventory.groups["last_group"].vars
    assert "group_x" in inv.inventory.groups["other_group"].children

# Generated at 2022-06-13 13:08:35.767296
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    '''
    Test for method verify_file of class InventoryModule
    '''
    # Parse result for a yaml file with .yml extension
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'test_inventory.yml')
    im = InventoryModule()
    result = im.verify_file(file_path)

    assert(result == True)

    # Parse result for a yaml file with .yaml extension
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'test_inventory.yaml')
    im = InventoryModule()
    result = im.verify_file(file_path)

    assert(result == True)

    # Par

# Generated at 2022-06-13 13:08:43.424541
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    handler = BaseFileInventoryPlugin()
    handler.set_options()
    handler.parse(None, None, 'tests/inventory-plugin/files/yaml_inventory_file1')
    handler.parse(None, None, 'tests/inventory-plugin/files/yaml_inventory_file2')
    handler.parse(None, None, 'tests/inventory-plugin/files/yaml_inventory_file3')
    handler.parse(None, None, 'tests/inventory-plugin/files/yaml_inventory_file4')


# Generated at 2022-06-13 13:08:56.376318
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create a dummy inv
    invfile = """TEST:
  hosts:
    test1:
    test2:
      host_var: value
  vars:
    group_all_var: value
  children:
    other_group:
      hosts:
        test4:
          ansible_host: 127.0.0.1
      children:
        group_x:
          hosts:
            test5:
        group_y:
          hosts:
            test6:
      vars:
        g2_var2: value3
    last_group:
      hosts:
        test1:
      vars:
        group_last_var: value
"""
    try:
        import yaml
    except ImportError:
        pyyaml_found = False

# Generated at 2022-06-13 13:09:02.633372
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # creating a plugin
    src = 'plugins/inventory/yaml/__init__.py'
    plugin = InventoryModule()

    # below is an example of one of the existing inventory files
    test_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../test/integration/inventory_samples/yaml_sample')
    with open(test_file_path, 'r') as f:
        test_file = f.read()

    test_file = test_file.replace('\\', '\\\\')

    # ansible.parsing.dataloader.DataLoader() to create an instance of the dataloader class
    test_loader = plugin.loader

    # ansible.parsing.yaml.objects.AnsibleMapping() to

# Generated at 2022-06-13 13:09:03.315637
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:09:21.307116
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class Obj:
        def __init__(self):
            self._data_cache = {}
    fake_loader = Obj()
    fake_loader._data_cache[1] = { '_ansible_inventory_script_vars': '' }
    inventory = Obj()
    inventory.loader = fake_loader
    inventory.groups = {}

    test_obj = InventoryModule()
    test_obj.parse(inventory, fake_loader, 1)


# Generated at 2022-06-13 13:09:33.707338
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = "all:\n  hosts:\n    test1:\n    test2:\n      host_var: value\n  vars:\n    group_all_var: value\n  children:\n    other_group:\n      children:\n        group_x:\n          hosts:\n            test5\n        group_y:\n          hosts:\n            test6\n      vars:\n        g2_var2: value3\n      hosts:\n        test4:\n          ansible_host: 127.0.0.1\n    last_group:\n      hosts:\n        test1\n      vars:\n        group_last_var: value\n"
    plugin = InventoryModule()
    plugin.parse(data)

# Generated at 2022-06-13 13:09:48.024184
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.parser = lambda self, inventory, loader, path, cache=True: None
    inv.get_option = lambda self, opt: None
    inv.set_options = lambda self: None
    inv.loader = MockLoader()

    inv.parse(None, None, None)

    inv.loader.data = ''
    try:
        inv.parse(None, None, None)
        assert False
    except AnsibleParserError:
        pass

    inv.loader.data = None
    try:
        inv.parse(None, None, None)
        assert False
    except AnsibleParserError:
        pass

    inv.loader.data = {}
    inv.parse(None, None, None)

    inv.loader.data = {'plugin': 'none'}

# Generated at 2022-06-13 13:09:51.170956
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()

    assert inv._parse_host('localhost:2000') == (['localhost'], 2000)
    assert inv._parse_host('localhost') == (['localhost'], None)

# Generated at 2022-06-13 13:10:03.516392
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.inventory import InventoryFile

    import yaml

    global_vars = yaml.safe_load('''
        plugin: yaml
        yaml_valid_extensions:
            - .yml
            - .yaml
    ''')
    inventory = InventoryFile(loader=None, sources=None, vault_password=None, global_vars=global_vars)
    inventory.subset('all')
    yaml_data = yaml.safe_load(EXAMPLES)
    plugin = InventoryModule()
    plugin.parse(inventory, loader=None, path=None, cache=False)
    # Method parse initializes inventory with the data from the TEST_EXAMPLES
    # So we can compare the contents of the inventory with the contents of yaml_data to
    # check if the data from

# Generated at 2022-06-13 13:10:07.629349
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 13:10:08.251472
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:10:12.677234
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory.verify_file = lambda x:True
    inventory.loader = DictDataLoader()
    inventory.set_options()

    inv_src = {"local": {"hosts": ["localhost"]}}
    inventory.parse(inventory, inventory.loader, path='src', cache=False, index_hosts=True)
    assert inventory.hosts['localhost'] == inv_src

# Generated at 2022-06-13 13:10:20.290942
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    This test is added to check the fix for issue ansible/ansible#54841

    Set yaml_valid_extensions = ['.yaml', '.yml', '.json'] in
    config file.

    Ansible will consider .json as a valid file for parsing YAML
    content.

    This testcase mainly checks whether parsing of .json file is
    as per YAML format.
    """
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    i = inventory_loader.get("yaml")
    d = DataLoader()

    class Inventory():
        def add_group(self, name):
            pass

        def set_variable(self, group, var, val):
            y[group][var] = val


# Generated at 2022-06-13 13:10:29.935384
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.plugins.loader import inventory_loader
    from ansible.inventory import Inventory
    from ansible.context import CLIContext
    from ansible.module_utils.six.moves import StringIO

    class FakeModule:
        def __init__(self, params):
            self.params = params
            self.args = {
                'fail_on_undefined_vars': True
            }

    class FakeCLI:
        def __init__(self):
            self.options = FakeModule({
                'ask_vault_pass': False,
                'ask_vault_pass_ask_pass': False
            })

    class FakeVaultLib:
        def __init__(self):
            self.secrets = ['password']
            self.secrets_mtime = [0]



# Generated at 2022-06-13 13:10:58.931469
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    yaml_extensions = ['.yaml']
    yaml_extensions_ans = ['.yaml']
    yaml_extensions_exp = ['.yaml']
    value = ''
    value_ans = ''
    value_exp = ''
    path = './test/test_yaml/test_yaml_inventory_1.yaml'
    path_ans = './test/test_yaml/test_yaml_inventory_1.yaml'
    path_exp = './test/test_yaml/test_yaml_inventory_1.yaml'
    verify_file_ans = True
    verify_file_exp = True
    super_verify_file_ans = True
    super_verify_file_exp = True
    # Calling the functions
    test_1 = InventoryModule()
   

# Generated at 2022-06-13 13:11:07.695256
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.plugins.inventory import InventoryModule
    root = os.path.split(os.path.dirname(__file__))[0]
    inventory_path = os.path.join(root + '/inventory')
    obj = InventoryModule()
    obj.set_options()
    assert (True == obj.verify_file(inventory_path + '/dynamic_inventory.json'))
    assert (True == obj.verify_file(inventory_path + '/dynamic_inventory.yml'))
    assert (True == obj.verify_file(inventory_path + '/dynamic_inventory.yaml'))
    assert (False == obj.verify_file(inventory_path + '/dynamic_inventory'))

# Generated at 2022-06-13 13:11:09.822348
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_module = InventoryModule()
    # Test case 1
    path = 'test_InventoryModule_parse_01.yaml'
    inventory_module.parse(None, None, path)


# Generated at 2022-06-13 13:11:11.974902
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import ansible.plugins.inventory.yaml
    inventory = ansible.plugins.inventory.yaml.InventoryModule()
    inventory._parse_host("host")

# Generated at 2022-06-13 13:11:21.147604
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    yaml_valid_extensions = ['.yaml', '.yml', '.json']

    # create valid json file
    json_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    json_file.write(EXAMPLES)
    json_file.close()

    # create valid yaml file
    yaml_file = tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False)
    yaml_file.write(EXAMPLES)
    yaml_file.close()

    # create invalid json file
    invalid_json_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)

# Generated at 2022-06-13 13:11:33.441066
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader

    myinv = inventory_loader.get("yaml", class_only=True)()

# Generated at 2022-06-13 13:11:39.821377
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    mod = InventoryModule()
    inv = mod.parse(EXAMPLES)
    assert inv['all']['hosts'] == ['test1', 'test2']
    assert inv['other_group']['hosts'] == ['test4']
    assert inv['other_group']['children'] == ['group_x', 'group_y']
    assert inv['group_x']['hosts'] == ['test5', 'test7']
    assert inv['last_group']['hosts'] == ['test1']
    assert inv['other_group']['vars']['g2_var2'] == "value3"

# TODO: add unit test for other functionalities

# Generated at 2022-06-13 13:11:52.064018
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.plugins.inventory import InventoryModule
    from ansible.errors import AnsibleError

    # parameters for test
    ext = []
    path = "/path/to/file"

    # mocks for test
    class Mock_super:
        def verify_file(self, path):
            return True
    import mock
    mock_super = Mock_super()
    m = mock.patch.object(InventoryModule, '_get_base_class', return_value=mock_super)
    m.start()
    # execute test
    inventory_module = InventoryModule()
    result = inventory_module.verify_file(path=path)
    # verify test results
    assert result is True
    # cleanup mocks
    m.stop()

# Generated at 2022-06-13 13:12:03.422763
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # initialize inventory object
    inventory = {}
    # initialize loader obj
    # ( cannot mock it as it needs a variable called inventory_loader )
    loader = None
    # initialize a inventory plugin object to test its methods
    plugin = InventoryModule()

    # unit test for parsing yaml file with invalid data
    # testcase 1 : data with no extension
    assert_exception(plugin, loader, inventory, "testfile", 'Parsed empty YAML file')

    # unit test for parsing yaml file with valid data
    # testcase 2 : data with valid extension
    assert_no_exception(
        plugin,
        loader,
        inventory,
        "testfile.valid.extension",
        'Parsed empty YAML file'
    )

    # unit test for parsing yaml file with invalid data
    # testcase 3 :

# Generated at 2022-06-13 13:12:17.602978
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory

    inv_yaml_str = '''
all:
  children:
    child1:
      hosts:
        host1:

'''
    inv_yaml_str_len = len(inv_yaml_str.split('\n'))
    inv_yaml_str_all_group_len = len(inv_yaml_str.split('\n')) - 1

    inv_loader = DataLoader()
    inv = Inventory(loader=inv_loader, variable_manager=None, host_list=None)

    yaml_obj = InventoryModule()

# Generated at 2022-06-13 13:13:11.020792
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Create and prepare a temporary file from the YAML data
    import tempfile
    import os

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(EXAMPLES)
    temp_file.close()

    def teardown():
        os.remove(temp_file.name)

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=os.path.basename(temp_file.name))
    plugin = InventoryModule()

# Generated at 2022-06-13 13:13:19.525672
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    class TestInventoryModule(InventoryModule):

        def __init__(self):
            self.loader = TestLoader()
            self.all = TestAllGroup()
            self.groups = {}
            self.hosts = {}

        def add_group(self, group):
            self.groups[group] = [group]
            return group

        def add_host(self, host, group=None):
            self.hosts[host] = host

        def add_child(self, group, subgroup):
            self.groups[group].append(subgroup)

        # We have to overwrite that method as it uses a display plugin
        def setup_loader(self):
            pass

        def set_variable(self, host, varname, value):
            pass


# Generated at 2022-06-13 13:13:29.229523
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''test_InventoryModule_parse'''

    # inventory.py requires that ansible.cfg be present.
    # use a temporary one
    ansible_cfg = tempfile.NamedTemporaryFile(mode='w', delete=False)
    with open('tests/inventory/ansible.cfg') as infile:
        ansible_cfg.write(infile.read())
    ansible_cfg.close()

    # if no groups are defined, ansible-inventory will print 'all'
    # since we are parsing (not generating) a file, we'll add the
    # group to the file
    group_name = 'all'
    inventory_file = NamedTemporaryFile(mode='w', delete=False)

# Generated at 2022-06-13 13:13:41.248026
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory_management/inventory/test_inventory_yaml'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    inventory.parse_sources(cache=False)
    assert inventory.list_hosts() == ['host1', 'host2', 'host3']
    assert inventory.list_groups() == ['group1', 'group2', 'all']
    assert variable_manager.get_vars()['group_all_var'] == 'hello'

# Generated at 2022-06-13 13:13:42.344788
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  inv = InventoryModule()
  inv.parse("", "", "", False)

# Generated at 2022-06-13 13:13:43.048861
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:13:54.287269
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin_settings = [
        {
            'name': 'yaml',
            'plugin_type': 'inventory',
            'path': '/bin/inventory/yaml.py'
        }
    ]
    env = [
        {
            'key': 'ANSIBLE_INVENTORY_PLUGIN_EXTS',
            'value': ['.yml', '.yaml']
        },
        {
            'key': 'ANSIBLE_YAML_FILENAME_EXT',
            'value': ['.yml', '.yaml']
        }
    ]

    inv_m = InventoryModule()
    inv_m.plugin_settings = plugin_settings
    inv_m.YAML_EXTENSIONS = ('.yml', '.yaml')
    inv_m.file_name = "hosts.yaml"

# Generated at 2022-06-13 13:14:05.378899
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import json
    import os
    import sys
    import unittest

    TEST_INVENTORY = os.path.dirname(__file__) + '/../../../../plugins/inventory/test/unit/data/inventory.yaml'

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught
        by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught
        by the test case"""
        pass


# Generated at 2022-06-13 13:14:15.741351
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    '''
    Making sure that file verification works as expected
    '''

    data = '''
all:
    hosts:
        test1:
        test2:
            host_var: value
    vars:
        group_all_var: value
    children:
        other_group:
            children:
                group_x:
                    hosts:
                        test5
                group_y:
                    hosts:
                        test6:
            vars:
                g2_var2: value3
            hosts:
                test4:
                    ansible_host: 127.0.0.1
        last_group:
            hosts:
                test1
            vars:
                group_last_var: value
'''


# Generated at 2022-06-13 13:14:16.293135
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert False