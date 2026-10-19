

# Generated at 2022-06-13 17:18:47.873745
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # target_method = VariableManager.get_vars
    # test_obj = None
    
    # expected_error = None
    # error = None
    
    # expected_result = None
    # result = None
    return

# Generated at 2022-06-13 17:18:55.230676
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    # Unit test for method set_host_variable of class VariableManager

    vm = VariableManager()

    set_host_variable(vm, "ansible_ssh_host", "my_hostname")
    assert vm._vars_cache["my_hostname"]["ansible_ssh_host"] == "my_hostname"

    set_host_variable(vm, "ansible_ssh_host", "other_host")
    assert vm._vars_cache["other_host"]["ansible_ssh_host"] == "other_host"

    set_host_variable(vm, "ansible_ssh_host", "my_hostname")
    assert vm._vars_cache["my_hostname"]["ansible_ssh_host"] == "my_hostname"

    # An existing vars_cache attribute cannot be overwritten


# Generated at 2022-06-13 17:19:05.040358
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # NOTE: This test is using vars, as they are a subset of the variable types that can be stored.

    # In Ansible 2.0 vars can be stored in the inventory, play, host and task.
    # In Ansible 2.1 vars can also be stored in a role.

    # Create a variable manager for the test
    variable_manager = VariableManager()

    # Create an inventory for the test
    inventory = Inventory(loader=Mock(), variable_manager=variable_manager, host_list=[])

    # Create a play for the test

# Generated at 2022-06-13 17:19:08.573627
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    v = VarsWithSources({'k1': 'v1'})
    v['k1']
    # Test that a non-existing key raises an exception
    with pytest.raises(KeyError):
        v['k2']

# Generated at 2022-06-13 17:19:09.422665
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    VariableManager.get_vars()

# Generated at 2022-06-13 17:19:16.827211
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    inv_data = dict(
        all=dict(
            children=dict(
                foo_group=dict(
                    host=dict(
                        foo='foo.example.org',
                        bar='bar.example.org',
                    ),
                ),
            ),
        ),
    )

    mgr = VariableManager()

# Generated at 2022-06-13 17:19:20.913746
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    global g_vars_cache

    g_vars_cache = dict()
    vm = VariableManager(loader=DictDataLoader({}), inventory=Inventory(loader=None), cache=g_vars_cache)

    # Test 1
    vm.set_host_variable('host_01', 'varname_01', 'value_01')
    assert g_vars_cache == {'host_01': {'varname_01': 'value_01'}}

    # Test 2
    vm.set_host_variable('host_02', 'varname_01', 'value_01')
    assert g_vars_cache == {'host_01': {'varname_01': 'value_01'}, 'host_02': {'varname_01': 'value_01'}}

    # Test 3

# Generated at 2022-06-13 17:19:28.934581
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    class MockDisplay:
        def __init__(self):
            self.data = []
        def debug(self, *args, **kwargs):
            self.data.append(args[0])
    display = MockDisplay()
    v = VarsWithSources({'a':1})
    v.sources = {'a':'file'}
    v['a']
    assert display.data[-1] == "variable 'a' from source: file"
    v.data['b'] = 2
    v['b']
    assert display.data[-1] == "variable 'b' from source: unknown"
    v.copy()
    # No assert for copy() method as it does not know that display is a mock object so sends data to stderr


# Generated at 2022-06-13 17:19:39.810319
# Unit test for constructor of class VariableManager
def test_VariableManager():
    if os.path.exists('/etc/ansible/hosts'):
        inventory = InventoryManager(loader=Loader(), sources='/etc/ansible/hosts')
    else:
        inventory = None
    variable_manager = VariableManager(loader=None, inventory=inventory)
    assert variable_manager._loader is None
    assert variable_manager._inventory == inventory
    assert variable_manager._fact_cache == dict()
    assert variable_manager._nonpersistent_fact_cache == dict()
    assert variable_manager._vars_cache == dict()
    assert variable_manager._host_vars_files == dict()
    assert variable_manager._group_vars_files == dict()
    assert variable_manager._playbook_basedir == './'
    assert variable_manager._options_vars == dict()


# Generated at 2022-06-13 17:19:51.996893
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    # inventory for tests
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=[])
    host = Host('testhost')
    host.set_variable('ansible_python_interpreter', '/usr/bin/python')
    host.set_variable('test_var', 'test_value')
    group = Group('test_group')

