

# Generated at 2022-06-13 13:05:42.353685
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader
    plugin = inventory_loader.get('yaml')
    yaml_file_content = '''
all:
    hosts:
        test1:
            host_var: value
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
    inventory = dict()

# Generated at 2022-06-13 13:05:46.912675
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.set_options()
    inv.parse(None, None, 'tests/inventory/test_yaml.yml')

    groups = inv.get_groups()
    groups.sort()
    assert groups == ['all', 'other_group', 'other_group/group_y', 'other_group/group_x', 'last_group']

# Generated at 2022-06-13 13:05:57.256528
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    class Object(object):
        '''
        Generic object class
        '''
        pass

    test_obj = Object()
    test_obj.yaml_extensions = ('.yaml', '.yml', '.json')
    test_obj.get_option = lambda x: test_obj.yaml_extensions


# Generated at 2022-06-13 13:06:06.696456
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    inv.set_options()
    inv.inventory = MagicMock()
    inv.inventory.add_group = MagicMock()
    inv.inventory.add_child = MagicMock()
    inv.inventory.set_variable = MagicMock()
    inv.loader = MagicMock()
    data = {
        'group1': {
            'hosts': {
                'localhost': None
            }
        },
        'group2': {
            'hosts': {
                'localhost': None
            }
        }
    }
    inv.loader.load_from_file = MagicMock(return_value=data)
    inv.parse(inv.inventory, inv.loader, '/tmp')
    inv.inventory.add_group.assert_any_call('group1')
    inv.inventory

# Generated at 2022-06-13 13:06:18.929232
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    """
    Test case for method verify_file of class InventoryModule

    :return:
    """
    inv = InventoryModule()

    assert(inv.verify_file("/tmp/foo.yml"))
    assert(inv.verify_file("/tmp/bar.yaml"))
    assert(inv.verify_file("/tmp/baz.json"))

    inv.set_option("yaml_extensions", [".yml"])
    assert(inv.verify_file("/tmp/foo.yml"))
    assert(not inv.verify_file("/tmp/bar.yaml"))
    assert(not inv.verify_file("/tmp/baz.json"))

    inv.set_option("yaml_extensions", [".yaml"])

# Generated at 2022-06-13 13:06:28.820548
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    from ansible.plugins.loader import find_plugin_file
    from ansible.plugins.loader import InventoryModule
    from ansible.errors import AnsibleParserError

    for i in ['.yaml', '.yml', '.json']:
        path = find_plugin_file('inventory', os.path.join('test', 'test_inventory_plugin_yaml' + i))
        assert InventoryModule.verify_file(path) is True, path

    path = find_plugin_file('inventory', 'test/test_inventory_plugin_ini')
    assert InventoryModule.verify_file(path) is False, path
    path = find_plugin_file('inventory', 'test/test_inventory_plugin_yaml')
    assert InventoryModule.verify_file(path) is False, path



# Generated at 2022-06-13 13:06:34.188377
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # file without extension
    assert InventoryModule().verify_file('/tmp/hosts') == False
    # file with valid extension
    assert InventoryModule().verify_file('/tmp/hosts.yml') == True
    # file with invalid extension 
    assert InventoryModule().verify_file('/tmp/hosts.py') == False

# Generated at 2022-06-13 13:06:40.094851
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()
    assert inventory.verify_file('inventory.yml') == True
    assert inventory.verify_file('inventory.yaml') == True
    assert inventory.verify_file('inventory.json') == True
    assert inventory.verify_file('inventory.xml') == False
    assert inventory.verify_file('inventory.txt') == False


# Generated at 2022-06-13 13:06:50.544124
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

if __name__ == '__main__':
    import sys
    import json
    import unittest
    import shlex
    from ansible.compat.tests import mock
    from ansible.cli import CLI
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.plugins.strategy import StrategyBase

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host


# Generated at 2022-06-13 13:07:01.798492
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    mgr = InventoryManager(loader=DataLoader(), sources=['/dev/null'])
    inv = mgr.get_inventory()

    plugin = InventoryModule()
    plugin.set_options()
    plugin.inventory = inv
    plugin.loader = DataLoader()

    plugin.parse(path=None, original_path='/dev/null', cache=True)

    # Test all:
    assert(inv.groups[0].name == 'all')
    assert(len(inv.groups[0].hosts) == 2)
    assert(len(inv.groups[0].vars) == 1)

# Generated at 2022-06-13 13:07:16.579956
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    inv = InventoryModule()
    inv.parse(inventory, loader, "{}".format('example.yml'))
    assert len(inventory.get_groups()) == 4
    assert len(inventory.get_hosts()) == 5


# Generated at 2022-06-13 13:07:20.812969
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventoryModule = InventoryModule()
    inventoryModule.verify_file("hosts")
    inventoryModule.verify_file("hosts.yaml")
    inventoryModule.verify_file("hosts.yml")
    inventoryModule.verify_file("hosts.json")
    inventoryModule.verify_file("foobar.txt")

# Generated at 2022-06-13 13:07:33.083485
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    real_name = "tests/unit/plugins/inventory/sample_inventory.pdf"
    fake_name = "tests/unit/plugins/inventory/sample_inventory.yml"
    ans_inst = InventoryModule()

    ans_inst._option_map["yaml_extensions"] = [".yaml"]
    assert not ans_inst.verify_file(real_name)
    assert ans_inst.verify_file(fake_name)

    ans_inst._option_map["yaml_extensions"] = [".pdf"]
    assert ans_inst.verify_file(real_name)
    assert not ans_inst.verify_file(fake_name)



# Generated at 2022-06-13 13:07:41.841085
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    check_filenames = ['/etc/ansible/hosts', '/etc/ansible/ho.sts', '/etc/ansible/ho.st', '/etc/ansible/hosts.yaml', '/etc/ansible/hosts.yml', '/etc/ansible/hosts.json', '/etc/ansible/hosts.yaml.yaml', '/etc/ansible/hosts.yaml.yml']
    yaml_extensions = ['.yaml', '.yml', '.json']
    valid = []
    invalid = []
    inventory = InventoryModule()

    for check_filename in check_filenames:
        valid = []
        invalid = []
        for ext in yaml_extensions:
            inventory._options['yaml_extensions'] = ext

# Generated at 2022-06-13 13:07:44.078455
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    im = InventoryModule()
    assert im.verify_file("test.yaml") == False


# Generated at 2022-06-13 13:07:50.787799
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_module = InventoryModule()
    valid = inventory_module.verify_file('/tmp/tests/hosts.yaml')
    assert valid == True
    valid = inventory_module.verify_file('/tmp/tests/hosts.json')
    assert valid == True
    valid = inventory_module.verify_file('/tmp/tests/hosts.cfg')
    assert valid == False

# Generated at 2022-06-13 13:07:53.676059
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    file_path = './tests/units/plugins/inventory/yaml/test_file.yml'
    print(plugin.verify_file(file_path))

# Generated at 2022-06-13 13:08:01.336153
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # Set up test environment
    class inventory_module(InventoryModule):
        def __init__(self):
            self.options = {'yaml_extensions': ['.yaml', '.yml', '.json']}

    inventory_module = inventory_module()
    import os
    import tempfile
    import shutil

    # Empty file
    tmp_file = tempfile.mkstemp()[1]
    assert True == inventory_module.verify_file(tmp_file)
    os.remove(tmp_file)

    # File with content, but no extension
    tmp_file = tempfile.mkstemp()[1]
    with open(tmp_file, 'w') as f:
        f.write('foo: bar')
    assert True == inventory_module.verify_file(tmp_file)

# Generated at 2022-06-13 13:08:12.111123
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.inventory import BaseFileInventoryPlugin
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader

    # Define a mock class for InventoryModule (extends BaseFileInventoryPlugin)
    class InventoryModule(BaseFileInventoryPlugin):

        NAME = 'test_yaml'
        def __init__(self):
            super(InventoryModule, self).__init__()

        def verify_file(self, path):

            valid = False
            if not path or path.endswith('.yaml'):
                valid = True
            return valid

    # Define a mock class for BaseInventoryPlugin (extends BaseInventoryPlugin)
    class Inventory(object):

        def __init__(self):
            self.groups = {}

        # Only

# Generated at 2022-06-13 13:08:20.344527
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    hostvars = {'10.1.1.1': {'ansible_host': '10.1.1.1', 'host_var1': 'host_value1'},
                }

    inventory = {}

# Generated at 2022-06-13 13:08:47.948877
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Positive unit tests
    test1 = InventoryModule()
    assert test1.verify_file('foo.yml')
    assert test1.verify_file('foo')

    test2 = InventoryModule()
    test2.set_options(yaml_extensions=['.yml', '.yaml'])
    assert test2.verify_file('foo.yml')
    assert test2.verify_file('foo.yaml')

    test3 = InventoryModule()
    test3.set_options(yaml_extensions=[])
    assert test3.verify_file('foo')

    # Negative tests
    test4 = InventoryModule()
    assert not test4.verify_file('foo.xml')

    test5 = InventoryModule()

# Generated at 2022-06-13 13:08:53.538729
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    for valid_file in ['sample_yaml.yaml', 'sample_yaml.yml', 'sample_yaml.json']:
        assert plugin.verify_file(valid_file)
    assert not plugin.verify_file('sample_yaml.txt')


# Generated at 2022-06-13 13:09:02.560668
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Test 1
    # yaml_extensions is non empty list
    # with valid extension
    # and valid file
    # and path is absolute
    test_inventory_path = 'tests/contrib/inventory/test_inventory_yaml/valid.yaml'
    os_path_exists_mock = MagicMock(return_value=True)

# Generated at 2022-06-13 13:09:12.390274
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ########################
    #### SIMPLE TEST  ######
    ########################
    yaml_simple_test = '''
