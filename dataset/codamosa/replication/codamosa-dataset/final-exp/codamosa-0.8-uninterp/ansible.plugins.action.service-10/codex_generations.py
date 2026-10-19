

# Generated at 2022-06-13 10:26:53.294188
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # HACK: remove this when the method has been implemented
    raise NotImplementedError()

# Generated at 2022-06-13 10:26:56.340156
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit tests method run of class ActionModule'''
    render_template = lambda a, b: a.upper()
    assert render_template('{{ test }}', {}) == '{{ test }}'



# Generated at 2022-06-13 10:26:57.471577
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod is not None

# Generated at 2022-06-13 10:26:58.012117
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:26:58.673568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	pass

# Generated at 2022-06-13 10:27:04.562557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import os

    f = tempfile.NamedTemporaryFile(delete=False)
    f.write("""
    public:
        description:
    """
    )
    f.close()
    
    # TODO: make me work
    # a = ActionModule('test', 'root', None, None, {}, {'tasks': [{'action': 'service', 'hostname': 'test', 'register': 'test', 'use': 'test'}]})
    # a.run()

    os.remove(f.name)

if __name__ == "__main__":
  print("Running unit test for ActionModule class")
  test_ActionModule_run()


# Generated at 2022-06-13 10:27:09.430127
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    action_module = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)

    # Exception handling
    ret = action_module.run(tmp=None, task_vars=None)
    assert ret['failed']

# Generated at 2022-06-13 10:27:14.660978
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #test "default" use case
    # create a task to configure the localhost and set the connection to local
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader=loader))
    task = Task()
    variable_manager.set_loader(loader)
    variable_manager.set_inventory(Inventory(loader=loader))
    task.set_loader(loader)
    host = Host(name='localhost')
    variable_manager.set_host_variable(host, 'ansible_facts', {'service_mgr': 'openwrt/systemd'})
    task.set_variable_manager(variable_manager)
    task.connection = 'local'
    task.args = {}
    task.args['name'] = 'sshd'

# Generated at 2022-06-13 10:27:24.860821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # 1. create object
    action_module = ActionModule()
    sleep_action_args = dict(name='sleep', delay='5', async_val=40, poll=0)
    sleep_task_args = dict(name='sleep', sleep='5', async_val=40, poll=0)
    sleep_task = dict(action=dict(module='command', args=sleep_action_args))
    # 2. run method
    # This method is used to execute the module and get the results
    action_module.execute(sleep_task, sleep_task_args, module_defaults={'remote_tmp':'/tmp'}, wrap_async=40, asynchronous=40)
    # 3. get assertions
    # 4. get return value

# Generated at 2022-06-13 10:27:26.061862
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 10:27:40.330061
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import ansible.plugins.action
    action_mod = ansible.plugins.action.ActionModule(None, None, None, None, None)
    if action_mod._supports_async is None:
        print("TEST FAILED: _supports_async is None")
        sys.exit(1)

    if action_mod._supports_check_mode is None:
        print("TEST FAILED: _supports_check_mode is None")
        sys.exit(1)

    if action_mod.TRANSFERS_FILES is None:
        print("TEST FAILED: TRANSFERS_FILES is None")
        sys.exit(1)


# Generated at 2022-06-13 10:27:50.421905
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' AnsibleModule action class test case for method run '''

    '''
        AnsibleModule test case for method run
    '''

    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    import json


# Generated at 2022-06-13 10:27:52.289685
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(task=dict(action=dict(use="auto")))
    assert a._get_action_name() == 'service'

# Generated at 2022-06-13 10:27:56.218511
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create object of class ActionModule
    actionModule = ActionModule(
        connection = None,
        task = None,
        socket_path = 'None',
        loader = None,
        templar = None,
        shared_loader_obj = None
    )

    # Check type of object
    assert type(actionModule) == ActionModule

# Generated at 2022-06-13 10:28:00.778970
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = MockRunner()
    host.groups.append('rhel')
    action = ActionModule(host, dict(use='auto'))

    # Constructor with use='auto'
    assert action.run(task_vars={}) is not None


# Generated at 2022-06-13 10:28:13.157825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader
    import ansible.constants as C
    options = C.configuration.Options()
    variable_manager = VariableManager()
    loader = module_loader.ModuleLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['local'])
    play_source = dict(
        name="Ansible Play",
        hosts=['local'],
        gather_facts='no',
        tasks=[dict(action=dict(module='apt', args='name=nginx state=installed update_cache=true'))]
    )
    play = Play

# Generated at 2022-06-13 10:28:14.207660
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule('setup').run()

