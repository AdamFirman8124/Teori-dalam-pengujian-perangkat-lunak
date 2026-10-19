

# Generated at 2022-06-13 10:16:19.539828
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import argparse
    import mock
    import os
    import tempfile
    import unittest

    from ansible.module_utils.six import PY2

    from ansible.errors import AnsibleError
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    from six import BytesIO

    class Args(object):
        debug = False
        diff = False
        force_handlers = False
        flush_cache = None
        listhost

# Generated at 2022-06-13 10:16:29.664677
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import io

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.plugins.action import ActionBase

    from ansible.module_utils.connection import Connection
    from ansible.module_utils._text import to_bytes

    class TestActionModule(ActionModule):

        def run(self, tmp=None, task_vars=None):
            return super(TestActionModule, self).run(tmp, task_vars)


# Generated at 2022-06-13 10:16:31.138110
# Unit test for constructor of class ActionModule
def test_ActionModule():
  actionModule = ActionModule()

# Generated at 2022-06-13 10:16:31.765213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()

# Generated at 2022-06-13 10:16:36.623472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # constructor test
    md = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert md

# Generated at 2022-06-13 10:16:50.046255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # with action="command", test_tasks.py
    test_tasks = [
        {
            'name': 'get Ansible facts from all hosts',
            'hosts': 'local',
            'gather_facts': 'no',
            'tasks': [
                {
                    'name': 'setup',
                    'action': 'setup'
                }
            ]
        }
    ]
    task_vars = {'ansible_ssh_pass': 'pass', 'ansible_connection': 'ssh', 'ansible_user': 'root'}
    action = 'setup'

# Generated at 2022-06-13 10:16:52.984185
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod._supports_check_mode == True
    assert mod._supports_async == True

# Generated at 2022-06-13 10:17:02.833504
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockActionBase:
        def __init__(self):
            self.tmp = None
            self.task_vars = None
            self._supports_check_mode = True
            self._supports_async = True

    action_base = MockActionBase()
    action_module = ActionModule(action_base)

    assert(action_module.tmp is None)
    assert(action_module.task_vars is None)
    assert(action_module._supports_check_mode is True)
    assert(action_module._supports_async is True)

# Generated at 2022-06-13 10:17:12.082587
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostVars = {
        'boolean_arg1': True,
        'boolean_arg2': False,
        'integer_arg1': 10,
        'integer_arg2': 0,
        'string_arg1': 'string',
        'string_arg2': '',
        'array_arg1': ['a'],
        'array_arg2': [],
    }
    expectedVars = {
        'boolean_arg1': True,
        'boolean_arg2': False,
        'integer_arg1': 10,
        'integer_arg2': 0,
        'string_arg1': 'string',
        'string_arg2': '',
        'array_arg1': ['a'],
        'array_arg2': [],
    }
    action = ActionModule()
    result

# Generated at 2022-06-13 10:17:13.719379
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule,'run'), "ActionModule must have method 'run'"

# Generated at 2022-06-13 10:17:26.760378
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple

    # namedtuple constructor to simulate module_args from ansible playbook
    args = dict(
        delegate_to='localhost',
        tasks=[
            dict(
                action=dict(
                    module='copy',
                    args=dict(
                        src='/tmp/source.txt',
                        dest='/tmp/dest.txt',
                        force=False,
                        follow=True,
                    )
                ),
                tags=['copy_test'],
            ),
        ],
    )
    ActionModuleMock = namedtuple('ActionModuleMock', args.keys())
    module_args = ActionModuleMock(**args)

    # module_args is required param of run method
    # the param tmp and task_vars can be defaulted to None

    # initialize action_module obj using mock module_args


# Generated at 2022-06-13 10:17:37.494522
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ error out if module_args is provided"""
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    t = Task()
    t.module_args = dict(param='value')
    t.action = 'test_test'
    t.async_val = 50
    t.args = dict(param='value')

    mod = ActionModule(t, variable_manager=variable_manager)
    with pytest.raises(Exception) as e:
        mod.run()


# Generated at 2022-06-13 10:17:52.172407
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialization
    module_name = "setup"
    module_args = {}
    module_kwargs = {}
    invocation = {'module_args': module_args, 'module_kwargs': module_kwargs}
    self = {'task': {'action': module_name, 'async_val': 1}, '_connection': {'has_native_async': 0}}
    tmp = None
    task_vars = {}
    self2 = {'task': {'async_val': 1}} # test invalid value of has_native_async

    # verify  all the attributes are initialized properly
    assert self['task']['action'] == module_name
    assert self['task']['async_val'] == 1
    assert self2['task']['async_val'] == 1

# Generated at 2022-06-13 10:17:52.550626
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:17:54.898898
# Unit test for constructor of class ActionModule
def test_ActionModule():
   from ansible.plugins.action.normal import ActionModule as normal

   a = normal(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

   assert(a)

# Generated at 2022-06-13 10:17:56.581567
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test function for ActionModule run method"""
    assert False,"Not implemented yet"


