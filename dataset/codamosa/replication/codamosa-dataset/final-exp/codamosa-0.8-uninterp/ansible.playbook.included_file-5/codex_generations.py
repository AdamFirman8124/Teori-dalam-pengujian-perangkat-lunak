

# Generated at 2022-06-13 08:21:17.870165
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.plugins import module_loader

    sample_task_result = dict(
        includes=dict(
            files=dict(
                path_to_task_file="/dev/null",
                include_args={},
                include_result={},
                include_raw_params="my_include.yml"
            )
        )
    )

    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'modules'))

    actual_tasks = []


# Generated at 2022-06-13 08:21:29.055737
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    class Host(object):
        def __init__(self, name):
            self.name = name
            self._variable_manager = None
            self._data = dict()

        def get_vars(self):
            return self._data

        def set_variable_manager(self, variable_manager):
            self._variable_manager = variable_manager

        def get_variable_manager(self):
            return self._variable_manager


# Generated at 2022-06-13 08:21:33.441130
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    tmp = IncludedFile("/tmp/foo", {'a':'a'}, {'b':'b'}, None)
    tmp2 = IncludedFile("/tmp/foo/foo2", {'a':'a'}, {'b':'b'}, None)

    results = []

    host1 = 'foo_host1'
    host2 = 'foo_host2'
    host3 = 'foo_host3'
    host4 = 'foo_host4'

    res1 = type('', (), {})()
    res1._host = host1
    res1._task = tmp

# Generated at 2022-06-13 08:21:39.569910
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = []
    results.append(None)
    results.append(None)
    results.append(None)
    results.append(None)
    results.append(None)

    results[0]._host = 'localhost'
    results[0]._task = 'task4'
    results[0]._result = {'include': 'include1', 'include_args': {'custom_var': 'value'}, 'ansible_loop_var': 'item'}

    results[1]._host = 'localhost'
    results[1]._task = 'task4'
    results[1]._result = {'include': 'include2', 'include_args': {}, 'ansible_loop_var': 'item'}

    results[2]._host = 'localhost'
    results[2]._task = 'task4'

# Generated at 2022-06-13 08:21:50.954867
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.playbook.block import TaskBlock
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.utils.vars import combine_vars

    class ActionBase(object):
        def __init__(self):
            self._search_path = 'dummy'
            self._role_name = 'dummy'

# Generated at 2022-06-13 08:22:01.321029
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.vars import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_result import TaskResult

    included_files = []
    included_files.append(IncludedFile("/root/jimmy.yml", dict(), dict(), "task"))
    included_files.append(IncludedFile("/root/jimmy.yml", dict(), dict(), "task"))

    # Make results for process_include_results

# Generated at 2022-06-13 08:22:15.093297
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    loader = DictDataLoader({
        '/etc/ansible/playbooks/playbook.yml': """
        - hosts: all
          include: '/etc/ansible/playbooks/inc_playbook.yml'
          tasks:
            - debug:
                msg: one
        """,
        '/etc/ansible/playbooks/inc_playbook.yml': """
        - hosts: all
          tasks:
            - debug:
                msg: two
        """,
    })

    for playbook in ['/etc/ansible/playbooks/playbook.yml', 'file:///etc/ansible/playbooks/playbook.yml']:
        pb = Playbook.load(playbook, loader=loader, variable_manager=VariableManager())
        iterator = pb.get_iterator()


# Generated at 2022-06-13 08:22:26.792549
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible import variables
    res = []
    res.append(
        FakeResult(
            FakeTask(action='include_tasks', loop=False),
            FakeHost('localhost'),
            FakeTaskResult(include='../tasks/foo.yml')
        )
    )
    res.append(
        FakeResult(
            FakeTask(action='include_role', loop=False),
            FakeHost('localhost'),
            FakeTaskResult(include='../roles/foo')
        )
    )
    res.append(
        FakeResult(
            FakeTask(action='include_tasks', loop=False),
            FakeHost('localhost'),
            FakeTaskResult(include='../tasks/bar.yml')
        )
    )

