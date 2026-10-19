

# Generated at 2022-06-13 08:21:12.231079
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    obj = IncludedFile(None, None, None, None)

    included_files = obj.process_include_results([(None, [{'include': 'tasks/main.yml'}])])
    assert included_files[0]._filename == 'tasks/main.yml'

    included_files = obj.process_include_results([(None, [{'include': 'tasks/main.yml', 'with_items': [1, 2, 3]}]), (None, [{'include': 'tasks/main.yml', 'with_items': [4, 5, 6]}])])
    assert len(included_files) == 6
    assert included_files[0]._filename == 'tasks/main.yml'
    assert included_files[0]._args == {'item': 1}

    included_

# Generated at 2022-06-13 08:21:14.743453
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    assert IncludedFile(filename='/etc', args=dict(), vars=dict(), task=None) == IncludedFile(filename='/etc', args=dict(), vars=dict(), task=None)


# Generated at 2022-06-13 08:21:26.368867
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    class Play_object(object):
        def __init__(self, playbook, play_context, loader, variable_manager, host_list, module_handler):
            self._playbook = playbook
            self._play_context = play_context
            self._loader = loader
            self._variable_manager = variable_manager
            self._host_list = host_list
            self._module_handler = module

# Generated at 2022-06-13 08:21:34.456848
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' test process_include_results() by calling the method with dummy parameters '''
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Init parameters for Unit test
    results = []
    iterator = None
    loader = None
    variable_manager = None

    result1 = TaskQueueManager._Fact()
    result1._host = 'host1'
    result1._task = Task()
    result1._task._parent = Block()
    result1._task._action = 'include_tasks'

# Generated at 2022-06-13 08:21:44.267743
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import mock

    class FakeVariableManager:
        def get_vars(self, play, host, task):
            return {}

    loader = mock.MagicMock()
    loader.get_basedir.return_value = "tested/dir"

    iterator = mock.MagicMock()
    iterator._play = "playbook"

    class FakeTask:
        action = "include_tasks"
        def __init__(self, no_log):
            self.no_log = no_log
            self.loop = None
        def copy(self):
            return self
        def get_search_path(self):
            return ["search/path"]

    class FakeResult:
        _result = None
        _host = None
        _task = None

    results = [
        FakeResult(),
        FakeResult(),
    ]

   

# Generated at 2022-06-13 08:21:50.282874
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.plugins import callback_loader


# Generated at 2022-06-13 08:22:00.719617
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    def assert_counts(results, files, hosts, tasks):
        inc_files = IncludedFile.process_include_results(results, None, None, None)
        assert len(inc_files) == files
        for f in inc_files:
            assert len(f._hosts) == hosts
            assert len(f._task._include_tasks) == tasks

    # result without include is skipped
    result = type("Result", (object,), {"_result": {"skipped": True}, "_task": {"action": "include"}, "_host": {}})()
    assert_counts([result], 0, 0, 0)

    # result without include fails
    result = type("Result", (object,), {"_result": {"failed": True}, "_task": {"action": "include"}, "_host": {}})()

# Generated at 2022-06-13 08:22:15.597930
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.utils.unsafe_proxy import wrap_var

    # Create the inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create hosts

# Generated at 2022-06-13 08:22:27.045690
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

# Generated at 2022-06-13 08:22:32.404408
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Fake:
        def __init__(self):
            self._uuid = 'fake uuid'
            self._parent = Fake()

    class Fake1:
        def __init__(self):
            self._uuid = 'fake1 uuid'
            self._parent = Fake1()

    class Fake2:
        def __init__(self):
            self._uuid = 'fake2 uuid'
            self._parent = Fake2()

    fake = Fake()
    fake1 = Fake1()
    fake2 = Fake2()
    included_file = IncludedFile('file name', {'arg'}, {'var'}, fake)
    included_file1 = IncludedFile('file name', {'arg'}, {'var'}, fake1)

# Generated at 2022-06-13 08:22:53.731768
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import sys
    import io

    temp_stdout = sys.stdout
    sys.stdout = io.StringIO()

# Generated at 2022-06-13 08:22:59.398195
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()
    from ansible.playbook.play import Play
    from ansible.playbook.attribute import Attribute
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.base import Base
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    class Options():
        module_path = None


