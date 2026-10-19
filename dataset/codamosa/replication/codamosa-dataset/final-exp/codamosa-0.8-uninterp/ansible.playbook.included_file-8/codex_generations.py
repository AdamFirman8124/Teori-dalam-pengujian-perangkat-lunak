

# Generated at 2022-06-13 08:21:16.633778
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task

    results = []

    for i in range(2):
        task = Task()
        task._uuid = 'foo-%d' % i
        task._parent = 'bar'
        task.action = 'include'

        r = TaskResult(host=None, task=task, return_data={'failed': False, 'changed': False, 'skipped': False, 'results': []})

        results.append(r)

    included_files = IncludedFile.process_include_results(results, None, None, None)
    assert(len(included_files) == 2)
    assert(included_files[0] == included_files[1])


if __name__ == "__main__":
    import pytest

# Generated at 2022-06-13 08:21:27.995486
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test the method IncludedFile.__eq__()
    """

    from ansible.playbook import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:21:28.726546
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass

# Generated at 2022-06-13 08:21:36.421900
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    class Fake: pass
    results = [Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake(), Fake()]

    results[0]._host = "localhost"
    results[0]._result = {'include': "/home/me/playbooks/dummy1.yml"}
    results[0]._task = Fake()
    results[0]._task.action = 'include'
    results[0]._task._role_name = 'apache2'
    results[0]._task._from_files = {'role': '/home/me/roles/a/apache2/tasks/main.yml'}
    results[0]._task._parent = None

    results[1]._

# Generated at 2022-06-13 08:21:45.642565
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    assert IncludedFile('/a', {}, {}, None) == IncludedFile('/a', {}, {}, None)
    assert IncludedFile('/a', {'c': 'd'}, {}, None) == IncludedFile('/a', {'c': 'd'}, {}, None)
    assert IncludedFile('/a', {}, {'c': 'd'}, None) == IncludedFile('/a', {}, {'c': 'd'}, None)

    assert IncludedFile('/a', {}, {}, None) != IncludedFile('/b', {}, {}, None)
    assert IncludedFile('/a', {}, {}, None) != IncludedFile('/a', {'c': 'd'}, {}, None)

# Generated at 2022-06-13 08:21:50.954888
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    This test compare two objects of class IncludedFile
    :return: True if the test success
    """
    t = TaskInclude('some task')
    r = IncludedFile('my filename', 'my_args', 'my_vars', t)
    s = IncludedFile('my filename', 'my_args', 'my_vars', t)
    if r==s:
        return True
    else:
        return False

# Generated at 2022-06-13 08:22:01.281228
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib'))

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.output import OutputModule

    if not os.path.exists('/tmp/results'):
        os.mkdir('/tmp/results')

    class TestModule(object):
        def __init__(self, results_dir):
            self.results_dir = results_dir
            self.results = {}

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()

           

# Generated at 2022-06-13 08:22:16.131594
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.included_file import IncludedFile
    import ansible.plugins.loader
    import ansible.parsing.dataloader
    import os

    display = Display()
    loader = ansible.parsing.dataloader.DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = Play

# Generated at 2022-06-13 08:22:26.945312
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    inc1 = IncludedFile("file1", {"x": "y"}, {"x": "y"}, "test_task")
    inc2 = IncludedFile("file2", {"x": "y"}, {"x": "y"}, "test_task")
    inc3 = IncludedFile("file1", {"x": "y"}, {"x": "y", "m": "n"}, "test_task")
    inc4 = IncludedFile("file1", {"x": "y"}, {"x": "y"}, "test_task_2")
    inc5 = IncludedFile("file1", {"x": "y"}, {"x": "y"}, "test_task")

    assert inc1 != inc2
    assert inc1 != inc3
    assert inc1 != inc4
    assert inc1 == inc5

# Generated at 2022-06-13 08:22:36.367785
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import include_tasks_loader, import_role_loader, import_task_loader, import_playbook_loader

    # testcase for include_tasks loader plugin

# Generated at 2022-06-13 08:22:58.633463
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.playbook
    import ansible.play
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.include
    import ansible.playbook.role
    import ansible.playbook.role.include
    import ansible.executor.task_result
    import os

    dummy_src_path = '/path/to/playbook'
    dummy_playbook_name = 'test.yml'