# Generated at 2022-06-13 08:22:39.397051
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'tests/test/file'
    args = {'name': 'test'}
    vars = {'test': 'test'}
    task = None
    is_role = False

    included_file = IncludedFile(filename, args, vars, task, is_role)
    included_file_same = IncludedFile(filename, args, vars, task, is_role)
    included_file_other_filename = IncludedFile('tests/test/file2', args, vars, task, is_role)
    included_file_other_args = IncludedFile(filename, {'other': 'test'}, vars, task, is_role)
    included_file_other_vars = IncludedFile(filename, args, {'other': 'test'}, task, is_role)
    included_file_other_task = Included

# Generated at 2022-06-13 08:22:52.644038
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    for key in C._ACTION_INCLUDES:
        # first create a task object
        task = Task()
        task._uuid = 'task_uuid'
        # then create a play_context object
        play_context = PlayContext()
        play_context._uuid = 'play_context_uuid'
        # then create a task_result object
        task_result = TaskResult(host='host', task=task, play_context=play_context)
        # finally create two included_files object

# Generated at 2022-06-13 08:23:14.788624
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Verify that the __eq__ method of IncludedFile works as expected.
    """

    x = IncludedFile('/path/to/file.yml', {'key': 'value'}, {'key': 'value'}, None)
    y = IncludedFile('/some/other/file.yml', {'other_key': 'other_value'}, {'key': 'value'}, None)
    z = IncludedFile('/path/to/file.yml', {'key': 'value'}, {'key': 'value'}, None)

    assert(x == x)
    assert(x == z)
    assert(not x == y)

# Generated at 2022-06-13 08:23:22.849616
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class MockTask:
        def __init__(self):
            self._uuid = 'test-task-uuid'
    class MockPlay:
        def __init__(self):
            self._uuid = 'test-play-uuid'

    task1 = MockTask()
    task2 = MockTask()
    task1._parent = MockPlay()
    task2._parent = MockPlay()

    inc1 = IncludedFile('/foo/bar.yml', {}, {}, task1)
    inc2 = IncludedFile('/foo/bar.yml', {}, {}, task1)
    inc3 = IncludedFile('/foo/bar.yml', {'baz': 1}, {}, task1)
    inc4 = IncludedFile('/foo/baz.yml', {}, {}, task1)
    inc5 = Included

# Generated at 2022-06-13 08:23:34.371706
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_executor import TaskExecutor

    inventory = BaseInventory(host_list=[
        'host1.example.com',
        'host2.example.com',
        'host3.example.com',
        'host4.example.com',
        'host5.example.com',
    ])

    # FIXME: mock this stuff

# Generated at 2022-06-13 08:23:43.057325
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.plugins import include_role_plugin
    from ansible.template import Templar
    from ansible.vars import VariableManager
    loader = 'loader'
    results = 'results'
    itr = 'itr'
    variable_manager = VariableManager()
    display = Display()
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    # Test case: Role name is absolute path to a role
    play = Play()
    task = IncludeRole()
    task.action = 'include_role'
    task.args = {'name': '/home/user/role1'}
    task._parent = play
    task._role_name = 'role1'

# Generated at 2022-06-13 08:23:48.540758
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Create the expected object
    filename = '/path/to/filename'
    args = {'arg1': 'val1'}
    vars = {'var1': 'val1'}
    task = TaskInclude()
    task._uuid = 'UUID'
    task._parent = object()
    task._parent._uuid = 'PARENT_UUID'
    expected = IncludedFile(filename, args, vars, task)
    assert(expected == IncludedFile(filename, args, vars, task))

    # Non existing attribute should return False
    assert (expected == IncludedFile(filename, args, vars, task, is_role=True) == False)

    # 'filename' does not match
    other = IncludedFile(filename + '!', args, vars, task)
    assert (expected == other == False)
   

# Generated at 2022-06-13 08:23:57.970194
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test for the __eq__ method.

    Loader instance is needed for the test.
    """
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play_context import PlayContext

    config_manager = ConfigManager(config_data=dict())
    config_manager.get_config_value = lambda *args, **kwargs: None

    loader = config_manager.load_provider(os.getcwd())

    task = TaskInclude(loader=loader, play_context=PlayContext(), task_include=0, inherited_variables={})
    included_file_1 = IncludedFile('filename', 'args', 'vars', task)
    included_file_2 = IncludedFile('filename', 'args', 'vars', task)

