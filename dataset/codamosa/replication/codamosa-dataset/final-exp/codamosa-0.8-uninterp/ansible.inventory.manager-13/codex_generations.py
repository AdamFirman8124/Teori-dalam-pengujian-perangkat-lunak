

# Generated at 2022-06-12 22:27:07.499117
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager('localhost,')
    inventory.add_host(host='127.0.0.1',group='test')
    inventory.add_host(host='localhost',group='test')
    results = inventory._evaluate_patterns(['test'])
    assert set(results) == set(inventory._inventory.hosts.values())


# Generated at 2022-06-12 22:27:08.686042
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # check subset
    pass

# Generated at 2022-06-12 22:27:19.140329
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    class FakeInventoryPlugin(InventoryModule):
        def verify_file(self, path):
            return True

    class FakeInventoryPlugin2(InventoryModule):
        def verify_file(self, path):
            return True
        def parse(self, inventory, loader, path, cache):
            raise AnsibleError("should not be parsed")

    class FakeInventoryPlugin3(FakeInventoryPlugin):
        def parse(self, inventory, loader, path, cache):
            self.executed = True
            return True

    my_inventory_manager = InventoryManager(loader=Mock())
    my_inventory_manager._get_host_group_vars = MagicMock()
    my_inventory_manager.hosts = dict()
    my_inventory_manager.hosts['host1'] = MagicMock()

# Generated at 2022-06-12 22:27:26.571391
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    ansible = imp_load('ansible')
    inventory_manager = ansible.inventory.manager.InventoryManager()
    inventory_manager.parse_source({
        'host_list': [],
        'hostfile': [],
        'host_pattern': 'all',
        'inventory': [],
        'playbook_basedir': [],
        'plugin_dirs': [],
        'script': [],
        'subset': [],
        'vars_plugins': [],
        'yaml': [],
        'yml': []
    })


# Generated at 2022-06-12 22:27:29.481510
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    sources = ['localhost,']
    inventory = InventoryManager(sources)
    result = inventory.parse_sources()
    assert 'localhost' in result, "parse_sources failed to parse 'localhost,', got %s" % result


# Generated at 2022-06-12 22:27:40.745350
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    group = 'test_group'
    name = 'test_host'
    pattern = [group]
    subset_pattern = [group, name]
    # Create a new InventoryManager (actually _InventoryManager)
    im = InventoryManager(loader=None)
    # Add some results to caches
    im._hosts_patterns_cache = {pattern[0]: [name]}
    im._pattern_cache = {pattern[0]: [name]}
    # Run subset method on a InventoryManager object
    im.subset(subset_pattern[0])
    # Here we check that subset behaves as expected
    assert im._subset == subset_pattern
    assert im._hosts_patterns_cache == {pattern[0]: [name]}
    assert im._pattern_cache == {pattern[0]: [name]}

# Generated at 2022-06-12 22:27:45.677138
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    '''
    This test will assert to the following:
    1. subset accepts a string argument.
    2. subset accepts a list argument.
    3. subset accepts None argument.
    '''
    inv_mgr = InventoryManager()
    assert isinstance(inv_mgr.subset('all'), None)
    assert isinstance(inv_mgr.subset(list('all')), None)
    assert isinstance(inv_mgr.subset(None), None)

# Generated at 2022-06-12 22:27:52.587490
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    '''
    InventoryManager.list_hosts(pattern='all')
    '''
    # FIXME: Enable this test by writing a proper mock object
    # inventory = None
    # pattern = 'all'
    # obj = InventoryManager(inventory)
    # obj.list_hosts(pattern='all')


# Generated at 2022-06-12 22:28:01.248227
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    """Test the InventoryManager class"""

    im = InventoryManager(loader=None, sources='test/ansible/inventory/test_inventory.py')
    assert len(im.get_hosts()) == 6

    # no patterns should give all hosts
    assert len(im.get_hosts()) == 6

    # pattern should filter hosts
    assert len(im.get_hosts('host1')) == 1
    assert len(im.get_hosts('host[01]')) == 2
    assert len(im.get_hosts('host[!01]')) == 4

    # subset should filter hosts
    im.subset('host1')
    assert len(im.get_hosts()) == 1

    # duplicate patterns and groups should not result in duplicate hostnames

