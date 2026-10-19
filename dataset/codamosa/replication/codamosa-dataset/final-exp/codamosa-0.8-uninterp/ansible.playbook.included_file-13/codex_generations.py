

# Generated at 2022-06-13 08:21:05.725705
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    iterator = None
    loader = None
    variable_manager = None
    task_vars = dict(a="A")
    include_file = IncludedFile("filename", dict(b="B"), task_vars, TaskInclude("a", "b", True, False, False, False), False)
    assert include_file == IncludedFile("filename", dict(b="B"), task_vars, TaskInclude("a", "b", True, False, False, False), False)
    assert not include_file == IncludedFile("filename", dict(b="C"), task_vars, TaskInclude("a", "b", True, False, False, False), False)
    assert not include_file == IncludedFile("filename", dict(b="B"), dict(a="B"), TaskInclude("a", "b", True, False, False, False), False)

# Generated at 2022-06-13 08:21:12.692954
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.manager import VariableManager
    import os
    import random

    class TestCallbackModule(CallbackBase):
        def __init__(self, *args, **kwargs):
            super(TestCallbackModule, self).__init__(*args, **kwargs)
            self.event_data = dict()
            self.task_events = dict()
            self.playbook_results = list()

        def v2_runner_on_ok(self, result):
            host = result._host
            self.event_

# Generated at 2022-06-13 08:21:25.286442
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import get_all_plugin_loaders

    class FakeVariableManager:
        def get_vars(self, play, host, task):
            return {'LoopVar': 'LoopValue', 'IndexVar': 'IndexValue', 'IncludeVars': 'IncludeVarsValue'}

    class FakeTask:
        _parent = None
        action = 'action'
        loop = False
        _role = None
        _role_name = None
        _from_files = None
        _play = None
        no_log = False
        FROM_ARGS = ['from_myarg', 'from_myarg2']

        def __init__(self, loop):
            self.loop = loop
            self._from_files = {'myarg': 'value1', 'myarg2': 'value2'}


# Generated at 2022-06-13 08:21:34.367078
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # first test __eq__ of class TaskInclude
    class fake_TaskInclude:
        def __init__(self, uuid, parent_uuid):
            self._uuid = uuid
            self._parent = parent_uuid

    # second test __eq__ of class IncludeRole
    class fake_IncludeRole:
        def __init__(self, uuid, parent_uuid):
            self._uuid = uuid
            self._parent = parent_uuid

    # test for class IncludedFile
    for action in ["include", "include_tasks", "import_tasks", "import_playbook"]:
        filename = "test_file"
        args = {"tasks": [1, 2, 3]}
        vars = {"variable": "value"}

# Generated at 2022-06-13 08:21:44.153613
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Create a "fake" results with the following structure:
    # include:
    #   - include: file1
    #   - include: file2
    results = []
    for i in range(1, 3):
        result = FakeResult()
        result.action = 'include'
        result.task = FakeTask()
        result.task.name = 'task %d' % i
        result.task.action = 'include'
        result.task.loop = True
        if i % 2 == 0:
            result.task.loop_control = 'loop_var: "item"'
        result.host = 'host %d' % i

# Generated at 2022-06-13 08:21:53.588836
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.path import unfrackpath
    from tempdir import mkdir
    from ansible.utils.path import unfrackpath

    mock_task

# Generated at 2022-06-13 08:21:59.126526
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import pytest
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory/test_host_pattern.yml'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:22:14.029128
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task

    if1 = IncludedFile("filename1", "args1", "vars1", Task(), False)
    if2 = IncludedFile("filename1", "args1", "vars1", Task(), False)
    if3 = IncludedFile("filename1", "args1", "vars1", Task(), False)

    # comparing object with itself
    assert if1 == if1

    # comparing distinct objects of the same class
    assert if1 == if2

    # comparing distinct objects which differ in one field
    if3._filename = "filename2"
    assert if1 != if3
    assert if2 != if3

    # comparing distinct objects which differ in two fields
    if3._args = "args2"
    assert if1 != if3
    assert if2 != if3

    # comparing distinct objects which

