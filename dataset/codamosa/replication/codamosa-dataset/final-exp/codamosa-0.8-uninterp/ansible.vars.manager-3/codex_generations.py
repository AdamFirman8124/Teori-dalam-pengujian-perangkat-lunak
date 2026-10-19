

# Generated at 2022-06-13 17:18:56.784514
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # test using a real loader
    loader = DataLoader()
    inventory = Inventory(loader=loader, host_list=[])
    host_variable_manager = VariableManager(loader=loader, inventory=inventory)

    # test using null vars
    null_variable_manager = VariableManager(loader=loader, inventory=inventory)

    # test using a host with an address
    host = Host(name="test_host")
    host.address = "127.0.0.1"
    host_with_address_variable_manager = VariableManager(loader=loader, inventory=inventory)

    # test using a host with a custom vars
    host_with_custom_vars = Host(name="custom_host")
    host_with_custom_vars.set_variable("test_var", "test_value")
    host_with_custom_v

# Generated at 2022-06-13 17:19:05.681891
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    facts_expected = {'foo':'bar'}
    facts_real = {'foo':'bar'}
    dict_len_expected = 1
    dict_len_real = 0
    #Case 1:
    #Initialize
    v = VariableManager()
    #Execute
    v.set_nonpersistent_facts('127.0.0.1', facts_real)
    #Verify
    dict_len_real = len(v._nonpersistent_fact_cache)
    assert dict_len_expected == dict_len_real, "Expected len is {0} and real len is {1}".format(dict_len_expected, dict_len_real)
    facts_real = v._nonpersistent_fact_cache['127.0.0.1']

# Generated at 2022-06-13 17:19:11.062205
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    o = VariableManager()
    host = 'my_host'
    facts = {'foo': 'bar'}

    o.set_nonpersistent_facts(host=host, facts=facts)
    assert o.get_nonpersistent_facts(host=host, refresh=False) == facts

    # Test invalid facts
    try:
        o.set_nonpersistent_facts(host=host, facts=['invalid'])
    except AnsibleAssertionError:
        pass
    else:
        assert False, 'AnsibleAssertionError not raised'



# Generated at 2022-06-13 17:19:22.987889
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources='test/test_playbooks/hosts')
    variable_manager = VariableManager(loader=loader, inventory=inv)
    host = inv.get_host('jumper')
    variable_manager.set_host_variable(host=host, varname='ansible_ssh_host', value='127.0.0.1')
    variable_manager.set_host_variable(host=host, varname='ansible_ssh_port', value='321')

    variable_manager.set_host_variable(host=host, varname='ansible_ssh_host', value='127.0.0.1')
    variable_manager.set_host

# Generated at 2022-06-13 17:19:30.939950
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude
    from units.mock.inventory import MockInventory
    from ansible.vars.hostvars import HostVars
    from ansible.playbook.role import Role

    vm = VariableManager()

    # creating a task with a single role dependency
    data = {
        "name": "test",
        "hosts": "all",
        "roles": [
            "test"
        ]
    }

# Generated at 2022-06-13 17:19:37.213565
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager._fact_cache['127.0.0.1'] = {'ansible_version': {'full': '2.0.2.0', 'major': 2, 'minor': 0, 'revision': 2, 'string': '2.0.2.0'}}

# Generated at 2022-06-13 17:19:41.670465
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    facts = {'foo': 'bar'}
    # wrong type
    #vm.set_nonpersistent_facts(host='hostname', facts='foo')
    # update the existing facts
    vm.set_nonpersistent_facts(host='hostname', facts=facts)
    vm.set_nonpersistent_facts(host='hostname', facts=facts)



# Generated at 2022-06-13 17:19:50.784739
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # Input data for this unit test
    # We expect to get back a new updated instance of VariableManager
    mock_host = 'someserver.somesite.somewhere'
    mock_facts = [{'mock_fact': 'mock_fact_value'}]

    # Perform the test and get back the results
    vm = VariableManager()
    vm.set_nonpersistent_facts(mock_host, mock_facts)

    # Now do our assertions
    assert vm._nonpersistent_fact_cache is not None
    assert vm._nonpersistent_fact_cache[mock_host]['mock_fact'] == 'mock_fact_value'