# Generated at 2022-06-13 10:28:19.926665
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.vars.manager import VariableManager

    import os
    import sys
    import tempfile
    import subprocess
    import options
    import inventory
    import constants

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    test_vars = dict(
        os_name=dict(
            ansible_facts=dict(
                service_mgr='systemd'
            )
        )
    )


# Generated at 2022-06-13 10:28:26.411773
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = '127.0.0.1'
    task = 'Ansible task'
    action = 'Ansible action'
    shared_loader_obj = None
    play_context = None
    task_vars = {}
    templar = None
    connection = None

    # object initialization
    action_module_obj = ActionModule(host, task, action, shared_loader_obj, play_context, task_vars, templar, connection)

    # the properties of object
    assert action_module_obj._shared_loader_obj == shared_loader_obj
    assert action_module_obj._task == task
    assert action_module_obj._task_vars == task_vars
    assert action_module_obj._loader == shared_loader_obj
    assert action_module_obj._templar == templ

# Generated at 2022-06-13 10:28:37.057834
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    #module_loader.add_directory(ansible.constants.DEFAULT_MODULE_PATH)
    module_loader.add_directory('a/b')

# Generated at 2022-06-13 10:28:52.154372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:02.846920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.plugins.action.service import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    module_args = {'name': 'jenkins'}
    module_args.update({"key1": "value1", "key2": "value2"})

    task = Task()
    task.action = 'service'
    task.async_val = 2
    task.args = module_args
    task.delegate_to = None
    task._parent = "fake_play"
    task._role = "fake_role"
    task.run_once = False

    setattr(task, '_role', None)

    play_context = PlayContext()
    play_context.check_

# Generated at 2022-06-13 10:29:09.152926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    results = []

    def run_execute_module(*args, **kwargs):
        results.append(dict(
            ansible_facts=dict(
                service_mgr='module',
            )
        ))
        return results.pop()

    def run_not_found_module(*args, **kwargs):
        raise AnsibleActionFail('Could not detect which service manager to use. Try gathering facts or setting the "use" option.')

    def run_invalid_template(*args, **kwargs):
        raise AnsibleAction('Failed to get module')

    # set up required params
    block = Block()
    block.async_val = 1

# Generated at 2022-06-13 10:29:15.466223
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    config = {
        'hostvars': {'testhost':{'ansible_facts':{'service_mgr': 'auto'}}},
        'play': {'playbook_dir': 'playbookFolder'}
    }
    action_module = ActionModule(None)
    ActionModule.run_status = False
    action_module.run(config, None)
    assert ActionModule.run_status == True


ActionModule.run_status = False

# Generated at 2022-06-13 10:29:26.348716
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_args = dict(use='auto', state='started')
    task_vars = dict(
        ansible_facts=dict(service_mgr='sysvinit'),
    )

    module_ret = dict(
        rc=0,
        stdout="status",
        stderr="",
        changed=True,
    )

    m = ActionModule(task=dict(args=task_args), connection=dict(), play_context=dict())

    m._display = Mock()
    m._shared_loader_obj = Mock()
    m._shared_loader_obj.module_loader = Mock()
    m._shared_loader_obj.module_loader.find_plugin_with_context = lambda plugin: mock.MagicMock(resolved_fqcn='ansible.legacy.service')

# Generated at 2022-06-13 10:29:31.856287
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MockTask()
    action = ActionModule(task, MockConnection())
    assert action._task == task
    assert action._connection == MockConnection()
    assert action._templar is None
    assert action._loader is None
    assert action._shared_loader_obj is None
    assert action._display.verbosity == 3
    assert action._supports_check_mode is True
    assert action._supports_async is True
    assert action._supports_async_timeout is False
    assert action._task.__class__.__name__ == 'MockTask'



# Generated at 2022-06-13 10:29:44.841843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test case for module ansible.plugins.action.service"""

    # Unit test for module ansible.plugins.action.service.run_service
    def run_service(self, tmp=None, task_vars=None):
        """Test case for module ansible.plugins.action.service.run_service"""
        self._supports_check_mode = True
        self._supports_async = True

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        module = self._task.args.get('use', 'auto').lower()


# Generated at 2022-06-13 10:29:53.579015
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action.service import ActionModule
    import json
    import os


# Generated at 2022-06-13 10:29:53.995284
# Unit test for method run of class ActionModule
def test_ActionModule_run(): pass

# Generated at 2022-06-13 10:29:54.882762
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:30:27.787590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test normal instantiation
    p = ActionModule()
    assert p is not None
    assert isinstance(p, ActionModule)

    # test constructor with some bad parameters
    try:
        p = ActionModule(123)
        assert False, "should have thrown an exception"
    except TypeError:
        pass

