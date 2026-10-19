

# Generated at 2022-06-13 17:18:54.069116
# Unit test for constructor of class VariableManager
def test_VariableManager():
    v = VariableManager()
    assert v is not None

# Generated at 2022-06-13 17:19:04.154253
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    import random
    import string
    import time
    import pytest
    from unittest.mock import patch

    from ansible import constants as C
    from ansible.module_utils.six import PY3, text_type
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils._text import to_bytes

    from ansible.plugins.loader import vars_loader

    assert callable(VariableManager)

    # Set #1
    spec = dict(
        loader=dict(
            type='object',
        ),
        inventory=dict(
            type='object',
        ),
    )

    is_valid, errors = validate_spec(spec, VariableManager._argument_spec)
    assert not errors
    assert is_valid


# Generated at 2022-06-13 17:19:13.379881
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """ Host variables are returned in a dictionary structure.
        This dictionary is used for templating for the play.
    """
    # The code below is used to test the function get_vars from the class VariableManager
    # The code was taken from: file ansible/executor/task_executor.py, version 2.4.0.0
    # The values for the variables were hard-coded in the function,
    # and were changed to test different options of the function.
    # The list of values used here:
    #   vars_copy                          - a copy of the variable dictionary,
    #                                        where we store the values of 'host' and 'hostvars'
    #   variable                           - the variable name
    #   value                              - the variable value
    #   variables                          - the variable dictionary,
    #                                        where we

# Generated at 2022-06-13 17:19:25.712007
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    loader = DataLoader()
    reserved_d = Reserved()
    reserved_d.update(loader.load_from_file(C.DEFAULT_RESERVED_VARS_PATH))
    variable_manager = VariableManager(loader=loader, inventory=InventoryManager(loader=loader, sources=[]),
                                       version_info={"ansible_version": {"full": "2.9.9"}})

# Generated at 2022-06-13 17:19:32.438768
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader

    data = '''
    host_specific_vars:
      foo:
        - a
        - b
        - c
      host_specific_list:
        - 2
        - 3
        - 4
      host_specific_var: myvar
    '''
    dataloader = DataLoader()
    test_var_manager = VariableManager(loader=dataloader)
    ansible_vars = test_var_manager.get_vars(
        play=None,
        host=None,
        task=None,
        include_delegate_to=False,
        use_cache=False,
        include_hostvars=False,
    )



# Generated at 2022-06-13 17:19:33.668545
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    assert True

# Generated at 2022-06-13 17:19:38.403069
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vm = VariableManager()
    host = "test_host"
    varname = "test_varname"
    value = "test_value"

    vm.set_host_variable(host, varname, value)
    assert(vm._vars_cache[host][varname]==value)



# Generated at 2022-06-13 17:19:51.549220
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Testing: vars variable expansion.
    inventory = Inventory('tests/inventory')
    # Get host by name.
    host = inventory.get_host(u'jumper')
    # And the associated play
    play = Play().load(dict(
        name='test play',
        hosts=[u'jumper'],
        gather_facts='no',
        tasks=[dict(action=dict(module='debug', args=dict(msg='{{vars}}')))]
    ), variable_manager=VariableManager(loader=None, inventory=inventory))
    # Get associated tasks, should be one
    tasks = [play.compile()]
    # Create a task executor.
    ti = TaskExecutor(play, host, tasks)
    # Testing: vars variable expansion.
    ti._tqm._stdout_callback = Display()


# Generated at 2022-06-13 17:19:59.545344
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    v = VariableManager()

    assert v._vars_cache.get("", None) == None

    v.set_host_variable("dummy", "dummy", "dummy")
    assert v._vars_cache.get("dummy", {}).get("dummy") == "dummy"

    v.set_host_variable("dummy", "dummy2", "dummy2")
    assert v._vars_cache.get("dummy", {}).get("dummy") == "dummy"
    assert v._vars_cache.get("dummy", {}).get("dummy2") == "dummy2"


# Generated at 2022-06-13 17:20:07.487475
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    vm=VariableManager()
    vm.set_host_variable("h1", "a", 2)
    assert vm._vars_cache['h1'] == {'a': 2}
    vm.set_host_variable("h1", "a", {"b": 1})
    assert vm._vars_cache['h1'] == {'a': {'b': 1}}
    vm.set_host_variable("h1", "a", {"c": 2})
    assert vm._vars_cache['h1'] == {'a': {'b': 1, 'c': 2}}
    vm.set_host_variable("h1", "x", {"c": 2})
    assert vm._vars_cache['h1'] == {'a': {'b': 1, 'c': 2}, 'x': {'c': 2}}