# Generated at 2022-06-13 08:22:18.444541
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:22:33.684513
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class FakeResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class FakeTask:
        class FakePlay:
            pass
        def __init__(self, action):
            self.action = action
            self.loop = False
            self.no_log = False
            self._parent = None
            self._role = None
            self._play = FakeTask.FakePlay()
            self.FROM_ARGS = []
            self._from_files = {}
        def get_search_path(self):
            return []
        def copy(self):
            return FakeTask(self.action)

    class FakeVariableManager:
        cache = dict()

# Generated at 2022-06-13 08:23:06.817181
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import sys
    sys.path.append('../lib/ansible')

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_dependency import RoleDependency

    # Dummy TaskIn

# Generated at 2022-06-13 08:23:17.318177
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json

    fake_results = []

    # Include file by name, but only log the result

# Generated at 2022-06-13 08:23:29.553387
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)
    task_vars = HostVars({}, loader=loader)
    include_role = IncludeRole()
    include_role.args = {'name': 'role'}
    include_role._role_path = 'roles/rolename'
    task = Task()

# Generated at 2022-06-13 08:23:36.288941
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    '''Test method __eq__ of class IncludedFile'''
    inc_file1 = IncludedFile(
        "_filename",
        "_args",
        "_vars",
        "_task",
        "_is_role"
    )
    inc_file2 = IncludedFile(
        "_filename",
        "_args",
        "_vars",
        "_task",
        "_is_role"
    )
    assert inc_file1 == inc_file2


# Generated at 2022-06-13 08:23:45.795321
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor import task_executor
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.included_file import IncludedFile
    import unittest


# Generated at 2022-06-13 08:23:56.174128
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.play_iterator import PlayIterator

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler

    loader = DataLoader()
    hostvars = dict(foo="foobar")

# Generated at 2022-06-13 08:24:12.288935
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """Unit test for method process_include_results of class IncludedFile"""

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    # TODO: create an AnsibleBaseInclude module to get rid of the dummy_module below
    class DummyModule(object):
        def __init__(self, result):
            self.result = result


# Generated at 2022-06-13 08:24:24.573275
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:24:33.763263
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from collections import namedtuple

    # Variables used in the test
    fake_filename = "my_fake_filename.txt"
    args1 = (1, 2, 3)
    vars1 = {'key1': 'value1', 'key2': 'value2'}
    parent1 = Play()
    task1 = Task(use_main_task_vars=True, parent=parent1)
    is_role1 = True

    args2 = (1, 2, 3)
    vars2 = {'key1': 'value1', 'key2': 'value2'}
    parent2 = Play()
    task2 = Task(use_main_task_vars=True, parent=parent2)
    is_

# Generated at 2022-06-13 08:24:42.549935
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # setup
    results = []
    iterator = IncludedFile(None, None, None, None)
    loader = IncludedFile(None, None, None, None)
    variable_manager = IncludedFile(None, None, None, None)

    # no results
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)
    assert len(included_files) == 0

    # results with three includes
    # all with the same task and host
    results = []
    results.append(IncludedFile(None, None, dict(filename='filename_1', args='dict(name="role_1", role="role_1_name")', task='Task', host='host')))

# Generated at 2022-06-13 08:25:18.746955
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys,os

    # Import required classes in same order as they are imported in IncludedFile.process_include_results

    # Class to store the include results returned by Ansible
    class IncludeResult:
        def __init__(self, action, item):
            self._result = {'include': item}
            if action in C._ACTION_INCLUDE:
                display.deprecated('"include" is deprecated, use include_tasks/import_tasks/import_playbook instead', "2.16")
            self._task = TaskInclude(action=action, args={'_raw_params': item})
            self._host = 'lo'

        def __repr__(self):
            return "Include Result action=%s item=%s" % (self._task.action, self._result['include'])

    # Boolean to

# Generated at 2022-06-13 08:25:25.054081
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.playbook.play_context

    context = ansible.playbook.play_context.PlayContext()

    import ansible.playbook
    import ansible.inventory
    import ansible.vars.manager

    play = ansible.playbook.Play()
    play.set_loader()

    play._variable_manager = ansible.vars.manager.VariableManager()

    play.set_context(context)
    play._variable_manager.set_inventory(ansible.inventory.Inventory(loader=play.get_loader(), variable_manager=play._variable_manager))

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.plugins.loader import lookup_loader


