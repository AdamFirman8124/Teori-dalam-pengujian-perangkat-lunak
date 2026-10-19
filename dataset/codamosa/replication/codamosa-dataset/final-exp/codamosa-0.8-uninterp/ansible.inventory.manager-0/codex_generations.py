

# Generated at 2022-06-12 22:27:04.541650
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager(inventory=MagicMock())
    with open('./tests/inventory/tmp_limit_file', 'w') as f:
        f.write('foo1\nbar1\n')
    inventory_manager.subset('@./tests/inventory/tmp_limit_file')
    os.remove('./tests/inventory/tmp_limit_file')
    assert inventory_manager._subset == ['foo1', 'bar1']

# Generated at 2022-06-12 22:27:11.047315
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # FIXME: this test is broken
    raise SkipTest
    name = 'subset'
    inv_manager = InventoryManager(loader=None, sources=[])
    subset_pattern = None
    expected = None
    result = inv_manager.subset(subset_pattern)
    assert_true(expected is result, "Got %r" % (result,))


# Generated at 2022-06-12 22:27:20.378448
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():

    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.script import InventoryScript
    from ansible.parsing.dataloader import DataLoader

    class TestInventoryScript(InventoryScript):

        def __init__(self, loader, filename):
            super(TestInventoryScript, self).__init__(loader, filename)
            self.cache = None

        def parse(self, inventory, loader, cache=True):
            self.cache = cache
            self.filename = self.filename
            self.loader = loader
            inventory.add_group('test_group')
            inventory.add_host(Host(name='test_host'))

        def is_cacheable(self):
            return True


# Generated at 2022-06-12 22:27:26.200718
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # setup the mocks
    mock_subset_patterns = split_host_pattern.return_value = ['subset_pattern']
    mock_results = ['result']
    
    # create inventory manager
    inventory_manager = InventoryManager()
    # call method
    inventory_manager.subset(subset_pattern=mock_subset_patterns)
    
    # assert results
    assert inventory_manager._subset == mock_results

# Generated at 2022-06-12 22:27:27.156295
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    pass


# Generated at 2022-06-12 22:27:35.631575
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    # Test set up
    im = InventoryManager()
    im.add_group('group_name')
    im.add_host('', 'host_name')
    im.add_child('group_name', 'host_name')
    im.add_host('group_name', 'host_name_2')
    im.add_host('', 'host_name_1')

    # Test
    assert im.get_hosts('host_name') == [Host(name='host_name')]
    assert im.get_hosts(['host_name', 'host_name_1']) == [
        Host(name='host_name'), Host(name='host_name_1')
    ]

# Generated at 2022-06-12 22:27:37.282234
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    # Test the parameters using InventoryManager method parse_sources
    # This method is created for the sole purpose of unit testing
    # returns the populated Inventory object
    pass


# Generated at 2022-06-12 22:27:45.747170
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory_manager = InventoryManager()
    # get_hosts()
    host_results = inventory_manager.get_hosts()
    assert host_results is not None
    assert len(host_results) == 0
    assert isinstance(host_results, list)
    # get_hosts(pattern="all")
    host_results = inventory_manager.get_hosts(pattern="all")
    assert host_results is not None
    assert len(host_results) == 0
    assert isinstance(host_results, list)
    # get_hosts(pattern=None)
    host_results = inventory_manager.get_hosts(pattern=None)
    assert host_results is not None
    assert len(host_results) == 0
    assert isinstance(host_results, list)
    # get_hosts(ignore_

# Generated at 2022-06-12 22:27:57.800803
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    # Create a mock inventory for testing purposes
    class MockInventory():
        def __init__(self):
            self.hosts = {
                'host_1': "host_1_data",
                'host_2': "host_2_data",
                'host_3': "host_3_data"
            }
        def get_host(self, host_name):
            if host_name in self.hosts:
                return self.hosts[host_name]
            else:
                return None

    mock_inventory = MockInventory()
    # Create mock list_hosts method
    def list_hosts(pattern):
        return [
            'host_1',
            'host_2',
            'host_3'
        ]
    # Create mock get_host method

# Generated at 2022-06-12 22:28:09.903720
# Unit test for function order_patterns
def test_order_patterns():
    assert order_patterns(['a', 'b', '!c', '&d']) == ['a', 'b', '&d', '!c']
    assert order_patterns(['&a', 'b', '!c', 'd']) == ['b', 'd', '&a', '!c']
    assert order_patterns(['!a', 'b', '&c', 'd']) == ['b', 'd', '&c', '!a']
    assert order_patterns(['!a', '&b', 'c', 'd']) == ['c', 'd', '&b', '!a']
    assert order_patterns(['!a', '&b', 'c', 'd']) == ['c', 'd', '&b', '!a']

