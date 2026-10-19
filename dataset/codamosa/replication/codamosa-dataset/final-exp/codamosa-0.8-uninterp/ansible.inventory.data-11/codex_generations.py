

# Generated at 2022-06-12 22:05:25.387702
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    """
    Unit test for method add_host of class InventoryData
    """
    print('Testing InventoryData.add_host')
    inventory = InventoryData()
    inventory.add_host("127.0.0.1")
    inventory.add_host("127.0.0.2")
    inventory.add_host("127.0.0.3")

    assert inventory.hosts["127.0.0.1"] is not None
    assert inventory.hosts["127.0.0.2"] is not None
    assert inventory.hosts["127.0.0.3"] is not None
    print("            Test passed")


# Generated at 2022-06-12 22:05:38.169319
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    # Setup
    inv = InventoryData()
    inv.add_host('foo')
    inv.add_host('bar')
    inv.add_group('grp1')
    inv.add_group('grp2')
    inv.add_child('grp1', 'foo')
    inv.add_child('grp2', 'foo')
    inv.add_child('grp2', 'bar')

    # Test: hosts are not in ungrouped
    assert 'foo' not in inv.groups['ungrouped'].get_hosts()
    assert 'bar' not in inv.groups['ungrouped'].get_hosts()

    # Test: hosts are in all (and thus, implicitly, in ungrouped via group inheritance)
    assert 'foo' in inv.groups['all'].get_hosts()
   

# Generated at 2022-06-12 22:05:47.905942
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():

    #create Inventory
    data = InventoryData()

    #init hosts and groups
    data.add_group('group1')
    data.add_group('group2')

    data.add_host('host1', 'group1')
    data.add_host('host2', 'group1')

    data.add_host('host3', 'group2')
    data.add_host('host4', 'group2')

    #check that hosts are in correct groups
    host1 = data.hosts['host1']
    assert host1.get_groups()[0].name == 'group1'
    host2 = data.hosts['host2']
    assert host2.get_groups()[0].name == 'group1'
    host3 = data.hosts['host3']

# Generated at 2022-06-12 22:05:59.738044
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():
    '''
    Create an empty inventory.
    Create a group without host.
    Create a host without group.
    Create a host with a group and the group with the host.
    Call the remove_host method with the two last hosts.
    Check the existence of the hosts, groups and the membership.
    '''
    inventory_data = InventoryData()

    host = inventory_data.add_host('test_host_no_group')
    group = inventory_data.add_group('test_group_no_host')

    host_in_group = inventory_data.add_host('test_host_with_group')
    group_with_host = inventory_data.add_group('test_group_with_host')
    inventory_data.add_child(group_with_host, host_in_group)

    assert group not in inventory

# Generated at 2022-06-12 22:06:11.598944
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

    groups = dict()
    groups['test'] = Group('test')
    groups['test'].add_host(Host('host_test', None))

    invent = InventoryData()
    invent.groups['all'] = Group('all')
    invent.groups['test'] = Group('test')
    invent.hosts['host_test'] = Host('host_test', None)

    assert(groups['test'].hosts != invent.groups['test'].hosts)

    invent.remove_host(invent.hosts['host_test'])
    assert(groups['test'].hosts == invent.groups['test'].hosts)

# Generated at 2022-06-12 22:06:16.751171
# Unit test for method get_host of class InventoryData
def test_InventoryData_get_host():
    inventory = InventoryData()
    inventory.add_host("localhost")
    host = inventory.get_host("localhost")
    assert host == inventory.hosts["localhost"]
    host = inventory.get_host("127.0.0.1")
    assert host == inventory.localhost
    assert inventory.get_host("foo") is None


# Generated at 2022-06-12 22:06:24.273415
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():

    #
    # Create 3 groups, g1, g2, g3
    #
    g1host1, g1host2 = 'host1', 'host2'
    g2host1, g2host2 = 'host3', 'host4'
    g3host1, g3host2 = 'host5', 'host6'

    g1 = Group('g1')
    g2 = Group('g2')
    g3 = Group('g3')

    g1.add_host(Host(g1host1))
    g1.add_host(Host(g1host2))

    g2.add_host(Host(g2host1))
    g2.add_host(Host(g2host2))

    g3.add_host(Host(g3host1))

