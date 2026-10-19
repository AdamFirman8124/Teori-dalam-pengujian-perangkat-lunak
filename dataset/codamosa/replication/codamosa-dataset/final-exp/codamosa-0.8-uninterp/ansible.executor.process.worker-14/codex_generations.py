

# Generated at 2022-06-22 11:19:26.926437
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # create a queue
    q = multiprocessing_context.Queue()
    # create a worker
    worker = WorkerProcess(q, {}, None, None, None, None, None, None)
    # start the worker
    worker.start()
    worker.join()
    assert not worker._new_stdin.closed
    assert q.empty()

# Generated at 2022-06-22 11:19:39.463797
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    import os
    import shutil
    import stat
    import tempfile
    import time

    from os import path
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.callback import CallbackBase

    from ansible.playbook.task import Task

    class ResultCallback(CallbackBase):
        ''' A test callback which consumes data received from the execute_* call. '''

# Generated at 2022-06-22 11:19:40.061003
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    assert 1  # FIXME


# Generated at 2022-06-22 11:19:48.737057
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import tests.data.runner_data as runner_data

    (inventory, variable_manager, loader, options, shared_loader_obj) = runner_data.get_runner_data()
    host = inventory._get_host('example.com')
    task = host.get_task('setup')
    play_context = host.get_play_context(variable_manager)
    task_vars = variable_manager.get_vars(host=host, task=task)

    worker = WorkerProcess(None, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker._run()

# Generated at 2022-06-22 11:20:01.027974
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import queue
    import multiprocessing
    multiprocessing_context.set_forks_exec(False)
    state_q = multiprocessing.Queue()
    final_q = multiprocessing.Queue()
    task_vars = {}
    host = type('Host', (object,), dict(name='test_host'))()
    task = type('Task', (object,), dict(send_task_start=lambda: None, _uuid='test_uuid', dump_attrs=lambda: None))()
    play_context = type('PlayContext', (object,), dict(remote_addr='test_addr'))()
    loader = type('Loader', (object,), dict(_tempfiles=set(), cleanup_all_tmp_files=lambda self: self._tempfiles.clear()))()

# Generated at 2022-06-22 11:20:12.686102
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # create a queue for final results
    final_q = multiprocessing_context.Queue()
    # create a queue for results, populate it with a list of results
    results_q = multiprocessing_context.Queue()
    test_task_vars = dict()
    test_host = dict()
    test_task = dict()
    # create play context for the task
    play_context = dict()
    # create loader for the task
    loader = dict()
    # create variable manager for the task
    variable_manager = dict()
    # create shared_loader_obj
    shared_loader_obj = dict()

    # create workers object
    workers = WorkerProcess(final_q, test_task_vars, test_host, test_task, play_context, loader, variable_manager, shared_loader_obj)

    #

# Generated at 2022-06-22 11:20:23.464025
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Process
    from multiprocessing.managers import SyncManager
    class Queue(object):
        def __init__(self, *args, **kwargs):
            pass
        def send_task_result(self, *args, **kwargs):
            pass
    class Manager(object):
        def __init__(self, *args, **kwargs):
            pass
        SyncManager.register('Queue', type)
        Queue = SyncManager.Queue
    class Loader(object):
        def __init__(self, *args, **kwargs):
            pass
    class Host(object):
        def __init__(self, *args, **kwargs):
            pass
    class Task(object):
        def __init__(self, *args, **kwargs):
            pass

# Generated at 2022-06-22 11:20:30.774769
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.parsing.dataloader import DataLoader

    final_q = Queue()
    task_vars = dict()
    host = 'localhost'
    task = dict()
    play_context = dict()
    loader = DataLoader()
    variable_manager = dict()
    shared_loader_obj = dict()

    wp = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    wp.start()

# Generated at 2022-06-22 11:20:43.377442
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    import sys
    import os
    import tempfile
    import errno
    import getpass

    # Create a worker process object
    worker_process = WorkerProcess(multiprocessing.Queue(), 'task_vars', 'host', 'task', 'play_context', 'loader', 'variable_manager', 'shared_loader_obj')

    if worker_process._new_stdin is None:
        # Changing _new_stdin value for testing it
        worker_process._new_stdin = os.devnull
        # Creating a temp file with content
        fd, fname = tempfile.mkstemp(text=True)
        os.write(fd, b"Hello from %s\n" % getpass.getuser().encode('utf-8'))
        os.close(fd)
        #

# Generated at 2022-06-22 11:20:44.503738
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    return True

# Generated at 2022-06-22 11:21:01.158530
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # create a worker process with mocks
    worker_process = WorkerProcess(final_q=None, task_vars=None, host=None,
                                   task=None, play_context=None, loader=None,
                                   variable_manager=None, shared_loader_obj=None)
    worker_process.start()


# Generated at 2022-06-22 11:21:09.937590
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    class FinalQueue(object):
        def __init__(self):
            self.results = []

        def send_task_result(self, host, task_uuid, result, task_fields=None):
            self.results.append(result)

    task_vars = dict(
        foo='bar',
        user='root'
    )

    host = Host('localhost')
    loader = DataLoader()
    variable_manager = VariableManager()
    final_q

# Generated at 2022-06-22 11:21:11.473572
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    print('... not implemented ...')

# Generated at 2022-06-22 11:21:12.195080
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:21:13.039344
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:21:24.311283
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import random
    import time
    import multiprocessing

    class FakeQueue(object):
        def __init__(self):
            self.items = []

        def empty(self):
            return not self.items

        def get(self):
            return self.items.pop()

        def put(self, item):
            self.items.append(item)

    class FakePlayerContext(object):
        def __init__(self):
            self.extra_vars = {}
            self.command_timeout = 10
            self.timeout = 10
            self.become = False
            self.become_user = None
            self.become_method = None
            self.become_pass = None

    class FakeLoader(object):
        def __init__(self):
            self._tempfiles = set()


# Generated at 2022-06-22 11:21:30.013777
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    # Test run with monkey-patching

    # Test run with empty queues
    wp = WorkerProcess(multiprocessing.Queue(), {}, 'a', {}, {}, None, None, None)
    wp._save_stdin = lambda: None
    wp.start()
    assert wp._new_stdin is not None

# Generated at 2022-06-22 11:21:30.842503
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    # TODO

    pass

# Generated at 2022-06-22 11:21:40.558186
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    module_loader.add_directory('./lib/ansible/modules/extras')
    loader = DataLoader()
    variable_manager = VariableManager()
    final_q = multiprocessing_context.Queue(10)

    host = Host("127.0.0.1")
    task = Task()
    task.action = "ping"
    task._uuid = "123456789"

    worker = WorkerProcess(final_q, None, host, task, play_context, loader, variable_manager, None)
    worker._run()


# Generated at 2022-06-22 11:21:50.771856
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    '''
    Workers execution is based on multiprocessing.Pool and multiprocessing.Process,
    and it's not possible to test it directly.
    So I test only _cleanup() and some attributes initialization.
    '''
    class Dummy_FinalQueue(object):
        def __init__(self):
            self.is_called = False

        def send_task_result(self, *args, **kwargs):
            self.is_called = True

    final_q = Dummy_FinalQueue()
    wp = WorkerProcess(final_q=final_q, task_vars=[], host='', task='', play_context='', loader='', variable_manager='', shared_loader_obj=False)

# Generated at 2022-06-22 11:22:13.443855
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Given
    result_q = multiprocessing_context.Queue()

    # When
    wp = WorkerProcess(result_q, None, None, None, None, None, None, None)
    wp.start()
    result = result_q.get()

    # Then
    assert result

# Generated at 2022-06-22 11:22:21.707254
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.proc import MockProcess
    import ansible.constants as C

    class Test_task_executor(MockProcess):
        def __init__(self):
            pass

    # patch out the task executor with our mock
    old_executor = TaskExecutor
    TaskExecutor = Test_task_executor

    # set up needed objects
    host = Host(name="hostname")
    task

# Generated at 2022-06-22 11:22:31.328671
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    class MockFinalQ:
        def __init__(self):
            self.send_task_result = Mock()

    class MockHost:
        def __init__(self, name):
            self.name = name
            self.vars = dict()
            self.groups = []

    class MockTask:
        def __init__(self, uuid):
            self._uuid = uuid

        def dump_attrs(self):
            return dict()

    mock_task_vars = dict()

    mock_play_context = dict(remote_addr='/dev/null')

    class MockLoader:

        def __init__(self, uuid):
            self._tempfiles = set()
            self._add_tempfile(uuid)


# Generated at 2022-06-22 11:22:42.751889
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins import module_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.vars import combine_vars
    from ansible.utils.multiprocessing import create_manager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import multiprocessing
    #import os

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-22 11:22:51.223878
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.executor.process.worker import WorkerProcess

    # Create a WorkRequest
    final_q = Queue()
    task_vars = {}
    host = "localhost"
    task = object()
    play_context = object()
    loader = object()
    variable_manager = object()
    shared_loader_obj = object()

    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    worker_process.start()


if __name__ == '__main__':
    # Run test cases
    test_WorkerProcess_start()

# Generated at 2022-06-22 11:22:53.694678
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    Unit test for method start of class WorkerProcess
    '''
    pass

# Generated at 2022-06-22 11:23:05.540530
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Make connections.WorkerProcess instance for executing test
    # Note: since get_connection() method is used to create the
    # param `host`, that method of the connections.FileBasedLoader
    # class must be mocked and patched.
    final_q = multiprocessing_context.Queue()
    task_vars = None
    host = FileBasedLoader_mock().get_connection('localhost')
    task = dict()
    play_context = dict()
    loader = FileBasedLoader_mock()
    variable_manager = None
    shared_loader_obj = dict()
    worker = WorkerProcess(
            final_q, task_vars, host, task, play_context, loader,
            variable_manager, shared_loader_obj)
 
    # execute `_save_stdin()`

# Generated at 2022-06-22 11:23:06.200803
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:23:16.383716
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import queue
    import threading
    import multiprocessing
    import time
    import logging
    import tempfile
    import shutil
    import os
    import sys
    # We don't use the built-in unittest package in Ansible because we
    # don't want to introduce a dependency on Python 2.7 or above.
    # Instead we implement our own.
    class WorkerProcessUnitTest():
        class UnitTestError(Exception):
            pass

        class AssertionError(UnitTestError):
            pass

        @staticmethod
        def assertTrue(value, msg=''):
            if not value:
                raise WorkerProcessUnitTest.AssertionError(msg)

        @staticmethod
        def assertFalse(value, msg=''):
            if value:
                raise WorkerProcessUnitTest.AssertionError(msg)



# Generated at 2022-06-22 11:23:27.957590
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Setup
    task_q = multiprocessing_context.Queue()
    result_q = multiprocessing_context.Queue()
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=['localhost,']),
        variable_manager=VariableManager(loader=DataLoader()),
        loader=DataLoader(),
        passwords={},
        stdout_callback='default',
        run_tree=False,
    )

    # Execute

# Generated at 2022-06-22 11:24:11.065100
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = dict()
    host = dict()
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()

    # Initialize the instance of WorkerProcess class
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Start method of WorkerProcess class
    worker.start()

    # Clean the resources
    worker.join()



# Generated at 2022-06-22 11:24:22.044922
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import mock
    import multiprocessing
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class FinalQueue:
        def send_task_result(self, host, task_uuid, result, task_fields=None):
            pass

    final_q = FinalQueue()

    host = mock.Mock()
    host.name = '127.0.0.1'

    action = action_loader.get('setup', class_only=True)()
    module_args = dict(gather_subset='default')
    action._display.verbosity = 3

    play_context = PlayContext(verbosity=3, connection='local')
    variable_manager

# Generated at 2022-06-22 11:24:33.753462
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = dict()

    host = multiprocessing_context.SimpleNamespace()
    host.name = 'localhost'

    task = multiprocessing_context.SimpleNamespace()
    task._uuid = '2b1a9adc-9aea-4c56-a305-f639b20c61b6'
    task.action = 'shell'
    task.args = 'ls'

    play_context = multiprocessing_context.SimpleNamespace()
    play_context.new_stdin = 'new_stdin'

    loader = multiprocessing_context.SimpleNamespace()
    loader.cleanup_all_tmp_files = lambda: None
    loader._tempfiles = set()

    variable_manager = multiprocess

# Generated at 2022-06-22 11:24:34.571673
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:24:38.902558
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    from multiprocessing import Process

    q = multiprocessing.Queue()
    p = Process(target=worker_run_test, args=(q,))
    p.start()
    p.join()
    assert q.get() == 0


# Generated at 2022-06-22 11:24:48.633793
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars

    # worker_process_start() creates a new process which
    # creates a new, separate copy of its entire memory space.
    # As such, we cannot populate it with any objects and
    # expect them to still be there after multiprocessing.Process.start().

    # Create queues
    final_q = Queue(2)
    loader = DataLoader()

    # Create 'host

# Generated at 2022-06-22 11:24:55.169647
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    class FakeHost:
        def __init__(self):
            pass
    class FakeTask:
        def __init__(self):
            pass
    class FakePlayContext:
        def __init__(self):
            pass
    class FakeLoader:
        def __init__(self):
            pass
    class FakeVariableManager:
        def __init__(self):
            pass
    class FakeSharedLoaderObj:
        def __init__(self):
            pass
    host = FakeHost()
    task = FakeTask()
    play_context = FakePlayContext()
    loader = FakeLoader()
    variable_manager = FakeVariableManager()
    shared_loader_obj = FakeSharedLoaderObj()
    final_q = Queue()
    task_vars = Queue()
    worker

# Generated at 2022-06-22 11:25:01.325548
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # set up mocks
    mp_queue = MockQueue()
    super_start = MockMethod('super_start')

    # create a WorkerProcess instance
    WorkerProc = WorkerProcess(mp_queue, 'task_vars', 'host', 'task', 'play_context', 'loader', 'variable_manager', 'shared_loader_obj')

    # mock the worker process's start method
    WorkerProc.start = super_start.call
    # call the method under test
    WorkerProc.start()

    # assert things
    super_start.assert_called()
    assert WorkerProc._new_stdin is not None


# Generated at 2022-06-22 11:25:11.712018
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.plugins.strategy.linear import LinearStrategy
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_vars
    from collections import namedtuple

    playbook = []
    Options = namedtuple('Options', 'connection,module_path,forks,become,become_method,become_user,check,diff')

# Generated at 2022-06-22 11:25:22.489772
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    try:
        import __main__
    except ImportError:
        __main__ = None
    import unittest
    import sys

    class Test_WorkerProcess(unittest.TestCase):
        setUp = unittest.TestCase.setUp

        def test_WorkerProcess__save_stdin(self):
            import __main__
            from ansible.playbook.play import Play
            from ansible.inventory.manager import InventoryManager
            from ansible.module_utils.common.collections import ImmutableDict
            from ansible.vars.manager import VariableManager
            from ansible.parsing.dataloader import DataLoader
            from ansible.inventory.host import Host
            from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-22 11:26:49.985451
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    Unit test for method start of class WorkerProcess.
    '''
    import multiprocessing_context
    from collections import deque

    class DummyProcess(multiprocessing_context.Process):
        def __init__(self, *args, **kwargs):
            super(DummyProcess, self).__init__(*args, **kwargs)
            self.val = -1
        def run(self):
            self.val = 1

    def dummy_communicator(q, item):
        q.append(item) # append is thread safe

    q = deque()
    p = DummyProcess(target=dummy_communicator, args=(q, 'hello'))
    p.start()
    p.join()
    assert p.val == 1
    assert len(q) == 1
    assert q

# Generated at 2022-06-22 11:27:01.554542
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import unittest
    from ansible.vars import VariableManager
    from ansible.inventory import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils._text import to_text
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskResult

    class TestWorkerProcessShared(object):

        pass
    test_shared_loader_obj = TestWorkerProcessShared()


# Generated at 2022-06-22 11:27:08.932778
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Run the process
    q = multiprocessing_context.Queue()
    task_vars = dict()
    host = u'testhost'
    task = u'testtask'
    play_context = dict()
    loader = u'testloader'
    variable_manager = u'testvariable_manager'
    shared_loader_obj = u'testshared_loader_obj'
    workerProc = WorkerProcess(q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    workerProc.start()
    workerProc.join()

    assert True


# Generated at 2022-06-22 11:27:16.790350
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from multiprocessing import Queue
    import time

    final_q = Queue()
    task_vars = dict(gateway='192.168.0.1')
    host = 'test-host'
    task = dict(action=dict(module='ping', args={}), register='out')
    play_context = dict(remote_addr='127.0.0.1', password='password', become=False,
        become_method='sudo', become_user='root', become_pass='password')

    loader = 'test'
    variable_manager = 'test'
    shared_loader_obj = 'test'

    proc = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    proc.start()

    time.sleep(1)


# Generated at 2022-06-22 11:27:27.006224
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import ansible.executor.task_queue_manager as tqm
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    hosts = []
    host = '127.0.0.1'
    hosts.append(host)

    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    # There are a few things we need to do here:
    #
    # 1. Create a job queue manager, and give it our inventory.
    # 2. Create a result queue
    # 3. Create the shared dictionary containing the variables.
    # 4. Create the task queue manager, handing it the job and result queues, the inventory and the shared dictionary


# Generated at 2022-06-22 11:27:35.330671
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    global __multiprocessing_context__
    del __multiprocessing_context__
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.process.worker import multiprocessing_context
    from ansible.executor.task_executor import TaskExecutor
    import ansible.config.loader
    config = ansible.config.loader.load_configuration([], runtime_vars=dict())
    assert WorkerProcess(None, None, None, None, None, None, None, None).run() == None


# Generated at 2022-06-22 11:27:44.585353
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import connection_loader, module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager

    playbook = '''---
- hosts: localhost
  tasks:
    - debug: msg="hello world"
'''
    manager = multiprocessing.Manager()
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    result_queue = manager.Queue()
    task_queue = manager.Queue()
    task_vars = dict()


# Generated at 2022-06-22 11:27:55.395363
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # test with no stdin
    class _Test_WorkerProcess(WorkerProcess):
        def __init__(self, final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj):
            super(_Test_WorkerProcess, self).__init__(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
            self._new_stdin = None

    final_q = Queue()
    task_vars = {}
    host = ''
    task = ''
    play_context = ''
    loader = ''
    variable_manager = ''
    shared_loader_obj = ''


# Generated at 2022-06-22 11:28:02.119635
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import ansible.playbook.play as play
    import ansible.playbook.play_context as play_context
    import ansible.playbook.task_include as task_include
    import ansible.playbook.block as block
    import ansible.module_utils.connection as connection
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    import ansible.plugins.loader as plugin_loader

    from multiprocessing import Queue
    from itertools import chain
    import jinja2
    import pytest
    import shutil
    import tempfile
    import tempfile
    import traceback


# Generated at 2022-06-22 11:28:08.697562
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # set parameters
    task_vars = dict()
    host = dict()
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    final_q = dict()
    shared_loader_obj = dict()

    # create instance of WorkerProcess
    worker_process = WorkerProcess(
        final_q,
        task_vars,
        host,
        task,
        play_context,
        loader,
        variable_manager,
        shared_loader_obj
    )

    # run method under test
    worker_process.run()

    # check if worker_process is same as it's own
    assert worker_process is worker_process