# Generated at 2022-06-13 17:20:15.831875
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    test_obj = VariableManager()
    host = 'fake_host'
    varname = 'fake_varname'
    value = {}
    test_obj.set_host_variable(host, varname, value)

# Generated at 2022-06-13 17:20:21.474043
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    vm = VariableManager()
    fact = {u'foo': u'what'}
    vm.set_host_facts(host=u'myhost', facts=fact)
    assert fact == vm._fact_cache[u'myhost']
    vm.clear_facts(hostname=u'myhost')
    vm.set_host_facts(host=u'myhost', facts=fact)
    fact = {u'bar': u'what'}
    vm.set_host_facts(host=u'myhost', facts=fact)
    assert {u'foo': u'what', u'bar': u'what'} == vm._fact_cache[u'myhost']
    vm.set_host_facts(host=u'someotherhost', facts={u'what': u'what'})
    assert fact == vm._fact

# Generated at 2022-06-13 17:20:26.068582
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    # Arrange
    subject = VarsWithSources()
    subject.data = {'test': 'test'}
    subject.sources = {'test': 'test'}

    # Act
    actual = subject.__getitem__('test')
    # Assert
    assert actual == 'test'


# Generated at 2022-06-13 17:20:28.598292
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()
    assert(v.get_vars() is not None)



# Generated at 2022-06-13 17:20:36.330121
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # TODO: Create a mock for the class AnsibleLoader
    # TODO: Create a mock for the class DataLoader
    # TODO: Create a mock for the class TaskExecutor
    # Initialize a mock object for TaskExecutor
    # mock_play = MagicMock()
    # mock_task = MagicMock()
    # mock_task._ds = 'task'
    # Initialize a mock object for AnsibleLoader
    # mock_ansible_loader = AnsibleLoader(mock_data_loader)
    # Initialize the object under test
    variable_manager = VariableManager()
    variable_manager._options_vars = {'foo': 'bar'}
    variable_manager._loader = mock_ansible_loader
    variable_manager._inventory = None
    variable_manager._tqm = mock_task_executor


# Generated at 2022-06-13 17:20:41.060316
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    data = [('test_host', 'test_varname', 'test_value'), ('test_host', 'test_varname', {'test_key': 'test_value'})]

    for host, varname, value in data:
        vm = VariableManager(loader=DictDataLoader())
        vm.set_host_variable(host, varname, value)

        assert vm._vars_cache.get(host, {}).get(varname) == value



# Generated at 2022-06-13 17:20:44.037600
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    fp = u'ansible/playbooks/library/debug.py'
    args = dict()
    #qc = dict(src=fp)

    #v = VariableManager._load_vars(fp, args, qc)
    #assert(v == dict())