# Generated at 2022-06-12 22:06:30.307987
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():
    # Setup fixture
    inv = InventoryData()
    inv.add_host('myhost')
    inv.add_group('mygroup')
    inv.add_child('mygroup', 'myhost')

    # Remove host
    inv.remove_host(inv.get_host('myhost'))

    # Test that host has been removed
    assert len(inv.hosts) == 0
    assert 'myhost' not in inv.hosts

# Generated at 2022-06-12 22:06:38.193457
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    """
    Test add_host method of class InventoryData
    """
    idata = InventoryData()
    assert idata.hosts == {}
    assert idata.groups == {}

    # Test bad_name_1
    display.verbosity = 4
    bad_name_1 = [None]
    for host in bad_name_1:
        try:
            idata.add_host(host)
        except AnsibleError as err:
            assert err.message in "Invalid empty host name provided: None"
        else:
            assert False

    # Test bad_name_2
    bad_name_2 = [True]

# Generated at 2022-06-12 22:06:50.214723
# Unit test for method remove_host of class InventoryData
def test_InventoryData_remove_host():
    """
    Test InventoryData.remove_host
    :return:
    """
    # Create data
    inv_data = InventoryData()

# Generated at 2022-06-12 22:07:07.099131
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    # Test implicit localhost
    from collections import namedtuple
    MockHost = namedtuple('MockHost', ['name', 'groups_dict'])

    mh1 = MockHost('localhost', {})
    mh2 = MockHost('127.0.0.1', {})

    display = Display()
    display.verbosity = 0

    i = InventoryData()
    i.hosts = {
        'localhost': mh1,
        '127.0.0.1': mh2,
        'not-implicit': MockHost('not-implicit', {}),
        'another': MockHost('another', {}),
    }

    # Test implicit localhost
    display.display("implicit localhost")
    i.reconcile_inventory()

# Generated at 2022-06-12 22:07:13.291312
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    # Setup
    inventory = InventoryData()

    # Act
    inventory.add_host("host", group="group")

    # Assert
    assert inventory.hosts["host"] is not None
    assert inventory.groups["group"] is not None
    assert inventory.hosts["host"] in inventory.groups["group"].get_hosts()

# Generated at 2022-06-12 22:07:24.147549
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    inv_data = InventoryData()

    inv_data.add_host('hostname', group='group1')
    inv_data.add_host('hostname', group='group2')
    inv_data.add_host('hostname', group='group3')
    inv_data.add_host('hostname1', group='group1')
    inv_data.add_host('hostname1', group='group2')
    inv_data.add_host('hostname1', group='group3')
    inv_data.add_host('hostname2', group='group1')
    inv_data.add_host('hostname2', group='group2')
    inv_data.add_host('hostname2', group='group3')
    inv_data.add_host('hostname3', group='group1')
    inv_

# Generated at 2022-06-12 22:07:31.403742
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    i = InventoryData()
    i.add_group('g1')
    i.add_host('h1')
    i.add_host('h2', 'g1')
    i.add_host('h3', 'g1')
    i.add_host('h4')
    assert i.get_groups_dict() == {'g1': ['h2', 'h3'], 'all': ['h1', 'h2', 'h3', 'h4'], 'ungrouped': ['h1', 'h4']}

# Generated at 2022-06-12 22:07:43.595183
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    new_inventory = InventoryData()
    # case 1: add host without port
    new_inventory.add_host("10.0.0.1")
    new_inventory.add_host("10.0.0.2")
    # assert that hosts is an object and hosts has 10.0.0.1 and 10.0.0.2
    assert(isinstance(new_inventory.hosts,dict))
    assert("10.0.0.1" in new_inventory.hosts)
    assert("10.0.0.2" in new_inventory.hosts)
    # assert host 10.0.0.1 has name and port
    host_1 = new_inventory.hosts["10.0.0.1"]

# Generated at 2022-06-12 22:07:51.520956
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory = InventoryData()
    inventory.localhost = Host('localhost')
    inventory.add_group('test')
    assert inventory.groups['test'].name == 'test'
    inventory.add_host('test')
    assert inventory.hosts['test'].name == 'test'
    inventory.add_child('test', 'test')
    assert inventory.hosts['test'] in inventory.groups['test'].get_hosts()
    assert len(inventory.hosts['test'].groups) == 2
    inventory.add_host('test', 'test')
    output = inventory.reconcile_inventory()
    assert len(inventory.hosts['test'].groups) == 2
    assert inventory.hosts['test'] in inventory.groups['test'].get_hosts()
    assert inventory.localhost

