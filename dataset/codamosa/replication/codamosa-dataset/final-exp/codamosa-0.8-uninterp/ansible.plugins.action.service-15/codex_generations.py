

# Generated at 2022-06-13 10:26:59.183157
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing test_ActionModule_run")
    import ansible.modules.system.service
    import ansible.module_utils.basic
    task = ansible.modules.system.service.ActionModule({'name': 'ntpd', 'state': 'started'}, {'ansible_facts': {'service_mgr': 'openwrt'}})
    task.run()


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:27:05.582677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = {}
    task = {}
    args = {}
    args['use'] = 'auto'
    host['module_name'] = 'service'
    host['module_defaults'] = {}
    host['module_defaults']['use'] = 'auto'
    host['module_defaults']['name'] = 'sname'
    host['module_defaults']['state'] = 'state'
    host['module_defaults']['enabled'] = 'enabled'
    host['module_defaults']['pattern'] = 'pattern'
    host['module_defaults']['runlevel'] = 'runlevel'
    host['module_defaults']['sleep'] = 'sleep'
    host['module_defaults']['arguments'] = 'arguments'

# Generated at 2022-06-13 10:27:06.150548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:09.999202
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_task = dict(name='test_task', action='auto')
    my_task.action = auto(my_task, {},[])
    assert my_task.action.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:27:20.950547
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.local import LocalAnsibleModule

    module_args = dict(
        use='auto'
    )
    set_module_args(module_args)
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default='running',
                       choices=['stopped', 'started', 'restarted', 'reloaded', 'restarted']),
            enabled=dict(type='bool', default='yes'),
            name=dict(required=True),
        ),
        supports_check_mode=True,
    )

    context = PlayContext()

    mod = ActionModule(module, LocalAnsibleModule, context)
    result = mod.run({'service_mgr': 'init'})

# Generated at 2022-06-13 10:27:23.093394
# Unit test for constructor of class ActionModule
def test_ActionModule():

    ac = ActionModule()
    assert ac.run() == ac

# Generated at 2022-06-13 10:27:24.549173
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert(module.run() == None)

# Generated at 2022-06-13 10:27:34.900377
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # sample_task is the task object created from sample service.yaml
    sample_task = {
        'version': 2,
        '_attributes': {
            'name': 'sample service',
            'use': 'auto',
            'state': 'started'
        },
        'name': 'sample service',
        'use': 'auto',
        'state': 'started'
    }
    # sample_task_vars is the task vars received in the main run loop
    sample_task_vars = {
        'ansible_facts': {
            'ansible_service_mgr': 'auto'
        }
    }
    # sample_task_vars_service is the task vars received in the main run loop

# Generated at 2022-06-13 10:27:46.228441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.runner.connection_plugins.local import Connection
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.dataloader import DataLoader
    import json
    import os
    import pytest
    import sys

    if sys.version_info < (3, 0):
        import mock
    else:
        from unittest import mock

    def get_mock_task(collections=[]):
        mock_task = mock.Mock()
        if mock_task._task.collections != collections:
            mock_task._task.collections += collections
        mock_task._task.args = dict(name='foo',state='present',enable='yes')

# Generated at 2022-06-13 10:27:53.016631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a mock task and connection and
    # create a ActionModule object with it
    task_args = {"use":"systemd", "name":"nginx"}
    mock_task = MockTask(args=task_args)
    mock_connection = MockConnection()
    action_module = ActionModule(task=mock_task, connection=mock_connection)
    # execute method run
    action_module.run()
    # test if run method was executed
    assert action_module._execute_module.call_count == 1
    for call in action_module._execute_module.call_args:
        assert call == ()


# Generated at 2022-06-13 10:28:04.656477
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()
    assert module._task.args.get('use', 'auto').lower() == 'auto'
    assert module._templar.template('{{ansible_facts.service_mgr}}') == 'auto'
    assert module._task.async_val == 0

