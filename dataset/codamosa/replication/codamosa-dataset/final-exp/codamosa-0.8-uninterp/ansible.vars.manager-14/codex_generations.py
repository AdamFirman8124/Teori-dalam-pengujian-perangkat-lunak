

# Generated at 2022-06-13 17:19:35.161475
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # test when self._inventory is None
    # initialize an VariableManager object
    var_manager = VariableManager()
    var_manager._vars_cache = {}
    var_manager._options_vars = {"option1":"value1", "option2":"value2"}
    var_manager._hostvars = {}
    var_manager._nonpersistent_fact_cache = {"host1.example.com": {"fact1":"value1", "fact2":"value2"}}
    var_manager._fact_cache = {"host1.example.com":{"fact1":"value1", "fact2":"value2"}}
    var_manager._inventory = None

# Generated at 2022-06-13 17:19:36.365431
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass

# Generated at 2022-06-13 17:19:44.224891
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    vault_secrets = {}
    get_host_vars_dict = {}
    get_host_vars_result = {}
    get_host_vars_result["success"] = True
    get_host_vars_result["host_vars"] = None
    get_hosts_vars_dict = {}
    get_hosts_vars_result = {}
    get_hosts_vars_result["success"] = True
    get_hosts_vars_result["result"] = copy.deepcopy(get_host_vars_dict)
    get_hosts_vars_result["failed"] = []
    get_hosts_vars_result["unreachable"] = []
    get_hosts_vars_result["skipped"] = []
    get_host_vars_dict_verify

# Generated at 2022-06-13 17:19:54.233453
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    MockHost = namedtuple('Host', ['name'])
    mock_loader = Loader()
    mock_inventory = InventoryManager(
        loader=mock_loader,
        sources=None,
    )
    mock_options = Options()
    mock_options_vars = {"a": 1, "b": 2}
    variable_manager = VariableManager(
        loader=mock_loader,
        inventory=mock_inventory,
        options_vars=mock_options_vars,
        options=mock_options,
    )
    vars_result = variable_manager.get_vars(host=MockHost(name="test_host"))
    # Expecting a dictionary
    assert isinstance(vars_result, dict)
    # Expecting expected keys
    assert "a" in vars_result
   

# Generated at 2022-06-13 17:19:56.263086
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # As we are testing a method of a class, we need to instantiate an object first for the test
    vm = VariableManager()
    vm.set_nonpersistent_facts(host='localhost', facts=dict())
    assert vm._nonpersistent_fact_cache == {'localhost': {}}



# Generated at 2022-06-13 17:20:04.614420
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # Test with a nonmapping type for facts
    vm = VariableManager()
    vm.clear_nonpersistent_facts()
    vm.set_nonpersistent_facts('localhost', 'facts')
    assert_raises(AnsibleAssertionError, lambda: vm.set_nonpersistent_facts('localhost', 'facts'))
    # Test with a mapping type for facts
    vm.clear_nonpersistent_facts()
    vm.set_nonpersistent_facts('localhost', {'fact1': 'value1'})
    vm.set_nonpersistent_facts('localhost', {'fact2': 'value2'})
    assert vm.get_nonpersistent_facts(host='localhost')['fact1'] == 'value1'

# Generated at 2022-06-13 17:20:11.488206
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    ##
    # Unit test setup
    ##
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from collections import MutableMapping
    from ansible.parsing.yaml.objects import AnsibleMapping

    # Create the inventory, which will populate the hostvars

# Generated at 2022-06-13 17:20:12.492600
# Unit test for constructor of class VariableManager
def test_VariableManager():
    vm = VariableManager()
    assert vm is not None

# Generated at 2022-06-13 17:20:16.958975
# Unit test for constructor of class VariableManager
def test_VariableManager():
    initial_vars = {'var1': 'value1', 'var2': 'value2'}
    variables = VariableManager(include_cache=initial_vars)
    assert isinstance(variables._fact_cache, DefaultFactCache)
    assert variables.get_vars() == {'var1': 'value1', 'var2': 'value2'}



# Generated at 2022-06-13 17:20:26.034309
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    vm = VariableManager()
    vm.set_inventory(None)
    vm._vars_cache = {
        'all': {},
        'local': {},
        'host': {}
    }
    class FakeTask(object):
        def __init__(self, name, action=None):
            self.name = name
            self.action = action
        _delegate_to = 'host'
        def get_name(self):
            return self.name
        def delegate_to(self):
            return self._delegate_to
        def set_delegate_to(self, delegate_to):
            self._delegate_to = delegate_to
    ansible_play_hosts = ('host1', 'host2')

