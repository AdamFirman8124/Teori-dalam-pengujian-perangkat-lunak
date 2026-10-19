

# Generated at 2022-06-13 12:44:34.281097
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    pattern = "{{ type }}_{{ environment }}_{{ app }}_runner"
    variables = {
        'type': 'build',
        'environment': 'dev',
        'app': 'web',
    }
    inventory = InventoryManager(loader=DataLoader(), sources=[])
    var_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    template = var_manager.template
    host = template(pattern, variables)
    inventory.add_host(host)
    group = template('runner', variables)
    inventory.add_group(group)
    inventory.add_child(group, host)
    plugin = InventoryModule()

# Generated at 2022-06-13 12:44:46.418059
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import itertools

    class MockInventory:
        def __init__(self):
            self.hosts = []
            self.groups = {}

        def add_host(self, host):
            self.hosts.append(host)

        def add_child(self, group, child):
            self.groups[group].append(child)

        def add_group(self, group):
            self.groups[group] = []

        def set_variable(self, name, value):
            self.groups[name].variables = value

    inventory = MockInventory()

    module = InventoryModule()
    module.parse(inventory, None, 'test.config')


# Generated at 2022-06-13 12:44:55.820356
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Make sure to import the source file of this test
    import sys
    sys.path.insert(0, '..')

    from ansible.inventory.plugin import InventoryModule

    # Configuration file in YAML format
    config = "plugin: generator\n"
    config += "hosts:\n"
    config += "    name: \"{{ operation }}_{{ application }}_{{ environment }}_runner\"\n"
    config += "    parents:\n"
    config += "      - name: \"{{ operation }}_{{ application }}_{{ environment }}\"\n"
    config += "        parents:\n"
    config += "          - name: \"{{ operation }}_{{ application }}\"\n"
    config += "            parents:\n"
    config += "              - name: \"{{ operation }}\"\n"

# Generated at 2022-06-13 12:44:59.597984
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # create a new instance of InventoryModule class
    im = InventoryModule()
    # test a valid file path
    path = 'test.config'
    assert im.verify_file(path)
    # test a valid file path with an extension in constants.YAML_FILENAME_EXTENSIONS
    path = 'test.yml'
    assert im.verify_file(path)
    # test an invalid file
    path = 'test.py'
    assert not im.verify_file(path)

# Generated at 2022-06-13 12:45:03.040539
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
   config_file_path = './config'
   inventory = InventoryModule()
   loader = None
   cache=False

   inventory.parse(inventory, loader, config_file_path, cache=cache)

# Generated at 2022-06-13 12:45:12.812844
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create an instance of class InventoryModule to call its method parse
    inventoryModule = InventoryModule()

# Generated at 2022-06-13 12:45:17.356300
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    inventory.parse_options()
    config = {'hosts': {'name': 'localhost', 'parents': []}, 'layers': {}}
    inventory.parse(inventory, None, None, cache=False, config=config)
    assert inventory.hosts['localhost'].get_vars() == {}


# Generated at 2022-06-13 12:45:25.333577
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    options = {'plugin': ['generator']}
    inventory_module = InventoryModule()
    assert(inventory_module.verify_file('inventory.config') is True)
    assert(inventory_module.verify_file('inventory.yml') is True)
    assert(inventory_module.verify_file('inventory.yaml') is True)
    assert(inventory_module.verify_file('inventory.json') is False)


# Generated at 2022-06-13 12:45:32.510875
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """ Unit test for method parse of class InventoryModule """

    # create a class instance for testing
    mod = InventoryModule()

    # create a fake inventory class for testing
    class Inventory:
        """ fake inventory class """
        # pylint: disable=too-few-public-methods
        def __init__(self):
            self.hosts = dict()
            self.groups = dict()

        def add_host(self, host, aliases=None):
            """ fake method add_host """
            self.hosts[host] = aliases

        def add_group(self, groupname, fail_on_missing=False):
            """ fake method add_group """
            self.groups[groupname] = dict()

        def add_child(self, parent_name, child_name):
            """ fake method add_child """

