

# Generated at 2022-06-13 08:21:05.183761
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.playbook.role_include import IncludeRole

    test_dir = os.path.join(C.DEFAULT_MODULE_PATH, '../../test/integration/')

    add_all_plugin_dir

# Generated at 2022-06-13 08:21:12.286507
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    """
    Test some cases for method add_host.
    """
    # Case 1.
    included_file = IncludedFile('test_file', None, None, None)
    assert included_file.add_host('test_host') == ['test_host']
    # Case 2.
    included_file = IncludedFile('test_file', None, None, None)
    included_file.add_host('test_host')
    assert included_file.add_host('test_host') == ['test_host', 'test_host']
    # Case 3.
    included_file = IncludedFile('test_file', None, None, None)
    included_file.add_host('test_host')
    assert included_file.add_host('test_host') == ['test_host', 'test_host']
    # Case 4.


# Generated at 2022-06-13 08:21:25.046637
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role.includes import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import add_all_plugin_dirs

    # The following code adds all the plugins by loading all the python files present in the directory
    # `lib/ansible/plugins/` and its sub directories.
    # TODO: Find a more elegant way to import the plugins.
    add_all_plugin_dirs()

    loader = DataLoader()
    variable_manager = VariableManager()
    host = Host()
    role_include = RoleInclude()
    role_include2 = RoleInclude()
    role

# Generated at 2022-06-13 08:21:34.095433
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.tasks import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    loader = DataLoader()
    inventory = InventoryManager()

    h1 = inventory.get_host('localhost')
    h2 = inventory.get_host('localhost')

    play = Play()
    play.vars = {}

    # test with include:
    task = Task()
    task.action = 'include'

# Generated at 2022-06-13 08:21:43.916072
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host = "myhost"
    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)

# Generated at 2022-06-13 08:21:53.444958
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    result1 = {'include': 'foo.yml', 'include_args': dict(x=123)}
    result2 = {'include': 'bar.yml', 'include_args': dict(y=456), 'ansible_loop_var': 'item', 'item': 'test'}
    result3 = {'include': 'bar.yml', 'include_args': dict(y=456), 'ansible_loop_var': 'item', 'item': 'test', 'ansible_no_log': True}
    result4 = {'include': 'baz.yml', 'include_args': dict(z=789), 'ansible_loop_var': 'item', 'item': 'test'}

# Generated at 2022-06-13 08:22:02.834990
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.loader import DictDataLoader


# Generated at 2022-06-13 08:22:16.805048
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class MockTask:
        def __init__(self, uuid, action, no_log, loop=False, parent=None):
            self._uuid = uuid
            self.action = action
            self.no_log = no_log
            self.loop = loop
            self._parent = parent

    class MockResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result



# Generated at 2022-06-13 08:22:28.698902
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import collections

    # fake some results
    Result = collections.namedtuple('Result', '_host _task _result')

    Task = collections.namedtuple('Task', 'action loop no_log _parent')
    Role = collections.namedtuple('Role', '_role_name _role_path')

    Host = 'host'
    Arg = 'arg'
    ArgVal = 'argVal'
    Var = 'var'
    VarVal = 'varVal'
    Filename = 'filename'
    ResultVal = 'resultVal'
    IncludeVal = 'includeVal'

    iterator = Role('roleName', '/foo/bar')


# Generated at 2022-06-13 08:22:33.316741
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    obj = IncludedFile('test', 'args', 'vars', 'original task')
    assert obj._hosts == []
    obj.add_host('test')
    assert obj._hosts == ['test']
    try:
        obj.add_host('test')
    except ValueError:
        pass
    else:
        assert False, 'Should have raised a ValueException'


# Generated at 2022-06-13 08:23:00.056929
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.template import Templar

    class FakeOptions(object):
        def __init__(self):
            self.syntax = False
            self.connection = 'ssh'
            self.module_path = None
            self.forks = 5
            self.remote_user = 'root'
            self.private_key_file = None
            self.ssh_common_args = None
            self.ssh_extra_args = None
            self.sftp_extra_args = None
            self.scp_extra_args = None
            self.become = False
            self.become_method = 'sudo'
            self.become_