# Generated at 2022-06-13 10:28:05.955017
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert callable(ActionModule.run)

# Generated at 2022-06-13 10:28:07.052791
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:28:17.196745
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test basic create
    am = ActionModule(None, None, None)
    assert am
    # test if hasattr
    assert hasattr(am, 'run')
    assert hasattr(am, '_supports_async')
    assert hasattr(am, '_supports_check_mode')
    assert hasattr(am, '_display')
    assert hasattr(am, '_task')
    assert hasattr(am, '_connection')
    assert hasattr(am, '_shell')
    assert hasattr(am, '_loader')
    assert hasattr(am, '_templar')
    assert hasattr(am, '_shared_loader_obj')
    assert hasattr(am, '_play_context')
    assert hasattr(am, '_task_vars')

# Generated at 2022-06-13 10:28:18.243599
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Write unit test here
    pass

# Generated at 2022-06-13 10:28:25.438549
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:28:36.279553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    #The function will fail without a module named 'test'
    _shared_loader_obj = 'test'
    _connection = 'test'

    TaskVars_ = {'hostvars': {'localhost': {'ansible_facts': {'service_mgr': 'auto'}}}}
    TaskVars = json.dumps(TaskVars_)

    #The function will fail without a task named 'test'
    _task = {'delegate_to': 'localhost', 'args': {}, 'async_val': 'test', 'use': 'auto'}

    #The function will fail without a task named 'test'
    _display = {'vvvv': 'test', 'debug': 'test'}

    #The function will fail without a task named 'test'
    _templar = 'test'

   

# Generated at 2022-06-13 10:28:37.630207
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None), ActionModule)

# Generated at 2022-06-13 10:28:38.210406
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:48.095878
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModuleTest(ActionModule):

        RUN_RETURN = {'key':'value'}

        def run(self, tmp=None, task_vars=None):
            return self.RUN_RETURN

    class ActionModuleTest1(ActionModuleTest):
        RUN_RETURN = {'key':'value', 'ansible_facts': {'ansible_service_mgr': 'auto'}}

    class ActionModuleTest2(ActionModuleTest):
        RUN_RETURN = {'key':'value', 'ansible_facts': {}}

    class ActionModuleTest3(ActionModuleTest):
        RUN_RETURN = {'key':'value', 'ansible_facts': {'ansible_service_mgr': 'auto', 'ansible_processor': 'i386'}}


# Generated at 2022-06-13 10:29:08.537123
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native

    action = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=None, templar=None, shared_loader_obj=None)
    assert not action._supports_check_mode

    task = MagicMock()
    task._parent = MagicMock()
    task._parent.name = 'setup'
    task._parent._play = MagicMock()
    task._parent._play.name = 'testing-123'
    task._parent._play._action_groups = {'setup': {'module_defaults': {'path': '/my/path'}}}

# Generated at 2022-06-13 10:29:16.292763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Parsing an empty Task into a Module
    action = ActionModule(task=dict())
    assert action
    assert action._task.action == 'service'
    assert action._task.async_val == 0
    assert action._task.async_seconds == 0
    assert action._task.delegate_to is None
    assert action._task.delegate_facts is False
    assert action._task.delegate_to_host is None
    assert action._task.name == 'service'
    assert action._task.subset is None
    assert action._task.module_vars is None