# Generated at 2022-06-13 12:45:45.655854
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    mod = InventoryModule()
    mod.templar = DummyTemplar()
    inventory = DummyInventory()
    child = 'bob'
    parents = [{'name': '{{ name }}'}, {'name': '{{ name }}', 'parents': [{'name': '{{ name }}'}]}]
    var = {'name': child}
    mod.add_parents(inventory, child, parents, var)
    assert set(inventory.groups.keys()) == {child, child + '_' + child, child + '_' + child + '_' + child}
    assert inventory.groups[child + '_' + child]['_children'] == [child]
    assert inventory.groups[child + '_' + child + '_' + child]['_children'] == [child + '_' + child]



# Generated at 2022-06-13 12:45:57.954174
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    path = '/path/to/inventory'
    file_name, ext = os.path.splitext(path)
    m = InventoryModule()
    assert m.verify_file(path) == False
    assert m.verify_file(path) == False
    assert m.verify_file(file_name + '.config') == True
    assert m.verify_file(file_name + '.yaml') == True
    assert m.verify_file(file_name + '.yml') == True


# Generated at 2022-06-13 12:46:08.146361
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Mock of inventory with method add_host, add_group, groups
    class MockInventory(object):

        def __init__(self):
            self.hosts = {}
            self.groups = {}

        def add_host(self, key):
            self.hosts[key] = ''

        def add_group(self, key):
            self.groups[key] = {}

        def add_child(self, group1, group2):
            self.groups[group1][group2] = ''

        def get_groups(self, key):
            return self.groups[key]


# Generated at 2022-06-13 12:46:15.039300
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    path = "inventory/test_inventory_config_file"
    inventory_module = InventoryModule()
    loader = None
    inventory = None
    inventory_module.parse(inventory, loader, path, cache=False)
    print("Hosts:")
    for host in inventory.hosts:
        print(host)
    print("Groups:")
    for group in inventory.groups:
        print(group)
        print("Children:")
        for child in inventory.groups[group].get_hosts():
            print(child)
        print("Variables:")
        for var in inventory.groups[group].get_vars():
            print(var)


# Generated at 2022-06-13 12:46:27.115567
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    import pytest
    from collections import Mapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    im = InventoryModule()
    text_template = '''
      plugin: generator
      layers:
        word1:
          - run
          - walk
          - jump
        word2:
          - to
          - from
          - by
      hosts:
        name: "{{ word1 }}_{{ word2 }}"
    '''
    config = im._read_config_data(text_template)
    template_inputs = product(*config['layers'].values())
    for item in template_inputs:
        template_vars = dict()
        for i, key in enumerate(config['layers'].keys()):
            template_vars[key] = item[i]
       

# Generated at 2022-06-13 12:46:36.026691
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    generator = InventoryModule()

    # Config file with a host with no group
    config = {'layers': {'operation': ['build']}, 'hosts': {'name': '{{ operation }}'}}
    inventory = dict(hosts={})

    generator.parse(inventory, None, None, config)
    assert inventory == {'_meta': {'hostvars': {}}, 'hosts': {'build': {}}}

    # Config file with a host with 1 group
    config = {'layers': {'operation': ['build']}, 'hosts': {'name': '{{ operation }}', 'parents': [{'name': '{{ operation }}'}]}}

    generator.parse(inventory, None, None, config)

# Generated at 2022-06-13 12:46:42.490232
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    import os
    import json
    import unittest
    import tempfile
    from ansible.compat.tests import unittest
    from ansible.module_utils._text import to_bytes


    class TestInventoryModule(unittest.TestCase):
        def setUp(self):
            self.inventory = InventoryModule()

        def test_add_parents(self):
            inventory = {}
            child = "child"

# Generated at 2022-06-13 12:46:57.488968
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():

    # Setup
    class InventoryModuleMock:
        def __init__(self):
            self.inventory = None
        def add_host(i, h):
            self.inventory.add_host(h)
        def add_group(i, g):
            return self.inventory.add_group(g)
        def add_child(i, g, c):
            self.inventory.add_child(g, c)

    class InventoryMock:
        def __init__(self, s):
            self.source = s
            self.groups = {}
        def add_host(i, h):
            i.groups[h] = i.groups[h] if h in i.groups else {}

