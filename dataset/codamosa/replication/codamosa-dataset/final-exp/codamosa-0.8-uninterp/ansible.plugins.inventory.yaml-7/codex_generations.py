

# Generated at 2022-06-13 13:05:41.827600
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Run this test only when YAML is available
    try:
        import yaml
    except ImportError:
        return
    yaml_str = '''all:
    children:
        group1:
            hosts:
                host1:
                host2:
                    hostvars:
                        hostvar1: var1val
        group2:
            hosts:
                host3:
                    hostvars:
                        hostvar2: var2val
'''
    tmp_path = '/tmp/yaml_test'
    with open(tmp_path, 'wb') as f:
        f.write(yaml_str)

    inventory = {}
    inventory_module = InventoryModule()

    # Parse the inventory file
    file_loader = FakeFileLoader(tmp_path)

# Generated at 2022-06-13 13:05:50.141733
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

# Generated at 2022-06-13 13:05:59.370542
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.inventory.myyaml import InventoryModule
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    import os

    loader_mock = Mock()
    path = os.path.join('..', 'plugins', 'inventory', 'test', 'test_example.yml')

    # An inventory file should start with all group

# Generated at 2022-06-13 13:06:06.894145
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # Test without extension
    # FIXME: This should be done as a test_utils unittest
    test_inventory_item = InventoryModule()
    assert not test_inventory_item.verify_file("foo")

    # Test with valid extension
    test_inventory_item = InventoryModule()
    test_inventory_item.get_option = lambda _: ['.yaml']
    assert test_inventory_item.verify_file("foo.yaml")

    # Test with invalid extension
    test_inventory_item = InventoryModule()
    test_inventory_item.get_option = lambda _: ['.yml']
    assert not test_inventory_item.verify_file("foo.yaml")

# Generated at 2022-06-13 13:06:13.639606
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.cli import CLI
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.inventory import InventoryDirectory
    from ansible.utils.vars import combine_vars

    my_parser = CLI.base_parser(connect_opts=True,
                                meta_opts=True,
                                runas_opts=True,
                                subset_opts=True,
                                check_opts=True,
                                diff_opts=True)
    my_parser.add_option('-i', '--inventory', dest="inventory",
                         help="Path to a inventory file to use as a source "
                              "of variables", default=None)

# Generated at 2022-06-13 13:06:23.391065
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.utils.display import Display
    from ansible.plugins.inventory import Inventory

    d = Display()
    yaml_dir = '/opt/test'
    yaml_file = '/opt/test/test.yaml'

# Generated at 2022-06-13 13:06:33.899505
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader

    my_inv = inventory_loader.get('yaml')

    data = my_inv.from_yaml('', '''
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
''')


# Generated at 2022-06-13 13:06:40.805127
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # Create the inventory plugin
    obj = InventoryModule()

    # YAML extension
    assert obj.verify_file("file.yaml")

    # JSON extension
    assert obj.verify_file("file.json")

    # None extension
    assert obj.verify_file("file")

    # Invalid extension
    assert not obj.verify_file("file.txt")


# Generated at 2022-06-13 13:06:50.772189
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    assert plugin.verify_file('hello.yaml') is True
    assert plugin.verify_file('hello.yaml') is True
    assert plugin.verify_file('hello.yml') is True
    assert plugin.verify_file('hello.json') is True
    assert plugin.verify_file('hello.yam') is False
    assert plugin.verify_file('hello.ya') is False
    assert plugin.verify_file('hello.yml') is True

    assert plugin.verify_file('hello.yaml', filename_ext=['yaml']) is True
    assert plugin.verify_file('hello.yaml', filename_ext=['yml']) is False
    assert plugin.verify_file('hello.yaml', filename_ext=['yaml'])