# Generated at 2022-06-13 17:20:54.058721
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    unit test for the VariableManager method get_vars
    '''
    v = VariableManager()
    v.set_nonpersistent_facts('a', {'a': 'A'})
    v.set_nonpersistent_facts('b', {'a': 'B', 'b': 'B'})
    v.set_nonpersistent_facts('a', {'a': 'C', 'b': 'C'})
    v.set_nonpersistent_facts('a', {'c': 'A'})
    assert v.get_nonpersistent_facts() == {'a': {'a': 'C', 'b': 'C', 'c': 'A'}, 'b': {'a': 'B', 'b': 'B'}}

import unittest
import sys


# Generated at 2022-06-13 17:21:03.093530
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    variable_manager = VariableManager()

    variable_manager.set_nonpersistent_facts('localhost', dict(default_test_fact=True))
    assert hasattr(variable_manager, '_nonpersistent_fact_cache')
    assert variable_manager._nonpersistent_fact_cache.get('localhost')
    assert variable_manager._nonpersistent_fact_cache.get('localhost').get('default_test_fact')
    assert variable_manager._nonpersistent_fact_cache['localhost']['default_test_fact'] == True

    variable_manager.set_nonpersistent_facts('localhost', dict(default_test_fact=False, test_fact=True))
    assert variable_manager._nonpersistent_fact_cache['localhost']['default_test_fact'] == False
    assert variable_manager._nonpersistent_fact_

# Generated at 2022-06-13 17:21:04.222079
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # TODO: add unit test
    pass

 

# Generated at 2022-06-13 17:21:37.658237
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    vs = VarsWithSources({'a': 1, 'b': 2})
    assert vs['a'] == 1
    assert vs['b'] == 2
    vs.sources.update({'a': 'group_vars/all', 'b': 'inventory'})
    assert vs['a'] == 1
    assert vs['b'] == 2


# Generated at 2022-06-13 17:21:47.159336
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    varmgr = VariableManager()
    varmgr._vars_cache['localhost'] = {"foo":{"bar":"baz"}}
    varmgr.set_host_variable('localhost','foo','quux')
    assert varmgr._vars_cache['localhost'] == {'foo': 'quux'}
    varmgr.set_host_variable('localhost','foo',{"bar":"baz"})
    assert varmgr._vars_cache['localhost'] == {'foo': {'bar': 'baz'}}
    varmgr.set_host_variable('localhost','foo',{"bar":"quux"})
    assert varmgr._vars_cache['localhost'] == {'foo': {'bar': 'quux'}}


# Generated at 2022-06-13 17:21:50.567492
# Unit test for constructor of class VariableManager
def test_VariableManager():
    mock_loader = MagicMock()
    mock_inventory = MagicMock()
    v = VariableManager(loader=mock_loader, inventory=mock_inventory)
    assert v._loader is mock_loader
    assert v._inventory is mock_inventory
    with pytest.raises(AssertionError):
        VariableManager(loader='not_a_loader')

# Generated at 2022-06-13 17:21:57.235699
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    with mock.patch.object(display, 'debug') as display_debug:
        data = {'key_1': 'val_1', 'key_2': 'val_2'}
        sources = {'key_1': 'source_1', 'key_2': 'source_2'}
        v = VarsWithSources.new_vars_with_sources(data, sources)

        # Test that the debug message is displayed
        assert 'val_1' == v['key_1']
        display_debug.assert_called_with("variable 'key_1' from source: source_1")
        # Test that the display message is not called twice
        assert 'val_1' == v['key_1']
        assert 1 == display_debug.call_count



# Generated at 2022-06-13 17:21:59.401107
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    assert True

# Generated at 2022-06-13 17:22:03.977642
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    args = dict(
        inventory=None,
        loader=None,
        variable_manager=None,
        private_data_dir=None,
        play=None,
        options=None,
        hostvars=None,
    )

    variable_manager = VariableManager(**args)

    args = dict(
        host=None,
        task=None,
        include_hostvars=None,
        include_delegate_to=None,
    )

    variable_manager.get_vars(**args)

# Generated at 2022-06-13 17:22:04.573666
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# Generated at 2022-06-13 17:22:13.917678
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 17:22:19.825990
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # can't use a proper inventory in this unit test
    test_inv = [Host(name=h) for h in ['test_host']]
    vm = VariableManager(loader=None, inventory=Inventory(host_list=test_inv))
    vm.set_host_facts('test_host', {'fact': 'value'})
    assert vm.get_vars(host=Host(name='test_host'))['fact'] == 'value'
    vm.set_nonpersistent_facts('test_host', {'extrafact': 'value'})
    assert vm.get_vars(host=Host(name='test_host'))['extrafact'] == 'value'



# Generated at 2022-06-13 17:22:25.293768
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
  # initialize VariableManager object
  vm = VariableManager(loader=None, inventory=None)

  # check if the method get_vars exists and is callable
  assert hasattr(vm, 'get_vars') and callable(getattr(vm, 'get_vars'))

if __name__ == '__main__':
  # run tests
  pytest.main(['-v', __file__])


# Generated at 2022-06-13 17:22:59.756852
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    test_instance = VarsWithSources()
    assert test_instance.data == {}
    assert test_instance.sources == {}
    # __getitem__ method hasn't been defined in class VarsWithSources.
    # Unit test for __getitem__ method of class VarsWithSources is not yet implemented.


# Generated at 2022-06-13 17:23:04.753771
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    vs = VarsWithSources({'a': 1}, sources={'a': 'b'})
    print("'a' in vs", 'a' in vs)
    assert 'a' in vs
    assert vs.get_source('a') == 'b'
    print("vs['a']", vs['a'])
    assert vs['a'] == 1
    print("vs.copy()['a']", vs.copy()['a'])
    assert vs.copy()['a'] == 1

# This class is used to track the sources of vars at each level of the vars hierarchy

# Generated at 2022-06-13 17:23:12.400256
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    hostvars = {
        'my_host_1': {'my_var_1': 'somevalue'},
        'my_host_3': {'my_var_1': 'somevalue'},
    }
    inventory = InventoryManager(loader=DictDataLoader(), sources=[])
    set_connection_loader(inventory._loader)
    inventory.add_host(Host(name='my_host_1', variables={'my_var_2': 'someothervalue'}))
    inventory.add_host(Host(name='my_host_2', variables={'my_var_3': 'someothervalue'}))

# Generated at 2022-06-13 17:23:15.574805
# Unit test for constructor of class VariableManager
def test_VariableManager():
    options = dict(connection='local', module_path=None, forks=10, remote_user='root')
    variable_manager = VariableManager()
    variable_manager._add_options_vars(options)
    assert 'ansible_connection' in variable_manager._options_vars
    assert 'ansible_module_path' in variable_manager._options_vars
    assert 'ansible_forks' in variable_manager._options_vars
    assert 'ansible_remote_user' in variable_manager._options_vars



# Generated at 2022-06-13 17:23:17.251237
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    vars = VarsWithSources({'k1': 'v1'})



# Generated at 2022-06-13 17:23:26.212195
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test to get_vars of VariableManager returns the variables from vars_cache and fact_cache
    print("Testing VariableManager get_vars")
    var_cache = {'host_1': {'var_1': 'value_1'}, 'host_2': {'var_2': 'value_2'}, 'var_3': 'value_3'}
    fact_cache = {'host_1': {'fact_1': 'value_1'}, 'host_2': {'fact_2': 'value_2'}, 'fact_3': 'value_3'}
    vars = VariableManager(var_cache=var_cache, fact_cache=fact_cache).get_vars(host=None)

# Generated at 2022-06-13 17:23:35.168172
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    #
    # VariableManager.set_nonpersistent_facts() Test for functional testing
    #

    # setup test subject with a copy of the default config data
    config_data = copy.deepcopy(DEFAULT_CONFIG_DATA)

    # setup test subject with any other required args kwargs
    other_args = ()
    other_kwargs = dict()

    # create test subject
    test_subject = VariableManager(
        other_args, other_kwargs,
        config_data,
    )

    # create testing doubles:
    #   No doubles needed

    # define test data:
    #   No test data needed

    # perform the test:
    #   No test needed

    # validate the results:
    #   No validation needed

# Generated at 2022-06-13 17:23:37.823404
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    '''
    Unit test for method set_host_facts of class VariableManager
    '''
    v = VariableManager()
    v.set_host_facts('test', {'lol': 'lol'})
    assert True

# Generated at 2022-06-13 17:23:45.899741
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit tests for VariableManager class
    '''
    varmanager = VariableManager()
    test_vars = {'test_key': 'test_value'}
    varmanager._vars_cache = {'test_host': test_vars}
    varmanager.set_host_facts('test_host', test_vars)

    assert len(varmanager.get_vars(host=Host('test_host'))) == 3
    assert len(varmanager.get_vars(host=Host('test_host'), include_hostvars=True)) == 4
    assert len(varmanager.get_vars(host=Host('test_host'), include_delegate_to=False)) == 2


