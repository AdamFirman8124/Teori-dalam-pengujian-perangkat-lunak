

# Generated at 2022-06-12 22:32:54.024714
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    test_inventory = """
[centos:children]
debian
ubuntu
[centos:vars]
[debian]
debian1
debian2
debian3
[ubuntu]
ubuntu1
ubuntu2
"""
    inventory_manager = InventoryManager(loader=DictDataLoader({
        'inventory_test': DataSource({
            'path': 'inventory_test',
            'data': test_inventory,
            'type': 'host_list'})}),
                                          variable_manager=VariableManager())
    inventory_manager.parse_sources(['inventory_test'])
    inventory_manager.clear_pattern_cache()

    # [debian:children]
    hosts = inventory_manager.get_hosts("debian")
    assert len(hosts) == 3, hosts

    # debian
    hosts = inventory_manager.get_hosts

# Generated at 2022-06-12 22:32:57.482280
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory_manager = InventoryManager()
    result = inventory_manager.list_hosts()
    expected_result = []
    assert expected_result == result


# Generated at 2022-06-12 22:33:06.139953
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # Instantiation of class InventoryManager
    im = InventoryManager()

    # The function requires five parameters
    with pytest.raises(TypeError):
        im.parse_source()
    with pytest.raises(TypeError):
        im.parse_source(None)
    with pytest.raises(TypeError):
        im.parse_source(None, None)
    with pytest.raises(TypeError):
        im.parse_source(None, None, None)
    with pytest.raises(TypeError):
        im.parse_source(None, None, None, None)
    assert im.parse_source(None, None, None, None, None) == False



# Generated at 2022-06-12 22:33:11.300822
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory = InventoryManager()
    inventory.parse_sources('localhost,')
    assert len(inventory.hosts.keys()) == 1
    assert 'localhost' in inventory.hosts
    assert inventory.groups == {}
    assert inventory._sources == ['localhost,']

# Generated at 2022-06-12 22:33:21.923884
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    import pytest
    config = ConfigParser.ConfigParser()
    im = InventoryManager(config)
    im._inventory = Inventory()

    # Test if config variables are not present
    with pytest.raises(Exception) as excinfo:
        im.parse_source('')
    assert "--inventory (-i) is required" in str(excinfo)

    # Test if config variables are present
    config.add_section('defaults')
    config.set('defaults', 'inventory', '/etc/ansible/hosts')
    with pytest.raises(Exception) as excinfo1:
        im.parse_source('')
    assert "--inventory (-i) is required" in str(excinfo1)
    # Test if config variables are in place but empty
    config.set('defaults', 'inventory', '')

# Generated at 2022-06-12 22:33:33.204678
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():

    # prepare test data
    inventory = {
        'groups': {
            'testgroup': {
                'hosts':['testconn1', 'testconn2'],
                'children':['secondgroup']
                },
            'secondgroup': {
                'hosts':['secondgroup_host1', 'secondgroup_host2']
                },
            'thirdgroup': {
                'hosts':['thirdgroup_host1']
                }
            },
        'hosts': {
            'testconn1': {},
            'testconn2': {},
            'secondgroup_host1': {},
            'secondgroup_host2': {},
            'thirdgroup_host1': {}
            }
        }


# Generated at 2022-06-12 22:33:34.534657
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    pass
## InventoryManager

# InventoryParser

# Generated at 2022-06-12 22:33:42.718081
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inv = Inventory("test/test_inventories/test.yaml", loader).get_inventory()
    inv.hosts["host1"].name = "host"
    var_manager = VariableManager(loader=loader)
    var_manager.set_inventory(inv)

    inv_mgr = InventoryManager(loader=loader, sources=["test/test_inventories/test.yaml"])
    inv_mgr._inventory = inv
    # test parse_source handles source_user_specified
    parsed = inv_mgr.parse_source(['@/test/test_inventories/test.yaml'], var_manager)

# Generated at 2022-06-12 22:33:47.826714
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    im = InventoryManager('')
    im.subset('1,2,3')
    assert im._subset == ['1', '2', '3']

    im = InventoryManager('')
    im.subset('@/path/to/file')
    # TODO: Stub the file gets read and the results are in _subset

    im = InventoryManager('')
    im.subset('')
    assert im._subset is None

# Generated at 2022-06-12 22:33:51.282360
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    '''
    test subset method of class InventoryManager
    '''
    # new object
    i = InventoryManager()
    # test existence of subset method
    assert hasattr(i, 'subset')
