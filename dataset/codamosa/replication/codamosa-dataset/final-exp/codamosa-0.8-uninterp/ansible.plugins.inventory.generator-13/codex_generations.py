

# Generated at 2022-06-13 12:44:32.122589
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    path = "abc.config"
    result = inv.verify_file(path)
    assert result == True
    path = "abc.ini"
    result = inv.verify_file(path)
    assert result == False
    path = "abc"
    result = inv.verify_file(path)
    assert result == True
    path = ""
    result = inv.verify_file(path)
    assert result == False
    path = "abc.yml"
    result = inv.verify_file(path)
    assert result == True
    path = "abc.yaml"
    result = inv.verify_file(path)
    assert result == True

# Generated at 2022-06-13 12:44:44.953754
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    """ Unit test for method add_parents of class InventoryModule """

    config = {
        'hosts': {
            'name': 'MyHost',
            'parents': [
                {
                    'name': 'Group1',
                    'parents': [
                        {
                            'name': 'Group2',
                            'parents': [
                                {
                                    'name': 'Group3'
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        'layers': {
            'key1': (1, 2),
            'key2': (3, 4, 5),
            'key3': ('a', 'b')
        }
    }

    inventory = InventoryModule()

    # Ensure that group with no name element is given raises exception.
    raised = False

# Generated at 2022-06-13 12:44:55.252421
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Patch sets variables in the plugin configuration.
    def setup_plugin_configuration(self):
        self.plugin_vars = {}
        return {}
    BaseInventoryPlugin.setup_plugin_configuration = setup_plugin_configuration

    # This is the configuration for the plugin
    config = {
        'plugin': 'generator',
        'hosts': {
            'name': '{{ testing }}',
            'parents': [{
                'name': '{{ test }}{{ environment }}',
                'vars': {'testenv': '{{ environment }}'},
                'parents': [{ 'name': '{{ operation }}' }]}]},
        'layers': {
            'test': ['one', 'two'],
            'operation': ['run'],
            'environment': ['test']}}

    # Dummy configuration file


# Generated at 2022-06-13 12:45:10.637356
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    '''
    Testcase for method:
    add_parents(self, inventory, child, parents, template_vars)
    under class InventoryModule
    '''

    inv = InventoryModule()
    inventory = {
        'group1': {'hosts': []},
        'group2': {'hosts': []},
        'group3': {'hosts': []},
        'group4': {'hosts': []},
        'group5': {'hosts': []},
        'group6': {'hosts': []},
    }
    child = 'group1'

# Generated at 2022-06-13 12:45:20.614837
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    inventory = None
    loader = None
    path = './inventory.config'
    cache = False

    inventory_module = InventoryModule()

    # verify template parsing function
    config = inventory_module._read_config_data(path)
    inventory_module.verify_file(path)

    # verify parent group
    inventory_module.add_parents(inventory, 'host1', config['hosts'][1]['parents'], {
        'operation': 'build',
        'environment': 'dev',
        'application': 'web'
    })

    # verify host resolver function
    inputs = product(*config['layers'].values())
    variables = inputs.next()
    host = inventory_module.template(config['hosts']['name'], variables)

    print(host)

# Generated at 2022-06-13 12:45:27.435081
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    import unittest
    import ansible.parsing.yaml
    import ansible.inventory
    import sys

    config = ansible.parsing.yaml.load(EXAMPLES)
    inventory = ansible.inventory.Inventory()
    module = InventoryModule()
    module.parse(inventory, None, None, cache=False)


# Generated at 2022-06-13 12:45:34.294757
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import pytest

    plugin = InventoryModule()

    inventory = InventoryModule.Inventory('hosts')

    loader = pytest.Mock()

    path = 'path/to/inventory.config'

    with pytest.raises(AttributeError):
        config = plugin._read_config_data(path)

    config = plugin._read_config_data(path, config_data='plugin: generator')
    with pytest.raises(AttributeError):
        plugin.parse(inventory, loader, path)


# Generated at 2022-06-13 12:45:46.456597
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    from ansible.plugins.inventory import BaseInventoryPlugin
    from ansible.plugins.loader import InventoryLoader

    module = BaseInventoryPlugin()

    # Unit test for method verify_file of class InventoryModule with
    # an inventory.config file in YAML format


# Generated at 2022-06-13 12:45:48.389205
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    mod = InventoryModule()
    inventory = mod.parse(inventory, loader, path, cache=False)
    assertInventory(inventory)


# Generated at 2022-06-13 12:45:58.114444
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class Options:
        def __init__(self, verbosity=None):
            self.verbosity = None
            self.connection = None
            self.module_path = None
            self.forks = None
            self.remote_user = None
            self.private_key_file = None
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra_args = None
            self.become = None
            self.become_method = None
            self

# Generated at 2022-06-13 12:46:10.475565
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    
    def verify(input, expected_output):
        inventory = InventoryModule()
        actual_output = inventory.template(input, variables)
        assert actual_output == expected_output

    variables = {}
    verify('', '')
    verify('aws', 'aws')
    variables['data_center'] = 'aws'
    verify('{{ data_center }}', 'aws')

    variables['data_center'] = 'aws'
    variables['application'] = 'tornado'
    variables['environment'] = 'dev'

    verify('{{ application }}_{{ environment }}_{{ data_center }}', 'tornado_dev_aws')
    verify('{{ application }}_{{ environment }}_{{ data_center }}_{{ data_center }}', 'tornado_dev_aws_aws')


# Generated at 2022-06-13 12:46:16.453283
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Mock inventory object
    inventory = create_autospec(Inventory)

    # Mock loader object
    loader = create_autospec(Reader)

    # Mock parser object
    parser = create_autospec(Parser)

    # Mocked template_vars
    template_vars = {'a': 'b', 'c': 'd'}

    # Valid config data
    config = {
        'hosts': {
            'name': 'myhost'
        },
        'layers': {
            'key1': ['val1'],
            'key2': ['val2']
        }
    }

    # Mocked template function
    def template(pattern, variables):
        return 'myhost'

    # Call parse method

# Generated at 2022-06-13 12:46:22.557417
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    """ Test case to validate the correctness of add_parents method of class InventoryModule """

    import json
    import re
    import unittest

    # Example configuration for test_add_parents
    # hosts:
    #    name: "{{ operation }}_{{ application }}_{{ environment }}_runner"
    #    parents:
    #      - name: "{{ operation }}_{{ application }}_{{ environment }}"
    #        parents:
    #          - name: "{{ operation }}_{{ application }}"
    #            parents:
    #              - name: "{{ operation }}"
    #              - name: "{{ application }}"
    #          - name: "{{ application }}_{{ environment }}"
    #            parents:
    #              - name: "{{ application }}"
    #                vars:
    #                  application: "{{ application }}"

# Generated at 2022-06-13 12:46:35.791843
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    loader = AnsibleLoader(module_utils)
    yaml_file = AnsibleLoader(module_utils).load_from_file("./tests/fixtures/inventory.config")
    inventory = Inventory(loader=loader)
    InventoryModule().parse(inventory, loader, None, cache=False)

    for host, host_entry in inventory.hosts.items():
        if host == 'build_web_dev_runner':
            assert host_entry.name == 'build_web_dev_runner'

            assert host_entry.vars.keys() == set(host_entry.get_host_keys())
            assert host_entry.vars['environment'] == 'dev'
            assert host_entry.vars['application'] == 'web'

            parents = map(lambda x: x.name, host_entry.get_parents())

# Generated at 2022-06-13 12:46:36.431995
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    pass

# Generated at 2022-06-13 12:46:39.147035
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_module = InventoryModule()
    valid_extension = '.config'
    ext = '.notvalid'
    for e in C.YAML_FILENAME_EXTENSIONS:
        assert inventory_module.verify_file('inventory' + e)
    assert inventory_module.verify_file('inventory' + valid_extension)
    assert not inventory_module.verify_file('inventory' + ext)
    assert not inventory_module.verify_file('inventory')

# Generated at 2022-06-13 12:46:45.106149
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Instantiate an object of class InventoryModule
    obj_module = InventoryModule()

    # Test with a valid file
    path = 'inventory.config'
    result = obj_module.verify_file(path)
    assert result == True

    # Test with an invalid file
    path = 'inventory.txt'
    result = obj_module.verify_file(path)
    assert result == False

# Generated at 2022-06-13 12:46:47.209681
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory_obj = InventoryModule()
    # inventory_obj.parse(inventory, loader, path, cache=False)

# Generated at 2022-06-13 12:46:59.125593
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    """
    Constructs a parent child relationship defined by the parents parameter
    """

    # Arrange
    inventory = {}
    child = {}
    parents = [{'name': '{{ operation }}_{{ application }}_{{ environment }}', 'parents': [{'name': '{{ operation }}_{{ application }}', 'parents': [{'name': '{{ operation }}'}, {'name': '{{ application }}'}]}, {'name': '{{ application }}_{{ environment }}', 'parents': [{'name': '{{ application }}', 'vars': {'application': '{{ application }}'}}, {'name': '{{ environment }}', 'vars': {'environment': '{{ environment }}'}}]}]}, {'name': 'runner'}]

# Generated at 2022-06-13 12:47:07.735359
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from unittest import TestCase
    import ansible.inventory.Inventory as Inventory
    import ansible.plugins.inventory.Generator as Generator
    class TestInventoryModule_add_parents(TestCase):
        def setUp(self):
            self.generator = Generator.InventoryModule()
            self.inventory = Inventory.Inventory()

        def test_add_parents_single(self):
            generator = self.generator
            inventory = self.inventory
            generator.add_parents(inventory,
                'host',
                [
                 {'name': '{{ application }}',
                  'vars': {
                            'application': '{{ application }}'
                        }
                }
                ],
                {'application': 'app-name'}
                )
            self.assertIn('app-name', inventory.groups)

# Generated at 2022-06-13 12:47:16.987893
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    im = InventoryModule()
    path1 = "test1.config"
    path2 = "test2.yml"
    path3 = "test3.yaml"
    path4 = "test4.py"
    assert im.verify_file(path1)
    assert im.verify_file(path2)
    assert im.verify_file(path3)
    assert not im.verify_file(path4)

# Generated at 2022-06-13 12:47:27.409704
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # Test with an valid config file
    fake_loader = None
    fake_path = '/foo/bar/'
    fake_cache = False # Not a boolean
    
    fake_inventory = C()
    fake_inventory.hosts  = {}
    fake_inventory.groups = {}
    fake_inventory.add_host = lambda self, host: self.hosts.update({host : []})
    fake_inventory.add_group = lambda self, group: self.groups.update({group : []})
    fake_inventory.add_child = lambda self, group, child: self.groups.get(group, []).append(child)
    
    fake_inventory_module = InventoryModule()
    fake_inventory_module.templar = C()
    fake_inventory_module.templar.do_template = lambda self, pattern: pattern

# Generated at 2022-06-13 12:47:36.355818
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # TODO: inventory.py is a temporary expected result only, should be done by ansible-inventory -i inventory.config --list
    # TODO: seperate file for expected result
    arg_vars = {'operation': 'build', 'application': 'web', 'environment': 'dev'}
    inventory = {'all': {'children': {'env_dev': {'children': {'web': {'children': {'build_web_dev': {'hosts': {'build_web_dev_runner': {}}}}}}}}}, '_meta': {'hostvars': {'build_web_dev_runner': {}}}}

# Generated at 2022-06-13 12:47:38.981093
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Note: This test is for 'verify_file' method of ansible plugin
    # 'InventoryModule' of module 'inventory_plugins/generator.py'
    pass

# Generated at 2022-06-13 12:47:48.855116
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.plugins.loader import inventory_loader

    inventory = inventory_loader.get("generator", {})
    test_filename = os.environ.get("TEST_INVENTORY_CONFIG_FILE", "")
    if not os.path.exists(test_filename):
        raise Exception("No config file found in environment, expected path '{}'".format(test_filename))


# Generated at 2022-06-13 12:47:56.241739
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost']))

    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)
    play_source = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Hello Ansible!')))
        ]
    )

# Generated at 2022-06-13 12:48:07.635117
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    '''
    Check that the correct parents are added to the host
    '''
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(environment='dev', application='web', operation='build')
    inventory = dict()
    setattr(inventory, 'groups', dict())
    setattr(inventory, 'add_group', add_group)
    setattr(inventory, 'add_child', add_child)
    setattr(inventory, 'add_host', add_host)
    host = 'build_web_dev_runner'

# Generated at 2022-06-13 12:48:13.719287
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    assert inv.verify_file('my_inventory.config') == True
    assert inv.verify_file('my_inventory.yml') == True
    assert inv.verify_file('my_inventory.yaml') == True
    assert inv.verify_file('my_inventory.ymlz') == False
    assert inv.verify_file('my_inventory_without_extension') == True


# Generated at 2022-06-13 12:48:24.876922
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    
    # Create fake YAML config and fake inventory file path
    yaml_config = {}
    yaml_config['plugin'] = 'generator'
    yaml_config['layers'] = {
        'operation': ['build','launch'],
        'environment': ['dev','test','prod'],
        'application': ['web','api']
    }
    yaml_config['hosts'] = {}
    yaml_config['hosts']['name'] = '{{ operation }}_{{ application }}_{{ environment }}_runner'
    yaml_config['hosts']['parents'] = []

# Generated at 2022-06-13 12:48:27.325848
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    plugin = InventoryModule()

    path = "my_inventory"
    path_return = plugin.verify_file(path)
    assert path_return is True


# Generated at 2022-06-13 12:48:32.722861
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    file_name = __file__
    result = module.verify_file(file_name)

    assert result is False, "validating file name with wrong extension"


# Generated at 2022-06-13 12:48:37.012800
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    m = InventoryModule()
    assert m.template("{{ foo }} bar ", {"foo": "test"}) == "test bar "
    assert m.template("{{ foo |upper }} bar ", {"foo": "test"}) == "TEST bar "



# Generated at 2022-06-13 12:48:42.552695
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    filename = 'inventory.config'
    plugin = InventoryModule()
    # Verify that 'inventory.config' is a correct file for the generator plugin
    assert plugin.verify_file(filename)
    # Verify that 'inventory.config' is a correct file for the generator plugin
    filename = 'inventory.ini'
    assert not plugin.verify_file(filename)


# Generated at 2022-06-13 12:48:51.824721
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:48:56.506434
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    myinv = InventoryModule()
    # Test default extension .config
    assert(myinv.verify_file('inventory.config'))
    # Test other YAML extension
    assert(myinv.verify_file('inventory.yaml'))
    assert(myinv.verify_file('inventory.yml'))
    # Test no extension
    assert(myinv.verify_file('inventory'))
    # False case
    assert(not myinv.verify_file('inventory.json'))


# Generated at 2022-06-13 12:49:08.834334
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:49:22.260419
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    from ansible.module_utils.six import PY2
    if PY2:
        from ansible.parsing.yaml.objects import AnsibleUnicode

    inventory = InventoryModule()

    result = inventory.template('{{ operation }}_{{ application }}_{{ environment }}_runner',
                                {'operation': 'build',
                                 'application': 'web',
                                 'environment': 'dev'})
    assert result == 'build_web_dev_runner'
    if PY2:
        assert type(result) is AnsibleUnicode

    result = inventory.template('{{ operation }}_{{ application }}_{{ environment }}_runner',
                                {'operation': 'launch',
                                 'application': 'api',
                                 'environment': 'test'})
    assert result == 'launch_api_test_runner'


# Generated at 2022-06-13 12:49:28.565114
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    m = InventoryModule()
    path = "ansible_hosts.config"
    expected_outcome = True
    actual_outcome = m.verify_file(path)
    assert actual_outcome == expected_outcome
    path = "ansible_hosts.yml"
    expected_outcome = True
    actual_outcome = m.verify_file(path)
    assert actual_outcome == expected_outcome
    path = "ansible_hosts.yaml"
    expected_outcome = True
    actual_outcome = m.verify_file(path)
    assert actual_outcome == expected_outcome
    path = "ansible_hosts.py"
    expected_outcome = False
    actual_outcome = m.verify_file(path)
    assert actual_outcome

# Generated at 2022-06-13 12:49:41.945603
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 12:49:53.720139
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import sys
    import json

    if sys.version_info[0] < 3:
        from mock import patch, MagicMock, Mock
    else:
        from unittest.mock import patch, MagicMock, Mock

    # Patch open function
    with patch(__name__ + '.open', create=True) as mock_open:
        # Patch ansible.plugins.inventory.base.BaseInventoryPlugin.parse
        with patch('ansible.plugins.inventory.base.BaseInventoryPlugin.parse') as mock_base_parse:
            mock_base_parse.return_value = None

            # Patch helper methods

# Generated at 2022-06-13 12:50:06.033443
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule()
    p = 'import os; Config = {}; Config["layers"] = {}; Config["hosts"] = {}; Config["hosts"]["name"] = "{{ operation }}_{{ application }}_{{ environment }}_runner"; Config["layers"]["operation"] = []; Config["layers"]["operation"].append("build"); Config["layers"]["operation"].append("launch"); Config["layers"]["environment"] = []; Config["layers"]["environment"].append("dev"); Config["layers"]["environment"].append("test"); Config["layers"]["environment"].append("prod"); Config["layers"]["application"] = []; Config["layers"]["application"].append("web"); Config["layers"]["application"].append("api")'

# Generated at 2022-06-13 12:50:14.179297
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    path = "unit_test_file"
    assert plugin.verify_file(path) == True
    assert plugin.verify_file(path + ".test") == True
    assert plugin.verify_file(path + ".yaml") == True
    assert plugin.verify_file(path + ".yml") == True
    assert plugin.verify_file(path + ".json") == True
    assert plugin.verify_file(path + ".txt") == False

# Generated at 2022-06-13 12:50:25.741482
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    '''Template method test'''
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.vars import VariableManager
    from ansible.module_utils._text import to_native

    AnsibleConfigBase = './test/unit/plugins/inventory'
    test_file = tempfile.NamedTemporaryFile(mode="w+t")

# Generated at 2022-06-13 12:50:36.373161
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.plugins.loader import inventory_loader

    inventory = inventory_loader.get('generator', class_only=True)()
    inventory.add_group('a')
    inventory.add_group('b')
    inventory.add_group('c')
    inventory.add_group('d')

    # hosts:
    #   name: "{{ operation }}_{{ application }}_{{ environment }}_runner"
    #   parents:
    #     - name: "{{ operation }}_{{ application }}_{{ environment }}"
    #       parents:
    #         - name: "{{ operation }}_{{ application }}"
    #           parents:
    #             - name: "{{ operation }}"
    #             - name: "{{ application }}"
    #         - name: "{{ application }}_{{ environment }}"
    #           parents:


# Generated at 2022-06-13 12:50:45.269269
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inventory = {}
    inventory['_meta'] = {}
    inventory['_meta']['hostvars'] = {}
    loader = DataLoader()
    variable_manager = VariableManager()

    im = InventoryModule()
    im.parse(inventory, loader, "")

    # no group created
    assert(not inventory.get('_meta'))



# Generated at 2022-06-13 12:50:53.545264
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    IM = InventoryModule()
    inventory = {}
    vars = {'a': '1', 'b': '2'}
    child = {}
    parents = [{'name': 'c_1_2', 'parents': [{'name': 'c_1'}, {'name': 'c_2'}], 'vars': {'z': '0'}}]
    IM.add_parents(inventory, child, parents, vars)
    assert inventory['c_1_2']['z'] == '0'
    assert len(inventory) == 3
    assert len(inventory['c_1_2']) ==  4
    assert inventory['c_1_2']['children'] == [child]
    assert child in inventory['c_2']['children']

# Generated at 2022-06-13 12:51:06.879670
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.plugins.inventory import BaseInventoryPlugin
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[
                                 'localhost, application=app1, environment=test, operation=build'])
    variable_manager.set_inventory(inventory)
    generator = InventoryModule()
    group1 = Group('group1')
    group2 = Group('group2')
    group3 = Group('group3')


# Generated at 2022-06-13 12:51:11.075155
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    inventory = MockInventory()
    module = InventoryModule()
    child = "child"
    parents = [{'name': 'parent'}]
    template_vars = {'key': 'value'}
    module.add_parents(inventory, child, parents, template_vars)
    assert inventory.groups['parent'].children == ['child']
    assert inventory.groups['parent'].parents == ['']


# Generated at 2022-06-13 12:51:13.679979
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    inv = InventoryModule()
    assert inv.template('{{ x }}', {'x': 'hello world'}) == 'hello world'

# Generated at 2022-06-13 12:51:17.989185
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    assert module.verify_file('sample.config')
    assert module.verify_file('sample.yml')
    assert not module.verify_file('sample.yaml')
    assert not module.verify_file('sample')


# Generated at 2022-06-13 12:51:27.374775
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import ansible.plugins.inventory.generator.InventoryModule
    inv = ansible.plugins.inventory.generator.InventoryModule()
    assert 'parse' in dir(inv)
    # TODO: Write tests for verify_file and template

# Generated at 2022-06-13 12:51:31.674232
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    assert not module.verify_file("/tmp/somefile.csv")
    assert module.verify_file("/tmp/somefile.yml")
    assert module.verify_file("/tmp/somefile")
    assert module.verify_file("/tmp/somefile.config")


# Generated at 2022-06-13 12:51:38.310892
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    class FakeInventory(dict):

        def __init__(self):
            super(FakeInventory, self).__init__()

        def add_group(self, name):
            self[name] = FakeGroup(name)

        def add_host(self, name):
            self[name] = FakeGroup(name)

        def add_child(self, child, parent):
            self[parent].add_child(self[child])

    class FakeGroup(object):

        def __init__(self, name):
            self.name = name
            self.children = []

        def set_variable(self, key, value):
            setattr(self, key, value)

        def add_child(self, child):
            self.children.append(child)

    inventory = FakeInventory()

# Generated at 2022-06-13 12:51:47.724545
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    inv = InventoryModule()

    # Path without file extension
    path = os.path.join(os.path.dirname(__file__), 'inventory.config')
    assert(inv.verify_file(path))

    # Path with supported configuration file extension
    path = os.path.join(os.path.dirname(__file__), 'inventory_yaml.config')
    assert(inv.verify_file(path))

    # Path with unsupported configuration file extension
    path = os.path.join(os.path.dirname(__file__), 'inventory.ini')
    assert(inv.verify_file(path) == False)

    # Path without file extension and without file
    path = os.path.join(os.path.dirname(__file__), 'inventory_without_file.config')

# Generated at 2022-06-13 12:51:58.485914
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import mock
    mock_inventory = mock.Mock()
    mock_loader = mock.Mock()
    mock_path = mock.Mock()
    mock_cache = mock.Mock()
    InventoryModule().parse(mock_inventory, mock_loader, mock_path, cache=mock_cache)
    assert mock_inventory.groups == {}

    mock_config = {'layers': {'zone': ['a', 'b'], 'role': ['c', 'd']}, 'hosts': {'name': '{{ zone }}_{{ role }}'}}
    mock_inventory = mock.Mock()
    mock_loader = mock.Mock()
    mock_path = mock.Mock()
    mock_cache = mock.Mock()

# Generated at 2022-06-13 12:52:07.215341
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    file_name, ext = os.path.splitext("test.config")

    inventoryModule = InventoryModule()
    assert inventoryModule.verify_file("test.config")
    assert not inventoryModule.verify_file("test.cfg")
    assert not inventoryModule.verify_file("test")
    assert not inventoryModule.verify_file("test.txt")
    assert not inventoryModule.verify_file("test.yaml")

# Generated at 2022-06-13 12:52:08.545530
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
	inventory_module = InventoryModule();

# Generated at 2022-06-13 12:52:13.401182
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    global InventoryModule
    inventory = object()
    child = object()
    parents = object()
    template_vars = object()
    InventoryModule.add_parents(inventory, child, parents, template_vars)



# Generated at 2022-06-13 12:52:19.179349
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import mock
    import unittest

    InventoryModule.InventoryModule._read_config_data = mock.Mock(return_value =
        {
            'hosts': {
                'name': '{{ first }}_{{ second }}',
            },
            'layers': {
                'first': [
                    'hello',
                    'goodbye',
                ],
                'second': [
                    'world',
                ],
            },
        }
    )
    InventoryModule.InventoryModule.template = mock.Mock(side_effect = lambda pattern, variables: pattern.replace('{{ ', '').replace(' }}', ''))

    def _add_host(host):
        inventory.hosts[host] = {'vars': {}}
        inventory.add_group(host)
        inventory.add_child(host, host)



# Generated at 2022-06-13 12:52:30.269939
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Validates that given a valid inventory.config file, we can parse it
    correctly and generate groups and vars with given patterns.
    """
    from ansible.cli.playbook import PlaybookCLI
    from ansible.plugins.loader import inventory_loader
    import sys

    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'inventory.config')
    args = [config_file]

    pb = PlaybookCLI(args)
    pb.parse()
    pb.inventory.subset(pb.options.subset)

    print("Found the following groups:")
    for group in pb.inventory.groups:
        print('  ' + group.name)

    # validate that some specific groups were created

# Generated at 2022-06-13 12:52:45.136995
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    my_obj = InventoryModule()
    assert not my_obj.verify_file("abc.yaml")
    assert not my_obj.verify_file("abc.txt")
    assert my_obj.verify_file("inventory.config")



# Generated at 2022-06-13 12:52:58.761410
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    host = Host('localhost')
    g = Group('some_group')
    host.add_group('some_group')
    i = InventoryManager(loader=loader, sources=['localhost', 'some_group'])
    m = InventoryModule()

    # Normal use case
    m.add_parents(i, host, [{'name': '{{ foo }}', 'parents': [{'name': 'parent_group'}]}], {'foo': 'bar'})
    assert i.groups['bar'].get_hosts() == [host.name]

# Generated at 2022-06-13 12:53:10.491382
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # mock inventory and loader
    class inventory:
        def __init__(self):
            self.hosts = {}
            self.groups = {}

        def add_host(self, host):
            if host not in self.hosts:
                self.hosts[host] = True

        def add_group(self, host):
            if host not in self.groups:
                self.groups[host] = [host]

        def add_child(self, group, host):
            if group not in self.groups:
                self.groups[group] = [host]
            else:
                self.groups[group].append(host)

    class loader:
        def __init__(self):
            pass

        def get_basedir(self):
            return os.getcwd()

    inventory_mock = inventory()
   

# Generated at 2022-06-13 12:53:19.927809
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory


# Generated at 2022-06-13 12:53:24.960226
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    assert plugin.verify_file('inventory.config') is True
    assert plugin.verify_file('inventory.yaml') is True
    assert plugin.verify_file('inventory.yml') is True
    assert plugin.verify_file('inventory') is True
    assert plugin.verify_file('inventory.txt') is False


# Generated at 2022-06-13 12:53:32.788950
# Unit test for method add_parents of class InventoryModule
def test_InventoryModule_add_parents():

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    filename = "./inventory.config"

    # data is the dict object returned by _read_config_data for valid config file

# Generated at 2022-06-13 12:53:40.974907
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader

    inv_path = inventory_loader._get_path("inventory.yml")
    plugin = inventory_loader.get("generator", class_only=True)()
    assert plugin.verify_file(inv_path)
    inventory = inventory_loader.get("memory")
    plugin.parse(inventory, '', inv_path)
    assert "api_dev_runner" in inventory.hosts
    assert "build_web_dev" in inventory.groups
    assert "build_web" in inventory.groups
    assert "build" in inventory.groups
    assert inventory.groups["build_web_dev"].get_vars()['environment'] == 'dev'
    assert not inventory.groups["build"].get_vars()



# Generated at 2022-06-13 12:53:49.811262
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import collections

    test_inventory_path = './tests/inventory/config_generator'
    inventory_module = InventoryModule()
    inventory = collections.defaultdict(dict, {
        '_meta': {
            'hostvars': collections.defaultdict(dict)
        }
    })

    inventory_module.parse(inventory, None, test_inventory_path)

    assert inventory['_meta']['hostvars']['build_web_dev_runner'] == {}
    assert inventory['_meta']['hostvars']['build_web_test_runner'] == {}
    assert inventory['_meta']['hostvars']['build_web_prod_runner'] == {}
    assert inventory['_meta']['hostvars']['build_api_dev_runner'] == {}

# Generated at 2022-06-13 12:53:52.971573
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    gen_inv = InventoryModule()
    assert gen_inv.verify_file("inventory.config")
    assert not gen_inv.verify_file("inventory.txt")

# Generated at 2022-06-13 12:54:02.875425
# Unit test for method add_parents of class InventoryModule

# Generated at 2022-06-13 12:54:20.238531
# Unit test for method template of class InventoryModule
def test_InventoryModule_template():
    import ansible.plugins.inventory
    # pylint: disable=protected-access
    module = ansible.plugins.inventory.InventoryModule()

    template_vars = {
        'operation': 'action',
        'application': 'app',
    }

    result = module.template('{{operation}}_{{application}}', template_vars)
    assert result == 'action_app'