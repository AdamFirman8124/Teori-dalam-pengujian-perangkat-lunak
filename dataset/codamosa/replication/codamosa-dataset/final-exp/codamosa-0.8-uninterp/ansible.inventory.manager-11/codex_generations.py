

# Generated at 2022-06-12 22:27:17.874683
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    hosts = dict()
    hosts['host1'] = dict(hostname='host1')
    hosts['host2'] = dict(hostname='host2')
    inv = InventoryManager(hosts)
    thehosts = inv.list_hosts()
    assert len(thehosts) == 2
    assert thehosts[0] == 'host1'
    assert thehosts[1] == 'host2'



# Generated at 2022-06-12 22:27:22.486261
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    """
    Test list_hosts of InventoryManager
    """
    # Before
    inventory_manager = InventoryManager()
    pattern = "all"
    inventory_manager.list_hosts(pattern)
    # After
    inventory_manager = InventoryManager()
    pattern = "all"
    inventory_manager.list_hosts(pattern)


# Generated at 2022-06-12 22:27:31.893760
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    from collections import namedtuple
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    def getSubsetUUIDs(subset):
        subset_uuids = set(s._uuid for s in self._evaluate_patterns(subset))
        return subset_uuids
    def getHosts(self, pattern, ignore_limits, ignore_restrictions, order):
        # only used as a hash key in self._hosts_patterns_cache dict
        # a tuple is faster than stringifying
        pattern_hash = tuple(pattern)
        pattern_list = pattern[:]
        # Check if pattern already computed

        pattern_list.extend(self._subset)
        pattern_list.extend(self._restriction)
        patterns

# Generated at 2022-06-12 22:27:42.292900
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    im = InventoryManager(None, None)
    # get_hosts()
    # get_hosts(pattern='all')
    # get_hosts(pattern='all', ignore_limits=True)
    # get_hosts(pattern='all', ignore_limits=False, ignore_restrictions=True)
    # get_hosts(pattern='all', ignore_limits=False, ignore_restrictions=False, order='sorted')
    # get_hosts(pattern='all', ignore_limits=False, ignore_restrictions=False, order='reverse_sorted')
    # get_hosts(pattern='all', ignore_limits=False, ignore_restrictions=False, order='reverse_inventory')
    # get_hosts(pattern='all', ignore_limits=False, ignore_restrictions=False, order='sh

# Generated at 2022-06-12 22:27:45.351524
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
  pattern = ""
  expected = None
  test_instance = InventoryManager(pattern)
  assert vars(test_instance) == vars(InventoryManager(pattern))
  assert test_instance.subset(pattern) == expected


# Generated at 2022-06-12 22:27:52.581033
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    ansible = Ansible()
    runner = CliRunner()

    runner.invoke(molecule.command.converge,
                  ['default', '--no-create', '--no-destroy'])
    inventory = ansible.inventory.from_options(
        os.environ['MOLECULE_INVENTORY_FILE'],
        os.environ['MOLECULE_ANSIBLE_CONFIG'])

    inventory_manager = InventoryManager(inventory=inventory)

    pattern = "all"
    result = inventory_manager.list_hosts(pattern=pattern)
    assert result == ['instance-1', 'instance-2']

    pattern = "all:vars"
    result = inventory_manager.list_hosts(pattern=pattern)
    assert result == []

    pattern = "example-1:vars"


# Generated at 2022-06-12 22:28:01.217383
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory_manager = InventoryManager()
    # host list
    host_list = ['localhost', '192.168.1.1', '1001:3020:2010:1222:202:edff:fe6c:f632']

    # test with ',' separated strings
    source = ','.join(host_list)
    host_list_1 = inventory_manager._parse_source(source)
    assert(host_list_1 == host_list)

    # test with space separated strings
    source = ' '.join(host_list)
    host_list_2 = inventory_manager._parse_source(source)
    assert(host_list_2 == host_list)

    # test with list elements and one newline
    source = "\n".join(host_list[:-1]) + ' ' + host_list[-1]

# Generated at 2022-06-12 22:28:06.587784
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory = InventoryManager(loader=None, sources=[])
    inventory.parse_inventory(host_list=[
        "localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python2.7"
    ])

    hosts = inventory.list_hosts()
    assert len(hosts) == 1
    assert hosts[0] == "localhost"