# Generated at 2022-06-12 22:28:55.795759
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager("test")
    inventory_manager.subset("~")
    assert(inventory_manager._subset == ['~'])

# Generated at 2022-06-12 22:29:04.897374
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    digits = '0123456789'
    hostvars = dict()
    # hostvars maps from host name to dict of host variables
    hostvars['foo'] = dict()
    hostvars['foo']['private_key'] = 'private_key'
    hostvars['foo']['ansible_host'] = 'ansible_host'
    hostvars['foo']['ansible_port'] = 'ansible_port'
    hostvars['foo']['ansible_user'] = 'ansible_user'
    hostvars['foo']['ansible_ssh_pass'] = 'ansible_ssh_pass'
    hostvars['foo']['ansible_ssh_private_key_file'] = 'ansible_ssh_private_key_file'

# Generated at 2022-06-12 22:29:16.865342
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    print(common.init())

    # pass
    inventory_manager = common.init_inventory()
    print(inventory_manager.get_hosts())

    # pass
    print(inventory_manager.get_hosts('all'))

    # pass
    print(inventory_manager.get_hosts(['all']))

    # pass
    print(inventory_manager.get_hosts('127.0.0.1'))

    # pass
    print(inventory_manager.get_hosts(['127.0.0.1']))

    # pass
    print(inventory_manager.get_hosts('*'))

    # pass
    print(inventory_manager.get_hosts(['*']))

    # pass
    print(inventory_manager.get_hosts('*[2]'))

    # pass
   

# Generated at 2022-06-12 22:29:19.043148
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    mgr = InventoryManager('localhost')
    hosts = mgr.list_hosts()
    assert hosts == ['localhost']

# Generated at 2022-06-12 22:29:27.987449
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory_manager = InventoryManager(
        inventory=Inventory(
            host_list=[
                Host(name='test1'),
                Host(name='test2'),
                Host(name='test3'),
                ]
            )
        )
    assert inventory_manager.list_hosts() == ['test1', 'test2', 'test3']
    assert inventory_manager.list_hosts('test1') == ['test1']
    assert inventory_manager.list_hosts('tes') == []
    assert inventory_manager.list_hosts(['test1', 'test2']) == ['test1', 'test2']
    assert inventory_manager.list_hosts('all') == ['test1', 'test2', 'test3']
    assert inventory_manager.list_hosts('*') == []
    assert inventory_manager.list

# Generated at 2022-06-12 22:29:38.966080
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    import ansible.inventory
    host = ansible.inventory.Host('127.0.0.2')
    host.vars = {'foo': 'bar'}
    inventory = ansible.inventory.Inventory()
    inventory.add_host(host)
    inventory.add_group('group1')
    inventory.add_child('group1', host)
    inventory.add_child('group2', host)
    inventory.add_child('all', host)

    inventory_manager = InventoryManager(inventory=inventory)
    inventory_manager._subset = None
    assert inventory_manager._subset == None

    inventory_manager._subset = 'test'
    assert inventory_manager._subset == 'test'

    inventory_manager._subset = ['test1','test2','test3']

# Generated at 2022-06-12 22:29:49.750977
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    inventory_manager = InventoryManager(["localhost"], None)
    inventory_manager.clear_pattern_cache()
    assert inventory_manager.list_hosts(pattern="apache.example.org") == ['apache.example.org']
    assert inventory_manager.list_hosts(pattern="all") == ['apache.example.org']
    inventory_manager.clear_pattern_cache()
    assert inventory_manager.list_hosts(pattern=["localhost", "local*"]) == ['apache.example.org']
    inventory_manager.clear_pattern_cache()
    assert inventory_manager.list_hosts(pattern="webservers") == ['apache.example.org']
    inventory_manager.clear_pattern_cache()
    assert inventory_manager.list_hosts(pattern="foo") == []
    inventory_manager.clear_pattern_cache

# Generated at 2022-06-12 22:29:53.195245
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory_manager = InventoryManager(loader=None, sources='localhost')
    hosts = inventory_manager.get_hosts(pattern='all')
    assert hosts[0].get_name() == 'localhost'



