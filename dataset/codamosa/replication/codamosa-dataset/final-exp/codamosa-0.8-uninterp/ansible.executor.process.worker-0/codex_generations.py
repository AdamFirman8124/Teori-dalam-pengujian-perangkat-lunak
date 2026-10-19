

# Generated at 2022-06-22 11:19:29.647105
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    '''
    Test method run of class WorkerProcess with mocked multiprocessing.Queue
    '''

    import StringIO
    import multiprocessing

    class MockTaskExecutor(object):
        '''
        Mock class TaskExecutor
        '''
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def run(self):
            return self.kwargs

    class MockMultiprocessingQueue(object):
        '''
        Mock class multiprocessing.Queue
        '''
        def __init__(self):
            pass

        def send_task_result(self, *args, **kwargs):
            return (args, kwargs)

    test_host_name = 'test_host_name'
    test_task

# Generated at 2022-06-22 11:19:30.743730
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:19:44.398412
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from multiprocessing import Queue
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    class FakeTask(object):
        def __init__(self, name, task_uuid):
            self.name = name
            self._uuid = task_uuid
            self.block = False

        def dump_attrs(self):
            return '{"name": "%s", "_uuid": "%s", "block": %s}' % (self.name, self._uuid, self.block)

    class FakeTaskQueueManager(TaskQueueManager):
        def __init__(self, results_q):
            self._results_q = results_q

# Generated at 2022-06-22 11:19:51.402257
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # setup
    final_q = None
    task_vars = {}
    host = None
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    # action
    wp = WorkerProcess(
        final_q,
        task_vars,
        host,
        task,
        play_context,
        loader,
        variable_manager,
        shared_loader_obj,
    )
    wp._run()

# Generated at 2022-06-22 11:19:52.086522
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:19:52.792509
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:20:02.247710
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = {'foo': 'bar'}
    host = 'localhost'
    task = 'ping'
    play_context = 'play_context'
    loader = 'loader'
    variable_manager = 'variable_manager'
    shared_loader_obj = None
    worker_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker_process.start()
    worker_process.join()

# Generated at 2022-06-22 11:20:03.106525
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:20:11.139477
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    '''
    This method is used to test the WorkerProcess.run() method. It accepts a
    host, task, play_context as a parameter. Then it calls the run method of the
    WorkerProcess class and returns the result.
    '''
    from ansible.module_utils.common._collections_compat import UserDict
    from queue import Queue
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    localhost = 'localhost'
    task_queue = Queue()
    result_queue = Queue()

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost, '])