# Generated at 2022-06-13 12:47:05.221574
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    """
    construct a simple InventoryModule object and test its add_parents method
    """

    inv = InventoryModule()
    inv.inventory = {'groups': {}, 'hosts': {}}
    inv.template = lambda pattern, variables: pattern
    inv.add_parents(inv.inventory, 'child', [{'name': 'parent1', 'vars': {'var1': 'value1'}}, {'name': 'parent2'}], {})

    assert inv.inventory == {'hosts': {}, 'groups': {'parent1': {'vars': {'var1': 'value1'}, 'children': ['child']}, 'parent2': {'children': ['child']}}}

# Generated at 2022-06-13 12:47:18.917851
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Arrange
    test_path = 'test_inventory.yml'
    loader = None
    inventory_test = BaseInventoryPlugin()
    inventory_test.hosts = dict()
    inventory_test.groups = dict()

    expected_inventory = dict()
    expected_inventory['groups'] = dict()
    expected_inventory['_vars'] = dict()
    expected_inventory['_meta'] = dict()
    expected_inventory['_meta']['hostvars'] = dict()

    # Act
    inventory_test.parse(inventory_test, loader, test_path, cache=False)

    # Assert
    for host in inventory_test.hosts:
        for group in inventory_test.hosts[host]:
            hosts_in_group = expected_inventory['groups'].get(group, [])
            hosts_

# Generated at 2022-06-13 12:47:28.614678
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_module = InventoryModule()
    test_file = "test_file.config"
    test_relative_file = "../test_relative_file.config"
    assert inventory_module.verify_file(test_file) is True
    assert inventory_module.verify_file(test_relative_file) is True
    test_file = "test_file1.yaml"
    test_relative_file = "../test_relative_file.yaml"
    assert inventory_module.verify_file(test_file) is True
    assert inventory_module.verify_file(test_relative_file) is True
    test_file = "test_file1.txt"
    test_relative_file = "../test_relative_file.txt"
    assert inventory_module.verify_file(test_file) is False

# Generated at 2022-06-13 12:47:44.645065
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    i = InventoryModule()

    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'

    group1 = 'group1'
    group2 = 'group2'
    group3 = 'group3'

    class Inventory:
        def __init__(self):
            self.groups = {}
            self.hosts = {}
        def add_group(self, group):
            self.groups[group] = Group(group)
        def add_host(self, host):
            self.hosts[host] = Host(host)
        def add_child(self, parent, child):
            self.groups[parent].add_child(child)

# Generated at 2022-06-13 12:47:47.067932
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    instance = InventoryModule()
    path = 'inventory.config'

    assert instance.verify_file(path) is True


# Generated at 2022-06-13 12:47:50.201527
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    obj = InventoryModule()
    loader = "loader"
    inventory = "inventory"
    path = "path"
    cache = "cache"
    obj.parse(inventory, loader, path, cache=cache)
    assert path == "path"
    assert inventory == "inventory"

# Generated at 2022-06-13 12:48:03.486786
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_inventory = InventoryModule()
    config = dict()
    config['hosts'] = dict()
    config['hosts']['name'] = "{{ operation }}_{{ application }}_{{ environment }}_runner"
    config['hosts']['parents'] = list()
    group = dict()
    group['name'] = "{{ operation }}_{{ application }}_{{ environment }}"
    group['parents'] = list()
    group2 = dict()
    group2['name'] = "{{ operation }}_{{ application }}"
    group2['parents'] = list()
    group3 = dict()
    group3['name'] = "{{ operation }}"
    group2['parents'].append(group3)
    group3 = dict()
    group3['name'] = "{{ application }}"

# Generated at 2022-06-13 12:48:12.080296
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    # test data is provided as sample config file
    hosts = {}
    layers = {'operation': ['build'],
              'environment': ['dev', 'test', 'prod'],
              'application': ['web', 'api']}
    parent = {'name': '{{ application }}_{{ environment }}',
              'parents': [
                  {'name': '{{ application }}'},
                  {'name': '{{ environment }}'}
              ]}
    child = 'hostname'

    # init inventory object
    inventory = mock.MagicMock()
    inventory.groups = {}
    inventory.groups[child] = {}

    # init templar object
    templar = mock.MagicMock()
    template_variables = {}
    templar.available_variables = template_variables

    # init InventoryModule object
   

