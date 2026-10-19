

# Generated at 2022-06-13 08:20:57.133910
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    This is a unit test for method __eq__ in class IncludedFile.
    """
    # The following tests test the __eq__ method.
    # The test case is a dictionary with 4 keys and their respective value for testing the __eq__ method:
    #       case_no, filename, args, vars and is_role.
    # case_no refers to the test case number.
    # filename, args, vars and is_role are the parameters passed in to the __eq__ method in the test cases.

# Generated at 2022-06-13 08:21:04.375802
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Test with a loop that is skipped.
    included_files = IncludedFile.process_include_results([
        {'_host': 'foo', '_task': {'action': 'include', 'loop': True},
         '_result': {'results': [{'include': './path/file.yml'},
                                 {'include': './path/file.yml'},
                                 {'include': './path/file.yml', 'skipped': True}],
                    'msg': ''}}
    ], None, None, None)
    assert len(included_files) == 1
    assert included_files[0]._filename == './path/file.yml'
    assert included_files[0]._args == {}
    assert included_files[0]._hosts == ['foo']
    assert included_

# Generated at 2022-06-13 08:21:11.558583
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    results = [test_result1, test_result2, test_result3, test_result4, test_result5, test_result6, test_result7, test_result8]

    iterator = object

    loader = object

    variable_manager = object

    results = IncludedFile.process_include_results(results, iterator, loader, variable_manager)


# Generated at 2022-06-13 08:21:24.069646
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    sources = '/dev/null'
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:21:32.925333
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_execute import TaskExecutor, PlayContext
    from ansible.plugins.loader import filter_loader
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    group_vars = {}
    host_vars = {}

    # setup inventory

# Generated at 2022-06-13 08:21:39.224910
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible import inventory
    from ansible import variables as vars_mgr
    from ansible.playbook import play

    class Task:
        pass

    class TaskInclude:
        def __init__(self, parent):
            self.parent = parent

    class Result:
        def __init__(self, host, task, result):
            self.host = host
            self.task = task
            self.result = result

    inventory = inventory.Inventory(host_list=[])
    vars_mgr = vars_mgr.VariableManager()
    play = play.Play()

    task1 = Task()
    task1.action = 'include'
    result1 = Result(inventory.get_host('localhost'), task1, {'include': '../../../test1'})


# Generated at 2022-06-13 08:21:47.105544
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename1 = "file1.txt"
    args1 = {"arg1": "value1"}
    vars1 = {"var1": "value1"}
    task1 = "task1"
    filename2 = "file2.txt"
    args2 = {"arg2": "value2"}
    vars2 = {"var2": "value2"}
    task2 = "task2"

    inc_file1 = IncludedFile(filename1, args1, vars1, task1)
    inc_file2 = IncludedFile(filename2, args2, vars2, task2)

    assert inc_file1 == inc_file1
    assert inc_file2 == inc_file2

    assert not inc_file1 == inc_file2
    assert not inc_file2 == inc_file1

# Generated at 2022-06-13 08:21:55.496298
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ifil1 = IncludedFile('filename', 'args', 'vars', 'task', 'is_role=False')
    ifil2 = IncludedFile('filename', 'args', 'vars', 'task', 'is_role=False')
    ifil3 = IncludedFile('filename', 'args', 'varss', 'task', 'is_role=False')
    ifil4 = IncludedFile('filename', 'args', 'vars', 'tasks', 'is_role=False')
    ifil5 = IncludedFile('filenames', 'args', 'vars', 'task', 'is_role=False')
    ifil6 = IncludedFile('filename', 'args', 'vars', 'task', 'is_role=False')

    assert ifil1 == ifil2
    assert ifil1 != ifil3
    assert ifil1 != ifil

# Generated at 2022-06-13 08:22:03.815822
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class FakeHost:
        def __init__(self, name):
            self.name = name

    class FakeTask:
        def __init__(self, no_log, action, loop, parent=None, role=None, role_name=None):
            self.no_log = no_log
            self.action = action
            self.loop = loop
            self.parent = parent
            self.role = role
            self.role_name = role_name
            self._from_files = {}

        def copy(self):
            return FakeTask(self.no_log, self.action, self.loop,
                            parent=self.parent, role=self.role, role_name=self.role_name)


# Generated at 2022-06-13 08:22:08.962315
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.vars.manager import VariableManager

    add_all_plugin_dirs()

    # Test data
    # Test play
    hosts = [
        'host1',
        'host2'
    ]

# Generated at 2022-06-13 08:22:37.328262
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader
    import ansible.utils.plugin_docs

    class _ModuleDocs(ansible.utils.plugin_docs.ModuleDocParser):
        pass

    # Create a mock module_doc parser
    plugin_docs = _ModuleDocs(module_generator=None)

    # Create a mock set of results
    results = []

    # Create 2 mock hosts
    hosts = ['host1', 'host2']

    # Create a mock original_task
    original_task = object()

    # Create a mock iterator
    iterator = object()

    # Create a mock loader
    class _loader():
        def path_dwim(self, basedir, patterns=None, include_hidden=False, exclude_extensions=None):
            return basedir
    loader = _loader()

    # Create a mock variable_manager

# Generated at 2022-06-13 08:22:48.907482
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from six import string_types

    class TestPlaybookIteratorProcessIncludeResults(unittest.TestCase):
        def test_process_include_results(self):
            inventory = make_inventory()
            variable_manager = VariableManager()

            loader = object()
            iterator = object()

            host = inventory.get_host(u'localhost')
            host.set_variable(u'foo', u'bar')

            task = object()
            task._role = None
            task._role_name = None

            res = object()
            res._host = host
            res._result = {u'include_args': {}, u'include': u'test.yml'}
            res._task = task

           

# Generated at 2022-06-13 08:22:54.229377
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ifiles = []
    ifiles.append(IncludedFile("/tmp/test.yml", dict(), dict(), dict()))
    ifiles.append(IncludedFile("/tmp/test.yml", dict(), dict(), dict()))
    assert(ifiles[0] == ifiles[1])

    ifiles.append(IncludedFile("/tmp/test.yml", dict(extra="1"), dict(), dict()))
    assert(ifiles[0] != ifiles[2])

    ifiles.append(IncludedFile("/tmp/test.yml", dict(), dict(extra="1"), dict()))
    assert(ifiles[0] != ifiles[3])

    t = dict(uuid='xxxxxxxx')
    ifiles.append(IncludedFile("/tmp/test.yml", dict(), dict(), t))


# Generated at 2022-06-13 08:23:04.425544
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # First set up several results.
    import ansible.playbook.play_context
    res1 = ansible.playbook.play_context.AggregateResult()
    res1._host = 'testhost'
    res1._task = 'testtask'
    res1._result['include_args'] = 'someargs'
    res1._result['include'] = 'someinclude'
    res1._result['ansible_search_path'] = 'somesearchpath'

    res2 = ansible.playbook.play_context.AggregateResult()
    res2._host = 'testhost2'
    res2._task = 'testtask'
    res2._result['include_args'] = 'someargs'
    res2._result['include'] = 'someinclude'

# Generated at 2022-06-13 08:23:15.477407
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    itf = IncludedFile('/etc/hosts', {'foo': 'bar'}, {'baz': 'qux'}, 'this_is_a_task')
    assert itf == itf

    itf_equal = IncludedFile('/etc/hosts', {'foo': 'bar'}, {'baz': 'qux'}, 'this_is_a_task')
    assert itf == itf_equal

    assert itf != ['foo', 'bar']
    itf_not_equal = IncludedFile('/etc/not_hosts', {'foo': 'bar'}, {'baz': 'qux'}, 'this_is_a_task')
    assert itf != itf_not_equal

# Generated at 2022-06-13 08:23:27.807093
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    This test validates the method process_include_results() of class IncludedFile.
    :return:
    """

    loader, variable_manager, results = get_mocked_objects()

    included_files = IncludedFile.process_include_results(results, loader, variable_manager)