# Generated at 2022-06-13 17:21:10.482269
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Setup
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from collections import Mapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.vars.hostvars import HostVars

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager())
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager._fact_cache = dict()
    variable_manager._vars_cache = dict()
    variable_manager._nonpersistent_fact_cache = dict()

# Generated at 2022-06-13 17:21:13.112904
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    myVariableManager = VariableManager()
    result = myVariableManager.set_nonpersistent_facts('host', 'facts')
    assert result == None


# Generated at 2022-06-13 17:21:23.221436
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Case 01
    seed = 42
    random.seed(seed)

    vm = VariableManager()
    vm._vars_cache = dict(
        aa={
            'a' : 1,
            'b' : 2,
            'c' : 3
        },
        bb={
            'a' : 4,
            'b' : 5,
            'c' : 6
        }
    )
    vm._nonpersistent_fact_cache = dict(
        aa={
            'a' : 1,
            'b' : 2,
            'c' : 3
        },
        bb={
            'a' : 4,
            'b' : 5,
            'c' : 6
        }
    )
    host = 'aa'
    include_hostvars = False
    include_

# Generated at 2022-06-13 17:21:24.689019
# Unit test for constructor of class VariableManager
def test_VariableManager():
    v = VariableManager()
    assert v._fact_cache == dict()
    assert v._vars_cache == dict()

# Generated at 2022-06-13 17:21:25.289359
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    v = VariableManager()

# Generated at 2022-06-13 17:21:28.235829
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    assert vm.get_nonpersistent_facts('myhost') == dict()
    vm.set_nonpersistent_facts('myhost', dict(test=123))
    assert vm.get_nonpersistent_facts('myhost') == dict(test=123)

# Generated at 2022-06-13 17:21:34.381651
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    module_test = AnsibleModule(argument_spec={})
    task = None
    host = 'abc'
    _hostvars = None
    _hosts_all = None
    _hosts = None
    _hosts_remaining = None
    include_hostvars = True
    include_delegate_to = True
    play = None
    task = None

    vm = VariableManager()
    vm._omit_token = '__omit_place_holder__'
    variables = vm.get_vars(play, host, task, _hostvars, _hosts_all, _hosts, _hosts_remaining)
    assert 'groups' in variables, "groups is not in variables"
    assert 'inventory_hostname' in variables, "inventory_hostname is not in variables"

# Generated at 2022-06-13 17:21:42.047812
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # stub(self, play=None, host=None, task=None, include_delegate_to=True, include_hostvars=False,): 
    # play, host, task, include_delegate_to, include_hostvars
    stub = VariableManager()

    play = None
    host = None
    task = None
    include_delegate_to = True
    include_hostvars = False
    result = stub.get_vars(play, host, task, include_delegate_to, include_hostvars)

    print(result)



# Generated at 2022-06-13 17:21:49.880562
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
  from collections import namedtuple
  from ansible.errors import AnsibleError
  from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
  from ansible.parsing.yaml.objects import AnsibleUnicode
  from ansible.parsing.yaml.objects import AnsibleSequence
  from ansible.vars import VariableManager
  from ansible.vars import VersionInfo
  # Test typing of "host" parameter
  try:
    VariableManager().get_vars("", "", "")
  except TypeError as exc:
    assert "got an unexpected keyword argument 'host'" in str(exc)
  except Exception as exc:
    raise AssertionError("Unexpected exception raised when 'host' has invalid type: %s" % (type(exc).__name__))

# Generated at 2022-06-13 17:21:55.347359
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():

    VariableManager = ansible.vars.VariableManager
    Options = ansible.utils.options.Options
    Play = ansible.playbook.play.Play
    TaskExecutor = ansible.executor.task_executor.TaskExecutor
    Host = ansible.inventory.host.Host
    Task = ansible.playbook.task.Task
    Role = ansible.playbook.role.Role

    options = Options()
    options.roles_path = '/Users/mac/Desktop/ansible_test/test_roles'
    options.connection = 'local'
    options.timeout = 10
    options.module_path = None
    options.forks = 5
    options.become = None
    options.become_method = 'sudo'
    options.become_user = 'root'
    options.check = False

