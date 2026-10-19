

# Generated at 2022-06-13 10:26:53.247302
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:26:57.146448
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:26:59.030342
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:27:02.030879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task={'args': {}, 'task_action': 'setup'}, connection=None, tmp=None, share_loader_obj=None, task_vars=None, templar=None, remove_tmp_path=None, play_context=None)
    return action_module

# Generated at 2022-06-13 10:27:02.938269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ansible.plugins.action.service.ActionModule.run()
    """

# Generated at 2022-06-13 10:27:10.826697
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # mock object for arguments passed to ActionModule class constructor
    mock_task = mock.Mock()
    mock_task.args = {'use': 'auto'}

    mock_task.async_val = True
    mock_task.action = 'service'
    mock_task.delegate_to = None
    mock_task.get_args = mock.Mock(return_value=mock_task.args)

    # mock object for connection and module_loader attributes of the task
    mock_connection = mock.Mock()
    mock_connection._shell.tmpdir = '/test/test/test/test'
    mock_task._parent = mock.Mock()
    mock_task._parent._play = mock.Mock()
    mock_task._parent._play._action_groups = {}
    mock_task.collections = None

# Generated at 2022-06-13 10:27:21.727561
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test setup

    # Create test case
    test_case = {}
    test_case['action'] = 'service'

    module = 'auto'
    test_case['args'] = {'name': 'sshd',
                         'state': 'started',
                         'use': module}

    test_case['config'] = {'action': 'service'}

    class MockTemplar:
        def __init__(self, delegate_to):
            self.delegate_to = delegate_to

        def template(self, expr):
            if self.delegate_to == 'delegate_host':
                if expr != "{{hostvars['delegate_host']['ansible_facts']['service_mgr']}}":
                    raise Exception("Unexpected template expression: `%s`" % expr)
                return 'service'

# Generated at 2022-06-13 10:27:23.917737
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    task_vars["ansible_facts"] = {"service_mgr": "auto"}
    module = ActionModule(
            {"use": "auto"},
            task_vars=task_vars)
    assert module.run()

# Generated at 2022-06-13 10:27:28.582028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ModuleData is stubbed as dict for this unit test
    module_data = dict()
    action_module = ActionModule(module_data, 'tasks', 'tasks', 'tasks', 'tasks', 'tasks', 'tasks', 'tasks')
    assert action_module._shared_loader_obj

# Generated at 2022-06-13 10:27:37.733151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Init vars
    module_name = 'ansible.legacy.service'
    module_args = dict(action='start')
    task_vars = dict()
    tmp = None
    wrap_async = None

    # Init objects
    loader_mock = mock.Mock()
    shared_loader_mock = mock.Mock()
    connection_mock = mock.Mock()
    task_mock = mock.Mock()
    task_mock._parent = mock.Mock()
    task_mock._parent._play = mock.Mock()
    task_mock._parent._play._action_groups = mock.Mock()
    templar_mock = mock.Mock()
    display_mock = mock.Mock()
    action_module_mock = mock.Mock()

# Generated at 2022-06-13 10:27:51.881523
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import shutil
    import tempfile
    import json
    from ansible.plugins.action import ActionModule
    from ansible.parsing.dataloader import DataLoader
    dataloader = DataLoader()
    module_loader = None
    connection = None
    task_vars = {'ansible_service_mgr':'systemd'}
    task_args = {'name':'vsftpd', 'use':'auto'}
    tmp = tempfile.mkdtemp()
    action_module = ActionModule(connection, dataloader, task_vars, tmp, module_loader)
    action_module._task.args = task_args
    result = action_module.run(tmp, task_vars)
    shutil.rmtree(tmp)
    assert result

# Generated at 2022-06-13 10:27:54.156411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    #Initiate the class object
    ActionModule_obj = ActionModule()

    assert True == (ActionModule_obj.run() is not None)

# Generated at 2022-06-13 10:27:54.671989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:28:02.423560
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # action1 is an object of ActionModule class
    action1 = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # action1 is an object of ActionModule class
    action2 = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert(action1 != action2)

# Generated at 2022-06-13 10:28:06.158222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method `run` of class `ActionModule`."""
    # Since this method just wraps an action and delegates to it, we do not need to test it.
    pass