# Generated at 2022-06-13 13:07:01.869560
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    def _test_one( path, result ):
        module = InventoryModule()
        module.set_options()
        test_result = module.verify_file(path)
        assert test_result is result, "Returned %s for path %s, expected %s" % (test_result, path, result)

    # Test with invalid extensions
    _test_one( '/dev/null', False )
    _test_one( '/etc/hosts', False )
    _test_one( '/etc/hosts.txt', False )
    _test_one( '/etc/hosts.json.txt', False )

    # Test with valid extensions
    _test_one( '/etc/hosts.yaml', True )
    _test_one( '/etc/hosts.yml', True )

# Generated at 2022-06-13 13:07:18.164112
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    def _loader(path):
        return ''

    paths = ['/etc/ansible/hosts', '/etc/ansible/hosts.yaml', '/etc/ansible/hosts.yml', '/etc/ansible/hosts.json']

    for path in paths:
        inventory = InventoryManager(loader=DataLoader(), sources=paths)
        inventory.loader.load = _loader

        yaml_inventory = InventoryModule()
        assert yaml_inventory.verify_file(path)

# Generated at 2022-06-13 13:07:30.132954
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    def _get_plugin(data):

        class _InventoryModule(InventoryModule):

            def __init__(self):

                super(_InventoryModule, self).__init__()

            def verify_file(self, path):

                return True

        return _InventoryModule()

    plugin = _get_plugin(EXAMPLES)

    def parse_inventory(data, **kwargs):

        from ansible.inventory.manager import InventoryManager

        inventory_manager = InventoryManager(loader=None, sources=['test'])
        plugin.parse(inventory_manager, plugin.loader, 'test', cache=False)

    parse_inventory(EXAMPLES)

# Generated at 2022-06-13 13:07:31.555538
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    assert False


# Generated at 2022-06-13 13:07:40.417321
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    import os

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    inventory_file_path = os.path.join(current_dir_path, "yaml-example.yaml")

    manager = InventoryManager(loader=DataLoader())
    inventory = manager.load_inventory_from_source("my_yaml_inventory", source=inventory_file_path)

    assert isinstance(inventory, InventoryManager)
    assert len(inventory.get_groups()) == 6
    assert len(inventory.get_hosts()) == 6



# Generated at 2022-06-13 13:07:51.494765
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins import module_loader
    loader = module_loader._find_plugin('inventory', 'yaml')
    inventory = loader()
    inventory.loader.get_basedir = lambda: ''
    inventory.add_group = lambda group: group
    inventory.set_variable = lambda group, var, val: None
    inventory.add_child = lambda group, child: None
    inventory._populate_host_vars = lambda hostnames, vars, group, port: None
    inventory._expand_hostpattern = lambda host_pattern: (['a', 'b', 'c'], 1234)

    inventory.parse([], '', 'path')


