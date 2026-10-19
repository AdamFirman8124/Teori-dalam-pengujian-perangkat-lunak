

# Generated at 2022-06-13 12:55:00.965664
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.group import Group

    # Sample host_list string and expected output
    host_list = 'ansible-master, ansible-slave'
    expected_output = [Host(name='ansible-master'),
                       Host(name='ansible-slave')]

    # Parse host_list string using InventoryModule
    test_loader = DataLoader()
    test_im = InventoryManager(loader=test_loader, sources=host_list)
    test_vm = VariableManager(loader=test_loader, inventory=test_im)
    test_inventory_module = InventoryModule()
    test_inventory_

# Generated at 2022-06-13 12:55:13.695306
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = {
            '_meta':{
                'hostvars':{}
                },
            'all':{
                'hosts':{
                    'host1':{},
                    'host2.example.com':{},
                    }
                },
            'ungrouped':{
                'hosts':{
                    'localhost':{'port':1234}
                    }
                }
            }
    module = InventoryModule()
    module.parse(inventory,{},'host1,host2.example.com',True)
    assert module.parse(inventory, {}, 'host1,host2.example.com', True) == None
    assert inventory['_meta']['hostvars'] == {'localhost':{'port':1234}, 'host1':{},'host2.example.com':{}}

# Generated at 2022-06-13 12:55:22.445238
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class TestInventoryModule(InventoryModule):
        NAME = 'host_list'

    current_directory = os.path.dirname(__file__)
    inventory_dir = os.path.join(current_directory, '../../')
    loader = DataLoader()
    inventory = InventoryManager(loader, sources=inventory_dir)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    test_inv_module = TestInventoryModule()

    test_inv_module.parse(inventory, loader, host_list='www.example.com, 172.16.1.1')


# Generated at 2022-06-13 12:55:32.870211
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventories = {}
    loader = {"_find_path": lambda x, y: x}
    host_list = "10.10.2.6, 10.10.2.4"
    InventoryModule().parse(inventories, loader, host_list)
    assert inventories['_meta']['hostvars'] == {}
    assert inventories['all']['hosts'] == ['10.10.2.6', '10.10.2.4']
    assert inventories['all']['vars'] == {}
    assert inventories['all']['children'] == []
    assert inventories['ungrouped']['hosts'] == ['10.10.2.6', '10.10.2.4']
    assert inventories['ungrouped']['vars'] == {}

# Generated at 2022-06-13 12:55:44.122411
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    host = 'localhost,'
    group = 'group'
    port = '22'

    inventory = object()
    loader = object()
    cache = True
    cli_args = {}

    result = InventoryModule(cli_args=cli_args).parse(inventory, loader, host, cache)
    assert result == None

    result = InventoryModule(cli_args=cli_args).parse(inventory, loader, host)
    assert result == None

    result = InventoryModule(cli_args=cli_args).parse(inventory, loader, host, cache=False)
    assert result == None

# Generated at 2022-06-13 12:55:48.445397
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():

        # not a path, and has a comma, so it a valid host list
        assert InventoryModule.verify_file(None, "foo,bar")

        # a path, and has a comma, so it is not a host list
        assert not InventoryModule.verify_file(None, "/foo,bar")

# Generated at 2022-06-13 12:55:55.034107
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    module = InventoryModule()
    example = 'host1.example.com, host2'
    assert module.verify_file(example) == True, 'hosts example is not valid'

    example = 'host1.example.com,host2'
    assert module.verify_file(example) == True, 'hosts example is not valid'

    example = 'host1.example.com'
    assert module.verify_file(example) == False, 'hosts example must be not valid'


# Generated at 2022-06-13 12:56:02.484743
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    
    plugin = InventoryModule()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost,", "foo.com,bar.com"])

    plugin.parse(inventory, loader, "localhost,")
    plugin.parse(inventory, loader, "foo.com,bar.com")

    assert(inventory.get_host("localhost") != None)
    assert(inventory.get_host("foo.com") != None)
    assert(inventory.get_host("bar.com") != None)

# Generated at 2022-06-13 12:56:06.510396
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    assert InventoryModule().verify_file('/tmp/filename_missing') is False
    assert InventoryModule().verify_file('somehost, someotherhost') is True

