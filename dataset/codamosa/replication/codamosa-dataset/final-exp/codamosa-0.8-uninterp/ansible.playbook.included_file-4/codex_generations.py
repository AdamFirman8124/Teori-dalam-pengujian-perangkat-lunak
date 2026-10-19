

# Generated at 2022-06-13 08:21:05.672732
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import os

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    try:
        import mock
    except ImportError:
        from unittest import mock


# Generated at 2022-06-13 08:21:12.644488
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common._collections_compat import Mapping

    hosts = [Host('host1'), Host('host2')]

# Generated at 2022-06-13 08:21:23.306158
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # AnsibleTaskIncludeTask.process_include_results(results, iterator, loader, variable_manager):
    # AnsibleTaskIncludeTask.process_include_results(results, iterator, loader, variable_manager):
    # AnsibleTaskIncludeTask.process_include_results(results, iterator, loader, variable_manager):
    # AnsibleTaskIncludeRole.process_include_results(results, iterator, loader, variable_manager):
    # AnsibleTaskIncludeRole.process_include_results(results, iterator, loader, variable_manager):
    # AnsibleTaskIncludeRole.process_include_results(results, iterator, loader, variable_manager):
    pass

# Generated at 2022-06-13 08:21:33.417001
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import unittest

    class MockTask:
        def __init__(self, action, loop, no_log, _uuid, _parent, _role, search_path):
            self.action = action
            self.loop = loop
            self.no_log = no_log
            self._uuid = _uuid
            self._parent = _parent
            self._role = _role
            self.search_path = search_path

        @staticmethod
        def get_search_path():
            return self.search_path

    class MockTaskResult:
        def __init__(self, _host, _task, _result):
            self._host = _host
            self._task = _task
            self._result = _result


# Generated at 2022-06-13 08:21:39.527316
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = None
    filename = 'roles/test/tasks/main.yml'
    args = {}
    vars = {'test':'test'}
    task = Task()
    task.vars = vars
    task.loop = "test_loop"
    is_role = False
    included_file = IncludedFile(filename, args, vars, task, is_role)
    host = 'test_host'
    included_file.add_host(host)
    assert included_file._hosts[0] == host
    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_

# Generated at 2022-06-13 08:21:50.912947
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class Task:
        def __init__(self, action, no_log=False, loop=False, parent=None, search_path=None, role=None):
            self.action = action
            self.no_log = no_log
            self.loop = loop
            self._parent = parent
            self._search_path = search_path
            self._role = role
            
        def get_search_path(self):
            return self._search_path

    class Host:
        def __init__(self, hostname):
            self.name = hostname

    class Play:
        def __init__(self):
            pass


# Generated at 2022-06-13 08:21:56.585682
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    try:
        a = IncludedFile('filename', 'args', 'vars', 'task')
        b = IncludedFile('filename', 'args', 'vars', 'task')
        c = IncludedFile('filename', 'args', 'vars', 'task2')

        print(a == b)
        print(a == c)
    except ValueError:
        print("Error")


# Generated at 2022-06-13 08:22:04.353814
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Generate a test loader
    class Loader:
        def __init__(self):
            self.path = []
        def get_base_path(self):
            return self.path
        def path_dwim(self, path):
            return path
        def path_dwim_relative(self, base, path):
            return path
    loader = Loader()

    # Generate a variable manager
    variable_manager = VariableManager()

    # Setup an included file
    # Generate a test host
    class Host:
        def __init__(self, name):
            self.name = name
    host

