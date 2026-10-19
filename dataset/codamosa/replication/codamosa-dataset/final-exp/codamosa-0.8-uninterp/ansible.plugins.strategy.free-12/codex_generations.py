

# Generated at 2022-06-13 15:06:47.397966
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mock_iterator = MagicMock()
    mock_play_context = MagicMock()

    test_obj = StrategyModule(MagicMock())
    test_obj.run(mock_iterator, mock_play_context)

# Generated at 2022-06-13 15:06:49.114207
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  main()
if __name__ == '__main__':
  test_StrategyModule_run()

# Generated at 2022-06-13 15:06:54.307306
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    Test case for running the strategy for free module
    """
    test_tqm = DummyTaskQueueManager()
    test_play_context = DummyPlayContext()
    test_iterator = DummyIterator()
    test_obj = StrategyModule(test_tqm)
    # Test case : When strategy module is executed
    assert test_obj.run(test_iterator, test_play_context) == None

# Generated at 2022-06-13 15:06:55.537866
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager()
    assert True


# Generated at 2022-06-13 15:06:57.192151
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(1)
    strategy_module.run()

# Generated at 2022-06-13 15:07:01.286138
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import RoleInclude

    s = StrategyModule(tqm=None)
    t = Task()
    p = Play()
    p.handlers = [Handler()]
    h = [Host(name='host1'), Host(name='host2')]
    assert s.hosts_left(p, h)
    b = Block(play=p)
    r = RoleInclude(statically_loaded=True)
    r._role_name = "xyz"
    assert s.get_dependency_tree(play=p, role_include=r)
    assert not s.get

# Generated at 2022-06-13 15:07:11.901868
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import unittest
    from mock import MagicMock, patch
    from nose.tools import assert_raises
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task 
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult 
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 15:07:14.373407
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    assert isinstance(StrategyModule(tqm), object)



# Generated at 2022-06-13 15:07:26.512111
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    import ansible.module_utils.six as six
    import json
    import os
    import sys
    import unittest
    import yaml
    class MockSocket:
        def __init__(self):
            pass
    class MockConnection:
        def __init__(self, host):
            pass
        def get_become_method(self):
            return 'sudo'
    class MockVaultSecret:
        _secret = 'ansible'
        def __init__(self):
            pass
        def look(self, key):
            return MockVaultSecret._secret
        def decrypt(self, key):
            return MockVaultSecret._secret

# Generated at 2022-06-13 15:07:28.067265
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule(tqm)


# Generated at 2022-06-13 15:08:12.653527
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import sys
    from models.ansible_task import AnsibleTask

    class AnsibleTaskMock():
        def __init__(self, action=None, args=None):
            self.action = action
            self.args = args

    mock_task = AnsibleTaskMock(action='ping')
    mock_tasks = [mock_task]

    sys.argv = ['ansible-playbook', '-i', 'inventory', '-e', 'ansible_python_interpreter=/opt/rh/rh-python36/root/usr/bin/python']

# Generated at 2022-06-13 15:08:13.789818
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:21.822012
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.utils.path import makedirs_safe
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.compat.six import string_types
    from ansible.plugins.loader import module_loader
    import os
    import unittest
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible import errors
    import json
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    import ansible
    from ansible.context import CLIContext
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 15:08:28.036409
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    _tqm=None
    _tqm.send_callback=lambda x,y,z,**kwargs: None
    _tqm._terminated=False
    _tqm._unreachable_hosts=[]

    _tqm.RUN_OK=True

    _tqm.send_callback=lambda x,y,z,**kwargs: None
    _tqm.send_callback=lambda x,y: None
    iterator=None
    iterator.is_failed=lambda x: None
    iterator._play=None
    iterator._play.max_fail_percentage=None

    iterator._play=Mock()
    iterator._play.max_fail_percentage=None
    iterator._play.max_fail_percentage=20

# Generated at 2022-06-13 15:08:32.196468
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # this is a hack, but it works for now
    from ansible.plugins.strategy import Strategy

    strategy = StrategyModule(tqm=Strategy(display=None))


if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:42.663297
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.strategy.free import StrategyModule
    from ansible.vars.manager import VariableManager
    import ansible.utils.vars

    class MockTask:
        def __init__(self, action='', name='', run_once=''):
            self.action = action
            self.name = name
            self.run_once = run_once
            self._role = 'test_role'

    class MockHost:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class MockIterator:
        def __init__(self, play):
            self.host

# Generated at 2022-06-13 15:08:43.294048
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:54.275539
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Initialize the temporary directory
    temp_dir = tempfile.mkdtemp()
    # Create a temporary file
    temp_file = tempfile.mkstemp()
    # Write to the temporary file
    os.write(temp_file[0],b"Hello World")
    # Initialize a host variable
    host_vars = {}
    # Initialize a variable manager instance
    variable_manager = VariableManager(loader=None, variables=host_vars)
    # Initialize a dummy display class
    display = DummyDisplay()
    # Initialize a dummy variable manager class
    variable_manager = DummyVariableManager()
    # Initialize dummy inventory with some arbitrary hosts
    inventory = Inventory(loader=None, variable_manager=variable_manager, host_list=["dummy_hosts"])
    # Get the host object
    host

# Generated at 2022-06-13 15:08:54.950461
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	pass

# Generated at 2022-06-13 15:08:57.525219
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    args = dict(
        iterator=iterator,
        play_context=play_context
    )
    strategy_module = StrategyModule(tqm=tqm)
    result = strategy_module.run(**args)
    assert result is None

# Generated at 2022-06-13 15:10:17.864315
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


    #########################
    # Overridden Methods
    #########################



# Generated at 2022-06-13 15:10:27.578641
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create objects
    play_context = 'play_context'
    tqm = 'tqm'
    host_results = 'host_results'
    included_files = 'included_files'
    iterator = 1
    last_host = '1'
    result = 'result'
    result_is_false = 'result_is_false'
    task = 'task'
    task_vars = 'task_vars'
    templar = 'templar'
    workers_free = 'workers_free'
    work_to_do = 'work_to_do'
    hosts_left = 'hosts_left'
    starting_host = 'starting_host'
    host_name = 'host_name'
    action = 'action'
    task_name = 'task_name'

# Generated at 2022-06-13 15:10:35.503437
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        class Module:
            class Playbook:
                class Play:
                    max_fail_percentage = None
                    name = 'fake_play'
                def __init__(self):
                    self.play = StrategyModule.StrategyModule.TQM.Module.Playbook.Play()
            def __init__(self):
                self.playbook = StrategyModule.StrategyModule.TQM.Module.Playbook()
                self.inventory = None
                self.variable_manager = None
                self.loader = None
                self.options = None
                self.stdout_callback = None
                self.run_handlers = True
                self.run_tasks = True
                self._terminated = True

# Generated at 2022-06-13 15:10:45.790239
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  class TestStrategyModule():
    def __init__(self):
      self.RUN_OK = 1
      self.RUN_UNKNOWN_ERROR = 2
    def send_callback(self, a, b, c=False):
      pass
    def _queue_task(self, a, b, c, d):
      pass
    def get_hosts_left(self, a):
      return []

  class TestStrategyBase():
    pass
  
  from ansible.errors import AnsibleError
  from ansible.playbook.play_context import PlayContext
  from ansible.template import Templar, Jinja2TemplateModule
  from ansible.vars.manager import VariableManager
  from ansible.vars.hostvars import HostVars
  from ansible.parsing.yaml.objects import AnsibleBase

# Generated at 2022-06-13 15:10:47.155362
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    x = StrategyModule(tqm)



# Generated at 2022-06-13 15:10:50.201822
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  test = '''
  from ansible.plugins.strategy import StrategyModule
  from ansible.module_utils._text import to_text
  from ansible.errors import AnsibleError
  import time
  '''
  return test


# Generated at 2022-06-13 15:10:52.866602
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  my_StrategyModule = StrategyModule(tqm)
  try:
    my_StrategyModule.run(iterator, play_context)
  except:
    pass


# Generated at 2022-06-13 15:10:54.220950
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my = StrategyModule(tqm)
    my.run(iterator,play_context)

################################################################################



# Generated at 2022-06-13 15:10:56.242432
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Unit test for constructor of class StrategyModule """
    # pylint: disable=abstract-class-instantiated
    strategy = StrategyModule(None)
    assert strategy is not None