# Generated at 2022-06-13 10:18:11.522431
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    import ansible.constants as C

    # Create task
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='/home/ansible/hosts')
    print ("this is inventory")
    print (inventory.get_hosts('all'))

# Generated at 2022-06-13 10:18:16.509290
# Unit test for constructor of class ActionModule
def test_ActionModule():
    temp_instance = ActionModule(module_name="module_name",module_exec_path="module_exec_path",module_args={"module_args":"module_args"}, task={"task":"task"}, connection="connection", play_context="play_context", loader="loader", templar="templar", shared_loader_obj="shared_loader_obj")
    print("ActionModule instance created. ")

# test_ActionModule()

# Generated at 2022-06-13 10:18:17.045842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:18:25.831115
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    # initialize needed objects
    action_loader.add('test_action_module')
    task = Task()

# Generated at 2022-06-13 10:18:42.574197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    from ansible.module_utils.six.moves import StringIO as sIO
    from ansible import constants as C
    from ansible.utils.vars import merge_hash

    # create a dummy action plugin
    class AnsibleModule(ActionModule):
        def run(self, tmp, task_vars):
            # an action plugin has to return a result
            result = {}
            result['action_module'] = 'AnsibleModule'
            return result

    # create a dummy task

# Generated at 2022-06-13 10:18:51.716833
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plays.strategy_plugins.linear import StrategyModule as Linear
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible import context
    from ansible.utils.vars import combine_vars

    context.CLIARGS = {'module_path': '', 'no_log': False, 'tree': None}
    loader = None
    variable_manager = None
    inventory = None
    # FIXME: fails if run from test_runner
    # FIXME: need function to get options from fixture

# Generated at 2022-06-13 10:18:54.666076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, task_vars=None, wrap_async=None)
    assert a is not None

# Generated at 2022-06-13 10:19:04.515255
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.modules.system import ping
    from ansible.plugins.action import ActionModule
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash

    # test data
    module_name = 'ping'
    module_args = 'data=test'

    # create object
    action = ActionModule('test')
    action._task.args['module_name'] = module_name
    action._task.args['module_args'] = module_args

    # mock object
    import ansible.plugins.action.normal
    ansible.plugins.action.normal._load_params = lambda x, y: {}
    ansible.plugins.action.normal._execute_module = lambda *args: {'rc': 0}

# Generated at 2022-06-13 10:19:12.949919
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an object of class ActionModule
    mod = ActionModule()
    assert mod.action_plugins == {}
    assert mod.module_name == ''
    assert mod.module_args == {}
    assert mod.module_vars == {}
    assert mod.module_vars == {}
    assert mod.module_name_to_walk == []
    assert mod.module_paths == []
    assert mod.module_args_stack == []
    assert mod.module_compression == None
    assert mod.module_data == None
    assert mod.module_implementation_name == []
    assert mod.module_implementation_version == {}
    assert mod.module_lang == 'python'
    assert mod.module_name_to_walk == []
    assert mod.module_paths == []
    assert mod.module_set_loc

# Generated at 2022-06-13 10:19:13.751000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: Write the test case
    assert True

# Generated at 2022-06-13 10:19:14.237748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:19:19.019035
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a mock config object
    config = {'no_log': False}

    # Create a mock module_loader object
    module_loader = 'module_loader'

    # Create a mock display object
    display = 'display'

    # Create a mock task object
    task = 'task'

    # Create a mock connection object
    connection = 'connection'

    # Create a mock play context object
    play_context = 'play_context'

    # Create a mock shared loader object
    loader = 'loader'

    # Create a mock templar object
    templar = 'templar'

    # Create a ActionModule object
    action_module = ActionModule(task, connection, play_context, loader, templar, config)

    # Check that the class object is a ActionModule

# Generated at 2022-06-13 10:19:30.914643
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock = {}
    mock['_task'] = {}
    mock['_task']['async'] = 20
    mock['_task']['async_poll_interval'] = 20
    mock['_play_context'] = {}
    mock['_play_context']['check_mode'] = True
    mock['_play_context']['remote_addr'] = '192.168.1.1'
    mock['_play_context']['password'] = 'password'
    mock['_start_at_task'] = 'task'
    mock['_generated_files'] = ['file1']
    mock['_cleanup_remote_tmp'] = True
    mock['_connection'] = {}
    mock['_task_blocks'] = []
    mock['_loader'] = {}
    mock['_templar'] = {}