# Generated at 2022-06-13 08:24:09.656155
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.playbook.role_include

    FAKE_INCLUDED_FILE = 'fake_included_file_name'

    def _get_fake_result(return_value=None, include_args=None, loop_var='host', include_index_var=None, include_item_label=None, include_loop=None, failed=False, skipped=False):
        class FakeResult(object):
            class FakeTask(object):
                def __init__(self, action):
                    self.action = action
                def __eq__(self, other):
                    return self.action == other

            class FakeHost(object):
                def __init__(self, hostname):
                    self.name = hostname
                    self.vars = {}
                def __eq__(self, other):
                    return self.name == other



# Generated at 2022-06-13 08:24:16.720408
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import sys
    import unittest

    sys.modules['ansible'] = type('', (), {'constants':type('', (), {'__file__':'', '__name__':'constants'})})
    from ansible.plugins.loader import action_loader, cache_loader, callback_loader, connection_loader, shell_loader, strategy_loader
    from ansible.plugins.action import ActionBase
    from ansible.plugins.shell import ShellModule
    from ansible.plugins.connection import ConnectionBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

# Generated at 2022-06-13 08:24:24.518739
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a1 = IncludedFile("filename1", {"args1": 1}, {"vars1": 1}, {"task": 1}, True)
    a2 = IncludedFile("filename1", {"args1": 1}, {"vars1": 1}, {"task": 1}, True)
    assert a1 == a2
    a3 = IncludedFile("filename1", {"args1": 1}, {"vars1": 1}, {"task": 2}, True)
    assert a1 != a3


# Generated at 2022-06-13 08:24:33.730578
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    ret1 = {}
    ret2 = {}

    res1 = Bunch()
    res2 = Bunch()

    res1._host = 'host1'
    res1._task = Bunch()
    res1._task._parent = Bunch()
    res1._task._parent._uuid = '1'
    res1._task._uuid = '2'
    res1._result = ret1

    res2._host = 'host1'
    res2._task = Bunch()
    res2._task._parent = Bunch()
    res2._task._parent._uuid = '1'
    res2._task._uuid = '2'
    res2._result = ret2

    results = [res1, res2]

    iterator = Bunch()

    loader = Bunch()

    vm = Bunch()

# Generated at 2022-06-13 08:25:12.241962
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from collections import namedtuple

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    class FakeVarsModule(HostVars):

        def __init__(self):
            self.vars = {}

        def get_vars(self, loader=None, play=None, host=None, task=None):
            return {}

    class FakePlay(object):

        def __init__(self):
            self.hosts = 'localhost'

    class FakeIncludedFile(object):

        def __init__(self, filename, args, vars, task, is_role=False):
            self._filename = filename

# Generated at 2022-06-13 08:25:24.293956
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    results = [
        Result(host=inventory.get_host('localhost'), task=None, result={'include': 'test.yml'}),
        Result(host=inventory.get_host('localhost'), task=None, result={'include': 'test.yml'})
    ]

    included_files = IncludedFile.process_include_results(results, None, loader, variable_manager)

# Generated at 2022-06-13 08:25:39.377227
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile('file1',{'key1':'value1'},{'key2':'value2'},'task1')
    b = IncludedFile('file2', {'key3': 'value3'}, {'key4': 'value4'}, 'task2')
    assert False == (a==b)
    b = IncludedFile('file1', {'key3': 'value3'}, {'key4': 'value4'}, 'task2')
    assert False == (a == b)
    b = IncludedFile('file1', {'key1': 'value1'}, {'key4': 'value4'}, 'task2')
    assert False == (a == b)
    b = IncludedFile('file1', {'key1': 'value1'}, {'key2': 'value2'}, 'task2')

