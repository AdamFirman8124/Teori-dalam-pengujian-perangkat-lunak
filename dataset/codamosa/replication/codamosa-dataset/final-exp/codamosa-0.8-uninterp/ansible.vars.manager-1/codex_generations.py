

# Generated at 2022-06-13 17:19:06.818460
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # create ansible object
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager._fact_cache['1.1.1.1'] = {'foo': 'bar'}
    variable_manager.set_host_variable('1.1.1.1', 'var', {'foo': 'bar'})
    variable_manager.set_host_variable('1.1.1.2', 'var', {'foo': 'bar'})


# Generated at 2022-06-13 17:19:14.749839
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()
    a = Host('a')
    setattr(a, 'vars', {'a': 'b'})
    v.set_nonpersistent_facts(a.name, a.vars)
    v.set_host_variable('a', 'c', 'd')
    v._vars_cache['a']['foo'] = "bar"
    h = v.get_vars(a, include_delegate_to=True)
    assert_equal(h['inventory_hostname'], a.name)
    assert_equal(h['a'], 'b')
    assert_equal(h['c'], 'd')
    assert_equal(h['foo'], 'bar')
    assert_equal(h['ansible_host'], a.name)

# Generated at 2022-06-13 17:19:20.807310
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.role.role_include
    vars_man = VariableManager()
    vars_man._inventory = 'an_inventory'
    vars_man._fact_cache = 'a_fact_cache'
    vars_man._vars_cache = 'a_vars_cache'
    vars_man._omit_token = 'an_omit_token'
    vars_man._extra_vars = 'extra_vars'
    vars_man._fact_extraction_cache = 'a_fact_extraction_cache'

# Generated at 2022-06-13 17:19:26.637508
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    from collections import Mapping
    from ansible.vars import VariableManager
    manager = VariableManager()
    manager.set_host_variable("testHost", "testVar", "testValue")
    assert isinstance(manager._vars_cache, Mapping)
    assert manager._vars_cache["testHost"] == {"testVar": "testValue"}

# Generated at 2022-06-13 17:19:32.840876
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))

    #
    #test get_vars with additional_context
    #

    test_vm = VariableManager(loader=DictDataLoader({}), inventory=Inventory(loader=DictDataLoader({})), version_info=C.DEFAULT_DEBUG)

    #test get_vars with special variables

# Generated at 2022-06-13 17:19:42.385159
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    def mock_init(self, loader, inventory, play_context=None, options_vars=None):
        '''
        mock for initializing VariableManager
        '''
        self._loader = loader
        self._inventory = inventory
        self._options_vars = options_vars
        self._omit_token = None
        self._hostvars = None
        self._fact_cache = dict()
        self._fact_progress_cache = dict()
        self._vars_cache = dict()
        self._nonpersistent_fact_cache = dict()

    def mock_getvars(self, play=None, host=None, task=None, include_delegate_to=False, include_hostvars=False,):
        '''
        mock for method get_vars of VariableManager
        '''

# Generated at 2022-06-13 17:19:48.556883
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    class Host:
        def __init__(self, name=''):
            self.name = name
    class VariableManager:
        def __init__(self, inventory=None):
            self._inventory = inventory 
            self._vars_cache = dict()
    class Inventory:
        def __init__(self):
            self._hosts = []
            self.hosts = []
            self.hosts_dict = dict()
            self._vars_per_host = dict()
            self.set_variable('1', {'1': '1'})
            self.set_variable('2', {'2': '2'})

        def set_variable(self, host, var_dict):
            self._vars_per_host[host] = var_dict
            self.hosts.append(host)
            host_

# Generated at 2022-06-13 17:19:58.558296
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Clear any cached or persisted variables from previous tests
    cache = 'tests/unit/test_variable_manager/ansible_local.yml'
    try:
        os.unlink(cache)
    except OSError:
        pass

    # Test with empty inventory:
    vm = VariableManager()
    vm.hostvars = dict()
    assert not vm.hostvars
    # Test with no inventory
    vm = VariableManager(loader=DictDataLoader({}))
    vm.hostvars = dict()
    assert not vm.hostvars
    # Test with no host in inventory
    vm = VariableManager(loader=DictDataLoader({'all': {'vars': {'foo': 'bar'}}}))
    vm.hostvars = dict()
    assert not vm.hostvars
    # Test with host