# Generated at 2022-06-13 10:30:36.875059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    facts_vars = dict(
        ansible_facts=dict(service_mgr='auto')
    )
    name = 'test'
    sourced_vars = 'test2'
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=facts_vars,
        loader=None,
        passwords=None,
        stdout_callback='dummy')
    playbook_executor = PlaybookExecutor(
        playbooks=[],
        inventory=None,
        variable_manager=tqm.variable_manager,
        loader=tqm.loader,
        passwords=None,
        stdout_callback=None)

# Generated at 2022-06-13 10:30:38.366948
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am is not None

# Generated at 2022-06-13 10:30:39.267793
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:30:45.142646
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a mock task
    task = MagicMock()
    args = {'pattern': 'a', 'sleep': 'b', 'arguments': 'c', 'args': 'd', 'runlevel': 'e'}
    task.args = args

    # Create a mock action class
    action = ActionModule(task, MagicMock())

    # Create a new task
    new_task = {
        'async': '1',
        'connection': '2',
        'delegate_to': '3',
        'name': '4'
    }

    # Create a new task variables
    result = {
        'changed': '5',
        'failed': '6'
    }

    # Create a mock_execute_module class

# Generated at 2022-06-13 10:30:54.840353
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for ActionModule"""
    task = DummyTask()
    action = ActionModule(task, DummyConnection(), '/tmp', './test/test.txt')
    assert action
    assert action._task is task
    assert action._shared_loader_obj is not None
    assert action._connection is not None
    assert action.BUILTIN_SVC_MGR_MODULES is not None
    assert action.UNUSED_PARAMS is not None
    assert action._loader is not None
    assert action.TRANSFERS_FILES is False
    assert action._supports_check_mode is True
    assert action._supports_async is True

# Generated at 2022-06-13 10:30:55.417117
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:31:06.012803
# Unit test for constructor of class ActionModule
def test_ActionModule():
    data = {
        'args': {},
        'delegate_to': '',
        'async_val': 10,
        'collections': ['my.collections'],
        'module_defaults': {
            'param1': 'value1'
        }
    }

    task_vars = {
        'ansible_facts': {},
        'hostvars': {}
    }

    class TaskObj:
        def __init__(self, data):
            for k, v in data.items():
                setattr(self, k, v)

    class ConnectionObj:
        def __init__(self):
            class ShellMock:
                def __init__(self):
                    self.tmpdir = "/tmp/xxx"

            self._shell = ShellMock()

    connection = ConnectionObj()
   

# Generated at 2022-06-13 10:31:17.323769
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test for module load

    :return:
    """
    from ansible.plugins.action.service import ActionModule
    from ansible.plugins.loader import PluginLoader
    from ansible.module_utils.actions import AnsibleModule
    from ansible.module_utils._text import to_text

    class Connection:

        def __init__(self):
            self._shell = None

    class Shell:

        def __init__(self):
            self.tmpdir = "/tmp"

    con = Connection()
    shell = Shell()
    con._shell = shell
    my_action_module = ActionModule(None, None, True)
    my_action_module._connection = con
    my_action_module._shared_loader_obj = PluginLoader()
    my_action_module._templar = None
    my_action

# Generated at 2022-06-13 10:31:26.630534
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:32:17.944362
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # FIXME
    RemoteModule.test()
    pass

# Generated at 2022-06-13 10:32:22.886975
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None, None, None, None, None)
    assert action_module is not None
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True
    assert action_module.TRANSFERS_FILES is False
    assert action_module.UNUSED_PARAMS is not None
    assert action_module.BUILTIN_SVC_MGR_MODULES is not None