# Generated at 2022-06-13 08:25:47.598336
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import mock
    mock_host = mock.MagicMock()
    mock_task = mock.MagicMock()
    mock_task2 = mock.MagicMock()
    mock_task.action = 'include'
    mock_task2.action = 'include'
    mock_task.loop = True
    mock_task2.loop = True
    mock_task.loop_control = dict()
    mock_task2.loop_control = dict()
    mock_task2.action = 'role'
    mock_task.no_log = False
    mock_task2.no_log = False
    mock_task2._parent = mock_task
    mock_task.args = dict()
    mock_task.args['_raw_params'] = 'some_task_included_file.yml'
    mock_task.get_

# Generated at 2022-06-13 08:26:00.522843
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import random
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class RunnerMock(object):
        def __init__(self, host, task, res, task_vars, loader, variable_manager):
            self._host = host
            self._task = task
            self._result = res
            self.task_vars = task_vars
            self._loader = loader
            self._variable_manager = variable_manager
            self._task_execution_status = {}

        def get_description(self):
            return "Runner"

    class PlayMock(object):
        def __init__(self, name):
            self.name = name



# Generated at 2022-06-13 08:26:08.855807
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    import os

    class MyLoader(object):
        @staticmethod
        def get_basedir():
            return "/some/basedir"

        @staticmethod
        def path_dwim_relative(base, relative, path, is_role=False):
            return path


# Generated at 2022-06-13 08:26:19.338796
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    A = Task(name='A', action='include', loop='1')
    B = Task(name='B', action='include', loop='2')
    C = Task(name='C', action='include_tasks', loop='3')
    D = Task(name='D', action='include_role', loop='4')
    E = Task(name='E', action='include_vars', loop='5')
    F = Task(name='F', action='import_tasks', loop='6')

# Generated at 2022-06-13 08:26:31.398110
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    results = [
        {'include_result':{'skipped':False, 'failed':False, 'meta':{}, 'invocation':{'module_name':'tasks', 'module_args':'include=role', 'module_complex_args':{'role':'test_role'}}}}
    ]
    iterator = []
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)
    assert len(included_files) == 1
    assert included_files[0]._filename == 'test_role'

if __name__ == '__main__':
    test_IncludedFile_

# Generated at 2022-06-13 08:26:42.563506
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # The host already exists for this include, advance forward, this is a new include
    filename = 'abc'
    args = {'name':'abc'}
    vars = {}
    task = IncludedFile(filename, args, vars, None)

    same_filename = 'abc'
    same_args = {'name':'abc'}
    same_vars = {}
    same_task = IncludedFile(same_filename, same_args, same_vars, None)
    try:
        assert task == same_task
    except ValueError:
        raise ValueError('Unit test for method __eq__ of class IncludedFile failed!')

    diff_filename = 'def'
    diff_args = {'name':'def'}
    diff_vars = {}

# Generated at 2022-06-13 08:26:52.338362
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    test_filename = "tests/test_include_file.yml"
    test_content = """
    - name: include file
      action: include test_include_file.yml include_vars=vars.yml
      tags: included
    - name: include file
      action: include test_include_file.yml include_vars=vars.yml
      tags: included
    """.strip()

    check_filename = "tests/check_include_file.yml"

# Generated at 2022-06-13 08:28:04.816523
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager)

    first_task = Task()
    first_task.action = 'include'
    first_task._role_name = 'defaults'

    second_task = Task()
    second_task.action = 'include'
    second_task._role_name = 'defaults'

    play_context = PlayContext()
    play = Play()
    play.hosts = "localhost"
    play.name = 'test'

# Generated at 2022-06-13 08:28:13.134297
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.plugins import loader
    from ansible.parsing.loader import DataLoader
    from ansible.executor.playbook_iterator import PlayIterator

    loader.clear_all_data()
    loader.add_directory(C.DEFAULT_LOADER_PATH)

    class Options(object):
        connection = 'local'
        module_path = None
        forks = None
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False
        private_key_file = C.DEFAULT_PRIVATE_KEY_FILE
        remote_user = 'ansible'
        verbosity = 3
        timeout = 10