# Generated at 2022-06-13 12:56:18.167682
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = type('Inventory',(),{})

    loader = type('Loader', (), {})
    inventory.add_host = type('add_host',(),{})
    inventory.hosts = type('hosts',(),{})
    inventory.hosts.add = type('add',(),{})

    inventory.add_host.return_value = inventory.hosts.add
    inventory.add_host.__name__ = 'add_host'
    inventory.hosts.__getitem__ = type('__getitem__',(),{})
    inventory.hosts.__getitem__.return_value = type('__getitem___return_value',(),{'vars':{}})

    h = InventoryModule()
    h.parse(inventory=inventory, loader=loader, host_list='host1,host2', cache=True)


# Generated at 2022-06-13 12:56:26.738964
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    i = InventoryModule()

    inventory = 'inventory'

    loader = 'loader'

    host_list = 'localhost,192.168.0.1'

    cache = True

    i.parse(inventory, loader, host_list, cache)

# Generated at 2022-06-13 12:56:34.220571
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../lib'))
    from ansible.inventory.manager import InventoryManager

    plugin = InventoryModule()
    inv_mgr = InventoryManager(loader=None, sources=[plugin])
    inv_mgr._inventory.parse_inventory(plugin, inv_mgr.loader, '10.10.1.1,10.10.1.2')

    assert '10.10.1.1' in inv_mgr._inventory.hosts
    assert '10.10.1.2' in inv_mgr._inventory.hosts

# Generated at 2022-06-13 12:56:40.890415
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # create instances of test class
    invMod = InventoryModule()

    # create mocks of variables needed to run test
    inventory = MagicMock()
    inventory.hosts = {}
    loader = MagicMock()
    host_list = "10.10.2.6, 10.10.2.4"
    cache = True

    # run code to be tested
    # create ansible.parsing.dataloader.DataLoader objects to catch loader data
    invMod.parse(inventory, loader, host_list, cache)

# Generated at 2022-06-13 12:56:44.782933
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Given
    inventory_module = InventoryModule()
    host_list = 'localhost'

    # When
    valid = inventory_module.verify_file(host_list)

    # Then
    assert not valid


# Generated at 2022-06-13 12:56:47.930900
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    inventoryModule = InventoryModule()
    inventory = {}
    loader = {}
    cache = True
    host_list = "10.10.2.6, 10.10.2.4"

    result = inventoryModule.verify_file(host_list)

    assert result == True


# Generated at 2022-06-13 12:57:03.298509
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    pc = PlayContext()
    im = InventoryModule()

    # Test undefined variable
    im.parse(inventory, loader, "")
    assert len(inventory.get_hosts()) == 0

    # Test variable with valid value
    im.parse(inventory, loader, "localhost")
    assert len(inventory.get_hosts()) == 1
    assert inventory.get_hosts()[0].name == "localhost"

    # Test variable with valid value
    im.parse(inventory, loader, "localhost,10.0.0.1")

# Generated at 2022-06-13 12:57:06.423633
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # b = '10.10.2.6, 10.10.2.4'
    b = '/tmp/hosts1'
    c = 'host1.example.com, host2'
    d = 'localhost,'
    assert not InventoryModule.verify_file(b)
    assert InventoryModule.verify_file(c)
    assert InventoryModule.verify_file(d)


# Generated at 2022-06-13 12:57:12.318161
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    inventory = FakeInventory()
    loader = FakeLoader()
    inventoryModule = InventoryModule()
    host_list = "10.10.2.6, 10.10.2.4"

    inventoryModule.parse(inventory, loader, host_list)
    assert inventory.hosts == ['10.10.2.6', '10.10.2.4']



# Generated at 2022-06-13 12:57:17.529351
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    result = inv.verify_file('/tmp/test')
    assert result is False
    result = inv.verify_file('/tmp/test,')
    assert result is False
    result = inv.verify_file('/tmp/test,example.com')
    assert result is True


# Generated at 2022-06-13 12:57:25.463928
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    invmod = InventoryModule()
    fake_loader = object()
    fake_inventory = object()

# Generated at 2022-06-13 12:57:32.299102
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory_string = '10.10.2.6, 10.10.2.4'
    plugin = InventoryModule()
    result = plugin.verify_file(inventory_string)
    assert result