# Generated at 2022-06-12 22:28:11.604669
# Unit test for method parse_source of class InventoryManager

# Generated at 2022-06-12 22:28:35.066131
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    parser = argparse.ArgumentParser(description='Inventory Manager unit tests')
    parser.add_argument('--inventory', type=str, default=None)

    # parse the args
    args = parser.parse_args()

    # setup and run the test
    fake_options = Options()
    fake_options.tags = []
    fake_options.skip_tags = []
    fake_options.inventory = args.inventory

    im = InventoryManager(
        loader=None,
        sources=fake_options.inventory)
    im.parse_sources(fake_options, 'host_list', cache=False)
    #import epdb; epdb.st()

    # when done, de-initialize the inventory
    im.clear_pattern_cache()
    im.remove_restriction()
    im.subset(None)



# Generated at 2022-06-12 22:28:38.934976
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    t = {
        'value': 'foo'
    }
    inventory = Mock()
    inventory.hosts_list.return_value = []
    self = InventoryManager(t, inventory)
    self.subset(12)



# Generated at 2022-06-12 22:28:51.177159
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inv = InventoryManager('localhost,')
    inv.clear_pattern_cache()
    assert inv.parse_source(b"localhost ansible_connection=local", u'host_list') == ['localhost']

    inv = InventoryManager('localhost,')
    inv.clear_pattern_cache()
    assert inv.parse_source(u"localhost ansible_connection=local", u'host_list') == ['localhost']

    inv = InventoryManager('localhost,')
    inv.clear_pattern_cache()
    assert inv.parse_source("localhost ansible_connection=local", u'host_list') == ['localhost']

    inv = InventoryManager('localhost,')
    inv.clear_pattern_cache()

# Generated at 2022-06-12 22:28:59.576989
# Unit test for function split_host_pattern
def test_split_host_pattern():

    assert split_host_pattern('a, b[1],c[2:3], d') == ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern('a:b:c:d') == ['a:b:c:d']
    assert split_host_pattern('x:y') == ['x:y']
    assert split_host_pattern('[::1]') == ['[::1]']
    assert split_host_pattern('[fe80::]') == ['[fe80::]']
    assert split_host_pattern('fe80::') == ['fe80::']
    assert split_host_pattern('[a:b:c:d]') == ['[a:b:c:d]']

# Generated at 2022-06-12 22:29:06.750724
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    from nose import SkipTest
    from nose.tools import assert_equals, assert_raises

    raise SkipTest("TODO")
    return

    raise AssertionError("TODO")
    return

    _inventory = 'tests/unit/ansible_inventory.py'
    _name = "foobar"

    object = InventoryManager(_inventory, _name)
    object.clear_pattern_cache()
    object.subset(None)
    object.load()

    assert_equals(expected, object.list_hosts(pattern="all"))


# Generated at 2022-06-12 22:29:18.237701
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    from ansible.parsing.dataloader import DataLoader

    # Create the loader and inventory manager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)

    # Add the inventory source
    inventory.parse_source(
        [
            '# comment line 1',
            'localhost ansible_connection=local',
            '# comment line 2',
            'web1',
            'web2',
            'web3',
            '[webservers]',
            'web[1:3]',
            '# comment line 3'
        ],
        'test_inventory',
        'test_playbook'
    )

    # Check the group and host count
    assert len(inventory.groups) == 1
    assert len(inventory.hosts) == 3

    # Get the hosts

# Generated at 2022-06-12 22:29:23.610609
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    im = InventoryManager(None)

    im.subset(None)
    assert im._subset == None

    im.subset("foo")
    assert im._subset == ["foo"]

    im.subset(["a", "b"])
    assert im._subset == ["a", "b"]

    im.subset(None)
    assert im._subset == None


# Generated at 2022-06-12 22:29:28.901618
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory = InventoryManager(Host, Group, loader=None)
    print(inventory.list_hosts())
    print(inventory.list_groups())
    print(inventory._pattern_cache)
    print(inventory._match_one_pattern('localhost'))
    print(inventory._split_subscript('localhost[1-3]'))
    print(inventory._enumerate_matches('localhost'))
    print(inventory._match_list(inventory._inventory.hosts, 'localhost'))
    print(inventory._match_list(inventory._inventory.groups, 'all'))



