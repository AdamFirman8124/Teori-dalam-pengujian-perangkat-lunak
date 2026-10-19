

# Generated at 2022-06-13 08:21:00.381880
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar

    task1_include_results = [{"_ansible_parsed":True,"stderr":"", "stdout":"", "stdout_lines":[], "warnings":[], "include_args":{"_raw_params":"/tmp/test.yml", "name":None, "no_log":True, "private":{}, "tags":[], "tasks_from":"{{ test.tasks_from }}", "vars_from":"{{ test.vars_from }}"}, "results":[]}]

# Generated at 2022-06-13 08:21:03.965020
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    obj1 = IncludedFile('filename', 'args', 'vars', 'task', 'is_role')
    obj2 = IncludedFile('filename', 'args', 'vars', 'task', 'is_role')
    try:
        obj1.add_host('host')
        obj2.add_host('host')
    except ValueError:
        x = 1
    else:
        x = 0
    assert x == 1



# Generated at 2022-06-13 08:21:11.171450
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role

    p1 = ansible.playbook.play.Play()
    p1._uuid = 1
    p2 = ansible.playbook.play.Play()
    p2._uuid = 2
    p2._parent = p1
    p3 = ansible.playbook.play.Play()
    p3._uuid = 3
    p3._parent = p2
    t1 = ansible.playbook.task.Task()
    t1._uuid = 1
    t1._parent = p1
    t2 = ansible.playbook.task.Task()
    t2._uuid = 2
    t2._parent = p1
    t3 = ans

# Generated at 2022-06-13 08:21:23.920388
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    my_file_1 = IncludedFile('file1', 'my_args', 'my_vars', 'my_task', 'is_role')
    my_file_2 = IncludedFile('file1', 'my_args', 'my_vars', 'my_task', 'is_role')

    assert(my_file_1 == my_file_2)

    my_file_2._filename = 'file2'
    assert(my_file_1 != my_file_2)

    my_file_2._filename = 'file1'
    my_file_2._args = 'my_args_bis'
    assert(my_file_1 != my_file_2)

    my_file_2._args = 'my_args'
    my_file_2._vars = 'my_vars_bis'

# Generated at 2022-06-13 08:21:33.454977
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test initializing an IncludedFile object with _is_role=False
    filename = "/home/michael/ansible/example1.ya?ml"
    args = dict()
    vars = dict()
    task = type("task", (), {"_uuid": 1,
                             "_parent": type("parent", (), {"_uuid": 1})})
    is_role = False
    included_file = IncludedFile(filename, args, vars, task, is_role)

    # The filename is unique, so the two IncludedFile objects are not equal
    # Create a new IncludedFile object
    new_filename = "/home/michael/ansible/example2.yaml"
    new_included_file = IncludedFile(new_filename, args, vars, task, is_role)

# Generated at 2022-06-13 08:21:43.790014
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.playbook

    class FakeHost(object):
        name = 'some host name'
        def __str__(self):
            return self.name

    class FakeModuleResult(ansible.playbook.ModuleResult):
        def __init__(self, res):
            self._result = res
            self._host = FakeHost()

    loader = FakeLoader()

    class FakeVariableManager():
        def get_vars(self, play=None, host=None, task=None):
            return dict()

    vm = FakeVariableManager()

    def fake_make_iterator(play):
        class FakeIterator(object):
            _play = play

        return FakeIterator()


# Generated at 2022-06-13 08:21:53.337808
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """ test method __eq__ of class IncludedFile """

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    task1 = Task()
    task1._uuid = 'A'

    task2 = Task()
    task2._uuid = 'B'
    task2._parent = task1

    task2_copy = Task()
    task2_copy._uuid = 'B'
    task2_copy._parent = task1

    task1_copy = Task()
    task1_copy._uuid = 'A'

    task3 = Task()
    task3._uuid = 'C'
    task3._parent = task1

    assert(task1 != task2)
    assert(task2 == task2_copy)
   

# Generated at 2022-06-13 08:22:02.743983
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    class Dummy:
        def __init__(self, *_, **__):
            pass

        def get_vars(self, *_, **__):
            return dict()

    loader = Dummy()

# Generated at 2022-06-13 08:22:15.581715
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.sentinel import Sentinel
    from ansible.template import Templar
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.plugins.loader import module_loader