# Generated at 2022-06-13 12:57:40.471028
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Unit test for method parse of class InventoryModule.
    """
    import ansible

    mock_loader = ansible.parsing.dataloader.DataLoader()
    mock_host_list = """host1,host2"""

    invmod = InventoryModule()
    invmod._loader = mock_loader
    invmod.parse(None, mock_loader, mock_host_list, cache=False)

    assert invmod._inventory.hosts["host1"]
    assert invmod._inventory.hosts["host2"]

# Generated at 2022-06-13 12:57:43.592698
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv = InventoryModule()
    assert inv.verify_file("host1.example.com, host2")


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 12:57:48.436052
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    module = InventoryModule()
    inventory = {}
    loader = {}
    host_list = "10.10.2.6, 10.10.2.4"
    cache = True
    module.parse(inventory, loader, host_list, cache)
    assert inventory['hosts'] == ['10.10.2.6', '10.10.2.4']

# Generated at 2022-06-13 12:57:48.930804
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert True

# Generated at 2022-06-13 12:57:53.974356
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    """
    Unit test for method verify_file of class InventoryModule
    """
    module = InventoryModule()
    host_list = [',', ',']
    results = [False, True]

    for i in range(len(host_list)):
        assert module.verify_file(host_list[i]) == results[i]

# Generated at 2022-06-13 12:57:57.657308
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    test_object = InventoryModule()
    assert test_object.verify_file(',') == True
    assert test_object.verify_file('localhost,') == True
    assert test_object.verify_file('localhost,127.0.0.1') == True
    assert test_object.verify_file('localhost') == False
    assert test_object.verify_file('localhost, 127.0.0.1') == False
    assert test_object.verify_file('localhost-127.0.0.1') == False

# Generated at 2022-06-13 12:58:06.771582
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    import base64
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    INVENTORY_DATA = b"""
plugin: host_list
"""

    INI_DATA = b"""