# Generated at 2022-06-13 08:23:07.496819
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    Process include results
    '''
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import _load_params
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Create TaskResult, Task, Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    task_vars = variable_manager.get_vars()
    task_vars['omit'] = ["other"]

    orig_

# Generated at 2022-06-13 08:23:17.949226
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from units.mock.loader import DictDataLoader
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Result:
        def __init__(self, host, task):
            self._host = host
            self._task = task
            self._result = dict(changed=False, failed=False, skipped=False, ansible_loop_var='item', ansible_index_var='index', _ansible_item_label='item')

    class Task:
        def __init__(self, action):
            self.action = action
            self._search_paths = ['roles/role1', 'roles/role2']
            self._parent = None
            self._role = None
            self._role_name = None

# Generated at 2022-06-13 08:23:19.484845
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    pass

# Generated at 2022-06-13 08:23:31.022736
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import jinja2
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    from ansible.plugins.callback import CallbackBase
    from collections import namedt

# Generated at 2022-06-13 08:23:41.568925
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # Test data
    # Note: search_paths are not used in this test

# Generated at 2022-06-13 08:23:47.480654
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import os
    import sys

    if sys.version_info < (3, 0):
        from mock import MagicMock, mock_open, patch
    else:
        from unittest.mock import MagicMock, mock_open, patch

    # Mock the iterator and loader classes
    class _mockTaskResult:
        _host = None
        _task = None
        _result = None
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class _mockTaskInclude:
        _uuid = None
        _parent = None
        action = 'include'
        loop = False
        no_log = False
        _role = None
        def __init__(self, uuid, parent, role):
            self._uu

# Generated at 2022-06-13 08:23:57.371234
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    ansible.playbook.include.IncludedFile._process_include_results()
    :return:
    """
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext

    results=[]
    dataloader= DataLoader()
    variable_manager = VariableManager()
    host_list=["192.168.11.181"]
    loader=dataloader
    options=PlayContext()
    inventory=variable_manager.get_inventory()
    pb=Playbook()

# Generated at 2022-06-13 08:24:09.250802
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    included_files = IncludedFile.process_include_results([], [], [], [])
    assert included_files == []

    included_files = IncludedFile.process_include_results([
        {'_host': '127.0.0.1', '_task': 'task', '_result': {'include_results': []}}
    ], [], [], [])
    assert included_files == []



# Generated at 2022-06-13 08:24:41.702250
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    include_result_1 = TaskResult(host=dict(name='localhost'), task=Task(), result=dict(
        include='/foo/bar', include_args=dict(name='foobar', bar='foo')
    ))
    include_result_2 = TaskResult(host=dict(name='localhost'), task=Task(), result=dict(
        include='/foo/bar', include_args=dict(foo='bar')
    ))
    include_result_3 = TaskResult(host=dict(name='localhost'), task=Task(), result=dict(
        include='/bar/bar', include_args=dict(foo='bar')
    ))

# Generated at 2022-06-13 08:24:49.999089
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.task import Task

    filename = 'test.yml'
    args = dict(a=1)
    vars = dict(b=2)
    role_path = './test'
    task = Task()
    is_role = True

    included_file = IncludedFile(filename, args, vars, task)
    included_file_copy = IncludedFile(filename, args, vars, task)

    assert included_file == included_file_copy, 'IncludedFile objects must be equal'

    included_file_no_args = IncludedFile(filename, None, vars, task)
    included_file_no_vars = IncludedFile(filename, args, None, task)

    assert included_file != included_file_no_args, 'IncludedFile objects must be distinct if args is different'
   

# Generated at 2022-06-13 08:25:01.550329
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.playbook.play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.executor.task_result import TaskResult
    play = ansible.playbook.play.Play()
    play._included_files = []
    play._handler_blocks = []
    play._role_handlers = {}
    task1 = TaskInclude()
    task1._uuid = 'uuid1'
    task1._role = None
    task1._parent = play
    task1.action = 'include'
    task1.args = {'_raw_params':'test_include.yml'}
    task2 = TaskInclude()
    task2._uuid = 'uuid2'
    task2._role = None
    task

# Generated at 2022-06-13 08:25:11.486597
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__(): # noqa

    import re

    task_include = TaskInclude()
    task_include.init(dict(static=1))

    assert IncludedFile('file', dict(), dict(), task_include) == IncludedFile('file', dict(), dict(), task_include)
    assert IncludedFile('file', dict(), dict(a=1), task_include) == IncludedFile('file', dict(), dict(a=1), task_include)
    assert IncludedFile('file', dict(a=1), dict(), task_include) == IncludedFile('file', dict(a=1), dict(), task_include)
    assert IncludedFile('file', dict(a=1), dict(b=2), task_include) == IncludedFile('file', dict(a=1), dict(b=2), task_include)


# Generated at 2022-06-13 08:25:19.579349
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test case 01
    # Check whether the comparison works when:
    # - filename, args, vars and uuid_task are equal (chained)
    # - but the uuid of the parent tasks are different
    filename01 = 'test01'
    args01 = 'test01'
    vars01 = 'test01'
    task01 = 'test01'
    is_role01 = 'test01'
    included_file01 = IncludedFile(filename01, args01, vars01, task01, is_role01)

    filename02 = 'test01'
    args02 = 'test01'
    vars02 = 'test01'
    task02 = 'test01'
    is_role02 = 'test01'

# Generated at 2022-06-13 08:25:32.651422
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class _IncludeRole:
        def __init__(self, role_name):
            self._role_name = role_name

    class _Result(object):
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class _Task(object):
        def __init__(self, uuid, parent, action, loop, role):
            self._uuid = uuid
            self._parent = parent
            self._action = action
            self._loop = loop
            self._role = role

        @property
        def action(self):
            return self._action

        @property
        def loop(self):
            return self._loop

        @property
        def no_log(self):
            return False


# Generated at 2022-06-13 08:25:44.010860
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import ansible.constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Playbook with two roles: included_role and role1

# Generated at 2022-06-13 08:25:56.819862
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    results = []
    hosts = ['testhost']

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/unit/inventory'])
    inventory.subset('testhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:26:06.973127
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = None
    variable_manager = VariableManager(loader=loader)
    #variable_manager.extra_vars = runner_vars
    variable_manager.set_inventory(loader.inventory)

    play_context = PlayContext()


# Generated at 2022-06-13 08:26:17.746919
# Unit test for method __eq__ of class IncludedFile

# Generated at 2022-06-13 08:27:19.828611
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.meta import RoleMetadata

    TestPlay = namedtuple('TestPlay', ['_role_paths'])

    FakeTask = namedtuple('FakeTask', ['action', '_role', '_role_name', '_parent', 'args', 'FROM_ARGS', 'loop', 'get_search_path', 'no_log', '_uuid'])
    FakeRole = namedtuple('FakeRole', ['_role_path'])
    FakeLoader = namedtuple('FakeLoader', ['get_basedir'])
    FakeResult = namedtuple('FakeResult', ['_host', '_task', '_result'])
    FakeVariableManager = namedtuple

# Generated at 2022-06-13 08:27:26.039433
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    assert IncludedFile(None, None, None, None).__eq__(IncludedFile(None, None, None, None))

    assert not IncludedFile(None, None, None, None).__eq__(IncludedFile(None, None, None, None, is_role=True))

    assert not IncludedFile(None, None, None, None).__eq__(None)


# Generated at 2022-06-13 08:27:31.533680
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.utils.color import stringc
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.plugins.callback import CallbackBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleUndefinedVariable

    if C.color.strip() == 'false':
        stringc = (lambda s, color: s)


# Generated at 2022-06-13 08:27:45.298874
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a1 = TaskInclude.load(dict(include='test'),Loader())
    a2 = TaskInclude.load(dict(include='test'),Loader())
    b1 = TaskInclude.load(dict(include='test2'),Loader())
    b2 = TaskInclude.load(dict(include='test2'),Loader())

    i1 = IncludedFile('test', {}, {}, a1)
    i2 = IncludedFile('test', {}, {}, a2)
    i3 = IncludedFile('test2', {}, {}, a1)
    i4 = IncludedFile('test2', {}, {}, a2)
    i5 = IncludedFile('test', {}, {}, b1)
    i6 = IncludedFile('test', {}, {}, b2)
    i7 = IncludedFile('test2', {}, {}, b1)

# Generated at 2022-06-13 08:27:54.870038
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Dummy:
        def __init__(self, uuid):
            self._uuid = uuid

    included_file = IncludedFile('file.yml', {}, {}, Dummy('abcdef'))
    included_file.add_host('localhost')
    assert included_file == IncludedFile('file.yml', {}, {}, Dummy('abcdef'))
    assert included_file != IncludedFile('file.yml', {'a': 'b'}, {}, Dummy('abcdef'))
    assert included_file == IncludedFile('file.yml', {'a': 'b'}, {}, Dummy('abcdef'))
    assert included_file != IncludedFile('file.yml', {}, {'a': 'b'}, Dummy('abcdef'))

# Generated at 2022-06-13 08:28:03.000895
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader

    hosts = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=[])

# Generated at 2022-06-13 08:28:09.477144
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' Test IncludedFile.process_include_results()'''
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class Host(object):
        def __init__(self, name):
            self.name = name
            self._vars = dict()

        def set_variable(self, varname, value):
            self._vars[varname] = value