# Generated at 2022-06-13 08:22:26.996176
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 08:22:49.718521
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    iterator = None

    play = Play()
    play.name = "test_play"
    play._groups = ['jumper']
    play._hosts = ['kicker']
    play._variable_manager = None

    task = Task()
    task._uuid = "somerandomuuid"
    task._role = None
    task._parent = None
    task._role_name = "test_role"
    task._play = play
    task._loader = None
    task._block = None
    task.diff = False
    task.always_run = False
    task.loop = None
    task.when = None
    task.name = "test_task"
    task.dep_chain = None
    task.notify

# Generated at 2022-06-13 08:23:01.087042
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task

    results = []
    results.append(Result(host=Host(name='aa'), task=TaskInclude(name='include', action='include', args={'_raw_params': 'file1', 'omit_token': '!secret'})))
    results.append(Result(host=Host(name='bb'), task=TaskInclude(name='include', action='include', args={'_raw_params': 'file2', 'omit_token': '!secret'})))


# Generated at 2022-06-13 08:23:13.615138
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    class Host:
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return self.name == other.name

        def __repr__(self):
            return self.name

    class Task:
        def __init__(self):
            pass

        def __eq__(self, other):
            return isinstance(other, Task)

        def __repr__(self):
            return "<Task()>"

    def test(hosts, task):
        included_files = []
        for host in hosts:
            included_files.append(IncludedFile("", {}, {}, task))
        return included_files

    # Duplicate host, should raise
    hosts = [Host("localhost"), Host("localhost")]
    result = test(hosts, Task())
   

# Generated at 2022-06-13 08:23:22.146905
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Setup environment
    class Task:
        def __init__(self, uuid):
            self._uuid = uuid
        def __eq__(self, other):
            return self._uuid == other._uuid
    class Play:
        def __init__(self, uuid):
            self._uuid = uuid
        def __eq__(self, other):
            return self._uuid == other._uuid
    class Host:
        def __init__(self, uuid):
            self._uuid = uuid
        def __eq__(self, other):
            return self._uuid == other._uuid

    # Setup fixtures
    mock_play1 = Play('play1')
    mock_play2 = Play('play2')
    mock_host1 = Host('host1')

# Generated at 2022-06-13 08:23:33.535578
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    if sys.version_info >= (3, 0):
        long = int

    import ansible.vars.hostvars
    import ansible.vars.manager
    ansible.vars.manager.__sessions__ = dict()
    h = ansible.vars.hostvars.HostVars(dict(), '127.0.0.1')
    ansible.vars.manager.__sessions__['127.0.0.1'] = dict(hostvars=h)

    class Result:
        def __init__(self, host, task, include_result):
            self._host = host
            self._task = task
            self._result = include_result


# Generated at 2022-06-13 08:23:42.565669
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import ansible.playbook.task as task
    t1 = task.Task()
    f1 = IncludedFile('/tmp', {'a': 'b'}, {'c': 'd'}, t1)

    t2 = task.Task()
    f2 = IncludedFile('/tmp', {'a': 'b'}, {'c': 'd'}, t2)

    t3 = task.Task()
    f3 = IncludedFile('/tmp', {'a': 'b'}, {'c': 'd'}, t3)

    t4 = task.Task()
    f4 = IncludedFile('/tmp', {'a': 'b'}, {'c': 'd'}, t4)

    assert f1 == f2
    assert f1 != f3
    assert f1 != f4
    assert f2 != f3

# Generated at 2022-06-13 08:23:54.156205
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    class TestHost:
        def __init__(self):
            self.name = 'testHost'
            self.address = 'test_address'
            self.port = 1234

    h = TestHost()
    assert h.name == 'testHost'
    assert h.address == 'test_address'
    assert h.port == 1234

    inf = IncludedFile('filename', 'args', 'vars', 'task')
    assert inf._filename == 'filename'
    assert inf._args == 'args'
    assert inf._vars == 'vars'
    assert inf._task == 'task'
    assert inf._is_role == False

    inf.add_host(h)
    assert len(inf._hosts) == 1
    assert inf._hosts[0] == h

    # Test adding a host twice raises a ValueError

# Generated at 2022-06-13 08:24:03.591478
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    task = IncludeRole(dict(name='apa'))
    res1 = IncludedFile('apa', {}, {}, task)
    res2 = IncludedFile('apa', {}, {}, task)
    res3 = IncludedFile('bmw', {}, {}, task)
    res4 = IncludedFile('apa', {'name': 'apa'}, {}, task)
    assert(res1 == res2)
    assert(not res3 == res2)
    assert(not res4 == res2)

