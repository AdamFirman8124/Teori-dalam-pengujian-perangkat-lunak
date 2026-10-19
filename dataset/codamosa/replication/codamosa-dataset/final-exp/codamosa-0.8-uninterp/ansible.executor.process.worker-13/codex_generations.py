

# Generated at 2022-06-22 11:19:24.665389
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    print("No unit tests implemented for WorkerProcess.run()")

# Generated at 2022-06-22 11:19:34.112629
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    class final_q:
        def __init__(self):
            self.metadata = dict()
            self.metadata['is_multiprocessing'] = True
            self.metadata['workers'] = 2
            self.metadata['connection'] = u'local'
            self.metadata['playbook_basedir'] = u'playbook'
            self.metadata['words'] = u'words'
        def send_host_result(self, host, result):
            pass
        def send_task_result(self, host, uuid, result, task_fields):
            pass

    class task_vars:
        def __init__(self):
            self.hostvars = dict()
            self.hostvars['local'] = dict()
            self.hostvars['local']['domain'] = u'localhost'


# Generated at 2022-06-22 11:19:46.115505
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = multiprocessing_context.Manager().dict()
    host = multiprocessing_context.Manager().host
    task = multiprocessing_context.Manager().task
    play_context = multiprocessing_context.Manager().play_context
    loader = multiprocessing_context.Manager().loader
    variable_manager = multiprocessing_context.Manager().variable_manager
    shared_loader_obj = multiprocessing_context.Manager().shared_loader_obj
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    assert True


# Generated at 2022-06-22 11:19:52.209639
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    import multiprocessing.queues
    import tempfile
    manager = multiprocessing.Manager()
    q = multiprocessing.queues.SimpleQueue()
    tmpdir = tempfile.mkdtemp()
    p = multiprocessing.Process(target=WorkerProcess, args=(q,))
    p.start()
    p.join()
    p.close()

