

# Generated at 2022-06-13 10:52:52.512602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    connection = MockConnection(module)
    connection._connected = True
    play_context = MockPlayContext(connection, module)

    action_module = ActionModule(
        task=MockTask(action='shell', args={}, module=module),
        connection=connection,
        play_context=play_context,
        loader=MockLoader(module),
        templar=MockTemplar(module),
        shared_loader_obj=MockLoader(module),
    )


# Generated at 2022-06-13 10:53:03.822271
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    target_obj = ActionModule()
    target_obj._shared_loader_obj.action_loader.get('ansible.legacy.command').run = lambda *args, **kwargs:\
         {'stdout': 'test_command', 'stdout_lines': ['test_command'], 'output': 'test_command', 'changed': False}
    target_obj._task.args = {'_uses_shell': True}
    target_obj._task.args['chdir'] = 'cd ansible'
    target_obj._task.args['cmds'] = ['python', '-m', 'pytest -s test.py::test_ActionModule_run']

# Generated at 2022-06-13 10:53:08.367745
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_base = ActionBase()
    tmp = None
    task_vars = None
    action_module = ActionModule(action_base, tmp, task_vars)

    result = action_module.run(tmp, task_vars)
    assert result is not None
    assert result["msg"] == "use ANSIBLE_ACTION_PLUGINS"

# Generated at 2022-06-13 10:53:18.618451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Verify the run method of class ActionModule in the ansible/plugins/action directory returns the correct status.
    """
    # setup the test

    module_args = {
        '_raw_params': 'ls -rl /',
        '_uses_shell': True,
        '_uses_delegate': True,
        '_uses_async': True,
        'argv': 'ls -rl /',
    }

    from ansible.plugins.action import ActionModule
    am = ActionModule()
    assert am.run(module_args) is not None

# Generated at 2022-06-13 10:53:21.935373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = action_module.run()

    assert result, "test_ActionModule_run: result is empty"
    #assert result == , "test_ActionModule_run: result should be "

# Generated at 2022-06-13 10:53:27.498569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task.args['_uses_shell'] = True
    module._task.args['_raw_params'] = 'ls'
    assert module.run()['stdout'] == '\n'.join(['__init__.py', '__init__.pyc', 'connection.py', 'connection.pyc', '__main__.py', '__main__.pyc', 'action.py', 'main.py', 'main.pyc', 'main.pyo'])



# Generated at 2022-06-13 10:53:37.186433
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Params for create instance of class ActionModule
    task_vars = dict(
        ansible_connection='winrm',
        ansible_user=dict(
            groups=['vagrant', 'Users', 'BUILTIN\\Users'],
            name='vagrant',
            password='vagrant',
            userId='S-1-5-21-188012312-1742119756-579699057-500'
        ),
        ansible_winrm_server_cert_validation='ignore',
        ansible_winrm_transport='ntlm'
    )
    shared_loader_obj = dict()

    # Unit under test

# Generated at 2022-06-13 10:53:48.230213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None)

    class MockTask:
        def __init__(self, args):
            self.args = args

    class MockLoader:
        def get(self, name1, task, connection, play_context, 
                loader, templar, shared_loader_obj):
            self.name1 = name1
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj

    task = MockTask({})
    mock_loader = MockLoader()
    action_module._task = task
    action_module._shared_loader_obj = mock_loader
    action_module._connection = None
    action_module._play

# Generated at 2022-06-13 10:53:50.881930
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Begin test_ActionModule_run")
    tmp=None
    task_vars=None
    ActionModule.run(tmp, task_vars)
    print("End test_ActionModule_run")

test_ActionModule_run()

# Generated at 2022-06-13 10:53:53.740313
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create an instance of class ActionModule
    action_module = ActionModule()
    tmp = None
    task_vars = {}

    # call method run of action_module with tmp and task_vars
    result = action_module.run(tmp, task_vars)
    assert result['rc'] == 0

# Generated at 2022-06-13 10:54:07.131803
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.module_utils._text import to_bytes
    from ansible.executor.task_queue_manager import TaskQueueManager

    host = 'localhost'
    connection = 'local'
    play_context = 'default'
    loader = 'default'
    templar = 'default'
    shared_loader_obj = 'default'
    name = 'default'
    task_args = {}
    action_args = {'name': name}
    task_vars = {}
    default_args = {}
    action_plugin = ActionModule(host, connection, play_context, loader, templar, shared_loader_obj)
    module_name = 'ansible.legacy.command'

    task_args['_uses_shell'] = True
    action_plugin.run

# Generated at 2022-06-13 10:54:16.460084
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class ActionBase(object):

        def __init__(self, action_loader, action_connection, action_task, action_play_context, action_loader, action_templar, action_shared_loader_obj):

            self._loader = action_loader
            self._connection = action_connection
            self._task = action_task
            self._play_context = action_play_context
            self._templar = action_templar
            self._shared_loader_obj = action_shared_loader_obj

    class test_loader(object):

        def get(self, action_name, task, connection, play_context, loader, templar, shared_loader_obj):

            print("Running test_loader")


# Generated at 2022-06-13 10:54:17.731548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Example test for class ActionModule().
    """
    pass

