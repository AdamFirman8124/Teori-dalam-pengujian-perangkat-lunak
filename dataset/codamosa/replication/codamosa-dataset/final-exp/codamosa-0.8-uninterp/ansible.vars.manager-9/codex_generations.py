

# Generated at 2022-06-13 17:18:37.792812
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager._options_vars = {"a":1, "b":"value"}
    variable_manager._fact_cache = {
        "hosta": {
            "fact_name1": "fact_value1"
        }
    }
    variable_manager._nonpersistent_fact_cache = {
        "hosta": {
            "nonpersistent_fact_name1": "nonpersistent_fact_value1"
        }
    }
    variable_manager._vars_cache = {
        "hosta": {
            "var_name1": "var_value1"
        }
    }

# Generated at 2022-06-13 17:18:42.220456
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()
    assert variable_manager._fact_cache is not None
    assert variable_manager._vars_cache is not None
    assert variable_manager._vars_plugins is not None

# Generated at 2022-06-13 17:18:48.949827
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    var_mgr = VariableManager()
    var_mgr._fact_cache = {
        'host1': {
            'a': 'A',
            'b': 'B',
        },
    }
    expected = {
        'hostvars': {
            'host1': {
                'a': 'A',
                'b': 'B',
            }
        },
        'omit': '*****',
    }
    result = var_mgr.get_vars(host='host1', include_hostvars=True)
    assert result == expected


# Generated at 2022-06-13 17:18:57.256369
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Setup the testcase
    config = MagicMock(spec=ConfigParser)
    config.get.side_effect = [None, None]

    # Default inventory, no extra vars
    vm = VariableManager(loader=MagicMock(), inventory=MagicMock(), version_info=config)
    vars_ = vm.get_vars()
    assert vars_ == {'gid': 1000, 'group_names': [], 'groups': {}, 'home': '/home/ansible', 'inventory_dir': None,
    'inventory_file': None, 'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost',
    'omit': '__omit_place_holder__', 'playbook_dir': None, 'uid': 1000, 'user_id': 'ansible'}, vars_

    # No

# Generated at 2022-06-13 17:19:00.929559
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    variable_manager = VariableManager()
    variable_manager.set_host_variable('test_host', 'x', 'y')
    assert variable_manager.get_vars(play=None, host=Host('test_host'))['x'] == 'y'

# Generated at 2022-06-13 17:19:09.307429
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # setup
    inventory = InventoryManager(loader=None, sources=None)
    options = Options(connection='local', module_path=None, forks=100, become=None,
                      become_method=None, become_user=None, check=False, diff=False,
                      syntax=None, start_at_task=None, verbosity=None, inventory=inventory)
    loader = DataLoader()
    playbook = Playbook.load(playbook='playbook.yml', loader=loader, inventory=inventory)
    manager = VariableManager(
        loader=loader, inventory=inventory,
        version_info=SETUP_CACHE['ansible_version']
    )
    play = playbook.get_plays()[0]

    # manager.set_inventory(inventory)
    # Test1: No inventory set.

# Generated at 2022-06-13 17:19:09.845306
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    pass

# Generated at 2022-06-13 17:19:12.789346
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    v_m = VariableManager()
    v_m.set_host_variable("var", "varname", "value")
    assert v_m._vars_cache.get("var") == {"varname": "value"}

# Generated at 2022-06-13 17:19:24.582380
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    variable_manager = VariableManager()
    # Test 1
    rst = variable_manager.set_host_variable(host="1", varname="2", value={})
    ok_(rst is None)
    # Test 2
    rst = variable_manager.set_host_variable(host="1", varname="2", value={})
    ok_(rst is None)
    # Test 3
    rst = variable_manager.set_host_variable(host="2", varname="1", value={})
    ok_(rst is None)
    # Test 4
    rst = variable_manager.set_host_variable(host="1", varname="a", value={})
    ok_(rst is None)




# Generated at 2022-06-13 17:19:29.395021
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Setup test
    inventory = None
    loader = DictDataLoader({"/": {}})
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Execute test
    variable_manager.get_vars(play=None, host=None, task=None, include_delegate_to=True, include_hostvars=True)