# Generated at 2022-06-13 12:48:19.015135
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=['sample_inventory.config'])
    assert 'build_api_dev_runner' in inventory.hosts
    assert 'build_api_test_runner' in inventory.hosts
    assert 'build_api_prod_runner' in inventory.hosts
    assert 'launch_api_dev_runner' in inventory.hosts
    assert 'launch_api_test_runner' in inventory.hosts
    assert 'launch_api_prod_runner' in inventory.hosts
    assert 'build_web_dev_runner' in inventory.hosts
    assert 'build_web_test_runner' in inventory.hosts

# Generated at 2022-06-13 12:48:21.923805
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    path = "inventory.config"
    inventory = InventoryModule()
    expected = True
    actual = inventory.verify_file(path)
    assert actual == expected


# Generated at 2022-06-13 12:48:30.943892
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    import os
    import mock
    import __builtin__

    plugin = InventoryModule()

    setattr(os, 'path', mock.MagicMock())
    setattr(os.path, 'join', mock.MagicMock(return_value='some_path'))

    setattr(__builtin__, 'open', mock.mock_open(read_data='---\nplugin: generator'))

    setattr(plugin, 'templar', mock.MagicMock())
    setattr(plugin.templar, 'do_template', mock.MagicMock(side_effect=['group1', 'group2', 'group3', 'group1:vars', 'group2:vars', 'group3:vars']))

    inventory = mock.MagicMock()
    setattr(inventory, 'groups', {})
    loader

# Generated at 2022-06-13 12:48:38.477724
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    import yaml
    # Create a test inventory file to use as data source
    tmp_inv_file = "/tmp/inventory.config"

# Generated at 2022-06-13 12:48:44.041455
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
   inventory_module = InventoryModule()
   assert(inventory_module.verify_file('myfile.config') == True)
   assert(inventory_module.verify_file('otherfile.yaml') == True)
   assert(inventory_module.verify_file('otherfile.yml') == True)
   assert(inventory_module.verify_file('otherfile.json') == True)
   assert(inventory_module.verify_file('otherfile') == True)
   assert(inventory_module.verify_file('otherfile.') == True)
   assert(inventory_module.verify_file('otherfile.foo') == False)
   assert(inventory_module.verify_file('otherfile.bar') == False)


# Generated at 2022-06-13 12:49:01.843756
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
  from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
  from ansible.plugins.inventory import BaseInventoryPlugin

  # inherit from BaseInventoryPlugin in order to force parse function to run
  class InventoryModule(BaseInventoryPlugin):
      """ constructs groups and vars using Jinja2 template expressions """

      NAME = 'generator'

      def __init__(self):

          super(InventoryModule, self).__init__()

  # create a dummy inventory object
  class inventory():
    def __init__(self):
      self.groups = {}
      self.hosts = {}
      self.groups['generic'] = {}
      self.groups['generic'].set_variable = set_variable
      self.groups['generic'].get_variable = get_variable


# Generated at 2022-06-13 12:49:11.666842
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader

    hostvars = dict()
    groups = dict()

    def add_host(hostname, *args, **kwargs):
        hostvars[hostname] = dict()

    def add_group(groupname, *args, **kwargs):
        if groupname not in groups:
            groups[groupname] = dict(name=groupname, hosts=[])

    def add_child(parent, child):
        if parent not in groups:
            groups[parent] = dict(name=parent, hosts=[])
        if child not in groups[parent]['hosts']:
            groups[parent]['hosts'].append(child)

    def set_variable(hostname, varname, value):
        if hostname not in hostvars:
            hostvars[hostname]

# Generated at 2022-06-13 12:49:24.511391
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    plugin = InventoryModule()
    inventory = unittest.mock.Mock()
    groupname = 'group1'
    group = unittest.mock.Mock()
    group.set_variable = unittest.mock.Mock()
    inventory.groups = {groupname:group}
    inventory.add_group = unittest.mock.Mock()
    inventory.add_child = unittest.mock.Mock()
    plugin.add_parents(inventory, groupname, [{'name': 'g2'}], {'g2': 'g2'})
    assert inventory.add_group.call_count == 1
    assert inventory.add_child.call_count == 1
    assert plugin.template.call_count == 1
    assert group.set_variable.call_count == 0



