

# Generated at 2022-06-13 11:18:53.709384
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:18:54.917103
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert hasattr(a, 'run')

# Generated at 2022-06-13 11:18:58.349559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    # test for bool instance
    assert isinstance(module._supports_check_mode, bool)
    # test for bool instance
    assert isinstance(module._supports_async, bool)
    # test for list instance
    assert isinstance(module.VALID_BACKENDS, frozenset)
    # test for bool instance
    assert isinstance(module.TRANSFERS_FILES, bool)

# Generated at 2022-06-13 11:19:00.050822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    success = (False, True)
    assert False


# Generated at 2022-06-13 11:19:00.698841
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 11:19:06.774775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ test the run() method of class ActionModule """
    module = ActionModule()

    # Test with use_backend set
    assert module.run({'use_backend': 'yum'}) == {'changed': True, 'msg': 'Run module: yum', 'rc': 0}

    # Test with use_backend and delegate_to set
    assert module.run({'use_backend': 'yum', 'delegate_to': 'delegate_to'}) == {'changed': True, 'msg': 'Run module: yum', 'rc': 0}

    # Test with invalid use_backend value
    assert module.run({'use_backend': 'invalid'}) == {'changed': True, 'msg': 'Could not find a yum module backend for ansible.legacy.invalid.', 'failed': True}

# Generated at 2022-06-13 11:19:08.297404
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert type(action) == ActionModule


# Generated at 2022-06-13 11:19:11.008114
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 11:19:19.722178
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager._extra_vars = {
        'ansible_facts': dict(pkg_mgr='yum4')
    }

    class Values(object):
        def __init__(self, value):
            self.value = value

        def __getitem__(self, args):
            return self.value

    task = Values({'args': dict(name='vim-enhanced')})
    task_vars = Values({'delegate_to': None, 'delegate_facts': True, 'async_val': 0})


# Generated at 2022-06-13 11:19:28.389552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict()
    task['action'] = dict()
    task['action']['args'] = {}
    task['action']['args']['use'] = 'auto'
    task['action']['args']['name'] = 'some_package'
    action = ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionBase)


if __name__ == '__main__':
    # running unit tests through python interpreter
    test_ActionModule()

# Generated at 2022-06-13 11:19:44.068555
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.playbook import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars


    class MockTaskInclude:
        def __init__(self):
            self.async_val = 0
            self.delegate_to = None


    class MockTask:
        def __init__(self):
            self.action = "yum"
            self.args = {}
            self.async_val = 0
            self.delegate_to = None
            self.delegate_facts = True

# Generated at 2022-06-13 11:19:46.388693
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert action_module is not None


# Generated at 2022-06-13 11:19:52.446971
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ACTION_MODULE = ActionModule()
    class MockModuleReturn:
        def __init__(self, _ansible_facts, _failed, _msg, _class):
            self.ansible_facts = _ansible_facts
            self.failed = _failed
            self.msg = _msg
            self.__class__ = _class

    class MockTemplate:
        def template(self, arg):
            return arg

    class MockActionBase:
        def __init__(self, _task):
            self._task = _task
            self._templar = MockTemplate()

    class MockTask:
        def __init__(self, args):
            self.args = args
            self.delegate_to = None
            self.delegate_facts = True
            self.async_val = None


# Generated at 2022-06-13 11:19:55.155256
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, task=None)

    # Assert if object creation is successful.
    assert action is not None



# Generated at 2022-06-13 11:20:03.526044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule({},{},None,None,None).__class__.__name__ == 'ActionModule'
    assert ActionModule(Task('myArgs','myLoader','myVarManager','myTemplar','myDelegateTo','myDelegateFacts','myAsync','myCheck','myBecome','myBecomeMethod','myBecomeUser','myDiff','myTags','mySkipTags','myAnyTags','myNotTags','myRunOnce','myVector','myVars'),{},None,None,None).__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:20:12.886449
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # unittest.skip unless either yum or dnf are installed
    module = ActionModule()
    # initialize non intrusive defaults
    module.task_vars = dict()
    module.task_vars['ansible_pkg_mgr'] = 'yum'
    module._connection = type('obj', (object,), {'_shell': type('obj', (object,), {'tmpdir': '/tmp'})})
    module._templar = type('obj', (object,), {'template': lambda self, x: x})()
    module._shared_loader_obj = type('obj', (object,), {'module_loader': type('obj', (object,), {'has_plugin': lambda self, x: x})})()
    # run with use_backend which will override the default behavior (dynamic backend selection)
   

# Generated at 2022-06-13 11:20:15.266426
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, dict(
        name='ansible-test',
        state='present',
    ))

    module.run(task_vars=dict(
        ansible_facts=dict(pkg_mgr='yum'),
    ))

# Generated at 2022-06-13 11:20:17.873917
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert isinstance(action_module._supports_check_mode, bool)
    assert isinstance(action_module._supports_async, bool)

# Generated at 2022-06-13 11:20:25.417832
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action as action
    action_module = action.ActionModule(
    {
        "name": "apt",
        "action": "ansible.legacy.yum",
        "args": {
            "name": "apache2",
            "update_cache": True
        }
    },
    {},
    connection={})

    assert action_module._task.args.get('name') == "apache2"
    assert action_module._task.args.get('update_cache') == True
    assert action_module._task.action == "ansible.legacy.yum"
    assert action_module._task.args.get('name') == "apache2"

# Generated at 2022-06-13 11:20:34.905712
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import ansible.constants as C

    old_stdout = None
    result = {}
    module_return = {}

    # initialize args
    args = dict(name=['httpd'])

    # initialize task_vars
    task_vars = dict(
        ansible_pkg_mgr='yum'
    )

    # initialize tmp
    tmp = None

    # initialize success and changed
    success = False
    changed = False

    # initialize ansible action module
    action_module = ActionModule(
        task=dict(args=args),
        connection=None,
        play_context=dict(check_mode=C.DEFAULT_CHECK_MODE),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    # call run
    result = action

# Generated at 2022-06-13 11:20:50.918436
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(foo="bar")
    module = ActionModule(task=dict(action=dict()), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    result = module.run(None, task_vars)
    assert result['msg'] == ("'use' is required: the yum module requires you to call either the yum or dnf backend directly.", "You should use a name like this 'yum_repository: use: yum'.")

# Generated at 2022-06-13 11:21:01.085082
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.loader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.modules.yum import yum
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFacts
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import module_loader

    loader = DataLoader()
    
    pb_vars = {
        'ansible_connection': 'local',
    }

    host_vars = {}
    task_vars = {}

    inventory = InventoryManager(loader=loader, sources=[])

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable

# Generated at 2022-06-13 11:21:10.485044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = {'action': {'__ansible_module__': 'yum'},
        'args': {'name': 'tree', 'install_repoquery': True}, 'delegate_to': 'localhost'}
    mock_task['args']['use'] = 'yum'
    mock_task['async_val'] = 42
    mock_task['delegate_facts'] = True
    mock_task['_ansible_verbosity'] = 3
    mock_task['_ansible_no_log'] = False
    mock_task['_ansible_debug'] = True
    am = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:21:15.486657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(name="test_module", async_val=False, async_timeout=10,
                  args=dict(use_backend="yum"))
    )
    assert action._task.async_val is False
    assert action._task.async_timeout == 10
    assert 'use_backend' in action._task.args
    assert action._task.args['use_backend'] is "yum"

# Generated at 2022-06-13 11:21:22.689254
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We cannot test ActionModule.run() with module_utils=ansible.module_utils.basic
    # as module_utils=ansible.module_utils.basic imports the ansible.module_utils.basic.AnsibleModule()
    # class which has a dependency on the os module of the system where 'ansible' is run.
    # This is why we use module_utils=tests.module_utils
    # See ansible.module_utils.basic.py
    from ansible.plugins.action.yum3 import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 11:21:26.003165
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(),
                          templar=dict(), shared_loader_obj=dict())
    assert module._supports_check_mode is True
    assert module._supports_async is True

# Generated at 2022-06-13 11:21:39.357817
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(
        task=MagicMock(), connection=MagicMock(), templar=MagicMock(),
        shared_loader_obj=MagicMock(), loader=MagicMock())

    task_vars = {}
    tmp = None

    # Test with yum4 module
    action_module._task.args = {"use": "yum4"}
    ret = action_module.run(tmp, task_vars)
    pprint(ret)
    assert ret['failed'] is False

    # Test with yum module
    action_module._task.args = {"use": "yum"}
    ret = action_module.run(tmp, task_vars)
    pprint(ret)
    assert ret['failed'] is False

    # Test with dnf module

# Generated at 2022-06-13 11:21:45.260810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # test_action_module = ActionModule(requested_action='action=ansible.legacy.yum', handler='action_handler',
    #                                   connection='connection', loader='_loader', templar='_templar',
    #                                   shared_loader_obj='_shared_loader_obj', ansible_version='ansible_version')
    pass

# Generated at 2022-06-13 11:21:50.823112
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task_vars = dict()
    mock_connection = object()
    mock_tmp = object()

    action_module = ActionModule(mock_task_vars, mock_connection, tmp=mock_tmp)
    
    # test backends
    mock_action_base_run = MockActionBaseRun(dict(), dict())

    action_module.run(dict(), dict(), mock_action_base_run=mock_action_base_run)

    mock_display_debug = MockDisplayDebug("Facts None")
    MockDisplay().register_type(mock_display_debug)

    mock_action_base_run = MockActionBaseRun({'ansible_facts': {'pkg_mgr': 'yum'}}, dict())


# Generated at 2022-06-13 11:21:59.398697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from yaml import load as yamlload
    from ansible.parsing.yaml.loader import AnsibleLoader

    test_actionModule = ActionModule(dict(
        name="yum",
        action=dict(
            module="yum",
            args=dict()
        )
    ))

    test_actionModule._supports_check_mode = True
    test_actionModule._supports_async = True

    with open("test/unit/plugins/action/yum/yum.yml") as f:
        facts = AnsibleLoader(f).get_single_data()

    with open("test/unit/plugins/action/yum/yum.py") as f:
        task_vars = AnsibleLoader(f).get_single_data()

    module = "yum"
    new_module

# Generated at 2022-06-13 11:22:24.137005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for action plugin module
    ActionModule.run
    """

    pass