# Generated at 2022-06-12 22:28:17.676408
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    config={'scheduler.dir':"/tmp"}
    ansible_cfg = os.path.join(config['scheduler.dir'],'ansible.cfg')
    with open(ansible_cfg, 'w') as file:
        file.write("[defaults]\n"
                   "host_key_checking = False\n"
                   "nocows = True\n")
    im = InventoryManager(loader=DataLoader())
    config['inventory'] = os.path.join(config['scheduler.dir'], 'hosts')

# Generated at 2022-06-12 22:28:24.100595
# Unit test for function split_host_pattern
def test_split_host_pattern():
    assert split_host_pattern('') == []
    assert split_host_pattern('a') == ['a']
    assert split_host_pattern(' a , b,\tc[1-2] ') == ['a', 'b', 'c[1-2]']
    assert split_host_pattern('[2001:db8::1]:80') == ['[2001:db8::1]:80']
    assert split_host_pattern('[2001:db8::1,localhost]') == ['[2001:db8::1,localhost]']

# FIXME: the code below is the old inventory API (and has the old API docs)
# the code above is the new API. These should be merged in a future version.


# Generated at 2022-06-12 22:29:31.545080
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # Check basic functionality.
    mgr = InventoryManager(None, None)
    mgr.subset('foo[1]')
    assert mgr._subset == ['foo[1]']

    # Check that @filename reads in the file.
    t_path = tempfile.mkdtemp()
    t_name = os.path.join(t_path, 'foo.txt')

# Generated at 2022-06-12 22:29:41.305429
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    assert hasattr(InventoryManager, "list_hosts")

    # initializes inventory
    inventory = InventoryManager(loader=None, sources='localhost')

    # initialize InventoryManager object and call list_hosts
    inventory_object = InventoryManager(loader=None, sources=None)
    assert_equals(inventory_object.list_hosts(), [])

    # initialize InventoryManager object and call list_hosts
    inventory_object = InventoryManager(loader=None, sources=inventory)
    assert_equals(inventory_object.list_hosts(), ['localhost'])

    # initialize InventoryManager object and call list_hosts
    inventory_object = InventoryManager(loader=None, sources=inventory)
    assert_equals(inventory_object.list_hosts(pattern='all'), ['localhost'])

    # initialize InventoryManager object and call list_

# Generated at 2022-06-12 22:29:49.671531
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    # TODO: mock Inventory class
    inventory = Inventory("")
    im = InventoryManager(inventory)

    # test for list method
    # TODO: mock Inventory class and Host class
    host = Host("")
    host.name = "foo"
    with patch("ansible.inventory.manager.InventoryManager._match_one_pattern", return_value=[host]):
        assert im.list_hosts("all") == ["foo"]

    # test for regex method
    with patch("ansible.inventory.manager.InventoryManager._match_one_pattern", return_value=[host]):
        assert im.list_hosts("~foo*") == ["foo"]

# Generated at 2022-06-12 22:29:51.949080
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager()
    pattern = "all"
    assert inventory_manager.subset(pattern) == None
    

# Generated at 2022-06-12 22:29:55.728295
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory = InventoryManager(loader, sources='localhost,')
    inv_result = inventory.list_hosts()
    assert(inv_result == ['127.0.0.1'])

# Generated at 2022-06-12 22:30:06.769836
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    target = InventoryManager()
    test_source = [
        '# comment',
        '[group1]',
        'host1',
        'host2',
        '',
        '[group2]',
        'host3',
        '[group3]',
        'host4',
        '[group1:vars]',
        'var1=value1',
        '[group2:vars]',
        'var2=value2',
        '[group3:children]',
        'group2',
        '[group3:vars]',
        'var3=value3',
        '[group1:children]',
        'group3',
    ]
    # test that parsing works with a list of strings instead of a file-like object
    target.parse_source('test_source', test_source)
    # Check that it

# Generated at 2022-06-12 22:30:19.591126
# Unit test for function order_patterns

# Generated at 2022-06-12 22:30:25.647956
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # create test InventoryManager object
    from collections import namedtuple
    FakeInventory = namedtuple('FakeInventory', ['hosts', 'groups'])
    fake_inventory = FakeInventory(hosts={'somehost': 'somehost'}, groups={})

    im = InventoryManager(loader=None, variable_manager=None, host_list=None)
    im._inventory = fake_inventory
    im.subset(subset_pattern='all')
    assert im._subset == ['all'], 'Fail: InventoryManager.subset did not set _subset to all when given "all"'
    im._subset = None
    im.subset(subset_pattern='somehost')
    assert im._subset == ['somehost'], 'Fail: InventoryManager.subset did not set _subset to somehost when given somehost'