all:
  hosts:
    h1:
  children:
    child1:
      hosts:
        h2:
    child2:
     hosts:
       h3:
       h4:
'''

# Generated at 2022-06-13 13:09:15.118926
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
  inv = InventoryModule()
  assert inv.verify_file('/home/dell/ansible/ansible-doc/plugin/inventory/yaml.py')

# Generated at 2022-06-13 13:09:23.594616
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test a inventory with 'all' group defined
    inventory_module = InventoryModule()

# Generated at 2022-06-13 13:09:33.629284
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    """validates the given file name and file extension"""
    inventory_module = InventoryModule()
    inventory_module.set_options()

    inventory_module.set_option('yaml_extensions', ['.yaml', '.yml', '.json'])
    assert inventory_module.verify_file("test.yaml") == True
    assert inventory_module.verify_file("test.yml") == True
    assert inventory_module.verify_file("test.json") == True
    assert inventory_module.verify_file("test.txt") == False


# Generated at 2022-06-13 13:09:49.414397
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:10:02.057696
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    ''' Unit test for method parse of class InventoryModule '''

    loader = DictDataLoader({
        "hosts": "{{ inventory_dir }}/hosts",
        "yaml": "{}",
    })
    yaml_plugin = InventoryModule()
    yaml_plugin.loader = loader
    yaml_plugin.parse({}, loader, "yaml")
    assert yaml_plugin.get_option('yaml_extensions') == ['.yaml', '.yml', '.json']

    with pytest.raises(AnsibleParserError):
        yaml_plugin.parse({}, loader, "hosts")


# Generated at 2022-06-13 13:10:16.196434
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Initialize the InventoryModule plugin
    yaml_inventory_plugin = InventoryModule()
    yaml_inventory_plugin.file_path = 'host_vars/ec2.yml'
    yaml_inventory_plugin.get_option = lambda x: ['.yaml', '.yml', '.json']
    assert yaml_inventory_plugin.verify_file('.yml') == True
    assert yaml_inventory_plugin.verify_file('.yaml') == True
    assert yaml_inventory_plugin.verify_file('.json') == True
    assert yaml_inventory_plugin.verify_file('.fakeyaml') == False

test_InventoryModule_verify_file()

# Generated at 2022-06-13 13:10:58.123611
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins import InventoryModule

    loader = Mock(spec_set=DictDataLoader)
    loader.load_from_file.return_value = {
        'all': {
            'hosts': ['test1', 'test2'],
            'vars': {'foo': 'bar'},
            'children': {
                'group1': {
                    'hosts': ['test3']
                }
            }
        },
        'group1': {
            'hosts': ['test4'],
            'vars': {'foo': 'group1'}
        },
        '_meta': {
            'hostvars': {
                'test1': {'ansible_host': '127.0.0.1'}
            }
        }
    }
    # pylint: disable=no

# Generated at 2022-06-13 13:11:08.170874
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: fix this test
    pass
    # inventory = {
    #     "all": {
    #         "hosts": {
    #             "test1": {},
    #             "test2": {
    #                 "host_var": "value"
    #             }
    #         },
    #         "vars": {
    #             "group_all_var": "value"
    #         },
    #         "children": {
    #             "other_group": {
    #                 "children": {
    #                     "group_x": {
    #                         "hosts": {
    #                             "test5": {}
    #                         }
    #                     },
    #                     "group_y": {
    #                         "hosts": {
    #                             "test6": {}
   

# Generated at 2022-06-13 13:11:13.324351
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class Options(object):
        filename = "test.yml"
        yaml_extensions = ['.yaml', '.yml', '.json']

    class Inventory(object):
        def __init__(self):
            self.groups = dict()

        def add_group(self, name):
            self.groups[name] = dict()
            return name

        def add_child(self, parent, child):
            self.groups[parent]['children'] = self.groups[parent].get('children', []) + [child]

        def set_variable(self, group, name, value):
            self.groups[group]['vars'] = self.groups[group].get('vars', {})
            self.groups[group]['vars'][name] = value


# Generated at 2022-06-13 13:11:14.493186
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    invmod = InventoryModule()
    assert invmod.parse()

# Generated at 2022-06-13 13:11:26.763923
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    filepath = os.path.join(os.path.dirname(__file__), 'yaml_inventory.yaml')
    yamlinventory = InventoryModule()
    yamlinventory.reader = open(filepath, 'r')
    yamlinventory.parse('/dev/null', None, None)
    assert yamlinventory.inventory.groups["all"].name == "all"
    assert yamlinventory.inventory.groups["all"].get_variable("group_all_var") == "value"
    assert yamlinventory.inventory.groups["all"].hosts["test1"].name == "test1"
    assert yamlinventory.inventory.groups["all"].hosts["test2"].name == "test2"

# Generated at 2022-06-13 13:11:34.431266
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # test with True
    i = InventoryModule()
    i.set_options()

    path_test1 = 'test1.json'
    path_test2 = 'test2.yml'
    path_test3 = 'test3.yaml'
    path_test4 = 'test4.txt'
    path_test5 = 'test5'

    assert i.verify_file(path_test1)
    assert i.verify_file(path_test2)
    assert i.verify_file(path_test3)
    assert not i.verify_file(path_test4)
    assert not i.verify_file(path_test5)

# Generated at 2022-06-13 13:11:35.834456
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory.parse(Yaml_Example_File)

# Generated at 2022-06-13 13:11:40.205864
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = TestInventoryModule()

    assert inventory.verify_file(path="path/to/inventory/file.yaml") == True
    assert inventory.verify_file(path="path/to/inventory/file.yml") == True
    assert inventory.verify_file(path="path/to/inventory/file.py") == False


# Generated at 2022-06-13 13:11:49.601044
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Setup with default values
    test_object = InventoryModule()

    assert test_object.verify_file('/tmp/test.yaml')
    assert test_object.verify_file('/tmp/test.yml')
    assert test_object.verify_file('/tmp/test.json')

    # Test empty file
    assert not test_object.verify_file('')

    # Test file with non-whitelisted extension
    assert not test_object.verify_file('/tmp/test.invalid')

# Generated at 2022-06-13 13:11:53.680697
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import tempfile
    import os

    # Create temporary files with valid extensions
    (fd1, file1) = tempfile.mkstemp(suffix = '.yml')
    (fd2, file2) = tempfile.mkstemp(suffix = '.yaml')
    (fd3, file3) = tempfile.mkstemp(suffix = '.json')

    # Create temporary files with invalid extensions
    (fd4, file4) = tempfile.mkstemp(suffix = '.foo')
    (fd5, file5) = tempfile.mkstemp(suffix = '.bar')
    (fd6, file6) = tempfile.mkstemp(suffix = '.baz')

    # It should return True for files with 'valid' extensions
    assert InventoryModule().verify_file(file1)
    assert Inventory

# Generated at 2022-06-13 13:12:51.241124
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """Unit test for method parse of class InventoryModule."""

    inventory_module = InventoryModule()
    inventory = {}
    loader = {}
    path = {}

    inventory_module.parse(inventory, loader, path, cache=True)


# Generated at 2022-06-13 13:12:56.169629
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Test empty file
    inventory_string = ''
    inventory = InventoryModule()
    inventory.parse(inventory_string)

    # Test Valid yaml inventory
    inventory_string = '''
    all:
        hosts:
            server1:
            server2:
        children:
           child_group1:
               hosts:
                   server1:
                   server2:
    '''
    inventory = InventoryModule()
    inventory.parse(inventory_string)

# Generated at 2022-06-13 13:13:02.625726
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import pytest
    from collections import MutableMapping

    class TestInventoryModule(InventoryModule):

        NAME = 'test.yaml'

        def __init__(self):

            super(TestInventoryModule, self).__init__()

    class TestAnsibleInventory:
        def __init__(self):
            self.groups = {}
        def add_group(self, group_name):
            grp = TestAnsibleGroup(group_name)
            self.groups[group_name] = grp
            return grp
        def add_child(self, group, subgroup):
            self.groups[group].children.append(subgroup)
        def set_variable(self, group, variable_name, variable_value):
            self.groups[group].vars[variable_value] = variable_value



# Generated at 2022-06-13 13:13:08.161861
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    try:
        inv.verify_file("inventory")
    except AnsibleParserError as e:
        assert str(e) == "No inventory was parsed, check your configuration and options"
    inv.set_options()
    assert inv.verify_file("inventory") == False
    assert inv.verify_file("inventory.yaml") == True


# Generated at 2022-06-13 13:13:11.117964
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    module.__init__()
    module.verify_file("inventory.yaml")
    module.parse("inventory", None, ".inventory.yaml")
    module.set_options()

# Generated at 2022-06-13 13:13:14.643298
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventoryModule = InventoryModule()
    assert inventoryModule.verify_file('./test/inventory/yaml_valid.yaml') == True
    assert inventoryModule.verify_file('./test/inventory/yaml_invalid.yaml') == False

# Generated at 2022-06-13 13:13:17.920925
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import sys
    import json
    import textwrap

    inv_file = textwrap.dedent(EXAMPLES)
    inv_data = json.loads(inv_file)

    inv = InventoryModule()

    inv.parse(inv_data)

# Generated at 2022-06-13 13:13:19.060174
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    loader = InventortyLoader()
    inventory = Inventory(loader)



# Generated at 2022-06-13 13:13:28.831580
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    plugin = InventoryModule()
    plugin.parse(file_name='test/test_dynamic_inventory.yml', inventory=inv_manager, loader=loader)

    assert inv_manager.get_groups() == ['sfc', 'sfc_test0', 'sfc_test1', 'sfc_test2']
    assert inv_manager.get_hosts() == ['sfc-testvm-0', 'sfc-testvm-1']

# Generated at 2022-06-13 13:13:40.882876
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class InventoryModuleNew(InventoryModule):
        def __init__(self):
            super(InventoryModuleNew, self).__init__()

    # create tests