# Generated at 2022-06-13 08:23:39.032502
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeIncludeResult:
        def __init__(self, include, task):
            self._result = {'include': include}
            self._task = task
            self._host = 'foo'
            self._task._parent = None

    class FakeTaskInclude:
        def __init__(self, no_log):
            self.action = 'include_tasks'
            self.no_log = no_log
            self._parent = None
            self._role = None
            self._role_name = None
            self._from_files = {}

        def copy(self):
            copy = FakeTaskInclude(self.no_log)
            copy._role = self._role
            copy._role_name = self._role_name
            copy._from_files = self._from_files.copy()
            return copy

       

# Generated at 2022-06-13 08:23:47.693702
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import tempfile
    import shutil

    def get_results(**kwargs):
        # Testing
        import ansible.playbook.play
        from ansible.executor.task_executor import TaskExecutor
        from ansible.executor import ResultCallback
        from ansible.inventory.manager import InventoryManager
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager
        from ansible.plugins.loader import load_callback_plugins
        from ansible.inventory.host import Host
        from ansible.playbook.block import Block
        from ansible.playbook.task import Task

        loader = DataLoader()
        variable_manager = VariableManager()
        variable_manager.extra_vars = dict()

        host = Host(name='hostname')
        host.set

# Generated at 2022-06-13 08:23:57.467684
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    included_file = IncludedFile(filename="", args=[], vars=[], task="")
    hosts = ['host1', 'host2', 'host3']
    for host in hosts:
        included_file.add_host(host)
    assert "host1" in included_file._hosts
    assert "host2" in included_file._hosts
    assert "host3" in included_file._hosts
    # repeat of host1
    try:
        included_file.add_host('host1')
    except ValueError:
        pass
    # repeat of host1
    try:
        included_file.add_host('host1')
    except ValueError:
        pass
    assert "host1" in included_file._hosts
    assert "host2" in included_file._hosts
    assert "host3"

