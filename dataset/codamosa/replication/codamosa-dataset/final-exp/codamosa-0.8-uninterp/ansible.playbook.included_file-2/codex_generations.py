

# Generated at 2022-06-13 08:21:11.431340
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    Unit test for method process_include_results of class IncludedFile

    :return:
    """
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    results = []
    included_files = []

    external_vars = [dict()]
    inventory = PlaybookExecutor.load_inventory(loader, 'localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:21:18.393555
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.handler import Handler

    task1 = Task()
    task1._parent = Block()
    task1._parent._role = IncludeRole('RoleName')
    task1.action = 'include_role'

# Generated at 2022-06-13 08:21:29.434874
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    import ansible.playbook.task_include as task_include
    task_result = TaskResult({}, {})
    include_result = task_include.TaskIncludeResult(task_result, {}, {})
    include_results = [include_result]
    included_files = []
    loader = FakeLoader()
    iterator = FakeIterator()
    variable_manager = FakeVariableManager()

    IncludedFile.process_include_results(include_results, iterator, loader, variable_manager)
    included_file = included_files[0]
    assert included_file._filename == 'filename'
    assert included_file._args == 'args'
    assert included_file._vars == 'vars'
    assert included_file._task == 'task'
    assert included_file._

# Generated at 2022-06-13 08:21:36.863705
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class FakeHost:
        pass

    class FakeTask:
        def get_search_path(self):
            return []

        def __init__(self, uuid, action, parent=None):
            self._uuid  = uuid
            self.action = action
            self._parent = parent

    class FakePlay:
        def __init__(self, uuid):
            self._uuid  = uuid

    class FakeVariableManager:
        pass

    class FakeLoader:
        def __init__(self, basedir='/'):
            self._basedir = basedir

        def get_basedir(self, filename=None):
            return self._basedir

    class FakeResult:
        def __init__(self, host, task, result):
            self._host  = host
            self._task  = task
           

# Generated at 2022-06-13 08:21:41.059940
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    loader, iterator, variable_manager = (None, None, None)
    results = [IncludedFileResult(host=None, task=None, result=None)]
    included_file = IncludedFile.process_include_results(results, iterator, loader, variable_manager)
    assert len(included_file) == 0


# Generated at 2022-06-13 08:21:52.214606
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import yaml
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager

    def get_include_results(include_results):
        return [x for x in include_results if not isinstance(x, str) and isinstance(x, dict) and x.get('include')]

    def process_include_results(results, iterator, loader, variable_manager):

        included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)


# Generated at 2022-06-13 08:22:01.995809
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class AnsibleMock:
        pass

    class Host:
        pass

    class Playbook:
        pass

    class PlayIterator:
        pass

    class Task:
        pass

    class TaskInclude:
        pass

    class TaskResult:
        pass

    class VariableManager:
        pass

    class DataLoader:
        pass

    # Setup
    mock = AnsibleMock()
    mock.constants = AnsibleMock()
    mock.constants.ACTION_ALL_INCLUDES = C._ACTION_ALL_INCLUDES
    mock.constants.ACTION_INCLUDE = C._ACTION_INCLUDE

    host = Host()
    host.name = "host_name"

    play = Playbook()
    play.hosts = [host]

    iterator = PlayIterator()

# Generated at 2022-06-13 08:22:16.427835
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'
    host4 = 'host4'

    filename1 = 'filename1'
    filename2 = 'filename2'

    args1 = {'arg1': 'value1'}
    args2 = {'arg2': 'value2'}

    vars1 = {'var1': 'value1'}
    vars2 = {'var2': 'value2'}

    task1 = {'task1': 'value1'}
    task2 = {'task2': 'value2'}

    # Test creation
    included_file1 = IncludedFile(filename1, args1, vars1, task1)
    assert included_file1._filename == filename1
    assert included_file1._args == args1
   

# Generated at 2022-06-13 08:22:31.873922
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    task1 = TaskInclude()
    task2 = TaskInclude()
    filename1 = "/path/to/file1"
    filename2 = "/path/to/file2"
    filename3 = "/path/to/file1"
    args1 = {"_raw_params": "file1"}
    args2 = {"_raw_params": "file2"}
    args3 = {"_raw_params": "file1"}
    vars1 = {"var1": "value1"}
    vars2 = {"var2": "value2"}
    vars3 = {"var1": "value1"}
    inc1 = IncludedFile(filename1, args1, vars1, task1)
    inc2 = IncludedFile(filename2, args2, vars2, task1)

# Generated at 2022-06-13 08:22:34.634315
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    obj = IncludedFile('a', 'b', 'c', 'd')
    obj.add_host('e')
    assert obj._hosts == ['e']
    obj.add_host('e')
    assert obj._hosts == ['e', 'e']

# Generated at 2022-06-13 08:23:01.853547
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class Host(object):

        def __init__(self, name):
            self.name = name

    class ActionModule(object):

        def __init__(self, action='include'):
            self.action = action

        def __eq__(self, other):
            return self.action == other.action

    class Task(object):

        def __init__(self, action='include'):
            self.action = action
            self._parent = None
            self._role = None

    class ModuleResult(object):

        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result


# Generated at 2022-06-13 08:23:14.164375
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test __eq__ method of class IncludedFile
    """
    # Create two instances of IncludedFile
    # for testing __eq__ method
    # string 'c1' will be a key
    # in _vars and _args dicts
    # in both instances of IncludedFile
    c1 = 'c1'
    c2 = 'c2'
    filename1 = 'filename1'
    filename2 = 'filename2'
    args1 = {c1: 10}
    args2 = {c1: 11}
    vars1 = {c1: 20}
    vars2 = {c1: 21}
    task1 = 'task1'
    task2 = 'task2'

    # first instance of IncludedFile
    included_file1 = IncludedFile(filename1, args1, vars1, task1)