# Generated at 2022-06-22 11:20:18.726443
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    Unit test for method start of class WorkerProcess
    '''

    try:
        queue = multiprocessing_context.Queue()
        worker = WorkerProcess(queue, {}, "127.0.0.1", "", "", "", "", "", "")
        worker.start()
    except Exception as e:
        print(e)
        assert 1


# Generated at 2022-06-22 11:20:29.530075
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:20:41.833051
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # construct a fake task with a simple action
    task = dict(action=dict(module='shell', args='echo "Hello, world!"'))

    # launch a worker process to run the task
    queue = multiprocessing_context.Queue()
    worker = WorkerProcess(queue, {}, 'fake_host', task, dict(), dict(), dict(), dict())
    worker.start()
    worker.join()

    # make sure the right results were generated
    result = queue.get()
    assert result['_ansible_verbose_always'] == True
    assert 'failed' not in result
    assert 'rc' in result
    assert result['rc'] == 0
    assert result['stdout'] == 'Hello, world!\n'


# Generated at 2022-06-22 11:20:45.257731
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.vars.unsafe_proxy import UnsafeProxy

    def _safe_dump(self):
        return dict(self._dict)

    def _to_safe_dict(self, full=False):
        return dict(self._dict)

    UnsafeProxy._safe_dump = _safe_dump
    UnsafeProxy._to_safe_dict = _to_safe_dict
    worker = WorkerProcess(None, UnsafeProxy(dict(a=1)), UnsafeProxy(dict(a=1)), UnsafeProxy(dict(a=1)), UnsafeProxy(dict(a=1)), UnsafeProxy(dict(a=1)), UnsafeProxy(dict(a=1)), None)
    worker.start()

# Generated at 2022-06-22 11:20:46.341387
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    raise NotImplementedError

# Generated at 2022-06-22 11:20:57.365518
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost,')
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()


# Generated at 2022-06-22 11:21:08.539776
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    import Queue
    import tempfile
    import time

    #
    # A simple test case using a dummy task which returns a string
    #

    # create a queue in which to store the results
    final_q = multiprocessing.Queue()

    # create the host on which the task is to be executed
    host = "localhost"

    # create a task which returns a string
    task = dict(action=dict(module="command", args=dict(cmd="echo foobar")))

    # create a mock play_context to be used with TaskExecutor
    play_context = dict(basedir=".")

    # create a temp file and mock it as the ansible loader obj
    # _ AnsibleLoader does not have a proper unit test
    (fd_b, fqn_b) = tempfile.mkstem

# Generated at 2022-06-22 11:21:20.102526
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    class FakeFinalQ(object):
        def send_task_result(self, host, task_uuid, result, task_fields=None):
            return True

    class FakeTask(object):
        def __init__(self):
            self._uuid = 'fake-task-uuid'
            self.tags = set()
            self.when = 'always'
            self.notify = []
            self.handlers = []

        def dump_attrs(self):
            return dict(tags=self.tags, when=self.when, notify=self.notify, handlers=self.handlers)

    class FakeHost(object):
        def __init__(self):
            self.name = 'fake-host'
            self.groups = []
            self.vars = dict()

    task_vars = dict()
   

# Generated at 2022-06-22 11:21:20.747815
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:21:31.937836
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader
    import ansible.constants as C

    def _init_worker_process(self):
        def _queue_empty():
            return True

        def _send_worker_msg(self, msg):
            return True

        # create a fake task queue to put things in for the process to consume
        self._final_q._process_queue = multiprocessing_context.Queue()
        self._final_q._cache = dict()

        # monkey patch methods to get us past initialization
        self._final_q._queue_empty = _

# Generated at 2022-06-22 11:21:39.304938
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    def fake_start():
        WorkerProcess.start(WorkerProcess(queue.Queue(), dict(), '127.0.0.1', dict(), dict(), dict(), dict(), dict()))

    try:
        import pytest
        pytest.fail('This test should never run')
    except RuntimeError:
        pass

    try:
        fake_start()
    except AssertionError:
        pass
    except:
        raise AssertionError('This exception should not have been raised')

    assert True is True

# Generated at 2022-06-22 11:22:05.742817
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    from multiprocessing import Queue
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.playbook_executor import PlaybookExecutor

    class TestPlaybookExecutor(PlaybookExecutor):
        def __init__(self, playbooks, inventory, variable_manager, loader, options, passwords):
            self.playbooks = playbooks
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.passwords = passwords

        def run(self):
            pass

   

# Generated at 2022-06-22 11:22:12.484214
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = 'hostname'
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # method start() is not unit testable in this context because it uses multiprocessing module

# Generated at 2022-06-22 11:22:22.856228
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from multiprocessing import JoinableQueue

    from ansible.executor.task_queue_manager import TaskQueueManager

    final_q = JoinableQueue()
    task_vars = dict()

    class Host(object):
        def __init__(self):
            self.name = 'n1'

        def vars(self):
            return dict()

    host = Host()

    class Task(object):
        def __init__(self, uuid=None):
            self._uuid = uuid

        def dump_attrs(self):
            return dict()

    class PlayContext(object):
        pass

    class Loader(object):
        pass

    class VariableManager(object):
        pass

    class SharedLoaderObj(object):
        module_vars = dict()
        group_vars = dict()
       

# Generated at 2022-06-22 11:22:32.577855
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Process, Queue
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(host_list='tests/inventory'))

    play_context = dict(
        connection='local',
        remote_addr=None,
        password=None,
        port=None,
        private_key_file=None,
        become=None,
        become_method=None,
        become_user=None,
        sudo=True,
        sudo_user='notarealuser',
        module_name='shell',
        module_path=None,
        module_args='whoami',
        forks=10,
        become_pass=None,
        check=False,
    )


# Generated at 2022-06-22 11:22:43.866116
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    The os module is mocked by the @patch decorator
    '''
    from ansible import constants as C
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader
    from ansible.vars import VariableManager

    C.DEFAULT_LOAD_CALLBACK_PLUGINS = True
    C.DEFAULT_STDOUT_CALLBACK = 'default'

    # create a mock queue and mock host
    queue = multiprocessing_context.Queue()
    mock_host = type('host', (object,), {'name': 'test_host'})
    mock_host.__class__.get_vars = lambda x: {}

    class MockModule(object):
        def __init__(self):
            self.params = {}


# Generated at 2022-06-22 11:22:55.017583
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader, sources="localhost,")
    host = inventory.get_host("localhost")
    play = Play()

    def _queue_wrapper(q):
        def put(val):
            q.append(val)
        return put

    task_vars = dict()
    final_q = []
    TaskExecutor_final_q = _queue_wrapper(final_q)