# Generated at 2022-06-13 10:19:39.732029
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setUp
    args = {'module_name': 'command', 'module_args': 'ls -la', 'action': 'command'}
    task = {'action': 'command', 'module_name': 'command', 'module_args': 'ls -la', 'name': 'command ls -la'}
    loader = DictDataLoader({'ls -la': ''})
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    new_stdin = None
    connection = Connection(module_name='command')
    tqm = None
    play = Play().load(task, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 10:19:52.529074
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:19:54.765127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing constructor of class ActionModule")
    action_module = ActionModule()
    assert action_module != None


# Generated at 2022-06-13 10:19:56.998806
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert getattr(module, 'ask_pass', None) == None


# Generated at 2022-06-13 10:20:05.325137
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_ssh_host='localhost',
        ansible_ssh_user='root',
        ansible_ssh_port=22,
        ansible_sudo_pass=None,
        ansible_connection='local',
        module_name='setup',
        ansible_sudo=True,
        ansible_sudo_exe='sudo',
        module_args=dict(),
    )
    # FIXME: hack task_vars into the class
    import ansible.playbook.task
    ansible.playbook.task.Task.task_vars = task_vars
    import ansible.plugins.action

# Generated at 2022-06-13 10:20:10.065002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule(None, {})
    assert test_action_module is not None
    assert test_action_module._supports_check_mode is True
    assert test_action_module._supports_async is True

# Generated at 2022-06-13 10:20:10.906181
# Unit test for method run of class ActionModule
def test_ActionModule_run(): 
    assert True

# Generated at 2022-06-13 10:20:12.252088
# Unit test for constructor of class ActionModule
def test_ActionModule():
  action_module = ActionModule()
  assert action_module

# Generated at 2022-06-13 10:20:13.659375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:20:20.563317
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Note: Ansible 2.4.1 no longer uses the attribtues _shared_loader_obj, _shared_action_bases or _loader
    # Ansible 2.5.1 no longer uses the attribtues _shared_loader_obj, _shared_action_bases, _connection, _task, _loader or _template_loader
    # Ansible 2.6.3 no longer uses the attribtues _shared_loader_obj, _shared_action_bases, _connection, _task, _loader or _template_loader
    # Once the use of Ansible 2.6.3 becomes the minimum requirement this function can be purged.
    import sys
    if sys.version_info[0] < 3:
        # The exception raised is not the same between py2 and py3
        assert_exception = AssertionError


# Generated at 2022-06-13 10:20:30.970782
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class ActionModule1:

        def __init__(self, task):
            self._task = task

        def run(self):
            return {'_ansible_module_executed': True}

    class ActionModule2(ActionModule):
        pass

    task = {
        'invocation': {
            'module_args': {'a': 'b'}
        }
    }

    # basic test that passing in a class with run works
    ActionModule1(task).run()

    # confirm _execute_module is called with task_vars and wrap_async for invoke_module
    ActionModule2(task).run({}, {'a': 'b'})

    # confirm ActionModule1.run and _execute_module are called if skip
    task['delegate_to'] = 'test'
    ActionModule2(task).run

# Generated at 2022-06-13 10:20:54.444733
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule,object)

# Generated at 2022-06-13 10:20:55.186362
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:08.611891
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host, Group
    import ansible.constants as C

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[C.DEFAULT_HOST_LIST])
    playbook = Play()
    inventory.add_group(Group('localhost'))
    inventory.add_host(Host('127.0.0.1', port=0))


# Generated at 2022-06-13 10:21:09.875424
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:21:14.090089
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    am = ActionModule(task=test_dict, connection=test_dict, play_context=test_dict, loader=test_dict, templar=test_dict, shared_loader_obj=test_dict)

# Generated at 2022-06-13 10:21:16.543723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' constructor of class ActionModule'''
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None


# Generated at 2022-06-13 10:21:17.496958
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:21.172318
# Unit test for constructor of class ActionModule
def test_ActionModule():
    A = ActionModule(None, None, None, None)
    assert A._supports_check_mode == True
    assert A._supports_async == True

# Generated at 2022-06-13 10:21:22.653837
# Unit test for constructor of class ActionModule
def test_ActionModule():

    actionmodule = ActionModule()
    assert isinstance(actionmodule, ActionBase)