# Generated at 2022-06-13 10:29:16.909871
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:20.259854
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global action_module
    global action_loader
    global module_loader
    global display
    global task
    display = Display()
    action_loader = ActionLoader(None, '', None, display)
    module_loader = ModuleLoader(None, action_loader, display)
    task = Task()
    action_module = ActionModule(task, connection=None, play_context=None, loader=module_loader, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:29:28.640902
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:29:39.600868
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = dict(
        async_val = 'test_async',
        args = dict(
            state = 'test_state',
            use = 'test_use'
        ),
        delegate_to = None,
        _parent = dict(
            _play = dict(
                _action_groups = dict()
            )
        )
    )
    action_module = ActionModule(mock_task, dict())
    assert action_module._task.async_val == 'test_async' and \
        action_module._task.args.get('use') == 'test_use'

# Generated at 2022-06-13 10:29:41.182142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    # TODO: implemented test

# Generated at 2022-06-13 10:29:48.997268
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import connection_loader
    from ansible.module_utils.common.removed import removed_module
    from ansible.utils.display import Display
    adhoc_manager = connection_loader.get('local')('testhost', 'testuser')
    display = Display()
    ac = ActionModule(adhoc_manager, '/tmp/test', {}, display, removed_module, 'test.setup')
    assert ac
    assert ac.noop_flag is False

# Generated at 2022-06-13 10:29:58.163715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    print("ActionModule test")
    print("ActionModule UNUSED_PARAMS:", am.UNUSED_PARAMS)
    print("ActionModule BUILTIN_SVC_MGR_MODULES:", am.BUILTIN_SVC_MGR_MODULES)

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:30:06.504672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import yaml
    from ansible import context
    from ansible.cli.playbook.playbook_cli import PlaybookCLI
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.removed import removed_module

    from io import StringIO

    # 1. Setup
    my_cli = PlaybookCLI(['/bin/true'])
    my_cli.options = {'inventory': 'localhost,'}
    context.CLIARGS = my_cli.parse()

    inventory = InventoryManager(my_cli.options.inventory, my_cli.options, support_newlines=True)

# Generated at 2022-06-13 10:30:41.135691
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, {}, None, None)
    assert mod.TRANSFERS_FILES is False
    assert mod.UNUSED_PARAMS is None
    assert mod.BUILTIN_SVC_MGR_MODULES is None

# Generated at 2022-06-13 10:30:42.290127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None, None)
    assert action_module != None

# Generated at 2022-06-13 10:30:45.833262
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        'setup',
        {'use': 'auto'},
        False,
        None,
        None,
        None,
        None,
        None,
        None
    )
    module.run()

# Generated at 2022-06-13 10:30:48.297420
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_obj = ActionModule(
        tasks=[{
            'action': {
                '__ansible_module__': 'ansible.module_service'
            },
            'loop': None,
            'name': 'my task',
        }],
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert test_obj is not None

# Generated at 2022-06-13 10:30:49.416429
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:30:51.045680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup test objects
    action_module = ActionModule()

    # TODO: unit test
    pass

# Generated at 2022-06-13 10:30:55.337803
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.plugins.action.service import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    from ansible.errors import AnsibleError
    TESTING_ANSIBLE_ERROR = 'TESTING ANSIBLE ERROR'

    def get_task_queue_manager(**kwargs):
        return TaskQueueManager(
            stdout_callback=None,
            **kwargs
        )


# Generated at 2022-06-13 10:31:01.373439
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    temp=None
    test_task_vars={
        'ansible_facts': {},
        'ansible_service_mgr': 'systemd',
        'hostvars': {
            'localhost': {
                'ansible_facts': {
                    'service_mgr': 'systemd'
                }
            }
        }
    }

    test_task_args={
        'use': 'auto',
        'name': 'nginx',
        'state': 'started',
        'enabled': True
    }

    test_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    test_action_module._task.args=test_task_args
    test_action_module._task.delegate

# Generated at 2022-06-13 10:31:04.060141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = 'service'
    action_module = ActionModule(None, {'use': module})
    assert action_module._task.args['use'] == module

# Generated at 2022-06-13 10:31:07.890174
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(action='test'),
                        connection=None,
                        play_context=None,
                        loader=None,
                        templar=None,
                        shared_loader_obj=None)


# Generated at 2022-06-13 10:32:04.524517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule class, which is the constructor
    # of the class, and then test if some of its properties exist
    action_module_instance = ActionModule()

    assert action_module_instance.TRANSFERS_FILES == False

    assert action_module_instance._supports_check_mode == True

    assert action_module_instance._supports_async == True