# Generated at 2022-06-13 10:28:16.909105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, None, None, None, None)
    # case 1
    task_args = {'name': 'httpd', 'state': 'restarted'}
    assert am._execute_module.called == False
    assert am.run(None, task_args) == {'rc':0, 'changed':True}
    assert am._execute_module.called == True
    # case 2
    task_args = {'use': 'auto', 'name': 'httpd', 'state': 'restarted'}
    assert am._execute_module.called == True
    assert am.run(None, task_args) == {'rc':0, 'changed':True}
    assert am._execute_module.called == True
    # case 3

# Generated at 2022-06-13 10:28:25.501410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Declare a modluar action to use in testing
    def mock_run(module_name=None, module_args=None, task_vars=dict(), wrap_async=None):
        return dict(
            module_name=module_name,
            module_args=module_args,
            task_vars=task_vars
        )

    class MockActionBase():
        def __init__(self, module_name, module_args, task_vars):
            self._task = dict(args=module_args, async_val=None)
            self._connection = dict()
            self._connection._shell = dict()
            self._display = dict()
            self._shared_loader_obj = dict()
            self._task = dict(args=module_args, async_val=None)
            self._task._parent

# Generated at 2022-06-13 10:28:36.309445
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # The following mock data is the output we want to try and reproduce
    mock_in_task_vars = {'ansible_service_mgr': 'systemd'}
    mock_in_tmp = None
    mock_in__execute_module = {'msg': "Successfully used systemctl", 'rc': 0, 'changed': True, 'invocation': {'module_args': {'name': 'htop', 'state': 'started', 'enable': 'no', 'daemon_reload': False}}, '_ansible_verbose_always': True}
    mock_in_module_name = 'ansible.legacy.service'
    mock_in_module_args = {'name': 'htop', 'state': 'started', 'enable': 'no', 'daemon_reload': False}
    mock_in_wrap_

# Generated at 2022-06-13 10:28:40.624838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(
        task = dict(action = dict(module = "service", args = dict(
            name = "foo",
            enabled = True,
            state = "started"
        ))),
        connection = dict(transport = "local"),
        play_context = dict(),
        loader = dict(),
        templar = dict(),
        shared_loader_obj = dict()
    )

    assert a is not None

# Generated at 2022-06-13 10:28:52.025930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('\nunit test')
    module = {
        'action': 'service',
        'args': {
            'name': 'sshd',
            'use': 'auto',
            'state': 'started'
        }
    }
    result = {}
    _templar = object()
    _task = object()
    _display = object()
    _connection = object()
    _shared_loader_obj = object()
    action = ActionModule(_templar, _task, _connection, _display, _shared_loader_obj)
    action.run(result, module, task_vars=None)
    print(result)

# Generated at 2022-06-13 10:29:09.809250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(task=dict(action=dict(module='service', use='auto')), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod

# Generated at 2022-06-13 10:29:11.819457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(ActionModule, 'tmp', 'task_vars')