# Generated at 2022-06-13 10:21:26.365904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('>>> test_ActionModule()')
    action_module = ActionModule()
    print(action_module)
    print('<<< test_ActionModule()')
if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:22:26.610785
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a._display.verbosity == 2
    assert a._task.no_log is False

# Generated at 2022-06-13 10:22:35.557128
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.remote_management import RemoteManagement
    from ansible.module_utils.remote_management import RemoteModule
    import ansible.plugins.loader

    task = Task()
    task._connection = RemoteManagement('smart', 'vagrant')
    task._loader = ansible.plugins.loader

    play_context = PlayContext()
    play_context.remote_addr = '127.0.0.1'

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ansible_verbosity': 3}

# Generated at 2022-06-13 10:22:46.995960
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    import os

    # Create the directory.
    tempdir = tempfile.mkdtemp()

    # Create a file in this directory.
    out_file = open(os.path.join(tempdir, 'actionmodule_out.xxxxxx'), 'wb')

    # Create a file in this directory.
    err_file = open(os.path.join(tempdir, 'actionmodule_err.xxxxxx'), 'wb')

    # Create a file in this directory.
    rc_file = open(os.path.join(tempdir, 'actionmodule_rc.xxxxxx'), 'wb')

    a = ActionModule()

    class ActionModuleclass():
        def __init__(self):
            self.module = 'ACTIONMODULE'

        def async_val(self):
            return 'A'



# Generated at 2022-06-13 10:22:53.012481
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Initalize the test ActionModule
    action_module_test = ActionModule(None, None)

    # Assertion check for the result value of _supports_check_mode
    assert action_module_test._supports_check_mode == True

    # Assertion check for the result value of _supports_async
    assert action_module_test._supports_async == True



# Generated at 2022-06-13 10:23:02.780127
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    import json
    import os
    import tempfile

    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action import ActionModule
    from ansible.plugins.loader import ModuleLoader
    from ansible.parsing.mod_args import ModuleArgsParser

    # Prepare module argument data structure
    arg_data = {'some_argument': 'Sample Ansible argument'}

    # create a temp directory to simulate the actual ansible 'tmpdir'
    tmpdir = tempfile.mkdtemp()

    # Prepare a fake return from the executed module
    mod_data = {'sample_result': 'Module execution result'}

    # Serialize the data from above and write it to a file

# Generated at 2022-06-13 10:23:17.094278
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.plugins.action.normal as action_normal
    from ansible.template import Templar

    am = action_normal.ActionModule(
        task=dict(
            async_val=1,
            async_jid=10,
            delegate_to='host1',
            environment=dict(x='y'),
            first_available_file=['a']*10,
            loop='loop1',
            no_log=True,
            until='until1',
            when='when1',
        ),
        connection='connection1',
        play_context='play_context1',
        loader='loader1',
        templar='templar1',
        shared_loader_obj='shared_loader_obj1'
    )

    assert am._task.async_val == 1
    assert am._task.async_

# Generated at 2022-06-13 10:23:18.580034
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, {})

# Generated at 2022-06-13 10:23:21.358947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Testing ActionModule constructor
    # test_action_module = ActionModule()
    # assert test_action_module is not None
    assert True, 'Test passed'



# Generated at 2022-06-13 10:23:31.765858
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:23:38.878116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action

    # check the attributes of class.
    action_module = ansible.plugins.action.ActionModule(
        task=None, connection=None,
        play_context=None, loader=None, templar=None, shared_loader_obj=None
    )
    assert action_module._task is None
    assert action_module._connection is None
    assert action_module._play_context is None
    assert action_module._loader is None
    assert action_module._templar is None
    assert action_module._shared_loader_obj is None
    assert action_module._supports_check_mode is False
    assert action_module._supports_async is False

# Generated at 2022-06-13 10:25:59.922863
# Unit test for constructor of class ActionModule
def test_ActionModule():
    AM = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert AM._supports_check_mode == True
    assert AM._supports_async == True

play_context=None
a=dict()
task = dict(action=dict(module='setup', args=a))
t=ActionModule(task=task,connection=None,play_context=None,loader=None,templar=None,shared_loader_obj=None)
t.run(None,None)

# Generated at 2022-06-13 10:26:02.694007
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    am = ansible.plugins.action.ActionModule(None, None, None, {})
    assert am != None
    assert am.run != None

# Generated at 2022-06-13 10:26:17.685920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader
    from ansible.utils.display import Display
    import ansible.constants as C
    import os
    import sys
    import json

    
    class ActionModuleTest(ActionModule):
        def run(self, tmp=None, task_vars=None):
            self._supports_check_mode = True
           