# Generated at 2022-06-13 08:24:14.893260
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Test add_host
    inc_file1 = IncludedFile('r1/tasks/main.yml', None, None, None)
    inc_file1.add_host('h1')
    inc_file1.add_host('h2')
    inc_file2 = IncludedFile('r1/tasks/main.yml', None, None, None)
    inc_file2.add_host('h1')
    inc_file2.add_host('h2')
    assert inc_file1 == inc_file2
    inc_file3 = IncludedFile('r1/tasks/main.yml', {'a1': 'v1'}, None, None)
    inc_file3.add_host('h1')
    inc_file3.add_host('h2')

# Generated at 2022-06-13 08:24:22.375100
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    variable_manager = None
    loader = None

    # test task include
    block = Block()
    task = TaskInclude(name='include', block=block, role_name=None)
    task._uuid = '12345'
    block._uuid = '23456'
    play = Play()
    play._uuid = '34567'
    task._parent = block
    block._parent = play

# Generated at 2022-06-13 08:24:43.141014
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.dictionary import Dictionary
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

# Generated at 2022-06-13 08:24:58.302655
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from collections import namedtuple
    from ansible.playbook.task import Task

    FakeHost = namedtuple('FakeHost', 'get_name')
    fake_host = FakeHost(lambda: 'test_host')

    FakeTask = namedtuple('FakeTask', '_uuid _parent get_search_path')
    # TODO: replace value 'None' with FakeTask()
    fake_task = FakeTask('fake_task_id', None, lambda: [])

    args = {'a': 1, 'b': 2}
    vars = {'x': 11, 'y': 12}

    # same filename & args & vars & task_id
    inc_file_1 = IncludedFile('123.txt', args, vars, fake_task)