# Generated at 2022-06-13 08:24:09.322068
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    host = 'localhost'

    play_context = PlayContext()
    inv = InventoryManager(["localhost"], vault_password='password')
    vars_manager = VariableManager()

    play = Play()
    task = Task()
    task.vars = play_context.acquire_task_vars(vars_manager, inv, host)
    filename = './test/test_runner/test_runner.py'
    args = dict()
    args['host'] = host

# Generated at 2022-06-13 08:24:23.191608
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass
    # TO DO

# Generated at 2022-06-13 08:24:32.918033
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    vars1 = {'v1': 1, 'v2': 'apple'}
    task1 = TaskInclude(None, 'file1')
    inc_file1 = IncludedFile('file1', 'args1', vars1, task1)

    result = False
    try:
        inc_file1.add_host('host1')
        inc_file1.add_host('host2')
        inc_file1.add_host('host3')
    except ValueError:
        result = True
    assert result is False

    result = False
    try:
        inc_file1.add_host('host1')
    except ValueError:
        result = True
    assert result is True

    vars2 = {'v1': 1, 'v2': 'apple'}

# Generated at 2022-06-13 08:24:41.996972
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task

    results = [IncludedFile.process_include_results(
        [
            {"_host": "1.1.1.1", "ansible_loop_var": "item", "item": "A"},
            {"_host": "2.2.2.2", "ansible_loop_var": "item", "item": "B"},
            {"_host": "1.1.1.1", "ansible_loop_var": "item", "item": "C"},
            {"_host": "2.2.2.2", "ansible_loop_var": "item", "item": "D"},
        ],
        None, None, None)
    ]
    assert(len(results) == 4)
    assert(results[0]._filename == 'A')

# Generated at 2022-06-13 08:24:50.253842
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook.play_context
    import ansible.plugins.loader
    import ansible.template.template
    import ansible.vars.manager
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role.include
    import ansible.playbook.task_include
    import ansible.utils.vars

    pb = ansible.playbook.play.Play()
    pb._hosts = ["host1", "host2"]

    h1 = ansible.playbook.task.Task()
    h1._uuid = "UUID1"
    h1._role = None
    h1._parent = pb
    h1._task = None
    h1.action = 'include'

    h2 = ansible.playbook.task