# Generated at 2022-06-13 08:28:26.212691
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class FakeResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class FakeIterator:
        def __init__(self, play):
            self._play = play

    class FakeHost:
        def __init__(self, name):
            self.name = name

    class FakePlay:
        def __init__(self, basedir):
            self._basedir = basedir

    class FakeTask:
        def __init__(self, uuid, no_log, search_path, action, loop, args, parent, role, from_files):
            self._uuid = uuid
            self.no_log = no_log
            self.get_search_path = lambda: search_path
            self.action = action


# Generated at 2022-06-13 08:28:36.980109
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # This unit test compares the output of process_include_results method
    # with the expected output of the method.
    # The expected output is taken from `ansible-playbook --list-tasks --list-hosts
    # -i ../../../test/sanity/playbooks/hosts -vvvv ../../../test/sanity/playbooks/include_no_loop.yml'
    # This include test doesn't use loop and hence include_results has only
    # one result and play has only one host.
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 08:28:44.287197
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    iterator = object()
    loader = object()
    variable_manager = object()

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

    block = object()
    play_context = PlayContext()
    play_context.network_os = 'network_os'
    play_context.remote_addr = 'remote_addr'

    var1 = {}
    var2 = {}
    var3 = {}
    var4 = {}
    var5 = {}
    var6 = {}

    result = object()
    result._host = object()
    result._task = object()
    result._task._uuid = 'uuid'

    task_uuid

# Generated at 2022-06-13 08:28:50.452006
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeTask:

        def __init__(self, _uuid, _parent):
            self._uuid = _uuid
            self._parent = _parent
            self.action = None
            self._role_name = None
            self._from_files = None
            self._role = None

        def get_search_path(self):
            pass

        def copy(self):
            pass

    class FakeHost:
        def __init__(self, _name):
            self._name = _name

        def get_name(self):
            return self._name

    ansible_play_hosts = ["host1", "host2", "host3"]
    play_host1 = FakeHost(ansible_play_hosts[0])
    play_host2 = FakeHost(ansible_play_hosts[1])


# Generated at 2022-06-13 08:29:01.828006
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

    play = Play().load(dict(
        name='minimal',
        hosts='all',
        vars={},
        roles=[],
        tasks=[])
    )
    block = Block().load(dict(
        name='minimal',
        roles=[],
        tasks=[])
    )


# Generated at 2022-06-13 08:29:13.941369
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    ROLE_PATH = 'playbooks/test/roles'

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()

    taskq = TaskQueueManager(
        inventory=None,
        variable_manager=variable_manager,
        loader=loader,
        options=None,
        passwords=None
    )

    results = []

# Generated at 2022-06-13 08:29:28.642997
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    '''
    Test method __eq__ of class IncludedFile.
    '''
    class Mock_task:

        def __init__(self):
            self._uuid = "this is uuid"
            self._parent = Mock_play()

        def get_search_path(self):
            return '/etc/ansible/playbooks/file'

    class Mock_play:

        def __init__(self):
            self._uuid = "this is uuid"

    mock_task = Mock_task()
    file1 = IncludedFile(
        '/etc/ansible/playbooks/file/file1.yaml',
        {'_raw_params': '/etc/ansible/playbooks/file/file1.yaml'},
        'test vars',
        mock_task,
        is_role=False)
   

# Generated at 2022-06-13 08:29:38.135908
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    task = {"action": "", "include": "", "loop": "", "_parent": "", "_role_name": "", "_role": "", "FROM_ARGS": "", "no_log": ""}

    results = [{"_host": "", "_task": task, "_result": {"skipped": "", "failed": "", "include_args": {"_raw_params": ""},
                                                       "ansible_loop_var": "", "ansible_index_var": "",
                                                       "_ansible_item_label": "", "ansible_loop": "", "include": ""}}]
    iterator = {"_play": ""}
    loader = {"get_basedir": ""}
    variable_manager = {"get_vars": ""}