# Generated at 2022-06-12 22:08:01.469966
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory_data = InventoryData()

    inventory_data.add_host('host1')
    inventory_data.add_host('host2', 'group1')

    inventory_data.reconcile_inventory()

    assert inventory_data.groups['all'].get_hosts()[0].name     == 'host1'
    assert inventory_data.groups['all'].get_hosts()[1].name     == 'host2'
    assert inventory_data.groups['ungrouped'].get_hosts()[0].name == 'host1'
    assert inventory_data.groups['group1'].get_hosts()[0].name  == 'host2'

# Generated at 2022-06-12 22:08:05.939131
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    g1 = Group('g1')
    g2 = Group('g2')
    g3 = Group('g3')
    g4 = Group('g4')

    g1_children = [g2, g3]
    g2_children = [g3]

    g1.add_child_groups(g1_children)
    g2.add_child_groups(g2_children)
    groups = {g1.name: g1, g2.name: g2, g3.name: g3, g4.name: g4}
    id = InventoryData()
    id.groups = groups

    g1_children_after_merge = g1.get_child_groups()


# Generated at 2022-06-12 22:08:15.420261
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    """
    Run the reconcile_inventory method of the InventoryData class on a simple inventory
    Checks that the ungrouped group contains the host 'jumper'
    Checks that the group windows contains the host 'jumper'
    Checks that the group all contains the host 'jumper'
    """
    hosts = [
        "jumper ansible_port=5555 ansible_host=192.0.2.50",
        "[windows]",
        "jumper",
    ]

    inventory = InventoryData()
    for line in hosts:
        inventory.add_host(line)

    inventory.reconcile_inventory()
    assert inventory.get_host('jumper').name == 'jumper'

    # Check that the ungrouped group contains the host 'jumper'

# Generated at 2022-06-12 22:08:24.967250
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory = InventoryData()
    inventory.add_host(host="host1", group="group1")
    inventory.add_host(host="host2", group="group1")
    inventory.add_host(host="host3", group="group2")
    inventory.add_host(host="host4", group="group2")
    inventory.add_host(host="host5", group="group3")
    inventory.add_host(host="host6", group="group3")

    inventory.remove_group("group3")
    inventory.add_host(host="host7", group="group4")
    inventory.add_host(host="host8", group="group4")
    inventory.add_host(host="host9", group="group4")
    inventory.add_host(host="host10", group="group4")

   

# Generated at 2022-06-12 22:08:40.046892
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    '''
    Function to test method to reconcile_inventory of InventoryData class
    '''
    inventory_data = InventoryData()
    test_inventory = {'group1': {'hosts': ['host1', 'host2'], 'vars': {'ansible_connection': 'local'}},
                      'group2': {'hosts': ['host2', 'host3'], 'vars': {'ansible_connection': 'local'}},
                      'all': {'hosts': ['host2'], 'vars': {'ansible_connection': 'local'}}}
    for group, group_data in iteritems(test_inventory):
        # add groups with its details
        inventory_data.add_group(group)
        # add group vars

# Generated at 2022-06-12 22:08:48.984606
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory_data = InventoryData()
    inventory_data.add_host("foo.example.org")
    inventory_data.add_host("bar.example.org")
    inventory_data.add_group("qinling")
    inventory_data.add_group("devops")
    inventory_data.add_child("qinling", "foo.example.org")
    inventory_data.add_child("qinling", "bar.example.org")
    inventory_data.reconcile_inventory()
    assert inventory_data.get_group("qinling").get_hosts() == [inventory_data.get_host("bar.example.org"), inventory_data.get_host("foo.example.org")]

# Generated at 2022-06-12 22:09:00.429756
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    """Unit test for method 'reconcile_inventory' of class 'InventoryData'"""
    # Initializations
    id=InventoryData()
    assert 'all' in id.groups
    assert 'ungrouped' in id.groups
    assert 'all' in id.groups['all'].get_children()
    assert 'ungrouped' in id.groups['all'].get_children()
    assert id.groups['all'].name=='all'
    assert id.groups['ungrouped'].name=='ungrouped'
    assert id.groups['all'] in id.groups['ungrouped'].get_ancestors()
    assert id.groups['all'].name=='all'
    assert id.groups['ungrouped'].name=='ungrouped'
    assert id.hosts=={}