# Generated at 2022-06-12 22:30:01.770173
# Unit test for method list_hosts of class InventoryManager
def test_InventoryManager_list_hosts():
    script = inspect.getfile(inspect.currentframe())
    scriptpath = os.path.dirname(script)
    yaml_inventory = os.path.join(scriptpath, '../inventory/test_inventory.yaml')
    yaml_inventory = os.path.normpath(yaml_inventory)
    pattern = 'webservers'

    inventory = InventoryManager(loader=DataLoader(), sources=(yaml_inventory,))
    host_list = inventory.list_hosts(pattern)
    assert len(host_list) == 3



# Generated at 2022-06-12 22:30:09.853886
# Unit test for function split_host_pattern
def test_split_host_pattern():
    assert (split_host_pattern([u'a,b[1], c[2:3] , d']) ==
            [u'a', u'b[1]', u'c[2:3]', u'd'])
    assert (split_host_pattern([u'a,b[1], c[2:3] , d:1234']) ==
            [u'a', u'b[1]', u'c[2:3]', u'd:1234'])
    assert (split_host_pattern([u'a, b[1], c[2:3] , d:1234']) ==
            [u'a', u'b[1]', u'c[2:3]', u'd:1234'])



# Generated at 2022-06-12 22:30:47.805509
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    sources = ['one', 'two', 'three']
    cm = InventoryManager(sources)
    assert cm is not None
    

# Generated at 2022-06-12 22:30:52.633501
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inventory_manager = InventoryManager()

    with patch.object(display, 'deprecated') as mock_display_deprecated:
        inventory_manager.parse_source('host_list', 'host1')
        assert mock_display_deprecated.call_count == 1
        mock_display_deprecated.assert_called_with('DEPRECATION: host_list is as string.  You should now use host_list as a list.', version='2.14')


# Generated at 2022-06-12 22:31:02.090518
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():

    inventory_manager = InventoryManager()
    assert inventory_manager.parse_source("foo") == {u'{0}/foo'.format(DEFAULT_HOST_LIST): u'foo'}
    assert inventory_manager.parse_source("foo:bar") == {u'{0}/foo'.format(DEFAULT_HOST_LIST): u'bar'}
    assert inventory_manager.parse_source("foo:bar:baz") == {u'{0}/foo'.format(DEFAULT_HOST_LIST): u'bar:baz'}
    assert inventory_manager.parse_source("plugin") == {u'{0}/plugin'.format(DEFAULT_HOST_LIST): None}

# Generated at 2022-06-12 22:31:08.910721
# Unit test for method parse_sources of class InventoryManager

# Generated at 2022-06-12 22:31:19.133888
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    file_name = "/home/lxm/devops/ansible-workspace/ansible_source_code/lib/ansible/inventory/__init__.py"
    manager = InventoryManager(loader=None, sources=[file_name])
    manager.subset("*")
    # print("source: ", manager._sources)
    # print("subset: ", manager._subset)
    # print("pattern_cache: ", manager._pattern_cache)
    # print("host_pattern_cache: ", manager._hosts_patterns_cache)
    # print("host: ", manager._inventory.hosts)
    # print("group: ", manager._inventory.groups)
    # print("host_pattern: ", manager._match_one_pattern("db*"))

# Generated at 2022-06-12 22:31:23.148955
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # 1. Create mock params to pass to method
    pattern = None
    # 2. Get method and hold it in variable
    method = InventoryManager.subset
    # 3. Call the method with parameters
    results = method(pattern)


# Generated at 2022-06-12 22:31:26.601741
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    '''InventoryManager.parse_sources()'''
    myinv = InventoryManager('localhost,')
    myinv.parse_sources()
    assert(myinv._inventory._hosts['localhost'].name == 'localhost')


# Generated at 2022-06-12 22:31:27.498339
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
	pass

# Generated at 2022-06-12 22:31:37.841689
# Unit test for method subset of class InventoryManager

# Generated at 2022-06-12 22:31:40.680996
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory = InventoryManager()
    hosts = inventory.get_hosts()
    assert hosts == []

# Generated at 2022-06-12 22:32:12.553467
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    import shutil
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import get_dist_file

    def assert_type_and_len(res, value_type, value_len):
        assert isinstance(res, list)
        assert len(res) == value_len
        for v in res:
            assert isinstance(v, value_type)

    dataloader = DataLoader()
    basedir = get_dist_file(os.path.join('playbooks', 'inventory'))
    basedir = os.path.join(basedir, 'host_vars')
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    os.chmod(basedir, 0o777)

    # empty host_list
   