# Generated at 2022-06-13 10:54:18.396303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:25.563084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.hostvars import HostVarsVarsVars
    from ansible.utils.vars import combine_vars
    import os
    class Runner:
        def __init__(self, vars, basedir=None, verbosity=0):
            self.vars = vars
            self._basedir = basedir

# Generated at 2022-06-13 10:54:34.601047
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(loader=None, 
                          connection=None, 
                          play_context=None, 
                          loader=None, 
                          templar=None, 
                          shared_loader_obj=None)
    command_action = CommandAction(loader=None, 
                                   connection=None, 
                                   play_context=None, 
                                   loader=None, 
                                   templar=None, 
                                   shared_loader_obj=None)
    command_action.task = Task(name='Test', args={'_uses_shell': True})
    module.run()

# Generated at 2022-06-13 10:54:35.230055
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:41.974837
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task.args = {}
    action_module._task.args['_uses_shell'] = True
    action_module._shared_loader_obj.action_loader.get = lambda command, task, connection, play_context, loader, templar, shared_loader_obj: lambda task_vars: True
    assert action_module.run(None, None) == True

# Generated at 2022-06-13 10:54:51.281279
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    options = {
        'ignore_error': True,
        'command': 'ls',
        'shell': '/bin/bash'
    }
    task = {'args': options}
    task_vars = None
    tmp = None
    connection = None
    play_context = None
    loader = None
    shared_loader_obj = None

    action_module = ActionModule(task, connection,
                                 play_context, loader,
                                 tmp, task_vars,
                                 shared_loader_obj)

    result = action_module.run(tmp, task_vars)
    assert isinstance(result, dict)
    assert result['_ansible_verbose_always'] == True
    assert result['rc'] == 0

# Generated at 2022-06-13 10:55:01.214381
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 10:55:08.248341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    task_vars["ansible_verbosity"] = "1"
    action_module = ActionModule("command", "ansible-playbook -i hosts site.yml -vvvv", "", "", "", task_vars)
    print(action_module.run())

# Generated at 2022-06-13 10:55:13.933530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 10:55:15.630682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    assert a.run() == None

# Generated at 2022-06-13 10:55:16.341686
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:17.237748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:27.439185
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestActionModule(ActionModule):
        def __init__(self, loader, connection, play_context, shared_loader_obj, task):
            self._shared_loader_obj = shared_loader_obj
            self._loader = loader
            self._connection = connection
            self._play_context = play_context
            self._task = task
            self._task.args['_uses_shell'] = True

    class TestActionLoader():
        def __init__(self, action_base):
            self.action_base = action_base

        def get(self, *args, **kwargs):
            return self.action_base

    class TestCommandAction():
        def __init__(self, task_vars):
            self._task_vars = task_vars


