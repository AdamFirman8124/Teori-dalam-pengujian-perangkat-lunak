

# Generated at 2022-06-13 08:20:59.492494
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.helpers import load_list_of_blocks

    class BaseTask(Base):
        def __init__(self, base_action):
            self._base_action = base_action

        @property
        def action(self):
            return self._base_action

       

# Generated at 2022-06-13 08:21:06.050867
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import IncludeTasks

    # Mypy doesn't like AnsibleModule because it is used in a dynamic way, so we
    # disable type checking for this stub code.
    from ansible.module_utils.common.collections import AnsibleModule # type: ignore

    # Construct a temporary file
    temppath = tempfile.mktemp()

# Generated at 2022-06-13 08:21:15.779011
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import json

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    variable_manager.extra_vars = {
        'my_name':'"Munir Njiru"',
        'short_version':'"v1"'
    }

# Generated at 2022-06-13 08:21:27.271808
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    class Host:
        name = None
        def __init__(self, name):
            self.name = name

    class Play:
        def __init__(self, name):
            self.name = name

    class Role(object):
        def __init__(self, role_path):
            self._role_path = role_path

    class RoleInclude(IncludeRole):
        def __init__(self, from_files, role, task_include):
            super(RoleInclude, self).__init__(from_files)
            self._role_name = role
            self._task_include = task_include


