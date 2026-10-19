

# Generated at 2022-06-13 10:05:36.971201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:05:37.787239
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return True

# Generated at 2022-06-13 10:05:48.388602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hosts = ['host1.example.com', 'host2.example.com', 'host3.example.com']
    hostvars = {
        'host1.example.com': {
            'group': 'foo',
        },
        'host2.example.com': {
            'group': 'foo',
        },
        'host3.example.com': {
            'group': 'bar',
        },
    }

    task = {
        'args': {
            'key': 'group',
            'parents': 'all',
        },
    }

    host = hosts[0]
    host_data = {
        'ansible_ssh_host': host,
    }
    host_data.update(hostvars[host])


# Generated at 2022-06-13 10:05:49.510731
# Unit test for constructor of class ActionModule
def test_ActionModule():
  module = ActionModule()
  assert module != None

# Generated at 2022-06-13 10:05:59.648418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = ''
    action = ActionModule(dict(), tmp, task_vars)
    task = dict()
    task['args'] = dict()
    task['action'] = 'group_by'
    task['args']['key'] = 'app'
    task['args']['parents'] = ['all', 'instance']
    ans = action.run(task_vars=task_vars, tmp=tmp, task=task)
    assert ans['changed'] == False
    assert ans['add_group'] == 'app'
    assert ans['parent_groups'] == ['all', 'instance']

    task['args']['key'] = 'app'
    task['args']['parents'] = 'all'

# Generated at 2022-06-13 10:06:07.228960
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostvars = {}

    def load_file_into_dict(filename):
        with open(filename) as f:
            return json.load(f)

    def load_file(filename):
        return load_file_into_dict(filename)

    def get_bin_path(name, required=False, opt_dirs=[]):
        return name

    class Connection:
        def __init__(self):
            self._shell = Shell(True, False)

        def _connect(self):
            return self

        def close(self):
            pass

        def exec_command(self, cmd, tmp_path, sudo_user=None, sudoable=False, executable='/bin/sh', in_data=None):
            return 0, cmd, ''


# Generated at 2022-06-13 10:06:20.086611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import imp
    #from ansible.compat.tests import unittest

    # create a mock object by importing/reloading modules
    # that this module depends on
    sys.modules['ansible.plugins.action'] = imp.new_module('action')
    #sys.modules['ansible.plugins.action.ActionBase'] = imp.new_module('ActionBase')


    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.group_by import ActionModule

    actionBase = ActionBase()
    actionModule = ActionModule(actionBase._task, actionBase._connection, actionBase._play_context, actionBase._loader, actionBase._templar, actionBase._shared_loader_obj)

    # test code here

    #
    # TESTS FOR METHODS
    #

   