# Generated at 2022-06-13 08:23:22.483886
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import collections
    import copy
    import json
    import os
    import sys
    import tempfile

    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lib'))
    import ansible.plugins.loader

    # Provide a valid configuration
    ansible.constants.load_config_file()

    # Check the private method _ansible_load_callbacks of the module ansible.plugins.loader
    tempdir = tempfile.mkdtemp()

    loader = ansible.plugins.loader.ActionModuleLoader()

    iterator = collections.namedtuple('Iterator', ['play'])(play=None)

    variable_manager = ansible.vars.VariableManager()


# Generated at 2022-06-13 08:23:33.846576
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:23:39.108081
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = "hogehoge"
    args = "hoge"
    vars = "hoge"
    task = "hoge"
    is_role = "hoge"

    obj1 = IncludedFile(filename, args, vars, task, is_role)
    obj2 = IncludedFile(filename, args, vars, task, is_role)
    assert(obj1 == obj2)


# Generated at 2022-06-13 08:23:47.725938
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    import os
    import tempfile
    import shutil
    import textwrap
    from ansible.module_utils.six import PY3
    from ansible.plugins.loader import include_role_plugin, action_loader
    from ansible.plugins.action import ActionBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

# Generated at 2022-06-13 08:23:57.499140
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:24:09.323079
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 08:24:20.853499
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:24:31.884086
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    t1 = TaskInclude(play=None, block=None, role=None, task_include=None,
            args={'_raw_params': './include_me.yml', '_role': {}, '_has_task_include': True},
            local_action=None, private=None, no_log=None, delegate_to=None)
    t2 = TaskInclude(play=None, block=None, role=None, task_include=None,
            args={'_raw_params': './include_me.yml', '_role': {}, '_has_task_include': True},
            local_action=None, private=None, no_log=None, delegate_to=None)
    if1 = IncludedFile(filename='file1.yml', args={}, vars={}, task=t1)

# Generated at 2022-06-13 08:25:04.084302
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:25:13.068057
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    play = Play()
    task1 = Task()
    task1._uuid = '123'
    task1._parent = play
    task2 = Task()
    task2._uuid = '123'
    task2._parent = play

    included_file1 = IncludedFile('filename1', 'args1', 'vars1', task1)
    included_file2 = IncludedFile('filename2', 'args2', 'vars2', task2)
    included_file3 = IncludedFile('filename1', 'args1', 'vars1', task1)

    assert included_file1 != included_file2
    assert included_file1 == included_file3

# Generated at 2022-06-13 08:25:26.982036
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.module_utils.basic
    import ansible.inventory.manager


# Generated at 2022-06-13 08:25:40.326201
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import TaskIterator
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import plugin_loader

    # fake results
    results = []
    results.append({"skipped": False, "include": "include_file.yml", "include_args": {"some_var": "foo"}})
    results.append({"skipped": False, "include": "include_file.yml", "include_args": {"some_var": "foo"}})

# Generated at 2022-06-13 08:25:48.087843
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # Load modules needed for the unit test
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    # Create an empty variable_manager
    variable_manager = VariableManager()

    # Create a simple inventory of hosts
    inventory = InventoryManager(loader=DataLoader(), variable_manager=variable_manager)
    host_list = ['localhost', 'localhost']
    for h in host_list:
        inventory.add_host(h)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:26:01.033108
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import os
    import ansible.playbook.task_include as ti
    import ansible.playbook.role_include as ri
    import ansible.constants as C
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.template import Templar
    from ansible.vars import VariableManager

    DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'unit', 'data', 'task_include')

    # a variable manager is needed for Template
    variable_manager = VariableManager()

    # when testing just the results object, we use fake play and tasks
    fake_play = "Fake Play"

