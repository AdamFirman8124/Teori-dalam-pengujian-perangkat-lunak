

# Generated at 2022-06-13 10:26:54.507473
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 10:27:02.614469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections
    import unittest

    import ansible.plugins.action

    mock_shared_obj = collections.namedtuple('MockSharedObj', ['action_loader'])
    mock_task = collections.namedtuple('MockTask', ['async_val', 'collections', 'args', 'module_defaults', '_parent'])
    mock_play = collections.namedtuple('MockPlay', ['_action_groups'])
    mock_loader = collections.namedtuple('MockModuleLoader', ['has_plugin'])
    mock_connection = collections.namedtuple('MockConnection', ['_shell'])

    class MockTemplar():
        def template(self, arg):
            return arg


# Generated at 2022-06-13 10:27:03.771094
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:27:11.212527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Result object returned by module declares dict object to store result
    '''
    result = dict(
        _ansible_verbose_always=True,
        changed=False,
        failed=False
    )

    # Create module object
    action_module = ActionModule()

    # Create task object
    task = dict(
        async_val=True,
        delegate_to='test',
        args=dict(
            use='auto',
            pattern='test',
            state='test',
            enabled=True,
            name='test',
            reload=True,
            sleep=1
        )
    )

    # Create AnsibleFacts object
    ansible_facts = dict(
        ansible_service_mgr='auto'
    )

    # Create task_vars object
    task_vars = dict

# Generated at 2022-06-13 10:27:22.013817
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ActionModuleMixin
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.service import ActionModule
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import os
    import json

    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    actionModule._connection = Connection(None)

# Generated at 2022-06-13 10:27:22.866642
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:23.459682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:29.676392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    global_vars = dict()
    global_vars["hostvars"] = dict()
    global_vars["hostvars"]["ansible_facts"] = dict()
    global_vars["hostvars"]["ansible_facts"]["service_mgr"] = "redhat"
    action_module.run(tmp=None, task_vars=global_vars)

# Generated at 2022-06-13 10:27:31.648070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    am = ActionModule()
    am.__class__.__call__(am)

# Generated at 2022-06-13 10:27:39.686493
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.connection import Connection
    import ansible.module_utils.service
    module_args = dict(name="sshd", use="auto")
    curr_module = ansible.module_utils.service.Service()
    connection = Connection()

# Generated at 2022-06-13 10:27:46.693159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:27:55.448355
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager

    test_task = {
        'use': 'auto',
        'name': 'test_service',
        'state': 'started'
    }

    # create a basic task object
    task = Task()
    task._role = None
   

# Generated at 2022-06-13 10:27:59.129198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case 1:
    # TODO: Test case 1
    
    # Test case 2:
    # TODO: Test case 2

    pass

# Generated at 2022-06-13 10:28:01.762122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None)
    module._Supports_async = True
    assert module.run() is None

# Generated at 2022-06-13 10:28:03.621015
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ast = ActionModule()
    assert(ast.run() == 'test')

# Generated at 2022-06-13 10:28:14.833380
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' unit testing for ansible.plugins.action.normal.ActionModule '''

    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module.BUILTIN_SVC_MGR_MODULES == {'openwrt_init', 'service', 'systemd', 'sysvinit'}, \
        'test_ActionModule assert#1 has failed.'
    assert module.UNUSED_PARAMS == {'systemd' : ['pattern', 'runlevel', 'sleep', 'arguments', 'args']}, \
        'test_ActionModule assert#2 has failed.'
    assert module.TRANSFERS_FILES is False, 'test_ActionModule assert#3 has failed.'

# Generated at 2022-06-13 10:28:15.826416
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert ActionModule.run() is undefined

# Generated at 2022-06-13 10:28:20.249959
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    adhoc = AnsibleActionModule('{{test}}', {}, {'test': 'test string'})
    assert adhoc.run()['ansible_facts']['test'] == "test string"

    playbook = AnsibleActionModulePlaybook('{{test}}', {}, {'test': 'test string'}, {'a': 'b'})
    assert playbook.run()['a'] == 'b'

# Generated at 2022-06-13 10:28:28.379631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=line-too-long
    class fake_task:
        args = {'name': 'ntpd', 'use': 'auto', 'state': 'restarted'}
        async_val = None

    class fake_args:
        connection = "local"
        diff = False
        remote_tmp = "$HOME/.ansible/tmp/~ansible_unit_test_run"
        debug = False
        run_once = False

    class fake_self:
        _task = fake_task()
        _connection = "local"
        _display = None
        _options = fake_args()
        _shared_loader_obj = None
        _task.async_val = None


# Generated at 2022-06-13 10:28:29.578451
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:28:49.001157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dep_list=[], task=dict(args=dict(name="nginx")))
    assert action.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:28:57.733979
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:29:01.915496
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(ansible={'playbook': 'playbook'}, task={'action': {'module': 'module'}}, connection='connection', play_context={'check_mode': 'check_mode'}, loader='loader', templar='templar', shared_loader_obj='shared_loader_obj')