# Generated at 2022-06-12 22:09:14.159238
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    groups = {
        'alpha': Group('alpha'),
        'beta': Group('beta'),
        'all': Group('all'),
        'ungrouped': Group('ungrouped')
    }
    groups['all'].add_child_group(groups['ungrouped'])

    # Initialize InventoryData with groups.
    # The inventory would have contained one group 'all' and one child group called 'ungrouped'
    inventory_data = InventoryData()
    inventory_data.groups = groups

    # Adding a new group should add the new group 'gamma' in the groups dictionary
    inventory_data.add_group('gamma')
    assert('gamma' in inventory_data.groups)
    assert(inventory_data.groups['gamma'].name == 'gamma')

    # If we already have a group 'gamma', then

# Generated at 2022-06-12 22:09:26.099235
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventory = InventoryData()
    assert(inventory)
    inventory.add_host("test_host")
    assert("test_host" in inventory.hosts)
    assert("test_host" not in inventory.groups)
    assert("test_host" not in inventory.groups.get("test_host", {}).hosts)
    assert("test_host" not in inventory.groups.get("test_host", {}).children)
    assert("test_host" not in inventory.groups.get("test_host", {}).parent.hosts)
    assert("test_host" not in inventory.groups.get("test_host", {}).parent.children)
    assert("test_host" not in inventory.groups.get("test_host", {}).parent.parent.hosts)

# Generated at 2022-06-12 22:09:36.147481
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    inventory_data = InventoryData()
    assert len(inventory_data.groups) == 2
    #Test add a new group and make sure that it is added to groups
    inventory_data.add_group('test_group')
    assert len(inventory_data.groups) == 3
    #Test add a existing group and make sure that it is not added twice and existing entry
    #is not changed
    inventory_data.add_group('test_group')
    assert len(inventory_data.groups) == 3
    assert 'test_group' in inventory_data.groups
    assert 'test_group' in inventory_data.groups['all'].children


# Generated at 2022-06-12 22:09:43.717347
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    from ansible.inventory.host import Host

    # 0. Precondition: set environment
    host = 'host1'
    group = 'group1'
    inventory = InventoryData()

    # 1. Construct host object
    host1 = Host(host)
    inventory.add_host(host1.name, group)

    # 2. Reconcile inventory
    inventory.reconcile_inventory()

    # 3. Check result
    assert(group in inventory.groups[group].get_hosts()[0].get_groups())

# Generated at 2022-06-12 22:09:52.075063
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventory = InventoryData()
    inventory.add_host('hosts')
    host = inventory.hosts['hosts']
    assert host.name == 'hosts'
    assert host.vars == {}
    assert inventory.get_groups_dict() == {}

    inventory.add_group('group')
    group = inventory.groups['group']
    assert group.name == 'group'
    assert group.vars == {}
    assert group.children == []
    assert group.get_hosts() == []
    assert inventory.get_groups_dict() == {'group': []}

    inventory.add_host('hosts', 'group')
    host = inventory.hosts['hosts']
    assert host.name == 'hosts'
    assert host.vars == {}
    assert host.get_groups() == ['group']


# Generated at 2022-06-12 22:09:54.428310
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    inventory = InventoryData()
    inventory.add_group('mygroup')
    inventory.add_group('mygroup')
    print(inventory.groups)



# Generated at 2022-06-12 22:10:01.670699
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    test_inventory = InventoryData()

    test_inventory.add_group('group1')
    test_inventory.add_group('group2')
    test_inventory.add_group('group3')

    test_inventory.add_host('localhost')
    test_inventory.add_host('localhost2', 'group1')
    test_inventory.add_host('localhost3', 'group2')
    test_inventory.add_host('localhost4', 'group3')

    test_inventory.add_child('group2', 'localhost')
    test_inventory.add_child('group3', 'localhost')
    test_inventory.add_child('group2', 'group1')

    test_inventory.reconcile_inventory()

    assert test_inventory.localhost.name == 'localhost'

# Generated at 2022-06-12 22:10:18.778590
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    # Initialize
    expected_result = {'all': Group(name='all'), 'ungrouped': Group(name='ungrouped'), 'test': Group(name='test'), 'test1': Group(name='test1')}
    inventory_data = InventoryData()
    #
    # add first group
    inventory_data.add_group('test')
    # add second group
    inventory_data.add_group('test1')
    # add third group (with same name)
    inventory_data.add_group('test')
    # add fourth group (with same name)
    inventory_data.add_group('test1')
    # add fifth group (with special char)
    inventory_data.add_group('*')
    # add sixth group (with special char)
    inventory_data.add_group('$')
    #

