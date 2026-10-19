

# Generated at 2022-06-22 11:19:34.773228
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import sys
    sys.path.append('..')
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.config.manager import ConfigManager
    from ansible.plugins.loader import connection_loader, module_loader
    from ansible.utils.display import Display
    display = Display()

    c = ConfigManager()
    m = ModuleLoader(c)
    c = connection_loader.get('local', m, c)
    c.HOST_NAME = 'localhost'
    i = InventoryManager(loader=None, sources=None, display=display)
    h = i.hosts.add('localhost')
    v = VariableManager(loader=None, inventory=i, version_info=c.ansible_version_info)


# Generated at 2022-06-22 11:19:36.301008
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass


# Generated at 2022-06-22 11:19:48.107510
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    import StringIO
    import io

    def on_start():
        # check stdin is closed
        assert sys.stdin.closed

        # ensure we've duped stdin
        assert sys.stdin is not initial_stdin

    def on_run(*args):
        # check stdin is closed
        assert sys.stdin.closed

        # ensure we can still use the dupe
        assert sys.stdin.read(1) == 'a'

        # ensure we preserve the original stdin (assuuing we haven't duped more than once)
        assert initial_stdin.read(1) == 'a'

    initial_stdin = sys.stdin

    # sys.stdin is a file descriptor and we cannot run the tests on a closed
    # one since that fails with a RuntimeError

# Generated at 2022-06-22 11:19:57.888610
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    import json

    class TestCallbackModule(CallbackBase):
        def __init__(self, queue):
            super(TestCallbackModule, self).__init__()
            self._queue = queue

        def v2_runner_on_ok(self, result, **kwargs):
            self._queue.put(result)


# Generated at 2022-06-22 11:20:06.559371
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # Setup
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = multiprocessing_context.Queue()
    task = multiprocessing_context.Queue()
    play_context = multiprocessing_context.Queue()
    loader = multiprocessing_context.Queue()
    variable_manager = multiprocessing_context.Queue()
    shared_loader_obj = multiprocessing_context.Queue()
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Execute
    worker_process.run()

# Generated at 2022-06-22 11:20:15.561574
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars
    from ansible.playbook.task import Task

    manager = multiprocessing_context.Manager()

    final_q = manager.Queue()
    task_vars = dict()
    host = HostVars()
    play_context = PlayContext()
    loader = None
    variable_manager = VariableManager()
    shared_loader_obj = None

    worker = WorkerProcess(final_q, task_vars, host, Task(), play_context, loader, variable_manager, shared_loader_obj)
    assert worker.start() is None

# Generated at 2022-06-22 11:20:24.708940
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    This is a helper function to unit test the private _save_stdin()
    method of class WorkerProcess.
    '''

    parent_stdin_fileno = sys.stdin
    parent_stdin_fileno.isatty = lambda : True

    parent_stdin_fileno.fileno = lambda : 0

    class MockFinalQueue(object):
        def __init__(self):
            self.task_results = []

        def send_task_result(self, host_name, task_uuid, result, task_fields=None):
            self.task_results.append((host_name, task_uuid, result, task_fields))

    final_q = MockFinalQueue()

    task = dict(action=dict(module='setup', args=''))

# Generated at 2022-06-22 11:20:33.454546
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    Unit test for the start method of WorkerProcess class
    '''
    final_q = None
    task_vars = None
    host = None
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    # Class is a subclase of Process
    assert issubclass(WorkerProcess, multiprocessing_context.Process)

    # Setup a WorkerProcess object
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # When start is called, it returns something.  This is what we're testing
    ret = worker.start()
    assert ret



# Generated at 2022-06-22 11:20:46.139955
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import test.utils as utils
    def _final_q_mock_send(*args, **kwargs):
        pass

    # name, _final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj
    task_executor = WorkerProcess(
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
        utils.Mock(),
    )

    task_executor._final_q.send_task_result = _final_q_mock_send
    task_executor._host.vars = utils.Mock()
    task_executor

# Generated at 2022-06-22 11:20:46.839794
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    print("test_WorkerProcess_start")
    assert True