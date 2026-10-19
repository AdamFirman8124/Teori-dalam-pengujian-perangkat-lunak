

# Generated at 2022-06-13 13:05:40.998532
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()

# Generated at 2022-06-13 13:05:48.060626
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    extensions = ['.yaml', '.json']
    plugin = InventoryModule()
    plugin.set_options(extensions)
    assert plugin.verify_file('/etc/ansible/hosts') == False
    assert plugin.verify_file('/etc/ansible/hosts.yaml') == True
    assert plugin.verify_file('/etc/ansible/hosts.yml') == True
    assert plugin.verify_file('/etc/ansible/hosts.json') == True
    assert plugin.verify_file('/etc/ansible/hosts.txt') == False


# Generated at 2022-06-13 13:05:48.610539
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 13:05:52.909335
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    yaml_extensions = ['.yaml', '.yml', '.json']

    assert plugin.verify_file('/foo/bar.yaml', yaml_extensions)
    assert plugin.verify_file('/foo/bar.yml', yaml_extensions)
    assert plugin.verify_file('/foo/bar.json', yaml_extensions)

# Generated at 2022-06-13 13:06:01.784102
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """Unit test for method parse of class InventoryModule"""
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()
    from ansible.plugins.inventory import InventoryModule
    import os
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures',
                                'inventory_yaml_parse.yml')
    inv = InventoryModule()
    inv.parse(fixture_path, loader=None, cache=False)

# Generated at 2022-06-13 13:06:09.667315
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Given
    inventory_module = InventoryModule()
    path = os.path.join(os.path.dirname(__file__), "test_yaml_inventory.yml")

    # When/Then
    try:
        assert inventory_module.verify_file(path)
    except:
        assert False, "Exception found while verifying file"

if __name__ == '__main__':
    test_InventoryModule_verify_file()

# Generated at 2022-06-13 13:06:12.540140
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_InventoryModule = InventoryModule()
    test_InventoryModule.parse(None, None, None, True)

# Generated at 2022-06-13 13:06:21.194469
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = {'plugin': 'yaml'}
    data = '''
    foo:
        hosts:
          foo1:
          foo2:
          foo3:
        vars:
          var1: value1
          var2: value2
        children:
            bar:
                hosts:
                    bar1:
                        foo_var1: value3
                    bar2:
                    bar3:
        '''

    class MockFileLoader:

        def load_from_file(self, path, cache=True):
            return data

    class MockInventory:

        def __init__(self):
            self.groups = {}

        def add_group(self, group):
            self.groups[group] = MockGroup(group, self)
            return self.groups[group]


# Generated at 2022-06-13 13:06:32.184363
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    im = InventoryModule()
    im.set_options()
    # case with no extension is valid
    assert(im.verify_file('/path/to/file') == True)
    # case with an extension that is valid is valid
    assert(im.verify_file('/path/to/file.json') == True)
    # case with an extension that is not valid is invalid
    assert(im.verify_file('/path/to/file.txt') == False)
    # case with an extension that is valid but not in lower case is valid
    assert(im.verify_file('/path/to/file.YAML') == True)

    # case with an extension that is valid and in upper case is valid
    im.set_option('yaml_extensions', ['.YAML'])

# Generated at 2022-06-13 13:06:44.052142
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:07:00.501576
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    assert inv.verify_file('test.a') == False
    assert inv.verify_file('test.yaml') == True
    assert inv.verify_file('test.bogus') == False
    assert inv.verify_file('test.yml') == True
    assert inv.verify_file('test.json') == True

    inv.set_options({'yaml_extensions': ['.bogus', '.yaml']})
    assert inv.verify_file('test.a') == False
    assert inv.verify_file('test.yaml') == True

