

# Generated at 2022-06-22 11:19:33.672853
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    class FakeHost:
        def __init__(self):
            self.name = 'fakehost'
            self.vars = dict()
            self.groups = []

    class FakeTask:
        def __init__(self):
            self._ds = 'fake_ds'
            self._task_vars = dict()
            self._role_name = 'fake_role_name'
            self._role_params = dict()
            self._parent = dict()
            self._play = dict()
            self._loader = dict()
            self._block = dict()
            self._loop = dict()
            self._do_not_log = False
            self._uuid = 'fake_uuid'


# Generated at 2022-06-22 11:19:46.119552
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template.template import AnsibleTemplate
    from ansible.parsing.dataloader import DataLoader

    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()

    loader._template_class = AnsibleTemplate

    final_q = Queue()
    task_vars = dict()
    host = 'localhost'
    task = ''
    shared_loader_obj = None

    p = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    p.start()

# Generated at 2022-06-22 11:19:58.770293
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import sys
    import os
    import shutil
    import tempfile

    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.stats import AggregateStats
    from ansible.plugins.callback.default import CallbackModule

    from multiprocessing import Manager, Process

    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueManagerStub

    class Host(object):
        def __init__(self, name):
            self.name = name
            self.vars = dict()
            self.groups = []


# Generated at 2022-06-22 11:20:00.577442
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # unit test needs to be implemented
    print("AnsibleNIT: method run of class WorkerProcess is not tested")

# Generated at 2022-06-22 11:20:09.621671
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # pass

    # mock module to get around the import block in __init__
    from ansible.executor.task_executor import TaskExecutor
    sys.modules['ansible.executor.task_executor'] = TaskExecutor

    # mock module to get around the import block in __init__
    from ansible.executor.connector import Connector
    sys.modules['ansible.executor.connector'] = Connector

    # mock module to get around the import block in __init__
    from ansible.utils.multiprocessing import TaskQueueManager
    sys.modules['ansible.utils.multiprocessing'] = TaskQueueManager

    # mock module to get around the import block in __init__
    from ansible.utils.listify import listify_lookup_plugin_terms

# Generated at 2022-06-22 11:20:22.616016
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from ansible.utils.multiprocessing import fork_context
    from ansible.utils.multiprocessing import ProcessManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.module_utils.six import PY2

    if PY2:
        from StringIO import StringIO
    else:
        from io import StringIO

    fake_task = UnsafeProxy({'id': 1})
    fake_host = UnsafeProxy({'name': 'foo', 'vars': {'ansible_host': 'bar', 'ansible_port': 1234}})
    fake_play_context = UnsafeProxy({'remote_addr': '127.0.0.1'})

    mock_pm = ProcessManager([])

# Generated at 2022-06-22 11:20:32.272615
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    import multiprocessing
    from multiprocessing import Queue

    mp = multiprocessing
    queue = Queue()

    def func(queue):
        a = queue.get()
        b = queue.get()
        c = queue.get()
        queue.put([a, b, c])

    a = WorkerProcess(queue, 'a', 'b', 'c')
    b = mp.Process(target=func, args=(queue,))
    b.start()
    queue.put('a')
    queue.put('b')
    queue.put('c')
    result = queue.get()
    assert result == ['a', 'b', 'c']
    assert b.exitcode == 0



# Generated at 2022-06-22 11:20:40.090714
# Unit test for method run of class WorkerProcess

# Generated at 2022-06-22 11:20:49.411048
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    class Fake_Final_Q:
        def __init__(self):
            self.send_task_result_args = None

        def send_task_result(self, *args, **kwargs):
            self.send_task_result_args = (args, kwargs)

    class Fake_Task:
        def __init__(self):
            self._uuid = '101'
            self.dump_attrs_call = 0

        def dump_attrs(self):
            self.dump_attrs_call += 1
            return self.dump_attrs_call

    class Fake_Host:
        def __init__(self, name):
            self.name = name
            self.vars = dict()
            self.groups = []

    final_q = Fake_Final_Q()
    task = Fak

# Generated at 2022-06-22 11:20:50.483892
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass

# Generated at 2022-06-22 11:21:00.370730
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:21:01.056458
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    return -1

# Generated at 2022-06-22 11:21:09.894583
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    # NOTE: multiprocessing.Process may cause a fork and switch stdin in the process
    # we cannot run this test under it, so instead we use a library based multiprocessing
    # implementation that does not rely on forking and can be run under nosetests.
    # TODO: investigate better unit testing for the process manager code.
    from multiprocessing.dummy import Pool
    from multiprocessing import Process
    try:
        from multiprocessing import set_start_method
        set_start_method('spawn')
    except ImportError:
        pass

    class TaskExecutor(Process):
        def run(self):
            pass

    class Host():
        pass

    class Task():
        pass

    class ResultQueue():
        pass

    class PlayContext():
        pass

    class Loader():
        pass



# Generated at 2022-06-22 11:21:11.421280
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    assert False, "TODO"

# Generated at 2022-06-22 11:21:12.058002
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:21:22.462716
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import os
    import shutil

    m = multiprocessing_context.Manager()
    q = m.Queue()
    p = WorkerProcess(q, None, None, None, None, None, None, None)
    p.start()
    p.run()
    p.join()

    p = WorkerProcess(q, None, None, None, None, None, None, None)
    p.start()
    p.run()
    p.join()
    p.terminate()

    # Test if _hard_exit works:
    temp_dir = os.path.abspath('./_test_WorkerProcess_run_')
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

