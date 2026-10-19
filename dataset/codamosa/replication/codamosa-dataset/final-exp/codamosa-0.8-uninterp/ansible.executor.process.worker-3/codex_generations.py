

# Generated at 2022-06-22 11:19:33.179437
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    final_q = Queue()
    task = Task()
    task.action = 'setup'
    task_vars = {'inventory_hostname': 'localhost'}
    host = 'localhost'
    play_context = dict()
    loader = None
    variable_manager = VariableManager()

    worker = WorkerProcess(final_q=final_q, task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=None)
    worker.start()

# Generated at 2022-06-22 11:19:46.071198
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    from time import sleep
    import os
    import signal
    import tempfile
    import shutil
    import traceback
    import atexit

    # Function to shutdown the worker process gracefully
    def shutdown():
        for p in processes:
            print('Sending TERM signal to worker process with pid %s' % p.pid)
            # This is not needed on linux, but it is needed on macosx
            p.terminate()
        for p in processes:
            print('Waiting for worker process with pid %s to finish' % p.pid)
            p.join()

    print('Called test_WorkerProcess_run')

    # Check to see if this is needed on linux.
    atexit.register(shutdown)

    # Create a temporary directory to use
    tmpdir = tempfile.mk

# Generated at 2022-06-22 11:19:52.327349
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    import time

    q = multiprocessing.Queue()

    class MockHost:
        def __init__(self, name):
            self.name = name

    class MockVariableManager:
        def get_vars(self, play=None, host=None, task=None, include_hostvars=True):
            return {'foo':'bar'}

    class MockTask:
        def __init__(self, name):
            self.name = name

        def notify_handler(self, event):
            pass

        def copy(self):
            return self

        def get_name(self):
            return self.name

        def run(self, tmp=None, task_vars=None):
            return {'failed':False}


# Generated at 2022-06-22 11:20:02.433763
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import os
    import tempfile
    import pytest
    import multiprocessing
    from ansible.executor.task_queue_manager import TaskQueueManager

    fd, test_q_path = tempfile.mkstemp()
    test_q = multiprocessing.Manager().Queue()
    final_q = multiprocessing.Manager().Queue()

    p = WorkerProcess(final_q, {}, "host", TestTask(), Host(), plugin_loader, None, None)
    p.start()
    assert p.is_alive()
    p.join()
    os.close(fd)