# Generated at 2022-06-13 10:29:23.669312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    This method tests if the run method in ActionModule works correctly.
    '''
    task_vars = {'abc': 'abc', 'service_mgr': 'systemd'}
    args = {'use': 'auto'}
    module = ActionModule(task=None, connection=None, _shared_loader_obj=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._display = MockDisplay()
    module._execute_module = MockExecuteModule()
    module._connection = MockConnection()
    module._task = MockTask()
    module._task.args = args
    module._task.delegate_to = None
    module._task.async_val = 1

# Generated at 2022-06-13 10:29:31.489475
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:29:44.532600
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup a fake task.
    task = {"delegate_to": "localhost",
            "async": 60,
            "poll": 20,
            "async_val": 30,
            "args": {"use": "auto"},
            "action": "service"}
    task_vars = {"delegate_to": "localhost",
         "ansible_facts": {"service_mgr": "auto"}}
    tmp = "/tmp/ansible_service_payload"

    # Test the constructor.
    action_plugin = ActionModule(task, tmp, task_vars)
    # Test the override of the _supports_check_mode member.
    assert action_plugin._supports_check_mode == True
    # Test the override of the _supports_async member.

# Generated at 2022-06-13 10:29:45.099219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:53.709702
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.utils.path import unfrackpath
    from ansible.utils.display import Display
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader

    import os
    import sys
    import shutil
    import pytest


# Generated at 2022-06-13 10:30:06.177635
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Obviously the class obj needs to be initialized before
    # calling the method with arguments.
    action_module_obj = ActionModule(None, None, None, None, None, None, None, None)
    action_module_obj._task = task

    # Lets start testing the __init__ method of the ActionModule
    # class.
    # Define a None value for the self._task.args.get('use', 'auto').lower()
    action_module_obj._task.args = {'use': 'auto', 'name': 'MySQL'}
    assert action_module_obj.run()['failed'] == True

    # Define a 'auto' value for the self._task.args.get('use', 'auto').lower()

# Generated at 2022-06-13 10:30:13.274723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for action methods
    module = ActionModule()
    module._remove_tmp_path("this is a test string")
    module._display.display("this is a test string", True)
    module._display.debug("this is a test string")
    module._display.warning("this is a test string")
    module._display.vvvv("this is a test string")

# Generated at 2022-06-13 10:30:14.680265
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Test start')
    return

# Generated at 2022-06-13 10:30:55.204484
# Unit test for constructor of class ActionModule
def test_ActionModule():
    s = ActionModule()
    assert s._supports_check_mode == True
    assert s._supports_async == True


# Generated at 2022-06-13 10:31:00.860214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {}
    task_vars = {}
    tmp = None
    mock_templar = object

    # NOTE: ansible_facts.service_mgr must be defined to not enter the auto detection
    mock_templar.template = lambda x: 'ansible.legacy.service'

    plain_am = ActionModule(task=object, connection=object, play_context=object, loader=object, templar=mock_templar, shared_loader_obj=object)

    try:
        plain_am.run(tmp, task_vars)
        result.update(plain_am.run(tmp, task_vars))
    except Exception as err:
        print("ActionModule run error ({0})".format(err))

# Generated at 2022-06-13 10:31:07.162797
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES == False
    assert ActionModule.UNUSED_PARAMS == {
        'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
    }
    assert ActionModule.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])


# Generated at 2022-06-13 10:31:08.229901
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule()
    assert isinstance(actionmodule, ActionBase)

# Generated at 2022-06-13 10:31:09.843732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'module_name' in ActionModule.run.__code__.co_varnames

# Generated at 2022-06-13 10:31:11.268341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    # TODO: add unit tests
    pass

# Generated at 2022-06-13 10:31:12.449122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()


# Generated at 2022-06-13 10:31:18.560464
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = MagicMock()
    mock_task.async_val = None
    mock_task._parent = MagicMock()
    mock_task._parent._play = MagicMock()
    mock_task._parent._play._action_groups = MagicMock()
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:31:19.119546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   pass

# Generated at 2022-06-13 10:31:20.208546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:32:22.132770
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.inventory.host
    import ansible.executor.task_result
    import ansible.vars.manager
    import ansible.executor.module_common

    # create a task and a play to put the task in
    play = ansible.playbook.play.Play()
    task = ansible.playbook.task.Task()
    task._role = None
    play.add_task(task)

    # create a block to put the task in
    block = ansible.playbook.block.Block()
    block._role = None
    task._block = block

    # create a play to put the block in

# Generated at 2022-06-13 10:32:22.632578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:32:32.225787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule

    class Module1(ActionModule):
        TRANSFERS_FILES = False

        UNUSED_PARAMS = {
            'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
        }

        # HACK: list of unqualified service manager names that are/were built-in, we'll prefix these with `ansible.legacy` to
        # avoid collisions with collections search
        BUILTIN_SVC_MGR_MODULES = set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

        def run(self, tmp=None, task_vars=None):
            ''' handler for package operations '''

            self._supports_check_mode = True
            self._supports_async = True

# Generated at 2022-06-13 10:32:39.245257
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an object of class ActionModule
    task_vars = {
        'ansible_facts': {
            'service_mgr': 'auto'
        }
    }
    actionmodule = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Test the method
    assert actionmodule.run(task_vars=task_vars) == dict()

# Generated at 2022-06-13 10:32:39.825005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:32:44.859972
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {'name': 'test_service'}
    module_class = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert(module_class._task.args['name'] == 'test_service')
    assert(module_class._task.args['use'] == 'auto')
    return module_class


# Generated at 2022-06-13 10:32:55.970738
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pm = AnsibleActionModule()
    module_name = 'system'
    my_name = 'AnsibleModule'
    module_args = {'user': 'foo'}
    pm.load_name(module_name)

    # test using table
    pm_table = [
        {'run': pm.run},
        ]

    pm_result = {}
    for m in pm_table:
        pm_result = m['run'](tmp='', task_vars={'ansible_service_mgr': 'systemd'})

    assert pm_result['changed']

# Generated at 2022-06-13 10:33:04.349969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks needed for the test
    tmp_path = {'_ansible_no_log': False,
                '_ansible_tmpdir': '/tmp',
                '_ansible_verbosity': 0}

    task_vars = {}
    tmp = None

    # Create an instance of ActionModule and and call the run method
    action_to_test = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_to_test.run(tmp=tmp, task_vars=task_vars)

# Generated at 2022-06-13 10:33:05.046714
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 10:33:12.588928
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test started")
    host1 = Host("localhost")
    fact = {}
    fact["ansible_service_mgr"] = "win_service_desktop"
    host1.set_fact(fact)
    extra_vars = {}
    extra_vars["ansible_facts"] = {}
    extra_vars["ansible_facts"]["ansible_service_mgr"] = "win_service_desktop"
    task_vars = {}
    task_vars["hostvars"] = {}
    task_vars["hostvars"]["localhost"] = {}
    task_vars["hostvars"]["localhost"]["ansible_facts"] = {}

# Generated at 2022-06-13 10:35:42.101960
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule
    test_spec = {
        'delegate_to': 'localhost',
        'gather_facts': 'no',
        'name': 'foo',
        'state': 'started',
        'use': 'auto',
        'autoremove': True
    }
    test_data = {
        'ansible_facts': {
            'service_mgr': 'init',
            'ansible_service_mgr': 'init',
            'ansible_pkg_mgr': 'yum'
        }
    }
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

# Generated at 2022-06-13 10:35:49.501611
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:35:58.546906
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:36:00.827913
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    ACTION_MODULE = ActionModule()

    # act
    result = ACTION_MODULE.run()

    # assert
    assert result

# Generated at 2022-06-13 10:36:08.862024
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test class ActionModule
    '''
    # Init args
    tmp=None
    task_vars={'service_mgr': 'auto'}

    # Create class
    action = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Run method
    res = action.run(tmp, task_vars)

    assert res['failed'] == False
    assert res['kwargs'] == {'name': 'crond', 'state': 'reloaded'}
    assert res['module_args'] == {'name': 'crond', 'state': 'reloaded'}
    assert res['msg'] == 'crond reloaded/restarted'