# Generated at 2022-06-13 12:49:39.269471
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import os
    import tempfile
    import shutil
    # create temporary directory
    tmpdir = tempfile.mkdtemp()
    # add test yaml file
    test_yaml_file = os.path.join(tmpdir, 'test_yaml.yaml')

# Generated at 2022-06-13 12:49:43.197796
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    i = InventoryModule()
    assert i.verify_file('inventory.cfg') is True
    assert i.verify_file('inventory.config') is True
    assert i.verify_file('inventory.yaml') is True
    assert i.verify_file('inventory.yml') is True
    assert i.verify_file('inventory') is False


# Generated at 2022-06-13 12:49:48.334963
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    verify_file_obj = InventoryModule()
    assert verify_file_obj.verify_file('./inventory.config')
    assert not verify_file_obj.verify_file('./inventory.yml')


# Generated at 2022-06-13 12:50:01.649240
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    from ansible.plugins.inventory import BaseInventoryPlugin
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    class FakeVaultLib(VaultLib):
        def __init__(self):
            self.secrets = dict()

        def encrypt(self, value):
            return "vault(%s)" % value

        def decrypt(self, value):
            if value.startswith("vault("):
                return value[6:-1]
            return value

    plugin = InventoryModule()
    templar = BaseInventoryPlugin(loader=DataLoader())._templar
    templar.vault_secrets = FakeVaultLib()
    plugin.templar = templar

# Generated at 2022-06-13 12:50:04.664007
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    m = InventoryModule()
    is_valid = m.verify_file("inventory.config")
    assert not is_valid

    is_valid = m.verify_file("inventory.yml")
    assert is_valid

    is_valid = m.verify_file("inventory.yaml")
    assert is_valid

    is_valid = m.verify_file("inventory.yml.config")
    assert is_valid


# Generated at 2022-06-13 12:50:12.607288
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    import jinja2
    from ansible.inventory import Inventory


# Generated at 2022-06-13 12:50:21.731994
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from collections import namedtuple
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    layer = namedtuple('layer', ['name', 'vars'])


# Generated at 2022-06-13 12:50:48.657599
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    im = InventoryModule()
    result = im.verify_file("/etc/puppet/hieradata/common.yaml")
    assert result == True
    result = im.verify_file("/etc/puppet/hieradata/common")
    assert result == True
    result = im.verify_file("/etc/puppet/hieradata/common.txt")
    assert result == False

# Generated at 2022-06-13 12:51:00.811921
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # setup
    inventory = {}
    loader = {}
    path = ""
    cache = True
    inventory_module = InventoryModule()
    template_inputs = [
        ('build', 'dev', 'web'),
        ('build', 'dev', 'api'),
        ('build', 'test', 'web'),
        ('build', 'test', 'api'),
        ('build', 'prod', 'web'),
        ('build', 'prod', 'api'),
        ('launch', 'dev', 'web'),
        ('launch', 'dev', 'api'),
        ('launch', 'test', 'web'),
        ('launch', 'test', 'api'),
        ('launch', 'prod', 'web'),
        ('launch', 'prod', 'api')
    ]


# Generated at 2022-06-13 12:51:10.058538
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    """
    Unit test to check that this function adds one parent to the child,
    and then recursively applies the same operation by adding one
    parent to another child.
    """

    # Create an InventoryModule
    i_m = InventoryModule()
    # Create an inventory to be passed as argument
    inventory = BaseInventoryPlugin(name='test')
    # Create the children template variables passed as argument
    template_child = {'app1': 'app1', 'env1': 'env1'}
    # Create the parents template variables passed as argument
    template_parents = {'app1': 'app1', 'env1': 'env1'}
    # Create the parent tree to be passed as argument
    parent = {'name': 'app_{{ app1 }}_{{ env1 }}'}
    parents = [parent]