# Generated at 2022-06-13 08:25:39.524008
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Task:
        def __init__(self):
            self._uuid = 'uuid'
            class _Parent:
                def __init__(self):
                    self._uuid = 'parent_uuid'
            self._parent = _Parent()
    # Test case 1: all attributes are the same
    _filename = 'filename'
    _args = 'args'
    _vars = 'vars'
    _task = Task()

    included_file = IncludedFile(_filename, _args, _vars, _task)
    included_file_same = IncludedFile(_filename, _args, _vars, _task)

    # In this case, both two included_file instances are the same one.
    assert included_file == included_file_same


# Generated at 2022-06-13 08:25:51.415300
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    '''tests the method IncludedFile.__eq__'''
    i1 = IncludedFile('/path/to/file1', dict(), dict(), None)
    i2 = IncludedFile('/path/to/file1', dict(), dict(), None)
    i3 = IncludedFile('/path/to/file2', dict(), dict(), None)
    i4 = IncludedFile('/path/to/file1', dict(a=1), dict(), None)
    i5 = IncludedFile('/path/to/file1', dict(a=1), dict(), None)
    i6 = IncludedFile('/path/to/file1', dict(a=1), dict(), None, is_role=True)
    assert i1 == i2
    assert i1 != i3
    assert i1 != i4
    assert i4 == i5

# Generated at 2022-06-13 08:26:03.310259
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # test that two IncludedFiles are equal if they have identical data
    # fields
    if1 = IncludedFile("foo", dict(), dict(), None)
    if2 = IncludedFile("foo", dict(), dict(), None)
    if3 = IncludedFile("foo", dict(), dict(), None)

    assert if1 == if1
    assert if1 == if2
    assert if2 == if3

    # test that two IncludedFiles are not equal if they have different data
    # fields
    if1 = IncludedFile("foo", dict(), dict(), None)
    if2 = IncludedFile("foo", dict(), dict(bad=True), None)
    if3 = IncludedFile("foo", dict(), dict(), None)
    if4 = IncludedFile("foo", dict(bad=True), dict(), None)
    if5 = IncludedFile("foo", dict(), dict(), None)



# Generated at 2022-06-13 08:26:13.436767
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play_executor import PlayExecutor
    from ansible.playbook.play_context import PlayContext

    pb = Playbook()

# Generated at 2022-06-13 08:26:22.418614
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    pb = Playbook()
    play = Play()
    play.vars = dict()
    play._loader = loader
    pb.set_loader(loader)
    play._variable_manager = VariableManager(loader=loader, play=play)
    playcontext = PlayContext()

# Generated at 2022-06-13 08:26:23.552346
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass


# Generated at 2022-06-13 08:26:36.342768
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    #import pdb
    #pdb.set_trace()
    import collections
    import ansible.inventory
    import ansible.template
    import ansible.vars
    class FakeIterator:
        def __init__(self):
            self._play = collections.namedtuple('play', ['vars'])(vars={})
    class FakeHost:
        def __init__(self, name):
            self.name = name
    class FakeTask:
        def __init__(self, action, args=None, loop=None, no_log=None, parent=None, _parent=None, _uuid=None):
            self.action = action
            self.args = args if args else {}
            self.loop = loop
            self.no_log = no_log
            self.parent = parent
            self._parent = _

# Generated at 2022-06-13 08:26:47.202890
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import sys
    import json
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager


    class IncludedFileTest(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.variable_manager = VariableManager()
            self.host = Host(name="localhost")
            self.play = Play().load({}, loader=self.loader, variable_manager=self.variable_manager, loader_cache=self.loader._find_file_in_search_path)
            self.play_context = PlayContext()
            self.iterator = self

# Generated at 2022-06-13 08:27:44.169939
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        'one.yml': '',
        'dir/two.yml': '',
        'dir/three.yml': '',
        'dir/dir2': {'four.yml': ''}
        })
    inventory = DictInventory({'all': DictHost({})})
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=VariableManager(loader=loader, inventory=inventory),
        loader=loader,
        passwords={}
        )

    result = CommandResult(host=inventory.get_host('all'))
    result.start()
   