# Generated at 2022-06-13 10:32:24.276053
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
        Unit test to test constructor of class ActionModule
    """
    action_module = ActionModule()

# Generated at 2022-06-13 10:32:24.849884
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ## TODO
    #
    # return
    pass

# Generated at 2022-06-13 10:32:34.077052
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.loader import action_loader

    ActionModule = action_loader.get('service', task=Task(), connection=None, play_context=Play().set_connection_info(None, 'local', None), loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(ActionModule, ActionModule)
    assert isinstance(ActionModule._task, Task)
    assert isinstance(ActionModule._play_context, Play)

# Generated at 2022-06-13 10:32:44.001983
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.module_utils.facts.system.service_mgr import ServiceMgr
    from ansible.module_utils.facts.system.service import Service


# Generated at 2022-06-13 10:32:52.318525
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action.TRANSFERS_FILES == False
    assert action.UNUSED_PARAMS['systemd'] == ['pattern', 'runlevel', 'sleep', 'arguments', 'args']
    assert action.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:32:59.753401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    sys.path.append('..')

    # assign
    result = {'ansible_facts': {}}

    # create a class instance
    action_module = ActionModule()

    # do the test
    result = action_module.run(result)

    # verify
    assert (result['ansible_facts']['service_mgr'] == 'systemd')

# Generated at 2022-06-13 10:33:08.193558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    data = {
        "name": "test",
        "connection": "local",
        "action": "test_service",
        "delegate_to": "",
        "args": {
            "enabled": "yes",
            "state": "started",
            "use": "systemd"
        },
        "module_defaults": {
            "force": "yes"
        },
        "async": 65,
        "poll": 0,
        "sudo": False,
        "sudo_user": "root",
        "transport": "local"
    }

    assert ActionModule(None, data, '/root', 0, 0)

# Generated at 2022-06-13 10:33:14.374311
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=protected-access
    a = ActionModule()
    a._shared_loader_obj = None
    a._task = None
    a._templar = None
    a._connection = None
    a._play_context = None
    a._display = None
    a.set_loader(None)
    # pylint: enable=protected-access
    a.run()

# Generated at 2022-06-13 10:35:32.758442
# Unit test for constructor of class ActionModule
def test_ActionModule():

    task = dict(use="auto")
    task_vars = dict(service_mgr="abc")
    # test with service_mgr in facts
    test_actionModule = ActionModule(task, task_vars)
    assert test_actionModule._execute_module.call_count == 1
    assert test_actionModule.run(None, task_vars) == test_actionModule._execute_module(module_name="ansible.legacy.setup", module_args=dict(gather_subset="!all", filter="ansible_service_mgr"), task_vars=task_vars)

    task_vars = dict()
    # test without service_mgr in facts
    test_actionModule = ActionModule(task, task_vars)

# Generated at 2022-06-13 10:35:42.765040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This function tests the constructor of class ActionModule and it's methods
    """
    from ansible.plugins.action.service import ActionModule
    from ansible.module_utils.common.network import Interface
    from ansible.module_utils.facts.network.base import NetworkCollector

    network = NetworkCollector()

# Generated at 2022-06-13 10:35:43.260419
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return True

# Generated at 2022-06-13 10:35:50.442246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor")
    test_service_params = {
        "backup": False, "changed": True, "created": "/home/jse/.ansible_galaxy/roles/role1", "failed": False, "invocation": {"module_args": {"action": "role1.geerlingguy.java", "name": "role1.geerlingguy.java"}, "module_name": "galaxy"}, "message": "", "name": "role1.geerlingguy.java", "path": "/home/jse/.ansible_galaxy/roles", "role_path": "/home/jse/.ansible_galaxy/roles/role1.geerlingguy.java", "skipped": False, "status": "not-installed", "unmet_dependencies": [], "version": None
    }

# Generated at 2022-06-13 10:35:50.911548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:58.280213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mach = ActionModule(
            task=dict(action=dict(module_name='module', module_args='args')),
            connection='connection',
            tempfile='tempfile',
            runner_Queue='runner_queue',
            play_context='play_context',
            loader='loader',
            templar='templar',
            shared_loader_obj='shared_loader_obj')
    assert mach._task == dict(action=dict(module_name='module', module_args='args'))
    assert mach._connection == 'connection'
    assert mach._templar == 'templar'
    assert mach._shared_loader_obj == 'shared_loader_obj'

# Generated at 2022-06-13 10:36:05.234881
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Constructor test for ansible.plugins.action.service")

    module = ActionModule()
    if hasattr(module, 'TRANSFERS_FILES'):
        print("TRANSFERS_FILES present")
    if hasattr(module, 'UNUSED_PARAMS'):
        print("UNUSED_PARAMS present")
    if hasattr(module, 'BUILTIN_SVC_MGR_MODULES'):
        print("BUILTIN_SVC_MGR_MODULES present")

# Generated at 2022-06-13 10:36:07.622454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test', dict(), False, False, load_plugins=True, runner_queue=None)
    assert ActionModule('test', dict(), False, False, load_plugins=False, runner_queue=None)

# Generated at 2022-06-13 10:36:14.162111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    with patch.object(ActionModule, 'run') as mock_run:
        mock_run.return_value = dict(test_key='test_value')
        assert ActionModule(MagicMock(), MagicMock()).run() == dict(test_key='test_value')

# Generated at 2022-06-13 10:36:22.960746
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Basic testing of action module service
    :return:
    """
    import ansible.plugins.action.service

    # arrange
    action_module = ansible.plugins.action.service.ActionModule(
        MockTask(), MockConnection, MockPlayContext(), MockLoader(), MockTemplar(),
        {
            'use': 'auto'
        }
    )

    action_module.setup_cache()

    # act
    result = action_module.run(None, None)

    # assert
    print(result)

