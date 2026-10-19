

# Generated at 2022-06-13 09:34:13.366974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule


# Generated at 2022-06-13 09:34:14.916594
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None, None, None, None)
    # ImportError: cannot import name _get_version
    #return action.run(None, None)
    pass

# Generated at 2022-06-13 09:34:19.820186
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mod = ActionModule()

    # Test fail_msg, success_msg and quiet options of fail module
    # when the assert expression is False
    args = {'fail_msg': 'Custom failure Message', 'success_msg': 'Custom success Message', 'quiet': 'False', 'that': 'vars.not_defined == "True"'}
    # task_vars are not passed since "that" expression is not dependent on task_vars
    result = mod.run(task_vars=None, tmp=None, **args)
    assert result == {'_ansible_verbose_always': True, 'assertion': 'vars.not_defined == "True"', 'changed': False, 'evaluated_to': False, 'failed': True, 'msg': 'Custom failure Message'}

    # Test fail_msg and success_msg options of fail module

# Generated at 2022-06-13 09:34:20.456395
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:34:30.252199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import unittest

    # Mock the Options class and AnsibleModule class so that we can run the code
    # without error. The AnsibleModule class will be created at runtime
    # and AnsibleModule.__init__() will be called. This is needed because
    # our code calls AnsibleModule.__init__().
    # For this test to work we set up these mocks.
    class MockAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.check_mode = False

    class MockAnsibleOptions(object):
        verbosity = 0
        connection = 'local'
        module_name = ''
        forks = 5
        become = False
        become_method = None
        become_user = None
       

# Generated at 2022-06-13 09:34:30.792723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:34:36.159760
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(fail_msg='fail this test', success_msg='success message'), args=dict()),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert module

# Generated at 2022-06-13 09:34:42.952237
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test successful assertion
    am = ActionModule(task=dict(action=dict(fail_msg=['foo', 'bar'])))
    am._templar.template = lambda x: x
    am.run()
    assert not am._result['failed']
    assert am._result['changed'] == False
    assert am._result['msg'] == 'All assertions passed'

    # Test unsuccessful assertion
    am = ActionModule(task=dict(action=dict(that=['foo == bar'], fail_msg=['foo', 'bar'])))
    am._templar.template = lambda x: x
    am.run()
    assert am._result['failed']
    assert am._result['changed'] == False
    assert am._result['msg'] == 'Assertion failed'
    assert am._result['evaluated_to'] == False
   

# Generated at 2022-06-13 09:34:47.641910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for ActionModule constructor'''
    temp_actionmodule = ActionModule()
    assert temp_actionmodule._VALID_ARGS == frozenset(['fail_msg', 'msg', 'quiet', 'success_msg', 'that'])
    assert temp_actionmodule.TRANSFERS_FILES == False


# Generated at 2022-06-13 09:34:51.424982
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.TRANSFERS_FILES is False
    assert am._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

# Generated at 2022-06-13 09:35:06.828790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import copy
    from ansible.plugins.action import ActionBase
    from ansible.playbook.task import Task

    am = ActionModule()
    assert am._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert am.TRANSFERS_FILES == False
    assert am._display.verbosity == 3

    am2 = copy.deepcopy(am)
    assert am == am2

# Generated at 2022-06-13 09:35:10.068530
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:35:12.378233
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(load_plugins={'Test': {}}, task={'args': {'that': '127.0.0.1'}})
    assert action_module is not None

# Generated at 2022-06-13 09:35:21.943624
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class test_ActionModule_ActionBase_test1(ActionBase):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(test_ActionModule_ActionBase_test1, self).run(tmp, task_vars)
            return result
    class test_ActionModule_ActionBase_test2(ActionBase):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(test_ActionModule_ActionBase_test2, self).run(tmp, task_vars)
            return result

# Generated at 2022-06-13 09:35:29.987528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.task import Task
    import ansible.constants as C

    # Create a temporary

# Generated at 2022-06-13 09:35:31.061545
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 09:35:42.036103
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import types
    import unittest
    script_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(script_dir + "/../../")
    test_utils_path = script_dir + "/../../test_utils"
    if test_utils_path not in sys.path:
        sys.path.append(test_utils_path)

    class AnsibleModuleStub():
        def __init__(self):
            self.params = {'that': ['var is defined', 'var == "abc"']}

    class TaskStub():
        def __init__(self):
            self.args = {'that': ['var is defined', 'var == "abc"']}


# Generated at 2022-06-13 09:35:43.993517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(args=dict()), play_context=dict())
    assert module is not None

# Generated at 2022-06-13 09:35:56.439016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader

    module = action_loader.get('assert', class_only=True)
    result = module.run(task_vars={'a': 1, 'b': 2})
    assert result['evaluated_to'] == False, result['evaluated_to']
    assert result['assertion'] == '{{a}} == {{b}}', result['assertion']
    assert result['msg'] == 'Assertion failed', result['msg']

    result = module.run(task_vars={'a': 1, 'b': 1, 'c': 2})
    assert result['evaluated_to'] == False, result['evaluated_to']
    assert result['assertion'] == '{{a}} != {{b}}', result['assertion']