# Generated at 2022-06-12 22:10:20.916139
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventory_data = InventoryData()
    test_host = 'test_host'
    assert(test_host.name not in inventory_data.hosts)
    inventory_data.add_host(test_host)
    assert(test_host.name in inventory_data.hosts)

# Generated at 2022-06-12 22:10:23.613970
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    data = InventoryData()
    data.add_host("test_host")
    assert("test_host" in data.hosts)
    assert("test_host" not in data.groups)


# Generated at 2022-06-12 22:10:25.346699
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    inventory_data = InventoryData()
    assert inventory_data.add_group("TestGroup") == "TestGroup"


# Generated at 2022-06-12 22:10:37.671898
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    inv_obj = InventoryData()

    # add group 'test_group'
    assert inv_obj.add_group('test_group') == 'test_group'

    # add same group 'test_group' again
    assert inv_obj.add_group('test_group') == 'test_group'

    # add new group 'test_group2'
    assert inv_obj.add_group('test_group2') == 'test_group2'

    # add empty group
    try:
        inv_obj.add_group('')
    except AnsibleError:
        # expected exception
        pass
    else:
        # unexpected result
        assert False

    # add a group which is not a string

# Generated at 2022-06-12 22:10:44.303112
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    # Tests a valid group
    inventory = InventoryData()
    assert inventory.add_group('test') == 'test'
    # Tests a None group
    try:
        inventory.add_group(None)
    except AnsibleError as e:
        assert 'Invalid empty/false group name provided' in str(e)
    # Tests a group that already exists, returns the same group
    assert inventory.add_group('test') == 'test'


# Generated at 2022-06-12 22:10:45.814446
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    pass


# Generated at 2022-06-12 22:10:49.523881
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    instance = InventoryData()
    host = 'localhost'
    group = 'all'
    port = None
    expected = 'localhost'
    actual = instance.add_host(host, group, port)
    assert actual == expected

# Generated at 2022-06-12 22:11:00.570507
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    # Reconcile an empty inventory
    inventory = InventoryData()
    inventory.reconcile_inventory()
    assert inventory.groups == {'all': Group('all'), 'ungrouped': Group('ungrouped')}
    assert inventory.hosts == {}
    assert inventory.get_groups_dict() == {}

    # Reconcile an inventory with one host and no groups
    inventory = InventoryData()
    inventory.add_host('localhost')
    inventory.reconcile_inventory()
    assert inventory.groups == {'all': Group('all'), 'ungrouped': Group('ungrouped')}
    assert inventory.hosts == {'localhost': Host('localhost')}
    assert inventory.get_groups_dict() == {'all': {'localhost'},
                                           'ungrouped': {'localhost'}}

    #

# Generated at 2022-06-12 22:11:05.847743
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    # Test: no item to delete
    i = InventoryData()
    assert i.add_group('newgroup') == 'newgroup'
    assert i.groups['newgroup'].name == 'newgroup'

    # Test invalid group name

# Generated at 2022-06-12 22:11:22.982042
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    id = InventoryData()
    id.add_host('host1')
    id.add_host('host2')
    id.add_host('host3')
    id.add_group('group1')
    id.add_group('group2')
    id.add_child('group1', 'host1')
    id.add_child('group1', 'host2')
    id.add_child('group2', 'host2')
    id.add_child('group2', 'host3')
    id.add_child('group1', 'group2')
    id.reconcile_inventory()
    assert id.hosts['host1'].get_groups()[0].name == 'group1'
    assert id.hosts['host1'].get_groups()[1].name == 'group2'
   

# Generated at 2022-06-12 22:11:31.811463
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    # _groups_dict_cache should be empty
    inventory = InventoryData()
    assert inventory._groups_dict_cache == {}

    # add a group to inventory and check _groups_dict_cache is not empty
    group_name = "test_group"
    inventory.add_group(group_name)
    assert group_name in inventory._groups_dict_cache

    # add a host to inventory and check _groups_dict_cache is not empty
    host_name = "test_host"
    inventory.add_host(host_name, group=group_name)
    assert host_name in inventory._groups_dict_cache

    # remove the group from inventory and check _groups_dict_cache is empty
    inventory.remove_group(group_name)
    assert not inventory._groups_dict_cache

    # set a variable for host and check