# Generated at 2022-06-13 17:20:06.049775
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    from collections import Mapping
    from ansible.errors import AnsibleAssertionError
    
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import json

    loader = DataLoader()

    inventories = [
        InventoryManager(loader=loader, sources='./test/unit/files/host_vars.yml'),
    ]

    host = Host(name='fake_host')
    
    vm = VariableManager(loader=loader, inventory=inventories[0])
    vm.extra_vars={'fake_host': {'var1': {'subvar1': 'subvalue1'}}, 'all': {'var1': 'value1'}}


# Generated at 2022-06-13 17:20:07.587467
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    v = VarsWithSources({'a': 1})
    assert v['a'] == 1
    v.sources['a'] = 'b'
    assert v['a'] == 1
    assert v.sources['a'] == 'b'

# Generated at 2022-06-13 17:20:18.964063
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
	host = Host("host_name")
	host_variables = dict(
		ansible_inventory_hostname='host_name',
		ansible_play_hosts_all=['host_name'],
		ansible_play_hosts=['host_name'],
		ansible_play_batch=['host_name'],
		play_hosts=['host_name']
	)

	variable_manager = VariableManager()
	variable_manager.set_host_variable(host, 'hostvars', host_variables)

	import pdb; pdb.set_trace()
	variables = variable_manager.get_vars(
		host = host,
		include_hostvars = True
	)


# Generated at 2022-06-13 17:20:22.544691
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    host = 'testhost'
    facts = dict()
    facts["a"] = "a"
    facts["b"] = "b"
    facts["c"] = "c"

    vc = VariableManager()
    # Setup
    vc.set_host_facts(host, facts)

# Generated at 2022-06-13 17:20:32.921143
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test get_vars:
    # (1) with inventory, host, play and task
    # (2) without inventory, host, play and task
    # (3) without inventory, host and task, with play
    # (4) without inventory, host and play, with task
    # (5) without inventory, play and task, with host

    inventory = TestInventory()
    host = TestHost("localhost")
    play = TestPlay()
    task = TestTask("localhost")

    # Test get_vars with inventory, host, play and task
    variables = VariableManager(loader=DictDataLoader()).get_vars(inventory=inventory, host=host, play=play, task=task)
    # With inventory, host, play and task, is_playbook should be True, ansible_play_batch should be []
    assert variables

# Generated at 2022-06-13 17:20:33.653637
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """
    Test for get_vars
    """
    pass


# Generated at 2022-06-13 17:20:41.572718
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    vm = VariableManager()
    vm.add_host_vars_file("hostvars")
    vm.set_inventory(None)
    vm.set_loader(None)
    vm.set_vault_secrets(None)
    vm.set_options({'ansible-playbook': '/Users/jeff/ansible_vault/ansible/ansible-playbook'})
    vm.set_hostvars(None)
    vm.set_fact_cache(None)
    vm.data = DataLoader._create_vault_secrets(None)
    vm.get_vars(None, None, None, None, None)
    vm.get_vars(None, None, None, False, False)
    vm.get_vars(None, None, None, True, True)
    vm.get

# Generated at 2022-06-13 17:20:42.459369
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    assert True


# Generated at 2022-06-13 17:20:51.622269
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # get_vars is an instance method, so we have to create an instance of VariableManager to test it
    # set up

    # VariableManager already has a reference to a loader, but we need to create a new one for our tests
    # otherwise we will be loading from the inventories and playbooks in our checkout, and they won't necessarily
    # contain all of the necessary examples
    test_loader = DataLoader()
    new_inventory = Inventory(loader=test_loader, host_list=[])
    # test_vars_cache is a fixture set up in conftest.py

    variable_manager = VariableManager()
    variable_manager._fact_cache = test_vars_cache['_fact_cache']
    variable_manager._hostvars = test_vars_cache['_hostvars']

# Generated at 2022-06-13 17:21:01.425795
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # load the test inventory
    inventory = InventoryManager(loader=None, sources=['test/test_variable_manager/test_vars/inventory.ini'])

    # create a variable manager passing the inventory
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # load the test variables

# Generated at 2022-06-13 17:21:46.458041
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()  # is a VariableManager

    setattr(v, '_fact_cache', {})
    setattr(v, '_vars_cache', {'ok': {'a': 1}})
    setattr(v, '_hostvars', {})

    # Call method with only required arg
    result = v.get_vars()

    assert result == {}

    # Call method with one optional arg
    result = v.get_vars(host=None)

    assert result == {'a': 1}