# Generated at 2022-06-22 11:20:01.593652
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    results_queue = multiprocessing_context.SimpleQueue()
    final_q = multiprocessing_context.SimpleQueue()
    task_vars = dict()
    host = 'localhost'
    task = dict()
    play_context = dict()
    loader = 'test'
    variable_manager = 'test'
    shared_loader_obj = True

    worker = WorkerProcess(results_queue, final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker.start()
    worker.__del__()

# Generated at 2022-06-22 11:20:02.763406
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:20:03.775276
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass


# Generated at 2022-06-22 11:20:14.402817
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.executor.process.result import TaskResult
    from ansible.executor.process.worker import WorkerProcess
    from ansible.module_utils.facts.system.osx import OsxHardware
    from ansible.module_utils.facts.system.osx import OsxSystem
    from ansible.module_utils.facts.system.posix import DefaultSysinfo
    from ansible.module_utils.facts.system.smartos import SmartOSHardware
    from ansible.module_utils.facts.system.smartos import SmartOSNetwork
    from ansible.module_utils.facts.system.smartos import SmartOSVirtual
    from ansible.module_utils.facts.system.smartos import SmartOSZoneinfo
    from ansible.module_utils.facts.system.virtual import Virtual

# Generated at 2022-06-22 11:20:21.493215
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = dict()
    host = 'localhost'
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()
    worker = WorkerProcess(final_q, task_vars, host, task,
                           play_context, loader, variable_manager,
                           shared_loader_obj)
    worker.start()

# Generated at 2022-06-22 11:20:32.198966
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # Set up objects needed in order to test the method run of class
    # WorkerProcess. These are needed since the method attempts to access
    # attributes of these objects.
    #
    # Basic approach to test is to check the TaskResult object return by the
    # method run.

    # Set up dummy inventory
    class Host(object):
        pass
    class TaskExecutor(object):
        def __init__(self, host, task, task_vars, play_context, new_stdin, loader, final_q):
            self.host = host
            self.task = task

            # Set up dummy result for executor
            self.result = dict(failed=True, changed=False)

        def run(self):
            # Check that input values are correct
            assert self.host.name == "localhost"
            assert self.task.action

# Generated at 2022-06-22 11:20:42.766719
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # TODO: not sure if this is how this code should be unit tested
    pass

# Generated at 2022-06-22 11:20:51.640454
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    from ansible.utils.shlex import shlex_split
    from ansible import constants as C
    from ansible.plugins.loader import action_loader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import module_loader
    #from ansible.plugins.loader import action_loader

    class CallbackModule:
        def __init__(self):
            self.results = []
            self.unreachable_hosts = []
            self.contacted = []
            self.failed_hosts = []


# Generated at 2022-06-22 11:20:53.837216
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from multiprocessing import Queue
    wp = WorkerProcess(Queue())
    wp.run()

# Generated at 2022-06-22 11:21:06.873030
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    host = MagicMock()
    task = MagicMock()
    final_q = MagicMock()
    task_vars = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    worker = WorkerProcess(
        final_q=final_q,
        task_vars=task_vars,
        host=host,
        task=task,
        play_context=play_context,
        loader=loader,
        variable_manager=variable_manager,
        shared_loader_obj=shared_loader_obj
    )
    assert not worker._new_stdin
    worker.start()
    assert worker._new_stdin

# Generated at 2022-06-22 11:21:14.207568
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    def fail(self):
        raise Exception("error")
    def empty(self):
        pass
    import multiprocessing
    q = multiprocessing.Queue()
    # check if exception behavior is correct
    worker = WorkerProcess(q, "task_vars", "host", "task_executor", "play_context", "loader", "variable_manager", "shared_loader_obj")
    worker._host.vars = empty
    worker.run()
    assert q.qsize() == 1
    result = q.get()
    assert "failed" in result
    # check if exception behavior is correct
    WorkerProcess._run = fail
    worker = WorkerProcess(q, "task_vars", "host", "task_executor", "play_context", "loader", "variable_manager", "shared_loader_obj")
   

# Generated at 2022-06-22 11:21:25.118090
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Process, Pipe
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    final_q, results_queue = Pipe()
    task_vars = dict()
    host = 'localhost'
    task = Task()
    play_context = PlayContext()
    loader = None
    variable_manager = VariableManager()
    shared_loader_obj = None
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    res = worker

# Generated at 2022-06-22 11:21:31.939626
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.JoinableQueue()
    task_vars = dict()
    host = dict()
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()

    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker.start()
    worker.join()

# Generated at 2022-06-22 11:21:36.386451
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    workerProcess = WorkerProcess(None, None, None, None, None, None, None, None)
    assert not workerProcess._new_stdin.closed
    workerProcess.start()
    assert workerProcess._new_stdin.closed


# Generated at 2022-06-22 11:21:47.879325
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import ansible.plugins.loader

    # loader.get_plugin is patched automatically by the test runner
    # Other imports are patched inside the test
    from ansible.executor.task_queue_manager import TaskQueueManager

    # this is needed to prevent a crash, as the test will try to load
    # some plugins (lookup) and they don't exist in python code, so
    # the plugin gets loaded from the actual package and fails to
    # find a loader class as it is not in python code
    ansible.plugins.loader.plugin_loader = None

    display = Display()

    loader, inventory, variable_manager = ansible.cli.CLI.setup_locations('all')
    variable_manager.extra_vars = {'hosts': "localhost"}

# Generated at 2022-06-22 11:21:58.585513
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.executor.task_result import TaskResult
    import multiprocessing
    import uuid

    class FakeFinalQueue:
        def __init__(self):
            self.tasks = []

        def send_task_result(self, hostname, task_uuid, result, task_fields):
            self.tasks.append((hostname, task_uuid, result, task_fields))

    class FakeHost:
        def __init__(self):
            self.name = 'foohost'
            self.vars = dict()
            self.groups = []

        def add_group(self, group):
            self.groups.append(group)

        def reset(self):
            self.vars = dict()
            self.groups = []