# Generated at 2022-06-13 12:51:15.610094
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()
    assert inventory.verify_file("inventory.config") == True
    assert inventory.verify_file("inventory.yml") == True
    assert inventory.verify_file("inventory.ini") == True
    assert inventory.verify_file("inventory.json") == True
    assert inventory.verify_file("inventory.yaml") == True

# Generated at 2022-06-13 12:51:20.159139
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    i = InventoryModule()
    assert i.verify_file('/test/test/test.config') == True
    assert i.verify_file('/test/test/test.yaml') == True
    assert i.verify_file('/test/test/test') == False


# Generated at 2022-06-13 12:51:24.274344
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    import copy
    import unittest
    import ansible.plugins.loader as loader
    from ansible.plugins.inventory import InventoryBase
    import ansible.plugins.inventory.base as base

    class TestInventoryModule(InventoryModule):

        def __init__(self):
            super(TestInventoryModule, self).__init__()

        def set_inventory(self, inventory):
            self.inventory = inventory

        def template(self, pattern, variables):
            return pattern

    class TestInventoryManager(InventoryBase):

        def __init__(self):
            super(TestInventoryManager, self).__init__()
            self._hosts = {}
            self._patterns = {}
            self._hosts_cache = {}
            self._vars_per_host = {}

# Generated at 2022-06-13 12:51:33.859710
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    inv = InventoryModule()

    # Testing with a valid config file
    path = os.path.join(os.path.dirname(__file__), "../../plugins/inventory/test.config")
    assert inv.verify_file(path)

    # Testing with a valid YAML file
    path = os.path.join(os.path.dirname(__file__), "../../plugins/inventory/test.yml")
    assert inv.verify_file(path)

    # Testing with a valid YAML file
    path = os.path.join(os.path.dirname(__file__), "../../plugins/inventory/test.yaml")
    assert inv.verify_file(path)

    # Testing with a valid YAML file

# Generated at 2022-06-13 12:51:44.095053
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    config = {
      "layers": {
        "environment": ["dev", "test", "prod"],
        "application": ["web", "api"]
      },
      "hosts": {
        "name": "{{ application }}_{{ environment }}",
        "parents": [{
          "name": "{{ application }}",
          "vars": {
            "application": "{{ application }}"
          }
        }, {
          "name": "{{ environment }}",
          "vars": {
            "environment": "{{ environment }}"
          }
        }]
      }
    }
    inventory.parse(config)
    assert 'web_dev' in inventory._inventory.hosts
    assert 'web_test' in inventory._inventory.hosts
    assert 'web_prod' in inventory._

# Generated at 2022-06-13 12:51:51.121728
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    class Inventory():
        def __init__(self):
            self.groups = {}
    class InventoryModule():
        def __init__(self, inventory, loader, path, cache=False):
            self.inventory = inventory
            self.loader = loader
            self.path = path
            self.cache = cache
        def _read_config_data(self, path):
            layers = {
                'operation': ['build', 'launch'],
                'environment': ['dev', 'test', 'prod'],
                'application': ['web', 'api']
            }

# Generated at 2022-06-13 12:51:56.779125
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    # Setup
    counters = {'inventory.add_group.call_count':0,
                'inventory.add_child.call_count':0,
                'group.set_variable.call_count':0}

    class Inventory_mock(object):
        def __init__(self, counters):
            self._counters = counters
        def add_group(self, name):
            self._counters['inventory.add_group.call_count'] += 1
            return name
        def add_host(self, name):
            self._counters['inventory.add_host.call_count'] += 1
            return name
        def add_child(self, group, child):
            self._counters['inventory.add_child.call_count'] += 1
            return group

# Generated at 2022-06-13 12:52:47.711726
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    import unittest.mock as mock
    import collections

    Group = collections.namedtuple('Group', ['name'])

    inventory = mock.Mock()
    inventory.add_group = mock.Mock(side_effect=(lambda x: Group(name=x)))
    inventory.add_child = mock.Mock(side_effect=(lambda x, y: None))
    inventory.groups = {'master': Group(name='master'), 'generic': Group(name='generic')}
    im = InventoryModule()