# Generated at 2022-06-13 17:20:37.318541
# Unit test for constructor of class VariableManager
def test_VariableManager():
    assert hasattr(VariableManager(), '_fact_cache')
    assert hasattr(VariableManager(), '_vars_cache')
    assert hasattr(VariableManager(), '_host_cache')
    assert hasattr(VariableManager(), '_host_vars_files_cache')
    assert hasattr(VariableManager(), '_extra_vars')
    assert hasattr(VariableManager(), '_play_context')
    assert hasattr(VariableManager(), '_inventory')
    assert hasattr(VariableManager(), '_loader')
    assert hasattr(VariableManager(), '_options_vars')
    assert hasattr(VariableManager(), '_omit_token')


# Generated at 2022-06-13 17:20:38.476371
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    pass


# Generated at 2022-06-13 17:20:39.609150
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test the method get_vars of class VariableManager
    pass



# Generated at 2022-06-13 17:20:48.230913
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    def get_host_vars(hostname):
        return dict(hostname = hostname)
    def get_host_variables(hostname):
        return dict(hostvars=get_host_vars(hostname))
    def get_host(hostname):
        return Host(name=hostname)
    def get_inventory(host=None):
        if host:
            return host
        return Inventory(loader=DataLoader())
    def get_variable_manager():
        return VariableManager(loader=None, inventory=get_inventory())

# Generated at 2022-06-13 17:20:51.192557
# Unit test for constructor of class VariableManager
def test_VariableManager():
    assert(VariableManager is not None)

    hosts_include = None
    variable_manager = VariableManager()

    variable_manager.get_vars(loader=None, play=None, host=None, task=None)

# Generated at 2022-06-13 17:21:00.971124
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    manager = VariableManager()
    test_vars = dict(a=1,b=2,c=3)
    manager._fact_cache = dict(host1=test_vars,host2=test_vars)
    manager._vars_cache = dict(host1=test_vars)
    test_hosts = [Host(name="host1")]
    assert manager.get_vars(host=test_hosts[0], include_hostvars=True) == test_vars
    assert manager.get_vars(host=test_hosts[0], include_hostvars=False) == {}
    assert manager.get_vars(host=test_hosts[0], include_hostvars=True) == test_vars

# Generated at 2022-06-13 17:21:09.116538
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition

    # test for get_vars(play, host, task)
    play = Play()
    variable_manager = VariableManager()
    variable_manager._options_vars = {}
    variable_manager._inventory = None
    variable_manager._loader = None
    variable_manager._hostvars = None

    variable_manager.set_nonpersistent_facts(host=None, facts=None)
    variable_manager._vars_cache = {}
    variable_manager._fact_cache = {}
    variable_manager._nonpersistent_fact_cache = {}
    variable_manager._omit_token = ""




# Generated at 2022-06-13 17:21:18.266995
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Set up the inventory
    inventory = Inventory()
    inventory.parse_inventory_sources([])

    # Set up the play context
    play = Play()
    play.transport = 'local'

    # Set up the loader
    loader = DataLoader()

    # Variable manager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Set up the task
    task = Task()
    task._role = None
    task._ds = ""
    task.action = {"module": "testmodule"}
    task.loop = "{{ listvars }}"

    # Set up the execution context
    context = {}

    # Set up the templar singleton
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=play, task=task, context=context))

    #

# Generated at 2022-06-13 17:21:25.485116
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    v = VariableManager()
    v.set_nonpersistent_facts("test", dict({"foo":"bar"}))
    assert v._nonpersistent_fact_cache == dict({"test": dict({"foo":"bar"})})

    v.set_nonpersistent_facts("test", dict({"foo":"baz"}))
    assert v._nonpersistent_fact_cache == dict({"test": dict({"foo":"baz"})})

    v.set_nonpersistent_facts("test", dict({"hello":"world"}))
    assert v._nonpersistent_fact_cache == dict({"test": dict({"foo":"baz", "hello":"world"})})

