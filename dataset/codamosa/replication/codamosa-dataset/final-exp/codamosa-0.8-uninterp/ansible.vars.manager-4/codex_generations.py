

# Generated at 2022-06-13 17:18:53.522879
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    args = dict(
        loader = None,
        inventory = None,
        host_vars = None,
        group_vars = None,
        play_vars = None,
        extra_vars = {},
        options_vars = None,
        play = None,
        task = None,
        host = None,
        include_delegate_to = True,
        omit_token = None,
        is_playbook = False,
        is_task = False,
        use_cache = False,
        run_once = False,
        fail_on_undefined_vars = False,
        use_task_vars = False,
        merge_task_vars = False,
        is_role = False,
        dep_chain = None,
        allow_unsafe_lookups = False,
    )

# Generated at 2022-06-13 17:19:03.680496
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory import Host, Group
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager


    def return_groups():
        groups = {
            'all': Group('all'),
            'ungrouped': Group('ungrouped'),
            'ungrouped.local': Group('ungrouped.local'),
        }
        groups['all'].add_children('ungrouped.local')
        groups['all'].add_children('ungrouped')
        groups['ungrouped'].add_children('ungrouped.local')

        return groups

    def return_hosts():
        hosts

# Generated at 2022-06-13 17:19:13.001196
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
  vm = VariableManager()
  from ansible.vars.manager import VariableManager
  # Testing if the method get_vars takes 3 arguments
  assert len(inspect.getargspec(VariableManager.get_vars).args) == 4
  
  # Testing if the method is able to answer the following query correctly
  # What is the type of the object returned by method get_vars of class VariableManager for the following inputs
  # get_vars(host=None) -> Dict[str, Any]
  # get_vars(host=None, include_hostvars=True) -> Dict[str, Any]

# Generated at 2022-06-13 17:19:25.280935
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    mgr = VariableManager()
    mgr.set_host_variable(host='test_host', varname='varname', value='value')
    assert mgr._vars_cache['test_host']['varname'] == 'value'
    mgr.set_host_variable(host='test_host', varname='varname', value='value_updated')
    assert mgr._vars_cache['test_host']['varname'] == 'value_updated'

    mgr.set_host_variable(host='test_host', varname='varname_dict', value={'k1': 'v1'})
    assert mgr._vars_cache['test_host']['varname_dict'] == {'k1': 'v1'}

# Generated at 2022-06-13 17:19:26.753164
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()
    assert variable_manager is not None


# Generated at 2022-06-13 17:19:32.906339
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # 1. Without vars_plugins
    # TODO: Add more test cases covering more usages of vars_plugins,
    #       if vars_plugins is needed. See Issue #35386.
    vms = VariableManager()
    vms._vars_cache = {'host1': {'a': 'b'}, 'host2': {'a': 'c'}}
    vms._fact_cache = {'host1': {'f': 'g'}}
    vms._nonpersistent_fact_cache = {'host1': {'f': 'g'}}
    vms._options_vars = {'option1': 'value1', 'option2': 'value2'}
    vms._vars_providers = []
    vms._inventory = None
    vms._loader = DictDataLoader({})

# Generated at 2022-06-13 17:19:42.415818
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vmanager = VariableManager()
    assert vmanager.get_vars() == {}
    vmanager.set_host_variable(None, "ansible_network_os", "junos")
    assert vmanager.get_vars() == {'ansible_network_os': 'junos'}
    vmanager.set_host_variable(None, "ansible_network_os", "ios")
    assert vmanager.get_vars() == {'ansible_network_os': 'ios'}


    vmanager = VariableManager()
    assert vmanager.get_vars() == {}
    vmanager.set_host_variable(None, "ansible_network_os", {"default": "junos"})

# Generated at 2022-06-13 17:19:53.066083
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Construct ansible objects
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    var_manager = VariableManager(loader=loader, inventory=inventory)

    # Construct test objects
    host = FakeHost(name='host1')
    group = FakeGroup(hosts=[host])
    inventory.add_group(group)
    inventory.add_host(host)
    inventory.set_variable_manager(var_manager)

    #
    # set_host_fact(host, facts) tests
    #

    # Test for TypeErrors and AnsibleAssertionErrors

