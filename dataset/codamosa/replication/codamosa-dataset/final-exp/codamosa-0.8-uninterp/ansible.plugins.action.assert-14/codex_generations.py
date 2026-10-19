

# Generated at 2022-06-13 09:34:13.132122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.run()

# Generated at 2022-06-13 09:34:13.751280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module != None

# Generated at 2022-06-13 09:34:18.792910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit tests for ActionModule class"""
    from ansible.parsing.dataloader import DataLoader

    # Create a basic task from a reasonable set of arguments
    task_args = dict(
        fail_msg='Assertion failed!',
        msg='Assertion failed!',
        quiet=False,
        success_msg='Assertion succeeded!',
        that=dict(a=1, b=2, c=3)
    )

    action = ActionModule(task=dict(args=task_args),
                          connection=dict(host=None),
                          play_context=dict(),
                          loader=DataLoader(),
                          templar=None,
                          shared_loader_obj=None)
    assert action is not None, "ActionModule constructor failed"

# Generated at 2022-06-13 09:34:29.545585
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a mock task object
    task = dict()

    # Create a mock task_vars object
    task_vars = dict()

    task['args'] = dict()
    task['args']['that'] = ['hostvars["localhost"]["ansible_processor_count"] == 2','hostvars["localhost"]["ansible_processor_count"] == 2','hostvars["localhost"]["ansible_processor_count"] == 2']
    task['args']['fail_msg'] = "The custom error message is"
    task['args']['quiet'] = False

    # Create an instance of the ActionModule
    am = ActionModule()
    am._task = task
    am._loader = None
    am._templar = None

    # Call method "run" of the ActionModule
    result = am.run

# Generated at 2022-06-13 09:34:32.867469
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert module.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:34:35.437837
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('', {}, {}, {}, {}, {})
    assert action.transfers_files == False

# Generated at 2022-06-13 09:34:36.496896
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    # mod.run()

# Generated at 2022-06-13 09:34:41.221246
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create a object of type ActionModule
    test_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    expected_result = frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

    # Test for value of 'VALID_ARGS' in the instance of class ActionModule
    assert(expected_result == test_module._VALID_ARGS)

# Generated at 2022-06-13 09:34:51.463788
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Is this function called in test? If so, check if class exists and return True
    if 'ansible.plugins.action.assert' in sys.modules:
        if 'ActionModule' in sys.modules['ansible.plugins.action.assert'].__dict__:
            return True

    # Constructor test:
    # If the constructor does not require any arguments,
    # you can omit the argument list entirely:

# Generated at 2022-06-13 09:35:05.111709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    am = action_loader.get('assert', variable_manager=variable_manager, loader=loader, play_context=play_context)

    task_vars

# Generated at 2022-06-13 09:35:22.196943
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def TestActionModule():
        from ansible.utils.listify import listify_lookup_plugin_terms
        from ansible.playbook.play_context import PlayContext
        from ansible.plugins.loader import action_loader
        import ansible.constants as C
        # For testing purpose, mock ansible.context variable
        context._ansible_context = PlayContext()
        context._ansible_context.remote_addr = None
        context._ansible_context.connection = None
        context._ansible_context.accelerate = 0
        context._ansible_context.accelerate_port = 5099
        context._ansible_context.network_os = 'default'
        context._ansible_context.remote_user = 'root'
        context._ansible_context.remote_pass = None
        context._ansible_

# Generated at 2022-06-13 09:35:34.109673
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks
    class ActionModuleMock(ActionModule):
        def __init__(self):
            self.super_class_run_called = False
            self.super_class_run_return = None
            self.run_called = False
            self.run_return = None
            self.tmp = None
            self.task_vars = None

        def run(self, tmp=None, task_vars=None):
            self.run_called = True
            self.run_return = super(ActionModuleMock, self).run(tmp, task_vars)
            self.tmp = tmp
            self.task_vars = task_vars
            return self.run_return

        def super_class_run(self, tmp=None, task_vars=None):
            self.super_class_run

# Generated at 2022-06-13 09:35:36.712605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module != None
    

# Generated at 2022-06-13 09:35:41.606196
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print ('')
    # Create a mock for the class ActionModule
    mock_actionmodule = ActionModule() 
    # Assign a value to method run of the mocked ActionModule
    mock_actionmodule.run = lambda x,y: 'ActionModule.run executed'
    # Assert return value of method run equals 'ActionModule.run executed'
    assert mock_actionmodule.run(None,None) == 'ActionModule.run executed'

# Generated at 2022-06-13 09:35:53.101723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action import ActionBase
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class FakeTmp(object):
        pass

    class FakeTask(object):
        def __init__(self):
            self.args = {'fail_msg':'fail message', 'success_msg': 'success message'}

    class FakeModuleUtils(object):
        class PluginLoader(object):
            def __init__(self):
                pass