# Generated at 2022-06-12 22:32:21.949032
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    import doctest
    import os
    import tempfile
    import unittest

    from ansible.parsing.dataloader import DataLoader

    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.ini import InventoryParser

    test_dir = os.path.join(os.path.dirname(__file__), 'test_files')

    loader = DataLoader()
    test_inv = InventoryManager(loader=loader, sources=[os.path.join(test_dir, 'hosts_test')])
    test_host = Host(name='justatest')
    test_host.vars['test_var'] = 'test_value'
    test_group1 = Group(name='test_group1')


# Generated at 2022-06-12 22:32:27.173224
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # Test with buffer io.StringIO
    params = {
        'hosts': io.StringIO('host1\nhost2'),
        'cache': False,
    }
    assert InventoryManager._parse_source(params) == {'hosts': ['host1', 'host2']}


# Generated at 2022-06-12 22:32:32.568903
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    mgr = InventoryManager(loader=None, sources=None)

    sources = []
    ansible.utils.plugin_docs.load_docs(sources, ignore_errors=True)
    inv_data = ansible.utils.plugin_docs.get_inventory_group_info(sources, ignore_errors=True)
    host_data = ansible.utils.plugin_docs.get_inventory_host_info(sources, ignore_errors=True)
    inv_data.update(host_data)
    inv_data = {'localhost': inv_data}
    inv = Inventory(loader=None, variable_manager=None, host_list=None)
    inv.parse_inventory(inv_data)
    mgr._inventory = inv


# Generated at 2022-06-12 22:32:43.259712
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    log_capture_string = six.StringIO()
    logging_manager.configure_logger(log_capture_string, C.DEFAULT_LOG_PATH)
    display_factory = Display(verbosity=3)
    display_factory.verbosity = 4
    display_factory.info("InventoryManager - test_subset_pattern")
    inventory_manager = InventoryManager(inventory=[])
    # TODO - add more test cases
    # case 1 -
    inventory = None
    subset_pattern = "linux2"
    inventory_manager.subset(subset_pattern)
    assert subset_pattern in inventory_manager._subset

    # case 2 -
    inventory = None
    subset_pattern = ""
    inventory_manager.subset(subset_pattern)
    assert subset_pattern in inventory_manager._

# Generated at 2022-06-12 22:32:48.413728
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    im = InventoryManager(loader, sources=C.DEFAULT_HOST_LIST)
    im.subset("srv[0:2]")
    assert im._subset == ['srv[0:2]']
    im.clear_pattern_cache()

# Generated at 2022-06-12 22:32:59.589591
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_json = open("./test/integration/ansible.inventory").read()
    inventory_dict = json.loads(inventory_json, strict=False)
    inventory = Inventory(host_list=(),
                          loader=DataLoader(),
                          variable_manager=VariableManager(),
                          host_pattern="test")
    inventory.host_variable_cache = variable_cache.VariableCache(inventory)
    inventory.group_variable_cache = variable_cache.VariableCache(inventory)
    inventory.parse_inventory(inventory_dict)
    inventory.reconcile_inventory()

    inv_manager = InventoryManager(loader=DataLoader(), sources=['test/integration/ansible.inventory'])
    inv_manager.inventory = inventory
    inv_manager.parse_sources()

# Generated at 2022-06-12 22:33:02.980256
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
  '''
  Test for the InventoryManager subset method
  '''
  imanager = InventoryManager()
  imanager.subset(None)
  assert imanager._subset == None
  return 0


# Generated at 2022-06-12 22:33:03.950425
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # TODO
    pass


# Generated at 2022-06-12 22:33:07.338349
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    inventory = InventoryManager(inventory=[Host("example.com")])
    result = inventory.get_hosts("example.com")
    assert result == [Host("example.com")]



# Generated at 2022-06-12 22:33:36.473897
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    assert True

# Generated at 2022-06-12 22:33:44.216215
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    # Test a normal inventory:
    inv = InventoryManager('InventoryManagerUnitTest')
    inv_list = [
        'host1 ansible_host=host1.example.com',
        'host2 ansible_host=host2.example.com',
        '[somegroup]',
        'host2',
        'host3 ansible_host=host3.example.com',
        '[othergroup:children]',
        'somegroup',
        '',
        '[somestaticgroup]',
        'localhost',
    ]
    inv_file = os.path.join(tempfile.mkdtemp(), 'inventory')
    with open(inv_file, 'w') as f:
        f.write('\n'.join(inv_list))
    assert inv.parse_source(inv_file)

    # Test empty inventory