# Generated at 2022-06-13 17:19:55.241139
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    a = VarsWithSources({'a': 1})
    assert a.get_source('a') is None
    assert a['a'] == 1

    b = a.copy()
    b.sources['a'] = 'test'
    assert b.get_source('a') == 'test'
    assert b['a'] == 1

# Generated at 2022-06-13 17:20:02.463922
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    a = VariableManager()
    a.set_host_variable("host1","var1","val1")
    a.set_host_variable("host1","var2","val2")
    a.set_host_variable("host1","var1","val2")
    a.set_host_variable("host2","var1","val1")
    a.set_host_variable("host1","var1","new_val")
    a.set_host_variable("host3","var1","new_val")
    a.set_host_variable("host2","var2","new_val2")

# Generated at 2022-06-13 17:20:32.004234
# Unit test for method set_host_facts of class VariableManager

# Generated at 2022-06-13 17:20:39.796333
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:20:47.305969
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    # Create a VarsWithSources object
    a = VarsWithSources.new_vars_with_sources(
        data = {'one_good': 1},
        sources = {'one_good': 'inventory'})

    # Test the VarsWithSources object
    def check(var, expected_value, expected_source):
        value = a[var]
        source = a.get_source(var)
        assert value == expected_value, \
            "value={!r} != {!r} (expected)".format(value, expected_value)
        assert source == expected_source, \
            "source={!r} != {!r} (expected)".format(source, expected_source)

    check('one_good', 1, 'inventory')

# Generated at 2022-06-13 17:20:51.233944
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()

    facts = {
        'one': 1,
        'two': 2,
    }

    host = "testhost"
    vm.set_nonpersistent_facts(host, facts)

    assert vm._nonpersistent_fact_cache == {host: {'one': 1, 'two': 2}}



# Generated at 2022-06-13 17:21:01.010850
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Arguments to be provided to the method under test
    host = 'host'
    play = 'play'
    task = 'task'
    include_delegate_to = True
    include_hostvars = False

    # Create a variable manager object
    variable_manager = VariableManager()

    # get_vars() should not raise any exception
    variable_manager.get_vars(host, play, task, include_delegate_to, include_hostvars)
    # get_vars() should not raise any exception
    variable_manager.get_vars(host, play, task, include_delegate_to, include_hostvars)

    # Test the get_vars() with different values of the host
    host = 'host-1'

# Generated at 2022-06-13 17:21:09.146672
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    C = lambda x: x

    class DummyHost:
        name = 'dummy_host'
        vars = {'foo': 'bar'}

    class DummyTask:
        _role = C(None)
        delegate_to = C('localhost')
        loop = C(None)
        loop_with = C(None)
        register = C(None)
        name = C('dummy_task')
        action = C('dummy_action')

    class DummyRole:
        _role_name = C('limit_role')
        _role_path = '/usr/share/ansible/roles/limit'
        _uuid = C('12345')
        _role_collection = C('bla.example.org')


# Generated at 2022-06-13 17:21:14.913155
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # Initialize
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost")
    variables = VariableManager(loader=loader, inventory=inventory)

    # Check all the attributes
    assert(isinstance(variables._fact_cache, MutableMapping))
    assert(isinstance(variables._nonpersistent_fact_cache, MutableMapping))
    assert(isinstance(variables._vars_cache, MutableMapping))
    assert(isinstance(variables._hostvars, MutableMapping))
    assert(isinstance(variables._omit_token, string_types))
    assert(isinstance(variables._loader, DataLoader))
    assert(isinstance(variables._inventory, InventoryManager))

    # Check passing of parameters to constructor
    loader = DataLoader()
    inventory = Inventory