# Generated at 2022-06-13 13:07:12.431765
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    plugin = InventoryModule()

    class MockInventory:

        class MockGroup:

            def __init__(self):
                pass

            def add_child(self, child):
                return child

        def add_group(self, group_name):
            if group_name not in groups:
                groups[group_name] = self.MockGroup()
                print(group_name, 'not in groups')
            return groups[group_name]

        def add_host(self, host_name, group):
            if host_name not in hosts:
                hosts[host_name] = group

        def set_variable(self, group, var, val):
            if group not in vars:
                vars[group] = {}
            vars[group][var] = val

    #example
    example = {}

# Generated at 2022-06-13 13:07:19.064378
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['examples/hosts'])
    plugin = InventoryModule()
    assert plugin.verify_file('examples/hosts')
    assert plugin.verify_file('examples/hosts.yaml')
    assert plugin.verify_file('examples/hosts.yml')
    assert plugin.verify_file('examples/hosts.json')
    assert not plugin.verify_file('examples/hosts.py')



# Generated at 2022-06-13 13:07:29.941911
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    '''test if file exists'''
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.inventory import BaseFileInventoryPlugin
    from io import StringIO

    path = './test.yml'
    loader = DataLoader()
    myobject = BaseFileInventoryPlugin()
    myobject.loader = loader

    with open(path, 'w') as f:
        f.write(StringIO(EXAMPLES).getvalue())

    value = myobject.verify_file(path)
    os.remove(path)
    assert value



# Generated at 2022-06-13 13:07:40.453391
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # ansible/plugins/inventory/yaml.py
    # class InventoryModule(BaseFileInventoryPlugin)
    # method parse(self, inventory, loader, path, cache=True)

    #
    # Initialize objects
    #

    import ansible.plugins.inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()   # DataLoader()

    # InventoryModule()
    inventory_dir_path = os.path.dirname(ansible.plugins.inventory.__file__)
    module_path = os.path.join(inventory_dir_path, "yaml.py")
    inventory_module = imp.load_source('inventory_module', module_path)
    inventory_module_obj = inventory_module.InventoryModule()

    # create a Mock object for inventory.
    inventory

# Generated at 2022-06-13 13:07:52.980588
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_config = {
        "plugin": "yaml",
        "strict": False,
        "groups": {
            "ungrouped": {
                "vars": {
                    "ansible_connection": "local"
                }
            }
        }
    }

# Generated at 2022-06-13 13:07:57.917096
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
  inventory_module = InventoryModule()
  yaml_extensions = ['.yaml', '.json']
  inventory_module.set_options(dict(yaml_extensions=yaml_extensions))
  assert inventory_module.verify_file("file.yaml") is True
  assert inventory_module.verify_file("file.json") is True
  assert inventory_module.verify_file("file.yml") is False


# Generated at 2022-06-13 13:08:09.007762
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  import sys
  import tempfile
  import yaml

  # Create a temporary temporary file and write data to it.

# Generated at 2022-06-13 13:08:18.408586
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    namespace = 'ns1'
    ini_key = 'yaml_extensions'
    config_data = dict()
    check_ini_key = True
    check_env_key = True
    env_key = [
        'ANSIBLE_YAML_FILENAME_EXT',
        'ANSIBLE_INVENTORY_PLUGIN_EXTS',
    ]
    config_data['plugin_name'] = ['yaml']
    config_data['defaults'] = {ini_key : ['.yaml', '.yml', '.json']}
    config_data[namespace] = {ini_key : ['.yaml', '.yml', '.json']}
    config_data['defaults']['inventory_plugins'] = ','.join(config_data['plugin_name'])

# Generated at 2022-06-13 13:08:24.837175
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    """Unit test for verify_file method of InventoryModule class."""
    config = {'yaml_extensions': ['.yaml']}
    assert not InventoryModule().verify_file("testfile.yml", config)
    assert InventoryModule().verify_file("testfile.yaml", config)
    assert not InventoryModule().verify_file("testfile.ini", config)

