

# Generated at 2022-06-13 09:55:35.087166
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Note that this test has no mocking of the AnsiblePlugin.
    #
    # As of 2017-01-12, this test fails because the plugins can't be imported.  This is due to
    # the plugins not being in the Python path.
    # The workaround is to launch the python interpreter as follows so that the test can be run
    # from the ansible/test directory:
    #
    # $ python -m ansible.module_utils.basic

    import unittest2 as unittest
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook import Play, Playbook
    from ansible.playbook.play import Play as Play_
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

# Generated at 2022-06-13 09:55:44.003823
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    class TestModule(unittest.TestCase):
        def setUp(self):
            self.passed_task_vars = {}
            self.passed_tmp = None
            self.passed_connection = None
            self.passed_play_context = None
            self.action = None

        def run_action(self, task_vars, tmp, connection, play_context):
            self.passed_task_vars = task_vars
            self.passed_tmp = tmp
            self.passed_connection = connection
            self.passed_play_context = play_context
            self.action = ActionModule(task=self.task, connection=connection, play_context=play_context, loader=None, templar=None, shared_loader_obj=None)
            return self

# Generated at 2022-06-13 09:55:55.016502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action as action
    import ansible.plugins.action.setup as setup

    Action = action.ActionModule(
        task=dict(vars=dict(ansible_facts=dict(network_os='ios'))),
        connection=dict(_load_name='network_cli'),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    Action._connection._shell.tmpdir = '/tmp/ansible_dir'

# Generated at 2022-06-13 09:55:57.941387
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = __import__('ansible.plugins.action', fromlist=['ActionModule'])
    # TODO: INSERT UNIT TEST HERE
    # assert False, "Unimplemented"

# Generated at 2022-06-13 09:56:09.257553
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.vars as av
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    # test 'run' method
    action = ActionModule(ActionBase())
    result = action.run(tmp=None, task_vars=None)

    assert result['ansible_facts'] == {}
    assert type(result['ansible_facts']) is dict

    # test '_combine_task_result' method
    comb_res = action._combine_task_result({}, {'ansible_facts': {'test': 'test_dict'}, 'warnings': [], 'deprecations': []})
    assert comb_res['ansible_facts'] == {'test': 'test_dict'}

    # test '_execute_module' method
    task

# Generated at 2022-06-13 09:56:10.332340
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test an instance of class ActionModule
    ActionModule()

# Generated at 2022-06-13 09:56:12.828713
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test start
    x_module = ActionModule(None, None, None)
    x_module.run(tmp='tmp', task_vars={})

# Generated at 2022-06-13 09:56:13.459804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:56:14.638071
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:56:15.832645
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()


# Generated at 2022-06-13 09:56:27.635322
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: implement
    pass

# Generated at 2022-06-13 09:56:30.118136
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'
    test_action_module = ActionModule(None, None, None, None )
    assert test_action_module


# Generated at 2022-06-13 09:56:33.936046
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_loader_obj = None
    mock_play_context = None
    mock_task = None
    am = ActionModule(mock_loader_obj, mock_play_context, mock_task)
    assert am is not None

# Generated at 2022-06-13 09:56:35.556973
# Unit test for constructor of class ActionModule
def test_ActionModule():
    facts_module = ActionModule()
    assert facts_module is not None

# Generated at 2022-06-13 09:56:45.735247
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup
    action_module = ActionModule()
    assert action_module is not None

    # Test for method _get_module_args

    def _get_module_args(self, fact_module, task_vars):
        return action_module._get_module_args(fact_module, task_vars)
    action_module._get_module_args = _get_module_args
    assert action_module._get_module_args('os_setup', {}) is not None

    # Test for method _combine_task_result

    def _combine_task_result(self, result, task_result):
        return action_module._combine_task_result(result, task_result)
    action_module._combine_task_result = _combine_task_result
    action_module._combine_task_

# Generated at 2022-06-13 09:56:47.089146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionBase)

# Generated at 2022-06-13 09:56:50.138825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionBase = ActionBase()
    actionModule = ActionModule(actionBase._task, actionBase._connection, actionBase._play_context, actionBase._loader, actionBase._templar, actionBase._shared_loader_obj)
    assert actionModule is not None

# Generated at 2022-06-13 09:56:51.631984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule is not None)


# Generated at 2022-06-13 09:57:06.798175
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    facts_modules = [
        "ansible.builtin.raw",
        "ansible.legacy.setup"
    ]
    tmp = None
    task_vars = {
        'ansible_facts': {},
        'ansible_facts_parallel': False,
        'ansible_facts_module_list': facts_modules
    }
    # mock SharedPluginLoaderObj
    class SharedPluginLoaderObj():
        def find_plugin(self, module_name):
            return True
        def find_plugin_with_context(self, module_name, collection_list):
            return True
    m._shared_loader_obj = SharedPluginLoaderObj()
    class Task():
        def __init__(self):
            self.args = {}
            self.collections = []

# Generated at 2022-06-13 09:57:14.745552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.setup import ActionModule
    from ansible.module_utils import basic
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import load_provider
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import load_provider_variables
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.providers import NetworkBase
    import sys
    import argparse

    module_dir = os.path.dirname(os.path.abspath(argparse.__file__))
    sys.path.append(module_dir)

    results = {}
    results[0] = {'ansible_fact_module': {}}

# Generated at 2022-06-13 09:57:44.645133
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_path = 'ansible.plugins.action.setup.ActionModule'
    import ansible.plugins.action.setup as setup
    module = setup.ActionModule()
    module._supports_check_mode = True
    module._supports_async = True
    common_load_name = 'ansible.plugins.connection.local.Connection'
    module._templar = _templar()
    module._play_context = _play_context()
    module._shared_loader_obj = _shared_loader_obj()
    module._connection = _connection(common_load_name)
    module._task = _task()
    module._task_vars = _task_vars()
    module._display = _display()
    module.run()


# Group of Unit Test for class ActionModule

# Generated at 2022-06-13 09:57:58.977430
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_facts':{'ansible_distribution':'Ubuntu', 'os_family':'Debian'}}

    res = {}
    modules = ['ansible.legacy.setup', 'ansible.legacy.setup_grains']
    for fact_module in modules:
        # just one module, no need for fancy async
        mod_args = get_action_args_with_defaults(fact_module, {}, {}, task_vars)
        res = merge_hash(res, get_action_results(fact_module, mod_args, task_vars))

    # test result
    assert(res.get('ansible_facts', {}).get('ansible_distribution') == 'Ubuntu')

# Generated at 2022-06-13 09:57:59.461423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:00.834485
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(task=dict(args=dict())))