# Generated at 2022-06-13 11:22:33.901586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Play
    from ansible.inventory import Inventory
    from ansible.module_utils._text import to_bytes

    class TestActionModule(ActionModule):
        def _execute_module(self, module_name, module_args, task_vars, wrap_async):
            return dict(module_name=module_name, module_args=module_args, task_vars=task_vars)


# Generated at 2022-06-13 11:22:36.683479
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test the constructor of class ActionModule
    """
    assert True



# Generated at 2022-06-13 11:22:41.720649
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module

# Generated at 2022-06-13 11:22:43.818284
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Creating the object of ActionModule class.
    yum_backend = ActionModule()

    # Asserting the object of ActionModule class.
    assert yum_backend

# Generated at 2022-06-13 11:22:53.716607
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing constructor of %s " % __name__)
    task = {"name": "test", "args": {"use": 'yum4'}, "async_val": 0}
    task_vars = {}
    tmp = None
    am = ActionModule(task, tmp, task_vars)
    r = am.run(tmp, task_vars)
    assert type(r).__name__ == "dict"

    print("Testing constructor of %s with no parameter" % __name__)
    r = am.run(tmp, task_vars)
    assert type(r).__name__ == "dict"

    print("Testing constructor of %s with bogus backend" % __name__)
    task_vars = {"ansible_facts": {}}
    task["args"]["use"] = 'bogus'


# Generated at 2022-06-13 11:23:01.950744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''

    action_module = ActionModule()
    test_tmp = "test_tmp"
    test_task_vars = dict()

    attribute_list = ['_tqm', '_supports_async', '_supports_check_mode', '_display', '_loader', '_templar']
    for attribute in attribute_list:
        if not hasattr(action_module, attribute):
            raise Exception('ActionModule __init__ missing attribute %s' % attribute)

    class MockExecutor(object):

        def __init__(self):
            self.connection_class = Connection()
            self.connection_class.tmpdir = u'test_tmp'
            self.stats = dict()

    action_module = ActionModule()
    action_

# Generated at 2022-06-13 11:23:12.743395
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def run_ActionModule_run(module, test_module, task_vars, backend):
        action = ActionModule(task=dict(args=dict(module=module, use_backend=backend)), loader=None, templar=None, shared_loader_obj=None)
        results = action.run(tmp=None, task_vars=task_vars)
        assert results is not None
        assert results["module_name"] == test_module
        assert results["module_args"] is not None
        assert results["module_args"] == module
        assert results["module_name"] == test_module
        assert results["module_args"] == module


# Generated at 2022-06-13 11:23:13.364704
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:23:14.023142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:24:01.290278
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert module.run()

# Generated at 2022-06-13 11:24:05.136616
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.yum as yum_module
    am = yum_module.ActionModule(0, dict(), 0, 0, 0)
    assert am is not None, "Create ActionModule object failed."

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 11:24:10.841931
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=None, shared_loader_obj=None, templar=None, ansible_version_info=[2, 7, 0])

    assert action_module
    assert action_module.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:24:14.677546
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:24:25.344804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test for action plugin backend handler for yum3 vs yum4(dnf) operations:
    Enables the yum module to use yum3 and/or yum4. Yum4 is a yum
    command-line compatibility layer on top of dnf.
    """

    # The following arguments are used to instantiate an object of ActionModule()
    tmp = 'tmp'
    task_vars = dict()
    task_vars['ansible_pkg_mgr'] = 'yum3'

    # test_yum3_with_delegate_to is used to test the following use-case:
    # If there is 'delegate_to' argument in self._task.args, then we should use delegated host's facts
    # i.e. we should use 'yum3' as backend.

    test_yum