# Generated at 2022-06-13 17:20:00.670709
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # Test signature of init
    debug_mocking = None
    if os.environ.get('ANSIBLE_DEBUG') is not None:
        debug_mocking = True
    elif C.DEFAULT_DEBUG:
        debug_mocking = True

    vm = VariableManager(loader=MagicMock(), inventory=MagicMock(), use_task_vars=False)
    assert isinstance(vm, VariableManager)
    assert isinstance(vm._fact_cache, FactCache)
    assert vm._use_task_vars is False
    assert vm._options_vars['ansible_debug'] == debug_mocking
    assert vm._priorities == {}
    assert vm._hosts_cache == {}
    assert vm._hostvars == {}
    assert vm._vars_cache == {}
    assert vm._nonpersistent_fact

# Generated at 2022-06-13 17:20:08.359395
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    playbook_vars = dict()
    options_vars = dict()
    direct_vars = dict()
    extra_vars = dict()
    inventory = MagicMock()
    loader = MagicMock()
    vm = VariableManager(loader=loader, inventory=inventory,
            extra_vars=extra_vars, options_vars=options_vars,
            direct_vars=direct_vars, playbook_vars=playbook_vars)
    vm.set_host_variable('test-host', 'test-varname', 'test-varname-value')
    assert(vm._vars_cache['test-host']['test-varname'] == 'test-varname-value')

# Tests for method set_nonpersistent_facts of class VariableManager

# Generated at 2022-06-13 17:20:33.710358
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Create VariableManager argument
    vm_to_set_host_facts_arg = VariableManager()

    vm_to_set_host_facts_arg._fact_cache = dict()

    # Call set_host_facts
    vm_to_set_host_facts_arg.set_host_facts("host", {"a": "b"})

    # Verify _fact_cache
    assert vm_to_set_host_facts_arg._fact_cache == {"host": {"a": "b"}}


# Generated at 2022-06-13 17:20:41.349448
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    variableManager = VariableManager()
    variableManager.set_host_variable('host1', 'var1', 'value1')
    variableManager.set_host_variable('host2', 'var2', 'value2')
    assert variableManager._vars_cache is not None
    assert 'host1' in variableManager._vars_cache
    assert 'host2' in variableManager._vars_cache
    assert 'var1' in variableManager._vars_cache['host1']
    assert 'var2' in variableManager._vars_cache['host2']
    assert variableManager._vars_cache['host1']['var1'] == 'value1'
    assert variableManager._vars_cache['host2']['var2'] == 'value2'


# Generated at 2022-06-13 17:20:50.276191
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Setup a task so that we can set the base context and search path of a lookup
    task = Task()
    task.action = 'template'
    task.args = dict(src='{{ item }}.j2', dest='/tmp/{{ item }}')

    # Create a host and add it to the inventory
    host = Host(name='localhost')
    inventory = InventoryManager(loader=DataLoader())
    inventory.add_host(host, 'all')

    # Create the variable manager
    vars_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    # Create a play context, which is needed for the inventory.get_host
    play_context = PlayContext()
    play_context.network_os = 'default'

    # Create a temporary file which will be created by a lookup plugin
    temp_file = tempfile.Named

# Generated at 2022-06-13 17:21:00.170978
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:21:00.774434
# Unit test for constructor of class VariableManager
def test_VariableManager():
    assert VariableManager()

# Generated at 2022-06-13 17:21:08.955199
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    args = dict(
        inventory=dict(
            hosts='localhost',
            group_vars=dict(
                all=dict(
                    group_var_1='group_var_1_value',
                    group_var_2='group_var_2_value'
                )
            )
        ),
        loader=dict(
            class_name='TestCollectionIncludeOne',
            options_vars=dict(
                foo='bar'
            ),
            path_file='path/file',
            search_paths=['search_paths1', 'search_paths2']
        ),
        include_hostvars=False
    )

    vars_manager = VariableManager()
    vars = vars_manager.get_vars(**args)


# Generated at 2022-06-13 17:21:15.079572
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    inventory = InventoryManager(loader=None, sources='localhost,')
    host = inventory.get_host(host_name='localhost')
    play = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'user': 'test_user',
        'connection': 'local',
        'gather_facts': 'no',
        'tasks': [
            {'action': {'module': 'shell', 'args': 'ls'}}
        ]
    }, loader=DataLoader(), variable_manager=None)
    # play.set_loader(DataLoader())
    tqm = None
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    task = play.tasks[0]
    # def get_vars(self, play=None,