# Generated at 2022-06-13 08:22:09.465137
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    Unit test of method IncludedFile.process_include_results
    """

    import ansible.constants as C
    import ansible.executor.task_queue_manager
    import ansible.executor.task_result
    import ansible.executor.task_executor
    import ansible.vars
    import ansible.playbook.play_context
    import ansible.playbook.role
    import ansible.playbook.task

    class group():
        def __init__(self):
            self.hosts = {}

    class host():
        def __init__(self):
            self.name = "host1"

    class play():
        def __init__(self):
            self.hosts = ["host1"]
            self.name = "play1"

            self.connection = "local"



# Generated at 2022-06-13 08:22:15.326717
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = [{'ansible_loop_var': 'item', 'item': 'test'}]
    # See usage of IncludedFile.process_include_results in task_include.py
    # def _run_tasks_from_included_file(self, results, iterator, loader, variable_manager):
    assert IncludedFile.process_include_results(results)

# Generated at 2022-06-13 08:22:38.226083
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Role:
        def __init__(self, role_path):
            self._role_path = role_path

    class RoleInclude(TaskInclude):
        def __init__(self, role):
            TaskInclude.__init__(self, 'role', None)
            self._role = role

    class Task:
        def __init__(self, parent):
            self._uuid = '0'
            self._parent = parent

    file1 = IncludedFile('/var/include_files/foo', {'a': '1'}, {'b': '2'}, Task(None))
    file2 = IncludedFile('/var/include_files/foo', {'a': '1'}, {'b': '2'}, Task(None))

# Generated at 2022-06-13 08:22:49.773244
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import types
    import sys
    import json
    import copy
    import os
    import tempfile

    # utility functions to create a temp file and save the given data to that
    # file in json format

    # used in the test since we need to mock the iterator and loader
    class MockIterator:
        def __init__(self, test_play, test_host):
            self._play = test_play
            self._host = test_host

    class MockLoader:
        def __init__(self, basedir):
            self._basedir = basedir

        def get_basedir(self):
            return self._basedir

    # create a temp file and save the given data in json format to that file
    # used to mock a test playbook or role

# Generated at 2022-06-13 08:22:54.819042
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Setup
    import ansible.plugins.loader as plugin_loader
    Display().verbosity = 0

    loader = plugin_loader.get('loader', 'file')
    variable_manager = plugin_loader.get('variable_manager')
    variable_manager.extra_vars = dict(
        my_test_var1='my_test_val1',
        my_test_var2='my_test_val2',
    )

    # Create a task with no_log set and action "include"
    from ansible.playbook.task import Task
    from ansible.utils.shlex import shlex_split
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:23:04.866134
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    host1 = type("Host", (object,), dict(name="host1"))
    host2 = type("Host", (object,), dict(name="host2"))
    task1 = Task()
    task2 = Task()
    task3 = Task()
    irole1 = IncludeRole()
    irole2 = IncludeRole()
    role = Role()
    loader = None
    variable_manager = VariableManager()
    variable_manager._vars = dict()
    variable_manager

# Generated at 2022-06-13 08:23:15.814436
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    obj_1 = IncludedFile('filename', 'args', 'vars', 'task')
    obj_2 = IncludedFile('filename', 'args', 'vars', 'task')
    try:
        assert obj_1 == obj_2
    except AssertionError:
        print('Method __eq__ of class IncludedFile() doesn\'t work')

    obj_3 = IncludedFile('', 'args', 'vars', 'task')
    try:
        assert obj_1 != obj_3
    except AssertionError:
        print('Method __eq__ of class IncludedFile() doesn\'t work')

    obj_4 = IncludedFile('filename', '', 'vars', 'task')

# Generated at 2022-06-13 08:23:23.409314
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task

    filename = 'test_file'
    args = 'test_args'
    vars = {
        'test_var': True,
        'test_var_2': False,
    }
    task = IncludeRole()
    task._uuid = 'test_uuid'
    task._parent = Task()
    task._parent._uuid = 'test_parent_uuid'

    inc_file_1 = IncludedFile(filename, args, vars, task)
    inc_file_2 = IncludedFile(filename, args, vars, task)

    assert inc_file_1 == inc_file_2

    vars['test_var_2'] = True

# Generated at 2022-06-13 08:23:34.821171
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    import tempfile, shutil

    TEMP_DIR = tempfile.mkdtemp()

    test_hosts = 'localhost'

# Generated at 2022-06-13 08:23:43.377124
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    loader.set_basedir('tests/lib/ansible/playbooks')
    pb = Playbook.load('test_included_file.yml', variable_manager=variable_manager, loader=loader, use_deprecated_authenticate=True)

# Generated at 2022-06-13 08:23:48.763900
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import re
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    playbook_path = os.path.join(os.path.dirname(__file__), '../../test/playbooks/recursive_include.yml')
    assert os.path.exists(playbook_path)

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['local'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:23:58.077744
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:24:20.853026
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    class FakeParent:
        def __init__(self):
            self._uuid = 'uuid'

    class FakeTask:
        def __init__(self):
            self._uuid = 'uuid'
            self._parent = FakeParent()

    fakeTask = FakeTask()

    # "==" should return True if the same arguments are used
    includedFile1 = IncludedFile(None, None, None, fakeTask)
    includedFile2 = IncludedFile(None, None, None, fakeTask)
    assert(includedFile1 == includedFile2)

    # "==" should return False if a different file is used
    includedFile3 = IncludedFile('filename', None, None, fakeTask)
    assert(not (includedFile1 == includedFile3))

    # "==" should return False if a different argument is used
    includedFile

# Generated at 2022-06-13 08:24:27.044032
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # setUp
    it1 = IncludedFile("/home/foo/test.yml", "test_args", "test_vars", "test_task", is_role=True)
    it2 = IncludedFile("/home/foo/test.yml", "test_args", "test_vars", "test_task", is_role=True)
    it3 = IncludedFile("/home/foo/test.yml", "test_args", "test_vars", "test_task", is_role=True)
    it3.add_host("test01")
    it3.add_host("test02")

    # test
    assert it1 == it2
    assert not it1 == it3
    assert it2 == it3



# Generated at 2022-06-13 08:24:37.757348
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import pytest
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    filename = '/path/to/filename1'
    filename2 = '/path/to/filename2'
    args = {'a': 4, 'c': 6}
    args2 = {'a': 1, 'c': 2}
    vars = {'b': 5, 'd': 7}
    vars2 = {'b': 2, 'd': 2}
    task = TaskInclude()
    task2 = TaskInclude()
    task2._role = None
    task2._parent = None
    task3 = TaskInclude()
    task3._role = None
    task3._parent = None
    task3._uuid = 'test_test_test'

    test_obj = IncludedFile

# Generated at 2022-06-13 08:24:47.797148
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook import task_include
    from ansible.playbook import role_include
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os

    display = Display()
    loader = DataLoader()
    loader.set_basedir(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'lib', 'ansible', 'test', 'sanity', 'include_vars', 'roles', 'role1'))
    display.description('TESTING INCLUDE RESULTS')

    # the task queue manager allows us to retrieve include results
    tqm

# Generated at 2022-06-13 08:25:02.700699
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    class Iterator(object):
        _play = Play()

    # Display is required by task_queue_manager
    display = Display()

    # Create a dummy data loader
    loader = DataLoader()

    # Create a dummy inventory
    inventory = InventoryManager(loader=loader, sources='localhost,')

    # Create a dummy variable manager
    variables = VariableManager()

    # Create a task queue manager

# Generated at 2022-06-13 08:25:18.318171
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


    # Setup inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    var_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext(become=False)
    play_context.accelerate = False
    play_context.network_os = "ios"
    play_context.remote_addr = "127.0.0.1"
    play_context.remote_user = "user"
   

# Generated at 2022-06-13 08:25:31.676926
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.color import stringc
    from ansible.vars.task_vars import TaskVars
    from ansible.vars.hostvars import HostVars

    from six import iteritems

    class FakePlugin:
        def __init__(self):
            self.results = []
            self.name = ""


# Generated at 2022-06-13 08:25:43.371613
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # Mock the results
    class Host:
        def __init__(self, name):
            self._name = name

        def __eq__(self, other):
            if isinstance(other, Host):
                return other._name == self._name
            return NotImplemented

        def __repr__(self):
            return "%s" % self._name

    class Task:
        def __init__(self, parent, name='include_a_task'):
            self._parent = parent
            self._name = name
            self._uuid = "UUID_%s" % self._name
            self.action = 'include_tasks'

        @property
        def loop(self):
            if 'loop' in self._name:
                return True
            return False


# Generated at 2022-06-13 08:25:56.361082
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.task import Task
    from ansible.playbook.block import TaskBlock
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # Test1: compare with same class object
    included_file = IncludedFile('test_filename', {'test_arg': 'test_value'}, {'test_var': 'test_var_value'}, 'test_task', False)
    assert included_file == included_file

    # Test2: compare with different class object
    assert included_file != IncludedFile('test_filename', {'test_arg': 'test_value'}, {'test_var': 'test_var_value'}, 'test_task', False)

    # Test3: compare with same

# Generated at 2022-06-13 08:26:06.568955
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from tests.mock.loader import DictDataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    results = []
    loader = DictDataLoader({})
    host = InventoryManager(loader=loader, sources=['localhost', 'otherhost'])
    variable_manager = VariableManager(loader=loader, inventory=host)
    iterator = None

# Generated at 2022-06-13 08:26:32.024610
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    display.v(3)
    return

# Generated at 2022-06-13 08:26:43.197112
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    Unit test for class IncludedFile
    """

    import sys
    import os
    import re
    import time
    import shutil
    import copy
    import datetime
    import json

    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.utils.display import Display