# Generated at 2022-06-13 17:21:26.628942
# Unit test for constructor of class VariableManager
def test_VariableManager():
    v = VariableManager()
    assert v is not None


# Generated at 2022-06-13 17:22:18.492959
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    varmgr = VariableManager()
    varmgr._fact_cache = {'host': {'a': 'A'}}
    host = 'host'
    facts = {'b': 'B'}
    varmgr.set_host_facts(host, facts)
    assert host in varmgr._fact_cache and varmgr._fact_cache[host] == {'a': 'A', 'b': 'B'}
    facts = {'c': 'C'}
    varmgr.set_host_facts(host, facts)
    assert host in varmgr._fact_cache and varmgr._fact_cache[host] == {'a': 'A', 'b': 'B', 'c': 'C'}


# Generated at 2022-06-13 17:22:28.144533
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.parsing.dataloader import DataLoader

    vm = VariableManager()
    loader = DataLoader()
    result = vm.get_vars(play={}, host={}, include_delegate_to=False, include_hostvars=None)
    assert result == {'omit': '__omit_place_holder__'}

    result = vm.get_vars(play={}, host=None, include_delegate_to=None, include_hostvars=0)
    assert result == {'omit': '__omit_place_holder__'}

    result = vm.get_vars(play={}, host=None, include_delegate_to=None, include_hostvars=None, include_role_tasks=True, include_play_tasks=True)

# Generated at 2022-06-13 17:22:34.421026
# Unit test for constructor of class VariableManager
def test_VariableManager():
    variable_manager = VariableManager()

    assert variable_manager.extra_vars == dict()
    assert variable_manager.options_vars == dict()
    assert variable_manager.tqm == None
    assert variable_manager.vars_cache == dict()
    assert variable_manager._fact_cache == dict()
    assert variable_manager._nonpersistent_fact_cache == dict()
    assert variable_manager._vars_plugins == []
    assert variable_manager._hostvars == None
    assert variable_manager._inventory == None


# Generated at 2022-06-13 17:22:44.399445
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Test set_host_facts(host, facts) when facts is not mapping.
    host = "myhost"
    facts = "myfacts"  # Not Mapping
    variable_manager = VariableManager()

    try:
        variable_manager.set_host_facts(host, facts)
        raise AssertionError("Expected exception")
    except AnsibleAssertionError:
        pass

    # Test set_host_facts(host, facts) when facts is Mapping
    facts = {"mykey": "myval", "mykey2": "myval2"}

    variable_manager.set_host_facts(host, facts)
    host_cache = variable_manager._fact_cache[host]
    assert host_cache == {'mykey': 'myval', 'mykey2': 'myval2'}

    # Test update

# Generated at 2022-06-13 17:22:52.336614
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Used to test whether all required arguments have been provided
    args = set()
    # Used to test whether all required keyword arguments have been provided
    kwargs = set()
    # Used to test whether all required arguments have been provided
    args_with_defaults = {"include_delegate_to": True, "include_hostvars": True}
    # Used to test whether all required keyword arguments have been provided
    kwargs_with_defaults = {}
    # Used to test whether all required arguments have been provided
    all_args = {"include_delegate_to": True, "include_hostvars": True, "host": "host", "play": "play", "task": "task"}
    # Used to test whether all required keyword arguments have been provided
    all_kwargs = {}

# Generated at 2022-06-13 17:23:02.061153
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test method get_vars of class VariableManager
    variable_manager = VariableManager()
    variable_manager.get_vars()
    variable_manager.set_host_variable('a', 'b', 'c')
    variable_manager.set_host_facts('d', 'e')
    variable_manager.clear_facts('f')
    variable_manager.set_nonpersistent_facts('g', 'h')
    variable_manager.extra_vars = {'i': 'j'}
    variable_manager.options_vars = {'k': 'l'}
    variable_manager._get_delegated_vars('m', 'n', 'o')
    
    print('成功调用 %s.get_vars()' % (variable_manager,))
 

# Generated at 2022-06-13 17:23:08.283329
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    host1 = Host(name='host1')

    vars_manager = VariableManager()
    vars_manager._vars_per_host[host1] = {'hostvar': 1}
    vars_manager._vars_per_host[host1]['var1'] = 'valuevar1'
    vars_manager._vars_per_host[host1]['var2'] = 'valuevar2'
    vars_manager._vars_per_host[host1]['var3'] = 'valuevar3'

    for host in vars_manager._vars_per_host:
        print("{0} --> {1}".format(host.name, vars_manager._vars_per_host[host]))

    print("")