# Generated at 2022-06-13 08:23:13.069610
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    IncludedFile.process_include_results() Test
    Testing to see if IncludedFile.process_include_results() returns the correct included files given a number of different example results.
    """

    import types
    import utils

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext

    # Create variables
    loader = types.SimpleNamespace(path_dwim='', path_dwim_relative='', get_basedir='')
    variable_manager = types.SimpleNamespace(get_vars='')

    # Create results

# Generated at 2022-06-13 08:23:21.795515
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Play, Playbook, PlayContext
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_source = dict(
        name="test_play_source",
        hosts=["test_play_source_host"],
        gather_facts="no",
        tasks=[
            dict(action=dict(module="include_role", name="test_role"))
        ]
    )

    loader = DataLoader()
    variable_manager = VariableManager()

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:23:33.218527
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''Return the list of included files'''

    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    # Create the Play
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='env'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

# Generated at 2022-06-13 08:23:42.339156
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    from io import StringIO

    display.verbosity = 4
    loader = None
    variable_manager = None
    play = None
    task = None
    host = None
    # 1 -- running the method
    ret = IncludedFile.process_include_results([], None, loader, variable_manager)
    # 2 -- capture stdout and check output
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    ret = IncludedFile.process_include_results([], None, loader, variable_manager)
    assert capturedOutput.getvalue() == ""
    # 3 -- check results
    assert ret == []
    # 4 -- running the method
    object1 = IncludedFile('filename1', {'a': 1, 'b': 2, 'c': 3}, {'d': 4}, 'task1')

# Generated at 2022-06-13 08:23:53.931376
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.vars import VariableManager

    play = Play()
    play.hosts = "all"


# Generated at 2022-06-13 08:24:09.909077
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test with different filename
    included_files = IncludedFile('test_filename.yml', {}, {}, None)
    included_file_other = IncludedFile('another_test_filename.yml', {}, {}, None)
    assert not (included_files == included_file_other)

    # Test with same filename
    included_files = IncludedFile('test_filename.yml', {}, {}, None)
    included_file_other = IncludedFile('test_filename.yml', {}, {}, None)
    assert included_files == included_file_other

    # Test with different args
    included_files = IncludedFile('test_filename.yml', {'key': 'value'}, {}, None)
    included_file_other = IncludedFile('test_filename.yml', {}, {}, None)

# Generated at 2022-06-13 08:24:21.636676
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:24:32.078245
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins import module_loader

    def load_fixture(file_name):
        file_path = os.path.join(os.path.dirname(__file__),
                                 'fixtures',
                                 file_name)
        with open(file_path, 'r') as f:
            return f.read()

    class FakeModuleLoader(module_loader.ModuleLoader):

        def get(self, name, *args, **kwargs):
            class FakeModule():
                RUN_OK = load_fixture('run_ok.txt')
                RUN_FAILED = load_fixture('run_failed.txt')
                RUN_FAILED_WITH_IGNOR

# Generated at 2022-06-13 08:24:40.453610
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test __eq__ method of class IncludedFile

    For the six combinations of bool values in _args and _vars (2^2), we test
    three cases:
    1. when _args and _vars are identical, expect return True
    2. when _args and _vars are different, expect return False
    3. when _args or _vars is empty, expect return False

    """
    i1_args = {'foo': True}
    i1_vars = {'bar': False}
    i2_args = {'foo': True}
    i2_vars = {'bar': False}

    args_same_vars_same = IncludedFile('file1', i1_args, i1_vars, 'task1')

# Generated at 2022-06-13 08:25:23.778293
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    filename = 'filename'
    args = {'a':'args'}
    vars = {'v':'vars'}

    role = Role()
    role._role_path = 'role_path/role_name'

    block = Block()
    block._parent = role

    play = Play()
    play._loader = 'loader'
    play._basedir = 'basedir/roles/role_path/role_name/tasks'
    play._role_contexts = {'role_name': block}

    task1 = TaskIn

# Generated at 2022-06-13 08:25:31.112494
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = [
        IncludedFile(filename='test1.yml', args={}, vars={}, task='task1'),
        IncludedFile(filename='test2.yml', args={}, vars={}, task='task2')
    ]

    included_files = IncludedFile.process_include_results(results)

    assert len(included_files) >= 1


# Generated at 2022-06-13 08:25:32.108098
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass

# Generated at 2022-06-13 08:25:43.700731
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    class testIncludedFile(IncludedFile):
        def __init__(self, filename, args, vars, task):
            self._filename = filename
            self._args = args
            self._vars = vars
            self._task = task
            self._hosts = []
            self._is_role = False

    a = testIncludedFile('a.yml', {}, {}, 't-a.yml')
    b = testIncludedFile('a.yml', {}, {}, 't-a.yml')
    c = testIncludedFile('a.yml', {}, {'name': 'role-a'}, 't-a.yml')
    d = testIncludedFile('a.yml', {'name': 'role-a'}, {}, 't-a.yml')
    e

# Generated at 2022-06-13 08:25:56.592139
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    orig = IncludedFile('filename', 'args', 'vars', 'task')
    same = IncludedFile('filename', 'args', 'vars', 'task')
    different_filename = IncludedFile('filename1', 'args', 'vars', 'task')
    different_args = IncludedFile('filename', 'args1', 'vars', 'task')
    different_vars = IncludedFile('filename', 'args', 'vars1', 'task')
    different_tasks_uuid = IncludedFile('filename', 'args', 'vars', 'task1')
    different_tasks_parent_uuid = IncludedFile('filename', 'args', 'vars', 'task')

    assert orig == same
    assert orig != different_filename
    assert orig != different_args
    assert orig != different_vars
    assert orig != different_tasks_uu

# Generated at 2022-06-13 08:26:06.794143
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import os
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    class Options(object):
        """ dummy class for options """
        hosts = "localhost"
        become = False
        become_user = False
        become_method = False
        become_ask_pass = False
        extra_vars = {}
        verbosity = 0

    inventory = InventoryManager(loader=DataLoader(), sources=["/dev/null"])

