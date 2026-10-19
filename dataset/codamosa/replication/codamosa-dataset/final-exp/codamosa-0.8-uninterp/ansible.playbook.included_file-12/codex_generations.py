

# Generated at 2022-06-13 08:21:05.979841
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import include_tasks_loader, import_role_loader


# Generated at 2022-06-13 08:21:15.740989
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.vars import VariableManager
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from io import StringIO
    '''
    Tests the process_include_results method of class IncludedFile.
    '''

    # This test is incomplete as it only tests the first 'if' block.
    # It tests if results are processed when first 'if' block is True.
    loader = DataLoader()


# Generated at 2022-06-13 08:21:23.306521
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from collections import namedtuple
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:21:33.416872
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import load_reserved_vars

    class FakePlay:
        class FakeOptions:
            def __init__(self):
                self.roles_path = []
        def __init__(self):
            self.options = self.FakeOptions()

    class FakeIterator:
        def __init__(self):
            self._play = FakePlay()

    class FakeHost:
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 08:21:43.748336
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import copy
    from ansible.playbook.play_context import PlayContext

    class TestIncludedFile_process_include_results(unittest.TestCase):
        ''' test class for the method process_include_results of class IncludedFile '''

        def setUp(self):
            context = PlayContext(remote_user='root', remote_addr=None, become=False, become_method=None, become_user=None, become_pass=None, serial=0)
            variable_manager = VariableManager()
            loader = DataLoader()
            variable_manager.extra_vars = {}
            variable_manager.options_vars = {}
            variable_manager.hostvars = {}

# Generated at 2022-06-13 08:21:53.301192
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class IncludeResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result
    class Task:
        def __init__(self, action, loop, no_log, parent, _uuid):
            self.action = action
            self.loop = loop
            self.no_log = no_log
            self._parent = parent
            self._uuid = _uuid
    class Play:
        def __init__(self, play):
            self._play = play
    class VariableManager:
        def __init__(self, get_vars):
            self.get_vars = get_vars
        def get_vars(self, play, host, task):
            return self.get_vars(play, host, task)

# Generated at 2022-06-13 08:22:02.743515
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager

    results = list()
    include_result = dict()
    include_result['ansible_loop_var'] = '_loop_var'
    include_result['ansible_index_var'] = '_index_var'
    include_result['_ansible_item_label'] = '__ansible_item_label'
    include_result['ansible_loop'] = '_ansible_loop'
    include_result['include_args'] = dict()
    include_result['include_args']['_raw_params'] = '_raw_params'
    include_result['include_args']['role'] = 'role'
    include_result['include_args']['name'] = 'name'

# Generated at 2022-06-13 08:22:16.753495
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    Basic test of the included_file.process_include_results method.
    '''
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

    # create an instance of IncludedFile
    IncludedFile_instance = IncludedFile('/tmp/file.yml', [], {}, Task())

    ###
    ### Happy path
    ###

    # create a list of tasks and results
    task1 = Task()
    task1._action = 'include'
    task1._parent = Task()
    task1._parent._action = 'include'
    task1._parent._parent = Task()
    result1 = TaskResult('localhost', 'include', {'include': 'file1.yml'}, 'ok')

    task2 = Task()

# Generated at 2022-06-13 08:22:32.093480
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import include_tasks_loader

    inventory = InventoryManager(loader=DataLoader())
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)


# Generated at 2022-06-13 08:22:39.787584
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    import ansible.constants as C

    from ansible.module_utils.common._collections_compat import Mapping

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:23:02.021816
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''Tests process_include_results method of class IncludedFile
    '''
    import sys
    sys.path.append('/home/git/playbooks/library')
    import ansible.runner.action_plugins.include_role_tasks as include_role_tasks
    import ansible.runner.action_plugins.include_tasks as include_tasks
    import ansible.runner.action_plugins.include as include

    from ansible.utils.display import Display
    display = Display()

    from ansible.plugins import loader
    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.playbook.play
    import ansible.playbook.play_context

    # we need mock object for Host and Task in the results
    results = []
    mock_host = MagicMock()