# Generated at 2022-06-13 17:23:09.396716
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # TODO: need to be rewritten to work with new changes in 2.10
    pass

# Generated at 2022-06-13 17:23:14.338369
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Ensure that get_vars returns the right data structure
    v = VariableManager()
    # Test when loader is not None
    assert isinstance(v.get_vars(loader=True, play=True, host=True, task=True, include_delegate_to=True, include_hostvars=True), dict)
    # Test when loader is None
    assert isinstance(v.get_vars(loader=False, play=True, host=True, task=True, include_delegate_to=True, include_hostvars=True), dict)


# Generated at 2022-06-13 17:23:17.178555
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    """Tests for method set_host_facts of class VariableManager."""
    v = VariableManager()
    v.set_host_facts('host_name', {})



# Generated at 2022-06-13 17:24:12.983533
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    variable_manager2 = VariableManager()

    variable_manager.set_inventory(InventoryManager())

    variable_manager.extra_vars = dict(a=1, b=2)
    variable_manager.options_vars = dict(c=1, d=2)

    variable_manager2.set_inventory(InventoryManager())

    variable_manager2.extra_vars = dict(a=1, b=2)
    variable_manager2.options_vars = dict(c=1, d=2)

    variable_manager2.set_nonpersistent_facts('127.0.0.1', {'a': 2, 'b': 1})


# Generated at 2022-06-13 17:24:15.399068
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Initialize the object
    variable_manager = VariableManager()

    # Test the method
    variable_manager.get_vars()


# Generated at 2022-06-13 17:24:23.293982
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variableManager = VariableManager()
    variableManager._options_vars = {"ANSIBLE_TARGET_HOSTS":"test"}
    variableManager._generate_vars_cache()
    variableManager._fact_cache.clear()

    play = None
    host = None
    task = None
    include_delegate_to = None
    include_hostvars = None
    include_play_hosts = None
    include_playvars = None
    include_task_vars = None
    _hosts_all = None
    _hosts = None
    _hostvars = None
    _hosts_patterns = None


# Generated at 2022-06-13 17:24:32.407004
# Unit test for constructor of class VariableManager
def test_VariableManager():
    """
    Test the constructor for the VariableManager class.

    :return: <bool> True, when all tests are passed.
    """

    vm = VariableManager()

    # test to make sure that we have 2 default options passed in
    if not 'ansible_diff_mode' in vm._options_vars:
        return False
    if not 'ansible_output_encoding' in vm._options_vars:
        return False

    # test to make sure that we have a root fact_cache
    if not 'root' in vm._fact_cache:
        return False

    # test to make sure that we have a root _variable_store
    if not 'root' in vm._vars_cache:
        return False

    return True

# Generated at 2022-06-13 17:24:42.967680
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Arrange
    fake_loader = MagicMock()
    fake_inventory = MagicMock()
    fake_host = MagicMock()
    fake_host.get_vars = MagicMock(return_value={'host_vars': 'host vars'})
    fake_host.name = 'hostname'
    fake_host.address = 'hostname'
    fake_task = MagicMock()
    fake_play = MagicMock()
    fake_play.roles = []
    fake_play.dep_chain = []
    fake_play.get_vars = MagicMock(return_value={'play_vars': 'play vars'})
    fake_play._removed_hosts = []

    # Act
    vm = VariableManager(loader=fake_loader, inventory=fake_inventory)
   

# Generated at 2022-06-13 17:24:44.575317
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    target = VariableManager()
    result = target.get_vars()
    assert isinstance(result, Mapping)
    

# Generated at 2022-06-13 17:24:49.792895
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from collections import namedtuple
    import random
    
    
    
    
    
    
    
    
    
    
    
    
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'listhosts', 'listtasks', 'listtags', 'syntax'])
    options = Options(connection='', module_path='/usr/share/ansible', forks=100, become=None, become_method=None, become_user=None, check=False, listhosts=False, listtasks=False, listtags=False, syntax=False)
    passwords = dict()