# Generated at 2022-06-13 17:22:51.399665
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    print("Testing VariableManager.set_nonpersistent_facts()")
    variable_manager = VariableManager()
    host = 'localhost'
    variable_manager.set_nonpersistent_facts(host, dict())
    variable_manager.set_nonpersistent_facts(host, dict(a=1))
    variable_manager.set_nonpersistent_facts(host, dict(b=2))
    variable_manager.set_nonpersistent_facts(host, dict(a=3))
    nonpersistent_facts = variable_manager.get_vars(play=None, host=None, task=None, include_delegate_to=False, include_hostvars=False, include_nonpersistent_facts=True)['nonpersistent_facts']
    assert nonpersistent_facts == dict(a=3, b=2)


# Generated at 2022-06-13 17:23:01.389490
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    import copy
    import unittest
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 17:23:07.802139
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Set up some test cases
    # We use a dict of dicts to avoid having to mock PlayContext, Task and Host
    # This is designed such that there is one test case per branch in the code
    # for each of the methods it calls too
    testcases = dict()

    testcase_basic = dict()
    testcase_basic['play'] = dict(variable_manager=dict(play_vars=dict(play_var="play_var_value"),
                                                        extra_vars=dict(extra_var="extra_var_value"),
                                                        )
                                  )
    testcase_basic['task'] = dict(variable_manager=dict(task_vars=dict(task_var="task_var_value"),
                                                        ))

# Generated at 2022-06-13 17:23:14.593727
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManagerOptions


# Generated at 2022-06-13 17:23:24.143066
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    """
    get_vars() of class VariableManager should always return a dictionary.
    This unit test asserts that the method get_vars returns a dictionary.
    """
    gvars = VariableManager(loader=BaseLoader())
    assert type(gvars.get_vars(loader=BaseLoader())) == dict, "get_vars() of class VariableManager should always return a dictionary"
    assert type(gvars.get_vars(play=object(), loader=BaseLoader())) == dict, "get_vars() of class VariableManager should always return a dictionary"
    assert type(gvars.get_vars(play=object(), host=object(), loader=BaseLoader())) == dict, "get_vars() of class VariableManager should always return a dictionary"

# Generated at 2022-06-13 17:23:33.448055
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from units.compat import unittest

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    INVENTORY = """
        [group1]
        localhost
        local2
        """


# Generated at 2022-06-13 17:23:41.260435
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Setup
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager, Host
    from ansible.utils.vars import combine_vars

    # Get a mock inventory, loader, and var manager
    loader = unittest.mock.Mock()
    vm = VariableManager(loader)
    hosts = [Host(name='badger')]

    # Test when delegation is disabled
    # TODO: move this into a test for the role resolver

# Generated at 2022-06-13 17:23:46.982372
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Test to check if all the variables in the variable dictionary are returned
    variable_manager = VariableManager()
    variable_manager._vars = {'ansible_version': '2.3'}
    variable_manager._nonpersistent_facts = None
    variable_manager._fact_cache = None
    variable_manager._vars_cache = {'localhost': {'ansible_version': '2.3'}}
    variable_manager._omit_token = '<OMITTED>'
    variable_manager._options_vars = dict()
    variable_manager._hostvars = None
    variable_manager._inventory = None
    variable_manager._loader = 'loader'
    variable_manager._vault_secrets = None
    variable_manager._unsafe_proxy = None
    variable_manager._task_vars = dict()


# Generated at 2022-06-13 17:23:52.190255
# Unit test for method set_host_variable of class VariableManager
def test_VariableManager_set_host_variable():
    variable_manager = VariableManager()
    variable_manager.set_host_variable('abc-123', 'testvar', 'test')
    variable_manager.set_host_variable('abc-123', 'testvar2', 'test2')
    variable_manager.set_host_variable('abc-123', 'testvar', {'testvar': 'test'})
    variable_manager.set_host_variable('abc-123', 'testvar2', {'testvar2': 'test2'})

    variable_manager._vars_cache = {'abc-123': {'testvar': {'a': {'b': 'c'}}}}
    variable_manager.set_host_variable('abc-123', 'testvar', {'d': {'e': 'f'}})