# Generated at 2022-06-13 12:53:01.772524
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.plugins.inventory import BaseInventoryPlugin
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory, Host
    loader = DataLoader()
    inventory = Inventory(loader)

    inventory_module = InventoryModule()

    inventory_module.verify_file = lambda path: True

    inventory_module.parse(inventory, loader, '.')

    # Check that the root host and all its parents have been created
    assert inventory.hosts['build_api_prod_runner'] is not None
    assert inventory.hosts['build_api_prod'] is not None
    assert inventory.hosts['build_api'] is not None
    assert inventory.hosts['build'] is not None
    assert inventory.hosts['api_prod'] is not None
    assert inventory.hosts

# Generated at 2022-06-13 12:53:12.060789
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    c = InventoryModule()

    class inventory:
        def __init__(self):
            self.groups = dict()

        def add_group(self, groupname):
            self.groups[groupname] = group('group')

        def add_child(self, groupname, child):
            self.groups[groupname].children.append(child)

    class group:
        def __init__(self, name):
            self.name = name
            self.children = []

        def set_variable(self, k, v):
            self.children.append((k, v))

    inventory = inventory()
    inventory.add_group('parent')

    c.add_parents(inventory, 'child',
                  [{'name': 'parent'}],
                  dict())

# Generated at 2022-06-13 12:53:21.724306
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    import pytest
    tmp_path = pytest.ensuretemp('inventories')
    config_path = tmp_path.join('inventory.config')

# Generated at 2022-06-13 12:53:27.079954
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Arragne
    # Create object of class InventoryModule
    inventory_module = InventoryModule()
    # Create object of class InventoryData
    inventory_data = InventoryData()

    # Act
    inventory_module.parse(inventory_data, "loader", "path", False)

    # Assert
    expected_result = ("ok", None)
    assert result == expected_result


# Generated at 2022-06-13 12:53:37.946912
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    class args:
        # no args are required
        def __init__(self):
            pass

    # setup
    inventory = InventoryModule()
    inventory.args = args()

    # test invalid files
    assert not inventory.verify_file('/a/b/c/d.txt')
    assert not inventory.verify_file('/a/b/c/d.yml')
    assert not inventory.verify_file('/a/b/c/d.yaml')
    assert not inventory.verify_file('/a/b/c/d.json')

    # test valid files
    assert inventory.verify_file('/a/b/c/d.config')
    assert inventory.verify_file('/a/b/c/d')

    # setup

# Generated at 2022-06-13 12:53:44.648431
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    # Setup test data
    inventory = InventoryModule()
    template_vars = {'operation': 'build',
                    'environment': 'dev',
                    'application': 'web'}
    # Unit Test
    test_template_string = "{{ operation }}_{{ application }}_{{ environment }}_runner"
    assert inventory.template(test_template_string, template_vars) == "build_web_dev_runner"


# Generated at 2022-06-13 12:53:51.634003
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    # Create configuration template
    config = dict()
    config['hosts'] = dict()
    config['hosts']['name'] = "{{ operation }}_{{ application }}_{{ environment }}_runner"
    config['hosts']['parents'] = list()
    parent = dict()
    parent['name'] = "{{ operation }}_{{ application }}_{{ environment }}"
    parent['parents'] = list()
    sub_parent1 = dict()
    sub_parent1['name'] = "{{ operation }}_{{ application }}"
    sub_parent1['parents'] = list()
    sub_sub_parent1 = dict()
    sub_sub_parent1['name'] = "{{ operation }}"
    sub_parent1['parents'].append(sub_sub_parent1)
    sub_sub_parent2 = dict()
    sub_

# Generated at 2022-06-13 12:53:58.010110
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    test_obj = InventoryModule()
    # verify_file has not returns for correct filepath
    assert test_obj.verify_file("/usr/local/bin/sample_ansible_inventory_file.yml") == True
    # verify_file has not returns for incorrect filepath
    assert test_obj.verify_file("/usr/local/bin/sample_ansible_inventory_file.csv") == False


# Generated at 2022-06-13 12:54:05.803222
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import unittest
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from test.unit import MockLoader, MockOptions
    from ansible.inventory.manager import InventoryManager