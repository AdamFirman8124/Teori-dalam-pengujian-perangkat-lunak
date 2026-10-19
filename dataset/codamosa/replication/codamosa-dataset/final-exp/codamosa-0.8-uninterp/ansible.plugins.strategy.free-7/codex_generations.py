

# Generated at 2022-06-13 15:06:53.566638
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.plugins import strategy_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars

    from ansible.executor.playbook_executor import PlaybookExecutor
    import pdb

    # task_queue_manager
    options = Options()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='/tmp/hosts')
    extra_vars = load_extra_vars(loader=loader, options=options)
    variable_manager.extra_vars = extra_

# Generated at 2022-06-13 15:06:54.161831
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:06:55.100261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()


# Generated at 2022-06-13 15:07:07.075549
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.strategy import StrategyModule
    from ansible.template import Templar

    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
            {'name': 'dummy', 'action': {'module': 'debug', 'msg': 'dummy'}},
        ]
    }, variable_manager={}, loader=None)


# Generated at 2022-06-13 15:07:07.554276
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:18.134263
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import pytest
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars import Variable
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.included_file import IncludedFile
    from ansible.parsing.vault import VaultLib
    from ansible.plugins import strategy_loader, connection_loader

# Generated at 2022-06-13 15:07:18.648751
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:20.224765
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:07:22.922505
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    print("test_StrategyModule_run")

    # Placeholder for any unit tests for method run of class StrategyModule
    assert True

# Generated at 2022-06-13 15:07:23.447728
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass



# Generated at 2022-06-13 15:07:47.286309
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run of class StrategyModule
    '''
    pass

# Generated at 2022-06-13 15:07:59.233469
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import mock
    import random
    import unittest.mock
    
    class MockTemplar(object):
        def __init__(self, loader, variables):
            self._loader = loader
            self._variables = variables
        def template(self, value, fail_on_undefined=False):
            return "1"
    class MockHost(object):
        def __init__(self, name=None):
            self._name = name
        def get_name(self):
            return self._name
    class MockTask(object):
        def __init__(self, state=None, task=None):
            self._state = state
            self._task = task
        def get_next_task_for_host(self, host, peek=False):
            return (self._state, self._task)

# Generated at 2022-06-13 15:08:06.714896
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Unit tests for the StrategyModule constructor.
    """
    # Init
    import sys
    import unittest2 as unittest

    # Mocks

    # Test
    class test_StrategyModule(unittest.TestCase):

        def test_init(self):
            """ Test the constructor of the StrategyModule class.
            """
            result = StrategyModule(None)

            # Asserts
            self.assertIsInstance(result, StrategyBase)

    # Setup test
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

    # Execute test
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Process results
    print(result.errors)
    print(result.failures)

    # Return
    return result

# Generated at 2022-06-13 15:08:17.313919
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # mock object
    class mock_ansible_module(object):
        playbook_on_no_hosts_remaining = False
        def __init__(self, *args, **kwargs):
            self.fail_json = False
            pass

        def send_callback(self, *args, **kwargs):
            return True

        def v2_playbook_on_no_hosts_remaining(self):
            self.playbook_on_no_hosts_remaining = True
            return True

    class mock_queue_task(object):
        def __init__(self, *args, **kwargs):
            pass

    class mock_task(object):
        def __init__(self, *args, **kwargs):
            pass

        def get_name(self):
            return 'fake task name'

   

# Generated at 2022-06-13 15:08:18.463204
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    s = "This is a test function"
    assert s == s
    

# Generated at 2022-06-13 15:08:19.403332
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == False


# Generated at 2022-06-13 15:08:26.342365
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:30.251130
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    play_context = {}
    iterator = {}
    tqm = {}
    strat = StrategyModule(tqm)
    strat.run(iterator,play_context)

# Generated at 2022-06-13 15:08:41.428206
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:42.115359
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:09:42.525191
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Placeholder for automated testing
    '''

# Generated at 2022-06-13 15:09:43.264768
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:48.206968
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    display = Display()
    display.clear()
    #  display = Display(verbosity=0)
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars, load_options_vars
    options = parse_options()


    loader = DataLoader()
    passwords = {}
    inventory = InventoryManager(loader=loader, sources=options['inventory'])

    # inventory.add_group('eastbay')
    # inventory.add_host(

# Generated at 2022-06-13 15:09:58.461740
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import unittest.mock as mock
    import ansible.module_utils.facts.system.networking
    import ansible.inventory
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.plugins.strategy.none
    import ansible.template.template
    import ansible.vars.hostvars

    loader = mock.MagicMock()
    inventory = mock.MagicMock(ansible.inventory.Hosts)
    vars_manager = mock.MagicMock()
    shared_loader_obj = mock.MagicMock()
    variable_manager = mock.MagicMock(ansible.vars.hostvars.HostVars)
    variable_manager._fact_cache = {}
    variable_manager.get_vars = mock.MagicMock()
    variable_

