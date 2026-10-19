

# Generated at 2022-06-13 10:52:51.519523
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict(changed=True, rc=0, cmd=['/bin/echo', '-n', 'hello world'], stdout='hello world', stderr='')
    assert ActionModule().run() == result

    result = dict(changed=True, cmd=['/bin/sh', '-c', u'mkdir -pv /tmp/ansible/file-1-module-with-shell'],
                  stderr=u'',
                  stdout=u'mkdir: cannot create directory \'\'/tmp/ansible/file-1-module-with-shell\': Permission denied\nmkdir: cannot create directory \'\'/tmp/ansible\': Permission denied\n',
                  rc=1)
    assert ActionModule().run() == result

# Generated at 2022-06-13 10:53:05.308758
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  am = ActionModule()

  # the following code was copied from ansible's code base, it is used to
  # mock the run behavior of super()
  # it should be re-written
  class C(object):
    pass
  class D(object):
    def __init__(self, x):
      self.x = x
  class B(C):
    def __init__(self, x):
      super(B, self).__init__()
      self.y = x
  class A(object):
    def __init__(self, y):
      super(A, self).__init__()
      self.z = y
  class E(A, B, D):
    def __init__(self, x, y):
      A.__init__(self, y)

# Generated at 2022-06-13 10:53:05.822586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:14.142153
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.builtin import ActionModule
    from ansible.plugins.action import ActionBase
    from ansible_collections.ansible.community.plugins.module_utils.shell import ShellModule

    module_name = 'native'
    module_path = ('/usr/local/lib/python2.7/dist-packages/ansible_collections/ansible/'
                   'community/plugins/modules/shell/native.py')

# Generated at 2022-06-13 10:53:15.203462
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:53:15.987347
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:26.581529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = {
        'ansible_check_mode': False,
    }
    base_item = ActionModule(
        task={
            'args': {
                '_raw_params': 'echo Hi',
                '_uses_shell': True,
            },
            'delegate_to': None,
            'delegate_facts': False,
        },
        connection={},
        play_context={},
        loader={},
        templar={},
        shared_loader_obj={},
    )
    modified_item = base_item.run(tmp=tmp, task_vars=task_vars)
    assert modified_item['ansible_facts']['cmd_stdout'] == 'Hi\n'

# Generated at 2022-06-13 10:53:31.240199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test with no args
    temp_runner = ActionModule(None, None, None, None, None)
    action_result = temp_runner.run(None, None)
    assert action_result == {'failed': True, 'msg': 'missing required arguments: _raw_params'}


# Generated at 2022-06-13 10:53:40.659164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.process.result import ResultProcess
    from ansible.executor.connection_info import ConnectionInformation
    from ansible.executor.module_common import ADDITIONAL_GLOBAL_VARS, _module_build_id
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.task.copy import ActionModule as copy_ActionModule
    from ansible.plugins.task.shell import ActionModule as shell_ActionModule

# Generated at 2022-06-13 10:53:50.882098
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    task = {
        'args': {
            'chdir': None,
            'creates': None,
            'executable': None,
            'removes': None,
            'warn': True,
            'executable': None,
            'argv': None,
            '_raw_params': 'uptime',
            '_uses_shell': True,
        },
        'loop': '',
        'name': 'shell test',
        'loop_args': {
        },
    }
    task_vars = {}
    result = action.run(task_vars=task_vars, task=task)
    assert result.get('rc') is 0
    assert result.get('delta') == 0
    assert result.get('stdout').find('load averages') != -1


# Generated at 2022-06-13 10:53:55.909889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    runner = ansible.executor.task_executor.ActionModule('shell', {}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert runner.run() == {'alpha': 'beta'}

# Generated at 2022-06-13 10:53:56.972868
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    print (module.run())

# Generated at 2022-06-13 10:54:03.008032
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance of class ActionModule with parameters for initialization
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                                     shared_loader_obj=None)
    # Call method run of class ActionModule
    action_module_obj.run()