# Generated at 2022-06-13 08:25:04.433812
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task

    from ansible.playbook.play import Play

    parent = Play()
    task = Task()
    task._parent = parent
    inc_file = IncludedFile('filename', 'args', 'vars', task)

    assert not inc_file.__eq__(None)

    parent = Play()
    task = Task()
    task._parent = parent
    inc_file2 = IncludedFile('filename', 'args', 'vars', task)

    assert inc_file.__eq__(inc_file2)

    parent = Play()
    task = Task()
    task._parent = parent
    inc_file2 = IncludedFile('filename', 'args', 'vars', task)
    inc_file2._filename = 'filename2'


# Generated at 2022-06-13 08:25:19.533241
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import ansible.playbook.task_include
    import ansible.playbook.task_include

    task1 = ansible.playbook.task_include.TaskInclude(None, None, None, None, None)
    task1._parent = task1
    task1._uuid = '1234'
    task1._role = None
    task2 = ansible.playbook.task_include.TaskInclude(None, None, None, None, None)
    task2._parent = task2
    task2._uuid = '1234'
    task2._role = None
    inc1 = IncludedFile('/etc/passwd', 'args', 'vars', task1)
    inc2 = IncludedFile('/etc/passwd', 'args', 'vars', task2)

# Generated at 2022-06-13 08:25:26.248299
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.executor.task_result import TaskResult

    from ansible.playbook.task import Task

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template.safe_eval import safe_eval

# Generated at 2022-06-13 08:25:31.365932
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """ process_include_results(): returns a list of Ansible include files """
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # create a list of TaskResult
    task = TaskResult(host=None, task=None, return_data=None, cache=False, stderr_lines=None,
                                  warnings=None, collapsed=False, failed=False, _ansible_no_log=None, changed=False, skipped=False,
                                  unreachable=False)

    task._task = TaskInclude()
    task._task._parent = PlayContext()

    task._result = dict(include=None)
    task._result['include'] = 'test.yml'



# Generated at 2022-06-13 08:25:43.205737
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    results = [
        TaskResult(host='localhost', task=TaskInclude(), result=dict(changed=False, skipped=False, failed=False, include='./bar.yml')),
        TaskResult(host='localhost', task=TaskInclude(), result=dict(changed=False, skipped=False, failed=False, include='./bar.yml')),
        TaskResult(host='localhost', task=TaskInclude(), result=dict(changed=False, skipped=False, failed=False, include='../bar.yml')),
        TaskResult(host='localhost', task=TaskInclude(), result=dict(changed=False, skipped=False, failed=False, include='debug.yml', include_args=dict(msg='skipped'))),
    ]

# Generated at 2022-06-13 08:25:56.222427
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    play_context = PlayContext()
    play = Playbook.load(dict(
        name="test play",
        hosts=['test_host'],
        gather_facts='no',
        tasks=[]), loader=None, variable_manager=None, play_context=play_context)
    iterator = play.get_iterator()
    iterator._play = play
    loader = None
    variable_manager = None
    results = []
    task = Task()
    task._parent = play
    task._role = play
    task._role_name = "test_role"