# Generated at 2022-06-13 11:24:31.000460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    # Create a temporary directory to use
    import tempfile
    temp_dir = tempfile.mkdtemp()
    temp_files = tempfile.mkdtemp()

    # Mock the search for yum or dnf
    import mock
    from ansible.plugins.loader import find_plugin
    mock_module_finder = mock.create_autospec(find_plugin)
    mock_module_finder('yum', temp_files)
    mock_module_finder('yum', temp_files)
    mock_module_finder('dnf', temp_files)

    # Mock the execute_module so that we can return a mock result
    import json
    import os
    import shutil
    from ansible.plugins import action
    import ansible.plugins.loader as plugin_loader


# Generated at 2022-06-13 11:24:35.230640
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    task = mock.Mock()
    task.args = {'use_backend': 'dnf'}
    yum_action = ActionModule(task, mock.MagicMock())
    assert yum_action._task.args.get('use_backend') == 'dnf'

# Generated at 2022-06-13 11:24:44.725944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock class object to provide a Mocked method
    mock_class = type('MockClass', (object,), {})()

    # Create a mock object to provide a mocked _execute_module method
    mock_object = type('MockObject', (object,), {'_execute_module': mock_class._execute_module})()

    # Create a mock object to provide a mocked _execute_module method
    mock_object = type('MockObject', (object,), {'_execute_module': mock_class._execute_module})()

    # Create a mock task object with a mock _execute_module method
    mock_task = type('MockTask', (ActionBase,),
                     {'async_val': False,
                      '_execute_module': mock_object._execute_module})()

    # Create a ActionModule object with a

