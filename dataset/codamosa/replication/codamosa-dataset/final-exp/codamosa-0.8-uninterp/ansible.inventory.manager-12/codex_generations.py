

# Generated at 2022-06-12 22:26:50.074177
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory = InventoryManager(host_list=[])
    inventory.parse_source('localhost,')
    assert len(inventory._inventory.hosts) == 2
    assert len(inventory._inventory.groups) == 3
    assert 'localhost' in inventory._inventory.hosts
    assert 'all' in inventory._inventory.groups
    assert 'ungrouped' in inventory._inventory.groups


# Generated at 2022-06-12 22:26:57.745183
# Unit test for function order_patterns

# Generated at 2022-06-12 22:27:05.831335
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    assert _test_data_path.join('test_data').exists()
    assert _test_sub_dir.join('sub_dir_with_inventories').join('ansible.cfg').exists()
    
    # Test 1: Check if all files in inventory directory are parsed.
    manager = InventoryManager(loader=None, sources=str(_test_data_path))

# Generated at 2022-06-12 22:27:16.694063
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory = InventoryManager(ansible_vars={'ansible_ssh_pass': 'pass'})
    assert inventory.list_hosts('all') == ['a1', 'a2', 'b1']
    assert inventory.list_hosts('a*') == ['a1', 'a2']
    assert inventory.list_hosts('myhost') == ['a1']
    assert inventory.list_hosts('~') == ['b1']
    assert inventory.list_hosts(['a*', 'b1']) == ['a1', 'a2', 'b1']
    assert inventory.list_hosts(['myhost', 'a2']) == ['a1', 'a2']
    assert inventory.list_hosts('*') == []
    assert inventory.list_hosts('~') == ['b1']

# Generated at 2022-06-12 22:27:25.302754
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # test cases that are expected to fail
    cases = [
        # not a module
        [],
        # not a dict
        "",
        # not executable
        {'executable': '/not/existing/path'},
        # not existing
        {'path': '/not/existing/path'},
        # not executable
        {'path': 'test_InventoryManager_parse_source'},  # this test module
    ]
    im = InventoryManager('test_InventoryManager_parse_source')
    # make sure there is nothing cached
    assert_true(im.loader.inventory_directory is None)  # noqa

# Generated at 2022-06-12 22:27:26.289014
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    pass


# Generated at 2022-06-12 22:27:34.885808
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory = InventoryManager()

    assert isinstance(inventory.get_hosts(), list)
    assert isinstance(inventory.get_hosts('all'), list)
    assert isinstance(inventory.get_hosts(['all']), list)
    assert isinstance(inventory.get_hosts('all', False, False, 'inventory'), list)
    assert isinstance(inventory.get_hosts('all', True, False, 'inventory'), list)
    assert isinstance(inventory.get_hosts('all', False, True, 'inventory'), list)
    assert isinstance(inventory.get_hosts('all', True, True, 'inventory'), list)

    assert isinstance(inventory.get_hosts('all', order='sorted'), list)

# Generated at 2022-06-12 22:27:39.070048
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory = InventoryManager('/dev/null')
    inventory.parse_source("foo", "some_plugin", {"somevar": "somevalue"})
    assert(inventory.hosts['foo'].vars == {'somevar': 'somevalue'})

# Generated at 2022-06-12 22:27:47.053895
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    from ansible.parsing.dataloader import DataLoader

    def test_source_exception(src):
        try:
            InventoryManager(loader=DataLoader()).parse_source(src)
        except Exception as e:
            return str(e)


# Generated at 2022-06-12 22:27:47.722122
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    pass

# Generated at 2022-06-12 22:28:02.962485
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    im = InventoryManager(InventoryMock(), play=Play().load(dict(hosts=['server1']), variable_manager=VariableManager(), loader=None))
    assert ['server1'] == sorted(im.list_hosts())