# Generated at 2022-06-13 17:23:58.384408
# Unit test for constructor of class VariableManager
def test_VariableManager():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import create_manager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.clean import clean
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import os

    hosts = [Host('test1'), Host('test2')]
    hostvars = HostVars({'test1': {'name': 'test1', 'foo': 'bar'}, 'test2': {'name': 'test2', 'foo': 'rab'}})

    inventory = InventoryManager(loader=DataLoader(), sources=[])

# Generated at 2022-06-13 17:24:43.668812
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = ansible.vars.VariableManager()
    variable_manager.extra_vars = {}
    variable_manager.options_vars = {}
    variable_manager.set_inventory(ansible.inventory.Inventory())
    variable_manager.set_loader(ansible.parsing.dataloader.DataLoader())
    # Test with no args
    assert variable_manager.get_vars() is not None, \
        "VariableManager.get_vars should return a dictionary object, but returned: %s" % type(variable_manager.get_vars())
    # Test with valid args

# Generated at 2022-06-13 17:24:44.537056
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    pass



# Generated at 2022-06-13 17:24:49.775279
# Unit test for method get_vars of class VariableManager

# Generated at 2022-06-13 17:24:50.805383
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    pass # nothing to test



# Generated at 2022-06-13 17:24:55.639322
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    variable_manager = VariableManager()
    host = 'example.org'
    variable_manager.set_host_facts(host=host, facts={'foo':'bar'})
    assert variable_manager.get_vars(host=MagicMock(name='host(example.org)'), include_hostvars=True)['foo'] == 'bar'


# Generated at 2022-06-13 17:25:02.721519
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager._inventory = InventoryManager(loader=None, sources=None)
    variable_manager._fact_cache = { "localhost": { "ansible_connection": "local" } }
    variable_manager._vars_cache = { "localhost": { "ansible_connection": "local" } }
    variable_manager._nonpersistent_fact_cache = { "localhost": { "ansible_connection": "local" } }
    variable_manager._options_vars = { "ansible_connection": "paramiko" }
    variable_manager._omit_token = '<omit>'

    play_context = PlayContext()