# Generated at 2022-06-12 22:11:44.694676
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory = InventoryData()
    inventory.current_source = None
    inventory.add_group("all")
    inventory.add_group("ungrouped")
    inventory.add_group("first_group")
    inventory.add_group("second_group")
    inventory.add_host("localhost", "first_group")
    inventory.add_host("remote_host", "second_group")

    inventory.reconcile_inventory()

    assert inventory.get_hosts("first_group")[0].name == "localhost"
    assert inventory.get_hosts("second_group")[0].name == "remote_host"
    assert len(inventory.get_hosts("all")) == 2
    assert len(inventory.get_hosts("ungrouped")) == 0



# Generated at 2022-06-12 22:11:53.510955
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    # Test with empty inventory
    inventory = InventoryData()
    inventory.reconcile_inventory()
    assert inventory.current_source is None
    assert inventory.localhost is None
    assert len(inventory.hosts) == 0
    assert len(inventory.groups) == 2
    assert 'all' in inventory.groups
    assert 'ungrouped' in inventory.groups

    # Test with dummy data
    inventory = InventoryData()
    inventory.add_host("test_host1")
    inventory.add_host("test_host2")
    inventory.add_host("test_host3")
    inventory.add_host("test_host1", group='test_group1')
    inventory.add_host("test_host1", group='test_group2')

# Generated at 2022-06-12 22:12:02.064618
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    import os
    import sys
    import ansible.constants as C

    # Remove all previously cached plugins
    path = os.path.expanduser(C.DEFAULT_LOCAL_TMP)
    for plugin in os.listdir(path):
        try:
            os.remove(os.path.join(path, plugin))
        except Exception:
            continue

    sys.path.insert(0, C.DEFAULT_MODULE_PATH[0])
    from test_runner import ansible_test_show_custom_vars

    # Remove all custom variables
    if 'ansible_test_custom_vars' in os.environ:
        del os.environ['ansible_test_custom_vars']


# Generated at 2022-06-12 22:12:09.853547
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    """
    Test: 1. conflicts between hosts and groups are noticed, 2. all groups inherit from 'all', 3. implicit localhost is created

    :return:
    """
    data = InventoryData()
    data.add_group('group')
    data.add_host('group', 'group')
    data.reconcile_inventory()
    assert 'group' in data.groups
    assert 'group' in data.hosts
    assert 'all' in data.groups['group'].get_ancestors()
    assert data.localhost is not None
    assert data.localhost.name == 'group'

# test methods from the InventoryData class

# Generated at 2022-06-12 22:12:21.735823
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    '''
    Unit test for method reconcile_inventory of class InventoryData
    '''

    def check_host_and_group(host_name, host_object, group_name, group_object, result):
        '''
        Verify if the host and group are in the expected result
        '''
        try:
            assert host_name in result
        except AssertionError:
            print("Host %s is not in the result" % host_name)
            raise

        try:
            assert group_name in result
        except AssertionError:
            print("Group %s is not in the result" % group_name)
            raise

        try:
            assert result[host_name] == host_object
        except AssertionError:
            print("Host object %s is not right in the result" % host_name)
           

# Generated at 2022-06-12 22:12:33.134623
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    ''' Test InventoryData.reconcile_inventory() '''
    inventory_data = InventoryData()
    group = inventory_data.add_group(None)
    assert group == None

    group = inventory_data.add_group('group1')
    assert group == 'group1'

    host = inventory_data.add_host(host=None)
    assert host == None

    host = inventory_data.add_host(host='host0')
    assert host == 'host0'

    # Test the case that localhost is not in host.
    assert (inventory_data.localhost is None)
    assert (inventory_data.get_host('localhost'))

    # Test the case that localhost is in host.
    host2 = inventory_data.add_host(host='localhost')
    assert (host2 == 'localhost')


# Generated at 2022-06-12 22:12:39.612054
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    """
    Add host to inventory and possibly a group if not there already.
    """
    inventory = InventoryData()
    inventory.groups = { 'test_group': Group('test_group') }
    inventory.current_source = 'test_source'
    result = inventory.add_host('test_host', 'test_group', 123)
    assert(result == 'test_host')
    assert(len(inventory.hosts) == 1)
    assert(inventory.hosts['test_host'].name == 'test_host')
    assert(inventory.hosts['test_host'].port == 123)
    assert(inventory.hosts['test_host'].get_variable('ansible_host') == 'test_host')