# Generated at 2022-06-13 11:24:45.496837
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module

# Generated at 2022-06-13 11:24:47.208590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action._supports_check_mode == True
    assert action._supports_async == True

# Generated at 2022-06-13 11:26:25.002495
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 11:26:25.430030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:26:33.041066
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.module_utils.basic
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.selinux
    import ansible.module_utils.facts.system.ssh

    def ansible_facts_get_yum_version():
        return 4

    def ansible_facts_get_yum_base_cache_dir():
        return '/var/cache/yum'

    def ansible_facts_get_yum_pkg_mgr_name():
        return 'yum-deprecated'

    def ansible_facts_get_distribution():
        return "CentOS"

    def ansible_facts_get_distribution_major_version():
        return 7


# Generated at 2022-06-13 11:26:41.725174
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Mock: ansible.plugins.action.ActionBase.run
    ActionBase.run = lambda self, tmp=None, task_vars=None: {'msg': 'test'}

    # AnsibleModule: ansible.plugins.action.ActionBase.__init__
    ansible_module = AnsibleModule(
        argument_spec=dict(
            use=dict(type='str',),
            use_backend=dict(type='str',),
        ),
    )

    # AnsibleModule.run_command: ansible.module_utils.basic.AnsibleModule.run_command
    ansible_module.run_command = lambda cmd, check_rc=False, close_fds=True, executable=None, data=None, binary_data=None: "run_command"

    # TempDir: ansible.module_

# Generated at 2022-06-13 11:26:42.321157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:26:43.299830
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:26:45.461570
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule """
    assert ActionModule is not None

# Generated at 2022-06-13 11:26:54.948122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Task:
        async_val = False

    class Task2:
        async_val = True

    def task_vars(params):
        class TaskVars:
            def __init__(self, params):
                self.params = params

            def get(self, key, default=None):
                return self.params.get(key, default)

        return TaskVars(params)

    class ActionBase:
        def task_vars(self):
            return task_vars({'ansible_pkg_mgr': 'yum'})

    class ActionBase2:
        def task_vars(self):
            return task_vars({'ansible_pkg_mgr': 'dnf'})


# Generated at 2022-06-13 11:26:57.791365
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:27:11.201514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ModuleData = {'name': 'ActionModule', 'args': {'use': None, 'use_backend': None}, 'delegate_to': None,
                  'delegate_facts': True, 'async_val': 10, '_ansible_parsed': True, '_ansible_version': None,
                  '_ansible_no_log': False, '_ansible_self_contained_fmts': []}
    FactData = {'pkg_mgr': None, 'ansible_pkg_mgr': 'auto'}
    loader = None
    templar = None
    shared_loader_obj = None
    display = None
    connection = None
    play_context = None
    play = None
    task_vars = [FactData]
    tmp = None