# Generated at 2022-06-13 09:58:07.638631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager, host_list_to_dict
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins import module_loader
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    # Create the loader object, which is used to load various files and templates.
    loader = DataLoader()

# Generated at 2022-06-13 09:58:11.256418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    # mod._supports_check_mode = True
    result = mod.run(tmp=None, task_vars={})
    assert 'ansible_facts' in result
    assert '_ansible_facts_gathered' in result['ansible_facts']

# Generated at 2022-06-13 09:58:21.914242
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection_type = None
    connection = None
    args_dict = {'foo': 'bar'}
    tmp_path = None
    task_uuid = None
    play_context = None
    loader = None
    templar = None
    shared_loader_obj = None

    # Default test
    action_module = ActionModule(
        connection_type,
        connection,
        args_dict,
        tmp_path,
        task_uuid,
        play_context,
        loader,
        templar,
        shared_loader_obj
    )

    # The following test is not working because we cannot mock the connection object.
    # When we try to use the 'mock.Mock()' we get the following error:
    # TypeError: object() takes no parameters
    # We have to find a way to mock

# Generated at 2022-06-13 09:58:29.128952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.plugins.connection as connection
    from ansible.plugins.callback import CallbackBase
    import ansible.playbook.play as playbook_play
    import ansible.playbook.task as playbook_task
    import ansible.playbook.role.include as include_role
    import ansible.playbook.block as playbook_block
    import ansible.playbook.playbook as playbook
    import ansible.inventory.host as host
    import ansible.inventory.group as group
    import ansible.inventory.manager as inventory_manager
    import ansible.utils.connection as connection_utils

# Generated at 2022-06-13 09:58:39.098845
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod_args = dict(
        gather_subset='all'
    )

    action_module = ActionModule(dict(task=dict()), dict(loader=dict(mock=True)))
    action_module._templar = dict(mock=True)
    action_module._task._task_vars = dict(mock=True)
    action_module._shared_loader_obj = dict(mock=True)
    action_module._shared_loader_obj.module_loader = dict(mock=True)
    action_module._shared_loader_obj.module_loader.find_plugin_with_context = dict(mock=True)

# Generated at 2022-06-13 09:58:44.535541
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize arguments
    task_obj = {}
    tmp = None
    task_vars = {}
    result = {}
    module_name = 'ansible.legacy.setup'

    # check for run method for class ActionModule
    action_module_obj = ActionModule(task_obj, tmp, task_vars)
    module_return_value = action_module_obj.run(tmp, task_vars)
    assert module_return_value == result

# Generated at 2022-06-13 09:59:28.524856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:59:29.436730
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:59:36.740702
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.plugin_loader import add_directory
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.plugins.action.setup import ActionModule
    from ansible.utils.sentinel import Sentinel
    dataloader = DataLoader()
    host