# Generated at 2022-06-13 10:29:09.421476
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    result = dict()
    tmp = None
    ansible_module_instance = ActionModule()
    ansible_module_instance._shared_loader_obj.module_loader.has_plugin = MagicMock(return_value=False)
    ansible_module_instance._shared_loader_obj.module_loader.find_plugin_with_context = MagicMock(return_value=MagicMock(resolved_fqcn='ansible.legacy.systemd'))
    ansible_module_instance._execute_module = MagicMock(return_value=MagicMock(**{'stdout.find.return_value': -1}))
    ansible_module_instance._supports_check_mode = True
    ansible_module_instance._supports_async = True
    ansible_

# Generated at 2022-06-13 10:29:10.605083
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None

# Generated at 2022-06-13 10:29:19.943126
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    This is a unit test for constructor of class ActionModule
    '''
    mock_loader = MagicMock()
    mock_play = MagicMock()
    mock_play.get_variable_manager.return_value = MagicMock()
    mock_play._variable_manager.get_vars.return_value = dict()
    mock_play.options = MagicMock()
    mock_play.options.host_list = [MagicMock()]
    mock_task = MagicMock()
    mock_task.args = {'use': 'auto', 'name': 'httpd', 'state': 'started', "arguments": "-h -t"}
    mock_task.async_val = 1
    mock_connection = MagicMock()
    mock_connection._shell.tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-13 10:29:26.709100
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with pytest.raises(AnsibleActionFail) as err:
        try:
            if module == 'auto':
                facts = self._execute_module(
                    module_name='ansible.legacy.setup',
                    module_args=dict(gather_subset='!all', filter='ansible_service_mgr'), task_vars=task_vars)
                self._display.debug("Facts %s" % facts)
                module = facts.get('ansible_facts', {}).get('ansible_service_mgr', 'auto')
        except Exception as e:
            raise AnsibleActionFail(e)

# Generated at 2022-06-13 10:29:33.678868
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    test_case={
        # inputs
        "tmp":"???",
        "task_vars":{},
        # expected results 
        "result":{"_ansible_action":None, "_ansible_verbose_always":True, "msg":None},
        # expected exceptions
        "exception_expected":False,
    }
    print("\n")
    print(test_case.get("exception_expected"))
    print("\n")

# Generated at 2022-06-13 10:29:45.564501
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.errors
    from ansible.executor.module_common import get_action_args_with_defaults
    from ansible.module_utils.six import string_types

    # Simple test 1 -test main clause of ActionModule.run
    # Test ansible.module_utils.basic.AnsibleModule.run return value
    module = AnsibleModule()
    actual = module.run()
    expected = {'msg': 'Hello world!'}
    # print("actual = ")
    # pprint(actual)
    # print("expected = ")
    # pprint(expected)
    assert actual['failed'] == False
    assert actual['msg'] == expected['msg']
    # print("Test1 -test main clause of ActionModule.run- Passed")

    # Simple test 2 -test first clause of ActionModule.run


# Generated at 2022-06-13 10:29:46.103322
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:30:14.821817
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)



# Generated at 2022-06-13 10:30:25.542706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os
    import json
    import mock

    sys.modules['ansible'] = mock.Mock()
    sys.modules['ansible.module_utils.six.moves'] = mock.Mock()
    sys.modules['ansible.module_utils.six.moves.input'] = mock.Mock()
    sys.modules['ansible.module_utils.six.moves.builtins'] = mock.Mock()


# Generated at 2022-06-13 10:30:27.829657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, '/tmp/ansible_action')
    assert action is not None

# Generated at 2022-06-13 10:30:30.746237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(action=dict(module='service', use='auto'))
    connection = dict()
    play_context = dict()
    action = ActionModule(task, connection, play_context)

    assert action is not None

# Generated at 2022-06-13 10:30:31.782166
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_plugin = ActionModule()
    assert 1 == 1

# Generated at 2022-06-13 10:30:32.320961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    pass

# Generated at 2022-06-13 10:30:41.135791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Note: test will fail if you try to re-use existing system facts cache file
    # to workaround it, use different value for fact_cache or set fact_cache_type = none in ansible.cfg
    # Also, test will fail if you try to re-use existing system facts cache file created with python2

    module = ActionModule(
        task=dict(args=dict(use='auto')),
        connection=dict(module_implementation_preferences=['ansible.netcommon.network_cli']),
        play_context=dict(become=False),
        loader=None,
        shared_loader_obj=None,
        templar=None,
        task_vars=dict(ansible_facts=dict(service_mgr='auto'))
    )

    # Test with service_mgr defined in task_vars

# Generated at 2022-06-13 10:30:51.859374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import json
    import pytest
    from ansible.plugins.action.service import ActionModule
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 10:30:56.550562
# Unit test for constructor of class ActionModule
def test_ActionModule():
   # create object
   action_module = ActionModule(task=dict(action=dict(module_name="setup")), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

   # Check current module name
   assert action_module._task.action.get('module_name') == 'setup'

# Generated at 2022-06-13 10:31:06.296642
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.my_ansible_module import MyAnsibleModule
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    def play1_data():
        return dict(
                name = "play 1",
                hosts = 'local',
                gather_facts = 'no',
                tasks = [
                    dict(action=dict(module='shell', args='/usr/bin/false'))
                ]
        )


# Generated at 2022-06-13 10:32:12.737284
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:32:15.243474
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(load_plugins=False)
    assert mod.TRANSFERS_FILES is False
    assert mod.UNUSED_PARAMS['systemd'] == ['pattern', 'runlevel', 'sleep', 'arguments', 'args']

# Generated at 2022-06-13 10:32:23.027863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_task = Mock()
    m_task._parent = Mock()
    m_task._parent._play = Mock()
    m_task._parent._play._action_groups = {"all"}
    m_task._parent._play._action_groups = {
        'all': set(['shutdown'])
    }
    m_task._task.async_val = None
    m_task._task.args = {
        'name': 'foo.service', 'state': 'restarted', 'use': 'auto'}
    m_task.module_defaults = set()

    m_loader = Mock()
    m_loader.has_plugin = MagicMock()
    m_task._shared_loader_obj = Mock()
    m_task._shared_loader_obj.module_loader = m_loader

# Generated at 2022-06-13 10:32:24.278521
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of class ActionModule
    action_module = ActionModule()

    # Check method run
    assert action_module

# Generated at 2022-06-13 10:32:27.230434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert type(ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)) == ActionModule


# Generated at 2022-06-13 10:32:28.384016
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule(None, None)
    assert result

# Generated at 2022-06-13 10:32:32.261423
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)
    assert 'transfers_files' in module
    assert not module['transfers_files']
    assert 'UNUSED_PARAMS' in module
    assert 'BUILTIN_SVC_MGR_MODULES' in module

# Generated at 2022-06-13 10:32:34.462981
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, tempfile=None, connection=None)
    assert isinstance(action_module, dict)

# Generated at 2022-06-13 10:32:40.572690
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='service', delegate_to='127.0.0.1', use='auto', args=dict(name='sshd'))),
        connection=dict(),
        play_context=dict(check_mode=True),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert module


# Generated at 2022-06-13 10:32:41.488143
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m is not None

# Generated at 2022-06-13 10:35:03.210577
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.BUILTIN_SVC_MGR_MODULES = set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def has_plugin(self, test):
            if test == "ansible.legacy.openwrt_init":
                return True

            return False

    class FakeLoader(object):
        def __init__(self, *args, **kwargs):
            pass

        @property
        def module_loader(self):
            return FakeModule()

    class FakePlayObj(object):
        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 10:35:04.409416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 10:35:11.242820
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create test module instance
    test_module = ActionModule()

    # Create test module
    test_module_args = {'name': 'test_arguments', 'test_key': 'test_value'}

    # Test the actual module execution
    result = test_module._execute_module(module_args=test_module_args, wrap_async=False)

    # Test the actual module execution
    assert result['name'] == 'test_arguments'

# Generated at 2022-06-13 10:35:17.740579
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:35:20.658620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # FIXME: unit tests for new action plugin
    pass

if __name__ == '__main__':
    # FIXME: unit tests for new action plugin
    pass

# Generated at 2022-06-13 10:35:24.192070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(connection=None, play_context=None,
                            loader=None, templar=None, shared_loader_obj=None) is None

# Generated at 2022-06-13 10:35:37.411719
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import pytest
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Create the data loader
    loader = DataLoader()

    # Create the variable manager
    variable_manager = VariableManager()
    variable_manager.set_variable('ansible_facts',{'service_mgr':'auto'})
    variable_manager.set_variable('hostvars',{'test_host':{'ansible_facts':{'service_mgr':'auto'}}})

    # Create the task queue manager

# Generated at 2022-06-13 10:35:41.962589
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action._task.args['use'] = 'auto'
    result = action.run(tmp='temp_dir', task_vars='task_vars')
    assert isinstance(result, dict)
    assert result['module_args'] == {}
    assert result['module_name'] == 'ansible.legacy.service'


# Generated at 2022-06-13 10:35:44.077457
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(task={"args": ["service"], "name": "service test", "action": "service"})
    assert actionModule is not None

# Generated at 2022-06-13 10:35:45.473837
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ans_runner = AnsibleRunner('/tmp/ansible_test')
    ans_runner.run()