# Generated at 2022-06-13 10:54:04.744341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:54:08.363426
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    try:
        action_module.run()
    except Exception as e:
        assert e.args[0] == 'task path not found for connection'

# Generated at 2022-06-13 10:54:08.802296
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:17.272309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.cli import CLI
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.errors import AnsibleParserError
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import action_loader, module_loader, lookup_loader
    from ansible.errors import AnsibleError

# Generated at 2022-06-13 10:54:17.915536
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:20.754810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    aad = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert aad.run(tmp=None, task_vars=None) == 3

# Generated at 2022-06-13 10:54:23.690742
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

if __name__ == "__main__":
    
    # Test method run of class ActionModule
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:39.211508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test run of ansible/plugins/action/shell.py ActionModule"""
    
    TEST_RECORD = [
         {"Item": "bad", "Item Type": "AHH"},
         {"Item": "good", "Item Type": "GOOD"},
         {"Item": "bad", "Item Type": "BAD"},
         {"Item": "good", "Item Type": "GOOD"}
    ]
    
    TEST_TASK = {
        "action": {
            "__ansible_module__": "ansible.legacy.shell",
            "_ansible_parsed": True,
            "__ansible_arguments__": "_raw_params='' _uses_shell=True"
        },
        "failed": False
    }
    
    action_module = ActionModule()
    result = action_module.run

# Generated at 2022-06-13 10:54:48.415086
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader

    from ansible.playbook.task import Task

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play

    from ansible.executor.task_queue_manager import TaskQueueManager

    from units.mock.loader import DictDataLoader

    from units.mock.path import mock_unfrackpath_noop

    from units.compat import unittest
    from units.compat.mock import patch, MagicMock

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            self.loader = DictDataLoader({})


# Generated at 2022-06-13 10:54:49.306414
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:52.775640
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  a = ActionModule()
  b={"_uses_shell": True}
  task_vars = [1,2,3]
  result = a.run(tmp=None, task_vars=task_vars)
  print(result)

# Generated at 2022-06-13 10:54:54.834489
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    # FIXME: Add meaningfull tests!!!
    return action_module.run()

# Generated at 2022-06-13 10:54:57.028904
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Test of method ActionModule.run()')
    # TBD


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:57.607627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:55:01.491859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Tmp: pass

    task_vars = dict()
    tmp = Tmp()
    action_module_obj = ActionModule(tmp, task_vars, None, None, None, None, None, None)
    action_module_obj.run()


# Main
if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:55:07.633508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    # ---------------------------------------------------------------------------------------------
    # Command module is implemented via command with a special arg
    # ---------------------------------------------------------------------------------------------
    # command_action = self._shared_loader_obj.action_loader.get('ansible.legacy.command',
    #                                                            task=self._task,
    #                                                            connection=self._connection,
    #                                                            play_context=self._play_context,
    #                                                            loader=self._loader,
    #                                                            templar=self._templar,
    #                                                            shared_loader_obj=self._shared_loader_obj)
    # result = command_action.run(task_vars=task_vars)


# Generated at 2022-06-13 10:55:09.835011
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None).run()

# Generated at 2022-06-13 10:55:18.020180
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:18.903909
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:19.693138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:20.308196
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:29.163963
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    taskobj = MagicMock(spec = Task)
    conobj = MagicMock(spec = Connection)
    playobj = MagicMock(spec = PlayContext)
    loaderobj = MagicMock(spec = DataLoader)
    templarobj = MagicMock(spec = Templar)

    sharedobj = MagicMock(spec = SharedPluginLoaderObj)
    commandobj = MagicMock(spec = ActionModule)
    taskobj.args = { '_uses_shell': True }

    tmp_obj = ActionModule(taskobj, conobj, playobj, loaderobj, templarobj, sharedobj)
    sharedobj.action_loader.get.return_value = commandobj
    tmp_obj.run(task_vars = {})

# Generated at 2022-06-13 10:55:29.963342
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:55:39.367439
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Import modules under test
    import ansible.plugins.action.legacy
    import ansible.plugins.action.command

    # Create mock module and task
    mock_loader_obj = MagicMock()
    mock_loader_obj.get_basedir.return_value = ""
    mock_loader_obj.get_vars.return_value = {}
    mock_loader_obj.path_dwim.return_value = "path"
    mock_loader_obj.template.return_value = "template"

    mock_task = MagicMock()
    mock_task.args = {}
    mock_task.args['chdir'] = "chdir"
    mock_task.args['creates'] = "creates"
    mock_task.args['executable'] = "executable"

# Generated at 2022-06-13 10:55:39.908919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:55:47.922307
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Unit tests for method run of class ActionModule

    # Mock out a few things
    tmp = None
    task_vars = {}
    act_mod = ActionModule(None, None, None, None, None, None)
    res = act_mod.run(tmp, task_vars)

    assert res is not None
    assert not res['skipped']
    assert res['changed'] is False
    assert res['module_stderr'] == ''
    assert res['module_stdout'] == ''
    assert res['rc'] == 0
    assert res['stderr'] == ''
    assert res['stdout_lines'] == []

# Generated at 2022-06-13 10:55:54.659621
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    # Create an instance of the class
    action = ActionModule()
    
    # Set the _task attribute of the function to an instance of the class:
    # ansible.executor.task_result.TaskResult, so we can access the attribute
    # _result.
    # This code snippet is adopted from the class CommandAction.
    import ansible.playbook.play_context

    play_context = ansible.playbook.play_context.PlayContext()
    import ansible.executor.task_executor
    task_executor = ansible.executor.task_executor.TaskExecutor(host='host_name', task=None, play_context=play_context, variable_manager=None, loader=None)
    action._task = task_executor._task

# Generated at 2022-06-13 10:56:11.224519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:12.431158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    retval = a.run()
    assert retval is None

# Generated at 2022-06-13 10:56:24.891173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Module arguments
    module_args = dict(
        chdir=dict(type='path'),
        creates=dict(type='path'),
        removes=dict(type='path'),
        # Special args
        _raw_params=dict(type='str', no_log=True),
        _uses_shell=dict(type='bool'),
        # General args
        warn=dict(type='bool', default=True),
        executable=dict(type='path', default='/bin/sh'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    # Unit test arguments

# Generated at 2022-06-13 10:56:25.523231
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 10:56:32.894540
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = dict(command = 'echo')
    _shared_loader_obj = dict()
    _loader = dict()
    _templar = dict()
    _play_context = dict()
    connection = dict()
    task_vars = dict()
    self = ActionModule(task=task,
                        connection=connection,
                        play_context=_play_context,
                        loader=_loader,
                        templar=_templar,
                        shared_loader_obj=_shared_loader_obj)
    result = self.run(tmp='tmp', task_vars=task_vars)
    assert result == dict(failed=False,
                          skipped=False)

# Generated at 2022-06-13 10:56:40.899511
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock object, with a mock implementation of the method check_mode()
    # Test function build_command_line when check_mode is False
    mock_task = mock.MagicMock()
    mock_task.action = 'shell'
    mock_task.check_mode = False
    mock_task.args = {
        '_uses_shell': True,
    }
    mock_inject = { 'ansible_check_mode': False }

    # Instantiate the ShellAction module
    action_mod = ActionModule(mock_task, connection=None)
    # Execute method run of class ActionModule
    action_mod.run(task_vars=mock_inject)

    # Check if the method run executed the shell command if check_mode was False
    mock_task.run.assert_called_once()
   

# Generated at 2022-06-13 10:56:42.292339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
    # TODO: unit test for method run of class ActionModule

# Generated at 2022-06-13 10:56:43.639072
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Test run method of class ActionModule.'''

    pass

# Generated at 2022-06-13 10:56:44.403124
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:50.942759
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'localhost'
    conn = 'network_cli'
    port = 2222
    remote_user = 'ansible'
    password = 'ansible'
    action = 'shell'
    command = 'show version'

# Generated at 2022-06-13 10:57:22.281796
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionBase class")

# Generated at 2022-06-13 10:57:22.887418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 10:57:23.309627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:23.948700
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   pass

# Generated at 2022-06-13 10:57:25.356754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:57:26.414893
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	pass


# Generated at 2022-06-13 10:57:36.569617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.shell import ActionModule as ShellModule
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    am = ActionModule(
        Task(),
        variable_manager=VariableManager(loader=None, inventory=InventoryManager(loader=None, sources='')),
        loader=None,
        connection=None,
        play_context=None,
        shared_loader_obj=None,
        templar=None
    )


# Generated at 2022-06-13 10:57:38.159893
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    am = ActionModule()

    assert am.run() == None, "run() should return None"

# Generated at 2022-06-13 10:57:38.988195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()



# Generated at 2022-06-13 10:57:46.278818
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.builtin import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action.command import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task import Task
    from ansible.playbook import Playbook

    # Create task object
    task_obj = Task()
    task_obj._role = None
    task_obj._block = None
    task_obj._play = Play().load({}, variable_manager=VariableManager(), loader=DataLoader())

# Generated at 2022-06-13 10:59:09.829895
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.play_context import PlayContext

    args = ImmutableDict({'_uses_shell': True})
    task = ImmutableDict()
    vm = {}
    vm.name = 'vm-name'

    # Stub out some methods of vm module
    class Connection():
        def __init__(self):
            self.vm = vm

    class AnsibleModule():
        def __init__(self):
            self.params = args
            self.fail_json = self.exit_json = lambda x, y: None

    def loader():
        def get_basedir(*args, **kwargs):
            return 'basedir'
        return {'get_basedir': get_basedir}


# Generated at 2022-06-13 10:59:19.480616
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test_ActionModule_run
    # test case 1:
    # when command module run method with empty args,
    # it is expected that the returned result should be
    # the success with cmd module output

    # test case 2:
    # when command module run method with shell command,
    # it is expected that the returned result should be
    # the success with cmd module output
    print('test_ActionModule_run')

    # test case 1:
    class TestActionBase(ActionBase):
        ''' TestActionBase class'''
        def __init__(self):
            self._task = _task()
            self._connection = _connection()
            self._play_context = _play_context()
            self._loader = _loader()
            self._templar = _templar()
            self._shared_loader_obj = _

# Generated at 2022-06-13 10:59:21.349961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    assert action.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:59:28.979694
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = "127.0.0.1"
    port = 22
    user = "anonymous"
    passwd = "anonymous@"
    remote_user = "root"
    conn = Connection(host, port, user, passwd)
    conn.remote_user = remote_user
    play_context = PlayContext()
    task = Task()
    task.delegate_to = "127.0.0.1"
    action_plugin = ActionModule(task, conn, play_context, loader=None, templar=None, shared_loader_obj=None)
    action_plugin.run(tmp=None, task_vars=None)
    assert action_plugin._task.args['_uses_shell']

# Generated at 2022-06-13 10:59:29.535284
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:34.861525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize the class
    action = ActionModule(
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
        task_vars=None)

    # Return something
    return action

# Generated at 2022-06-13 10:59:35.684177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:59:44.635027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class mock_connection(object):
        def __init__(self):
            self.host = 'test_host'
            self.port = 8888
            self.remote_addr = '127.0.0.1'

    class mock_loader(object):
        def __init__(self):
            self.path_exists = None
            self.file_exists = None

    class mock_shared_loader_obj(object):
        class mock_action_loader(object):
            def get(self, action, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
                return 'test_action_loader'
        action_loader = mock_action_loader()


# Generated at 2022-06-13 10:59:45.140410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:55.709989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock args dictionary
    args = {'_uses_shell': True}

    # Mock the ansible.legacy.command ActionBase and its run() method
    command_action = mock.Mock(ActionBase)
    command_action.run = mock.Mock(return_value='fake-result')
    command_action.run.assert_called_with()

    # Initialize an ActionModule object with mocked ansible.legacy.command and its run() method
    module = ActionModule(command_action)

    # Call run() method on the mocked module
    module.run(task_vars=args)
    module.run.assert_called_with()