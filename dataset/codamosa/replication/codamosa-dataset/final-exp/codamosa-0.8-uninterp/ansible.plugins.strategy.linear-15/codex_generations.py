

# Generated at 2022-06-13 15:18:03.333601
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None, variables=None, loader=None, host_list=None, options=None, passwords=None)
    assert strategy is not None


# Generated at 2022-06-13 15:18:04.277605
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule()


# Generated at 2022-06-13 15:18:04.890690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:18:12.300328
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    playbook_executor_loader = PlaybookExecutorLoader()
    results_tracker = ResultsTracker()
    variables_manager = VariableManager()
    loader = DataLoader()
    callback_loader = CallbackLoader(playbook_executor_loader, variables_manager)
    callbacks = callback_loader.get('default')
    strategy = StrategyModule(
        loader=loader, 
        tqm=None, 
        inventory=None, 
        variable_manager=variables_manager, 
        loader=loader, 
        options=None, 
        passwords=None, 
        stdout_callback='default', 
        run_additional_callbacks=False, 
        run_tree=True, 
        stdout_callback_enabled=False
    )
    for callback_plugin in callbacks:
        strategy.add_

# Generated at 2022-06-13 15:18:25.849307
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # noinspection PyUnresolvedReferences
    import allure_commons
    import yaml
    import os
    import sys
    import subprocess
    import time
    import shutil
    import socket
    import json
    import stat
    import tempfile
    import paramiko
    import ansible.utils.vars
    import ansible.utils.unsafe_proxy
    import ansible.utils.template
    # noinspection PyUnresolvedReferences
    import ansible.plugins.loader
    import ansible.compat
    import ansible.compat.six
    import ansible.constants
    import ansible.utils.path
    import ansible.utils.display
    import ansible.utils.plugin_docs
    import ansible.plugins.action
    import ansible.plugins.cache

# Generated at 2022-06-13 15:18:26.549160
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:18:37.670522
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    m = ModuleStub()
    m._config = MagicMock()
    m._tqm = MagicMock()
    m._tqm.send_callback = MagicMock()
    m._tqm.RUN_OK = 1
    m._tqm.RUN_FAILED_BREAK_PLAY = 2
    m._tqm.RUN_UNKNOWN_ERROR = 3
    m._tqm.terminated = False
    m._tqm._terminated = False
    m._tqm.get_failed_hosts = MagicMock(return_value=['host1', 'host2'])
    m._tqm.get_unreachable_hosts = MagicMock(return_value=['host1', 'host2'])
    m._tqm.get_host_

# Generated at 2022-06-13 15:18:42.124994
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  _loader = None
  _inventory = None
  _variable_manager = None
  _all_vars = None
  _tqm = None
  strategy = StrategyModule(_loader, _inventory, _variable_manager, _all_vars, _tqm)
  _iterator = ()
  _play_context = None
  assert strategy.run(_iterator, _play_context) == -1


# Generated at 2022-06-13 15:18:44.617830
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule(FakeTaskQueueManager())
    result = module.run(None, None)
    assert result is None

# Generated at 2022-06-13 15:18:46.439690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    # should not throw an error


# Generated at 2022-06-13 15:19:21.251771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    if (strategy):
        print("success")
    else:
        print("failure")


# Generated at 2022-06-13 15:19:21.767146
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:19:22.669493
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # add test code
    pass

# Generated at 2022-06-13 15:19:33.294567
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print('running test for method run of class StrategyModule')

    from ansible import context
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    context.CLIARGS = ImmutableDict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False, syntax=False)

# Generated at 2022-06-13 15:19:39.498344
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible
    import ansible.inventory
    import ansible.playbook
    import ansible.plugins
    import ansible.utils.callback_plugins
    import ansible.utils.plugins

    import tempfile

    # Create temp directory to store temporary callback files
    tmp_dir = tempfile.mkdtemp()

    callback_plugins_path = os.path.join(tmp_dir, 'callback_plugins')
    os.mkdir(callback_plugins_path)
    callback_plugin_file = os.path.join(callback_plugins_path, 'a_plugin.py')

# Generated at 2022-06-13 15:19:42.046880
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('/home/eghilev/ansible', 1, 'test', 'test', 'test')
    assert isinstance(strategy_module, StrategyModule)
    

# Generated at 2022-06-13 15:19:52.959835
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(
        task_queue_manager = 'task_queue_manager',
        variable_manager = 'variable_manager',
        loader = 'loader',
        options = 'options',
        passwords = 'passwords',
        stdout_callback = 'stdout_callback'
    ) 
    assert module.task_queue_manager == 'task_queue_manager'
    assert module.variable_manager == 'variable_manager'
    assert module.loader == 'loader'
    assert module.options == 'options'
    assert module.passwords == 'passwords'
    assert module.stdout_callback == 'stdout_callback'
    assert module.host_hash_patterns == dict()


# Generated at 2022-06-13 15:20:04.216484
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    # setup needed objects
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])

# Generated at 2022-06-13 15:20:04.851865
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:20:14.543240
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.plays.base import BasePlay
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.plugins.loader import action_loader
    task = load_list_of_tasks([{'name': 'test', 'action': 'test'}])[0]
    play = BasePlay()
    play.add_task(task)
    play_context = PlayContext()
    def load_callbacks():
        calbacks = []
        return calbacks
    def set_loader(loader):
        pass
    def send_callback(name, *args, **kwargs):
        pass
    
    play_context.loader = None
    play_context.set_loader = set_loader
    play_context.variable_manager = None
    play_context.send_callback = send_callback