# Generated at 2022-06-13 08:26:24.081507
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Checks if __eq__ method of class IncludedFile will return true.
    """
    fake_vars = {}
    fake_args = {}
    fake_task = None
    fake_filename = 'fake_filename'

    actual_result = IncludedFile(fake_filename, fake_args, fake_vars, fake_task) == IncludedFile(fake_filename, fake_args, fake_vars, fake_task)

    assert actual_result



# Generated at 2022-06-13 08:26:37.185502
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    block = Block()
    task = Task()
    task._uuid = "00000000-0000-0000-0000-000000000000"
    task._parent = task

    vars = {}
    args = {}

    task_include = TaskInclude()
    task_include.vars = vars
    task_include.args = args
    task_include._task = task

    inc = IncludedFile("/etc/ansible/test.yml", args, vars, task_include)
    assert(inc._filename == "/etc/ansible/test.yml")
    assert(inc._args == args)
    assert(inc._vars == vars)

# Generated at 2022-06-13 08:26:47.807320
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    play = Play()
    play.name = 'Test play'
    play.hosts = 'all'
    play.tasks = []
    block = Block()
    block.hosts = 'all'
    block.tasks = []
    play.tasks.append(block)
    task = Task()
    block.tasks.append(task)
    task.argument_spec = dict()

# Generated at 2022-06-13 08:26:58.686811
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class MockResults:
        def __init__(self,host,task,result):
            self._host = host
            self._task = task
            self._result = result
            
    class MockPlay:
        pass
    
    class MockHost:
        pass

    class MockTask:
        def __init__(self,action,loop=False,parent=None,role=None,no_log=False):
            self.action = action
            self.loop = loop
            self._parent = parent
            self._role = role
            self.no_log = no_log
            if parent is None:
                self.FROM_ARGS = []

    class MockTaskInclude(MockTask):
        def __init__(self,action,loop=False,parent=None,role=None,no_log=False):
            super

# Generated at 2022-06-13 08:27:08.658456
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    pl = DataLoader()
    pc = PlayContext()


# Generated at 2022-06-13 08:27:20.031689
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import add_all_plugin_dirs

    task_vars = dict(
        omit='__omit_place_holder__',
        foo='bar',
        some_var='baz'
    )
    result = dict(
        changed=False,
        failed=False,
        skipped=False,
        include='some_file.yml',
        include_args=dict(
            something='{{ some_var }}'
        )
    )
    variable_manager = VariableManager()
    variable_manager.extra_vars = task_

# Generated at 2022-06-13 08:27:20.674495
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass

# Generated at 2022-06-13 08:27:32.217308
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import collections

    Collection = collections.namedtuple('Collection', 'results')
    Result = collections.namedtuple('Result', '_task _host _result')
    Task = collections.namedtuple('Task', '_uuid action loop _parent')

    # setup results

# Generated at 2022-06-13 08:27:45.891754
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    results = list()
    results.append(TaskResult(host=None, task=TaskInclude(), return_data={'results': [{'ansible_facts': {'a': 'b'}, 'ansible_no_log': False, 'changed': False, '_ansible_no_log': False, '_ansible_item_label': 'myitem', '_ansible_item_result': True, 'failed': False, 'include': 'myinclude.yml'}]}))

# Generated at 2022-06-13 08:27:56.738655
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    test_file = "%s/../test/include.yml" % os.getcwd()
    test_role_name = "test_role"
    test_role_path = "%s/test_role" % os.getcwd()
    role_task = Task.load(dict(action="include_role", args=dict(name=test_role_name, tasks_from='test_role_file.yml')), None, loader=None, play=None, variable_manager=None)
    role_task._role_path = test_role_path

# Generated at 2022-06-13 08:28:49.453602
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook.task import Task

    loader = DataLoader()
    host_list = [
        {
            "hostname": "okhost",
            "groups": ["ok_group"]
        },
        {
            "hostname": "skiphost",
            "groups": ["skip_group"]
        },
        {
            "hostname": "failhost",
            "groups": ["fail_group"]
        },
        {
            "hostname": "okhost2",
            "groups": ["ok_group2"]
        },
    ]

# Generated at 2022-06-13 08:29:01.124935
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # TODO: write a proper unit test suite.
    def create_include_file(filename, args, vars):
        from ansible.playbook.play_context import PlayContext
        from ansible.playbook.task import Task
        from ansible.playbook.task_include import TaskInclude
        from ansible.playbook.role_include import IncludeRole
        from ansible.template import Templar
        from ansible.vars.manager import VariableManager

        loader = DictDataLoader({})
        variable_manager = VariableManager()
        host = '127.0.0.1'
        play_context = PlayContext(variable_manager=variable_manager)
        iterator = None
        task = TaskInclude() if filename is not None else IncludeRole()
        templar = Templar(loader=loader, variables=vars)
        return

# Generated at 2022-06-13 08:29:08.160776
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ifl1=IncludedFile('/tmp/foo.yml', {'bar':'baz'}, {'foo':'bar'}, None)
    ifl2=IncludedFile('/tmp/foo.yml', {'bar':'baz'}, {'foo':'bar'}, None)
    ifl3=IncludedFile('/tmp/foo.yml', {'bar':'baz'}, {'foo':'bar'}, None)
    ifl4=IncludedFile('/tmp/foo.yml', {'bar':'baz'}, {'foo':'bar'}, None)
    ifl1.add_host('localhost')
    ifl2.add_host('localhost')
    ifl3.add_host('localhost')
    ifl4.add_host('localhost')

# Generated at 2022-06-13 08:29:17.219736
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import find_plugin
    from ansible.plugins.lookup import LookupBase

    from ansible.plugins.loader import lookup_loader, action_loader
    lookup_loader._all_classes['fileglob'] = find_plugin('lookup_plugins', 'fileglob')
    lookup_loader._all_classes['template'] = find_plugin('lookup_plugins', 'template')
    action_loader._all_classes['include_tasks'] = find_plugin('action_plugins', 'include_tasks')
    action_loader._all_classes['import_tasks'] = find_plugin('action_plugins', 'import_tasks')
   

# Generated at 2022-06-13 08:29:31.226070
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    assert IncludedFile("abc", "args", "vars", "task") == IncludedFile("abc", "args", "vars", "task")
    assert not (IncludedFile("abc", "args", "vars", "task") == IncludedFile("abc", "args", "vars", "task2"))
    assert not (IncludedFile("abc", "args", "vars", "task") == IncludedFile("abc", "args", "vars2", "task"))
    assert not (IncludedFile("abc", "args", "vars", "task") == IncludedFile("abc", "args2", "vars", "task"))
    assert not (IncludedFile("abc", "args", "vars", "task") == IncludedFile("abc2", "args", "vars", "task"))

# Generated at 2022-06-13 08:29:39.410758
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:29:48.230619
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    assert IncludedFile('test.yml', None, None, None) == IncludedFile('test.yml', None, None, None)
    assert IncludedFile('test.yml', None, None, None) != IncludedFile('test_2.yml', None, None, None)
    assert IncludedFile('test.yml', None, None, None) != IncludedFile('test.yml', {'a': 1}, None, None)
    assert IncludedFile('test.yml', None, None, None) != IncludedFile('test.yml', None, {'a': 1}, None)
    assert IncludedFile('test.yml', None, None, None) != IncludedFile('test.yml', None, None, 'b')

# Generated at 2022-06-13 08:29:57.922415
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.pip as pip

    loader = None
    variable_manager = None

    # Test an include in a loop

# Generated at 2022-06-13 08:30:09.165449
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''Test IncludedFile.process_include_results staticmethod'''
    import ansible.executor.task_result
    import ansible.executor.task_include
    import ansible.executor.role_result
    import ansible.playbook.role_include
    import ansible.playbook.play_context

    class Result(ansible.executor.task_result.TaskResult):
        def __init__(self, host, task, result, _task=None):
            super(Result, self).__init__(host, task, result)
            self._task = _task or task

    class Host(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 08:30:19.423769
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # IncludeResult
    class IRes:
        def __init__(self, h, t, i, v, k, li, lk, lv, ki, kv):
            self._host = h
            self._task = t
            self.include_args = v
            self.ansible_loop_var = li
            self.ansible_index_var = ki
            self[li] = lv
            self[ki] = kv
            self['_ansible_item_label'] = i
            self['failed'] = False
            self['skipped'] = False
            self['include'] = k

        def get(self, k, v=None):
            try:
                return self[k]
            except KeyError:
                return v

    # TaskInclude