# Generated at 2022-06-13 08:26:52.643415
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Create mock objects for the task and the host
    task = object()
    task._uuid = '123'
    task._parent = object()
    task._parent._uuid = '456'

    host = object()

    # Create two 'IncludedFile' instances
    included_file1 = IncludedFile(
        'filename',
        dict(),
        dict(),
        task
    )
    included_file1.add_host(host)

    included_file2 = IncludedFile(
        'filename',
        dict(),
        dict(),
        task
    )
    included_file2.add_host(host)

    # Verify that both instances are equal.
    # This test will fail if the method __eq__ doesn't return 'True'
    assert included_file1 == included_file2



# Generated at 2022-06-13 08:27:04.820719
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    import ansible.playbook
    import ansible.playbook.block
    from ansible.playbook.play_context import PlayContext
    import os
    import tempfile
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    def create_task_in_block(block):
        """ Create a TaskInclude instance, add it to the given Block and return the TaskInclude instance """
        task = ansible.playbook.TaskInclude()
        task._role._role_path = tempfile.gettempdir() # Ansible assumes that this exists
        task.action = 'include'
        task.loop = '{{ result }}'
        task.args['_raw_params'] = '{{ lookup("template", "myfile.j2") }}'
        task._parent = block
        task._play = block

# Generated at 2022-06-13 08:27:15.502106
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # create a fake inventory
    inventory_manager = InventoryManager(DataLoader())
    inventory_manager.add_host("localhost")
    inventory_manager.add_host("host")
    inventory_manager.add_host("host1")
    inventory_manager.add_host("host2")
    inventory_manager.add_host("host3")

    # create a fake play, connecting the inventory above
    playcontext = PlayContext()
    playcontext.set_inventory(inventory_manager)
    playcontext.set_variable_manager(VariableManager())
    playcontext.set_loader(DataLoader())

    # task and result