# Generated at 2022-06-13 15:21:26.910630
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # 1. test with no args
    tqm = mock.Mock()
    tqm._failed_hosts = dict()
    variable_manager = mock.Mock()
    loader = mock.Mock()
    inventory = mock.Mock()
    ssh_retries = mock.Mock()
    module_path = mock.Mock()
    connection_info = mock.Mock()
    module_name = mock.Mock()
    fork_count = mock.Mock()
    ansible_strategy = StrategyModule(tqm, variable_manager, loader, inventory, ssh_retries, module_path,
                                      connection_info, module_name, fork_count)
    assert ansible_strategy._tqm == tqm
    assert ansible_strategy._variable_manager == variable_manager

# Generated at 2022-06-13 15:21:29.163744
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None, None, None, None)
    assert strategy is not None

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:21:31.752088
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule()
    strategy_module = module.get_strategy('linear')
    strategy_module.run('iterator', 'play_context')
    del strategy_module


# Generated at 2022-06-13 15:21:33.037693
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module is not None


# Generated at 2022-06-13 15:21:34.686240
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = AnsibleModule({}, {}, {}, {})
    module.run()


# Generated at 2022-06-13 15:21:36.318010
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Unit test of method run() in class StrategyModule

# Generated at 2022-06-13 15:21:37.440152
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:21:39.630585
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy = StrategyModule()
    assert True

# Test class StrategyModule

# Generated at 2022-06-13 15:21:41.171280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:21:44.975633
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module.get_name() == 'linear'
    print("\n OK Constructor of StrategyModule")
    print("\n")


# Generated at 2022-06-13 15:24:03.766667
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()


# Generated at 2022-06-13 15:24:09.175786
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Unit test for the constructor of class StrategyModule
    """
    tqm = TaskQueueManager()
    tqm._initialize_processes(1)
    tqm._final_q = multiprocessing.Queue()
    strategy = StrategyModule(tqm)
    assert id(strategy._tqm) == id(tqm)
    assert strategy._use_multiprocessing == False
    assert id(strategy._final_q) == id(tqm._final_q)
    assert strategy._name == 'linear'
    assert strategy.get_host_list() == []
    assert strategy.get_failed_hosts() == []
    assert strategy.get_unreachable_hosts() == []
    assert strategy.get_changed_hosts() == []
    assert strategy.get_dark

# Generated at 2022-06-13 15:24:19.299925
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    hosts = [
    {
    "ansible_version": {
    "full": "2.4.3.0",
    "major": 2,
    "minor": 4,
    "revision": 0,
    "string": "2.4.3.0"
    },
    "id": "f43b7d61-c772-491a-bcf8-076d14d6c0b6",
    "inventory_hostname": "F0IX11DL560",
    "name": "F0IX11DL560",
    "playbook_dir": "/home/admispconfig/ispconfig_setup/playbooks"
    }
    ]

# Generated at 2022-06-13 15:24:23.810603
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(
        tqm = TaskQueueManager(
            inventory = None,
            variable_manager = VariableManager(),
            loader = None,
            options = None,
            passwords = None
        ),
        variable_manager = VariableManager(),
        loader = DataLoader()
    )
    result = strategy_module.run(None, PlayContext())
    assert result == strategy_module._tqm.RUN_OK

# Test if name of class have changed

# Generated at 2022-06-13 15:24:25.240003
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
StrategyModule.test_StrategyModule = test_StrategyModule


# Generated at 2022-06-13 15:24:36.276508
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # setup
    iterator = Mock()

    play_context = Mock()
    action_loader = Mock()
    action_loader.get.return_value = Mock()
    host_list = [
        Mock(job_id=1, name='host1', port=22, variables={}),
        Mock(job_id=2, name='host2', port=22, variables={}),
        Mock(job_id=3, name='host3', port=22, variables={}),
    ]
    host_name_list = [ host.name for host in host_list ]
    iterator._play.get_variable_manager.return_value.get_vars.return_value = {
      'some_var': 'some_value',
      'some_other_var': 'some_other_value'
    }
    iterator.get

# Generated at 2022-06-13 15:24:41.629930
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pm = test_utils.get_test_play_context()
    templar = Templar(loader=DataLoader())
    sm = StrategyModule(tqm=None, hosts=hostlist.list_hosts(), tqm_variables=dict(), loader=DataLoader(), variable_manager=VariableManager(), shared_loader_obj=None, templar=templar)
    assert isinstance(sm, StrategyModule)
    assert isinstance(sm.hostlist, list)


# Generated at 2022-06-13 15:24:43.591055
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    strategy = StrategyModule(tqm)
    assert strategy

# Generated at 2022-06-13 15:24:45.800693
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert(type(strategy_module) == StrategyModule)


# Generated at 2022-06-13 15:24:53.456568
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    playbook = mock.MagicMock()
    inventory = mock.MagicMock()
    variable_manager = mock.MagicMock()
    loader = mock.MagicMock()
    options = mock.MagicMock()
    passwords = mock.MagicMock()
    stdout_callback = mock.MagicMock()
    iterator = mock.MagicMock()
    shared_loader_obj = mock.MagicMock()
    play_context = mock.MagicMock()
    strategy_module = StrategyModule()

    result = strategy_module.run(iterator, play_context)
    assert result == strategy_module._tqm.RUN_OK