# Generated at 2022-06-13 17:25:12.465198
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    class TestObject(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class TestInventory(object):
        def __init__(self):
            self._hosts = ['localhost']

        def get_hosts(self, pattern='all'):
            for i in self._hosts:
                yield TestObject(i)

        def get_groups_dict(self):
            return {
                'group1': {
                    'hosts': ['localhost'],
                },
                'group2': {
                    'hosts': ['localhost'],
                },
            }

        def get_host(self, hostname):
            if hostname in self._hosts:
                return TestObject(hostname)
            return None


# Generated at 2022-06-13 17:25:14.873353
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    v_man = VariableManager()
    v_man.set_host_facts("host", {"fact1":"fact"})
    assert v_man._fact_cache["host"] == {"fact1":"fact"}


# Generated at 2022-06-13 17:25:18.179115
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # setup
    vm = VariableManager()
    host = 'localhost'
    facts = {'foo': 'bar'}
    # test
    vm.set_nonpersistent_facts(host, facts)
    # verify
    assert vm._nonpersistent_fact_cache[host] == facts

# Generated at 2022-06-13 17:25:26.196165
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # Initialize the class object
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManagerOptions
    from ansible.vars.hostvars import HostVars
    # Initialize the relevant classes
    host_vars = HostVars({"test_host": {"var1": "val1"}})
    inventory = Mock(get_host=lambda *args: Host(name="test_host"))
    option_manager = VariableManagerOptions("test")
    variable_manager = VariableManager(loader=None, inventory=inventory, options_vars=option_manager, host_vars=host_vars)
    # Run the test
    variable_manager.set_nonpersistent_facts("test_host", {"var2": "val2"})
    #

# Generated at 2022-06-13 17:27:06.281006
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # See https://github.com/ansible/ansible-modules-core/pull/3429
    # before this PR, get_vars() returned the wrong values for ansible_play_batch
    # when a play had limit/filters applied.

    test_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(test_dir, 'unit', 'vars', 'data')

    sut = VariableManager()

    inventory_file = os.path.join(data_dir, 'inventory')
    inventory = InventoryManager(loader=DataLoader(), sources=inventory_file)

    play_book_path = os.path.join(data_dir, 'playbook.yml')

# Generated at 2022-06-13 17:27:17.666112
# Unit test for method set_host_facts of class VariableManager
def test_VariableManager_set_host_facts():
    from copy import deepcopy

    import pytest

    from ansible.errors import AnsibleAssertionError
    from ansible.vars.hostvars import HostVars

    # Setup
    variable_manager = VariableManager()
    host_name = 'testhost'
    new_facts = dict(key1='value1', key2='value2')

    # Tests
    # New host has no vars
    with pytest.raises(KeyError):
        variable_manager._fact_cache[host_name]

    # Set the facts on a non-existent host
    variable_manager.set_host_facts(host_name, new_facts)
    assert variable_manager._fact_cache[host_name] == new_facts

    # Set the facts on the host again, but this time via dict assignment

# Generated at 2022-06-13 17:27:27.535508
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    '''
    Method set_nonpersistent_facts(host, facts):
    Sets or updates the given facts for a host in the fact cache.
    '''
    #  Test the case when 'facts' is not of the type dict.
    #  Test the case when 'facts' is of the type dict.
    #  Test the case when 'facts' is not of the type dict.
    #  Test the case when 'facts' is of the type dict.
    #  Test the case when 'facts' is of the type dict.

    #  Create an object which is suitable for testing of class VariableManager
    object_name = VariableManager(loader=None, inventory=None, version_info=None)
    object_name.set_nonpersistent_facts(host=str, facts=str)


# Generated at 2022-06-13 17:27:28.832499
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    t = VariableManager()
    return

test_VariableManager_get_vars()

# Generated at 2022-06-13 17:27:38.108269
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    vm = VariableManager()
    host = Host('example')
    facts = {'key1': 'value1', 'key2': 'value2'}
    facts_updated = {'key1': 'value1', 'key2': 'value2_updated'}
    facts_additional = {'key3': 'value3'}
    # Set facts with all the keys of facts_updated
    vm.set_nonpersistent_facts(host, facts)
    # Reset a value in the facts
    vm.set_nonpersistent_facts(host, facts_updated)
    # Add a new key value pair to facts
    vm.set_nonpersistent_facts(host, facts_additional)

# Generated at 2022-06-13 17:27:46.408930
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    # Create a new runner and variable manager
    variable_manager = VariableManager()
    variable_manager._fact_cache = {'test-host': {'hello': 'world', 'ansible_check_mode': True}}
    variable_manager._vars_cache = {'test-host': {'myvar': 'hello'}}
    variable_manager._nonpersistent_fact_cache = {'test-host': {'omit': 'me'}}
    variable_manager._hostvars = {'test-host': {'hostvar': 'foo'}}
    variable_manager._options_vars = {'foo': 'bar'}
    loader = DictDataLoader({'test-host': {'group_vars': {'group': {'gvar': 'myvar', 'myvar': 'hello'}}}})
    inventory = Inventory

# Generated at 2022-06-13 17:27:54.503893
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    variable_manager = VariableManager()
    play = Play()
    task = Task()
    host = Host()
    variable_manager.get_vars(play=play, host=host, task=task, include_hostvars=True, include_delegate_to=True)
    variable_manager.set_nonpersistent_facts('abc', {})
    variable_manager.set_nonpersistent_facts(host.name, {})
    variable_manager.set_host_variable('abc', 'a', 'b')
    variable_manager.get_vars(play=play, host=host, task=task, include_hostvars=True, include_delegate_to=True)
    variable_manager.set_host_fact('abc', {})
    variable_manager.set_host_fact(host.name, {})


# Generated at 2022-06-13 17:27:57.074266
# Unit test for method set_nonpersistent_facts of class VariableManager
def test_VariableManager_set_nonpersistent_facts():
    # verify set_nonpersistent_facts set the fact correctly
    fact_data = {}
    hostname = 'localhost'
    var_manager = VariableManager()
    var_manager.set_nonpersistent_facts(hostname, fact_data)
    assert var_manager._nonpersistent_fact_cache[hostname] == fact_data

# Generated at 2022-06-13 17:28:07.259416
# Unit test for method get_vars of class VariableManager
def test_VariableManager_get_vars():
    M = type_store.M
    def method(self):
        return self.vars_cache
    h = M.dict({M.str: M.dict({M.str: M.any()})})
    m = M.VariableManager._get_vars(h)
    m.update(M.VariableManager._get_vars._.return_type.__constraints__)