# Generated at 2022-06-22 11:23:06.956320
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # mocks of objects passed into the constructor of WorkerProcess
    def task_executor(host, task, task_vars, play_context, new_stdin, loader, shared_loader_obj, final_q):
        return {}

    final_q = mock.MagicMock(spec=Queue)
    final_q.send_task_result = mock.MagicMock()
    task_vars = {}
    host = mock.MagicMock(spec=dict)
    task = mock.MagicMock(spec=dict)
    play_context = mock.MagicMock(spec=dict)
    loader = mock.MagicMock(spec=dict)
    variable_manager = mock.MagicMock(spec=dict)
    shared_loader_obj = mock.MagicMock(spec=dict)
    # set up the mocks
   

# Generated at 2022-06-22 11:23:14.807427
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = 'localhost'
    task = 'ping'
    play_context = {}
    loader = 'loader'
    variable_manager = 'variable_manager'
    shared_loader_obj = 'shared_loader_obj'
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    worker.start()
    worker.join()
    worker.is_alive()

# Generated at 2022-06-22 11:23:15.647456
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:23:22.348599
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    final_q = 'queue'
    task_vars = 'task vars'
    host = 'host'
    task = 'task'
    play_context = 'play_context'
    loader = 'loader'
    variable_manager = 'variable_manager'
    shared_loader_obj = 'shared_loader_obj'
    workerProcess = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    workerProcess.start()
    assert workerProcess is not None

# Generated at 2022-06-22 11:24:05.058794
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import os
    import sys
    import shutil
    import multiprocessing
    import time

    from ansible import errors
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueIterator
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars

# Generated at 2022-06-22 11:24:06.111988
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:24:11.753445
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    '''
    This is a test function to test the start method of class WorkerProcess
    '''

    import multiprocessing

    job_q = multiprocessing.Queue(1)
    res_q = multiprocessing.Queue(1)

    try:
        worker = WorkerProcess(res_q, job_q, dict(), dict(), dict(), dict(), dict(), dict())
        worker.start()
    except Exception as e: # pylint: disable=broad-except
        print('test_WorkerProcess_start: exception')
        print(repr(e))
        return False

    return True

# Generated at 2022-06-22 11:24:22.519451
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    import os
    import sys
    from multiprocessing import Queue
    from ansible.executor.process.worker import WorkerProcess
    from ansible.plugins.loader import load_plugin, plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    # Create a TaskExecutor instance
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../plugins/action'))
    plugin_path = 'shell'
    plugin = load_plugin(plugin_path, plugin_loader)
    connection = plugin(None, task_uuid='dummy')

    # Create a PlayContext instance

# Generated at 2022-06-22 11:24:29.759903
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # dummy WorkerProcess object
    final_q = multiprocessing_context.Queue()
    task_vars = {}
    host = {}
    task = {}
    play_context = {}
    loader = {}
    variable_manager = {}
    shared_loader_obj = {}
    test_worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    assert (0 == test_worker._run())

# Generated at 2022-06-22 11:24:35.306636
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    return_task_result = WorkerProcess.start
    try:
        WorkerProcess.start = Mock(return_value=None)
        cls = WorkerProcess(None, None, None, None, None, None, None, None)
        cls.start()
        WorkerProcess.start.assert_called_once_with(cls)
    finally:
        WorkerProcess.start = return_task_result


# Generated at 2022-06-22 11:24:43.377999
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    from multiprocessing import Queue

    def fake_send_task_result(host, task_uuid, result, task_fields):
        return None

    q = Queue()
    worker = WorkerProcess(
        final_q=q,
        task_vars={},
        host=None,
        task=None,
        play_context=None,
        loader=None,
        variable_manager=None,
        shared_loader_obj=None
    )
    worker._new_stdin = None

    worker._final_q.send_task_result = fake_send_task_result

    worker.run()

# Generated at 2022-06-22 11:24:44.385350
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # TODO: fill this out
    pass

# Generated at 2022-06-22 11:24:52.919934
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    #def test_WorkerProcess():

    import sys
    import traceback
    from jinja2.exceptions import TemplateNotFound

    from ansible.errors import AnsibleConnectionFailure
    from ansible.executor.task_executor import TaskExecutor
    from ansible.module_utils._text import to_text

    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play

    #from ansible.module_utils.basic import *
    #from ansible.module_utils.six import *

    # set up the objects needed to execute
    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.network_os