# Generated at 2022-06-13 13:08:49.088870
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Test parse method of InventoryModule class
    '''
    # test parse method with empty path
    inv = InventoryModule()
    assert inv.parse('', '', '') == None

    # test parse method with valid path
    inv = InventoryModule()
    inv.verify_file = lambda path: True
    inv.set_options = lambda x: None
    inv.loader=MockLoader()
    inv.loader.load_from_file= lambda path, cache=True: {'all':{'hosts':{'test1':None, 'test2':{'host_var':'value'}}}}
    inv.inventory=MockInventory()
    inv.inventory.add_group = lambda group: group
    inv.inventory.add_host = lambda group, host, port=None: None
    inv.inventory.set

# Generated at 2022-06-13 13:09:00.059601
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    cwd = os.path.dirname(os.path.realpath(__file__))
    datafile = os.path.join(os.path.join(os.path.join(cwd, 'tests'), 'units'), 'data', 'inventory', 'test_data.yaml')
    #datafile = os.path.join(os.path.join(cwd, 'testing'), 'test_data.yaml')
    #datafile = os.path.join(os.path.join(os.path.join(os.path.join(cwd, '..'), '..'), '..'), 'test_data.yaml')

    print('\nTest inventory YAML code.')
    print('  Loading data from %s' % datafile)


# Generated at 2022-06-13 13:09:10.679341
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  from ansible.plugins.inventory import InventoryDirectory
  from ansible.plugins.loader import plugin_loader


# Generated at 2022-06-13 13:09:20.251829
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:09:34.153169
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader
    from collections import defaultdict
    inv_dat = defaultdict(lambda: defaultdict())
    InventoryModule = inventory_loader.get('yaml')
    myinv = InventoryModule()

    # Test case 1: data is a dict
    dat_1 = dict(plugin="yaml")
    try:
        myinv.parse(inv_dat, DataLoader(), path='/home/ansible', loader=DataLoader(), cache=False)
    except AnsibleParserError as e:
        assert "Plugin configuration YAML file, not YAML inventory" == to_text(e)
        assert inv_dat == defaultdict(lambda: defaultdict())

# Generated at 2022-06-13 13:09:49.475294
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    obj = InventoryModule()

# Generated at 2022-06-13 13:09:52.319113
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import json

    inventory_base = InventoryModule()
    assert isinstance(inventory_base, InventoryModule)

    print('Success: test_InventoryModule_parse')



# Generated at 2022-06-13 13:10:04.405862
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Test if the parser for yaml inventory parser is working as
    expected with different inputs
    '''
    from ansible.plugins.loader import inventory_loader

    inventory = inventory_loader.get('yaml', class_only=True)()


    # 1. Test with empty data
    def parse_empty_data():
        inventory.parse(None, None, '/tmp/empty_file.yml', cache=False)

    assert_raises(AnsibleParserError, parse_empty_data)


    # 2. Test with data that is not a dictionary
    def parse_data_not_dictionary():
        inventory.parse(None, None, '/tmp/test_yaml_file.yml', cache=False)

    assert_raises(AnsibleParserError, parse_data_not_dictionary)




# Generated at 2022-06-13 13:10:13.185616
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    data = '''
    all:
        hosts:
            host1:
                var1: 1
                var2: 2
            host2:
                var2: 3
                var3: 4
        vars:
            group_all_var: value
        children:
            other_group:
                children:
                    group_x:
                        hosts:
                            host4
                    group_y:
                        hosts:
                            host3:
                    group_z:
                        host:
                            host5
                vars:
                    g2_var2: value3
                hosts:
                    host5:
                        var3: 5
            last_group:
                hosts:
                    host1:
                        var1: 6
                vars:
                    group_last_var: value
    '''


# Generated at 2022-06-13 13:10:23.563071
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = BaseFileInventoryPlugin()
    loader = BaseFileInventoryPlugin()
    inventory_dir = os.path.join(os.path.dirname(__file__), '..', 'inventory')
    inventory_path = os.path.join(inventory_dir, 'test_dynamic_inventory.yml')
    host_vars_path = os.path.join(inventory_dir, 'host_vars')
    group_vars_path = os.path.join(inventory_dir, 'group_vars')
    yaml_vars_path = os.path.join(inventory_dir, 'vars.yml')
    # Test whether the required settings are in place
    assert inventory_path is not None
    assert host_vars_path is not None
    assert group_vars_path is not None