# Generated at 2022-06-13 08:26:09.161055
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    data1 = [
        {'hostname': 'host1', 'results': [{'include': 'web.yml'}]},
        {'hostname': 'host2', 'results': [{'include': 'web.yml'}]},
        {'hostname': 'host1', 'results': [{'include': 'database.yml'}]},
        {'hostname': 'host2', 'results': [{'include': 'database.yml', 'include_args': {'vars': {'db_pass': 'bar'}}}]}
    ]


# Generated at 2022-06-13 08:26:12.594481
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    task1 = TaskInclude()
    task1._uuid = 'something'
    task1._parent = None
    task1._parent._uuid = 'something else'

    task2 = TaskInclude()
    task2._uuid = 'something'
    task2._parent = None
    task2._parent._uuid = 'something else'

    assert(IncludedFile('a', 'b', 'c', task1) == IncludedFile('a', 'b', 'c', task2))

# Generated at 2022-06-13 08:26:27.396139
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class Task:
        def __init__(self):
            self._uuid = '1234567890'
        def get_parent(self):
            return Task()
        def __eq__(self, other):
            return (other._uuid == self._uuid)

    included_file_1 = IncludedFile('filename', {}, {}, Task())
    included_file_2 = IncludedFile('filename', {}, {}, Task())
    included_file_3 = IncludedFile('filename', {'arg1': 'value1'}, {'var1': 'value1'}, Task())
    included_file_4 = IncludedFile('filename1', {}, {}, Task())
    included_file_5 = IncludedFile('filename', {}, {'var1': 'value1'}, Task())

# Generated at 2022-06-13 08:26:39.708510
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

    class Task:

        def __init__(self, action):
            self.action = action
            self._uuid = 'task_uuid'
            self._parent = None
            self.no_log = False
            self.loop = False
            self._from_files = {}

        def __eq__(self, other):
            return self._uuid == other._uuid

        def get_search_path(self):
            return ['search_path']

        def copy(self):
            return self

    class Play:

        def __init__(self):
            self._uuid = 'play_uuid'


# Generated at 2022-06-13 08:27:29.328440
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role


# Generated at 2022-06-13 08:27:36.939101
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' Test case method tests the process_include_results method in IncludedFile '''
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.playbook_include import PlaybookInclude

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    itr = Play()
    it

# Generated at 2022-06-13 08:27:38.280973
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    pass


# Generated at 2022-06-13 08:27:49.325869
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.vars import combine_vars
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-13 08:28:04.666182
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    play1 = Play.load(dict(
        name="test play",
        hosts='webservers',
        )
    )

    task1 = Task.load(dict(
        action="foo",
        args=dict(name="testing"),
        )
    )

    inc_file1 = IncludedFile(filename='/path/to/file1.yml', args={'name': 'test'}, vars={}, task=task1)
    inc_file2 = IncludedFile(filename='/path/to/file1.yml', args={'name': 'test'}, vars={}, task=task1)

# Generated at 2022-06-13 08:28:14.509714
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Host:
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return self.name == other.name

        def __hash__(self):
            return hash(self.name)

    class Play:
        def __init__(self):
            self.hosts = ['localhost']

    class Task:
        def __init__(self):
            self.action = 'include_tasks'
            self._uuid = 'task1'
            self._parent = None

    class Role:
        def __init__(self, name):
            self._role_name = name
            self._uuid = name + 'uuid'

        def __eq__(self, other):
            return self._role_name == other._role_name


# Generated at 2022-06-13 08:28:28.530482
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    import json
    import unittest
    import yaml


    class fake_task(object):
        """
         Fake class to represent a task
        """

        def __init__(self, action, loop, no_log, parent, _raw_params):
            self.action = action
            self.loop = loop
            self.no_log = no_log
            self._parent = parent
            self._raw_params = _raw_params

        def get_search_path(self):
            return ['tasks']

        def copy(self):
            return fake_task(self.action, self.loop, self.no_log, self._parent, self._raw_params)

    class fake_result(object):
        """
        Fake class to represent a task result
        """


# Generated at 2022-06-13 08:28:41.238109
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json

    # test data

# Generated at 2022-06-13 08:28:49.587882
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    # Create host, group and play
    host = Host(name="test_host")
    group = Group('test_group', hosts=[host])
    play = Play().load({}, variable_manager=VariableManager(), loader=None)

    # Create results

# Generated at 2022-06-13 08:29:01.253530
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test 1: Equal parameters
    # Test 1.1: normal tasks
    task = TaskInclude()
    inc_file = IncludedFile('file1', 'args1', 'vars1', task)
    inc_file_2 = IncludedFile('file1', 'args1', 'vars1', task)
    assert inc_file == inc_file_2

    # Test 1.2: role tasks
    role_task = IncludeRole()
    inc_file_role = IncludedFile('file1', 'args1', 'vars1', role_task, True)
    inc_file_2_role = IncludedFile('file1', 'args1', 'vars1', role_task, True)
    assert inc_file_role == inc_file_2_role

    # Test 2: Different parameters
    # Test 2.1: file
   