# Generated at 2022-06-13 17:24:58.822387
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    '''
    Unit test for method get_vars of class VariableManager
    '''
    print("Testing VariableManager get_vars")
    var_manager = VariableManager()

    #
    #######
    # init
    #######
    #

    var_manager._fact_cache = dict()

    # Create a host
    host = Host(name="localhost")
    var_manager._fact_cache["localhost"] = dict()
    var_manager._vars_cache = dict()

    var_manager._options_vars = dict()
    var_manager._options_vars["remote_tmp"] = "/tmp"


# Generated at 2022-06-13 17:24:59.900137
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # FIXME: write tests in this file
    pass

# Generated at 2022-06-13 17:25:00.943531
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    VariableManager.get_host_vars()

 

# Generated at 2022-06-13 17:26:49.776437
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # TODO: implement unit test for method get_vars of class VariableManager
    pass

# Generated at 2022-06-13 17:26:51.916107
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    test_object = VariableManager(play_context=play_context)
    test_object.set_host_facts(host=host, facts=facts)


# Generated at 2022-06-13 17:26:57.313148
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Set up test data
    buffer = StringIO()
    log_capture_string = LogCapture(buffer)
    log_capture_string.handler.setFormatter(logging.Formatter('%(message)s'))
    loader = DataLoader()
    # Play context
    options = Options()
    passwords = dict()
    connection = Connection()
    stdout_callback = 'default'
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    inventory_loader = InventoryLoader(loader=loader, sources=[])

# Generated at 2022-06-13 17:27:06.575758
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    '''
    Unit test for method set_host_facts of class VariableManager.
    '''

    module = AnsibleModule(argument_spec={})
    module.exit_json = MagicMock(return_value=5)

    # Test passing in a value that is not a Mapping
    not_a_mapping = 'I am not a Mapping'
    vm = VariableManager()
    try:
        vm.set_host_facts('localhost', not_a_mapping)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError("Should have failed with an AnsibleAssertionError")

    # Test passing in a value that is not a Mapping
    host = 'localhost'
    facts = {'key1': 'value1', 'key2': 'value2'}

# Generated at 2022-06-13 17:27:07.286007
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# Generated at 2022-06-13 17:27:18.423980
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """
    test for method VariableManager.get_vars
    """
    # test for different values of play, host, task, include_delegate_to, include_hostvars
    # ===========================
    
    # ===========================
    x = VariableManager()
    x.extract_facts(host=None, loader=None, variables=None, filter_fqcn=None)
    x.set_host_variable(host=None, varname=None, value=None)
    x.set_nonpersistent_facts(host=None, facts=None)
    x.clear_facts(hostname=None)
    x.set_host_facts(host=None, facts=None)
    # ===========================

# Generated at 2022-06-13 17:27:27.888790
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    # Tests both the setting and the updating of host facts
    vars_manager = VariableManager()
    assert vars_manager._fact_cache == dict()
    test_hostname = 'somehost'
    test_facts = dict(fact1='value1',fact2='value2')
    vars_manager.set_host_facts(test_hostname, test_facts)
    assert vars_manager._fact_cache[test_hostname] is not test_facts
    assert vars_manager._fact_cache[test_hostname] == test_facts
    new_fact = dict(fact3='value3')
    vars_manager.set_host_facts(test_hostname, new_fact)
    assert vars_manager._fact_cache[test_hostname] != test_facts

# Generated at 2022-06-13 17:27:37.645442
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test 1: No options provided
    vm = VariableManager()
    assert vm._options_vars == {}

    # Test 2: Options provided
    options = {'ANSIBLE_FOO': 'FOO', 'ANSIBLE_BAR': 'BAR'}
    vm = VariableManager(options=options)
    assert vm._options_vars == options

    # Test 3: Play provided
    options = {u'ANSIBLE_FOO': u'FOO', u'ANSIBLE_BAR': u'BAR'}
    vm = VariableManager(options=options)
    play = Play()
    play.hosts = u'localhost'
    play.name = u'Test Play'
    vm.set_play_context(play)

# Generated at 2022-06-13 17:27:41.172613
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    vm = VariableManager()
    assert vm.get_vars() == {}
    assert vm.get_vars(host=None, play=None, task=None) == {}


# Generated at 2022-06-13 17:27:42.431074
# Unit test for constructor of class VariableManager
def test_VariableManager():
    # VariableManager has been tested in test_core
    # just set this file as up to date
    pass