# Generated at 2022-06-12 22:12:43.762087
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    i = InventoryData()
    i.add_host('localhost', 'default')
    assert(i.hosts['localhost'].get_group('default'))
    assert(not i.hosts['localhost'].get_group('not_default'))

# Generated at 2022-06-12 22:12:59.103206
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():

    # Create an empty InventoryData
    idata = InventoryData()

    # Add a host 'all' to a group 'all'
    idata.add_host('all',group='all')
    
    # Get the hosts and groups from the InventoryData
    groups = idata.groups
    hosts = idata.hosts
    # Check if the group 'all' exists
    assert ('all' in groups)

    # Check if 'all' is the only group
    assert (len(groups) == 1)

    # Get the only group 'all'
    group_all = groups['all']

    # Check if the group 'all' has the host 'all'
    assert ('all' in group_all.get_hosts())

    assert (len(hosts) == 1)

    assert ('all' in hosts)


# Generated at 2022-06-12 22:13:12.343341
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory_data = InventoryData()

    # test for empty inventory
    inventory_data.reconcile_inventory()
    assert(len(inventory_data.groups) == 2)
    assert(len(inventory_data.hosts) == 0)

    # test for non-implicit localhost
    inventory_data.hosts = {"localhost": Host("localhost")}
    inventory_data.reconcile_inventory()
    assert(len(inventory_data.groups) == 2)
    assert(len(inventory_data.hosts) == 1)
    assert(inventory_data.localhost == inventory_data.hosts["localhost"])

    # test for non-implicit localhost in ungrouped group
    inventory_data = InventoryData()
    inventory_data.hosts = {"localhost": Host("localhost")}

# Generated at 2022-06-12 22:13:23.358842
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventory = InventoryData()
    # Add new host
    inventory.add_host('test_host')
    assert 'test_host' in inventory.hosts
    assert inventory.hosts['test_host'].port is None
    # Add existing host
    inventory.add_host('test_host')
    assert 'test_host' in inventory.hosts
    # Test port
    inventory.add_host('test_host', port=22)
    assert 'test_host' in inventory.hosts
    assert inventory.hosts['test_host'].port == 22
    # Test group
    inventory.add_group('test_group')
    assert 'test_group' in inventory.groups
    inventory.add_host('test_host', group='test_group')
    assert 'test_host' in inventory.hosts

# Generated at 2022-06-12 22:13:30.112589
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventory_data = InventoryData()
    inventory_data.add_host('test_host', 'test_group')
    assert inventory_data.hosts['test_host'].name == 'test_host'
    assert inventory_data.groups['test_group'].name == 'test_group'
    assert inventory_data.groups['test_group'].get_hosts()[0].name == 'test_host'


# Generated at 2022-06-12 22:13:38.834991
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    data_inventory = InventoryData()

    # Test adding groups
    assert data_inventory.add_group("group_A") == "group_A"
    assert data_inventory.add_group("group_B") == "group_B"
    assert data_inventory.add_group("group_A") == "group_A"

    # Test adding non-string group
    try:
        data_inventory.add_group(123)
        assert False
    except AssertionError:
        raise AssertionError("Expected AnsibleError for adding a non-string group.")

    # Test adding empty string group
    try:
        data_inventory.add_group("")
        assert False
    except AssertionError:
        raise AssertionError("Expected AnsibleError for adding an empty string group.")


# Generated at 2022-06-12 22:13:50.947003
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    inventoryData = InventoryData()

    # Test: add_host method with arguments host, group and port
    inventoryData.add_host('www-example-com', 'all', '22')

    # Test: There is a dict of hosts
    assert(inventoryData.hosts != None)

    # Test: There is an host named www-example-com inside the dict
    assert('www-example-com' in inventoryData.hosts)

    # Test: The host www-example-com has 22 as port
    assert(inventoryData.hosts['www-example-com'].port == '22')

    # Test: The group all has the host www-example-com
    assert(inventoryData.groups['all'].has_host(inventoryData.hosts['www-example-com']))