# Generated at 2022-06-13 17:23:52.343501
# Unit test for constructor of class VariableManager
def test_VariableManager():
    class DummyLoader(object):
        pass

    class DummyInventory(object):
        def __init__(self):
            self.hosts = {}
            self.groups = {}
            self.patterns = {}

        def get_groups(self, hostname):
            return self.hosts[hostname].groups

        def get_hosts(self, pattern="all", ignore_restrictions=False):
            return self.groups[pattern]

        def add_host(self, new_host):
            self.hosts[new_host.name] = new_host

        def add_pattern(self, name, pattern):
            self.patterns[name] = pattern

        def add_group(self, new_group):
            self.groups[new_group.name] = new_group


# Generated at 2022-06-13 17:25:30.685788
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    v = VarsWithSources({'a': 1, 'b': 2})
    v.sources = {'a': 'a_host_file', 'b': 'b_host_file'}
    assert v['a'] == 1
    assert v['b'] == 2
    assert v.get_source('a') == 'a_host_file'
    assert v.get_source('b') == 'b_host_file'

# Generated at 2022-06-13 17:25:36.567041
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.loader import add_plugin_dir
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.utils.display import Display

    # Set up the search path for the lookup plugin loader
    add_plugin_dir(os.path.join(os.path.dirname(__file__), 'lookup_plugins'))

    # Find the lookup plugin loader and make sure it's set up correctly
    loader = plugins.lookup_loader