# Generated at 2022-06-13 08:28:17.293109
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile(filename="/home/username/my/ansible/playbook.yml",
                     args=dict(hello="world"),
                     vars=dict(),
                     task=object())
    b = IncludedFile(filename="/home/username/my/ansible/playbook.yml",
                     args=dict(hello="world"),
                     vars=dict(),
                     task=object())
    assert a == b

# Generated at 2022-06-13 08:28:30.149095
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins import module_loader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["/tmp/hosts"])
    module_loader.add_directory('/tmp/library')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:28:42.464364
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins import action
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    import json
    loader = DataLoader()
    results = []
    results.append(TaskResult(host=loader.load_from_file('/home/mohamed/ansible/test/unit/loader/test-host.json'), task=TaskInclude()))

# Generated at 2022-06-13 08:29:40.336927
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename1 = 'path/to/include.yml'
    filename2 = 'path/to/include2.yml'

    task1 = type('Task', (object, ), dict(args={}, _uuid='ansible-task-1', _parent=type('', (object, ), dict(_uuid='ansible-playbook-1'))()))
    task2 = type('Task', (object, ), dict(args={}, _uuid='ansible-task-1', _parent=type('', (object, ), dict(_uuid='ansible-playbook-1'))()))
    task3 = type('Task', (object, ), dict(args={}, _uuid='ansible-task-1', _parent=type('', (object, ), dict(_uuid='ansible-playbook-2'))()))
    task4