# Generated at 2022-06-13 17:21:50.428470
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # We don't really need to run any test cases here
    # Since the get_vars method is pretty much just a wrapper around other methods,
    # so we can just validate that it doesn't crash.
    host = FakeHost()
    variables = VariableManager()
    host.get_vars.return_value = dict()
    variables.get_host_vars(host=host)
    variables.get_vars(host=host)

# Generated at 2022-06-13 17:21:55.879879
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():

    vm = VariableManager()

    # Set empty facts
    vm.set_nonpersistent_facts('localhost', {})
    assert vm._nonpersistent_fact_cache['localhost'] == {}

    # Set non-empty facts
    vm.set_nonpersistent_facts('localhost', {'foo': 'bar'})
    assert vm._nonpersistent_fact_cache['localhost'] == {'foo': 'bar'}

    # Set empty facts on a different host
    vm.set_nonpersistent_facts('some_host', {})
    assert vm._nonpersistent_fact_cache['some_host'] == {}

    # Set non-empty facts on a different host
    vm.set_nonpersistent_facts('some_host', {'bar': 'baz'})

# Generated at 2022-06-13 17:21:59.564555
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    test_VariableManager = VariableManager()
    test_VariableManager.get_vars()


# Generated at 2022-06-13 17:22:01.101834
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()
    assert {} == v.get_vars()


# Generated at 2022-06-13 17:22:04.665642
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()

    # test call on get_vars() method
    variable_manager.get_vars(loader=None, play=None, host=None, task=None)

# Generated at 2022-06-13 17:22:13.916629
# Unit test for constructor of class VariableManager
def test_VariableManager():
    print("Testing creation of VariableManager")
    from collections import namedtuple
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    Inventory = namedtuple('Inventory', ['hosts', 'groups', '_hosts_cache'])
    FakeOptions = namedtuple('FakeOptions', ['forks'])

    inventory = Inventory(hosts={}, groups={}, _hosts_cache={})
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    variable_manager = VariableManager(loader=DataLoader(), inventory=InventoryManager(loader=DataLoader(), sources=[]))

    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory,
                                       options=FakeOptions(forks=42))

    variable_manager.extra_vars = dict