# Generated at 2022-06-13 08:25:10.397589
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:25:18.958406
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    The method process_include_results in the class IncludedFile is tested.
    The method takes a list of results and returns a list of includedFiles.
    An includedFile is added to included_files if it is not present within included_files.
    An includedFile is present if its filename, args and vars are identical to the respective
    values in other included_file. If a host in the results is already present in the included_file
    then the includedFile is incremented and the addition of the host is retried.
    '''

    loader = None
    variable_manager = None

    class TestTaskInclude(TaskInclude):

        def __init__(self, action='include'):
            super(TestTaskInclude, self).__init__(action=action, args={'a':'a', 'b':'b'})


# Generated at 2022-06-13 08:25:32.218990
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import unittest

    """Unit tests for class IncludedFile"""

    import unittest
    from ansible.module_utils.six import PY2

    class TestIncludedFile(unittest.TestCase):

        def test_process_include_results(self):
            hash_keys = dict()
            hash_keys['_uuid'] = 1
            hash_keys['action'] = 2
            hash_keys['include'] = 3
            hash_keys['include_args'] = 4
            hash_keys['ansible_loop_var'] = 5
            hash_keys['ansible_index_var'] = 6
            hash_keys['_ansible_item_label'] = 7
            hash_keys['ansible_loop'] = 8

            results = []

            # Test 1
            result = dict()

# Generated at 2022-06-13 08:25:43.793042
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class MockIterator:
        _play = 'play'
    class MockFileLoader:
        def get_basedir(self):
            return os.getcwd()
        def path_dwim(self, path):
            return os.path.abspath(path)
    class MockVariableManager:
        def get_vars(self, play, host, task):
            return dict()
    class MockHost:
        pass
    class MockRole:
        _role_path = '/'
    class MockTask:
        _parent = None
        no_log = 0

# Generated at 2022-06-13 08:25:56.637641
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    if1 = IncludedFile("filename1", {"arg1": "value1", "arg2": "value2"}, {"var1": "value1", "var2": "value2"}, "task1")
    if1.add_host("host1")
    if1.add_host("host2")

    if2 = IncludedFile("filename1", {"arg1": "value1", "arg2": "value2"}, {"var1": "value1", "var2": "value2"}, "task1")
    if2.add_host("host1")

    assert (if1 == if2) == True

    if3 = IncludedFile("filename2", {"arg1": "value1", "arg2": "value2"}, {"var1": "value1", "var2": "value2"}, "task1")

# Generated at 2022-06-13 08:26:01.632716
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader

    # With include_role and delegated to all hosts

# Generated at 2022-06-13 08:26:10.985120
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    def wrapped_test_func(test_func, test_name, test_data, test_result):
        print('Test %s: %s' % (test_name, 'As Expected' if test_result else 'Failed'))
        test_func(test_data, test_result)

    def test_single_task(data, result):
        assert len(result) == len(data['results'])
        assert result[0]._filename == data['results'][0]['include_results']['included']
        assert result[0]._hosts[0] == data['results'][0]['_host']

    def test_loop_task(data, result):
        assert len(result) == len(data['results'][0]['include_results']['results'])

# Generated at 2022-06-13 08:26:20.544019
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)
    variable_manager.set_play_context(play=Play())
    play = Play()
    play.vars = dict(include_file='data/plays/include_vars.yml')
    include_file = IncludedFile.process_include_results([], play=play, loader=loader, variable_manager=variable_manager)
    assert len(include_file) == 0

    play = Play()

# Generated at 2022-06-13 08:26:52.735346
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager

    class FakeVarsManager(object):
        class FakePlay(object):
            pass

        class FakeIncludedFile(object):
            def __init__(self, filename, args, vars, task, is_role=False):
                self._filename = filename
                self._args = args
                self._vars = vars
                self._task = task
                self._hosts = []
                self._is_role = is_role

            def add_host(self, host):
                self._hosts.append(host)


# Generated at 2022-06-13 08:26:53.681714
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # FIXME: write me
    pass

# Generated at 2022-06-13 08:27:05.795676
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Create instance
    included_file = IncludedFile("filename", "args", "vars", "task")
    # Check that it compares to iteself
    assert included_file == included_file
    # Check that it doesn't compare to something that is not an instance of
    # IncludedFile
    assert not included_file == "something that is not an instance of IncludedFile"
    # Create two instances who differ on the filename
    file_name2 = "filename2"
    included_file_copy = IncludedFile(file_name2, "args", "vars", "task")
    assert not included_file == included_file_copy
    # Create two instances who differ on the args
    args2 = "args2"
    included_file_copy = IncludedFile("filename", args2, "vars", "task")

# Generated at 2022-06-13 08:27:17.215222
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.vars.manager import VariableManager

    class Options(object):
        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = 5
            self.become = None
            self.become_method = None
            self.become_user = None
            self.check = False
            self.diff = False
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.syntax = None
            self.sudo_user = None
            self.sudo = None
           

# Generated at 2022-06-13 08:27:25.476181
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Task:
        def __init__(self, uuid = None, parent = None):
            self._uuid = uuid
            self._parent = parent

    class Play:
        def __init__(self, uuid):
            self._uuid = uuid

    class Host:
        def __init__(self, name):
            self._name = name

    h1 = Host("host1")
    h2 = Host("host2")
    h3 = Host("host3")
    h4 = Host("host4")
    h5 = Host("host5")
    h6 = Host("host6")

    p1 = Play("play1")
    p2 = Play("play2")

    t1 = Task("task1", None)
    t2 = Task("task2", t1)

# Generated at 2022-06-13 08:27:35.154281
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    play = [
        {'hosts': 'host', 'gather_facts': 'no', 'tasks': [
            {'action': 'include', 'include': 'foo', 'vars': dict(a=1, b=2)},
            {'action': 'include', 'include': 'bar', 'vars': dict(a=1, b=3)}
        ]}
    ]

    args = {'_raw_params': 'foo', 'vars': dict(a=1, b=2)}
    task1 = TaskInclude(play=play, connection='local', task_include=args)
    args = {'_raw_params': 'foo', 'vars': dict(a=1, b=2)}
    task2 = TaskInclude(play=play, connection='local', task_include=args)
    args

# Generated at 2022-06-13 08:27:48.272489
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
        unit test for method process_include_results of class IncludedFile
    '''
    #a simulate result for method process_include_results

# Generated at 2022-06-13 08:27:53.123774
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'tasks/main.yml'
    args = {}
    vars = {}
    task = TaskInclude()
    included_file = IncludedFile(filename, args, vars, task)
    assert included_file.__eq__(included_file) == True