# Generated at 2022-06-13 09:35:53.777298
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:35:55.479205
# Unit test for constructor of class ActionModule
def test_ActionModule():
   module = ActionModule()
   assert module is not None


# Generated at 2022-06-13 09:36:01.245757
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Run method of ActionModule
    """

    # Load and init ActionModule
    action_mod = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None)
    action_mod._task.args = {'fail_msg': 'Assertion failed',
                             'success_msg': 'All assertions passed',
                             'quiet': 'true',
                             'that': ['"123"|int == 123',
                                      'false']}
    # Replace templar with simple mock
    action_mod._templar = Templar(variables={})

    # Run method
    result = action_mod.run(None, {'a_vars': {'a': 1, 'b': 2, 'c': 3}})

    # Check results
    assert result['failed']


# Generated at 2022-06-13 09:36:08.429168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = ActionModule(task={"name": "test_action_module"}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test._play_context == {}
    assert test._task == {"name": "test_action_module"}
    assert test._loader == {}
    assert test._templar == {}
    assert test._shared_loader_obj == {}
    assert test._connection == {}

# Generated at 2022-06-13 09:36:08.868476
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:36:18.236851
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:36:26.094444
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fact_module = AnsibleModule(
        argument_spec = dict(
            msg=dict(required=False, type='list'),
            fail_msg=dict(required=False, type='list'),
            that=dict(required=False, type='list'),
            success_msg=dict(required=False, type='list'),
            quiet=dict(required=False, type='bool', default=True)
        ),
        supports_check_mode=True
    )

    fact_module.params['fail_msg'] = "fail message"
    fact_module.params['msg'] = "fail message from msg"
    fact_module.params['quiet'] = True
    fact_module.params['that'] = "jira.jira_ticket_key == 'TEST-9656'"


# Generated at 2022-06-13 09:36:37.965112
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import sys
    import os
    import ansible.constants

    # Hacky, but I don't know another way to make the logging module
    # think it has been configured.
    ansible.constants.mk_logger('critical')

    # Get the file with the tests
    current_file = os.path.abspath(os.path.dirname(__file__))
    test_json = os.path.join(current_file, 'test_ActionModule.json')
    with open(test_json) as test_file:
        tests = json.load(test_file)

    # Load the tests
    for test in tests:
        mod_args = test.get('args', '')
        module = ActionModule(mod_args, task=None)

# Generated at 2022-06-13 09:36:45.952113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    display = Display()
    context._init_global_context(display)

    set_remote_user = ['set_remote_user']
    vault_password = ['vault_password']
    module_name = ['module_name']
    module_args = ['module_args']
    forks = 1
    become = True
    become_method = 'sudo'
    become_user = 'dag'
    check = False
    diff = False
    private_key_file = '/abc/def'
    remote_user = 'dag'
    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = 'variable_manager'
    loader = 'loader'
    data = 1
    task

# Generated at 2022-06-13 09:36:49.056617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=dict(args=dict(msg="Message for failure")), task_vars=dict(boolean_var=False, string_var="String_var", list_var=[dict(port=55), dict(port=80)], dict_var=dict(port=8080)))
    result = module.run(task_vars=dict(boolean_var=True))
    assert isinstance(result, dict)

# Generated at 2022-06-13 09:36:57.464722
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")

    import sys
    import os
    import ansible.utils
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class MockTask(object):
        def __init__(self, args=None):
            if args is None:
                args = dict()

            self.args = args

    class MockPlayContext(object):
        def __init__(self):
            self.connection = 'local'
            self.become = False
            self.become_user = None
            self.become_method = None
            self.remote_addr = None

    class MockOptions(object):
        def __init__(self):
            self.remote_user = None
            self.ask_pass = None
            self.private

# Generated at 2022-06-13 09:37:08.931319
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory(host_list=['testhost']))

    play_context = PlayContext()
    play_context.become = False

    host = list(variable_manager.get_inventory().get_hosts('testhost'))[0]
    task = Task()
    task_vars = variable_manager.get_vars(loader=loader, play=None, host=host)


# Generated at 2022-06-13 09:37:10.601732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_mod = ActionModule()
    print(act_mod._VALID_ARGS)

# Generated at 2022-06-13 09:37:19.743921
# Unit test for constructor of class ActionModule
def test_ActionModule():
    constructor_args = dict(connection='connection',
            become='become',
            become_method='become_method',
            become_user='become_user',
            check='check',
            diff='diff',
            play_context='play_context',
            remote_user='remote_user',
            runner_callbacks='callbacks',
            loader='loader',
            templar='templar',
            shared_loader_obj='loader_obj')
    am = ActionModule(**constructor_args)
    for k in constructor_args:
        assert getattr(am, k) == constructor_args[k]

# Generated at 2022-06-13 09:37:27.031921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile

    test_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(test_dir, 'roles'))
    os.mkdir(os.path.join(test_dir, 'roles', 'test_role'))
    os.mkdir(os.path.join(test_dir, 'roles', 'test_role', 'tasks'))

    task_filename = os.path.join(test_dir, 'roles', 'test_role', 'tasks', 'main.yml')
    with open(task_filename, 'w') as task_file:
        task_file.write("""