# Generated at 2022-06-12 22:28:13.110533
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'
    host4 = 'host4'
    host5 = 'host5'

    # Setup
    inventory_manager = InventoryManager([])

    host1_obj = Mock()
    host1_obj.name = host1
    inventory_manager._inventory.hosts[host1] = host1_obj

    host2_obj = Mock()
    host2_obj.name = host2
    inventory_manager._inventory.hosts[host2] = host2_obj

    host3_obj = Mock()
    host3_obj.name = host3
    inventory_manager._inventory.hosts[host3] = host3_obj

    host4_obj = Mock()
    host4_obj.name = host4
    inventory_

# Generated at 2022-06-12 22:28:23.224757
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    import os
    import glob
    import ansible.inventory.manager

    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)
    test_inventory_path = "./test/integration/inventory"
    hosts_1_pattern_all = ["localhost"]
    hosts_2_pattern_all = ["winrm_1", "winrm_2", "winrm_3"]
    hosts_3_pattern_all = ["winrm_1", "winrm_2", "winrm_3"]
    hosts_4_pattern_all = ["winrm_1", "winrm_2", "winrm_3", "localhost"]
    hosts_5_pattern_all = ["localhost"]

# Generated at 2022-06-12 22:28:34.613734
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory_manager = InventoryManager()

    assert inventory_manager.parse_source(
        source="localhost",
    ) == dict(
        config_file="localhost",
        script_name=None,
        vault_password_file=None,
        inventory_dir="./",
        private_data_dir="./",
        create_vault_password_file=False,
    )

    assert inventory_manager.parse_source(
        source="localhost,",
    ) == dict(
        config_file="localhost,",
        script_name=None,
        vault_password_file=None,
        inventory_dir="./",
        private_data_dir="./",
        create_vault_password_file=False,
    )


# Generated at 2022-06-12 22:28:43.916738
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # No sources specified
    test_vars = {}
    test_options = {}
    test_inventory = Inventory()
    assert InventoryManager(test_loader, test_vars, test_options).parse_sources({}, test_inventory) == []
    # Source is a list of one string
    test_vars = {}
    test_options = {"inventory": ["inventories/test_inventory"]}
    test_inventory = Inventory()
    assert InventoryManager(test_loader, test_vars, test_options).parse_sources({}, test_inventory) == []
    # Source is a single string
    test_vars = {}
    test_options = {"inventory": "inventories/test_inventory"}
    test_inventory = Inventory()
    assert InventoryManager(test_loader, test_vars, test_options).parse_s

# Generated at 2022-06-12 22:28:49.488408
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    #
    # SETUP
    #
    im = InventoryManager('localhost,')

    #
    # TEST
    #
    result = im.parse_sources(im.get_inventory_sources())

    #
    # ASSERT
    #
    assert_result(result, dict())




# Generated at 2022-06-12 22:28:58.404017
# Unit test for function order_patterns
def test_order_patterns():
    assert order_patterns(['host.*', 'host1']) == ['host.*', 'host1']
    assert order_patterns(['host.example.com', 'host.example.net']) == ['host.example.com', 'host.example.net']
    assert order_patterns(['host.example.com', '&host.example.net']) == ['host.example.com', '&host.example.net']
    assert order_patterns(['&host.example.com', '!host.example.net']) == ['host.example.com', '&host.example.com', '!host.example.net']

# Generated at 2022-06-12 22:29:00.798009
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # Create the object under test
    im = InventoryManager([], [], None)

    # 'subset(subset_pattern)' may raise AnsibleError
    subset_pattern = None

    # Invoke the method under test
    im.subset(subset_pattern)


# Generated at 2022-06-12 22:29:05.978430
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager()
    inventory_manager.subset("foo")
    assert inventory_manager._subset
    assert inventory_manager._subset == ["foo"]
    # call it twice and make sure it is still correctly set
    inventory_manager.subset("foo")
    assert inventory_manager._subset
    assert inventory_manager._subset == ["foo"]

# Generated at 2022-06-12 22:29:10.658792
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory_manager = InventoryManager()

    # test match one pattern
    pattern = 'ubuntu1:ubuntu2'
    hosts = inventory_manager._match_one_pattern(pattern)
    assert hosts == ['ubuntu1', 'ubuntu2']

    # test get_hosts
    patterns = 'all'