# Generated at 2022-06-13 09:59:51.772482
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the run method of the action module

    The run method is tested by instantiating it with various mocked out
    objects and running it with different parameter values to ensure
    that the correct behaviours are exhibited

    """
    import types
    import json

    class ActionModule_Mock(ActionModule):
        def _display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            return
        
        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return 'bin path'
        

# Generated at 2022-06-13 09:59:53.222698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for either single or multiple facts being gathered in parallel mode
    # Test for single fact being gathered in serial mode
    pass


# Generated at 2022-06-13 09:59:53.656551
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:00:00.186624
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins import action
    import ansible.plugins.action.setup

    assert action.ActionModule(None, 'test_failed') is not None
    assert action.ActionModule(None, 'test_success') is not None

    # Test the action_type
    assert action.ActionModule.action_type == 'normal'

    # Test the action_type
    assert action.ActionModule.action_type == 'normal'

    # Test the action_type
    assert action.ActionModule.action_type == 'normal'

    # Test the args
    assert action.ActionModule.args == {}

    # Test the boolean_args
    assert action.ActionModule.boolean_args == {}

    # Test the check_mode
    assert action.ActionModule.check_mode == True

    # Test the display
    assert action.ActionModule.display

# Generated at 2022-06-13 10:00:01.678634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Run the test
    import ansible.modules.setup
    module = ActionModule(None, None)
    assert not module.run()

# Generated at 2022-06-13 10:00:02.166539
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:00:09.732858
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import PluginLoader

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    loader.set_basedir('/home/local/ANSIBLE/xuxinwei/python/ansible/test/units/modules/network/basics/')

# Generated at 2022-06-13 10:01:53.913322
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing constructor of class ActionModule")
    t = ActionModule()
    assert(t._supports_check_mode == True)
    assert(t._connection == None)
    assert(t._task ==  None)
    assert(t._templar == None)
    assert(t._shared_loader_obj == None)
    assert(t._loader == None)
    assert(t._display == None)
    print("Passed")


# Generated at 2022-06-13 10:01:54.777677
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    print(am)

# Generated at 2022-06-13 10:02:00.000159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    set_module_defaults = ActionModule.set_module_defaults
    _get_module_args = ActionModule._get_module_args
    _combine_task_result = ActionModule._combine_task_result
    run = ActionModule.run
    assert set_module_defaults != None
    assert _get_module_args != None
    assert _combine_task_result != None
    assert run != None

# Generated at 2022-06-13 10:02:06.969348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = MockTask()
    mock_play_context = MockPlayContext()
    mock_new_style_action_base = MockNewStyleActionBase()

    action_module_object = ActionModule(mock_task, mock_play_context, mock_new_style_action_base)

    assert isinstance(action_module_object, ActionModule)


# Generated at 2022-06-13 10:02:18.530142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    task = {}
    args = {}
    args['parallel'] = None
    task['args'] = args

    ansible_facts = {}
    ansible_facts['_ansible_facts_gathered'] = True

    result = {'ansible_facts': ansible_facts}
    result['_ansible_verbose_override'] = True
    result['msg'] = 'The following modules were skipped: ansible.legacy.setup\n'
    result['skipped_modules'] = {'ansible.legacy.setup': {}}
    result['skipped'] = True

    # Make sure a variable exists
    ansible_facts['_ansible_fact_name'] = 'ansible_facts'

    action_module = ActionModule()
   

# Generated at 2022-06-13 10:02:23.551996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=task, connection=connection, play_context=play_context, loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)
    action_module.run(tmp=tmp, task_vars=task_vars)


# Generated at 2022-06-13 10:02:33.708445
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Test 1: default module combination:
    #
    modules = ['ansible.legacy.setup', 'ansible.legacy.group_by', 'ansible.legacy.hostvars', 'ansible.legacy.consul']
    fact_module_names = [
        'ansible.legacy.setup',
        'ansible.legacy.group_by',
        'ansible.legacy.hostvars',
        'ansible.legacy.consul',
    ]
    modules_mod_args = [
        {'filter': 'ansible_distribution'},
        {'key': 'ansible_distribution'},
        {},
        {'key': 'ansible_distribution'},
    ]

    #
    # Test 2: default module combination used in combination with custom module:


# Generated at 2022-06-13 10:02:34.468794
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:02:35.819574
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule(None, None, None, None, None) is not None)

# Generated at 2022-06-13 10:02:39.245880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for run method of class ActionModule """
    import ansible.plugins.action.setup
    ActionModule_obj = ansible.plugins.action.setup.ActionModule(
        task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None
    )

    ActionModule_obj.run()