# Generated at 2022-06-13 17:21:19.528999
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vm = VariableManager()
    vm.set_host_variable(host='tst_host', varname='tst_varname', value='tst_value')
    
assert vm._vars_cache['tst_host']['tst_varname'] == 'tst_value'



# Generated at 2022-06-13 17:21:21.973890
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # TODO: add test here
    raise NotImplementedError('Test is not implemented yet.')

if __name__ == '__main__':
    run_test(VariableManager)

# Generated at 2022-06-13 17:21:29.211862
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:22:20.412109
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from collections import defaultdict
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars

    variable_manager = VariableManager()

    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.set_inventory(inventory=None)
    variable_manager.set_nonpersistent_facts(host='foo', facts={'foo': 'bar'})
    variable_manager.get_vars(play=None, task=None, include_delegate_to=False, include_hostvars=False)
    variable_manager.add_or_update_vars(host='foo', variables={'foo': 'bar'})

# Generated at 2022-06-13 17:22:23.397816
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()
    assert variable_manager.get_vars(host=Host('hostname'), include_hostvars=False) == dict()


#Tests for method get_vars() of class VariableManager


# Generated at 2022-06-13 17:22:30.151444
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class ansible.vars.VariableManager
    '''
    from ansible.template.safe_eval import safe_eval
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.play import Play
    from ansible.errors import AnsibleLookupError, AnsibleTemplateError
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor

# Generated at 2022-06-13 17:22:39.320666
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # TODO skip test if memory_cache is not installed or if we are loading from the database
    # Create mocks needed for execute
    x, loader, templar = mocks.mock_everything()

    # Create a test instance of PlaybookExecutor
    host, play = mocks.mock_inventory_and_play(loader)
    mock_variable_manager = VariableManager(loader=loader, inventory=x.inventory, check_hostvars=True)
    mock_variable_manager.clear_facts(host.name)

    # Prove that we have no facts
    facts = mock_variable_manager.get_host_facts(host=host)
    assert not facts

    # Set the facts

# Generated at 2022-06-13 17:22:42.877260
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Pass empty data
    host = {}
    facts = {}
    v = VariableManager()
    v.set_host_facts(host, facts)
    # We got here, no exception was raised
    assert True

# Generated at 2022-06-13 17:22:44.626121
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    my_obj = VariableManager()
    host = '127.0.0.2'
    facts = {}
    # Call method
    result = my_obj.set_host_facts(host, facts)
    assert result is None

# Generated at 2022-06-13 17:22:52.502940
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    '''
    Unit test for method set_host_variable of class VariableManager
    '''

    # Create a VariableManager object
    argument_spec = dict()
    argument_spec['_options_vars'] = dict(type='dict')
    argument_spec['loader'] = dict(type='object')
    argument_spec['inventory'] = dict(type='object')
    variable_manager = VariableManager(argument_spec)
    variable_manager._vars_cache['localhost'] = dict()
    variable_manager._vars_cache['localhost']['key1'] = 'value1'
    variable_manager._vars_cache['localhost']['key2'] = 'value2'
    variable_manager._vars_cache['localhost']['key3'] = dict()

# Generated at 2022-06-13 17:22:54.334863
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass



# Generated at 2022-06-13 17:23:02.861709
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    obj = VariableManager()
    # wrong_type_args will fail the type coercion.
    wrong_type_args = [
        (None,),
        (1,),
        (1.1,),
        (u'unicode_str',),
        (Exception(),),
        (1j,),
        (['a', 'list'],),
        (('a', 'tuple'),),
        ({'a': 'dict'},),
        (object(),),
    ]
    for arg in wrong_type_args:
        try:
            obj.set_host_variable(*arg)
        except TypeError as e:
            pass
        except Exception as e:
            print('Unexpected exception raised: {0}'.format(e))
        else:
            raise TypeError('ExpectedTypeError not raised')

    # args_

# Generated at 2022-06-13 17:23:09.046328
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    variable_manager = VariableManager()
    variable_manager._nonpersistent_fact_cache = {'foo': {'key': 'old_value'}}
    variable_manager.set_nonpersistent_facts('foo', {'key': 'new_value'})
    assert variable_manager._nonpersistent_fact_cache == {'foo': {'key': 'new_value'}}

# Generated at 2022-06-13 17:23:40.617219
# Unit test for constructor of class VariableManager
def test_VariableManager():
    '''
    Unit test for constructor of class VariableManager
    '''
    # test without inventory argument
    vm = VariableManager()
    assert not vm._inventory
    # test with inventory argument
    inv = InventoryManager(loader=DataLoader())
    vm2 = VariableManager(inventory=inv)
    assert inv == vm2._inventory
    # test with additional_arguments
    extra_vars = dict(hello='world')
    vm3 = VariableManager(loader=DataLoader(), inventory=inv, variables=extra_vars)
    assert vm3.extra_vars == extra_vars
    # test with options
    vm4 = VariableManager(loader=DataLoader(), inventory=inv, options=dict(
        hello='world',
        vault_password='password'
    ))
    assert 'ansible_vault_pass' not in vm4

# Generated at 2022-06-13 17:23:46.207304
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:23:47.797306
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vm = VariableManager()
    vm.set_host_variable({}, 'key', 'value')
    assert vm._vars_cache == {}
test_VariableManager_set_host_variable()


# Generated at 2022-06-13 17:23:49.013287
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager(loader=None, inventory=None)
    assert variable_manager is not None

# Generated at 2022-06-13 17:23:54.892920
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    varmgr = VariableManager(loader=None, inventory=None)
    play = Play()
    play.vars = {'a': 'a_value'}
    play.dep_chain = []

    play.roles.append(Role(name="role_one"))
    play.roles.append(Role(name="role_two"))

    task = Task(vars={'role_one': {'b': 'b_value'}})
    task._role = play.roles[0]
    task.action = ActionModule(module_name="test", module_args={})
    task.dep_chain = []
    result = varmgr.get_vars(play=play, host=None, task=task)
    assert(result['a'] == 'a_value')

# Generated at 2022-06-13 17:24:02.395434
# Unit test for constructor of class VariableManager
def test_VariableManager():

    def _test_load_kwarg(arg_name, **kwargs):
        # Test that the VariableManager constructor correctly handles the load
        # kwarg, and that the load kwarg can be passed in using various names.
        simple_test_params = {
            'test1': 'test1',
            'test2': 'test2'
        }
        simple_test_inventory = Inventory("localhost")
        if arg_name is not None:
            kwargs[arg_name] = False
        v = VariableManager(loader=DataLoader(), inventory=simple_test_inventory,
                            extra_vars=simple_test_params, **kwargs)
        assert simple_test_params == v.extra_vars
        assert simple_test_params == v.get_vars(play=None, host=None)

# Generated at 2022-06-13 17:24:07.811269
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Test object created
    '''
    # Test input value