- fail:
    fail_msg: Test fail message
    assert: 'True is False'
""")


# Generated at 2022-06-13 09:37:54.973007
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, None)
    variable_manager.set_inventory(inventory)
    task = Task()
    task.set_loader(loader)
    task.set_task_vars(dict())
    task.play_context = dict()
    task.playbook = None
    task.action = 'Setup'
    action = ActionModule('setup', task, variable_manager=variable_manager, loader=loader, play_context=task.play_context)
    task.set_action(action)


# Generated at 2022-06-13 09:37:57.596657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule  # strictly speaking this does not test anything, but it does invoke constructor


# Generated at 2022-06-13 09:38:03.077624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Setup
    import ansible.constants
    import ansible.utils.template as template
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.role_dependency import RoleDependency
    from ansible.playbook.play_context import PlayContext

    # Create a task
    test_task = Task()
    test_task._role = RoleDependency(name='test_role')
    test_task._role._role_path = '/home/dir'
    test_task._task_deps = []
    test_task.loop = None

# Generated at 2022-06-13 09:38:13.100519
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test the constructor of the class
    # Test with no arguments
    no_arg_test = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert no_arg_test is not None
    # Test with all arguments
    test_action = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test_action is not None

# Generated at 2022-06-13 09:38:15.170471
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert hasattr(module, 'run')

# Generated at 2022-06-13 09:38:26.418838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, "actionmodule_test.yml")
    actionmodule_test = open(test_file).read()
    print(actionmodule_test)
    def test_cache():
        cache = dict(foo='bar')
        return cache
    set_module_args({'fail_msg': actionmodule_test})
    my_module = ActionModule()
    my_module._templar._available_variables = set()
    my_module._templar.set_available_variables(test_cache())

# Generated at 2022-06-13 09:38:36.011731
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #create actionmodule instance
    ams = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    #create task_vars dict
    task_vars = {}
 
    #executing run method with specific arguments
    ams_result = ams.run(task_vars=task_vars)
    assert ams_result['evaluated_to'] == False
    assert ams_result['assertion'] == 'that'
    assert ams_result['failed'] == True
    assert ams_result['msg'] ==  'Assertion failed'

# Generated at 2022-06-13 09:38:37.252998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''

    pass

# Generated at 2022-06-13 09:38:47.455701
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule()

    results = action.run(tmp=None, task_vars=dict(a=True, b=False))
    assert type(results) is dict
    assert results['failed'] is True
    assert results['evaluated_to'] is False
    assert results['assertion'] is "b == True"
    assert results['msg'] == "Assertion failed"
    assert 'result' not in results

    results = action.run(tmp=None, task_vars=dict(a=True, b=False))
    assert type(results) is dict
    assert results['failed'] is True
    assert results['evaluated_to'] is False
    assert results['assertion'] is "a != True"
    assert results['msg'] == "Assertion failed"
    assert 'result' not in results

    results = action

# Generated at 2022-06-13 09:38:50.043557
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert type(am) == ActionModule


# Generated at 2022-06-13 09:39:30.281680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:39:38.054178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = dict(a=2, b=3, c=[1,2,3])
    task_vars = dict(z=1, a=5, b=dict(b=5))

    action_mod = ActionModule(
            task=dict(
                args=dict(
                    fail_msg='Assertion failed: {{ a }} == 2',
                    quiet=True,
                    success_msg='All assertions passed',
                    that='{{ a }} == 2'
                )
            )
        )

    action_mod._templar = MockTemplar(a)
    test_result = action_mod.run(None, task_vars)

    assert 'changed' not in test_result
    assert test_result['msg'] == 'All assertions passed'
    assert test_result['evaluated_to']


    action_mod

# Generated at 2022-06-13 09:39:38.779994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:39:51.299835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    task = Task()
    task.args = dict()
    task.args['that'] = ['myvar is defined', 'myvar is defined and myvar != "foo"', 'myvar is defined and myvar == "foo"']

    am = ActionModule(task, dict())
    result = am.run(None, dict(myvar='foo'))
    assert(result['failed'] == False)
    assert(result['msg'] == 'All assertions passed')

    result = am.run(None, dict(myvar='bar'))
    assert(result['failed'] == True)
    assert(result['msg'] == 'Assertion failed')

    result = am.run(None, dict(foo='bar'))
    assert(result['failed'] == True)

# Generated at 2022-06-13 09:39:58.738980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    # Task.args has been deprecated in Ansible 2.5
    mock_task = Task()
    mock_task.args = {
        'msg': 'Failed',
        'fail_msg': 'Failed',
        'success_msg': 'Passed',
        'quiet': False,
        'that': [
            "var == 'value'",
            'var2 is defined'
        ]}
    mock_task.when = "var is defined"

    # Mock the AnsibleModule class.
    import sys

    if sys.version_info[:2] == (2, 6):
        import mock
        mock_ansible_module = mock.MagicMock()
    else:
        from unittest.mock import MagicMock
        mock_ansible_module = Magic

# Generated at 2022-06-13 09:40:09.372478
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = dict(
        # verbosity=3,
        # quiet=1
    )

    # test that the function fails with the appropriate message
    # if the required argument is missing
    action = action_loader.get('action', play_context, variable_manager, loader)
    action._task = dict(action=dict(args=dict(fail_msg=dict(verbose=True, debug='test'))))

# Generated at 2022-06-13 09:40:14.248879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(loader=None,
                          action_plugin=None,
                          task_vars=None,
                          connection=None,
                          play_context=None,
                          loader_cache=None,
                          shared_loader_obj=None,
                          templar=None,
                          task=None)

# Tests for method run

# Generated at 2022-06-13 09:40:16.065573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ActionModule is tested via the 'fail' action, as ActionBase is abstract
    pass

import unittest


# Generated at 2022-06-13 09:40:18.498261
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action

    action_args = dict(
        name='test',
        action='test'
    )
    action_module = ansible.plugins.action.ActionModule(action_args, None)

    assert action_module

# Generated at 2022-06-13 09:40:19.215822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {}
    pass

# Generated at 2022-06-13 09:41:37.605872
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=dict(action=dict(module_name='assert')))
    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))



# Generated at 2022-06-13 09:41:46.850459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Call with 'fail_msg'
    new_action_module = ActionModule(task=dict(args=dict(fail_msg="msg1")))
    assert new_action_module is not None

    # Call with 'msg'
    new_action_module = ActionModule(task=dict(args=dict(msg="msg2")))
    assert new_action_module is not None

    # Call with 'success_msg'
    new_action_module = ActionModule(task=dict(args=dict(success_msg="msg3")))
    assert new_action_module is not None

    # Call with 'quiet'
    new_action_module = ActionModule(task=dict(args=dict(quiet=True)))
    assert new_action_module is not None

    # Call with 'that'
    new_action_module = ActionModule

# Generated at 2022-06-13 09:41:47.796900
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()

    # TODO: Add unittest code
    pass

# Generated at 2022-06-13 09:41:55.567952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'a': 3}
    variable_manager._host_vars = None
    variable_manager._hostvars_files = None
    variable_manager._hostvars_cache = None
    module_name = 'assert'
    task = Task()
    task.set_loader(loader)
    task._variable_manager = variable_manager
    task.action = module_name
    task.args = {'quiet':False}
    #task.when = [{'a': 3}]
    task_vars = {}
    tmp = None

    am = ActionModule(task, tmp)
    am.run(task_vars=task_vars)


# Generated at 2022-06-13 09:41:58.696376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # parameters for constructor (ActionModule)
    tmp = None
    task_vars = None
    # instance of ActionModule
    ad = ActionModule(tmp, task_vars)
    # check if class attribute (private or not) are set
    ad.tmp = tmp
    ad.task_vars = task_vars

# Generated at 2022-06-13 09:42:04.630301
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Creating object for ActionModule
    am = ActionModule()

    # Dummy vars
    tmp = None
    task_vars = {'inventory_hostname': 'my_hostname'}

    # Dummy task
    task = dict()

    # Dummy task args
    task_args = dict()

    # Dummy ansible_facts cache
    task_cache = dict()

    # Pass on all the dummy data to ActionModule
    am.setup(tmp, task_vars, task_args, task_cache)

    # Check for a single that
    task_args = {'that': 'inventory_hostname == my_hostname', 'msg': 'Test message for successful assert'}
    am.setup(tmp, task_vars, task_args, task_cache)

# Generated at 2022-06-13 09:42:15.687991
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    unit test for ActionModule
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=None)

# Generated at 2022-06-13 09:42:22.489482
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:42:25.516919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    result = {}
    tmp = None
    task_vars = {}

    # Act
    obj = ActionModule()
    # result = obj.run(tmp, task_vars)

    # Assert
    # obj.assertEqual()

# Generated at 2022-06-13 09:42:36.868195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)