# Generated at 2022-06-13 09:35:56.905326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:36:13.721737
# Unit test for constructor of class ActionModule
def test_ActionModule():
    tmp = None
    task_vars = dict(a=1, b=2)
    a = ActionModule(tmp, task_vars)


# Generated at 2022-06-13 09:36:21.228688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # name is a required argument
    module = ActionModule(None, action={}, task={}, connection={}, play_context={}, loader={},
            templar={}, shared_loader_obj={})
    assert module._play_context.port is None
    assert module._play_context.remote_addr is None
    assert module._play_context.remote_user is None
    module = ActionModule(None, action={}, task={}, connection={}, play_context={}, loader={},
            templar={}, shared_loader_obj={})
    assert module._play_context.port is None
    assert module._play_context.remote_addr is None
    assert module._play_context.remote_user is None

# Generated at 2022-06-13 09:36:25.356648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test for class ActionModule
    my_action = ActionModule()
    assert my_action is not None
    assert my_action._task is None
    assert my_action._play_context is None
    assert my_action._loaded_from is None
    assert my_action._templar is None
    assert my_action._connection is None
    assert my_action._loader is None



# Generated at 2022-06-13 09:36:34.558136
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initializing objects
    action_module = ActionModule()
    action_module.setup = 'setup'
    action_module._templar = {}
    action_module._loader = {}
    action_module._task = {}
    action_module._task.action = 'action'
    action_module._task.args = {}
    action_module._task.args.get = lambda: False

    # initializing test variables
    tmp = None
    task_vars = None

    # calling test method
    action_module.run(tmp, task_vars)

test_ActionModule_run()

# Generated at 2022-06-13 09:36:37.227851
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Begin unit test for constructor of class ActionModule")
    obj = ActionModule()
    print(obj)
    print("End unit test\n")



# Generated at 2022-06-13 09:36:38.677935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__doc__ == ' Fail with custom message '

# Generated at 2022-06-13 09:36:45.951150
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:36:55.717438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars
    import ansible.constants as C

    class MockTaskExecutor(object):

        def __init__(self):
            self._host_check_results = dict()

        def _host_check(self, host, check_method, conditionals, task_vars):
            return

# Generated at 2022-06-13 09:37:07.906722
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    obj = ActionModule( None, dict(), dict(), dict(), dict() )

    # action_module_fail.return_value = 1,1,1,1
    # obj.action = action_module_fail
    obj._loader = None
    obj._templar = None

    # _task.args._valid_args = 1,1,1
    # _task.args.get = 1,1,1,1
    # _task.args.get.return_value = 'fail_msg'
    # boolean.return_value = True
    # _task.args.get.return_value = 'success_msg'
    # _task.args.get.return_value = 'that'

    #assert isinstance(obj.run(), dict)
    #assert obj.run().get('failed') == True
    #assert isinstance(obj

# Generated at 2022-06-13 09:37:09.137413
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    assert isinstance(act, ActionModule)


# Generated at 2022-06-13 09:37:41.145572
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:37:43.641665
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 09:37:55.481579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.plugins import module_loader
    import json

    # Create a task and a play context, which is needed by the plugin
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    play_context

# Generated at 2022-06-13 09:38:08.583961
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import ansible.plugins
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Options(object):
        # Default options needed by base class
        verbosity = 0
        connection = 'local'
        module_path = None
        forks = 2
        become = False
        become_method = 'sudo'
        become_user = None
        become_ask_pass = False
        check = False
        listhosts = None
        listtasks = None
        listtags = None
        syntax = None
        diff = None