# Generated at 2022-06-22 11:25:01.389293
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as PlayObj
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueManagerResult
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    class MockHost(object):
        def __init__(self, name):
            self.name = name
            self._vars = dict()
            self._groups = []

        @property
        def vars(self):
            return self._vars


# Generated at 2022-06-22 11:26:23.642646
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import queue
    import tempfile
    import shutil
    import os
    import sys

    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cPickle as pickle

    if PY3:
        from io import StringIO
        stdout_pickle_protocol = 4
    else:
        from cStringIO import StringIO
        stdout_pickle_protocol = 2

    from ansible.plugins.loader import module_loader
    from ansible.module_utils.facts.cache import FactCache

    # make tmp dir
    tmp_dir = tempfile.mkdtemp()

    # make a fake results queue
    FakeFinalQueue = queue.Queue()

    # make a fake inventory
    Fake

# Generated at 2022-06-22 11:26:30.657298
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # test with a fake host
    connection = MagicMock()
    host = MagicMock()
    host.name = "fake_host"
    host.get_vars.return_value = {}
    host.get_groups.return_value = []
    host.get_group_vars.return_value = {}
    host.get_task_vars.return_value = {}
    host.get_variable_manager.return_value = MagicMock()
    host.get_connection.return_value = connection
    host.has_module_utils.return_value = True
    host.get_variable_manager.return_value = MagicMock()

    # test with a fake loader
    loader = MagicMock()
    loader.path_exists.return_value = True
    loader.get_real_file.return_

# Generated at 2022-06-22 11:26:40.957151
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.utils.multiprocessing import MultiprocessingManager
    from ansible.vars.manager import VariableManager
    from .strategy_worker import WorkerQueue

    display.verbosity = 3

    final_q = MultiprocessingManager(couple_type='manager').get_result_queue()
    worker_q = WorkerQueue(final_q)
    worker_q.put(dict(
        play_hosts=[dict(name='worker_test' '', ansible_play_hosts=['worker_test'])],
        play_context=dict(work_dir='/tmp'),
        loader=None,
        variable_manager=VariableManager(),
        task_vars=dict(),
        included_files=dict()
    ))

    worker = WorkerProcess(final_q, worker_q)
   

# Generated at 2022-06-22 11:26:47.565711
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    from multiprocessing import Queue
    from ansible.parsing.dataloader import DataLoader

    host = None
    task = None
    play_context = None
    loader = DataLoader()
    variable_manager = None
    shared_loader_obj = None

    final_q = Queue()
    task_vars = None

    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    assert(worker.run() is None)

# Generated at 2022-06-22 11:26:59.373928
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.become import Become
    from ansible.playbook.become_user import BecomeUser

    class MockPlayContext(object):
        def __init__(self, become, become_method, become_user):
            self.become = become
            self.become_method = become_method
            self.become_user = become_user

    class MockFinalQueue(object):
        def __init__(self):
            self.data = {}


# Generated at 2022-06-22 11:27:10.817550
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import mock
    import multiprocessing
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    SharedPluginLoaderObj = mock.Mock()
    DisplayObj = mock.Mock()

    # Using the multiprocessing module, using a different class
    # inorder to provide a mocked up Queue object
    class QueueMock(object):

        task_result = {}

        # Since method send_task_result() is going to be used in the test
        # provide a mock up method to store the result
        def send_task_result(self, host, uuid, task_result, task_fields):
            self.task_result = task_fields

    QueueObj = QueueMock()


# Generated at 2022-06-22 11:27:15.710835
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():

    # Mock parameters
    final_q = multiprocessing_context.SimpleQueue()
    task_vars = dict()
    host = ''
    task = ''
    play_context = ''
    loader = ''
    variable_manager = ''
    shared_loader_obj = ''

    # Make object with args
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)

    # Test
    worker.start()

# Generated at 2022-06-22 11:27:17.112096
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass


# Generated at 2022-06-22 11:27:27.334384
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    import multiprocessing
    from ansible.executor.play_iterator import TaskIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.multiprocessing import reset_pebook
    reset_pebook()
    manager = multiprocessing.Manager()
    results_queue = manager.Queue()

    def x_sleep(seconds):
        import time
        time.sleep(seconds)

    def get_next_task():
        return x_sleep, (0.01)

    class Host(object):
        def __init__(self, name):
            self.name = name

    class Queue(object):
        def __init__(self):
            self.hostname = "localhost"
            self.task = get_next_task()
            self.task_vars

# Generated at 2022-06-22 11:27:28.224897
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # Unit test for method start of class WorkerProcess
    pass