# Generated at 2022-06-13 08:21:35.472982
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    A test_IncludedFile_process_include_results() function has been provided to
    confirm that IncludedFile.process_include_results() will identify and
    correctly handle the many possible duplicate includes that can be generated
    using with_* loops, cross product and omit_token.
    '''

    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.handler import Handler
    from ansible.playbook.included_file import IncludedFile
    from ansible.vars.manager import VariableManager
    import os
    import json



# Generated at 2022-06-13 08:21:41.867355
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    included_file_ref = IncludedFile('filename', 'args', 'vars', 'task', 'is_role')
    included_file_ref.add_host('hosts')
    included_file_to_test = IncludedFile('filename', 'args', 'vars', 'task', 'is_role')
    included_file_to_test.add_host('hosts')
    assert (included_file_ref.__eq__(included_file_to_test))


# Generated at 2022-06-13 08:21:52.256325
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()

    class FakePlay:
        def __init__(self):
            self.hostvars = {}
            self.roles = []

    class FakeTask:
        def __init__(self, parent=None):
            self.action = None
            self.loop = False
            self._uuid = None
            self._parent = parent

        def copy(self):
            return FakeTask()

    class FakeHost:
        def __init__(self, name):
            self.name = name

   

# Generated at 2022-06-13 08:22:01.521349
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    play = Play()
    play.hosts = ['localhost']
    play.name = 'test play'
    play._play_context = PlayContext()
    play._variable_manager = VariableManager()
    play._variable_manager.set_fact_cache({'foo': 'bar'})

# Generated at 2022-06-13 08:22:16.258602
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    if1 = IncludedFile("foo",
                       {"a": "b"},
                       {"c": "d"},
                       "Task 1",
                       is_role=True)
    if2 = IncludedFile("foo",
                       {"a": "b"},
                       {"c": "d"},
                       "Task 1",
                       is_role=True)
    if3 = IncludedFile("bar",
                       {"a": "b"},
                       {"c": "d"},
                       "Task 1",
                       is_role=True)
    if4 = IncludedFile("foo",
                       {"a": "a"},
                       {"c": "d"},
                       "Task 1",
                       is_role=True)
    if5 = IncludedFile("foo",
                       {"a": "b"},
                       {"c": "c"},
                       "Task 1",
                       is_role=True)

# Generated at 2022-06-13 08:22:28.186127
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # include_role result is not used as include tasks should not have loop
    include_role_result = {
        'changed': False,
        '_ansible_no_log': False,
        'include_role': {
            'include_tasks': '/etc/ansible/roles/not-a-role/tasks/main.yml'
        },
        'include_task': '/etc/ansible/roles/not-a-role/tasks/main.yml',
        'invocation': {
            'module_args': 'role name=not-a-role',
            'module_name': 'include_role'
        }
    }
    # include_tasks result

# Generated at 2022-06-13 08:22:55.352181
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import os

    import json
    import sys
    import shutil
    import tempfile
    import unittest

    from ansible.module_utils import basic
    from ansible.module_utils.six.moves import builtins
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import play_context_variables

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_result import TaskResult
    from ansible.executor.stats import AggregateStats
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.display import Display

    from ansible.vars import VariableManager

# Generated at 2022-06-13 08:23:05.241915
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible import variables
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext


    class TestTaskExecutor:
        def get_host_result(self, result):
            return result


# Generated at 2022-06-13 08:23:16.131575
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.unsafe_proxy import UnsafeProxy

    class MyHost:
        def __init__(self):
            self.name = 'localhost'

# Generated at 2022-06-13 08:23:28.437497
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeModuleRunner:
        def __init__(self, results):
            self.results = results

        def run(self, task_vars=dict()):
            return self.results

    class FakeTask:
        def __init__(self, action, parent=None, _role=None, loop=False, _role_name=None, no_log=False, _from_files=dict()):
            self.action = action
            self._parent = parent
            self._role = _role
            self.loop = loop
            self._role_name = _role_name
            self.no_log = no_log
            self._from_files = _from_files


# Generated at 2022-06-13 08:23:39.565933
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    fake_loader = None
    fake_variable_manager = VariableManager()
    fake_iterator = None
    fake_task = TaskInclude()

    # A simple test with one host and one include
    tr1 = TaskResult(fake_host, fake_task, dict(failed=False, skipped=False, include='/tmp/test1'))
    results = [tr1]

# Generated at 2022-06-13 08:23:46.190513
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    loader = FakeLoader()
    variable_manager = FakeVariableManager()

# Generated at 2022-06-13 08:23:56.452833
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader

    class MockPlaybook:
        pass

    class MockTemplate:
        def __init__(self, loader):
            self.loader = loader
        def template(self, x, **kwargs):
            return x

    class MockIterator:
        def __init__(self, playbook):
            self._play = playbook

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(omit='$')
    loader = DataLoader()
    templar = MockTemplate(loader)

   

# Generated at 2022-06-13 08:24:08.650462
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'filename'
    args = 'args'
    vars = 'vars'
    task = 'task'
    is_role = 'is_role'

    inc_file = IncludedFile(filename, args, vars, task, is_role)
    if not inc_file.__eq__(inc_file):
        raise Exception('included file is not equal to itself')

    filename_2 = 'filename_2'
    inc_file_args = IncludedFile(filename_2, args, vars, task, is_role)
    if inc_file.__eq__(inc_file_args):
        raise Exception('included files with different filename are equal')

    inc_file_args_2 = IncludedFile(filename, args, vars, task, is_role)

# Generated at 2022-06-13 08:24:20.398808
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import datetime
    from ansible.playbook.task import Task

    args = {'a': 'b'}
    vars = {'v': 'w'}
    filename = 'file.yml'
    task_uuid = '9f8a30b1-1fda-4bcc-b6c2-6b98989b6c99'
    task_parent_uuid = '1d6acec0-ceca-48ce-b6f2-01e2d9b9cab4'

    task_1 = Task()
    task_1._uuid = task_uuid
    task_1._parent = datetime
    task_1._parent._uuid = task_parent_uuid

    task_2 = datetime
    task_2._uuid = task_uuid
   

# Generated at 2022-06-13 08:24:31.431230
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class MockHost:
        def __init__(self, name):
            self.name = name
        def __eq__(self, other):
            return self.name == other.name
        def __hash__(self):
            return hash(self.name)

    class MockTask:
        def __init__(self, uuid, action, args, no_log, parent, loop, role=None):
            self._uuid = uuid
            self.action = action
            self._parent = parent
            self.no_log = no_log
            self.loop = loop
            self._role = role
            self.args = dict()
            for k, v in args.items():
                self.args[k] = v

# Generated at 2022-06-13 08:25:11.509131
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Include:
        def __init__(self, include):
            self.include = include
        def __eq__(self, other):
            return self.include == other.include
    class Iterator:
        def __init__(self, play):
            self._play = play
    class Loader:
        def __init__(self, basedir):
            self._basedir = basedir
        def path_dwim(self, path):
            if os.path.isabs(path):
                return path
            else:
                return os.path.join(self._basedir, path)
        def get_basedir(self):
            return self._basedir
    class VariableManager:
        def __init__(self, variables):
            self._variables = variables

# Generated at 2022-06-13 08:25:19.579400
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # pylint: disable=unused-argument
    class Fake:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.no_log = False

    class FakeModule:
        def __init__(self, **kwargs):
            self.params = kwargs

    class FakeResult:
        def __init__(self, **kwargs):
            self._result = kwargs

    class FakeIterator:
        _play = Fake()

    class FakeRole:
        _role_path = '../roles/test'

    class FakeLoader:
        def get_basedir(self):
            return '../roles/test'


# Generated at 2022-06-13 08:25:26.274819
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:25:28.283047
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    ''' test case for process_include_results '''
    pass

# Generated at 2022-06-13 08:25:41.149824
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys

    class MockIncludeResult(object):
        def __init__(self, results_list, host, task):
            self.results_list = results_list
            self._result = results_list[0]
            self._host = host
            self._task = task

        def __iter__(self):
            return iter(self.results_list)

    class MockTask(object):
        def __init__(self, from_files, action, parent, uuid):
            self._from_files = from_files
            self.action = action
            self._parent = parent
            self._uuid = uuid

        def copy(self):
            return MockTask(self._from_files, self.action, self._parent, self._uuid)

        def get_search_path(self):
            return ['role']



# Generated at 2022-06-13 08:25:48.603364
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    import ansible.executor.task_result as task_result
    tr = task_result.TaskResult(task=None, host=None, task_fields=None, role_name=None)

    class TestIterator(object):
        def __init__(self):
            self._play = {'playbook_dir': 'playbook_dir'}

    test_res = task_result.TaskResult(task=None, host=None, task_fields=None, role_name=None)

# Generated at 2022-06-13 08:26:01.407698
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Two objects with different filename should not be equal
    # Two objects with the same filename but different args should not be equal
    # Two objects with the same filename and the same args but different vars should not be equal
    # Two objects with the same filename and the same args and the same vars but different task should not be equal
    # Two objects with the same filename and the same args and the same vars and the same task should be equal

    # Objects with same filename but different args should not be equal
    included_file_1 = IncludedFile("filename_1", {"arg_1": 1, "arg_2": 2}, {}, "Task1")
    included_file_2 = IncludedFile("filename_1", {"arg_2": 2, "arg_1": 1}, {}, "Task1")
    assert included_file_1 != included_file_2

    #

# Generated at 2022-06-13 08:26:09.446796
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.plugin_docs import get_docstring


# Generated at 2022-06-13 08:26:19.418981
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader

    def _clean_tasks(task_list):
        for t in task_list:
            if isinstance(t, TaskInclude):
                t._parent = None
                _clean_tasks(t.block)


    # collect the roles from the files, so we can reference them easily
    loader = DataLoader()
    play = plugin_loader.load_from_file(loader, 'tests/playbooks/role_data.yaml')
    play_hosts = set()
    play_tasks = list()

    # Remove all the parents to make these tasks easily indexable
    _clean_tasks(play.get_tasks())

    # Get the tasks and hosts in one easy list
    # For roles

# Generated at 2022-06-13 08:26:20.761746
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    obj = IncludedFile(None, None, None, None)
    assert obj.__eq__(object()) == False


# Generated at 2022-06-13 08:27:25.505928
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext

    # Mock the host result
    class Result:
        def __init__(self, failed, skipped, item_label, loop_var, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    class Task:
        def __init__(self, parent_task=None, no_log=False):
            self._parent = parent_task
            self.no_log = no_log

    # Mock the loader
    class Loader:
        def __init__(self, basedir):
            self.basedir = basedir

        def get_basedir(self):
            return self.basedir

    class Play:
        def __init__(self, basedir):
            self.basedir = basedir


# Generated at 2022-06-13 08:27:30.708904
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play

    class Host:
        name = 'host'

    class Task:
        action = 'include'
        loop = False
        no_log = False
        _hosts = []
        _role = None
        _role_name = None
        _from_files = []
        _parent = None

        def __init__(self):
            self._uuid = 'task-%s' % self.action

        def __repr__(self):
            return 'Task(%s)' % self.action

        FROM_ARGS = ('include_tasks_from', 'vars_from')

        def copy(self):
            copy = Task()
            copy._uuid = self._uuid
            copy.action = self.action
            copy.loop = self.loop

# Generated at 2022-06-13 08:27:44.523687
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    """
    Run the test
    :return:
    """
    import collections
    import json
    import unittest

    # Import here... to ensure that it is imported after the patching
    from ansible.playbook.included_file import IncludedFile

    # Create a mocked version of Loader
    class MockedLoader:

        _basedir = "some_basedir"

        def get_basedir(self):
            return self._basedir

        def path_dwim(self, other):
            return "mocked_path_dwim(%s)" % other

    # We only need a dummy class for the mocked role
    class MockedRole:
        """
        Dummy class for a Mocked Role
        """
        _role_path = "some_role_path"


# Generated at 2022-06-13 08:27:54.770086
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play

    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:27:57.622023
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    t = IncludedFile('filename', 'args', 'vars', 'task')
    t1 = IncludedFile('filename', 'args', 'vars', 'task')

    assert t == t1


# Generated at 2022-06-13 08:28:04.617339
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.task import Task
    results = [Result(host='fake-host', task=Task(action='include_tasks', omit_token='__omit_place_holder__',
                                                  args={'_raw_params':'fake.yml'}),
                     result={'include': 'fake.yml'})]
    variable_manager = DummyVariableManager()
    loader = DummyLoader()
    iterator = DummyPlaybookIterator()
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)

    assert included_files[0]._filename == 'query/fake.yml'
    assert included_files[0]._args == {}
    assert included_files[0]._task.action == 'include_tasks'

# Generated at 2022-06-13 08:28:10.779357
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO
    #TODO

    from ansible.executor.task_result import TaskResult
    from ansible.template import Templar
    from ansible.vars import VariableManager

    task_res1 = TaskResult(host=None, task=None)
    task_res1._result = {'include': 'tasks/main.yml', 'include_args': {'_raw_params': 'tasks/main.yml'}}
    task_res1._host = 'a'

    templar = Templar()
    var_mgr = VariableManager()



# Generated at 2022-06-13 08:28:24.879273
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook import Playbook
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_result import TaskResult

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])

    task_vars = dict()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.set_inventory(inventory)

    playbook_path = '../../lib/ansible/playbooks/include_role.yml'
    playbook = Playbook.load(playbook_path, variable_manager=variable_manager, loader=loader)



# Generated at 2022-06-13 08:28:36.260673
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # pylint: disable=bare-except
    from ansible.executor import task_result
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    fake_loader = FakeLoader()

    def create_task(name, play, include_action=None, no_log=None, loop=False, loop_with=None):
        task = Task()
        task.name = name
        task._role = None
        task._play = play
        task._parent = None
        task._action = include_action
        task._loop_with = loop_with
        task._loop = loop
        task._no_log = no_log
        task._dep_chain = []
        return task


# Generated at 2022-06-13 08:28:47.105821
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.module_utils.six import PY3

    if PY3:
        long = int

    play_data = dict(
        name='test_play',
        hosts='localhost',
        gather_facts='no',
        tasks=[dict(name='test_task', debug=dict(var='test_var'))]
    )
    pb = PlaybookInclude.load(play_data, loader=None, variable_manager=None)
    pb._load_name = 'test_playbook'
    play = pb.get_plays()[0]
    block