# Generated at 2022-06-13 13:11:06.513669
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # setup
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=None, variable_manager=variable_manager)
    inventory.add_group('all')

    # setup test obj
    obj = InventoryModule()
    obj._inventory = inventory

    # test with empty data
    with pytest.raises(AnsibleParserError) as error:
        obj.parse(inventory, loader, '', '')
    assert str(error.value) == 'Parsed empty YAML file'

    # test with plugin configuration

# Generated at 2022-06-13 13:11:09.535199
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    dm = InventoryModule()
    assert dm.verify_file('/etc/ansible/hosts')
    assert not dm.verify_file('/etc/ansible/hosts.bak')


# Generated at 2022-06-13 13:11:19.260668
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Create parser obj
    parser = InventoryModule()

    # Blocks

# Generated at 2022-06-13 13:11:32.488371
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()


# Generated at 2022-06-13 13:11:41.399426
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    import tempfile
    from ansible.module_utils.six import StringIO


# Generated at 2022-06-13 13:11:50.330730
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    assert module.verify_file("test/test-yaml.yaml") == True
    assert module.verify_file("test/test-yaml.yml") == True
    assert module.verify_file("test/test-yaml.json") == True
    assert module.verify_file("test/test-yaml-invalid.json") == True
    assert module.verify_file("test/test-yaml-invalid.txt") == False

# Generated at 2022-06-13 13:11:58.711932
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host

    loader = DataLoader()
    inv_data = '''
all:
  hosts:
    server1:
      ansible_host: testserver1
      ansible_port: 2222
    server2:
      ansible_port: 11022
      ansible_host: testserver2
  children:
    child_group:
      hosts:
        server3:
        server4:
    child_group2:
      hosts:
        server5:
        server6:
      children:
        child_group3:
          hosts:
            server7:
            server8:
'''


# Generated at 2022-06-13 13:12:06.532912
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import sys
    import os
    import unittest
    import tempfile

    class TestInventoryModule(unittest.TestCase):
        def setUp(self):
            env_overrides = {}
            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
            self.examples_dir = os.path.join(base_dir, 'examples')

# Generated at 2022-06-13 13:12:16.244903
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventoryModule = InventoryModule()
    inventoryModule.set_options()
    data = inventoryModule.load_file()
    inventoryModule.parse()

    # inventoryModule of method parse is not returned
    assert inventoryModule.parse() == None

    # data[host_pattern][hostnames] == hostnames
    for host_pattern in data:
        hostnames = inventoryModule._parse_host(host_pattern)
        assert data[host_pattern]['hosts'] == hostnames



# Generated at 2022-06-13 13:12:21.038632
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print('###Testing method parse of class InventoryModule###\n')

    # import class InventoryModule
    InventoryModule = ansible_inventory_module.InventoryModule()

    # initialize test variables
    inventory=None
    loader=None
    path='/home/vagrant/ansible/plugins/inventory/YAML.py'
    cache=True

    # call method with test variables
    print('###Testing following call: \nInventoryModule.parse(inventory, loader, path, cache=True)')
    InventoryModule.parse(inventory, loader, path, cache=True)

    pass


# Generated at 2022-06-13 13:13:22.018573
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv_module = InventoryModule()
    dummy_loader = object()
    dummy_inventory = object()
    dummy_path = object()
    inv_module.parse(dummy_inventory, dummy_loader, dummy_path)