# Generated at 2022-06-12 22:29:37.236975
# Unit test for function split_host_pattern
def test_split_host_pattern():
    assert split_host_pattern("foo:bar:baz") == ["foo", "bar", "baz"]
    assert split_host_pattern("foo, bar, baz") == ["foo", "bar", "baz"]
    assert split_host_pattern("foo,[1],bar") == ["foo", "[1]", "bar"]
    assert split_host_pattern("foo,[1]:bar") == ["foo", "[1]", "bar"]
    assert split_host_pattern("foo,[1]:bar,baz") == ["foo", "[1]", "bar", "baz"]



# Generated at 2022-06-12 22:29:48.550165
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    inventory = InventoryManager(loader=None, sources=[""])
    inventory.hosts[u'localhost'] = Host(name=u'localhost')
    inventory.groups[u'all'] = Group(name=u'all')
    inventory.groups[u'all'].add_host(inventory.hosts[u'localhost'])
    inventory.groups[u'all']._children[u'localhost'] = inventory.hosts[u'localhost']
    inventory._inventory.groups[u'all'] = inventory.groups[u'all']

    im = InventoryManager(loader=None, sources="")
    im.inventory = inventory

    # hosts = im.get_hosts()
    # assert

# Generated at 2022-06-12 22:30:19.799299
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    class Inventory(object):
        def __init__(self, host_list, group_list):
            self.hosts = host_list
            self.groups = group_list
        
        def get_host(self, hostname):
            for host in self.hosts:
                if host.name == hostname:
                    return host

            return None
        
        def get_groups(self, groupname):
            for group in self.groups.values():
                if group.name == groupname:
                    return group

            return None

    class Group(object):
        def __init__(self, name, host_list):
            self.name = name

            self.hosts = host_list
            self.children = []

        def get_hosts(self):
            return self.hosts


# Generated at 2022-06-12 22:30:25.831928
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    # Return empty list when no hosts
    assert len(InventoryManager([], [], None).list_hosts()) == 0

    # Return only hosts that match pattern
    hosts = [
        'foohost',
        'barhost',
        'bazhost',
        'foogroup',
        'bargroup',
        'bazgroup',
        'foohost_host',
        'barhost_host',
        'bazhost_host',
        'foogroup_group',
        'bargroup_group',
        'bazgroup_group',
        'foohost y',
        'barhost x',
        'bazhost z',
        'foogroup a',
        'bargroup b',
        'bazgroup c',
    ]

    # Return all hosts when pattern is 'all'

# Generated at 2022-06-12 22:30:38.227317
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    all_hosts = [Host(name='host0'), Host(name='host1'), Host(name='host2')]
    all_groups = [Group(name='group0'), Group(name='group1'), Group(name='group2')]
    all_groups.extend([g.copy() for g in all_groups])
    all_groups[0].name = 'group00'
    all_groups[1].name = 'group10'
    all_groups[2].name = 'group20'
    all_groups[3].name = 'group01'
    all_groups[4].name = 'group11'
   

# Generated at 2022-06-12 22:30:39.028544
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    pass

# Generated at 2022-06-12 22:30:39.941555
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    assert True

# Generated at 2022-06-12 22:30:50.650484
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    test_inventory = """
[hosts]
host1
host2
host3
[hosts:vars]
foo = bar
    """
    # test_InventoryManager_subset: with pattern
    inv = InventoryManager(loader=DataLoader())
    inv.add_host(host='host1', group='hosts')
    inv.add_host(host='host2', group='hosts')
    inv.add_host(host='host3', group='hosts')
    inv.set_variable(host='host1', varname='foo', value='bar')
    inv.set_variable(host='host2', varname='foo', value='bar')
    inv.set_variable(host='host3', varname='foo', value='bar')

# Generated at 2022-06-12 22:30:54.548466
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    args = {}
    args['inventory_manager'] = InventoryManager(None, None)
    args['subset_pattern'] = None
    result = InventoryManager.subset(**args)
    assert result is None
test_InventoryManager_subset()