# Generated at 2022-06-13 08:23:08.786809
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.module_utils.facts.system.distribution as distribution
    import unittest
    import tempfile
    import shutil
    import sys
    import os.path
    from ansible.module_utils.six import PY2

    class TestIncludedFile(unittest.TestCase):

        def setUp(self):
            if PY2:
                import __builtin__ as builtins
            else:
                import builtins
            self.builtins_open = builtins.open
            self.tmpdir = tempfile.mkdtemp()

            # mock open() so we don't have to create real files
            def open_mock(filename, *args, **kwargs):
                basename = os.path.basename(filename)

# Generated at 2022-06-13 08:23:14.065125
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class Host(object):
        def __init__(self, name):
            self.name = name
            self._uuid = name

        def get_name(self):
            return self.name

    class Task(object):
        def __init__(self, action):
            self.action = action
            self._uuid = 'task'

        def __eq__(self, other):
            return self.action == other.action

    class Playbook(object):
        def __init__(self, host_list_file, play):
            self.host_list

# Generated at 2022-06-13 08:23:16.603300
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    assert IncludedFile.process_include_results([], [], [], []) == []
    assert "a" in "ab"
    assert "a" not in "bc"

# Generated at 2022-06-13 08:23:24.996147
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task

    i1 = IncludedFile('inc_file', 'arg1', 'vars1', Task())
    i2 = IncludedFile('inc_file', 'arg1', 'vars1', Task())
    i3 = IncludedFile('inc_file', 'arg1', 'vars1', Task())
    i4 = IncludedFile('inc_file2', 'arg1', 'vars1', Task())

    assert i1 == i2
    assert i1 != i3
    assert i1 != i4



# Generated at 2022-06-13 08:23:36.528351
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.task import TaskLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    class MockHost(object):
        def __init__(self, host_name):
            self.host_name = host_name
            self._variable_manager = VariableManager()
            self._variable_manager.extra_vars = {}

        def get_variable_manager(self):
            return self._variable_manager

    class MockIterator(object):
        def __init__(self, loader, playbook, play_context, variable_manager):
            self._loader = loader
            self._playbook = playbook
            self._play

# Generated at 2022-06-13 08:23:45.994983
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import pprint
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager.set_inventory(inventory)

    import ansible.playbook.play


# Generated at 2022-06-13 08:23:56.295428
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    from ansible.executor.task_queue_manager import TaskQueueManager

    import pytest
    import os

    def results_with_items(task, res_task_name, num_items):
        # Create a result with items
        res = TaskResult(host=task.host, task=task)
        res._task = task
        # Set variable ansible_loop_var
        res._result['ansible_loop_var'] = 'item'
        # Create a list of items
        res._result['results'] = []
        for i in range(num_items):
            res_item = {}
            # Set the item
            res_item['item'] = {'key': 'value'}
            # Set the include key
            res_item['include'] = res_task_

# Generated at 2022-06-13 08:24:08.536963
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import pytest
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

# Generated at 2022-06-13 08:24:15.528118
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.facts.system.distribution import Distribution

    distro_cls = Distribution()

    results = []

    hosts = ['localhost', '127.0.0.1']
    for host in hosts:
        for i in range(0, 2):
            res = TaskResult(host=host, task=None, return_data=None, result=None)
            res._result = dict(
                include_args=dict(),
                include='files/hello.yml',
                ansible_loop_var='item',
                skipped=False,
                failed=False,
                ansible_item_label=i,
            )
            results.append(res)


# Generated at 2022-06-13 08:24:47.870777
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # we need a mocked task object with a parent so we can test relative paths
    class MockedTask:
        def __init__(self, action='include_tasks', relative_path='', name=None):
            self.action = action
            self.loop = None
            self.args = {'_raw_params': relative_path}
            self._parent = None
            self._role = None
            self._from_files = {}

        def get_search_path(self):
            return []

        def copy(self):
            return MockedTask(action=self.action, relative_path=self.args.get('_raw_params'), name=self.name)

    def mock_isabspath(path):
        return not path.startswith('.')


# Generated at 2022-06-13 08:25:02.703458
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    old_IncludedFile = IncludedFile("filename", "args", "vars", "task")
    new_IncludedFile = IncludedFile("filename", "args", "vars", "task")
    assert(old_IncludedFile == new_IncludedFile)

    old_IncludedFile = IncludedFile("filename", "args", "vars", "task")
    new_IncludedFile = IncludedFile("filename2", "args", "vars", "task")
    assert(old_IncludedFile != new_IncludedFile)

    old_IncludedFile = IncludedFile("filename", "args", "vars", "task")
    new_IncludedFile = IncludedFile("filename", "args2", "vars", "task")
    assert(old_IncludedFile != new_IncludedFile)