# Generated at 2022-06-13 08:27:51.173232
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json

    # Example taken from https://github.com/ansible/ansible/issues/20951

# Generated at 2022-06-13 08:28:06.132731
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible import context
    from ansible.executor.task_executor import TaskResult
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    fake_host = Host(name='hostname')
    fake_task = Task.load(dict(action='include_role', loop='results'))
    fake_task._role_name = 'fake_role'
    fake_task._parent = Task.load(dict(action='fake_action'))

    fake_result = TaskResult(fake_host, fake_task, is_changed=True, is_skipped=False)

    fake_results = []
    fake_results.append(fake_result)

    for fake_result in fake_results:
        fake_result._result['results'] = []

# Generated at 2022-06-13 08:28:18.037419
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

# Generated at 2022-06-13 08:28:30.614526
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest

    sys.modules['ansible'] = type('module', (object,), dict(__file__=__file__))

    from ansible.playbook.base import Play
    from ansible.playbook.play import Play as PlayBookPlay
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    action_plugins = action_loader.all()

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict()
    variable_manager._vars_cache = dict()
    variable_manager._hostvars = dict()
    variable

# Generated at 2022-06-13 08:28:42.422396
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'file'
    args = {'a': 'b'}
    vars = {'v': 'w'}
    task_uuid = 'aa-bb-cc'
    parent_task_uuid = 'dd-ee-ff'

    task = object()
    setattr(task, '_uuid', task_uuid)
    task_parent = object()
    setattr(task_parent, '_uuid', parent_task_uuid)
    setattr(task, '_parent', task_parent)

    inc_file1 = IncludedFile(filename, args, vars, task)
    inc_file2 = IncludedFile(filename, args, vars, task)

    assert inc_file1 == inc_file2


# Generated at 2022-06-13 08:28:50.096860
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.base import PlayContext

    PlayContext._init_global_context()  # initialize context

    play = Play()                   # create play
    play._hosts = ['localhost']     # set hosts of play

    play_context = PlayContext(play=play)  # create play context

    task = Task()                   # create task
    task._parent = play             # set task parent
    task._role = None               # set task role to None
    play._tasks.append(task)        # append task to play tasks

    filename = 'play_0.yml'         # set filename
    args = {'_raw_params': 'playbooks/play.yml'}      # set args
    vars = dict()                   #

# Generated at 2022-06-13 08:28:59.894928
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    include_file_1 = IncludedFile('playbook.yml', 'test@test.com', None, None)
    include_file_2 = IncludedFile('playbook.yml', 'test@test.com', None, None)
    include_file_3 = IncludedFile('passwords.yml', 'test@test.com', None, None)
    include_file_4 = IncludedFile('passwords.yml', 'test@test.com', None, None)

    assert include_file_1 == include_file_2
    assert include_file_3 == include_file_4
    assert include_file_1 != include_file_3


# Generated at 2022-06-13 08:29:07.013079
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.inventory
    import ansible.template
    import ansible.vars

    # Create an IncludeFile object
    obj = IncludedFile("foo.yaml", {'a': 1}, {'b': 2}, object())

    # Test object representation
    repr_str = repr(obj)
    assert repr_str == "foo.yaml (args={'a': 1} vars={'b': 2}): []"

    # Test equality of two IncludeFile objects
    other_obj = IncludedFile("foo.yaml", {'a': 1}, {'b': 2}, object())
    assert obj == other_obj

    # Create another IncludeFile object
    obj2 = IncludedFile("bar.yaml", {'a': 1}, {'b': 2}, object())

    # Test inclusion of host in IncludeFile objects
    obj.add

# Generated at 2022-06-13 08:29:16.521680
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars import VariableManager
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()

    variable_manager = VariableManager()

    play_path = "./test/integration/targets/include_tests/host_vars/"
    play_obj = Play.load(play_path, variable_manager=variable_manager)
    play_iterator = play_obj.make_iterator()