# Generated at 2022-06-22 11:21:33.686712
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    #Given
    class Queue():
        def send_task_result(self, hostname, task_uuid, executor_result, task_fields):
            assert hostname == 'host'
            assert task_uuid.startswith('tas')
            assert 'failed' not in executor_result
            assert executor_result['exception'] == 'exception'
            assert executor_result['stdout'] == 'stdout'
            assert task_fields == 'task_fields'

    final_q = Queue()
    task_vars = {}
    class Host():
        name = 'host'
    host = Host()
    class Task():
        def dump_attrs(self):
            return 'task_fields'
        _uuid = 'task_uuid'
    task = Task()

# Generated at 2022-06-22 11:21:37.688611
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    multiprocessing_context.multiprocessing = multiprocessing

    from multiprocessing import Queue
    wp = WorkerProcess(Queue(), dict(), dict(), dict(), dict(), dict(), dict(), dict(),)
    wp._run()

# Generated at 2022-06-22 11:21:49.076713
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import DEFAULT_VAULTABLE_ANSIBLE_VARS


# Generated at 2022-06-22 11:21:49.755814
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    pass

# Generated at 2022-06-22 11:22:09.342682
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    multiprocessing_context.Value

# Generated at 2022-06-22 11:22:18.449553
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    from multiprocessing import Queue
    from multiprocessing import Manager
    import json
    import tempfile


    _q = Queue()
    _final_q = None
    _result_q = None

    _play_context = None

    _loader = None
    _variable_manager = None

    _host = None
    _task = None

    _task_vars = None
    _final_q = Manager().Queue()
    _result_q = Queue()

    def mock_dict(**kwargs):
        return kwargs

    mock_display = mock_dict()
    mock_display.debug = mock_dict()

    global display
    display = mock_display
    os.dup = mock_dict(return_value=True)

# Generated at 2022-06-22 11:22:25.495057
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():

    from multiprocessing import Queue
    from nose.tools import assert_equal

    queue = Queue()
    queue.put({'name':'all','hosts':[]})
    queue.put(None)

    ansible_module_names = {'shell', 'command', 'raw', 'script', 'synchronize', 'apt', 'yum', 'apt_key', 'dnf', 'zypper', 'win_shell', 'win_ping'}

    # Create variables
    task_vars = dict()
    play_context = dict()
    task_vars['ansible_connection'] = 'local'
    task_vars['ansible_check_mode'] = False
    play_context['check_mode'] = False

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import Inventory

# Generated at 2022-06-22 11:22:36.454685
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import multiprocessing
    import time
    # import cProfile, pstats, StringIO
    # pr = cProfile.Profile()
    # pr.enable()

    q = multiprocessing.Queue()
    wp = WorkerProcess(q, None, None, None, None, None, None)
    wp.run()
    time.sleep(0.1)
    q.put(1)
    time.sleep(0.1)

    # pr.disable()
    # s = StringIO.StringIO()
    # sortby = 'time'
    # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # ps.print_stats()
    # with open('worker_run_%06d.stats' % os.getpid(), 'w') as f:
    #     f

# Generated at 2022-06-22 11:22:47.424568
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    import ansible.plugins.loader
    import ansible.plugins.action
    import ansible.plugins.cache
    import ansible.plugins.callback
    import ansible.plugins.connection
    import ansible.plugins.lookup
    import ansible.plugins.shell
    import ansible.plugins.strategy
    import ansible.plugins.test
    import ansible.plugins.vars
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class IterableQueue(object):
        '''
        Builds an iterable that reads from a multiprocessing queue
        '''

        def __init__(self):
            self._queue = multiprocessing_context.Queue()

        def __iter__(self):
            return self



# Generated at 2022-06-22 11:22:48.453513
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    pass


# Generated at 2022-06-22 11:22:51.639772
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    w = WorkerProcess(None, None, None, None, None, None, None, None)
    assert(w.start() is None)

# Generated at 2022-06-22 11:23:04.357404
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    # Make public class attribute private
    display = WorkerProcess.display
    WorkerProcess.display = None

    final_q = multiprocessing_context.Queue()
    task_vars = dict()
    host = None
    task = None
    play_context = None
    loader = None
    variable_manager = None
    shared_loader_obj = None

    # Test with failed TaskExecutor
    # Make private function public
    TaskExecutor_run = TaskExecutor.run
    TaskExecutor.run = lambda: dict(failed=True)
    WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj).run()
    assert final_q.get_nowait() == (host.get_name(), task.dump_attrs(), dict(failed=True))

# Generated at 2022-06-22 11:23:15.495942
# Unit test for method start of class WorkerProcess
def test_WorkerProcess_start():
    #verify that start() method of class WorkerProcess function correctly
    from multiprocessing import Queue
    from threading import Thread
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins import callback_loader
    from ansible.errors import AnsibleError

    display = Display()

    class CallbackModule(callback_loader.CallbackBase):
        CALLBACK_VERSION = 2.0

        def __init__(self, display):
            self.display = display

    callback = CallbackModule(display)
    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-22 11:23:22.524997
# Unit test for method run of class WorkerProcess
def test_WorkerProcess_run():
    final_q = multiprocessing.Queue()
    task_vars = {}
    host = multiprocessing.Queue()
    task = multiprocessing.Queue()
    play_context = multiprocessing.Queue()
    loader = multiprocessing.Queue()
    variable_manager = multiprocessing.Queue()
    shared_loader_obj = multiprocessing.Queue()
    ansible_process = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    assert ansible_process != None