# Generated at 2022-06-13 08:25:18.313484
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=[])

# Generated at 2022-06-13 08:25:24.575764
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import unittest

    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_result import TaskResult

    class TestIncludedFile(unittest.TestCase):
        def setUp(self):
            self.loader = ansible.parsing.dataloader.DataLoader()
            self.inventory = InventoryManager(self.loader, 'localhost,')

# Generated at 2022-06-13 08:25:39.669439
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # pylint: disable=protected-access
    class FakeVars(object):
        def get_vars(self, *args, **kwargs):
            return {'_test': kwargs['task']}

    class FakeRole(object):
        def __init__(self, role_path, role_name=None):
            self._role_path = role_path
            self._role_name = role_name

        def get_name(self):
            return self._role_name

    class FakePlay(object):
        def __init__(self, basedir, name=None):
            self._basedir = basedir
            self._name = name

        def get_name(self):
            return self._name

        def get_basedir(self):
            return self._basedir


# Generated at 2022-06-13 08:25:51.746502
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.role_include import IncludeRole
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


    #
    # Some constants for this test
    #
    class Mock_Iterator():
        def __init__(self, play=None):
            self._play = play

    class Mock_Play():

        def __init__(self, name=None):
            self.name = name


    class Mock_Task():
        def __init__(self, _uuid=None, no_log=None, action=None):
            self._uuid = _uuid

# Generated at 2022-06-13 08:25:52.482649
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass

# Generated at 2022-06-13 08:26:04.050789
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import copy
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    play_context = PlayContext()
    play_context.prompt = 'test playbook'
    play_context.vault_password = 'ASDFASDF'
    play_context.remote_addr = '10.10.10.10'
    play_context.connection = 'local'
    play_context.network_os = 'ios'
    play_context.remote_user = 'root'
    play_context.become = True
    play_context.become_method = 'sudo'
    play_context.become_user = 'root'
    play_context.check_mode = True
    task = Task()
    task._uuid = 'task_1'

# Generated at 2022-06-13 08:26:14.318300
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = '/path/to/include/file'
    args = dict()
    vars = dict()
    task = dict()
    # Test if two IncludedFiles are equal
    if1 = IncludedFile(filename, args, vars, task)
    if2 = IncludedFile(filename, args, vars, task)
    assert (if1.__eq__(if2))

    # Test if two IncludedFiles with different filename are not equal
    if1 = IncludedFile(filename, args, vars, task)
    if2 = IncludedFile('/path/to/other/include/file', args, vars, task)
    assert (not if1.__eq__(if2))

    # Test if two IncludedFiles with different args are not equal
    args1 = dict(a=1)
    args2 = dict(b=2)
   

# Generated at 2022-06-13 08:26:22.961224
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' test IncludedFile.process_include_results with a simple loop '''

    class MockIterator:
        def __init__(self):
            self._play = 1

    class MockLoader:
        def __init__(self):
            self._basedir = 'fake_basedir'

        def get_basedir(self):
            return self._basedir

        def path_dwim_relative(self, a, b, c, is_role=False):
            return 'fake_path_dwim_relative(%s, %s, %s)' % (a, b, c)

    class MockVariableManager:
        def __init__(self):
            self._variable_manager = 1

        def get_vars(self, play, host, task):
            return dict(ansible_search_path=[])


# Generated at 2022-06-13 08:27:09.577132
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    task_1 = TaskResult('host1', 'task_1')
    task_1._task = 'task_1'
    task_1._host = Host('host1')
    task_1._result = {'include': 'included_play_1.yml'}

    task_2 = TaskResult('host2', 'task_2')
    task_2._task = 'task_2'
    task_2._host = Host('host2')


# Generated at 2022-06-13 08:27:15.314088
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    inc1 = IncludedFile('/a/b/c', {'a': '1'}, {'d': '2'}, None)
    inc2 = IncludedFile('/a/b/c', {'a': '1'}, {'d': '2'}, None)

    assert inc1 == inc2
    assert inc1 == inc1