# Generated at 2022-06-13 10:36:22.296200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_mod = ActionModule()
    action_mod.__dict__['_shared_loader_obj'] = get_loader()
    action_mod.__dict__['_task'] = Task()

    action_mod.__dict__['_task'].__dict__['args'] = {
        'use': 'auto',
        'name': 'foo',
        'state': 'started'
    }

    action_mod.__dict__['_task'].__dict__['module_defaults'] = {}
    action_mod.__dict__['_task'].__dict__['_parent'] = Play()
    action_mod.__dict__['_task'].__dict__['_parent'].__dict__['_action_groups'] = []

    action_mod.__dict__['_supports_check_mode'] = True
   

# Generated at 2022-06-13 10:36:32.608610
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import sys
    import ansible.plugins
    from ansible.plugins.loader import action_loader
    from ansible.module_utils import six
    from io import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.parsing.vault import VaultLib

    class ActionModule(ActionBase):

        TRANSFERS_FILES = False

        def run(self, tmp=None, task_vars=None):
            ''' handler for package operations '''

            self._supports_check_mode = True
            self._supports_async = True

            result = super(ActionModule, self).run(tmp, task_vars)
            del tmp  # tmp no longer has any effect


# Generated at 2022-06-13 10:36:34.224380
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module is not None



# Generated at 2022-06-13 10:36:38.908897
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, dict(a=1, b=2, c=3), loader=None, templar=None, shared_loader_obj=None)
    print("DONE!")

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:36:43.483211
# Unit test for constructor of class ActionModule
def test_ActionModule():
    subaction_dict = dict()
    task_dict_1 = dict(name='action_module_1', action=subaction_dict)
    task_1 = ActionModule(task_dict_1, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert task_1._shared_loader_obj is None
    assert task_1._task.name == 'action_module_1'
    assert task_1._task.action is subaction_dict
    assert task_1._task.args == subaction_dict