# Generated at 2022-06-13 08:29:49.026022
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block

    class FakeIterator():
        def __init__(self):
            self._play = ansible.playbook.play.Play()

    class FakeRole():
        def __init__(self, name):
            self._role_name = name

    class FakeTask():
        def __init__(self, action="include", loop=False, parent=None, role=None):
            self._parent = parent
            self._role = role
            self._action = action
            self._loop = loop
            self._uuid = "FAKE_UUID"

        def copy(self):
            return FakeTask(self._action, self._loop, self._parent, self._role)


# Generated at 2022-06-13 08:29:59.464051
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    results = [
        {
            '_host': 'foo',
            'include': '{{ foo }}',
            'include_args': {'bar': 'baz'}
        },
        {
            '_host': 'foo',
            'include': '{{ foo }}',
            'include_args': {'bar': 'baz'}
        },
        {
            '_host': 'bar',
            'include': '{{ bar }}',
            'include_args': {'bar': 'baz'}
        },
    ]



# Generated at 2022-06-13 08:30:10.437248
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.shlex import split as shlex_split
    import json


# Generated at 2022-06-13 08:30:22.861574
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Host:
        def __init__(self, name):
            self.name = name
            self.vars = dict()

    class Task:
        def __init__(self, action):
            self.action = action
            self.loop = False
            self.vars = dict()
            self.no_log = False
            self._parent = None
            self._role = None
           

# Generated at 2022-06-13 08:30:37.666671
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import yaml
    import os.path
    from ansible.plugins.loader import become_loader, connection_loader, module_loader, lookup_loader
    from ansible.plugins.loader import callback_loader, strategy_loader, shell_loader, cache_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_executor import TaskExecutor
    from ansible.utils.display import Display
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task