# Generated at 2022-06-12 22:31:02.561057
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["/tmp/test"], variable_manager=variable_manager, vault_password=None)
    inventory.clear_pattern_cache()
    
    # Test with all arguments
    result = inventory.list_hosts(pattern="all")
    assert isinstance(result, list)
    
    # Test with default argument value
    result = inventory.list_hosts()
    assert isinstance(result, list)
    

# Generated at 2022-06-12 22:31:04.592863
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory = InventoryManager(loader=DataLoader())
    inventory.parse_inventory(host_list='localhost,')

    assert inventory.list_hosts() == ['localhost']


# Generated at 2022-06-12 22:31:06.023854
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inv_mgr = InventoryManager()
    assert inv_mgr.list_hosts() == []



# Generated at 2022-06-12 22:31:34.391590
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    from ansible.parsing.dataloader import DataLoader

    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources='')
    inventory._subset = None

    inventory.subset(None)
    assert inventory._subset == None

    inventory.subset('all')
    assert inventory._subset == ['all']

    inventory.subset('foo')
    assert inventory._subset == ['foo']

    inventory.subset('foo:bar')
    assert inventory._subset == ['foo:bar']



# Generated at 2022-06-12 22:31:36.495878
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
  host_list_result = inventory.list_hosts()
  print("\nHost result: ")
  for host in host_list_result:
    print("    " + host)


# Generated at 2022-06-12 22:31:46.375398
# Unit test for function split_host_pattern
def test_split_host_pattern():
    assert split_host_pattern('a,b[1],c[2:3],d') == ['a', 'b[1]', 'c[2:3]', 'd']
    assert split_host_pattern('::1,[2a00::f]:567,[::1]:,[udp::]') == ['::1', '[2a00::f]:567', '[::1]:', '[udp::]']
    assert split_host_pattern(['a,b[1],c[2:3],d', '::1,[2a00::f]:567,[::1]:,[udp::]']) == \
        ['a', 'b[1]', 'c[2:3]', 'd', '::1', '[2a00::f]:567', '[::1]:', '[udp::]']
    assert split_

# Generated at 2022-06-12 22:31:54.308791
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager()
    inventory_manager.subset("all")
    assert inventory_manager._subset == [u'all']
    inventory_manager.subset(["localhost", "127.0.0.1"])
    assert inventory_manager._subset == [u'localhost', u'127.0.0.1']
    inventory_manager.subset("host1,host2")
    assert inventory_manager._subset == [u'host1', u'host2']


# Generated at 2022-06-12 22:32:01.745505
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory = InventoryManager(loader=None, sources='localhost,')
    assert inventory.subset(subset_pattern=None) is None

    inventory = InventoryManager(loader=None, sources='localhost,')
    assert inventory.subset(subset_pattern='all') == ['all']

    inventory = InventoryManager(loader=None, sources='localhost,')
    assert inventory.subset(subset_pattern='foo') == ['foo']

    inventory = InventoryManager(loader=None, sources='localhost,')
    assert inventory.subset(subset_pattern='all:&foo') == ['all', '&foo']

    inventory = InventoryManager(loader=None, sources='localhost,')
    assert inventory.subset(subset_pattern='all:!foo') == ['all', '!foo']


# Generated at 2022-06-12 22:32:13.013767
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    sources = 'localhost,'
    inventory = InventoryManager(sources=sources)
    assert inventory.sources == sources
    assert len(inventory.sources_list) == 2
    assert inventory._get_host_group('localhost') == 'all'
    assert inventory.groups['all']

    sources = 'localhost:,'
    inventory = InventoryManager(sources=sources)
    assert inventory.sources == sources
    assert len(inventory.sources_list) == 2
    assert inventory._get_host_group('localhost') == 'all'
    assert inventory.groups['all']

    sources = 'localhost,,,'
    inventory = InventoryManager(sources=sources)
    assert inventory.sources == sources
    assert len(inventory.sources_list) == 4
    assert inventory._get_host_group('localhost') == 'all'

# Generated at 2022-06-12 22:32:14.671244
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    pass