# Generated at 2022-06-13 08:27:24.359748
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import unittest.mock
    class MockParent:
        _uuid = '1234-5678-90ab-cdef'
    class MockTask:
        _uuid = '1234-5678-90ab-cdef'
        _parent = MockParent()
    class MockVars:
        pass

    # 1. filename is different
    assert IncludedFile('filename_1', {}, MockVars, MockTask()) != IncludedFile('filename_2', {}, MockVars, MockTask())

    # 2. args are different
    assert IncludedFile('filename', {'arg1': 'val1'}, MockVars, MockTask()) != IncludedFile('filename', {'arg1': 'val2'}, MockVars, MockTask())

    # 3. vars are different

# Generated at 2022-06-13 08:27:34.539113
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeIterator:
        def __init__(self, play):
            self._play = play
    class FakePlay:
        def __init__(self, name):
            self.name = name
    class FakeTask:
        def __init__(self, uuid, action, no_log=False, _parent=None):
            self._uuid = uuid
            self.action = action
            self.no_log = no_log
            self._parent = _parent
    class FakeResult:
        def __init__(self, _host, _task, _result):
            self._host = _host
            self._task = _task
            self._result = _result
    class FakeHost:
        def __init__(self, name):
            self.name = name



# Generated at 2022-06-13 08:27:47.848857
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.basic import AnsibleModule

    # Create a fake module object constructed from an argument spec and a return value.
    module = AnsibleModule({'include': {'required': True, 'type': 'list'}}, '', 'include', '', '', '')


# Generated at 2022-06-13 08:27:58.337892
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible import context

    # FIXME: move this test to test infrastructure
    # FIXME: fix this test when we have an iterator mock

    import ansible.executor.task_result as task_result

# Generated at 2022-06-13 08:28:05.081689
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.reserved import Reserved

    vars_file = "vars_file"
    vars_dir = "vars_dir"
    vars_disk = "vars_disk"
    vars_all = "all"

    # a simple function to get a play context
    def get_play_context(var_manager=None):
        pc = PlayContext()
       