# Generated at 2022-06-12 22:33:55.738854
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    # Check InventoryManager.parse_source without arguments
    i = InventoryManager()
    assert i.parse_sources("") == [], "InventoryManager.parse_sources('') returned unexpected result: '%s'" % i.parse_sources("")
    # Check InventoryManager.parse_source with file plugin
    i = InventoryManager()
    assert i.parse_sources("file:") == [{"hosts": [], "vars": {}}], "InventoryManager.parse_sources('file:') returned unexpected result: '%s'" % i.parse_sources("file:")
    # Check InventoryManager.parse_source with script plugin
    i = InventoryManager()

# Generated at 2022-06-12 22:34:02.560404
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'ansible_sources',
        'inventory_manager'
    )
    with patch('ansible.inventory.Inventory') as mock_inventory:
        inventory_mgr = InventoryManager(mock_inventory, os.path.join(path, 'inventory_manager.yml'))
        result = inventory_mgr.parse_sources()
        assert result == [('localhost', 'all'), ('host-a', 'hosts'), ('host-b', 'hosts')]



# Generated at 2022-06-12 22:34:06.341682
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    InventoryManager = ansible.inventory.manager.InventoryManager()

    # No subset
    InventoryManager.subset(None)
    assert InventoryManager._subset is None

    InventoryManager.subset('a')
    assert InventoryManager._subset == ['a']


# Generated at 2022-06-12 22:34:08.756701
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inv_manager = InventoryManager('ansible-inventory --list')
    subset_pattern = 'foo'
    inv_manager.subset(subset_pattern)


# Generated at 2022-06-12 22:34:11.039673
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    self = InventoryManager('/tmp/ansible-test')
    pattern = 'all'
    ignore_limits = False
    ignore_restrictions = False
    order = None
    result = self.get_hosts(pattern, ignore_limits, ignore_restrictions, order)

# Generated at 2022-06-12 22:34:13.488741
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory_manager = InventoryManager()
    inventory_manager.subset('all')


# Generated at 2022-06-12 22:34:16.508814
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    my_inv_instance = InventoryManager()
    my_inv_instance.subset(subset_pattern=':'.join(['127.0.0.1', 'localhost']))
    assert my_inv_instance._subset == [':'.join(['127.0.0.1', 'localhost'])]
    assert my_inv_instance._restriction is None



# Generated at 2022-06-12 22:34:21.533783
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    # positive tests
    inventory = InventoryManager()
    inventory.set_inventory(Inventory("localhost,"))
    display.display("\ntest 1: all")
    hosts = inventory.get_hosts("all")
    assert hosts == [host]
    display.display("\ntest 2: all,restrict to localhost")
    hosts = inventory.get_hosts("all")
    assert hosts == [host]
    inventory.restrict_to_hosts([host])
    assert hosts == [host]
    display.display("\ntest 3: localhost")
    inventory.clear_pattern_cache()
    hosts = inventory.get_hosts("localhost")
    assert hosts == [host]
    display.display("\ntest 4: localhost,restrict to localhost")

# Generated at 2022-06-12 22:34:48.649373
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
  result = InventoryManager.parse_source("foo", "bar", "baz")
  assert result[0] == "foo"
  assert result[1] == "bar"
  assert result[2] == "baz"


# Generated at 2022-06-12 22:34:55.067532
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    class MockInventory(object):
        def __init__(self, hosts=None, groups=None, source_vars=None):
            self._hosts = {}
            self._groups = {}
            if hosts:
                for k, v in hosts.items():
                    self._hosts[k] = Host(k, source_vars=v)
            if groups:
                for k, v in groups.items():
                    self._groups[k] = Group(name=k)
                    if 'hosts' in v:
                        for x in v['hosts']:
                            self._groups[k].add_host(self.get_host(x))
            self.vars = {'inventory_dir': '.'}

        def get_host(self, name):
            return self._hosts[name]


# Generated at 2022-06-12 22:34:57.444064
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    pass


# Generated at 2022-06-12 22:35:04.592652
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    #subset
    #subset_pattern
    inv = InventoryManager(['localhost','somehost','someotherhost','testhost','test123'])
    assert inv.subset('all') == inv.subset_pattern == None
    inv.subset('some')
    assert inv.subset_pattern == ['some']
    assert inv.subset('someother') == inv.subset_pattern == ['someother']
    assert inv.subset(['test*','other*']) == inv.subset_pattern == ['test*','other*']
    assert inv.subset(None) == inv.subset_pattern == None