# Generated at 2022-06-13 15:11:00.247336
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """Test run method of class StrategyModule"""
    strategy = mock()
    when(strategy)._filter_notified_failed_hosts(mock(),mock()).thenReturn(mock())
    when(strategy)._filter_notified_hosts(mock()).thenReturn(mock())
    when(strategy).__init__(mock()).thenReturn(None)
    strategy.run(mock(),mock())

## Unit test for method get_hosts_left of class StrategyModule

# Generated at 2022-06-13 15:14:37.714923
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_StrategyModule = StrategyModule(None)
    ansible_module = AnsibleModuleHelper(
        argument_spec = dict(
            name = dict(type='str'),
            state = dict(type='str', default='present')
        ),
        supports_check_mode = True
    )

    ansible_module.params['name'] = 'Test'
    ansible_module.params['state'] = 'present'
    my_StrategyModule.run(ansible_module,None)

# Generated at 2022-06-13 15:14:42.234429
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:14:43.599864
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    It is a test case for method run of class StrategyModule 
    """

# Generated at 2022-06-13 15:14:44.801930
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == False


# Generated at 2022-06-13 15:14:53.871847
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    from ansible.plugins.action.normal import ActionModule
    from ansible.plugins import callback_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_vars
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.strategy.strategy_loader import add_strategy
    # Instantiation of VariableManager class
    test_loader

# Generated at 2022-06-13 15:14:54.419093
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:15:00.765349
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm=MagicMock())
    strategy_module.get_hosts_left(iterator=MagicMock())
    strategy_module.add_tqm_variables(task_vars=MagicMock(), play=MagicMock())
    strategy_module._set_hosts_cache(play=MagicMock())
    strategy_module._execute_meta(task=MagicMock(), play_context=MagicMock(), iterator=MagicMock(), target_host=MagicMock())
    strategy_module._take_step(task=MagicMock(), host_name='host_name')
    strategy_module._queue_task(host=MagicMock(), task=MagicMock(), task_vars=MagicMock(), play_context=MagicMock())

# Generated at 2022-06-13 15:15:02.870980
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == False



# Generated at 2022-06-13 15:15:08.253892
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = DummyTQM()
    hosts_list = []
    for x in range(1, 4):
        h = DummyHost(x)
        hosts_list.append(h)
    iterator = DummyIterator(hosts_list)
    play_context = DummyContext()
    s = StrategyModule(tqm)
    s.run(iterator, play_context)



# Generated at 2022-06-13 15:15:17.085754
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor import task_queue_manager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    import collections