# Generated at 2022-06-12 22:32:23.159565
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory_manager = InventoryManager()
    inventory_path = "/var/lib/awx/projects/my_project/.ansible"
    inventory_name = "my_inventory"
    host_pattern = "*"
    loader = "source"
    source = "localhost"
    enabled = True
    became_method = None
    became_username = None
    become_password = None
    become_password_script = None
    become_private_key_file = None
    vault_files = []
    vault_password = None
    vault_password_script = None
    forks = 100
    timeout = 10
    remote_user = "my_user"
    ssh_private_key_file = None
    tags = []
    skip_tags = []
    ansible_ssh_host = "10.0.0.9"
    ans

# Generated at 2022-06-12 22:32:34.298623
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    import collections
    import json
    import os

    Host = collections.namedtuple('Host', ['name'])
    Group = collections.namedtuple('Group', ['name', 'hosts'])

    _inventory_json_data = {
        "all": {
        "hosts": [
        "all-host"],
        "children": ["group1", "group2"]
        },
        "group1": {
        "hosts": [
        "group1-host"],
        "children": []
        },
        "group2": {
        "hosts": [
        "group2-host"],
        "children": ["group3"]
        },
        "group3": {
        "hosts": [
        "group3-host"],
        "children": []
        }
    }


# Generated at 2022-06-12 22:32:34.929574
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    pass

# Generated at 2022-06-12 22:32:56.756270
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    manager = InventoryManager(loader=None)
    manager.parse_source("test")


# Generated at 2022-06-12 22:33:05.893318
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    # Test method parse_sources of class InventoryManager
    # Sources is a string (type) or list (type)
    #    Sources can be a filename, directory, or URL
    #    Sources can be a YAML, JSON, or INI format file
    #    If a directory or URL is provided, each filename in the list is assumed
    #    to end with either '.yaml', '.yml', '.json' or '.ini'.
    #    The 'all' group will be created if it does not exist
    # Return: A dictionary representation of the inventory (type)
    # Raise:
    #    AnsibleOptionsError for invalid -i directory/file,
    #    AnsibleError for all other errors
    #    IOError for file access problems

    return

# Generated at 2022-06-12 22:33:12.873251
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # ok
    i1 = InventoryManager(None, loader=DictDataLoader({}))
    i1.subset('foo')

    # failure
    try:
        i1.subset('@foo')
        raise AssertionError("Failed to raise an exception")
    except AnsibleError:
        pass



# Generated at 2022-06-12 22:33:18.976058
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    MOCK_INVENTORY = mock.Mock()
    inventory_manager = InventoryManager(MOCK_INVENTORY)
    inventory_manager.subset(["host1","host2"])
    assert inventory_manager._subset == ["host1", "host2"]
    inventory_manager.clear_pattern_cache()
    assert inventory_manager._pattern_cache == {}

if __name__ == '__main__':
    pytest.main(['-q',__file__])

# Generated at 2022-06-12 22:33:30.800841
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    m = InventoryManager(loader=DictDataLoader({}))
    
    # {u'127.0.0.1': <ansible.inventory.host.Host object at 0x11c19a9d0>}
    ins = m.get_hosts()
    assert ins[0].name == u'127.0.0.1'
    assert ins[0].get_vars() == {}
        
    # {u'all': <ansible.inventory.group.Group object at 0x10d981c50>, u'ungrouped': <ansible.inventory.group.Group object at 0x10d981dd0>}
    ins = m.list_groups()
    assert len(ins) == 2
    assert ins[0] == u'all'
    assert ins[1] == u'ungrouped'

# Generated at 2022-06-12 22:33:31.724175
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():

    assert False, "No tests for this function yet"

# Generated at 2022-06-12 22:33:41.464211
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()

    # TODO: Improve unit test coverage for method subset
    im = InventoryManager(loader, variable_manager=VariableManager(loader=loader), host_list=[])
    im.subset("all")

    im.subset("foo")
    im.subset("foo[2:5]")
    im.subset("foo:bar[2:5]")
    im.subset("foo[2]")
    im.subset("foo,bar")
    im.subset("foo:bar")
    im.subset("&.foo")
    im.subset("&.foo,&.bar")
    im.subset("&.foo[2]")
    im.sub

# Generated at 2022-06-12 22:33:44.204514
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    hosts = 'localhost'
    self = InventoryManager()
    self.parse_source(hosts)
    assert hosts == 'localhost'


# Generated at 2022-06-12 22:33:47.560845
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory = InventoryManager(loader=Nope(), sources='localhost,')
    inventory.subset(u'nonexistent_host')
    assert inventory._subset == {u'nonexistent_host'}, 'subset() should store the argument in self._subset.'