# Generated at 2022-06-13 08:29:03.719842
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.inventory.manager

    from ansible.cli import CLI
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    results = []
    hosts = ['host1', 'host2', 'host3']
    args = {
        'first_param': '{{ item }}',
        'second_param': '{{ item }}',
        'third_param': '{{ item }}',
    }
    tasks = [
        Task(action='include_tasks', args=args)
    ]

    playbook = Play()
    block = Block(playbook=playbook, tasks=tasks)

    for host in hosts:
        task = tasks[0].copy()


# Generated at 2022-06-13 08:29:15.695364
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    results = []
    for haddr in ('host1', 'host2', 'host3', 'host4'):
        for htask in ('task1', 'task2'):
            r = type('FakeResult', (object,),
                     {'_host': haddr, '_task': htask, '_result': {'include': 'included_file'}})
            results.append(r)

    included_files = IncludedFile.process_include_results(results, None, None, None)
    assert len(included_files) == 1
    assert included_files[0]._filename == 'included_file'
    assert included_files[0]._hosts
    for host in ('host1', 'host2', 'host3', 'host4'):
        assert host in included_files[0]._hosts

# Generated at 2022-06-13 08:29:30.158178
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.lookup as lookup_loader
    import ansible.plugins.task as task_loader
    import ansible.plugins.vars as vars_loader
    import ansible.playbook.play as play
    import ansible.vars.manager as vars_manager

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task_include import TaskInclude

    # We create three different hosts named localhost and two others.
    hosts = [dict(name='localhost'), dict(name='other'), dict(name='another')]

    # We use a dict of dicts to simulate inventory content.
    hostvars = {
        'localhost': {},
        'other': {},
        'another': {}
    }

    #

# Generated at 2022-06-13 08:29:38.696272
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class FakeTask:
        def __init__(self):
            self._uuid = "abcd"
            self._parent = FakePlay()

    class FakePlay:
        def __init__(self):
            self._uuid = "1234"

    class FakeArgs:
        def __init__(self):
            self._raw_params = "file"

    class FakeVars:
        def __init__(self):
            self.no_log = True

    task = FakeTask()
    args = FakeArgs()
    vars = FakeVars()


    include_file1 = IncludedFile("filename", args, vars, task)
    include_file2 = IncludedFile("filename", args, vars, task)
    include_file3 = IncludedFile("filename2", args, vars, task)

    assert include_file

# Generated at 2022-06-13 08:29:47.779460
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import json
    import mock

    class LoaderModule:
        def get_basedir(self):
            return '.'

        def path_dwim(self, file_name):
            return file_name

        def path_dwim_relative(self, basedir, target, name, is_role=False):
            return os.path.join(basedir, target, name)

    class Play:
        pass

    class Host:
        pass

    class Task:
        def __init__(self, action='include_tasks', name=None):
            self.action = action
            self.no_log = False
            self.args = dict()
            self.get_search_path = mock.MagicMock(return_value=[os.getcwd()])
            self.name = name
           

# Generated at 2022-06-13 08:29:57.284261
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import json
    import os
    import sys

    # FIXME: the TQM should just accept a host_list, and a variable_manager object,
    #        rather than all the other arguments we have to pass here (and below)
    t

# Generated at 2022-06-13 08:30:08.609345
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.plugins import plugin_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    class FakeResult:
        def __init__(self, task, host, item, action, result):
            self._task = task
            self._host = host
            self._result = result
            self._task.action = action


# Generated at 2022-06-13 08:30:21.955996
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    context = PlayContext()
    variables = dict(omit='omit')
    variable_manager.set_host_variable(host='localhost', varname='omit', value='omit')

    # generate a task of a certain action
    def gen_task(action, source=None, loopdict=None):
        from ansible.parsing.yaml.objects import AnsibleUnicode

        class Task:
            def __init__(self):
                self.action = action

# Generated at 2022-06-13 08:30:35.122600
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class IncludeRole:
        def __init__(self, role_name):
            self._role_name = role_name

    class Task:
        def __init__(self, name, args, parent=None):
            self._name = name
            self.action = name
            self.args = args
            self._parent = parent
            self.no_log = False
            self.loop = False
            self._role = None

        def copy(self):
            new_task = Task(self.action, self.args, self._parent)
            new_task.no_log = self.no_log
            new_task.loop = self.loop
            new_task._role = self._role
            return new_task

    class Host:
        def __init__(self, name):
            self.name = name