# Generated at 2022-06-13 08:28:01.941332
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    p1 = { '_raw_params': 'file1' }
    p2 = { '_raw_params': 'file1' }
    p3 = { '_raw_params': 'file1' }
    p4 = { '_raw_params': 'file2' }
    p5 = { '_raw_params': 'file1', '_parent': '00' }
    p6 = { '_raw_params': 'file1', '_parent': '01' }
    p7 = { '_raw_params': 'file2', '_parent': '01' }
    p8 = { '_raw_params': 'file1', '_parent': '01', '_role_name': 'role1' }

# Generated at 2022-06-13 08:28:12.295396
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:28:42.677747
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import plugin_loader

    results = []
    iterator = None
    loader = plugin_loader
    variable_manager = None

    # Case 1: empty results
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)
    assert included_files == []

    # Case 2: results with two include files, two hosts and tasks

# Generated at 2022-06-13 08:28:50.209262
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    sys.path.append('ansible/executor')
    sys.path.append('ansible/plugins')
    sys.path.append('ansible/plugins/action')
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import RESERVED_VARS

    def get_loader():
        return

# Generated at 2022-06-13 08:29:01.632641
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    import json
    import copy

    sys.path.append(os.path.join(os.getcwd(), 'lib'))

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.vars.manager import VariableManager

    def get_vars(play, host, task):
        return dict(myvar = "bar")

    # There's no easy way to get the module logic out of the module manager, so
    # we'll just construct a fake module that looks like it.
    class FakeModule(TaskInclude):
        def __init__(self, task_include):
            self.task_include = task_include
            super(FakeModule, self).__init

# Generated at 2022-06-13 08:29:13.613684
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # test_process_include_results_include
    #
    # test process_include_results with included file
    #
    class TestHost:
        def __init__(self, name):
            self.name = name

    class TestTask:
        def __init__(self, uuid):
            self._uuid = uuid
            self._parent = None

        def __eq__(self, other):
            return other._uuid == self._uuid

    class TestRoleInclude(TaskInclude):
        def __init__(self, uuid, parent=None):
            super(TestRoleInclude, self).__init__('TestRoleInclude', dict(name='myrole'))
            self._uuid = uuid
            self._parent = parent


# Generated at 2022-06-13 08:29:20.079131
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = './tests/test_playbooks/include_test.yml'
    args = dict()
    vars = dict()
    task = None
    included_file1 = IncludedFile(filename, args, vars, task)
    included_file2 = IncludedFile(filename, args, vars, task)
    assert included_file1 == included_file2

    args = dict(k=1)
    vars = dict()
    included_file3 = IncludedFile(filename, args, vars, task)
    assert included_file1 != included_file3

    args = dict()
    vars = dict(k=1)
    included_file4 = IncludedFile(filename, args, vars, task)
    assert included_file1 != included_file4


# Generated at 2022-06-13 08:29:33.246731
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars

    class DummyInventory(Inventory):
        def __init__(self, hosts_path, groups_path=None, loader=None, variable_manager=None, host_list=None,
                     cache=False, vault_password=None):
            super(DummyInventory, self).__init__(hosts_path, groups_path, loader, variable_manager, host_list, cache, vault_password)
            self._hosts_path = hosts_path
            self._groups_path = groups_path
            self._loader = loader
            self._variable_manager = variable_manager

# Generated at 2022-06-13 08:29:35.955155
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    included_file = IncludedFile.process_include_results([])


# Unit test
if __name__ == '__main__':
    test_IncludedFile_process_include_results()

# Generated at 2022-06-13 08:29:46.318092
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' test_IncludedFile_process_include_results '''

    # TODO: Move this code out of __main__
    import json
    import copy

    logger = logging.getLogger("junit_test")
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('junit_test_IncludedFile_process_include_results.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   

# Generated at 2022-06-13 08:29:52.736021
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_iterator import PlaybookIterator
    from ansible.playbook.play import Play
    import ansible.constants as C
    import os


# Generated at 2022-06-13 08:30:03.000293
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class FakeTask:
        def __init__(self, uuid):
            self._uuid = uuid

        def __eq__(self, other):
            return (self._uuid == other._uuid)

    class FakeParent:
        def __init__(self, uuid):
            self._uuid = uuid

        def __eq__(self, other):
            return (self._uuid == other._uuid)

    # Example 1
    fake1 = FakeTask('uuid1')
    fake2 = FakeParent('uuid2')
    file1 = IncludedFile("filename1", "args1", "vars1", fake1)
    fake1._parent = fake2
    file2 = IncludedFile("filename1", "args1", "vars1", fake1)
    fake1._parent = fake2