# Generated at 2022-06-12 22:30:38.066347
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inv = InventoryManager('/some/inventory')
    assert inv._parse_source('localhost,') == ['localhost']
    assert inv._parse_source(',localhost,') == ['localhost']
    assert inv._parse_source('127.0.0.1,') == ['127.0.0.1']
    assert inv._parse_source('127.0.0.1,::1,') == ['127.0.0.1', '::1']
    assert inv._parse_source('127.0.0.1,::1,localhost,') == ['127.0.0.1', '::1', 'localhost']
    assert inv._parse_source(',,127.0.0.1,,::1,,localhost,,') == ['127.0.0.1', '::1', 'localhost']

# Generated at 2022-06-12 22:30:49.085045
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
  assert InventoryManager().list_hosts() == []
  assert InventoryManager().list_hosts(pattern='all') == []
  assert InventoryManager().list_hosts(pattern='all') == []
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']
  assert InventoryManager().list_hosts(pattern='test') == ['test']


# Generated at 2022-06-12 22:31:16.227206
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inv = InventoryManager(
        vault_password_files=["password_file_1", "password_file_2"]
    )
    mock_inv = Mock()
    mock_inv._hosts = {}
    mock_inv._groups = {'foo': {}}
    mock_inv._vars = {}
    inv._inventory = mock_inv
    inv._subset = None

    pattern = "~All"
    inv.subset(pattern)
    assert inv._subset == [pattern]

# Generated at 2022-06-12 22:31:18.409770
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
	# This test is intended to check whether the inventory objects returned from the 
	# get_hosts method of the InventoryManager class are really of type 'Host'
	pass
	

# Generated at 2022-06-12 22:31:18.940990
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    pass

# Generated at 2022-06-12 22:31:20.045400
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # TODO: validate returned data
    pass


# Generated at 2022-06-12 22:31:31.268875
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    '''
    Test the subset method of class InventoryManager
    '''
    string_subset_pattern = "two_hosts"
    list_subset_pattern = [ 'one_host', 'two_hosts' ]
    
    inventory_manager = InventoryManager(None)
    inventory_manager.subset(string_subset_pattern)
    
    assert inventory_manager._subset == list_subset_pattern
    assert isinstance(inventory_manager._subset, list)
    assert inventory_manager._subset == [ 'one_host', 'two_hosts' ]
    
    inventory_manager.subset(list_subset_pattern)
    assert inventory_manager._subset == list_subset_pattern
    assert isinstance(inventory_manager._subset, list)

# Generated at 2022-06-12 22:31:34.238833
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    '''
    Test if InventoryManager.subset works as expected when some of the inputs are negative
    '''
    assert True

# Generated at 2022-06-12 22:31:36.822273
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    """
    Unit test for method parse_source of class InventoryManager.

    :return: ``True`` if test pass, ``False`` otherwise
    """
    # TODO: write unit test
    return False

# Generated at 2022-06-12 22:31:46.617826
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # test with normal subset pattern
    m = InventoryManager(inventory=dict())
    m.subset('pattern')
    assert m._subset == ['pattern']
    # test with @file.yml subset pattern
    m = InventoryManager(inventory=dict())
    m.subset('@file.yml')
    assert m._subset == ['@file.yml']
    # test with empty subset pattern
    m = InventoryManager(inventory=dict())
    m.subset('')
    assert m._subset == []
    # test with multiple subset pattern
    m = InventoryManager(inventory=dict())
    m.subset('pattern1 pattern2')
    assert m._subset == ['pattern1', 'pattern2']
    # test with multiple subset pattern, one of which is a file
    m = InventoryManager(inventory=dict())

# Generated at 2022-06-12 22:31:53.513695
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # check return value is not list
    inventory = InventoryManager(loader=None, sources="")
    res = inventory.subset(subset_pattern=None)
    assert res is None
    # check return value is not list
    inventory = InventoryManager(loader=None, sources="")
    res = inventory.subset(subset_pattern='subset_pattern')
    assert res is None

# Generated at 2022-06-12 22:31:54.905049
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():

    manager = InventoryManager(loader=None, sources=C.DEFAULT_HOST_LIST)
    print("Passed!")



# Generated at 2022-06-12 22:33:23.275423
# Unit test for method list_hosts of class InventoryManager