# Generated at 2022-06-13 08:23:10.237233
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:23:20.060740
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import tempfile
    temphere = tempfile.gettempdir()
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    p1 = "test_IncludedFile___eq__:host:host1"
    p2 = "test_IncludedFile___eq__:host:host2"
    f1 = tempfile.NamedTemporaryFile(dir=temphere, delete=False)
    f2 = tempfile.NamedTemporaryFile(dir=temphere, delete=False)

    d1 = {"a":"b"}
    d2 = {"c":"d"}

    loader  = DataLoader()
    inv_mgr = InventoryManager(loader=loader, sources=[p1, p2])


# Generated at 2022-06-13 08:23:31.706100
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test 1: filenames, args and vars are equal, but the task_uuid are different.
    # The __eq__ method returns False.
    test_task_1 = TaskInclude()
    test_task_2 = TaskInclude()
    inc_file_1 = IncludedFile('my_file', {'a': 'a'}, {'b': 'b'}, test_task_1)
    inc_file_2 = IncludedFile('my_file', {'a': 'a'}, {'b': 'b'}, test_task_2)
    print(inc_file_1.__eq__(inc_file_2))

    # Test 2: filenames, args and vars are equal, but the parent uuids are different.
    # The __eq__ method returns False.
    test_play = Play()

# Generated at 2022-06-13 08:23:37.544888
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Check that no errors occurs when process_include_results is called

    # Creating mock object with nessesary methods
    class Mock:
        def __init__(self, play, host, task):
            self._play = play
            self._host = host
            self._task = task
    results = [Mock(1, "localhost", 2), Mock(2, "localhost", 3)]
    IncludedFile.process_include_results(results, None, None, None)

# Generated at 2022-06-13 08:23:46.740865
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:23:49.366513
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'test'
    args = dict()
    vars = dict()
    task = None
    is_role = False
    included_file_1 = IncludedFile(filename, args, vars, task, is_role)
    included_file_2 = IncludedFile(filename, args, vars, task, is_role)
    assert included_file_1 == included_file_2


# Generated at 2022-06-13 08:23:58.371830
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    # results - list of TaskResult objects
    # iterator - PlayIterator
    # loader - DataLoader

    items = [ 'alpha', 'beta', 'gamma', 'delta' ]
    results = []

# Generated at 2022-06-13 08:24:09.902778
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = []
    loader = None
    variable_manager = None
    class FakeIterator:
        def __init__(self, play):
            self._play = play
    class FakeTask:
        pass
    class FakeResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result
    class FakeHost:
        def __init__(self, name):
            self._name = name
        def __eq__(self, other):
            return self._name == other._name
        def __repr__(self):
            return self._name

    play = FakeTask()
    task = FakeTask()
    task._uuid = 'task1'
    task._parent = play
    play._uuid = 'play1'
    fakehost

# Generated at 2022-06-13 08:24:21.638745
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    args = dict(var1='value')
    vars = dict(var1='value')
    filename = dict(var1='value')
    class Task:
        def __init__(self, uuid, parent):
            self._uuid = uuid
            self._parent = parent
    parent = Task('3', None)
    task = Task('2', parent)
    host = dict()

    inc_file1 = IncludedFile(filename, args, vars, task)
    inc_file2 = IncludedFile(filename, args, vars, task)

    assert inc_file1._filename == filename
    assert inc_file1._args == args
    assert inc_file1._vars == vars
    assert inc_file1._filename == filename
    assert inc_file1._task._uuid == task._uuid
    assert inc

# Generated at 2022-06-13 08:25:03.346075
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.inventory import Host, Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.loader import get_all_plugin_loaders

    strategy = StrategyBase(get_all_plugin_loaders())

    results = []
    host = Host('example.com')
    host.set_variable('omit', 'omit_token')
    host_vars = host.get_vars()
    task = strategy.get_task_plugin('include_role')
    task.set_loader(strategy._loader)
    role_name = 'test-role'
    role_path = os.path.join(os.path.dirname(__file__), role_name)
    task