# Generated at 2022-06-12 22:14:01.613045
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():

    # Basic inventory data
    inventory_data = InventoryData()
    inventory_data.add_group('group1')
    inventory_data.add_group('group2')
    inventory_data.add_child('group1', 'group2')
    inventory_data.add_host('host1')
    inventory_data.add_host('host2')
    inventory_data.add_host('host3')
    inventory_data.add_child('group1', 'host1')
    inventory_data.add_child('group2', 'host2')
    inventory_data.add_child('group1', 'host3')

    # The following tests are based on documented behaviour of method reconcile_inventory

    # 1. test default localhost being created and set for inventory
    inventory_data.reconcile_inventory()
    localhost = inventory_data

# Generated at 2022-06-12 22:14:13.576496
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    # This is a test method for the InventoryData class's function reconcile_inventory
    #
    # It will be called automatically when executing unit test by running:
    # ansible-test units --python-version=2.7 --inventory
    #
    # The test code is wrapped in a function to avoid it executing
    # before we perform the test.

    data = InventoryData()

    # Add localhost to the inventory explicitly
    data.add_host('localhost', group='all')

    # No localhost was added implicitly yet
    assert data.localhost is None

    # Implicit localhost should be created when we try to add for the first time a host,
    # localhost, to the inventory.
    data.add_host('localhost', group='testhost1')
    assert data.localhost is not None

    # Now that a localhost was added implicitly, it

# Generated at 2022-06-12 22:14:24.293785
# Unit test for method add_group of class InventoryData
def test_InventoryData_add_group():
    inv = InventoryData()
    assert len(inv.groups) == 2
    inv.add_group("group1")
    assert len(inv.groups) == 3
    # group name has to be a string, it can not be an integer
    try:
        inv.add_group(1)
    except Exception as e:
        assert type(e) is AnsibleError
        assert e.args[0] == "Invalid group name supplied, expected a string but got <type 'int'> for 1"
    # group name can not be empty
    try:
        inv.add_group("")
    except Exception as e:
        assert type(e) is AnsibleError
        assert e.args[0] == "Invalid empty/false group name provided: "
    # when a group is already in the inventory, it won't be re-added
    inv

# Generated at 2022-06-12 22:14:29.478259
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    inventory_data = InventoryData()
    host1 = Host('host1')
    inventory_data.add_host(host1.name)
    inventory_data.add_group('group1')
    inventory_data.add_child('group1', host1.name)
    inventory_data.reconcile_inventory()
    assert len(inventory_data.groups['all'].get_hosts()) == 2


# Generated at 2022-06-12 22:14:43.000529
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():
    # test if add_host adds host to inventory and adds host to group
    test_host = "test_host"
    test_group = "test_group"

    new_inventory = InventoryData()
    new_inventory.add_host(test_host, test_group)
    new_inventory.add_group(test_group)
    if test_host in new_inventory.hosts and new_inventory.hosts[test_host] in new_inventory.groups[test_group].get_hosts():
        print("add_host add host to inventory and add host to group")
    else:
        print("add_host not add host to inventory and add host to group")

    # test if add_host removes group from host when host added a group
    new_inventory.add_child(test_group, test_host)

# Generated at 2022-06-12 22:14:54.765203
# Unit test for method reconcile_inventory of class InventoryData
def test_InventoryData_reconcile_inventory():
    """
    Special case where a host is present in more than one group, and
    if one of the hosting groups is being removed, the same host
    should still be present in the Inventory
    """

    inv_data = InventoryData()
    inv_data.add_host('test_host')
    inv_data.add_group('test_group_1')
    inv_data.add_group('test_group_2')
    inv_data.add_child('test_group_1', 'test_host')
    inv_data.add_child('test_group_2', 'test_host')

    inv_data.remove_group('test_group_1')
    inv_data.reconcile_inventory()

    assert inv_data.get_host('test_host')


# Generated at 2022-06-12 22:15:01.994444
# Unit test for method add_host of class InventoryData
def test_InventoryData_add_host():

    inventory = InventoryData()

    # List of the IP addresses of the configured servers, with the corresponding public hosts in the inventory
    servers = [('127.0.0.1', 'localhost'), ('1.1.1.1', '116.xip.io'), ('1.1.1.2', '17o.xip.io')]

    for ip, host in servers:
        inventory.add_host(host, group='all', port=22)
        inventory.set_variable(host, 'ansible_ssh_host', ip)
        inventory.set_variable(host, 'ansible_ssh_port', 22)

    inventory.reconcile_inventory()

    # We need to have 2 groups in the inventory
    assert len(inventory.groups) == 2
    # We need to have 3 hosts in the inventory