# Generated at 2022-06-12 22:33:59.171200
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager("/etc/ansible")
    assert inventory_manager.subset("foo") == None
    assert inventory_manager._subset == ["foo"]
    inventory_manager.subset("bar")
    assert inventory_manager._subset == ["foo", "bar"]
    inventory_manager.subset("bar baz")
    assert inventory_manager._subset == ["foo", "bar", "baz"]
    inventory_manager.subset("@/path/to/file")
    assert inventory_manager._subset == ["foo", "bar", "baz", "@/path/to/file"]
    inventory_manager.clear_pattern_cache()
    assert inventory_manager._pattern_cache == {}
test_InventoryManager_subset()

# Mocked InventoryVars object

# Generated at 2022-06-12 22:35:24.788631
# Unit test for function split_host_pattern
def test_split_host_pattern():
    # These should all be handled as a single pattern.
    assert split_host_pattern('foo') == ['foo']
    assert split_host_pattern('[foo]') == ['[foo]']
    assert split_host_pattern('foo:bar') == ['foo:bar']
    assert split_host_pattern('foo:bar,baz') == ['foo:bar,baz']

    # These should be split into two patterns.
    assert split_host_pattern('foo,bar') == ['foo', 'bar']
    assert split_host_pattern('[foo],[bar]') == ['[foo]', '[bar]']
    assert split_host_pattern('foo:bar baz') == ['foo:bar', 'baz']
    assert split_host_pattern('foo:bar:baz') == ['foo:bar:baz']

    #

# Generated at 2022-06-12 22:35:30.944136
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    """
    parse_source tests
    """

    from ansible.cli.inventory import AnsibleInventoryCLI
    from ansible.parsing.dataloader import DataLoader

    sources = [
        "localhost,",
        "localhost,",
        ",".join([
            "[test]",
            "localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3",
        ]),
        ",".join([
            "[test]",
            "localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3",
        ]),
    ]

# Generated at 2022-06-12 22:35:40.572147
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    inv_path = 'test/inventory/test_inventory.yml'
    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=[inv_path])
    variable_manager = VariableManager(loader=loader, inventory=inv_obj)
    inv_mgr = InventoryManager(loader=loader, sources=[inv_path], variable_manager=variable_manager)
    inv_mgr.parse_sources()
    assert inv_mgr.get_hosts('all') == [inv_obj.get_host('127.0.0.1')]

# Generated at 2022-06-12 22:35:50.213101
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    # set up
    inventory_manager = InventoryManager(inventory=None)
    inventory_manager._subset = False
    inventory_manager._restriction = False
    inventory_manager._hosts_patterns_cache = {}
    inventory_manager._pattern_cache = {}

    # tests:
    # assume that inventory_manager._subset has value False
    inventory_manager.get_hosts(pattern="all", ignore_limits=False, ignore_restrictions=False, order=None)
    # assume that inventory_manager._restriction has value False
    inventory_manager.get_hosts(pattern="all", ignore_limits=False, ignore_restrictions=False, order=None)

    # assume that inventory_manager._restriction has value "myhost"
    inventory_manager._restriction = "myhost"
    inventory_manager.get

# Generated at 2022-06-12 22:35:53.735109
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
	inventory = InventoryManager(loader=None, variable_manager=None, host_list='localhost')
	result = inventory.list_hosts('localhost')
	assert result == [u'localhost'], result
	result = inventory.list_hosts('127.0.0.1')
	assert result == [], result

# Generated at 2022-06-12 22:36:03.557242
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory = InventoryManager(loader=None, sources='')
    restrict_to_hosts = None
    subset_pattern = None
    im = InventoryModule(inventory=inventory, restrict_to_hosts=restrict_to_hosts,
        subset_pattern=subset_pattern)

    data = {
        "all": [
            "localhost",
            "www.sina.com.cn"
        ],
        "localhost": "localhost",
        "www.sina.com.cn": "www.sina.com.cn"
    }
    for k, v in data.items():
        im.clear_pattern_cache()
        assert im.get_hosts(pattern=k) == v
        assert im.get_hosts(pattern=v) == v