# Generated at 2022-06-13 17:24:14.586482
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Check if it can set the given facts for a host in the fact cache
    # host and facts given should be of type Mapping
    vm = VariableManager()
    class facts(object):
        def __init__(self):
            self.fqdn = 'localhost'
    host = 'example'
    facts = facts()
    vm.set_host_facts(host, facts)
    assert vm._fact_cache[host].fqdn == 'localhost'


# Generated at 2022-06-13 17:24:19.586037
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    # Test setting a variable for a host,
    # first use a Host object and then string
    for host in [Host('hostname'), 'hostname']:
        vmanager = VariableManager(loader=DictDataLoader())
        vmanager.set_host_variable(host, 'test', 'success')
        assert vmanager._vars_cache['hostname']['test'] == 'success'
        print('PASS: VariableManager set_host_variable, Host')

# Generated at 2022-06-13 17:24:28.405868
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    var_mgr = VariableManager()

    # Set a non-dict value for a host's variable
    host = 'host 1'
    varname = 'varname'
    value = 'value'
    var_mgr.set_host_variable(host, varname, value)

    # You can overwrite the value with a different value
    new_value = 'new_value'
    var_mgr.set_host_variable(host, varname, new_value)

    # You are unable to overwrite the value with a dict
    bad_value = {'key': 'value'}
    with pytest.raises(AnsibleAssertionError):
        var_mgr.set_host_variable(host, varname, bad_value)

    # Set a dict value for a host's variable
    host = 'host 2'