# Generated at 2022-06-13 08:25:18.602916
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible import constants as C
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.plugins import loader as plugin_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    import pytest

    loader = plugin_loader.PluginLoader(
        'ansible.plugins.action',
        'ActionModule',
        C.DEFAULT_ACTION_PLUGIN_PATH
    )
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:25:24.919191
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = []
    class Host:
        pass

    h1 = Host()
    h1.name = 'h1'
    h2 = Host()
    h2.name = 'h2'

    class Play:
        pass

    class Loader:
        def path_dwim_relative(self, basedir, arg1, arg2, is_role=True):
            return "%s/%s/%s" % (basedir, arg1, arg2)

        def path_dwim(self, path):
            return path

    class Task:
        _role_name = None
        _role_path = "role_path"
        _uuid = "uuid"
        def __init__(self, action):
            self.action = action
            self.name = "task_name"
            self._parent

# Generated at 2022-06-13 08:25:30.208435
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # Import here to avoid circular dependency
    from ansible.playbook.play_context import PlayContext

    iterator = unittest.mock.Mock(spec=PlayContext)
    iterator._play = unittest.mock.Mock()
    loader = unittest.mock.Mock()
    variable_manager = unittest.mock.Mock()

    res = unittest.mock.Mock()
    res._host = 'localhost'
    res._task = unittest.mock.Mock()
    res._task.loop = None
    res._task.action = 'include_tasks'
    res._task.no_log = False
    res._task._parent = None
    res._task._role = None
    res._task._uuid = 'uuid_0'
    res._task

# Generated at 2022-06-13 08:25:42.701551
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.vars.clean import cleanup_facts

    # TODO: This should not be the way to instantiate a play, but the
    #       current structure of the play / iterator is not amenable to
    #       refactoring and it will be replaced with a strategy pattern
    #       in Ansible 2.9
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    variable_manager._fact_cache = dict()
    variable_manager._host_cache = dict()
    variable_manager._hostv

# Generated at 2022-06-13 08:25:55.566625
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.block import Block
    from ansible.playbook.helpers import load_list_of_blocks
    from ansible.executor.task_result import TaskResult
    import ansible.constants as C

    test_action = "import_tasks"
    test_file = "myfile.yml"
    test_include_args = {"foo": "bar"}
    test_special_vars = {"_ansible_no_log": "nolog"}

# Generated at 2022-06-13 08:26:06.002700
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Dummy(object):
        pass

    class DummyPlay(object):
        pass

    class DummyTask(object):
        pass

    play = DummyPlay()
    task = DummyTask()
    task.action = 'include'
    task.loop = True
    task.no_log = False
    task.action = 'include'
    task.remove_join_regex = False
    task._parent = None
    task._role = None
    task._role_name = None
    task._from_files = {}
    task._search_path = ['/etc/ansible/roles', '/etc/ansible/playbooks']

    loader = Dummy()
    loader.get_basedir = lambda: '/usr/local/ansible/playbooks'

    class DummyIterator(object):
        play = play



# Generated at 2022-06-13 08:26:16.794607
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook
    import ansible.playbook.play_context
    import ansible.playbook.task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    playbook = ansible.playbook.PlayBook.load("test/test_include_results.yaml", variable_manager=VariableManager(), loader=ansible.cli.CLI.loader)
    play = playbook.get_plays()[0]
    play._variable_manager = VariableManager()
    play._variable_manager.set_inventory(playbook.inventory)
    # play._tqm = ansible.executor.task_queue_manager.TaskQueueManager(inventory=playbook.inventory, variable_manager=play._variable_manager, loader=ansible.cli.CLI.loader)