# Generated at 2022-06-13 10:55:31.353888
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # An instance of the action plugin
    action = ActionModule(None, None, None, None, None, None, None, None, None)

    # A result for a ActionModule
    result = action.run('/tmp/ansible_file.bin', task_vars={'ansible_check_mode': False})
    # Assert that result is not None
    assert result
    # Assert that result is of type dict
    assert isinstance(result, dict)

# Generated at 2022-06-13 10:55:39.367395
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import modules.actions.win_shell
    import ansible.legacy.action
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.vault import VaultLib

    ansible.legacy.action.ACTION_SHARED_LOADER_ARGS['vault_password'] = VaultLib()
    action = modules.actions.win_shell.ActionModule(None, None, {}, {}, {}, None, None, ansible.legacy.action.ACTION_SHARED_LOADER_ARGS)

    assert isinstance(action.run(tmp=None, task_vars={}), MutableMapping)

# Generated at 2022-06-13 10:55:46.599685
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = dict(action = dict(module = 'command', args = dict(command = 'echo "hello world"')), name = 'test_task')
    task_vars = dict()
    results = dict(failed = False, changed = False, msg = 'hello world')

    action_mod = ActionModule(task = task, connection = None, play_context = None, loader = None, templar = None,
                              shared_loader_obj = None)

    assert action_mod.run(task_vars = task_vars) == results

# Generated at 2022-06-13 10:55:52.924274
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(ansible_distribution_version='1.0.3', ansible_version='1.0.3')
    tmp = None
    result = ActionModule(None, None, None, None, None, None).run(tmp, task_vars)
    assert result == dict(ansible_facts=dict(ansible_distribution_version='1.0.3', ansible_version='1.0.3'),
                          ansible_facts_modified=False, changed=False, rc=0, stderr='', stdout='')

# Generated at 2022-06-13 10:56:00.278397
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            _raw_params='raw_params_value',
            _uses_shell='uses_shell_value',
        )
    )

    assert module._task.args['_raw_params'] == 'raw_params_value'
    assert module._task.args['_uses_shell'] == 'uses_shell_value'

# Generated at 2022-06-13 10:56:02.007596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:02.655292
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:56:04.321651
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    assert am.run() == 'test'

# Generated at 2022-06-13 10:56:13.572464
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	from task import Task
	from play_context import PlayContext
	from ansible.parsing.dataloader import DataLoader
	from ansible.vars.manager import VariableManager
	from ansible.inventory.manager import InventoryManager
	from ansible.module_utils.common.collections import ImmutableDict
	from ansible.executor import playbook_executor

	from ansible.module_utils._text import to_bytes
	from ansible.plugins.action import ActionBase
	from ansible.plugins.action import ActionModule
	from ansible.action.command import ActionModule as AssemblyActionModule
	from ansible.errors import AnsibleError
	from ansible.errors import AnsibleActionFail

	from ansible.playbook.play import Play
	from ansible.playbook.task import Task as AssemblyTask

# Generated at 2022-06-13 10:56:23.614559
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.shell import ActionModule
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_result import TaskResult
    from ansible.vars.clean import module_response_deepcopy
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins import connection_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.plugins.vars import vars_loader
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 10:56:26.868093
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    p = ActionModule(name='test.yml',connection='local',play_context={},loader=None,templar=None,shared_loader_obj=None)
    assert p.run() == "hello"

# Generated at 2022-06-13 10:56:28.313935
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    command_action_module = CommandActionModule()
    command_action_module.run()
    assert command_action_module

# Generated at 2022-06-13 10:56:33.682141
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    obj = ActionModule(ActionBase())
    tmp = ''
    task_vars = {'var':'value'}
    res = obj.run(tmp, task_vars)
    assert res == {'var':'value', 'changed': False, 'failed': False, 'msg': '', 'rc': 0}