[web]
127.0.0.1, 198.51.100.1, 198.51.100.2
"""

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["foobar_host_list"])
    inventory._subscriptions['foobar_host_list'] = InventoryModule()
    data = base64.b64encode(INI_DATA)
    inventory.parse_sources_with_plugin('foobar_host_list', data, cache=False)

# Generated at 2022-06-13 12:58:12.782416
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # We can not use BaseTestCase because there is no CONSTANTS at this point
    # and the inheritance is problematic
    host_list = '127.0.0.1, foo.example.com'
    inventory = FakeInventory()
    loader = FakeLoader()
    im = InventoryModule()
    im.parse(inventory, loader, host_list)
    assert len(inventory.hosts) == 2
    assert '127.0.0.1' in inventory.hosts
    assert 'foo.example.com' in inventory.hosts

# FakeInventory class for testing InventoryModule

# Generated at 2022-06-13 12:58:18.872420
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    host_list = 'host1,host2'
    inventory = FakeInventory()
    plugin = InventoryModule()
    plugin.parse(inventory, "loader1", host_list)
    assert len(inventory.hosts) == 2
    assert inventory.hosts['host1']['group'] == 'ungrouped'
    assert inventory.hosts['host2']['group'] == 'ungrouped'


# Generated at 2022-06-13 12:58:31.301399
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv_mod = InventoryModule()
    assert inv_mod.verify_file("host1,host2") is True
    assert inv_mod.verify_file("/tmp/inventory.ini") is False
    assert inv_mod.verify_file("/tmp/inventory.ini,") is False
    assert inv_mod.verify_file("/tmp/inventory.ini, ") is False
    assert inv_mod.verify_file(" /tmp/inventory.ini") is False
    assert inv_mod.verify_file("/tmp/inventory.ini, host1") is False


# Generated at 2022-06-13 12:58:41.615432
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = None
    loader = None

    # inv_string format: host1:port1, host2:port2, ...
    # Expected result of verify_file: True
    inv_string = 'localhost:22, localhost:21'
    host_list = InventoryModule()
    assert host_list.verify_file(inv_string)

    # inv_string format: host1, host2, ...
    # Expected result of verify_file: True
    inv_string = 'localhost, localhost'
    host_list = InventoryModule()
    assert host_list.verify_file(inv_string)

    # inv_string format: host1, host2, ...
    # Expected result of verify_file: False
    inv_string = 'host1, host2'
    host_list = InventoryModule()

# Generated at 2022-06-13 12:58:47.962698
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inv = InventoryModule()
    myhost = 'host1.example.com'
    myhost2 = 'host2.example.com'
    host_list = myhost + ',' + myhost2
    inv.parse(None, None, host_list)
    assert inv.get_hosts(myhost)
    assert inv.get_hosts(myhost2)

# Generated at 2022-06-13 12:58:54.277389
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    loader = None
    host_list = '10.10.2.10, 10.10.2.20'
    inventory = dict()
    i = InventoryModule()
    i.parse(inventory, loader, host_list)
    assert inventory == {'all': {'hosts': ['10.10.2.10', '10.10.2.20'], 'vars': {}},'_meta': {'hostvars': {}}}

# Generated at 2022-06-13 12:59:04.611404
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Setup
    iom = InventoryModule()
    test_host_list_01 = '/path/to/file'
    test_host_list_02 = 'host1, host2'
    expected_result_01 = False
    expected_result_02 = True

    # Execute
    result_01 = iom.verify_file(test_host_list_01)
    result_02 = iom.verify_file(test_host_list_02)

    # Verify outcome
    assert result_01 == expected_result_01
    assert result_02 == expected_result_02


# Generated at 2022-06-13 12:59:15.652892
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    # Test with a string that do not contains a comma
    inventory_module = InventoryModule()
    host_list = "127.0.0.1"
    assert False == inventory_module.verify_file(host_list)

    # Test with a string that contains a comma and is not a file
    inventory_module = InventoryModule()
    host_list = "127.0.0.1,127.0.0.2"
    assert True == inventory_module.verify_file(host_list)

    # Test with a string that contains a comma and is a file
    inventory_module = InventoryModule()
    host_list = "unit_test/test_inventory_host_list.py"
    assert False == inventory_module.verify_file(host_list)

# Generated at 2022-06-13 12:59:20.593517
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inv_mod = InventoryModule()
    assert(inv_mod.verify_file("10.10.2.6, 10.10.2.4") == True)
    assert(inv_mod.verify_file("hosts") == False)
    assert(inv_mod.verify_file("host1.example.com, host2") == True)
    assert(inv_mod.verify_file("localhost,") == True)


# Generated at 2022-06-13 12:59:32.656621
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class FakeInventory() :
        def __init__(self) :
            self.groups={}
            self.hosts={}
            self.vars={}
            self.get_host = lambda host : self.hosts.get(host)
            self.add_host = lambda host, group, port : self.hosts.__setitem__(host, {'groups':[], 'vars':{}, 'port':port})
            self.add_group = lambda group, **kwargs : self.groups.__setitem__(group,kwargs)
            self.add_child = lambda group,child : self.groups.get(group).__getitem__(child)


    class FakeLoader() :
        def __init__(self) :
            self.fail_on_undefined_errors = False


# Generated at 2022-06-13 12:59:41.791496
# Unit test for method verify_file of class InventoryModule
def test_InventoryModule_verify_file():
    inventory = InventoryModule()
    host_list = 'host1,host,host3'
    result = inventory.verify_file(host_list)
    assert result == True
    host_list = 'host1'
    result = inventory.verify_file(host_list)
    assert result == False
    host_list = 'host1,host,host3'
    result = inventory.parse(inventory, None, host_list)
    result == 1
    assert result == 1
    host_list = 'host1,host,host3'
    result = inventory.verify_file(host_list)
    assert result == True

# Generated at 2022-06-13 12:59:53.791709
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    test_module = InventoryModule()

    # create a pseudo Inventory
    class PseudoInventory(object):
        def __init__(self):
            self.hosts = []
        def add_host(self, hostname, group=None, port=None):
            self.hosts.append(hostname)

    inv = PseudoInventory()

    orig_hosts = ['10.10.2.6', '10.10.2.4', 'host1.example.com', 'host2', 'localhost']
    host_list = ','.join(orig_hosts)
    test_module.parse(inv, None, host_list)
    assert set(orig_hosts) == set(inv.hosts)



# Generated at 2022-06-13 13:00:20.603325
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    '''
    Unit test for method parse of class InventoryModule
    '''

    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.inventory import Host, Group

    # Create a Mock to replace the ansible.inventory.manager.InventoryManager Class
    class Mock_InventoryManager(MutableMapping):
        def __init__(self):
            self.store = dict()

        def __setitem__(self, key, value):
            self.store[key] = value

        def __getitem__(self, key):
            if key in self.store:
                return self.store[key]
            else:
                raise KeyError


# Generated at 2022-06-13 13:00:29.947212
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    data_loader = DataLoader()
    inv_string = ','.join(('localhost', 'localhost', '127.0.0.1'))
    inventory = InventoryModule()
    inventory.parse(
        inventory=dict(),
        loader=data_loader,
        host_list=inv_string,
        cache=True)
    # There is no need to test the method add_host of class Inventory because it calls the method _get_host of it.
    # Thus, it is indirectly tested here.
    assert len(inventory.inventory.hosts) == 3

# Generated at 2022-06-13 13:00:32.942388
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    """
    Return True if the parse method returns a dictionary
    """
    test_obj = InventoryModule()
    test_obj.parse('inventory', 'loader', 'host_list')
    return True

# Generated at 2022-06-13 13:00:44.069527
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import json

    class ResultCallback(CallbackBase):
        def v2_runner_on_ok(self, result, **kwargs):
            host = result._host
            print(json.dumps({host.name: result._result}, indent=4))

    # since the API is constructed for CLI it expects certain options to always be set in the context object

# Generated at 2022-06-13 13:00:55.856770
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    test_data = "11.11.11.11, 12.12.12.12, 13.13.13.13, 14.14.14.14"

    # NOTE: Creating a 'dummy' inventory.
    inventory = None
    loader = None

    test_obj = InventoryModule()
    # NOTE: This will invoke parse method of class InventoryModule
    test_obj.parse(inventory, loader, test_data)

    # NOTE: Asserting the outcome
    assert test_obj.inventory.hosts == {'11.11.11.11': {'port': None}, '12.12.12.12': {'port': None}, '13.13.13.13': {'port': None}, '14.14.14.14': {'port': None}}

# Generated at 2022-06-13 13:01:04.019197
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Create a InventoryModule object
    InvM = InventoryModule()

    # Create a Inventory object
    inv = Inventory()

    # Test the method parse
    InvM.parse(inv, "loader", "127.0.0.1, 127.0.0.2", cache=True)

    # Test if "localhost" is the first host in inventory hosts
    assert inv.hosts["localhost"] == "ungrouped"

    # Test if "127.0.0.1" is the second host in inventory hosts
    assert inv.hosts["127.0.0.1"] == "ungrouped"

    # Test if "127.0.0.2" is the third host in inventory hosts
    assert inv.hosts["127.0.0.2"] == "ungrouped"

# Generated at 2022-06-13 13:01:17.107068
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # Just use to check that there are no syntax errors in the method
    from ansible import context
    from ansible.plugins.loader import inventory_loader

    source = '1.1.1.1, 2.2.2.2,3.3.3.3,4.4.4.4'
    loader = inventory_loader.get('host_list', class_only=True)
    inventory = loader.parse(source, cache=False)
    assert inventory is not None

    assert len(inventory.hosts) == 4

    host_1 = inventory.get_host('1.1.1.1')
    assert host_1 is not None
    assert host_1.name == '1.1.1.1'
    assert len(host_1.groups) == 1
    assert 'ungrouped' in host_1.groups

# Generated at 2022-06-13 13:01:21.904985
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory=None
    loader={}
    host_list='xxx,yyy,zzz'
    cache=True
    im=InventoryModule()
    im.parse(inventory,loader,host_list,cache)
    print(inventory.get_groups_dict())
    print(inventory.get_hosts_dict())


# Generated at 2022-06-13 13:01:37.443699
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["127.0.0.1, 192.168.0.1"])

    # Explicitly setting host to not be intialized (initialized
    # based on file path), to test this scenario.
    inventory.hosts = {"127.0.0.1": Host(name="127.0.0.1")}
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    inventory_plugin = InventoryModule()

# Generated at 2022-06-13 13:01:45.893605
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():

    # arrange
    inventory = InventoryModule()
    host_list = "10.10.2.6, 10.10.2.4"

    # act
    inventory.parse(inventory, "loader", host_list)

    # assert
    assert inventory.group.name == "ungrouped"
    assert inventory.group.vars == {}
    assert inventory.host.name == "10.10.2.4"
    assert inventory.host.vars == {"ansible_host": "10.10.2.4"}

# Generated at 2022-06-13 13:02:22.682499
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # pylint: disable=protected-access,no-self-use
    '''
    Unit test for method parse
    '''
    cfg = {
        "plugin": "host_list",
        "host_list": "host1.example.com, host2",
    }
    inventory = None
    loader = None
    p = InventoryModule()
    p.parse(inventory, loader, cfg["host_list"])
    for _host in cfg["host_list"].split(','):
        _host = _host.strip()

# Generated at 2022-06-13 13:02:32.672468
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    class MockInventory(object):

        def __init__(self):
            self.hosts = []

        def add_host(self, host, group=None, port=None):
            self.hosts.append(host)

    class MockLoader(object):

        def __init__(self):
            pass

    mock_inventory = MockInventory()
    mock_loader = MockLoader()
    plugin = InventoryModule()
    plugin.parse(mock_inventory, mock_loader, "127.0.0.1,192.168.0.1,255.255.255.255,10.0.0.0,172.17.0.1,172.31.255.255")

# Generated at 2022-06-13 13:02:43.374002
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    # It should raise AnsibleError if comma is not present in string
    inventory = InventoryModule()
    with pytest.raises(AnsibleParserError):
        inventory.parse(None, None, '', None)

    inventory = InventoryModule()
    with pytest.raises(AnsibleParserError):
        inventory.parse(None, None, 'abc.def.com', None)

    # It should not raise exception if commas are present
    inventory = InventoryModule()
    assert ',' in inventory.parse(None, None, 'abc.def.com, ghi.jkl.com', None) == ','
    assert ',' in inventory.parse(None, None, 'abc.def.com,ghi.jkl.com', None) == ','

    inventory = InventoryModule()

# Generated at 2022-06-13 13:02:54.575911
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    im = InventoryManager(loader=loader, sources=None)

    im.add_plugin(InventoryModule())

    plugin_source = "\"localhost,10.10.2.4,example.org\""
    setattr(im, 'host_list', plugin_source)


# Generated at 2022-06-13 13:03:04.959218
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    im = InventoryModule()
    b_targets = to_bytes('10.10.2.6, 10.10.2.4', errors='surrogate_or_strict')
    assert im.verify_file(b_targets) == True
    c_inv = im.parse(None, None, b_targets)
    assert c_inv == {'all': {'hosts': ['10.10.2.4', '10.10.2.6']},
     '_meta': {'hostvars': {}}}

# Generated at 2022-06-13 13:03:06.041294
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    assert InventoryModule()

# Generated at 2022-06-13 13:03:10.901273
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = dict()
    loader = ""
    host_list = ""
    ansible_InventoryModule = InventoryModule()
    ansible_InventoryModule.parse(inventory, loader, host_list)

# Generated at 2022-06-13 13:03:19.021940
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.vault import VaultLib

    loader = DataLoader()

    passwords = dict(vault_pass='secret')

    inventory = InventoryManager(loader=loader, sources=["Test String"])


    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_vars = dict(ansible_ssh_pass='secret')

    # Test with simple string
    test_string = '10.10.2.6, 10.10.2.4'
    im = InventoryModule()
    im.parse(inventory, loader, test_string)


# Generated at 2022-06-13 13:03:23.159031
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    host_list = '10.10.2.6, 10.10.2.4'
    loader = 'ansible.parsing.dataloader.DataLoader'
    cache = True
    inventroy = 'ansible.inventory.manager.InventoryManager'
    im = InventoryModule()
    im.parse(inventroy, loader, host_list)

# Generated at 2022-06-13 13:03:31.063751
# Unit test for method parse of class InventoryModule

# Generated at 2022-06-13 13:04:47.321635
# Unit test for method parse of class InventoryModule
def test_InventoryModule_parse():
    inventory = '''
[testgroup]
testhost1
testhost2 'testhost2-alias'
'''

    try:
        from io import StringIO
    except ImportError:
        from cStringIO import StringIO

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    loader = DataLoader()