# Generated at 2022-06-13 17:25:38.603386
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    display.debug = MagicMock()

    v = VarsWithSources({'foo': 'bar'}, {'foo': 'group_vars'})
    v.__getitem__('foo')

    display.debug.assert_called_once_with("variable 'foo' from source: group_vars")


# Generated at 2022-06-13 17:25:41.854749
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    vm = VariableManager()
    vm.set_host_facts('localhost', {'ansible_local': {'a': 'b'}})

# Generated at 2022-06-13 17:25:46.430466
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, MagicMock

    with patch.dict('sys.modules', {'ansible.module_utils.facts': MagicMock()}):
        _ansible_module_dummy = MagicMock()
        _ansible_module_dummy.display.debug = MagicMock()
        _ansible_module_dummy.display.verbosity = 1
        with patch.object(TaskExecutor, '__init__', return_value=None) as patched_init:
            patched_init.return_value = None
            global_cache = TaskExecutor()
            global_cache.display = _ansible_

# Generated at 2022-06-13 17:25:56.178579
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager.clear_host_cache()

    assert variable_manager.get_vars() == dict(), "The variable manager variable dict should be empty but is not"

    variable_manager.set_host_variable("host1", "var1", True)
    variable_manager.set_host_variable("host1", "var2", True)
    variable_manager.set_host_variable("host2", "var1", True)

    assert len(variable_manager.get_vars()) == 2, "The variable manager variable dict should have two (2) elements but does not"
    assert len(variable_manager.get_vars(host="host1")) == 1, "The variable manager variable dict should have one (1) element but does not"

# Generated at 2022-06-13 17:25:58.194148
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    variables = VarsWithSources({"foo": "bar"}, {"foo": "test_source"})
    assert variables["foo"] == "bar"


# Generated at 2022-06-13 17:26:00.056599
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    vm.set_nonpersistent_facts('foo','bar')
    assert vm._nonpersistent_fact_cache['foo'] == 'bar'

# Generated at 2022-06-13 17:26:01.356329
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Test variable manager get_vars method
    '''
    variable_manager = VariableManager()

# Generated at 2022-06-13 17:26:07.060156
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    # First, create an instance of VarsWithSources with a dict of data
    test_data = dict(a=1, b=2, c=3, d=4)
    test_inst = VarsWithSources.new_vars_with_sources(test_data, dict())
    for key, value in test_data.items():
        assert key in test_inst
        assert value == test_inst[key]


# Generated at 2022-06-13 17:27:56.156284
# Unit test for method __getitem__ of class VarsWithSources
def test_VarsWithSources___getitem__():
    set_module_args({
        'a': 1,
        'b': 2,
        'c': { 'd': 3, 'e': 4 },
        'sources': {
            'a': 'A',
            'b': 'B',
            'c': 'C',
        },
    })
    vars = module.vars_with_sources(
        dict(a=1, b=2, c=dict(d=3, e=4)),
        dict(a='A', b='B', c='C'),
    )
    assert vars['a'] == 1
    assert vars['b'] == 2
    assert vars['c']['d'] == 3
    assert vars['c']['e'] == 4



# Generated at 2022-06-13 17:28:06.836741
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    module = ansible.modules.test.test_var_manager.AnsibleModule(
        argument_spec = dict(
            host = dict(required=True, choices=['localhost'])
        )
    )

    play_context = ansible.playbook.play_context.PlayContext()
    play_context.network_os = 'junos'

    loader = DictDataLoader({'host_vars/localhost': '{ "ansible_network_os": "junos" }'})
    inventory = ansible.parsing.dataloader.DataLoader().load_from_file('localhost,')
    inventory.set_variable_manager(VariableManager())