# Generated at 2022-06-22 11:20:10.872891
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    queue = multiprocessing.Queue(20)
    task_vars = dict()
    host = None
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    worker_process = WorkerProcess(queue, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker_process.start()
    worker_process.terminate()

test_WorkerProcess_run()

# Generated at 2022-06-22 11:20:22.754041
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = {'foo': 'bar'}
    host = 'localhost' # type: ansible_host.AnsibleHost
    task = 'fake' # type: ansible_task.AnsibleTask
    play_context = 'fake' # type: ansible_play_context.AnsiblePlayContext
    loader = 'fake' # type: ansible_loader.AnsibleLoader
    variable_manager = 'fake' # type: ansible_variable_manager.AnsibleVariableManager
    shared_loader_obj = 'fake' # type: ansible_loader.DataLoader
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker.start()



# Generated at 2022-06-22 11:20:32.908068
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import os
    import Queue
    import multiprocessing

    # test env
    if not os.path.exists('/etc/ansible/hosts'):
        os.mknod('/etc/ansible/hosts')

    if not os.path.exists('/tmp/test.retry'):
        os.mknod('/tmp/test.retry')

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Specify play

# Generated at 2022-06-22 11:20:45.847559
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    # Simulate test environment so we don't depend on forking
    import multiprocessing

    # Code to be tested
    class DummyWorkerProcess(WorkerProcess):
        '''
        Dummy subclass to test the WorkerProcess class
        '''
        def __init__(self):
            self.stdin_filename = '/dev/null'
            self.start_called = False

        def start(self):
            self.start_called = True

        def run(self):
            pass

    # function to simulate multiprocessing.Process.start()
    def fake_start(process):
        # Simulate start_called in subprocess
        process.start_called = True
        process.new_stdin = open(process.stdin_filename)

    # Patch multiprocessing.Process.start()

# Generated at 2022-06-22 11:20:56.963221
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    #
    #   Args:
    #       final_q:
    #       task_vars:
    #       host:
    #       task:
    #       play_context:
    #       loader:
    #       variable_manager:
    #       shared_loader_obj:
    #

    # init args
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = 'localhost'
    task = 1
    play_context = 1
    loader = 1
    variable_manager = 1
    shared_loader_obj = 1

    # test

# Generated at 2022-06-22 11:21:08.358036
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    def final_q_send_task_result(host, task_uuid, result, task_fields):
        assert(host=='h')
        assert(task_uuid=='t')
        assert(result==dict(a=1))
        assert(task_fields==dict(b=2))
    final_q = type('', (), dict(send_task_result=final_q_send_task_result))()
    task_vars = dict(d=3)
    host = type('', (), dict(name='h'))()
    task = type('', (), dict(
        uuid='t',
        run=lambda *args, **kwargs:dict(a=1),
        dump_attrs=lambda:dict(b=2),
        shared_loader_obj=None,
    ))()
    play_context

# Generated at 2022-06-22 11:21:26.878247
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader, task_loader

    import __main__
    __main__.display = Display()
    fake_loader = DictDataLoader({'fake_task.yml': "name: test", 'fake_module.py': "name: test"})
    host = MagicMock()
    task = task_loader.load('fake_task.yml', play_context=PlayContext(), variable_manager=None, loader=fake_loader)
    play_context = PlayContext()
    loader = DictDataLoader(dict())
    variable_manager = None
    shared_loader_obj = None

    worker = WorkerProcess(MagicMock(), MagicMock(), host, task, play_context, loader, variable_manager, shared_loader_obj)

# Generated at 2022-06-22 11:21:27.349018
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:21:28.019920
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:21:36.691342
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # setup
    result_q = multiprocessing_context.Queue()
    task_vars = dict(my_var='foo')

    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    class MyTask(Task):
        def __init__(self):
            self._uuid = 'blah'
            self.name = 'foo'
            self.action = 'setup'
            self.args = dict()

   

# Generated at 2022-06-22 11:21:39.323882
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

if __name__ == '__main__':
    test_WorkerProcess_run()

# Generated at 2022-06-22 11:21:45.181247
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing

    passed = False
    job_q = multiprocessing.Queue()
    result_q = multiprocessing.Queue()
    worker = WorkerProcess(result_q, job_q)
    worker.start()
    worker.join()
    assert worker.is_alive() == False
    passed = True

    if not passed:
        raise Exception("WorkerProcess.start() unit test failed")

# Generated at 2022-06-22 11:21:56.241202
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    '''
    Test WorkerProcess.run()
    '''
    from ansible.executor import task_queue_manager
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import module_loader
    from ansible.vars import VariableManager

    pb = Playbook()
    play = Play().load(dict(name='noop', hosts='localhost', gather_facts='no'), variable_manager=VariableManager(), loader=pb._loader)
    final_q = task_queue_manager.TaskQueueManager()
    task = Task().load(dict(action=dict(module='copy', args='src=foo dest=bar')), play=play)

# Generated at 2022-06-22 11:22:05.417063
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import mock
    import multiprocessing
    from ansible.errors import AnsibleConnectionFailure
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.play_iterator import TaskIterator

    fake_host = mock.Mock(name="fake_host")
    fake_host.name = 'fake_name'
    fake_host.vars = {}
    fake_host.groups = []
    fake_host.get_vars.return_value = {
        'ansible_connection': 'local',
        'ansible_python_interpreter': sys.executable,
        'ansible_ssh_executable': sys.executable,
    }
    fake_task = mock.Mock(name="fake_task")
    fake_task._uuid = 'fake_task_uuid'


# Generated at 2022-06-22 11:22:15.521378
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    from ansible.utils.multiprocessing import connection_util

    connection_util.set_play_context_to_acquire_connection(None)

    localhost = 'localhost'
    fork_q = multiprocessing.Queue()
    final_q = multiprocessing.Queue()
    task_vars = {}
    play_context = connection_util.PlayContext()
    loader = None
    variable_manager = None

    # Base class for test class
    class Test(object):
        pass

    # Test class for TaskExecutor
    class TestTaskExecutor(Test):
        def run(self):
            return {}

    # Test class for Task

# Generated at 2022-06-22 11:22:24.365212
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import jinja2.exceptions
    from ansible.errors import AnsibleConnectionFailure, AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from multiprocessing import Queue
    from queue import Empty

    from units.mock.proc_modules import MockModule

    mock_loader = DictDataLoader({
        "some_template.j2": "{{ var }}",
        "some_python.py": "raise Exception(foo)",
    })


# Generated at 2022-06-22 11:22:48.271017
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.executor.task_queue_manager import TaskQueueManager
    final_q = TaskQueueManager()
    task_vars = {}
    host = "host"
    task = "task"
    play_context = "play_context"
    loader = ""
    variable_manager = ""
    shared_loader_obj = ""
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker_process.start()

# Generated at 2022-06-22 11:22:49.509469
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:23:02.137293
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    child_process_result = [None]

    class m_Process(multiprocessing_context.Process):

        def __init__(self):
            super(m_Process, self).__init__()
            self.start_called = False
            self.start_called_with = None

        # function for replacing multiprocessing.Process.start
        def start(self, *args, **kwargs):
            try:
                self.start_called = True
                self.start_called_with = (args, kwargs)
                child_process_result[0] = self._run()
            except BaseException as e:
                self._hard_exit(e)

    # replacment for multiprocessing.Process
    class m_multiprocessing_context:

        Process = m_Process

    sys.modules

# Generated at 2022-06-22 11:23:07.775756
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # for unit test, some import needs to be done
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # create objects needed by class WorkerProcess
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager.set_inventory(inventory)
    play_context = Play().set_loader(loader)

    # create a worker object
    worker = WorkerProcess(None, None, inventory.get_host('localhost'), None, play_context, loader, variable_manager, None)

    # call run method of class WorkerProcess
    worker.run()

# Generated at 2022-06-22 11:23:18.198358
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.utils.multiprocessing import _multiprocessing
    _multiprocessing.MultiprocessingFactory.initialize()
    from ansible.plugins.loader import callback_loader, module_loader
    # import pdb
    # pdb.set_trace()
    variables = {
        'name': 'worker_process',
        'fail': False,
    }
    playbook_vars = {
        'worker_process': {
            'name': 'worker_process',
            'fail': False,
        }
    }
    variable_manager = AnsibleVariableManager(loader=DataLoader())
    variable_manager._extra_vars = playbook_vars
    variable_manager.set_inventory(Inventory(loader=DataLoader(), variable_manager=variable_manager))

# Generated at 2022-06-22 11:23:25.172502
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Create a MockFinalQueue
    final_q = multiprocessing_context.SimpleQueue()

    # Create a MockTask object
    class MockTask(object):
        def __init__(self, name='mock'):
            self.name = name
            self.was_task_executed = False
        def __repr__(self):
            return '<MockTask: %s>' % self.name
        def __eq__(self, other):
            return self.name == other
        def __getattr__(self, attr):
            return getattr(self.name, attr)
        def __setattr__(self, attr, value):
            return setattr(self.name, attr, value)
        def _execute(self):
            self.was_task_executed = True

# Generated at 2022-06-22 11:23:34.039634
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    result = {}
    class MyFinalQ(object):
        def send_task_result(self, *args, **kwargs):
            result['send_task_result'] = args, kwargs

    final_q = MyFinalQ()
    task_vars = {}
    host = {}
    task = {}
    play_context = {}
    loader = {}
    variable_manager = {}
    shared_loader_obj = {}

    wp = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    wp.start()
    wp.join()

    assert wp._new_stdin.closed

# Generated at 2022-06-22 11:23:36.959268
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    try:
        p = WorkerProcess(None, None, None, None, None, None, None, None)
        p.start()
    except Exception as e:
        print("Failed to start the worker: ", e)

# Generated at 2022-06-22 11:23:38.020598
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    """ test RunnerProcess.run() """
    raise NotImplementedError

# Generated at 2022-06-22 11:23:47.862999
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import ansible.inventory.host
    import ansible.playbook.play_context
    import ansible.playbook.task
    import ansible.plugins.loader
    import ansible.vars.manager
    import multiprocessing
    import tempfile
    import unittest

    def _get_random_tempfile_path():
        f = tempfile.NamedTemporaryFile()
        f.close()
        return f.name

    class _FakeFinalQueue:
        class _FakeSendTaskResult:
            def __init__(self, parent):
                self._parent = parent

            def __call__(self, *args, **kwargs):
                self._parent._fake_sent_task_results.append((args, kwargs))


# Generated at 2022-06-22 11:24:22.601949
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:24:34.205860
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # This code checks the method start of the class WorkerProcess
    # Tests with the following return values:
    #   - True, if the method returns successfully
    #   - False, if the method returns unsuccessfully

    # Create a mock multiprocessing.Queue() object
    mock_queue = multiprocessing_context.Queue()

    # Create a mock _variable_manager and assign it to the object
    mock_var_manager = mock_queue

    # Create a mock _final_q and assign it to the object
    mock_final_q = mock_queue

    # Create a mock _task_vars object
    mock_task_vars = object()

    # Create a mock _host object
    mock_host = object()

    # Create a mock _task object
    mock_task = object()

    # Create a mock _play_context object


# Generated at 2022-06-22 11:24:42.197392
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = dict()
    host = 'localhost'
    task = 'setup'
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()
    w = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    assert isinstance(w, WorkerProcess)
    assert isinstance(w, multiprocessing_context.Process)
    assert w.start() == None

# Generated at 2022-06-22 11:24:42.627919
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:24:50.266751
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import find_plugin
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # use a non-global variable so unit test does not interfere with others that use this
    manager_module = find_plugin('action')
    # initialize the shared module object, force shared execution
    templar = Templar(loader=None)
    variable_manager = VariableManager()
    variable_manager._extra_vars = dict(ansible_connection='local')
    pc = PlayContext()
    loader = None  # this is unused in this unit test for now

# Generated at 2022-06-22 11:25:00.025407
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/inventory')
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-22 11:25:08.812018
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    class TaskExecutorMock():
        class Host():
            name = 'localhost'
        class Task():
            _uuid = '12345'
            dump_attrs = lambda: None
        _host = Host()
        _task = Task()

        def run(self):
            return None

    def queue_result(*args, **kwargs):
        pass

    display.verbosity = 3
    final_q = type('FakeQueue', (object,), {'send_task_result': queue_result})()
    task_vars = {}
    host = WorkerProcess.TaskExecutorMock._host
    task = WorkerProcess.TaskExecutorMock._task
    play_context = type('FakePlayContext', (object,), {})()
    loader = type('FakeLoader', (object,), {})()

# Generated at 2022-06-22 11:25:17.939589
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import unittest

    class DummyHost(object):
        def __init__(self):
            self.name = 'dummyhost'
            self.vars = dict()
            self.groups = []

    def my_send_task_result(host,
                            task_uuid,
                            result,
                            task_fields=None):
        assert(host == 'dummyhost')
        assert(task_uuid == 'dummytask_uuid')
        assert(result['ok'])
        assert(task_fields is None)
        assert(isinstance(result['result'], dict))

    my_final_q = object()
    my_final_q.send_task_result = my_send_task_result

    class DummyTask(object):
        def __init__(self):
            self._

# Generated at 2022-06-22 11:25:21.567613
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    final_q = Queue()
    task_vars = dict()
    host = dict()
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()
    w = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    w.start()


# Generated at 2022-06-22 11:25:27.687617
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # setup the class to be tested
    task_q = multiprocessing_context.Queue()
    result_q = multiprocessing_context.Queue()
    worker_process = WorkerProcess(task_q, result_q)

    # execute the code to be tested
    worker_process.start()

    # check the results
    assert result_q.get() == 'result'


# Generated at 2022-06-22 11:26:49.699838
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Create the Queue's
    final_q = multiprocessing_context.Queue()

    # Create test data
    task_vars = dict()
    host = 'example.com'
    task = {
        'name': 'test task',
        'action': ['test', 'test1']
    }

    # Create the play_context and loader objects
    play_context = dict()
    loader = multiprocessing_context.Loader()
    variable_manager = multiprocessing_context.VariableManager()
    shared_loader_obj = multiprocessing_context.BaseManager.get_instance()

    # Create the WorkerProcess object
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Call the start method


# Generated at 2022-06-22 11:26:59.210028
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    class FinalQ:
        def send_task_result(self, host_name, uuid, result):
            print('host_name ', host_name)
            print('uuid ', uuid)
            print('result ', result)

    final_q = FinalQ()
    task_vars = dict()
    host = dict()
    task = dict()
    play_context = dict()
    loader = dict()
    variable_manager = dict()
    shared_loader_obj = dict()

    w = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    w.start()
    w.join()

# Generated at 2022-06-22 11:27:01.751727
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    """Unit test: ansible.executor.worker_process.WorkerProcess.start"""

    worker_process = WorkerProcess()
    worker_process.start()

# Generated at 2022-06-22 11:27:10.727055
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    class TestCallback(CallbackBase):
        def __init__(self, display=None):
            super(TestCallback, self).__init__(display)

        def v2_runner_on_ok(self, result, **kwargs):
            print(result)

    class TestWorkerProcess(WorkerProcess):
        def _run(self):
            pass

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-22 11:27:11.274964
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:27:16.000277
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    host = {"name": "example.org"}
    task = {"action": "ping"}
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    play_context = {}
    loader = "loader"
    variable_manager = "variable_manager"
    shared_loader_obj = None
    wp = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    wp.start()

# Generated at 2022-06-22 11:27:20.125395
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    parameters = dict(
        my_var='my_value',
    )
    worker = WorkerProcess(
        parameters,
        '/home/stack/ansible/lib/ansible/playbook/__init__.py'
    )
    worker.start()
    worker.join()

# Generated at 2022-06-22 11:27:29.758050
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import mock
    import multiprocessing
    multiprocessing.set_start_method('forkserver')
    final_q = mock.MagicMock()
    task_vars = mock.MagicMock()
    host = mock.MagicMock()
    task = mock.MagicMock()
    play_context = mock.MagicMock()
    loader = mock.MagicMock()
    variable_manager = mock.MagicMock()
    shared_loader_obj = mock.MagicMock()
    worker = WorkerProcess(
        final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker.run = mock.MagicMock()
    worker.start()

# Generated at 2022-06-22 11:27:30.322076
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:27:30.867291
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass