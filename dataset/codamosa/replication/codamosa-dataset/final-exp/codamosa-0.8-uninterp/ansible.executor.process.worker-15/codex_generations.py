

# Generated at 2022-06-22 11:19:34.165495
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    import multiprocessing

    # Mock required object/variable
    class obj(object):
        def __init__(self):
            self.name = 'name'

    class obj_manager(object):
        def __init__(self, obj):
            self.obj = obj

        def __enter__(self):
            return self.obj

        def __exit__(self, type, value, traceback):
            pass

    mock_task = obj()
    mock_task_vars = dict()
    mock_play_context = obj()
    mock_loader = obj()
    mock_variable_manager = obj()
    mock_shared_loader_obj = dict()

    mock_final_q = obj()

# Generated at 2022-06-22 11:19:40.282455
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play_context import PlayContext

    from ansible.plugins.loader import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    class PlayBookExecutor(object):
        def __init__(self):
            pass

    class Play(object):
        def __init__(self):
            self.hosts = 'all'

    class PlayContext(object):
        def __init__(self):
            pass

        def update_vars(self):
            pass


# Generated at 2022-06-22 11:19:48.300744
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # create some fake objects that are just enough to satisfy the init
    # method of WorkerProcess
    final_q = None
    task_vars = None
    host = None
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    # create the WorkerProcess object
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # call the run method of the WorkerProcess object
    worker_process.run()

# Generated at 2022-06-22 11:20:00.760625
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Ensure the class is defined As par Process
    assert issubclass(WorkerProcess, multiprocessing_context.Process)
    task_vars = {"ansible_connection": "winrm", "ansible_winrm_server_cert_validation": "ignore"}
    # host = lambda: None
    # host.name = "test_computer"
    # task = lambda: None
    # task._uuid = "UUID"
    # task.action = "test_action"
    # task.loop = "test_loop"
    # task.args = "test_args"
    # task.delegate_to = "test_delegate_to"
    # task.delegate_facts = "test_delegate_facts"
    # task.loop_control = "test_loop_control"
    # task.loop_

# Generated at 2022-06-22 11:20:08.788808
# Unit test for method run of class WorkerProcess

# Generated at 2022-06-22 11:20:09.692919
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:20:22.607437
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    import ansible.playbook
    import ansible.inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host_list = ['a', 'b']
    loader = DataLoader()
    inventory = ansible.inventory.Inventory(loader, host_list)
    variable_manager = VariableManager(loader, inventory)
    variable_manager._extra_vars = {"a": "a", "b": "b", "c": "c"}
    task = dict(action=dict(module='shell', args='echo hi'), tags=['c'])
    block = dict(rescue=[], always=[])
    task = ansible.playbook.Task.load(task, block, variable_manager=variable_manager)


# Generated at 2022-06-22 11:20:32.837795
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing

    class MockQueue(object):
        def __init__(self):
            self.items = []

        def send_task_result(self, host, task_uuid, result):
            self.items.append((host, task_uuid, result))

    class MockHost(object):
        def __init__(self, name):
            self.name = name

        def get_vars(self):
            return {}

        def get_groups(self):
            return []

        def setup(self):
            pass

    class MockTask(object):
        def __init__(self):
            self.name = "MockTask"

        def dump_attrs(self):
            return {'_uuid': 'fake_uuid'}


# Generated at 2022-06-22 11:20:45.796484
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    import time

    from unit.mock.loader import DictDataLoader
    from unit.mock.path import mock_unfrackpath_noop
    from unit.mock.vars import MockVarsModule
    from unit.mock.pm import MockTaskExecutor

    mock_unfrackpath_noop()
    display = Display()
    fake_loader = DictDataLoader({})
    fake_loader.set_basedir(os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'test_worker_process'))
    config = {'DEFAULT_ROLES_PATH': os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'roles')}

# Generated at 2022-06-22 11:20:56.922143
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    fake_loader = DictDataLoader({})
    fake_inventory = "localhost ansible_connection=local"
    fake_hosts = fake_inventory.split("\n")
    fake_variable_manager = VariableManager()
    fake_variable_manager.extra_vars = dict(foo="bar")
    fake_play_context = PlayContext()
    fake_play_context.remote_addr = '127.0.0.1'
    fake_play_context.connection = 'local'