# Generated at 2022-06-13 17:20:06.632393
# Unit test for constructor of class VariableManager
def test_VariableManager():

    # devel/test/vars/test_play_vars
    path = os.path.join(os.path.dirname(__file__), "vars", "play_vars")
    play_vars = {
        'role_var1': '1_override_role_var1',
        'role_var2': '1_override_role_var2',
        'role_var3': '1_remove_role_var3',
        'host_var': '1_override_host_var',
        'task_var': '1_override_task_var',
        'extra_var': '1_extra_var'
    }

    # devel/test/vars/test_play_vars

# Generated at 2022-06-13 17:20:12.849509
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    import ansible.inventory.manager
    from ansible.inventory.host import Host

    class VariableManagerTest(unittest.TestCase):

        def test_default_vars(self):
            '''Make sure default vars are always present'''

            mock_play = MagicMock()
            mock_play.get_name.return_value = 'test_play'

            mock_task = MagicMock()
            mock_task._role = None
            mock_task.loop = None
            mock_task.action = 'setup'

            v = VariableManager(loader=DictDataLoader({}))
            initial_vars = v.get_vars()
            # This is the common set of things that are set by default. If this changes, ensure that
            # the changes are accounted for in the test below

# Generated at 2022-06-13 17:20:49.676725
# Unit test for constructor of class VariableManager
def test_VariableManager():
    vm = VariableManager()
    assert isinstance(vm, VariableManager)
    assert vm._options_vars is not None