# Generated at 2022-06-13 13:07:59.923469
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:08:15.192366
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    This unit test checks many corner cases of the the parse function in the method InventoryModule
    """

    ###################
    # Testing initial parsing
    ###################
    # Test a simple case
    yaml_inventory = '\n'.join([
        'all:',
        '    hosts:',
        '        test1:'
    ])

    inventory_plugin = InventoryModule()
    inventory_custom = inventory_plugin.parse(yaml_inventory, None, None)
    assert inventory_custom['all']['hosts']['test1'] is not None

    # Test with a multiple groups

# Generated at 2022-06-13 13:08:28.001773
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    This test will try to parse the EXAMPLES string with the InventoryModule class and ensure that the host, vars and
    children are appearing. The main focus of this test will be the child element.
    This will create the following data structure:
                    all
                   /  | \
                g1  g2  lg
               /  \    \   \
             hg1  hg2  hg4  hg1
    '''

    from ansible.plugins.loader import inventory_loader

    plugin = inventory_loader.get('yaml.yaml')
    assert isinstance(plugin, InventoryModule)

    # Set the options if any, there is none in this case
    plugin.set_options({
        "plugin": "yaml"
    })

    # Create the inventory
    inventory = plugin.inventory

# Generated at 2022-06-13 13:08:35.959405
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    '''
    Tests whether the verify_file method of the class InventoryModule works properly
    '''
    from ansible.parsing.plugin_docs import read_docstring

    plugin = InventoryModule()

    # test proper extension
    assert plugin.verify_file('my_file.yaml') is True
    assert plugin.verify_file('my_file.yml') is True

    # test wrong extension
    assert plugin.verify_file('my_file.ini') is False

    # test extension at all
    assert plugin.verify_file('my_file') is True


# Generated at 2022-06-13 13:08:39.572026
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = InventoryModule()
    parser = InventoryParser(loader=DictDataLoader({}))
    parser.inventory = inventory
    inventory._populate(parser, 'all', {}, None)


# Generated at 2022-06-13 13:08:53.854536
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_module = InventoryModule()

    result = inventory_module.verify_file("/foo/bar")
    assert result == False

    result = inventory_module.verify_file("inventory.yml")
    assert result == True

    result = inventory_module.verify_file("inventory.ini")
    assert result == False

# Generated at 2022-06-13 13:09:02.745508
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import inventory_loader

    loader = DataLoader()
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    inventory_path = os.path.join(path, 'test/units/plugins/inventory/data/valid/simple_yaml')
    inv_manager = InventoryManager(loader=loader, sources=[inventory_path])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

    yaml_file = inventory_loader.get('yaml')

# Generated at 2022-06-13 13:09:12.520779
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Test extension list from context
    from ansible.context import CLIContext
    c = CLIContext()
    c._set_file_logger()
    c.config.yaml_valid_extensions = ['.yml', '.json']
    i = InventoryModule()
    i.set_options()
    assert(i.verify_file('./inventory.yml'))
    assert(i.verify_file('./inventory.json'))
    assert(~i.verify_file('./inventory.yaml'))
    # Test ini entry
    i = InventoryModule()
    i.set_options()
    assert(~i.verify_file('./inventory.yaml'))
    assert(i.verify_file('./inventory.yml'))

# Generated at 2022-06-13 13:09:21.718374
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    dl = DataLoader()
    im = InventoryManager(loader=dl, sources=['.'])
    vm = VariableManager()
    i = InventoryModule()
    i.parse(im, dl, 'example.yml')
    hosts = im.get_hosts()
    print(hosts[0].name)
    childs = im.get_groups()[0].get_child_groups()
    print(childs[0].name)
    print(childs[1].name)
    print(childs[2].name)
    print(childs[0].get_group_vars())

# Generated at 2022-06-13 13:09:32.571965
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # Prepare parameters for function under test
    path = "/home/calvin/hosts"

    # Prepare mocks for function under test
    # BaseFileInventoryPlugin.verify_file = mocker.MagicMock(return_value=True)

    # Run function under test
    obj = InventoryModule()
    result = obj.verify_file(path)

    # Verify mocks
    # BaseFileInventoryPlugin.verify_file.assert_called_once_with()
    # assert os.path.splitext.called

    # Verify results
    assert result == True


# Generated at 2022-06-13 13:09:35.526112
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    assert module.verify_file('inventory_file.yml') == True

# Generated at 2022-06-13 13:09:49.804663
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:09:52.722714
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    file_name = '../../../plugins/inventory/yaml.py'
    i = InventoryModule()
    print ("\nTo be implemented\n")


# Generated at 2022-06-13 13:10:04.857878
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:10:13.422670
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import os
    import sys
    import pytest

    from ansible.plugins.loader import inventory_loader
    from ansible.module_utils._text import to_bytes
    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.utils.display import Display

    yaml_path = os.path.join(os.path.dirname(__file__), 'EXAMPLES')
    assert os.path.exists(yaml_path)

    config = {}
    display = Display()
    loader = inventory_loader

    inventory = inventory_loader.get('yaml', display, config, None, yaml_path)
    assert inventory._file_name == os.path.join(yaml_path,'test.yaml')

    # Get all hosts from inventory, if parsed properly with no errors

# Generated at 2022-06-13 13:10:36.755356
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    yaml_extensions = ['.yaml', '.yml', '.json']
    plugin = InventoryModule()
    plugin.set_options({'yaml_extensions':yaml_extensions})

    valid = plugin.verify_file('./path/to/file.yaml')
    assert valid 

    valid = plugin.verify_file('./path/to/file.yml')
    assert valid

    valid = plugin.verify_file('./path/to/file.json')
    assert valid

    valid = plugin.verify_file('./path/to/file.yaml5')
    assert not valid

    valid = plugin.verify_file('./path/to/file.yml5')
    assert not valid


# Generated at 2022-06-13 13:10:47.185681
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.compat.tests.mock import patch
    from ansible import constants as C
    from ansible.plugins.loader import InventoryLoader

    data_yaml_inventory = '''
    # some YAML inventory
    group1: # group keys must be unique
        hosts:
          host1:
        vars:
            var1: value1
            var2: value2
        children:
            group2:
                hosts:
                    host2:
                vars:
                    var2: value2_2
                    var3: value3
            group3:
                hosts:
                    host3:
                    host4:
                    host5:
    '''


# Generated at 2022-06-13 13:11:03.679387
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.module_utils.yaml_loader import AnsibleLoader

    # Host
    class Host(object):
        def __init__(self, name):
            self.name = name
        def get_vars(self):
            return {'inventory_hostname': self.name}
    # Inventory
    class Inventory(Inventory):
        def __init__(self):
            self.hosts = {}
            self.groups = {}

        def add_group(self, name):
            self.groups[name] = {}
            return name

        def add_host(self, name):
            self.hosts[name] = Host(name)
            return name

   

# Generated at 2022-06-13 13:11:08.167021
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    assert module.verify_file('test.yaml') == True
    assert module.verify_file('test.yml') == True
    assert module.verify_file('test') == False
    assert module.verify_file('test.txt') == False

# Generated at 2022-06-13 13:11:13.403066
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    # check extensions
    for ext in ['.yml','.yaml','.json']:
        assert True == module.verify_file("/path/file"+ext)
    # check file without ext
    assert True == module.verify_file("/path/file")

    # check invalid extensions     
    for ext in ['.txt','.md','.py']:
        assert False == module.verify_file("/path/file"+ext)

# Generated at 2022-06-13 13:11:19.930511
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts.yaml") == True
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts.yaml.yml") == False
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts") == False
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts.json") == True
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts.yaml.json") == True
    assert InventoryModule().verify_file("/path/to/samples/ansible_hosts.yml.json") == True

# Generated at 2022-06-13 13:11:30.838345
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import tempfile

    inventory = InventoryModule()

    # create a temporary file
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()

    # Make sure it is valid
    assert inventory.verify_file(f.name)

    # Make sure it is also valid with the '.yaml' extension
    f.name += '.yaml'
    assert inventory.verify_file(f.name)

    # Make sure it is also valid with the '.yml' extension
    f.name = f.name.replace('yaml', 'yml')
    assert inventory.verify_file(f.name)

# Generated at 2022-06-13 13:11:40.374165
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Parse yaml and get the object of class InventoryModule
    yaml_string = '''
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
                        test6
            vars:
                g2_var2: value3
            hosts:
                test4:
                    ansible_host: 127.0.0.1
        last_group:
            hosts:
                test1:
            vars:
                group_last_var: value
'''
    from ansible.parsing.yaml.objects import AnsibleMapping

# Generated at 2022-06-13 13:11:46.524740
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    obj = InventoryModule()
    assert obj.verify_file(path='file.yaml') == True
    assert obj.verify_file(path='file.yml') == True
    assert obj.verify_file(path='file.json') == True
    assert obj.verify_file(path='file.yaml.txt') == False

# Generated at 2022-06-13 13:11:50.176091
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    _module = InventoryModule()
    _module.get_option = lambda _: ['.yaml', '.yml', '.json']
    _module.verify_file('test.yaml')

# Generated at 2022-06-13 13:12:34.887997
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

    # Create a mock Environment plugin target
    class Environment_Mock(object):
        def __init__(self):
            self.env = dict(ANSIBLE_INVENTORY_PLUGIN_EXTS='abc,def,xyz')

    # Create a mock plugin_loader class
    class PluginLoader_Mock(object):
        def __init__(self, env):
            self.environment = env

    # Create an object of the YAML InventoryModule class
    obj = InventoryModule()

    # Override the environment and plugin_loader attributes of the obj
    obj.environment = Environment_Mock()
    obj.plugin_loader = PluginLoader_Mock(Environment_Mock())

    # Test if the following two files are valid files

# Generated at 2022-06-13 13:12:45.099044
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    yaml_extensions = ['.yaml', '.yml', '.json']
    yaml_true_test = ['.yaml', '.yml', '.json', '.txt']
    yaml_false_test = ['.txt', '.cfg']
    inventory_module = InventoryModule()
    inventory_module.set_options({'yaml_extensions': yaml_extensions})
    for item in yaml_true_test:
        assert inventory_module.verify_file(item)
    for item in yaml_false_test:
        assert not inventory_module.verify_file(item)

# Generated at 2022-06-13 13:12:55.716397
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.inventory.manager import InventoryManager

    # Setup
    loader = 'any'
    inventory = InventoryManager(loader=loader, sources=['plugin_inventory'])

    src = "plugin_inventory"
    inventory.set_variable(src, {})
    my_plugin = InventoryModule()
    my_plugin.parse(inventory, loader, './tests/unit/plugins/inventory/inventory_yaml/yml_valid.yml')
    my_inventory = inventory.get_inventory_sources()

    # Tests

# Generated at 2022-06-13 13:13:01.193206
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    print("test_InventoryModule_parse: Start")

    # Prerequistes
    import os
    import ansible.utils.unicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import inventory_loader

    # Set the environment variable ANSIBLE_INVENTORY to point to the test data files
    #    export ANSIBLE_INVENTORY=~/git/ansible/test/units/inventory/test_data
    #
    #python_script = "/home/wrehfiel/git/ansible/hacking/test-module"
    python_script = "/Users/wrehfiel/ENV/ansible/hacking/test-module"

# Generated at 2022-06-13 13:13:01.856859
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
  pass

# Generated at 2022-06-13 13:13:11.601881
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    # generated by tests/scripts/dump_valid_yaml_inventory.py

# Generated at 2022-06-13 13:13:13.207937
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    plugin = InventoryModule()
    assert plugin.verify_file('/etc/ansible/hosts')

# Generated at 2022-06-13 13:13:21.024051
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # ini file
    plugin = InventoryModule()
    variable_manager = VariableManager()
    loader = DataLoader()


# Generated at 2022-06-13 13:13:23.845568
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()

    # Returns False as path does not have extension
    assert not inventory.verify_file('test')

    # Returns True as path have valid extension
    assert inventory.verify_file('test.yml')


# Generated at 2022-06-13 13:13:32.325191
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    import ansible.plugins.inventory.yaml as yaml
    inv = yaml.InventoryModule()

    # Data for testing
    data_str = EXAMPLES

    # Enable verbose logging for testing
    inv.display.verbosity = 2

    # Setup loader for the test
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    loader._basedir = './'

    # Call parse method
    inv.parse(None,loader,data_str, cache=True)

    # Check some of the results
    print("inv.hosts: %s" % inv.hosts)
    print("inv.groups: %s" % inv.groups)
    print("inv.groups['all'].vars: %s" % inv.groups['all'].vars)