# Generated at 2022-06-13 10:32:12.140688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import copy
    import json
    import os

    from ansible.plugins.action.service import ActionModule
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task

    class HostFake(Host):
        def __init__(self, *args, **kwargs):
            super(HostFake, self).__init__(*args, **kwargs)
            self.name = "fake"

    class TaskFake(Task):
        def __init__(self, *args, **kwargs):
            super(TaskFake, self).__init__(*args, **kwargs)
            self.args = {
                'arg1': 'value1',
                'arg2': 'value2',
            }


# Generated at 2022-06-13 10:32:19.588773
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:32:27.064731
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  print("test_ActionModule_run")
  f = open("../../ansible/test/units/module_utils/_text.py", "r")
  t = f.read()
  f.close()
  import runpy
  ns = runpy.run_path("./ansible/test/units/modules/net_tools/test_service.py", init_globals=dict(__file__="./ansible/test/units/modules/net_tools/test_service.py"))
  ns["args"] = dict(name = "httpd")

  exec (t, ns)

# Generated at 2022-06-13 10:32:27.609059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:32:30.525694
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_plugin

# Generated at 2022-06-13 10:32:31.193044
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    assert True

# Generated at 2022-06-13 10:32:35.198904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = {
        'version': 2,
        'use': 'auto',
        'args': {
            'name': 'zabbix-agent',
            'enabled': True,
            'state': 'started'
        }
    }
    module = ActionModule(task, {}, {'ANSIBLE_MODULE_ARGS': {}})
    assert module._task == task
    assert not module._shared_loader_obj.module_loader.has_plugin('service')
    assert module._shared_loader_obj.module_loader.has_plugin('ansible.legacy.service')

# Generated at 2022-06-13 10:32:44.001401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task = AnsibleTaskMock()
    mock_task.method = 'service'
    mock_task.args = {
        'name': 'httpd',
        'state': 'started',
        'enabled': True
    }

    module = ActionModule(mock_task)
    res = module.run(tmp='/tmp', task_vars=None)
    assert res is not None
    assert 'invocation' in res
    assert 'module_args' in res['invocation']
    assert res['invocation']['module_args'] == {
        'name': 'httpd',
        'enabled': True,
        'state': 'started'
    }


# Generated at 2022-06-13 10:32:45.088168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:35:02.440442
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:35:16.493611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.color import ANSIBLE_COLOR, stringc
    from ansible_collections.ansible.legacy.plugins.modules.system import service as service_module
    from ansible_collections.ansible.legacy.plugins.module_utils._text import to_text
    import os

# Generated at 2022-06-13 10:35:18.186778
# Unit test for constructor of class ActionModule
def test_ActionModule():
    atm = ActionModule()
    # Call parent constructor, this will just return None
    atm.run()

# Generated at 2022-06-13 10:35:18.760822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:25.471863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from Ansiballz import AnsiballzMethod
    from ansible.module_utils.six.moves import StringIO

    import ansible.module_utils.six as six

    # Create a dummy module and task, we won't actually use the module
    module = AnsiballzMethod(
        "ansible.legacy.service",
        "ActionModule",
        _uses_shell=True, _uses_unsafe_shell=False,
        _uses_terminal=False, _uses_delegate=False, _uses_expand=False,
        _uses_subprocess=True
    )

    # Complex args are not supported in Ansiballz right now
    del module._task.args['use']

    module._shared_loader_obj = StringIO()

# Generated at 2022-06-13 10:35:26.195465
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:30.069535
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({
        'use': 'auto',
        'name': 'ansible'
    }, {}, {}, {}, {})

    assert action is not None

# Generated at 2022-06-13 10:35:30.805238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:41.744427
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import get_action_args_with_defaults
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import plugin_loader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.display import Display



# Generated at 2022-06-13 10:35:42.582575
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO: Write a unit test