# Generated at 2022-06-13 10:06:22.742580
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule """

    action_module = ActionModule()
    assert action_module._VALID_ARGS == frozenset(['key', 'parents'])

# Generated at 2022-06-13 10:06:36.644396
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Set up test infrastructure
    import ansible.plugins.action.group_by
    import ansible.template
    import ansible.inventory

    tmp = None
    task_vars = dict()
    host = None

    # Set up mock objects
    class MockTask:
        def __init__(self, args):
            self._args = args

        @property
        def args(self):
            return self._args

    class MockInventory:
        def __init__(self, groups, hosts):
            self._groups = groups
            self._hosts = hosts

        def add_group(self, group):
            self._groups.append(group)

        def add_host(self, host):
            self._hosts.append(host)

        @property
        def hosts(self):
            return self._hosts


# Generated at 2022-06-13 10:06:42.356157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = __import__('ansible.plugins.action', fromlist=('ansible', 'plugins', 'action'))
    ActionModule(None, None)
    ActionModule.run(None, None)
    print(ActionModule._VALID_ARGS)
    print(ActionModule.TRANSFERS_FILES)


# Unit test

# Generated at 2022-06-13 10:06:52.358860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    group_name = 'test_group'
    parent_groups = ['parent_group', 'top_group']
    action = ActionModule({'key': group_name, 'parents': parent_groups}, {'inventory_name': 'test_inventory'})
    assert action.run() == {
        'changed': False,
        'add_group': group_name,
        'parent_groups': parent_groups,
        'inventory_name': 'test_inventory'
    }

# Generated at 2022-06-13 10:06:53.871293
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(isinstance(ActionModule('test', dict()), ActionBase))

# Generated at 2022-06-13 10:06:58.042287
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.TRANSFERS_FILES == False
    assert a._VALID_ARGS == frozenset(('key', 'parents'))

# Generated at 2022-06-13 10:07:01.389024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({},{})
    assert ('key' in action_module._VALID_ARGS)
    assert ('parents' in action_module._VALID_ARGS)

# Generated at 2022-06-13 10:07:02.175856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:07:03.094499
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert obj._task.args is not None

# Generated at 2022-06-13 10:07:14.561492
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    module = pytest.importorskip('ansible.plugins.action')
    action = module.ActionModule('some_name', 'task')

    obj = action.run('tmp')
    assert obj['failed'] == True
    assert obj['add_group'] == ''
    assert obj['parent_groups'] == []

    obj = action.run({'key':'some'})
    assert obj['changed'] == False
    assert obj['add_group'] == 'some'
    assert obj['parent_groups'] == ['all']

    obj = action.run({'key':'some more', 'parents':'all'})
    assert obj['changed'] == False
    assert obj['add_group'] == 'some-more'
    assert obj['parent_groups'] == ['all']


# Generated at 2022-06-13 10:07:18.702328
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test setup
    import ansible.plugins.action
    ansible.plugins.action.ActionModule
    # test implementation
    test_ActionModule_obj = ActionModule()

# Generated at 2022-06-13 10:07:25.559234
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create class instance
    module = ActionModule()

    # Check _VALID_ARGS
    assert isinstance(module._VALID_ARGS, frozenset)
    assert module._VALID_ARGS == frozenset(('key', 'parents'))

    # Check TRANSFERS_FILES
    assert isinstance(module.TRANSFERS_FILES, bool)
    assert module.TRANSFERS_FILES == False


# Generated at 2022-06-13 10:07:30.186240
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a test function for testing the constructor of the class ActionModule."""

    # Defining the function call variables
    tmp = None
    task_vars = dict(a=1, b=2)

    my_test = ActionModule()
    result = my_test.run(tmp, task_vars)

    assert(result['failed'] == True)
    assert(result['msg'])

# Generated at 2022-06-13 10:07:39.745068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == frozenset(('key', 'parents'))
    assert ActionModule.TRANSFERS_FILES == 0
    assert ActionModule.__name__ == 'ActionModule'


# Generated at 2022-06-13 10:07:44.661777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    params = {
        'name': 'test',
        'key': 'test_key'
    }
    action = ActionModule(params, {})
    result = {
        'changed': False
    }

    # act
    action.run(None, None)

    # assert
    assert result == { 'changed': True }

# Generated at 2022-06-13 10:07:45.340050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:07:47.381787
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.group_by
    tmp = ansible.plugins.action.group_by.ActionModule()
    return tmp

# Generated at 2022-06-13 10:07:52.247264
# Unit test for constructor of class ActionModule
def test_ActionModule():    
    ActionModule()
    task_vars = dict()
    tmp=None
    new_object = ActionModule().run(tmp, task_vars)
    if(new_object['failed'] == True and new_object['msg'] == "the 'key' param is required when using group_by"):
        assert True
    else:
        assert False

# Generated at 2022-06-13 10:07:52.739503
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:08:01.034238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Imports
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Initialize the ActionModule
    module = ActionModule()
    task = Task()
    play = Play()
    play._inject_facts = dict()
    task._role = play
    module._task = task
    module._task.args = {'key': 'inventory-key'}

    # Check that the parameters key and parents are required
    result = module.run()
    assert(result['failed'] == True)
    module._task.args['key'] = 'test'
    result = module.run({}, {'hostvars': {'host': {'inventory-key': 'test'}}})