# Generated at 2022-06-12 22:35:14.070394
# Unit test for method parse_source of class InventoryManager
def test_InventoryManager_parse_source():
    inv_info = {}
    # Empty inventory
    inventory_manager = InventoryManager(Inventory(Loader()), inv_info)
    inv_info = inventory_manager.parse_sources('localhost,')
    assert inv_info == {'localhost,': {}}
    inventory_manager = InventoryManager(Inventory(Loader()), inv_info)
    inv_info = inventory_manager.parse_sources(['localhost,'])
    assert inv_info == {'localhost,': {}}
    # Inventory with ini file
    # FIXME: Find a way to test an ini file without hardcoding the path
    inventory_manager = InventoryManager(Inventory(Loader()), inv_info)
    inv_info = inventory_manager.parse_sources('tests/inventory/test_inventory.ini')

# Generated at 2022-06-12 22:35:23.681836
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    inventory = InventoryManager(loader=None, sources=None)
    assert inventory.subset() == None
    assert inventory.subset("all") == None
    assert inventory.subset("host1") == None
    assert inventory.subset("host*") == None
    assert inventory.subset("host[1:10]") == None
    assert inventory.subset("group*") == None
    assert inventory.subset("!blacklist") == None
    assert inventory.subset("group1:group2") == None
    assert inventory.subset("group1:!group2") == None
    assert inventory.subset("group[1:2]:group[3:4]") == None

    inventory = InventoryManager(loader=None, sources=None)
    inventory.subset("host1")

# Generated at 2022-06-12 22:35:28.042807
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # Create a InventoryManager object
    inventory_manager = InventoryManager()

    # Call method subset with argument None
    result = inventory_manager.subset(None)

    # Check result
    assert result is None

    # Call method subset with argument 'test'
    # This will throw an error if limit file is not found.
    # So do not test this
    result = inventory_manager.subset(u"@/tmp/test",)

    # Check result
    assert result is None


# Generated at 2022-06-12 22:35:37.925367
# Unit test for method get_hosts of class InventoryManager
def test_InventoryManager_get_hosts():
    h1 = Host("host1")
    h2 = Host("host2")
    g1 = Group("group1", [h1,h2])
    g2 = Group("group2", [h2])

    inventory = Inventory([h1, h2], [g1, g2])

    manager = InventoryManager( inventory )

    # test all hosts
    result = manager.get_hosts("all")
    assert result == [h1, h2]

    # test host1
    result = manager.get_hosts("host1")
    assert result == [h1]

    # test host1, host2
    result = manager.get_hosts("host1:host2")
    assert result == [h1, h2]

    # test host2
    result = manager.get_hosts("host2")

# Generated at 2022-06-12 22:35:47.769098
# Unit test for method parse_sources of class InventoryManager
def test_InventoryManager_parse_sources():
    c = InventoryManager(playbook=playbook)
    sources = []
    sources.append(dict(name='foo'))
    assert c.parse_sources(sources) == {
        'all': {
            'hosts': {
                'foo': {}
            }
        }
    }
    sources = []
    sources.append(dict(name='foo', hosts=['a', 'b']))
    assert c.parse_sources(sources) == {
        'all': {
            'hosts': {
                'foo': {}
            }
        }
    }
    sources = []
    sources.append(dict(name='foo', hosts=['a', 'b']))
    sources[0]['hosts'].append(dict(name='a'))

# Generated at 2022-06-12 22:35:54.159252
# Unit test for method subset of class InventoryManager
def test_InventoryManager_subset():
    # A test case for InventoryManager.subset
    import ansible.parsing.dataloader
    import ansible.inventory.manager
    import ansible.inventory.host
    loader = ansible.parsing.dataloader.DataLoader()
    im = ansible.inventory.manager.InventoryManager(loader=loader, sources=["localhost,"])
    h = ansible.inventory.host.Host(name="localhost")
    im.subset(subset_pattern="localhost")
    h.vars["ansible_connection"] = "local"
    h.vars["ansible_ssh_host"] = "localhost"
    assert h.name == "localhost"
    assert h.vars["ansible_connection"] == "local"
    assert h.vars["ansible_ssh_host"] == "localhost"