# Generated at 2022-06-13 08:26:24.599931
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    process_include_results only uses the filename to distinguish a file
    it does not look at the variables, the content of the file, or the hosts
    this is a problem because included variables are not respected if the
    same file is included multiple times with different variables
    """

    included_files = []

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()
    fake_variable_manager = VariableManager()

    class FakeResults:
        def __init__(self, host, task):
            self._host = host
            self._task = task
            self._result = dict(include='test.yml')

    class FakeIterator:
        def __init__(self, play):
            self._play = play


# Generated at 2022-06-13 08:26:37.429503
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'omit': 'foo'}
    play_context = PlayContext(variable_manager=variable_manager)
    play = Play().load({}, variable_manager=variable_manager, loader=None)


# Generated at 2022-06-13 08:27:19.826791
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' Test the process_include_results method of the IncludedFile class '''
    pass


# Generated at 2022-06-13 08:27:27.109607
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Host:
        name = 'localhost'

    class Play:
        pass

    class PlayBook:
        pass

    class Task:
        action = 'include'
        no_log = False
        loop = False
        _uuid = '12345'
        _parent = Play()
        _parent._uuid = '67890'

        def get_search_path(self):
            return []

    class Result:
        _host = Host()
        _task = Task()
        _result = {'include': '/tmp/foo.yaml', 'include_args': dict()}

    variable_manager = None
    loader = None
    iterator = PlayBook()
    results = [Result]
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)

# Generated at 2022-06-13 08:27:36.051962
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # test_results var is used to emulate the results variable from the Ansible callback.
    test_results = [
        'ok',
        'ok',
        'ok',
        'ok',
        'ok',
        'ok',
        'ok',
        'ok',
        'ok'
    ]

# Generated at 2022-06-13 08:27:50.098549
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ansible_search_path': 'my_basedir'}

    class TestResult(object):
        def __init__(self, host, task, result, include_args={}):
            self._host   = host
            self._task   = task
            self._result = result


    class TestTask(object):
        def __init__(self, action, loop, parent, role, from_files):
            self.action       = action
            self.loop         = loop
            self.no_log       = True
            self._parent      = parent
            self._role        = role
            self._from_files  = from_files

        def get_search_path(self):
            return self._from

# Generated at 2022-06-13 08:28:04.963455
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Without loop results
    results = [{"_host": "localhost", "_task": "1", "results":[{"failed":"True"}]}]
    assert IncludedFile.process_include_results(results,"","","") == []

    # With loop results
    results = [{"_host": "localhost", "_task": "1", "results":[[{"failed":"True"}]]}]
    assert IncludedFile.process_include_results(results,"","","") == []

    # With good results
    results = [{"_host": "localhost", "_task": "1",
                "results":[{"skipped":False, "failed": False,"include": "tests/test_include_role.yml",
                           "include_args": {"name": "blabla","_ansible_item_label": "test"}}]}]
    assert IncludedFile.process_include_

# Generated at 2022-06-13 08:28:13.184754
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    from ansible.plugins.loader import discover_plugins
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.executor.task_executor import TaskExecutor

    class Iterator(object):
        def __init__(self, play):
            self._play = play


# Generated at 2022-06-13 08:28:26.233847
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    import unittest
    import tempfile
    import shutil
    import os
    import re
    from ansible.utils.display import Display
    from ansible.utils.hashing import checksum_s
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole

    display = Display()


# Generated at 2022-06-13 08:28:37.022074
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult

    results = []
    results.append(TaskResult('testhost1', {}, {'include_args': {}, 'include': 'test_include'}))
    results.append(TaskResult('testhost2', {}, {'include_args': {}, 'include': 'test_include'}))
    results.append(TaskResult('testhost3', {}, {'include_args': {}, 'include': 'test_include_2'}))
    results.append(TaskResult('testhost4', {}, {'include_args': {'loop_var': 'item'}, 'include': 'test_include_3_with_loop', 'item': 'testhost4'}))

# Generated at 2022-06-13 08:28:44.310732
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    display.deprecated('"include" is deprecated, use include_tasks/import_tasks/import_playbook instead', "2.16")

    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.playbook_executor import playbook_executor
    from ansible.inventory.manager import InventoryManager

    from ansible.vars.manager import VariableManager
    from ansible.vars import hostvars


# Generated at 2022-06-13 08:28:50.503701
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from test.support.fixtures import TempDir

    # This test is a direct copy of test_include_tasks_all_hosts in test/units/plugins/strategy/test_linear.py
    # except it has been modified to use the process_include_results method from this module

    # TODO: refactor the test to use mocks, allowing us to also test all the other IncludeFile methods

    # we do not want any plugins loaded for this test as we don't need to deal with vars plugins
    # this is normally done by the base class AnsiblePluginTest

# Generated at 2022-06-13 08:30:22.870849
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import yaml
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor import playbook_executor
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:30:35.837031
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import pytest
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    # data used by the test
    #  - results : array of task results
    #
    #  - expected_included_files : array of included files Expected value
    #
    #  - task_args : array of task_args Expected value
    #
    #  - vars : used for variable manager initialization
    #
    #  - loader: used for variable manager initialization
    #
    #  - include_args : array of include_args Expected value