# Generated at 2022-06-13 10:08:12.103737
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks
    tmp = None
    tmp_path_origin = '/root/ansible/molecule/default/playbook.retry'
    task_vars = {}
    task_vars['ansible_version'] = {'full': '2.5.5', 'major': 2, 'minor': 5, 'revision': 5, 'string': '2.5.5'}
    task_vars['ansible_subscription_manager_facts'] = {}
    task_vars['ansible_version']['string'] = '2.5.5'
    task_vars['ansible_version']['full'] = '2.5.5'
    task_vars['ansible_version']['major'] = 2
    task_vars['ansible_version']['minor']

# Generated at 2022-06-13 10:08:16.822294
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test the correct construction of the class
    test_class = ActionModule(None, None, None, None)
    # The class should exist
    assert(test_class is not None)
    # The class should be a instance of the class ActionModule
    assert(isinstance(test_class, ActionModule))


# Generated at 2022-06-13 10:08:25.297824
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:08:38.789137
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:08:45.550503
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    tmp = "MockTempDir"
    new_actmod = ActionModule(tmp, task_vars)
    # value of key 'key' not found in ActionModule._task.args
    assert new_actmod.run(tmp, task_vars)['msg'] == "the 'key' param is required when using group_by"

# Generated at 2022-06-13 10:08:48.515381
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.group_by as group_by
    x = group_by.ActionModule(None, dict(), False, None)

# Generated at 2022-06-13 10:08:54.742252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_case = dict(
        group_by=dict(key='test-key', parents=['test-parent']),
        inventory=dict(hostvars=dict(hostname=dict(test_key='test-value'))))
    am = ActionModule(dict(), test_case, 'test_host', 'test_task')
    result = am.run(tmp=None, task_vars={})
    assert result['changed'] == False
    assert result['add_group'] == 'test-key'
    assert result['parent_groups'] == ['test-parent']

# Generated at 2022-06-13 10:09:03.521321
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.group_by import ActionModule
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    test_host = Host('host1')
    test_host.vars = HostVars(host = test_host, variables = dict(arch = 'x86_64'))

    test_parent_group_1 = Group('group1')
    test_parent_group_1.vars = dict(color = 'blue')

    test_parent_group_2 = Group('all')
    test_parent_group_2.vars = dict

# Generated at 2022-06-13 10:09:15.752027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import module_utils.nxos
    import configparser

    # For test_ActionModule_run nxos_config
    ini_str = '''
    [DEFAULT]
    transport = nxapi

    [nxos_config]
    host = nxos1.example.org
    username = admin
    password = admin1234
    '''.strip()
    ini_fp = module_utils.nxos.safe_eval.tmp_file(ini_str)
    config = configparser.ConfigParser()
    config.readfp(ini_fp)
    group_vars = module_utils.nxos.safe_eval.from_ini(config, 'group_vars')


# Generated at 2022-06-13 10:09:25.330384
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = dict()
    task_vars = dict()

    module = ActionModule(task, task_vars)

    module._task.args['key'] = 'the-group'
    module._task.args['parents'] = ['the-main-group']

    module._task.args['parents'] = 'not a list'

    module._task.args['parents'] = ['the-main-group', 'another-group']

    module._task.args['key'] = 'the group'
    module._task.args['parents'] = ['the main group']

    module._task.args['key'] = 'the group'
    module._task.args['parents'] = ['the main group', 'another group']

    module._task.args['key'] = 'the group'

# Generated at 2022-06-13 10:09:29.474752
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # unit test for constructor of class ActionModule
    b = ActionModule()
    print(b.__dict__)
    assert False