# Generated at 2022-06-13 17:20:59.748860
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class VariableManager
    '''

    # Variables defined here will be imported from the main module
    # This will fail if an import statement is added to the main module
    import ansible.plugins.loader
    import ansible.plugins.test.test_vars_plugins.v1
    import ansible.plugins.test.test_vars_plugins.v2
    import ansible.plugins.vars.host_group_vars

    # Define the test structure here

    # create an instance of the class PluginLoader, which by loading the vars_plugins
    # declared in the directory ansible.plugins.vars

# Generated at 2022-06-13 17:21:08.087975
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible import constants
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible import context
    from ansible.vars.reserved import Reserved
    from ansible.utils.vars import combine_vars
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.vars.collection_loader import AnsibleCollectionConfig
    from ansible.vars.collection_loader import AnsibleCollectionRef
    from ansible.vars.collection_loader import AnsibleCollectionRequirement

# Generated at 2022-06-13 17:21:10.129002
# Unit test for constructor of class VariableManager
def test_VariableManager():
    """
    Test if variable manager can be constructed.
    """
    variable_manager = VariableManager()
    variable_manager.__repr__()


# Generated at 2022-06-13 17:21:15.885933
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    
    vm = VariableManager()
    
    # TBD: test coverage
    # TBD: changing a local var changes the dict?
    # TBD: changing the dict changes the local var?
    # TBD: merging the dict with a local var doesn't change the dict keys?
    
    assert(True)
 
# Unit test execution
if __name__ == "__main__":
    test_VariableManager_get_vars()
 
# vim: sts=4 sw=4 ts=4 et ft=python

# Generated at 2022-06-13 17:21:18.526480
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# The code below is used to generate the ArgumentSpec object
# This object is used to generate the docs in the auto API documentation

# Generated at 2022-06-13 17:21:26.709076
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Create a mock inventory object
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory_manager = InventoryManager(loader=DataLoader(), sources='localhost,')

    # Create a mock playbook object
    from ansible.playbook.play import Play
    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': []
    }, variable_manager=VariableManager(loader=DataLoader(), inventory=inventory_manager), loader=DataLoader())

    # Create a mock task object
    from ansible.playbook.task import Task
    task = Task()

    # Create a mock role object

# Generated at 2022-06-13 17:21:28.484444
# Unit test for constructor of class VariableManager
def test_VariableManager():
    vm = VariableManager(loader=None, inventory=Inventory(host_list=[]), version_info=__version__)
    assert isinstance(vm, VariableManager)



# Generated at 2022-06-13 17:21:34.565996
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Making this a list so we can modify it later
    play_context = PlayContext()
    inventory = InventoryManager(loader=DataLoader())
    host = Host(name="host")
    # This is not a proper task, but most fields are irrelevant to this method
    task = Task()

    # Testing the path that throws an error
    try:
        VariableManager(loader=DataLoader(), inventory=inventory, use_cache=False).get_vars()
    except AnsibleError:
        pass
    else:
        assert False, "VariableManager.get_vars should have thrown an AnsibleError"

    # Testing the default path
    # Note: This will not contain the 'role_names' variable

# Generated at 2022-06-13 17:21:44.421618
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    def test_task_vars(self):
        # type: (unittest.TestCase) -> None
        task = MagicMock()
        task._role = self.role1
        task._ds = dict(name='task', remote_user='bob')

        self.variable_manager.set_host_variable(host='host1', varname='var', value='abcd')
        self.variable_manager.set_host_variable(host='host1', varname='var2', value='foo')
        self.variable_manager.set_host_variable(host='host2', varname='var2', value='bar')

        vars_copy = self.variable_manager._fact_cache.copy()

        self.variable_manager.set_nonpersistent_facts('host1', {'asdf': 'abc123'})


# Generated at 2022-06-13 17:22:45.795786
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    vm = VariableManager()
    play = Play()
    host = Host()

    # if all args are None, we want to return an empty dict.
    assert vm.get_vars(host, play) == {}

    # if only host is set, we want to get the variables for that host
    vm = VariableManager()
    host_vars = {'var1': 'value1', 'var2': 'value2'}
    vm.set_host_variable(host, 'var1', 'value1')
    vm.set_host_variable(host, 'var2', 'value2')

    host_vars_from_vm = vm.get_vars(host)
    assert host_vars == host_vars_from_vm

    # if only play is set, we want to get the variables for that play

# Generated at 2022-06-13 17:22:53.736858
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.facts import FactManager

    # VariableManager(inventory=None, *args, **kwargs)
    # inventory
    inventory_manager = InventoryManager([])
    variable_manager = VariableManager(inventory=inventory_manager)
    assert variable_manager.inventory == inventory_manager
    assert variable_manager._vars_cache == dict()
    assert variable_manager._hostvars == HostVars(variable_manager)
    assert variable_manager._fact_manager == FactManager(variable_manager)
    assert variable_manager._omit_token == '__omit_place_holder__'

    # inventory : None
    variable_manager = VariableManager()

# Generated at 2022-06-13 17:22:55.764311
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # FIXME: Unit test this method
    pass



# Generated at 2022-06-13 17:23:03.549612
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    my_mapper = lambda a: a
    my_tm = TaskExecutor

    # Initialization
    fake_loader = DictDataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='localhost,')
    vm = VariableManager(loader=fake_loader, inventory=fake_inventory)

    facts_dict = {'test': 't1'}

    # Test with a new host
    vm.set_nonpersistent_facts('new_host', facts_dict)
    assert vm._nonpersistent_fact_cache['new_host'] == facts_dict

    # Test with an existing host
    facts_dict = {'test_dict': {'test_key': 't2'}}
    vm.set_nonpersistent_facts('new_host', facts_dict)
    assert vm._nonpersistent_fact

# Generated at 2022-06-13 17:23:09.396597
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # set_host_facts(self, host, facts) -> None
    # Sets or updates the given facts for a host
    manager = VariableManager()
    host = 'example.org'
    facts = {'ansible_distribution': 'CentOS', 'ansible_distribution_version': '7.2.1511'}

    manager.set_host_facts(host, facts)

    assert manager.get_facts(host) == facts


# Generated at 2022-06-13 17:23:15.792834
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class VariableManager
    '''

    # Create an instance of a plugin
    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._vars_cache = dict()
    variable_manager._nonpersistent_fact_cache = dict()

    # Test variables
    inventory = dict()
    play = dict()
    host = dict()
    task = dict()
    loader = dict()
    inventory_manager = dict()
    variable_manager._loader = loader

    # Invoke method
    vars = variable_manager.get_vars(inventory=inventory, play=play, host=host, task=task, include_delegate_to=False, include_hostvars=True)

    # Test assertions
    
    # Return value assertions


# Generated at 2022-06-13 17:23:24.237863
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    assert vm.get_host_vars('host') == {}
    vm.set_nonpersistent_facts('host', {'a': 'test'})
    assert vm.get_host_vars('host') == {'a': 'test'}
    vm.set_nonpersistent_facts('host', {'b': 'test'})
    assert vm.get_host_vars('host') == {'a': 'test', 'b': 'test'}
    vm.set_nonpersistent_facts('host', {'a': 'test2'})
    assert vm.get_host_vars('host') == {'a': 'test2', 'b': 'test'}



# Generated at 2022-06-13 17:23:28.840302
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variable_manager.options_vars = None
    variable_manager.hostvars = None
    variable_manager.omit_token = 'OMIT'
    variable_manager._options_vars = {}
    variable_manager._inventory = None
    variable_manager.get_vars(host, task, play, include_hostvars, include_delegate_to)