# Generated at 2022-06-13 10:56:41.432358
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Run this unit test with option:
    #   python3 -m pytest -s test_action_module.py
    #   or
    #   python2 -m pytest -s test_action_module.py
    # Following output is expected:
    #   {'result': {u'ansible_facts': {u'command_invocation': {u'module_args': u'ls', u'command': u'/bin/ls'}, u'debug': {u'changed': True}, u'changed': True}, 'changed': True, 'cmd': ['/bin/ls']}}
    # Note that if there are no errors, ansible_facts.debug has dict {'changed': True}.
    from collections import namedtuple
    from ansible.module_utils import basic

    # Setup test data

# Generated at 2022-06-13 10:56:51.140535
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:51.762318
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:53.134280
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.run()

# Generated at 2022-06-13 10:56:53.787096
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:02.648248
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    from ansible import context
    from ansible.executor import task_queue_manager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.action.command import ActionModule
    from ansible.template import Templar

    import os
    import test.support

    # TODO: get this from a global variable
    # This path is relative to the source code for Ansible

# Generated at 2022-06-13 10:57:04.253191
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # DOCUMENT ME
    pass

# Generated at 2022-06-13 10:57:14.920971
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    module = ActionModule()
    task_vars = {'ansible_check_mode': False, 'module_setup': True}

    module._task.args['_raw_params'] = ''
    result = module.run(tmp=None, task_vars=task_vars)
    assert result['rc'] == 0
    assert 'failed' not in result['stdout']
    assert 'failed' not in result['stderr']

    module._task.args['_raw_params'] = 'echo "Hello World" > /tmp/helloworld'
    result = module.run(tmp=None, task_vars=task_vars)
    assert result['rc'] == 0
    assert 'failed' not in result['stdout']

# Generated at 2022-06-13 10:57:15.505257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:16.108879
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:25.344986
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define parameters that would normally be passed to the method
    tmp = 'temp file'
    task_vars = {'var1': 'value1'}
    result = {'ansible_facts': 'answer1'}
    # Define mock objects used by the action
    action_name = 'module_name'
    connection = 'conn'
    class Task():
        def __init__(self):
            self.args = {'_uses_shell': True}
    class ActionLoader():
        def get(self, name, task, connection, play_context, loader, templar, shared_loader_obj):
            self.name = name
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
           

# Generated at 2022-06-13 10:57:42.143933
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:48.652101
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor import task_queue_manager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash
    from ansible.vars.reserved import reserved_vars

    loader = DataLoader()
    templar = Templar(loader=loader)

    #values as declared in example YAML playbook
    basic_inventory_dict = {"all": {"vars": {"ansible_connection": "local"}}}

    #values as declared in example YAML playbook

# Generated at 2022-06-13 10:57:50.472802
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Checking method run of class ActionModule")
    assert False

# Generated at 2022-06-13 10:58:01.373952
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None, task=None)

    action._task.args = {
        '_uses_shell': True,
        'chdir': '/home/vagrant',
        'creates': '/home/vagrant/demo.txt',
        'executable': None,
        'removes': '/home/vagrant/demo.txt',
        'warn': True
    }

    result = action.run(task_vars={
        'ansible_play_batch': 'localhost',
        'ansible_play_hosts': 'localhost',
        'ansible_play_uid': 'vagrant'
    })
    assert result == {}

# Generated at 2022-06-13 10:58:03.104323
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    result = action.run()
    assert result is None

# Generated at 2022-06-13 10:58:03.807764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:06.547658
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock the object attributes
    action_module_obj = ActionModule()
    action_module_obj.run()
    # test the results

# Generated at 2022-06-13 10:58:07.248757
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:58:18.974558
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.error import AnsibleUndefinedVariable
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.module_utils.facts import FactCache
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import module_loader

    variable_manager = VariableManager()