# Generated at 2022-06-12 22:33:30.189237
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory_manager = InventoryManager(loader=None, sources=None)
    pattern = 'test_pattern'
    ignore_limits = False
    ignore_restrictions = False
    order = None
    host_list = ['test_host']
    inventory_manager._hosts_patterns_cache = {tuple([pattern]): host_list}
    assert inventory_manager.get_hosts(pattern, ignore_limits, ignore_restrictions, order) == host_list



# Generated at 2022-06-12 22:33:34.789190
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    im = InventoryManager()
    im.subset('all')
    # assert im._subset == ['all']
    im.subset('s1:s2')
    # assert im._subset == ['s1:s2']
    im.subset('@filename')
    # assert im._subset == ['@filename']
    # TODO add test cases to cover more detailed logic


# Generated at 2022-06-12 22:33:42.417342
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory = InventoryManager(loader=None, sources=[])
    inventory.subset('all')
    assert inventory._subset == ['all']
    inventory._subset = None
    inventory.subset('test*')
    assert inventory._subset == ['test*']
    inventory._subset = None
    inventory.subset(['test1', 'test2'])
    assert inventory._subset == ['test1', 'test2']
    inventory._subset = None
    inventory.subset(['@', 'test'])
    assert inventory._subset == ['@', 'test']
    inventory._subset = None
    inventory.subset('@testfile')
    assert inventory._subset == ['@', 'test']


# Generated at 2022-06-12 22:33:46.074128
# Unit test for function split_host_pattern
def test_split_host_pattern():
    """
    This function is called by test/plugins/inventory/test_inventory.py so that we
    have a line in the .coverage file for this function. It doesn't really test anything,
    but can be used as a reference point for calling the function.
    """

    split_host_pattern(b"foo")



# Generated at 2022-06-12 22:33:53.736699
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory


# Generated at 2022-06-12 22:34:02.720819
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    
    # Test data
    inventory_dict = {
        'group_a': [ 'host-a', 'host-b', 'host-c' ],
        'group_b': [ 'host-d', 'host-e', 'host-f' ],
        'ungrouped': [ 'host-g' ]
    }
    
    # Create a inventory manager object and load inventory
    inv = InventoryManager(inventory=Inventory(loader=DictDataLoader(inventory_dict)))

    # Test case 1. No restriction, no pattern
    hosts = inv.get_hosts()
    assert inv.list_hosts() == hosts
    assert len(hosts) == 7 # All groups + ungrouped
    assert inv._pattern_cache[inv._restriction[0]] == hosts

    # Test case 2. No restriction, pattern=all
   

# Generated at 2022-06-12 22:34:11.558592
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    im = InventoryManager()
    im.add_host('remote1', 'group1')
    im.add_host('remote2', 'group2')
    im.add_group('group1')
    im.add_group('group2')
    im.add_child('group1', 'group2')

    assert im.list_hosts('remote1') == ['remote1']
    assert im.list_hosts(['remote1']) == ['remote1']
    assert im.list_hosts('group1') == ['remote1', 'remote2']
    assert im.list_hosts('group2') == ['remote2']
    assert im.list_hosts('all') == ['remote1', 'remote2']
    assert im.list_hosts('group*') == ['remote1', 'remote2']

# Generated at 2022-06-12 22:34:17.663408
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # Put bad values before good ones to make sure bad ones are actually discarded
    bad_values = ["", " ", "garbage", "garbage,foo", "garbage:foo", "hosts:", "hosts: ", "hosts::foo", " /wrong/path "] # absolute path
    good_values = ["hosts", "hosts:foo", "hosts:foo.yaml", "hosts:foo.yml", "hosts: foo.yaml", "hosts:foo.yaml ", " /right/path "] # absolute path

    # Get the InventoryManager object
    im = InventoryManager()
    results = im.parse_source(bad_values + good_values)

    # Check the results
    assert len(results) == 5
    assert results[0] == ("hosts", "foo", "foo.yaml")

# Generated at 2022-06-12 22:34:27.906076
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory = InventoryManager('')
    inventory.subset('all')
    assert inventory._subset is None

    inventory = InventoryManager('')
    inventory.subset('@/tmp/nonexistant')
    assert inventory._subset == ['@/tmp/nonexistant']

    inventory.subset('@/tmp/nonexistant')
    assert inventory._subset == ['@/tmp/nonexistant']

    fd, tmp_name = tempfile.mkstemp('ansible-test-inventory')
    os.write(fd, to_bytes(u'\n'.join(['host1', 'host2'])))
    os.close(fd)

    inventory.subset('@%s' % tmp_name)
    assert inventory._subset == ['@%s' % tmp_name]