# Generated at 2022-06-13 17:23:34.202937
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    host_vars = {}
    host_vars['testhost'] = {'var1': 'value1', 'var2': 'value2'}
    host_vars['testhost2'] = {'var1': 'value3', 'var2': 'value4'}
    return VariableManager(host_vars=host_vars)




# Generated at 2022-06-13 17:23:37.461037
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    facts = {'fact1':1, 'fact2':2}
    hostname = 'localhost'
    vm.set_nonpersistent_facts(hostname, facts)
    facts_dict = vm._nonpersistent_fact_cache
    assert facts_dict['localhost'] == facts

# Generated at 2022-06-13 17:25:27.879934
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    for i in range (0, 10):
        # Define the arguments that would be sent to the function
        var_manager = VariableManager()
        host = 'localhost'
        play = None
        include_hostvars = False
        include_delegate_to = False
        # Call the function under test
        result = var_manager.get_vars(host=host, play=play, include_hostvars=include_hostvars,include_delegate_to=include_delegate_to)
        # Check the results
        if result != {}:
            return False
    return True


# Generated at 2022-06-13 17:25:37.914595
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for VariableManager class method get_vars
    '''
    mock_inventory = MagicMock()
    mock_loader = MagicMock()
    mock_loader.get_basedir = MagicMock()
    mock_loader.get_basedir.return_value = None
    mock_loader.path_dwim = MagicMock()
    mock_loader.path_dwim.return_value = None
    mock_play = MagicMock()
    mock_play.get_hosts = MagicMock()
    mock_play.get_hosts.return_value = None
    mock_task = MagicMock()
    mock_task.get_search_path = MagicMock()
    mock_task.get_search_path.return_value = None

    vars_manager = VariableManager()


# Generated at 2022-06-13 17:25:41.737345
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for ansible.vars.VariableManager.get_vars()
    '''
# TODO: add tests later

# Test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:25:46.593327
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    source = """
        provider:
            name: foo
            class: foo
    """
    data = yaml.safe_load(source)
    data = {'property1':data}
    v2 = VariableManager()
    v2._vars_cache['hostname'] = data
    v2._vars_cache.update(data)
    #print(v2._vars_cache)

    vars = v2.get_vars(include_hostvars=True)
    #print(vars)


# Generated at 2022-06-13 17:25:56.247265
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class VariableManager
    '''
    # Create a mock for the class Options.
    options = mock.MagicMock(spec=Options)

    # Create a mock for the class Inventory.
    inventory = mock.MagicMock(spec=Inventory)

    # Create a variable manager.
    variable_manager = VariableManager(loader=None, inventory=inventory, variable_manager=None)
    variable_manager._options_vars = {}
    variable_manager._fact_cache = {}
    variable_manager._nonpersistent_fact_cache = {}
    variable_manager._vars_cache = {}
    variable_manager._hostvars = {}
    variable_manager._omit_token = '__omit_place_holder__'

    # Create a mock for the class PlayContext.
   

# Generated at 2022-06-13 17:25:58.862873
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    fake_host = object()
    fake_facts = object()
    vm = VariableManager()
    vm.set_nonpersistent_facts(fake_host, fake_facts)
    assert vm._nonpersistent_fact_cache.get(fake_host) == fake_facts

# Generated at 2022-06-13 17:26:08.161932
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Testing variable manager call
    # Required parameters
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars
    # to provide inventory object
    host_name = 'localhost'

# Generated at 2022-06-13 17:26:12.151268
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(None, None)
    variable_manager.set_nonpersistent_facts(None, None)
    variable_manager.set_host_facts(None, None)
    variable_manager.set_host_facts(None, None)
    variable_manager.set_host_variable(None, None, None)
    variable_manager.set_host_facts(None, None)
test_VariableManager_get_vars()


# Generated at 2022-06-13 17:26:21.056731
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class VariableManager
    '''
    args = ansible.module_utils.basic.AnsibleModule.parse_args(sys.argv)[2]
    options_vars_dict = {}
    option_var_names = [
        'options',
        'options_dict',
        'options_value',
        'options_dict_value'
    ]
    for name in option_var_names:
        options_vars_dict[name] = getattr(args, name)

    default_vars = VariableManager()
    default_vars.extra_vars = VariableManager.get_unbound_variable('extra_vars')
    default_vars._extra_vars = VariableManager.get_unbound_variable('_extra_vars')
    default_

# Generated at 2022-06-13 17:26:23.634629
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Call the method
    # Set the Variables
    # Check the value
    get_vars()