# Generated at 2022-06-13 08:26:16.349892
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ifile1 = IncludedFile("filename1", "args1", "vars1", 1)
    ifile2 = IncludedFile("filename1", "args1", "vars1", 2)
    ifile3 = IncludedFile("filename1", "args1", "vars1", 1)
    ifile4 = IncludedFile("filename2", "args2", "vars2", 2)

    assert ifile1 == ifile3
    assert ifile2 == ifile3
    assert not (ifile1 == ifile2)
    assert not (ifile1 == ifile4)
    assert not (ifile2 == ifile4)
    assert not (ifile3 == ifile4)


# Generated at 2022-06-13 08:26:24.283153
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # play
    play = {
        'hosts': 'localhost',
        'tasks': [
            {'include': 'test/test_playbook_include/playbook_include.yml'}
        ]
    }
    # result

# Generated at 2022-06-13 08:26:34.413711
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    inc_files = []
    # Create two results
    results = []
    results.append(IncludedFile(None, None, None, None))
    results.append(IncludedFile(None, None, None, None))

    # Create one iterator
    iterator = []
    # Create one loader
    loader = []

    # Create one variable manager
    variable_manager = []

    IncludedFile.process_include_results(results, iterator, loader, variable_manager)
    assert(len(inc_files) == 2)

if __name__ == '__main__':
    test_IncludedFile_process_include_results()

# Generated at 2022-06-13 08:26:45.351161
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:27:57.829168
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # This unit test is just to verify that the method
    # process_include_results() of class IncludedFile get
    # the proper included_files list. It doesn't test
    # the proper template substitution.
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])

# Generated at 2022-06-13 08:28:04.643673
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # Execute function process_include_results
    # I'm taking two different includes:
    # - a normal include, with a loop
    # - a role include, with a loop
    # Because, if the process is right, the two includes must be grouped.

    # The correct result are:
    # - a list of 2 elements
    # - the item of the list must be an object with the same
    #   properties, as reported in the code

    hosts = []

    from ansible.executor import module_common
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory
    from ansible.playbook import Playbook
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 08:28:13.092576
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 08:28:27.456459
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # initialize
    import ansible.playbook.task_include
    results = []
    host1 = ansible.inventory.host.Host(name='host1')
    host2 = ansible.inventory.host.Host(name='host2')
    iterator = None
    loader = None
    variable_manager = None
    class fakeplay(object):
        def get_variable_manager(self):
            return variable_manager
    play = fakeplay()
    iterator._play = play
    class fake_result(object):
        def __init__(self, _host, _task, _result):
            self._host = _host
            self._task = _task
            self._result = _result
    filename1 = 'include1'
    args1 = {'_raw_params': filename1}
    task1 = ansible.playbook

# Generated at 2022-06-13 08:28:40.429595
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    result = []
    result.append(["/home/username/my_playbook.yml", dict(), dict()])
    result.append(["/home/username/my_playbook.yml", dict(), dict()])

# Generated at 2022-06-13 08:28:49.176372
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import copy
    loader = None
    iterator = None
    variable_manager = None

    test_cases = dict()
    test_case = dict(
        filename = "file1.sql"
        , args = dict()
        , vars = dict(item=1)
        , task = dict(no_log=False)
        , is_role = False
        , result = IncludedFile(filename="file1.sql",args=dict(),vars=dict(item=1),task=dict(no_log=False))
    )
    test_cases["One host and one include file, no optional arguments"] = [test_case]

# Generated at 2022-06-13 08:28:54.182911
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile('f', {'a': 'b'}, {'c': 'd'}, 'task', True)
    b = IncludedFile('f', {'a': 'b'}, {'c': 'd'}, 'task', True)

    assert a == b



# Generated at 2022-06-13 08:29:03.656842
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import yaml
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play_context import PlayContext

    # Create a mock callback
    class ResultsCollector(CallbackBase):

        def __init__(self, *args, **kwargs):
            super(ResultsCollector, self).__init__(*args, **kwargs)
            self.task_ok = {}
            self.task_skipped = {}
            self.task_failed = {}
            self.task_status = {}
            self.task_un

# Generated at 2022-06-13 08:29:15.621535
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Example task results
    #
    # [
    #   {
    #     "_host": "localhost",
    #     "_result": {
    #       "changed": false,
    #       "failed": false,
    #       "include": "main.yml"
    #     },
    #     "_task": "include foo/bar"
    #   }
    # ]

    import ansible.executor.task_queue_manager

    # Create a task queue manager

# Generated at 2022-06-13 08:29:30.093841
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    Тестирует метод IncludedFile.process_include_results.
    """
    # Грязные данные для проверки.
    RESULT_1 = {'failed': False,
                'changed': False,
                'skip_reason': "Conditional result was False",
                'skipped': True,
                'ansible_item_label': "include-tasks-2",
                'ansible_index_var': "ansible_index_var",
                'ansible_loop_var': "ansible_loop_var",
                'ansible_facts': {'ansible_local': {'my_fact': '{{ my_fact }}'}}}