# Generated at 2022-06-13 09:38:23.604492
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    play = Play().load({'name': 'sometest',
                        'hosts': 'localhost',
                        'gather_facts': 'no',
                        'tasks': []}, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:38:34.994411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    module = ActionModule()
    task = dict()
    task['args'] = {}
    # Test that run() raises AnsibleError if args 'that' is not present in task
    with pytest.raises(AnsibleError) as exc:
        module.run(tmp=None, task_vars=None)
    assert 'conditional required in "that" string' in str(exc.value)
    task['args']['that'] = "setup.ansible_facts['os_family'] == 'RedHat'"
    module.run(tmp=None, task_vars={'setup':{'ansible_facts':{'os_family':'RedHat'}}})
    # Test that run() raises AnsibleError if args fail_msg or msg is not string or list of

# Generated at 2022-06-13 09:38:37.523355
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test case to validate the method run of class ActionModule """
    action_module_obj = ActionModule()
    action_module_obj.set_loader()
    action_module_obj.set_templar()

# Generated at 2022-06-13 09:38:47.675483
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os
    from ansible.errors import AnsibleError
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    variable_manager = VariableManager()
    hosts = []
    inventory = InventoryManager(loader=None, sources=hosts)
    variable_manager.set_inventory(inventory)
    myhost = Host(name="localhost")
    inventory.add_host(myhost)
    task1 = Task()

# Generated at 2022-06-13 09:38:48.945734
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:38:56.626087
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # import required modules
    import os
    # import unit test module
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from test import ModuleTestCase


    class TestActionModule(ModuleTestCase):
        '''
        Test case for checking fail_msg (or msg) parameter for fail module
        '''

        def setUp(self):
            super(TestActionModule, self).setUp()
            self.action = self.load_action_plugin('fail')

        def tearDown(self):
            super(TestActionModule, self).tearDown()

        #def test_fail_with_list_of_msg_and_success_msg(self):
        #    '''
        #

# Generated at 2022-06-13 09:39:54.813854
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play

    p = Play()
    a = ActionModule(p)
    assert a.play == p

# Generated at 2022-06-13 09:40:05.513591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    test_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_tmp = None
    test_task_vars = dict()
    test_conditional = "2 | int > 1"
    test_fail_msg = "Fail"
    test_success_msg = "Success"
    test_task_args = dict()
    test_task_args["that"] = test_conditional
    test_task_args["fail_msg"] = test_fail_msg
    test_task_args["success_msg"] = test_success_msg
    test_task = type('task', (object,), {"args": test_task_args})
    test_module._task = test_task

    # Test 1


# Generated at 2022-06-13 09:40:07.160874
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 09:40:07.947907
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 09:40:16.486360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()

    test_result = m._load_name_to_python('ansible.module_utils.basic')
    assert test_result is not None

    test_result = m._load_name_to_python('ansible.module_utils.basic.load_library')
    assert test_result is not None

    test_result = m._load_name_to_python('ansible.module_utils.basic.load_library')
    assert test_result is not None

    test_result = m._load_name_to_python('ansible.module_utils.basic.load_library')
    assert test_result is not None

# Unit test to check if method run fails with correct error 
# Argument that is not in valid args

# Generated at 2022-06-13 09:40:22.899961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader

    t = Task()
    t.action = "fail"
    t.args['that'] = "{{hostvars[inventory_hostname].ansible_ssh_host}} != {{ansible_ssh_host}}"

# Generated at 2022-06-13 09:40:37.772865
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Data:
        class MyException(Exception):
            pass

    data = Data()

    # Test fail_msg
    try:
        fail_msg = [1, 2]
        action_module = ActionModule(task=dict(args=dict(fail_msg=fail_msg)))
        raise data.MyException
    except AnsibleError:
        pass
    except data.MyException:
        assert False

    # Success
    try:
        fail_msg = ['something', 'another one']
        action_module = ActionModule(task=dict(args=dict(fail_msg=fail_msg)))
    except data.MyException:
        assert False

    # Test success_msg

# Generated at 2022-06-13 09:40:45.245392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {"hosts": "127.0.0.1", "fail_msg": "Assertion failed", "msg": "Assertion failed", "quiet": False, "success_msg": "All assertions passed", "that": "{{ ansible_lsb_release.description != 'Ubuntu 14.04.3 LTS' }}"}
    tmp = "$HOME/.ansible/tmp/ansible-tmp-1475921647.59-249898499087354/ansible-tmp-1475921647.59-249898499087354"

    task_vars = dict()
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:40:53.488940
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Intialize a fixture from class ActionModule
    action_module = ActionModule()

    # Set the tmp, task_vars and play_context attributes
    # of the fixture.
    action_module_tmp = None
    action_module_task_vars = None
    action_module_play_context = None

    # invoke the run method of action_module fixture
    # and store the result in result variable.
    result = action_module.run(action_module_tmp, action_module_task_vars)
    assert result == dict(
        failed=False,
        changed=True,
        # evaluted_to=True,
        assertion=None,
        msg='All assertions passed',
        )



# Generated at 2022-06-13 09:40:54.146098
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: add tests here
    pass

# Generated at 2022-06-13 09:43:56.603934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(action={
        '__ansible_arguments__': [],
        '__ansible_module__': 'fail',
        '__ansible_module_name__': 'fail'})
    print(action_module._task.keys())
    assert '__ansible_arguments__' in action_module._task.keys()
    assert '__ansible_module_name__' in action_module._task.keys()
    assert '__ansible_module__' in action_module._task.keys()
    assert '__ansible_version__' in action_module._task.keys()



# Generated at 2022-06-13 09:44:06.445631
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.task import Task
    from ansible.utils.plugin_docs import get_action_documentation
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from units.mock.loader import DictDataLoader
    dl = DictDataLoader({'fake_file': 'fake_content'})
    assert ActionModule._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert not ActionModule.TRANSFERS_FILES
    assert ActionModule.run.__doc__ == get_action_documentation(ActionModule.__name__)
    assert ActionModule.run.__name