# Generated at 2022-06-13 13:13:31.289163
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    host_path = "./tests/integration/inventory_plugins/inventory_module/hosts"
    yaml_valid_extensions = ['.yaml', '.yml']
    inventory = InventoryModule()
    inventory.set_option('yaml_valid_extensions', yaml_valid_extensions)
    valid = inventory.verify_file(host_path)
    assert valid is True

    host_path = "./tests/integration/inventory_plugins/inventory_module/hosts.txt"
    yaml_valid_extensions = ['.yaml', '.yml']
    inventory = InventoryModule()
    inventory.set_option('yaml_valid_extensions', yaml_valid_extensions)
    valid = inventory.verify_file(host_path)
    assert valid is False


# Generated at 2022-06-13 13:13:43.036965
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class MyInventoryModule(InventoryModule):
        def __init__(self):
            self._loader = FakeLoader()
            self.get_option = lambda x: []
            self.inventory = FakeInventory()
            self.display = FakeDisplay()
            self.loader = FakeLoader()
            self.set_options = lambda: None
            self.parse_extra_args = lambda args: {'hosts': [], 'groups': {'all': []}}
    i = MyInventoryModule()
    i.parse('', '', './tests/inventory_plugins/test_yaml.yml')


# Generated at 2022-06-13 13:13:54.245028
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.utils.addresses import parse_address
    from ansible.plugins.loader import inventory_loader
    from ansible.inventory import Host
    from ansible.vars.manager import VariableManager

    # Parsing yaml and comparing it with the expected result

    loader = DataLoader()
    inv_source = """
    all: # keys must be unique, i.e. only one 'hosts' per group
        hosts:
            test1:
            test2:
                host_var: value
"""
    inv = inventory_loader.get('yaml', loader=loader)
    inv.parse_inventory(inv_source)
    inv.add_hos('test1', 'test1')
    inv.add_hos('test2', 'test2')

    assert inv.hosts['test1'] == Host

# Generated at 2022-06-13 13:14:05.379765
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    #----------------------------------------------------------------------------------------------------
    # Build inventory file (TEMPORARY)
    #----------------------------------------------------------------------------------------------------
    a = open('test_InventoryModule_parse', 'w+')
    a.write(EXAMPLES)
    a.seek(0)
    #----------------------------------------------------------------------------------------------------
    # Tests
    #----------------------------------------------------------------------------------------------------
    keyword = ['hosts', 'vars', 'children']
    expected = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7']
    inventory = []
    inventory_plugin = InventoryModule()

    inventory_plugin.parse(inventory, 'asd', 'test_InventoryModule_parse')
    # ----------------------------------------------------------------------------------------------------
    # Confirm the expected output by reading the inventory file
    # ----------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 13:14:13.232027
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import json
    import pytest

    def mock_load_from_file(path, cache = True):
        return json.load(open(path, "r"))

    # Patching the loader.load_from_file to load from a json file instead of a yaml one
    # to make easier to serialize the test data
    mock_loader = type('loader', (object, ), {})
    mock_loader.load_from_file = mock_load_from_file
    yaml_inventory = InventoryModule()
    yaml_inventory.loader = mock_loader

    test_plugin_section = {'plugin': type('plugin_config', (object, ), {'name':'yaml'})()}

# Generated at 2022-06-13 13:14:17.872524
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.inventory.yaml import InventoryModule

    path, the_dir = get_test_path()
    inventory = InventoryModule()
    inventory.options = {'yaml_extensions': ['.yaml']}
    inventory.loader.set_basedir(path)
    inventory.parse('host', 'host', path)

# Generated at 2022-06-13 13:14:26.072727
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    from ansible.utils.display import Display
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.plugins.loader import inventory_loader

    if os.path.exists('test.yml'):
        raise Exception('test.yml file already exists. Test cannot continue as it should not overwite existing files')


# Generated at 2022-06-13 13:14:33.668430
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    m = InventoryModule()
    loader = DataLoader()

# Generated at 2022-06-13 13:14:35.903979
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    parser = InventoryModule()

    assert len(parser.parse()) == 2

    assert parser.parse()[0][0] == "test1.example.com"
    assert len(parser.parse()[0][1]["vars"]) == 10