# Main execution of unit test
if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:09:40.714850
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with valid args
    class Args(object):
        def as_dict(self):
            return {
                'key': 'group_name',
                'parents': ['parent1', 'parent2'],
            }
    class Task(object):
        def __init__(self):
            self.args = Args()

    class Connection(object):
        def __init__(self):
            self._shell = None
        def connect(self, args):
            return

    class PlayContext(object):
        def __init__(self):
            self.connection = 'local'

    class Play(object):
        def __init__(self):
            self.connection = 'local'
            self.context = PlayContext()


# Generated at 2022-06-13 10:09:44.565487
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m is not None
    assert m._VALID_ARGS is not None
    assert len(m._VALID_ARGS) == 2
    assert 'key' in m._VALID_ARGS
    assert 'parents' in m._VALID_ARGS


# Generated at 2022-06-13 10:10:12.694270
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert_equals(ActionModule.TRANSFERS_FILES, False)
    assert_equals(ActionModule._VALID_ARGS, frozenset(('key', 'parents')))

if __name__ == '__main__':
    from nose.tools import *
    test_ActionModule()

# Generated at 2022-06-13 10:10:22.346720
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule({'name': 'test_module'}, {}, {}, {}, {}, {})
    result = am.run()
    print('result: %s' % result)
    if result['failed']:
        raise AssertionError(result['msg'])

    # Test that it creates a group for the host variable device_type
    hostvars = dict(device_type='router', foo='bar')
    am = ActionModule({'name': 'test_module', 'args': dict(key='device_type')}, hostvars, {}, {}, {}, {})
    result = am.run()
    print('result: %s' % result)
    if result['failed']:
        raise AssertionError(result['msg'])

# Generated at 2022-06-13 10:10:32.525367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #  Test 1
    #  key = 'foo', parents = 'all'
    #  Return value should contain:
    #  * 'add_group' = 'foo'
    #  * 'parent_groups' = ['all']
    task_args = dict()
    task_args['key'] = 'foo'
    task_args['parents'] = 'all'
    result = ActionModule(task_args, my_host).run(task_vars)
    assert 'add_group' in result
    assert result['add_group'] == 'foo'
    assert 'parent_groups' in result
    assert len(result['parent_groups']) == 1
    assert result['parent_groups'][0] == 'all'

    #  Test 2
    #  key = 'foo', parents = 'all, foo'
    # 

# Generated at 2022-06-13 10:10:39.820194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    task = Task()
    task._role = Role()
    task._block = RoleInclude()

    play_context = dict(
        port=2222
    )

    # Create a temporary inventory file

# Generated at 2022-06-13 10:10:54.089022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import action_loader, connection_loader

    # Create an ActionModule object

# Generated at 2022-06-13 10:10:55.843943
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert isinstance(x, ActionModule)


# Generated at 2022-06-13 10:11:00.933217
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(b='c'),None)
    assert action._VALID_ARGS == frozenset(('key', 'parents'))
    assert action.TRANSFERS_FILES == False
    assert action.run() ==  {'changed': False, 'add_group': 'c', 'parent_groups': ['all'], 'msg': '', 'failed': False}




# Generated at 2022-06-13 10:11:08.794884
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = {}
    m['module_name'] = 'group_by'
    m['key'] = 'ansible_os_family'
    m['parent_groups'] = ['all']
    m['ansible_os_family'] = 'RedHat'
    m['groups'] = {}
    m['groups']['all'] = {}
    m['groups']['all']['hosts'] = ['foo.example.org']
    m['groups']['all']['vars'] = {'ansible_connection': 'local'}
    t = {}
    t['hostvars'] = {}
    t['hostvars']['foo.example.org'] = {}
    t['hostvars']['foo.example.org']['ansible_os_family'] = 'RedHat'

# Generated at 2022-06-13 10:11:12.461169
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.unsafe_proxy import unsafe_proxy

    am = ActionModule(Task(), TaskQueueManager('/tmp/test'), None, None)
    am.run()