# Generated at 2022-06-13 15:10:00.032155
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:10:02.572204
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Test constructor of class StrategyModule
    :return:
    '''
    strategy = StrategyModule()
    assert(strategy is not None)


# Generated at 2022-06-13 15:10:04.239774
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert(True)

# Generated at 2022-06-13 15:10:08.525667
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategy = StrategyModule(None)
   assert isinstance(strategy,  StrategyBase)
   assert strategy.get_hosts_left(None) == None
   assert strategy._filter_notified_failed_hosts(None, None) == None
   assert strategy._filter_notified_hosts(None) == None

if __name__ == '__main__':
   test_StrategyModule()

# Generated at 2022-06-13 15:10:11.634638
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


    # collect all the final results
    results = self._wait_on_pending_results(iterator)

    # run the base class run() method, which executes the cleanup function
    # and runs any outstanding handlers which have been triggered
    return super(StrategyModule, self).run(iterator, play_context, result)

# Generated at 2022-06-13 15:10:20.149035
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    synchronize_strategy = strategy_loader.get('free', None)

    assert synchronize_strategy

test_StrategyModule_run()

import math

import jinja2

from ansible.errors import AnsibleError, AnsibleActionFail
from ansible.plugins.loader import action_loader
from ansible.plugins.strategy import StrategyBase
from ansible.template import Templar
from ansible.utils.display import Display


display = Display()



# Generated at 2022-06-13 15:12:37.726366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(0) == None

# Generated at 2022-06-13 15:12:43.715679
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = ansible.executor.task_queue_manager.TaskQueueManager(inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords, run_tree=False, stdout_callback=results_callback)
    strategy_module = StrategyModule(tqm)
    result = strategy_module.run(iterator, play_context)
    assert result in [True, False]


# Generated at 2022-06-13 15:12:51.608716
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print("")
    print("##### In test_StrategyModule_run() #####")

    # creating objects
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                          'listhosts', 'listtasks', 'listtags', 'syntax', 'diff'])

# Generated at 2022-06-13 15:12:52.615493
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

    return None


# Generated at 2022-06-13 15:13:01.245522
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import ansible.plugins.strategy
    ansible.plugins.strategy.TEST_PASSTHROUGH = True
    import ansible.plugins.action
    ansible.plugins.action.TEST_PASSTHROUGH = True

    strategy = StrategyModule(None)
    __loader__ = strategy._loader # new with Ansible 2.10, don't know what it does
    strategy._loader = None
    iterator = None
    play_context = None
    strategy.run(iterator, play_context)

    strategy._loader = __loader__
    __loader__ = None

    return strategy

# Instantiate the StrategyModule class to test its run method
strategy = test_StrategyModule_run()
strategy = None # cleanup the memory
del test_StrategyModule_run
del strategy

# Generated at 2022-06-13 15:13:09.268261
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    import os
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import Include
    from ansible.playbook.handler import Handler
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    os.environ['ANSIBLE_CONFIG'] = 'ansible.cfg'

    connection = 'local'
    context = PlayContext()

# Generated at 2022-06-13 15:13:19.048114
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    itera = iterator.Iterator()
    play_c = play_context.PlayContext()

    # Initialize the instance
    tqm = task_queue_manager.TaskQueueManager(inventory=test_inventory, variable_manager=test_variable_manager, loader=test_loader, options=test_options, passwords=test_passwords, stdout_callback=test_stdout_callback)
    strategy = StrategyModule(tqm)

    # Execute the method
    strategy.run(itera, play_c)

    # Check the results obtained
    assert isinstance(strategy.run(itera, play_c), bool)


# Generated at 2022-06-13 15:13:27.279071
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # mock ansible.loader.action_loader
    mock_get_action_loader = MagicMock()
    mock_get_action_loader.ANY = Any()
    mock_get_action_loader.return_value = {
        'instance': None,
        'name': 'Copy',
        'path': '/opt/ansible/lib/ansible/modules/files/copy.py',
        '_filter_loader': None,
    }
    # mock ansible.display.Display
    mock_display = MagicMock()
    mock_display.display = Any()
    mock_display.display_newline = Any()
    mock_display.display_warning = Any()
    mock_display.display_ok = Any()
    mock_display.display_banner = Any()
    mock_display.display_error = Any()


# Generated at 2022-06-13 15:13:27.903537
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:13:38.051354
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Test the method with a failing task
    from mock import MagicMock
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    itr = MagicMock()
    itr.run_state = None
    itr.get_next_task_for_host = MagicMock(return_value=('ok', Task()))
    tqm = MagicMock()
    tqm.send_callback = MagicMock()
    tqm._unreachable_hosts = []
    tqm._terminated = False
    tqm.terminate_unreachable_hosts = MagicMock()
    p_ctx = PlayContext()
    p_ctx.cur_serial_num = 0