# Generated at 2022-06-13 17:21:19.337872
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    test_obj = VariableManager()
    host = 'test_host'
    facts = {'test': 'test'}
    test_obj.set_nonpersistent_facts(host, facts)
    assert test_obj._nonpersistent_fact_cache[host] == facts


# Generated at 2022-06-13 17:21:27.350822
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.reserved import Reserved

    loader = AnsibleLoader(None)
    inventory = InventoryManager(loader=loader, sources=['tests/unit/inventory_manager/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    source_vars = {'var1': 'value', 'var2': "{{ var1 }}"}

    result = variable_manager.get_vars(host=None, play=None, task=None, include_delegate_to=False, include_hostvars=False, source_vars=source_vars)
    assert result['var1'] == 'value'

# Generated at 2022-06-13 17:21:29.468887
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    h = Host('127.0.0.1')
    v = VariableManager()
    v.set_host_variable(host=h, varname='a', value='1')
    vars = v.get_vars(host=h)
    # assert vars['a'] == '1'
    assert vars.get('a') == '1'


# Generated at 2022-06-13 17:22:59.538060
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():

    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager

    vm = VariableManager()

    facts = {'ansible_variable': 'exists'}

    vm.set_host_facts('localhost', facts)

    assert vm._fact_cache['localhost'] == facts
    assert vm._fact_cache['localhost'] is not facts

    dummy_host = object()

    # Removing the reference to facts
    facts = None

    vm.set_host_facts(dummy_host, UnsafeProxy(dict(a=1)))

    assert vm._fact_cache[dummy_host]['a'] == 1
    assert isinstance(vm._fact_cache[dummy_host], MutableMapping)


# Generated at 2022-06-13 17:23:04.206426
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vars = {}
    host = 'hosta'
    varname = 'foo'
    varname2 = 'bar'
    expected = {
        varname: 'abc',
        varname2: 'def',
    }
    vm = VariableManager(vars)
    # Verify a normal variable using set_host_variable
    vm.set_host_variable(host, varname, 'abc')
    assert isinstance(vm._vars_cache[host], Mapping)
    assert vm._vars_cache[host][varname] == 'abc'
    # Verify a normal variable already in cache
    vm.set_host_variable(host, varname, 'def')
    assert isinstance(vm._vars_cache[host], Mapping)

# Generated at 2022-06-13 17:23:12.388768
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    host_1 = '192.0.2.2'
    host_2 = '192.0.2.3'

    vars_cache = {"host_1": {"var_1": "value_1"}}
    fact_cache = {"host_2": {"var_2": "value_2"}}
    host_vars = {"host_1": {'var_3': 'value_3'}, "host_2": {'var_4': 'value_4'}}
    vm = VariableManager(vars_cache=vars_cache,
                         fact_cache=fact_cache,
                         host_vars=host_vars)

    host = Host(name="192.0.2.2")
    variables = vm.get_vars(host=host)

# Generated at 2022-06-13 17:23:18.041324
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    '''
    Test for method set_host_facts of class VariableManager
    '''
    # set up first test
    test_obj = VariableManager()
    host = 'test1'
    facts = {"test1": "test1"}

    test_obj.set_host_facts(host, facts)
    assert(test_obj.fact_cache == {"test1": {"test1": "test1"}})

    # set up second test
    test_obj = VariableManager()
    host = 'test2'
    facts = {"test2": "test2"}

    with pytest.raises(TypeError):
        test_obj.set_host_facts(host, facts)

    # set up third test
    test_obj = VariableManager()
    host = 'test3'
    facts = "test3"


# Generated at 2022-06-13 17:23:26.795676
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """Test for VariableManager.get_vars."""
    def get_dependency_role_names(self, play):
        return []
    def load_extra_vars(self, loader):
        return {'a': 'b'}
    def _get_delegated_vars(self, play, task, existing_variables):
        return {}, None, None
    def set_options_vars(self, options):
        options.connection = "winrm"
    def get_fact_cache(self):
        return 'test cache'
    vm = VariableManager()
    vm._get_dependency_role_names = get_dependency_role_names
    vm._load_extra_vars = load_extra_vars
    vm._get_delegated_vars = _get_delegated_vars

# Generated at 2022-06-13 17:23:31.299737
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    v = [{'key': 'value'}, {'key': 'value'}]
    VariableManager._set_host_variable(v, 'host', 'key', 'new_value')
    assert v == [{'key': 'new_value'}, {'key': 'new_value'}]

# Generated at 2022-06-13 17:23:39.664437
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    inv = Inventory(loader=None)
    inv.add_group('example_group')
    inv.add_host(Host(name="example-host", groups=["example_group"]))

    variable_manager = VariableManager(loader=None, inventory=inv, version_info=dict(network_os='ios', network_os_version='3.1.1'))
    assert variable_manager.version_info['network_os_version'] == '3.1.1'

    variable_manager.options_vars = dict(
        ansible_connection='local',
        ansible_python_interpreter='/usr/bin/python',
        ansible_network_os='eos',
    )

# Generated at 2022-06-13 17:23:40.702704
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()
    myhash = dict()
    assert v.get_vars(myhash, True) == dict()


# Generated at 2022-06-13 17:23:41.290530
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()


# Generated at 2022-06-13 17:23:47.049621
# Unit test for method set_host_facts of class VariableManager

# Generated at 2022-06-13 17:24:48.545505
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    _test_task = """
    - name: test task
      shell: echo foo
    """
    _test_inventory = """
    all:
      hosts:
        localhost:
          ansible_connection: local
          foo: bar
      vars:
        foo: baz
        ansible_connection: docker
    """
    task = Task.load(_test_task)
    inventory = Inventory.load(_test_inventory)

    vm = VariableManager()
    vm.set_inventory(inventory)
    vm.add_host(host=Host(vars={'ansible_connection': 'local'}))

# Generated at 2022-06-13 17:24:58.048303
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    inventory = Inventory(loader=None, variable_manager=None, host_list=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play = None
    host = "hostname"
    task = None
    include_delegate_to=True
    include_hostvars=True
    variables = variable_manager.get_vars(play=play, host=host, task=task, include_delegate_to=include_delegate_to, include_hostvars=include_hostvars)

# Generated at 2022-06-13 17:25:04.947757
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    '''
    This function tests the functionality of method set_host_variable of class VariableManager for the cases:
        normal:
                test_host_name = "host_name"
                test_var_name = "var_name"
                test_value = "test_value"
                var_manager.set_host_variable(test_host_name,test_var_name,test_value)
        abnormal:
                test_host_name = "host_name"
                test_var_name = "var_name"
                test_value = "test_value"
                var_manager._vars_cache.pop(test_host_name)
                var_manager.set_host_variable(test_host_name,test_var_name,test_value)
    '''
    # initialization
    var_manager = VariableManager()

# Generated at 2022-06-13 17:25:12.536514
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    target_obj = VariableManager.__new__(VariableManager)
    target_obj.__init__(loader=None, inventory=None, version_info=None)
    host = 'valid_string'
    varname = 'valid_string'
    value = 'valid_string'
    assert hasattr(target_obj, 'set_host_variable')
    assert callable(getattr(target_obj, 'set_host_variable'))
    returned_obj = target_obj.set_host_variable(host, varname, value)
    assert returned_obj == None

# Generated at 2022-06-13 17:25:20.336151
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    var_mgr1 = VariableManager()
    var_mgr1._vars_cache = {'my_host':{'my_var': 'my_value'}}
    var_mgr1.set_host_variable('my_host', 'my_var2', 'my_value2')
    assert var_mgr1._vars_cache['my_host']== {'my_var': 'my_value', 'my_var2': 'my_value2'}
    var_mgr2 = VariableManager()
    var_mgr2._vars_cache = {'my_host':{'my_var': {'nested_var1': 'nested_value1'}}}

# Generated at 2022-06-13 17:25:21.876335
# Unit test for constructor of class VariableManager
def test_VariableManager():
    test_varmgr = VariableManager()
    assert test_varmgr is not None

# Generated at 2022-06-13 17:25:25.390685
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variable_manager.options_vars = {}
    variable_manager.omit_token = None
    variable_manager.hostvars = None
    variable_manager.get_vars({},None,None,False)


#

# Generated at 2022-06-13 17:25:26.288460
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()
    v.set_host_variable()



# Generated at 2022-06-13 17:25:31.736507
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # tests that calling set_host_facts with a non-mapping object will fail with a nice error message
    # This test requires that ANSIBLE_LIBRARY and ANSIBLE_MODULE_UTILS are set to valid directories
    vm = VariableManager()
    try:
        vm.set_host_facts('host1', [1, 2, 3])
        assert False, "Expected fail but did not get one."
    except AnsibleAssertionError:
        assert True
    except Exception as e:
        assert False, "Expected AssertionError but got %s" % type(e)


# Generated at 2022-06-13 17:25:33.476419
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    host = 'localhost'
    facts = dict(hostname='localhost')
    vm.set_nonpersistent_facts(host, facts)
    assert vm.get_nonpersistent_facts(host) == facts


# Generated at 2022-06-13 17:27:31.996065
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()

    # Check the existence of this method
    assert callable(getattr(vm, 'set_nonpersistent_facts', None))

    # We need an invalid value to check if this method is raising the right exception
    invalid_facts = 123
    host = "localhost"
    facts = {"a_fact" : "a_value"}

    # Check if the exception is raising
    assert_raises(AnsibleAssertionError, vm.set_nonpersistent_facts, host, invalid_facts)

    # Check if the fact is setting the right value
    vm.set_nonpersistent_facts(host, facts)
    assert vm._nonpersistent_fact_cache[host] == facts


# Generated at 2022-06-13 17:27:34.938200
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # This method is not implemented; it should be implemented
    # as part of the final declaration of this class.
    raise NotImplementedError

# Generated at 2022-06-13 17:27:42.382045
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # 1. Check empty constructor
    vm = VariableManager()
    assert vm._vars_cache == dict()
    assert vm._nonpersistent_fact_cache == dict()
    assert vm._fact_cache == dict()
    assert vm._inventory == None
    assert vm._fact_cache_loaded == False
    assert vm._loader is not None

    # 2. Check constructor with inventory
    inventory = Inventory('localhost,')
    vm = VariableManager(inventory=inventory)
    assert vm._vars_cache == dict()
    assert vm._nonpersistent_fact_cache == dict()
    assert vm._fact_cache == dict()
    assert vm._inventory == inventory
    assert vm._fact_cache_loaded == False
    assert vm._loader is not None

    # 2.5 test for constructor with hostvars
    hvars = dict()


# Generated at 2022-06-13 17:27:48.642276
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    vm = VariableManager()
    facts = {'a': 1, 'b': 2}
    vm.set_host_facts('hostname', facts)
    assert vm._fact_cache['hostname'] == facts


# Generated at 2022-06-13 17:27:53.268929
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    test_inventory = Inventory(host_list=[])
    test_var_manager = VariableManager(loader=DictDataLoader({}), inventory=test_inventory, version_info=__version_info__)
    test_var_manager._vars_cache = {'test_host': {'test_var': 'test_value'}}
    result = test_var_manager.get_vars(host=Host(name='test_host'))
    assert result['test_var'] == 'test_value'



# Generated at 2022-06-13 17:27:58.742904
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()

    variable_manager.set_nonpersistent_facts(host='hostname', facts={})


# Generated at 2022-06-13 17:28:06.838007
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    fake_host = Host('localhost')
    fake_host.set_variable('ansible_facts', dict())
    test_variable_manager = VariableManager(loader=None, inventory=None)
    test_variable_manager._vars_cache = dict()
    test_variable_manager._vars_cache[str(fake_host)] = dict()
    test_variable_manager.set_host_variable(fake_host, 'ansible_os_family', 'RedHat')
    assert test_variable_manager._vars_cache[str(fake_host)]['ansible_os_family'] == 'RedHat'