# Generated at 2022-06-13 10:11:13.173333
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(dict(), dict()) != None)

# Generated at 2022-06-13 10:12:17.698123
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #A test just to make sure the constructor is called without error
    action = ActionModule(task={'args': {}, 'action': {'add_group': 'test'}})
    assert action is not None

# Generated at 2022-06-13 10:12:24.269677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    parameters = {}
    action_module = ActionModule(parameters, {})

    def get_action_result(task_name, task_args):
        action_module._task = type("",(object,), {'name': task_name, 'args': task_args})
        return action_module.run("", {"inventory_hostname": "host1"})

    # Test with no key
    task_name = "test"
    task_args = {}
    result = get_action_result(task_name, task_args)
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"

    # Test with key and no parent
    task_args = {'key': 'my_group'}

# Generated at 2022-06-13 10:12:25.273936
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

# Generated at 2022-06-13 10:12:29.679805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import types
    import inspect
    assert 'action.ActionBase' in str(inspect.getmro(ActionModule))
    assert inspect.isclass(ActionModule)
    assert ActionModule.__name__ == 'ActionModule'
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:12:37.175356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six.moves import StringIO
    from ansible.vars.manager import VariableManager

    class MockTask(object):
        def __init__(self, args=None):
            self.args = args
            self.name = 'MockTask'

    variables = VariableManager()
    variables.add_host('localhost', 'all')

    module = ActionModule(task=MockTask(), connection=None, play_context=None, templar=None, loader=None)
    module._connection = None
    module._task = MockTask(args={})

# Generated at 2022-06-13 10:12:42.051251
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Unit test for method run of class ActionModule")
    module_args = {'key': "test_Key"}
    tmp = None
    task_vars = {}
    r = ActionModule(None, module_args, tmp, task_vars).run(tmp, task_vars)
    assert r['changed']
    assert r['add_group'] == "test_Key"
    assert r['parent_groups'] == ['all']

# Generated at 2022-06-13 10:12:48.154438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(
        task=dict(
            args=dict(
                key='variable',
                parents='all'
            ),
            name='group_by',
        ),
        play=dict(),
    )
    b = a.run()
    assert b['changed'] == False
    assert b['add_group'] == 'variable'
    assert b['parent_groups'] == ['all']

# Generated at 2022-06-13 10:12:50.735104
# Unit test for constructor of class ActionModule
def test_ActionModule():
	test_action_base = ActionModule()
	try:
		test_action_base.run()
	except Exception as e:
		assert type(e) == TypeError, "Still need to implement run to return"

# Generated at 2022-06-13 10:13:00.896320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Input parameters
    class Options(): 
        def __init__(self, action, **kwargs):
            self.verbosity = 1
            self._args = { 'key': action, **kwargs}

    inputs = [
        (
            'create group', 
            {
                'action': 'create', 
            },
        ),
        (
            'create group', 
            {
                'action': 'create', 
            },
        ),
        (
            'create group', 
            {
                'action': 'create', 
            }
        ),
    ]

    # Output

# Generated at 2022-06-13 10:13:04.209740
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # instantiate the class
    am = ActionModule()
    assert(am.TRANSFERS_FILES == False)


# Generated at 2022-06-13 10:15:31.676959
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor of class ActionModule
    '''
    # Construct a mock object to represent the ansible task_vars
    task_vars = dict()

    # Construct a mock object to represent the ansible tmp
    tmp = None

    # Construct a mock object to represent the ansible display
    display = None

    # Construct a object of class ActionModule
    a = ActionModule(task=None, connection=None, _play_context=None, loader=None,
        templar=None, shared_loader_obj=None)

    # Make a call the run method of class ActionModule
    result = a.run(task_vars=task_vars, tmp=tmp)

    # Test if the run return a changed result
    assert result['changed'] == False

    # Test if the run return a msg result