# Generated at 2022-06-13 17:25:37.440755
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    print("Testing VariableManager.get_vars")
    # initialize vars for host
    vars_dict = {
        'var1': 'one',
        'var2': 'two',
        'var3': 'three'
    }
    mock_variable_manager = MagicMock(VariableManager)
    mock_variable_manager.get_vars.return_value = vars_dict
    # initialize variable_manager instance
    variable_manager = mock_variable_manager
    # initialize host
    host = Host('host1')
    host.set_variable('host_var', 'host_host_var')
    vars_dict.update({'host_var': 'host_host_var'})
    # validate that get_vars() returns host variable dictionary

# Generated at 2022-06-13 17:25:37.997997
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# Generated at 2022-06-13 17:25:46.482153
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Testing the method VariableManager.get_vars
    # Test with following arguments:
    # host=None, play=None, include_delegate_to=True, include_hostvars=False
    # host=None, play=None, include_delegate_to=False, include_hostvars=True
    # host=None, play=None, include_delegate_to=False, include_hostvars=False
    # host=None, play=None, include_delegate_to=True, include_hostvars=True
    # host=None, play=None, include_delegate_to=True, include_hostvars=False
    # host=None, play=None, include_delegate_to=False, include_hostvars=False
    pass


# Generated at 2022-06-13 17:25:56.212758
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """ Test that get_vars returns the correct data structure. """

    vm = VariableManager()
    assert vm.get_vars(host=None, play=None, task=None, include_delegate_to=True, include_hostvars=True) == {'omit': '__omit_place_holder__'}
    assert vm.get_vars(host=None, play=None, task=None, include_delegate_to=False, include_hostvars=False) == {'omit': '__omit_place_holder__'}
    assert vm.get_vars(host=None, play=None, task=None, include_delegate_to=True, include_hostvars=False) == {'omit': '__omit_place_holder__'}
    assert vm.get_vars

# Generated at 2022-06-13 17:26:03.111090
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    import pytest
    import sys

    with pytest.raises(AnsibleAssertionError) as excinfo:
        vars_manager = VariableManager()
        loader = DataLoader()
        inventory = InventoryManager('/etc/ansible/hosts')

# Generated at 2022-06-13 17:26:08.279180
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    """
    Unit tests for set_host_variable() method
    """

    host = 'host_1'
    varname = 'varname'

    value = 'value'

    vm = VariableManager(loader=None, inventory=None)

    # Case:1
    vm.set_host_variable(host, varname, value)

    assert vm._vars_cache[host][varname] == value

    # Case:2
    vm._vars_cache[host] = {varname: value}

    vm.set_host_variable(host, varname, value)

    assert vm._vars_cache[host] == {varname: value}

    # Case:3
    value1 = 'value1'
    value2 = 'value2'


# Generated at 2022-06-13 17:26:10.477582
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    inven = Inventory(host_list='')
    vm = VariableManager(loader=None, inventory=inven)
    assert isinstance(vm, VariableManager)

# Generated at 2022-06-13 17:26:19.695199
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    from collections import MutableMapping
    from ansible import context
    from ansible.vars.manager import VariableManager
    from ansible.vars.facts import Facts

    host = '127.0.0.1'
    varname = 'testVar'
    value = 'testValue'
    varManager = VariableManager()

    # test with not exist var
    varManager.set_host_variable(host, varname, value)
    assert varManager._vars_cache[host][varname] == value

    # test when vars_cache[host][varname] is a MutableMapping
    value = {'testKey': 'testValue'}
    varManager._vars_cache[host][varname] = value
    varManager.set_host_variable(host, varname, value)
    assert var

# Generated at 2022-06-13 17:26:25.296297
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    inventory = Inventory()
    loader = DictDataLoader(dict())
    variable_manager = VariableManager(inventory=inventory, loader=loader)
    # return values are checked in the loop body

# Generated at 2022-06-13 17:26:29.353506
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    # Testing for method set_host_variable
    # Using default arguments
    VariableManager_obj = VariableManager(loader=None, inventory=None)
    if not isinstance(VariableManager_obj, VariableManager):
        raise AssertionError