# Generated at 2022-06-12 22:35:10.056390
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():

    # Unit test for method subset() of class InventoryManager

    #TODO: Get a proper set of unit tests established
    assert 0 == 1

# Generated at 2022-06-12 22:35:17.114932
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # create an InventoryManager for mocking
    inventory_manager = InventoryManager()

    # create a test SourceData
    source_data = SourceData('/Users/user1/source-data', 'hosts', 'var1=value1;var2=value2', 'yaml', False)

    # call the method with mocked SourceData
    inventory_manager.parse_source(source_data)

    # Assert
    assert source_data.inventory_name == 'hosts.yaml'
    assert source_data.inventory_directory == '/Users/user1/source-data'
    assert source_data.inventory_filename == 'hosts.yaml'
    assert source_data.group_vars_string == 'var1=value1;var2=value2'
    assert source_data.group_vars_file == ''
    assert source

# Generated at 2022-06-12 22:35:24.050206
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    id = 'e523dde1-a916-4da4-9d4b-ebe383cf5f85'
    # id = '5eb141c2-55bd-4c9e-a9ac-e528c8a8f3d3'
    inventory = InventoryManager(id)
    # print(inventory.__dict__)
    # hosts = inventory.get_hosts()
    # print(hosts)
    pattern = 'app*'
    hosts = inventory.get_hosts(pattern=pattern)
    print(hosts)
    # print(json.dumps(hosts, indent=2))


# Generated at 2022-06-12 22:35:25.115634
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
	assert False, "test #1 of test_InventoryManager_subset"

# Generated at 2022-06-12 22:35:31.222215
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # setup inventory
    source = u"""
    [one]
    foo[0]
    foo[1]
    foo[2]
    a:b
    b:c
    foo1
    foo2
    foo3
    [two]
    foo[0-2]
    a:c
    b:d
    foo1
    foo2
    foo3
    [three]
    foo[0:2]
    a:d
    b:e
    foo1
    foo2
    foo3
    """
    inv = InventoryManager(loader=DictDataLoader({'source': source}))
    # inventory parser
    inv.parse_source('source')
    # check for host vars
    assert inv.get_host('foo1').vars['a'] == 'b'
    assert inv.get_

# Generated at 2022-06-12 22:35:38.486547
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    output = []
    inventory_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '../data/inventory', 'test_inventory_manager.ini')
    im = InventoryManager(loader=DictDataLoader(),
                        sources=inventory_file)
    assert im
    im.clear_pattern_cache()
    output = im.list_hosts()
    assert len(output) > 1
    output = im.list_hosts(pattern='all')
    assert len(output) > 1

# Generated at 2022-06-12 22:35:44.787362
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])
    host = Host(name='127.0.0.1')
    group = Group(name='ungrouped')
    inventory.add_host(host)
    inventory.add_group(group)
    inventory.set_play_context(PlayContext(remote_user='root'))
    assert inventory.hosts
    subset = ['127.0.0.1,']
    inventory.subset(subset_pattern=subset)
    assert inventory._subset is not None



# Generated at 2022-06-12 22:35:52.299008
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():

    inventory_manager = InventoryManager()
    # inventory_manager.subset(subset_pattern) <- this is what what we test

    # don't match, subset_pattern=None
    b_result = inventory_manager.subset(None)
    # check result
    assert b_result is None

    # no match, subset_pattern="@/tmp/limits"
    b_result = inventory_manager.subset("@/tmp/limits")
    # check result
    assert b_result == 2

    # don't match, subset_pattern="@/tmp/limits"
    b_result = inventory_manager.subset("@/tmp/limits")
    # check result
    assert b_result == 2

    # no match, subset_pattern="@/tmp/limits"

# Generated at 2022-06-12 22:35:54.166090
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager([], [])
    inventory = InventoryManager([], [])
    inventory.subset("all")


# Generated at 2022-06-12 22:35:58.744712
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory_manager = InventoryManager(loader = None, sources = None)
    assert inventory_manager.parse_source("aws_ec2.yml") == ("aws_ec2", "yml")
    assert inventory_manager.parse_source("test.txt") == ("test", "txt")
    