# Generated at 2022-06-13 08:27:24.194166
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class FakeResult:

        def __init__(self, result, host, task):
            self._result = result
            self._host = host
            self._task = task


# Generated at 2022-06-13 08:27:34.354389
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.executor import task_result
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    # Create a play

# Generated at 2022-06-13 08:27:47.738823
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import filter_loader
    from ansible.plugins.loader import test_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # init plugin loaders with empty fake data
    module_loader.add_directory('')
    action_loader.add_directory('')
    lookup_loader.add_directory('')

# Generated at 2022-06-13 08:27:58.250928
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    m_task = mock.Mock()
    m_task.action = 'include'
    m_task.loop = False
    m_task.register = None

    m_host = mock.Mock(get_name=lambda: 'localhost')
    m_result = mock.Mock()
    m_result._host = m_host
    m_result._task = m_task
    m_result.is_failed = lambda: False
    m_result._result = {'include': './include1.yml'}
    res1 = [m_result]

    m_task2 = mock.Mock()
    m_task2.action = 'include'
    m_task2.loop = False
    m_task2.register = None

    m_result2 = mock.Mock()
    m_result2._

# Generated at 2022-06-13 08:28:01.145161
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Prepare some fake values for the test
    results = []
    iterator = None
    loader = None
    variable_manager = None

    # Test the method
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)

    # Test assert
    assert isinstance(included_files, list)

# Generated at 2022-06-13 08:28:12.125104
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    #import ansible.module_utils.basic
    #import ansible.module_utils.urls
    #import ansible.module_utils.common.text
    #import ansible.module_utils.facts.virtual
    #import ansible.module_utils.facts.system
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.plugins import module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create a dict with task results to process

# Generated at 2022-06-13 08:28:25.882717
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import pytest

    from ansible import errors

    from ansible_collections.testns.testcoll.plugins.module_utils._text import to_bytes

    class FakeLoader(object):
        def __init__(self, basedir):
            self._basedir = basedir

        def get_basedir(self):
            return self._basedir

        def get_real_file(self, path):
            return path


# Generated at 2022-06-13 08:28:36.895680
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import mock

    class TestIterator(object):
        _play = 'play.yml'

    class TestPlay(object):
        pass

    class TestHost(object):
        pass

    class TestTask(object):
        _uuid = 'task_uuid'
        _parent = TestPlay()

        @classmethod
        def get_search_path(cls):
            return ['basedir']

    class TestResult(object):
        def __init__(self):
            self._task = TestTask()
            self._host = TestHost()

# Generated at 2022-06-13 08:30:20.156373
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    include_results = [{'include': 'include_vars', 'include_args': {'a': 1}, 'ansible_search_path': 'search_path'},
                       {'include': 'include_vars', 'include_args': {'a': 2}, 'ansible_search_path': 'search_path'},
                       {'include': 'import_playbook', 'include_args': {'a': 3}, 'ansible_search_path': 'search_path'}]
    iterator = None
    loader = None
    variable_manager = None
    included_files = IncludedFile.process_include_results(include_results, iterator, loader, variable_manager)
    assert len(included_files) == 3
    assert included_files[0]._filename == included_files[1]._filename

# Generated at 2022-06-13 08:30:25.932301
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # declare classes and variables
    host1 = class_Host()
    host1._name = "host1"

    host2 = class_Host()
    host2._name = "host2"

    host3 = class_Host()
    host3._name = "host3"

    task1 = class_Task()
    task1._uuid = "u1"
    task1._action = "include_tasks"

    task2 = class_Task()
    task2._uuid = "u2"
    task2._action = "include_tasks"
    task2._parent = task1

    task3 = class_Task()
    task3._uuid = "u3"
    task3._action = "include_tasks"
    task3._parent = task1

    task4 = class_Task()
    task4

# Generated at 2022-06-13 08:30:40.593470
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import sys
    from io import open
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    def setup_loader():
        loader = DataLoader()
        path = os.path.dirname(__file__)
        loader.set_basedir(path)
        return loader

    def setup_variable_manager():
        variable_manager = VariableManager()
        return variable_manager

    def setup_inventory(variable_manager = None):
        inventory = InventoryManager(loader=setup_loader(), variable_manager=variable_manager)
        inventory