# Generated at 2022-06-13 10:58:24.590079
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit test for method run of class ActionModule
    # TODO: No tests yet
    return
##############################################################################
if __name__ == '__main__':
    # Unit test for method run of class ActionModule
    test_ActionModule_run()


#     def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):

# Generated at 2022-06-13 10:59:07.916667
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    run_method = ActionModule.run

    def run(task_vars=None):
        return run_method({}, task_vars)

    result = run()
    assert result['rc'] == 1

    counter = [0]

    def _execute_module(*args, **kwargs):
        counter[0] += 1
     

# Generated at 2022-06-13 10:59:10.555179
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test normal case
    ActionModule_run()

    # test case: command_action.run() raises an exception
    ActionModule_run_exc()


# Generated at 2022-06-13 10:59:11.204393
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:12.120731
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    t = ActionModule()
    t.run()

# Generated at 2022-06-13 10:59:13.742299
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule({}, {}, {})
    res = m.run()
    assert(res)

# Generated at 2022-06-13 10:59:21.781185
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup mocks
    task_vars = {}
    tmp = None
    mock_task = Mock()
    mock_task.args = {'_uses_shell': True}
    mock_connection = Mock()
    mock_play_context = Mock()
    mock_loader = Mock()
    mock_templar = Mock()
    mock_shared_loader_obj = Mock()

    mock_command_action = Mock()
    mock_command_action.run.return_value = 'test'
    mock_shared_loader_obj.action_loader.get \
        .return_value = mock_command_action

    # Create ActionModule object and call run with mocked args

# Generated at 2022-06-13 10:59:29.803487
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    from ansible.vars import VariableManager
    from ansible.executor import playbook_executor
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.callback import CallbackBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play


    loader = DataLoader()
    variable_manager = VariableManager()

    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1")

    class CallbackModule(CallbackBase):
        pass
    
    #

# Generated at 2022-06-13 10:59:30.616052
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:59:31.402461
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:32.254736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 11:01:20.088838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common import read_csv_values
    from ansible.module_utils.six.moves import zip as izip
    from ansible.module_utils.six.moves import range

    from ansible.module_utils.common._text import to_bytes
    from ansible.errors import AnsibleParserError
    from ansible.plugins.action.template import ActionModule as TemplateModule
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

# Generated at 2022-06-13 11:01:20.904348
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:21.658265
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:22.245554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:26.959532
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = None
    module._connection = None
    module._play_context = None
    module._loader = None
    module._templar = None
    module._shared_loader_obj = None
    result = module.run()

    assert result.keys() == ['msg']
    assert 'shell module has been moved to ansible.legacy.shell' in result['msg']

# Generated at 2022-06-13 11:01:29.423011
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	action_module = ActionModule()
	result = action_module.run(tmp=None, task_vars=None)
	return result

# Generated at 2022-06-13 11:01:38.174494
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars, load_extra_vars
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    from ansible.errors import AnsibleParserError
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.normal import ActionModule as normal

    import os
    import tempfile
    import sub

# Generated at 2022-06-13 11:01:38.697379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()

# Generated at 2022-06-13 11:01:40.949889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO(ggap)
    # assert result == expected
    pass

# Generated at 2022-06-13 11:01:46.611210
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test string to configure the following variable
    # action.ActionModule.run
    x = 0

    # Test string to configure the following variable
    # action.ActionModule.run
    y = 1

    # Test string to configure the following variable
    # action.ActionModule.run
    z = 2

    import ansible.plugins.action
    class TestActionModule(ansible.plugins.action.ActionModule):
        def run(self, x):
            print(x)

    # Test string to configure the following variable
    # action.ActionModule.run
    def put():
        # Test string to configure the following variable
        # action.ActionModule.run
        return "Hello World"

    # Test string to configure the following variable
    # action.ActionModule.run
    obj = TestActionModule()

    # Test string to configure the following variable