# Generated at 2022-06-13 17:22:19.228464
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    This method tests the following ways of get_vars():
    1. get_vars()
    2. get_vars(host=None)
    3. get_vars(host=None, include_hostvars=True)
    '''
    vms = VariableManager()
    vars = vms.get_vars()
    vars_1 = vms.get_vars(host=None)
    vars_2 = vms.get_vars(host=None, include_hostvars=True)
    assert vars == vars_1 == vars_2


# Generated at 2022-06-13 17:22:28.171002
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # Verify that the constructor of class VariableManager creates an
    # instance with correct attributes
    loader = DictDataLoader({'no_such_file.yml': "{}", 'some_file.yml': "{}"})
    inventory = Inventory(loader=loader)

    # Check initialisation and attributes
    var_manager = VariableManager(loader=loader, inventory=inventory)
    assert isinstance(var_manager._vars_cache, MutableMapping)
    assert isinstance(var_manager._fact_cache, MutableMapping)
    assert isinstance(var_manager._nonpersistent_fact_cache, MutableMapping)
    assert isinstance(var_manager._omit_token, string_types)
    assert isinstance(var_manager._options_vars, MutableMapping)

# Generated at 2022-06-13 17:22:37.755631
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """Variable_manager__get_vars(self, play=None, host=None, task=None, include_delegate_to=True, include_hostvars=True)"""
    m = MagicMock()
    m.serialize.return_value = "test"
    m.is_template.side_effect = [False, False, False, True, False]
    m.template.return_value = True
    m.get_search_path.return_value = ["a"]

    m1 = MagicMock()
    m1.name = "test"
    m1.address = "test address"

    m2 = MagicMock()
    m2.vars = {"a": 1, "b": 2}
    m2f = MagicMock()
    m2f.run.return_value = True

    m

# Generated at 2022-06-13 17:23:30.839719
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    def test_with_assert(*args, **kwargs):
        try:
            VariableManager().get_vars(*args, **kwargs)
        except Exception as error:
            assert True
        else:
            assert False
    play = Play()
    play._play_hosts = ['all']
    host = Host()
    host.vars = dict(a=1)
    test_with_assert()
    test_with_assert(host=host)
    test_with_assert(host=host, play=play)



# Generated at 2022-06-13 17:23:39.230329
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager.set_host_variable('host1','test','test_value')
    variable_manager.set_host_variable('host1','test2','test2_value')
    variable_manager.set_host_variable('host2','test3','test3_value')
    assert variable_manager.get_vars(host=None) == {'test': 'test_value', 'test2': 'test2_value'}
    assert variable_manager.get_vars(host='host1') == {'test': 'test_value', 'test2': 'test2_value'}
    assert variable_manager.get_vars(host='host2') == {'test3': 'test3_value'}

# Generated at 2022-06-13 17:23:47.184636
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    '''Unit test for method set_host_facts of class VariableManager'''
    # Create a temporary directory for config files
    tmp_dir = tempfile.mkdtemp()

    # Create a temporary ansible.cfg
    fd, path = tempfile.mkstemp(dir=tmp_dir)
    os.close(fd)
    with open(path, 'w') as f:
        f.write("[defaults]\nroles_path = %s" % (tmp_dir))
    os.chmod(path, 0o600)
    # Create a temporary roles folder
    os.mkdir(os.path.join(tmp_dir, 'roles'))

    # KeyError when facts don't exist
    # Create a VariableManager object
    inventory = InventoryManager([])
    loader = DataLoader()
    variable_manager

# Generated at 2022-06-13 17:23:49.809678
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    my_host = host.Host(name='myhost')
    # TODO: mock inventory
    my_inventory = inventory.Inventory()
    my_inventory.set_variable_manager(VariableManager())
    my_task = task.Task()
    assert my_inventory.get_variable_manager().get_vars(host=my_host, task=my_task) == {}

# Generated at 2022-06-13 17:23:55.541368
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    playbook_vars = dict(
        ansible_foo='bar',
        ansible_contact=dict(
            name='John Doe',
            email='jdoe@example.com',
        ),
        ansible_host=dict(
            ansible_ssh_host='fake-host'
        )
    )
    host_vars = dict(
        ansible_user='alice',
    )
    inventory = Inventory(host_list=[])
    inventory.set_variable_manager(VariableManager(loader=None, inventory=inventory, variables=playbook_vars))
    host = inventory.get_host('fake-host')
    host.set_variable_manager(
        VariableManager(loader=None, inventory=inventory, variables=host_vars)
    )
    variable_manager = host.get_variable_manager()

# Generated at 2022-06-13 17:24:02.557231
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    VariableManager = plugins.variable.VariableManager
    Host = inventory.host.Host
    custom_args = dict()
    custom_args['loader'] = dict()
    custom_args['inventory'] = dict()
    custom_args['variable_manager'] = dict()
    custom_args['variable_manager']['options_vars'] = dict()
    custom_args['variable_manager']['fact_cache'] = dict()
    custom_args['variable_manager']['host_fact_cache'] = dict()
    custom_args['variable_manager']['vars_cache'] = dict()
    custom_args['variable_manager']['extra_vars'] = dict()
    custom_args['variable_manager']['options_vars'] = dict()

# Generated at 2022-06-13 17:24:07.516695
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # test variable manager creation
    variable_manager = VariableManager()

    # test variable manager creation (with inventory)
    variable_manager = VariableManager(inventory=Inventory("myhosts"))

    # test variable manager with many hosts
    host1 = Host("host1")
    host2 = Host("host2")
    variable_manager = VariableManager(inventory=Inventory(hosts=[host1, host2]))
    if variable_manager._inventory.get_host("host1") is None:
        raise AssertionError("Host1 not found")
    if variable_manager._inventory.get_host("host2") is None:
        raise AssertionError("Host2 not found")
    if variable_manager._inventory.get_host("host3") is not None:
        raise AssertionError("Host3 found")

    # test variables creation

# Generated at 2022-06-13 17:24:17.478987
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=None, host_list=['localhost'])
    host = inventory.get_host('localhost')
    options = Options()
    #values = {'inventory_hostname':'localhost','host_name':'localhost','hostvars':{},'group_names':[u'all'],'groups':{u'all':{u'_meta':{u'hostvars':{}}}}}

    values = {'inventory_hostname':'localhost','hostvars':{},'group_names':[u'all'],'groups':{u'all':{u'_meta':{u'hostvars':{}}}}}

    vm = VariableManager(loader=loader, inventory=inventory, options=options)
    #assert vm.get_vars(host=host) ==

# Generated at 2022-06-13 17:24:19.584728
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    self = VariableManager()
    a = self.get_vars(play=None, host=None, task=None, include_hostvars=True)


# Generated at 2022-06-13 17:24:25.436389
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test playbook with tasks and roles
    # playbook_path = os.path.dirname(__file__) + '/test/test.yaml'
    # loader = DataLoader()
    # inventory = InventoryManager(loader=loader, sources=['localhost'])
    # variable_manager = VariableManager(loader=loader, inventory=inventory)
    # my_vars = variable_manager.get_vars()
    print('hi')

# Generated at 2022-06-13 17:26:01.802264
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import load_plugins
    from ansible.vars.manager import VariableManager
    from ansible.vars import combine_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.utils.vars import combine_hash
    from ansible.plugins.loader import collection_finder

    # First, initialize objects and data structures we will need
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["test/test_inventories/test_inventory"])
    hostvars = HostVars(inventory=inventory)
    reserved = Reserved(loader=loader)
    variable_manager

# Generated at 2022-06-13 17:26:02.240281
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# Generated at 2022-06-13 17:26:10.196499
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    '''
    Unit test for method set_nonpersistent_facts of class VariableManager
    '''
    # Create ansible-pan object
    p = PanObj()
    p.ansible_object_cache = {}
    p.ansible_object_cache['ansible.utils.unsafe_proxy.AnsibleUnsafeText'] = {}
    # Create ansible-playbook object
    play_host = 'host'
    play_hosts = [play_host]
    play_module = 'module'
    play_tasks = [{'hosts': play_host, 'module': play_module, 'name': 'Unit test for method set_nonpersistent_facts of class VariableManager'}]
    play_vars = {'var1': 'val1', 'var2': 'val2'}

# Generated at 2022-06-13 17:26:19.491373
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Create a new instance of VariableManager
    vm = VariableManager()

    # Test with a bare minimum of arguments
    result = vm.get_vars()

    # Test with as many arguments as possible
    vm.get_vars(play=None, host=None, task=None, include_delegate_to=False, include_hostvars=True)

    # Test with a bad type
    with pytest.raises(AnsibleAssertionError):
        vm.get_vars(None)

    # Test with a bad type
    with pytest.raises(AnsibleAssertionError):
        vm.get_vars(play=None, host=None, task=None, include_delegate_to=None, include_hostvars=True)

    # Test with a bad type

# Generated at 2022-06-13 17:26:25.350617
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:26:30.270598
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    data = {"name": "ansible"}
    host = "ansible"
    vm = VariableManager()
    facts = {"ansible_processor_vcpus": "2"}
    vm.set_nonpersistent_facts(host, facts)
    vm.set_nonpersistent_facts(host, data)



# Generated at 2022-06-13 17:26:37.539144
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """Unit tests for VariableManager.get_vars()."""
    import pytest

    from ansible.plugins.loader import lookup_loader
    from ansible.utils.vars import combine_vars

    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.vars.hostvars
    import ansible.vars.vars_cache
    import ansible.vars.unsafe_proxy

    import units.mock.loader
    import units.mock.path
    import units.mock.plugins.lookup
    import units.mock.plugins.task_loader

    # Parameters to control the test
    test_omit_token = 'test_omit_token'
    test_inventory = ansible.vars.hostvars.Host

# Generated at 2022-06-13 17:26:48.292755
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from models.inventory import Inventory
    from models.host import Host
    from models.inventory_script import InventoryScript
    from models.task import Task
    from models.play import Play
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader
    
    host = Host()
    host.name = 'localhost'
    host.address = '127.0.0.1'
    host.set_variable('ansible_connection',  'local')

    inventory = Inventory()
    inventory.add_host(host)
    inventory.set_variable('hostvars',  host.get_vars())

    play = Play()
    play.set_loader(DictDataLoader({}))
    play._hosts_cache = {'all': inventory.get_hosts()}
    play

# Generated at 2022-06-13 17:26:50.476173
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.get_vars()


# Generated at 2022-06-13 17:26:56.320365
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    from ansible.inventory import Inventory
    from ansible.vars import VariableManager as VariableManagerClass

    inventory = Inventory("test/ansible/inventory/hosts")
    variable_manager = VariableManagerClass(loader=None, inventory=inventory)
