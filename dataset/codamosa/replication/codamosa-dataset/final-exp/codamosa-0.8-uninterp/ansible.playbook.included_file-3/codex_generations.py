

# Generated at 2022-06-13 08:21:07.570583
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    include_file = IncludedFile(filename='foo.yaml', args=None, vars=None, task=None)
    include_file2 = IncludedFile(filename='foo.yaml', args=None, vars=None, task=None)

    assert include_file == include_file2

# Generated at 2022-06-13 08:21:16.069203
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    x = IncludedFile('x', 'y', 'z', 'a')
    y = IncludedFile('x', 'y', 'z', 'a')
    z = IncludedFile('y', 'y', 'z', 'a')
    w = IncludedFile('x', 'y', 'z', 'not a')

    # normal usage
    a = 'a'
    x.add_host(a)
    assert x._hosts == [a]

    # If we try to add the same host we should get a ValueError
    try:
        x.add_host(a)
    except ValueError:
        assert 1 == 1
    else:
        assert 1 == 0

    # If we try to add a different host to a diferent IncludedFile with
    # the same file and args, we should get a ValueError
    b = "b"

# Generated at 2022-06-13 08:21:27.547100
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import IncludeRole
    import yaml

    filename1 = "/home/user/roles/include_role/include_vars_files"
    args1 = dict()
    args1["role"] = "/home/user/roles/include_role/tasks"
    vars1 = dict()
    vars1["vars"] = dict()
    vars1["vars"]["include_role"] = dict()
    vars1["vars"]["include_role"]["var"] = "value"
    vars1["vars"]["include_role"]["var"] = "value"

# Generated at 2022-06-13 08:21:35.697389
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.plugins.loader import action_loader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    class Host:

        def __init__(self, name):
            self._name = name
            self._vars = None

        def get_name(self):
            return self._name

        def set_variable(self, k, v):
            if self._vars is None:
                self._vars = dict()
            self._vars[k] = v

        def get_vars(self):
            return self._vars


# Generated at 2022-06-13 08:21:45.271365
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    filename = 'my.file'
    args = {'key': 'value'}
    vars = {'var1': 'value1'}
    uuid = 'task-uuid'
    task = Task()
    task._uuid = uuid
    task._parent = object()
    task._parent._uuid = 'parent-uuid'
    incFile1 = IncludedFile(filename, args, vars, task)
    incFile2 = IncludedFile(filename, args, vars, task)
    incFile3 = IncludedFile('other.file', args, vars, task)
    incFile4 = IncludedFile(filename, {'key': 'other-value'}, vars, task)
    incFile5 = IncludedFile

# Generated at 2022-06-13 08:21:54.425718
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import mock
    import tempfile

    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    def _write_include(filename, content):
        fd, path = tempfile.mkstemp()
        os.write(fd, content)
        os.close(fd)
        return path

    def _mock_return(text):
        return text

    tqm = TaskQueueManager(inventory=mock.MagicMock(), variable_manager=mock.MagicMock())
    include_file = tempfile.mkdtemp()
    value = 'value'
    host = mock.MagicMock()
    host.name = 'host.example.com'
    loader = mock.MagicMock()
    loader.get_basedir.return_value

# Generated at 2022-06-13 08:22:03.403939
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    module_results = [{'include': 'test.yml'}, {'include': 'test.yml'}]
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=DataLoader()))
    variable_manager.extra_vars = dict(
        included=module_results
    )
    variable_manager.options_vars = dict()

    loader = DataLoader()

# Generated at 2022-06-13 08:22:17.037767
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook.base
    import ansible.vars.manager

    class TestIterator(ansible.playbook.base.BasePlay):
        _basedir = u"/home/username/ansible"

    test_iterator = TestIterator()
    test_iterator._play = ansible.playbook.base.Play()
    test_iterator._play.name = "test_iterator play"

    test_res = ansible.playbook.base.TaskResult()
    test_task = ansible.playbook.task.Task()
    test_task._uuid = u"36b67d2b-9de9-48b2-acd0-ab71cfaec27b"
    test_res._task = test_task

    test_res._host = ansible.inventory.host.Host(u"hostname")

# Generated at 2022-06-13 08:22:32.305544
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # mock data
    task_vars = {
        'ansible_search_path': '/path/to/roles/to/include',
    }
    class Role:
        def __init__(self, role_path):
            self._role_path = role_path
    class Task:
        def __init__(self, uuid):
            self._parent = None
            self._uuid = uuid
        def __repr__(self):
            return "Task(%s)" % self._uuid
        def copy(self):
            # no need to copy, just pretend
            return self
    class PlayBook:
        def __init__(self):
            pass
    class Host:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self

# Generated at 2022-06-13 08:22:39.932219
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    task_args = dict(
        _raw_params='/path/to/include.yml',
        _role=None,
        action='include_tasks',
        delegate_to='{{ inventory_hostname }}',
        delegate_facts=True,
        loop='{{ ansible_devices }}',
        loop_control=dict(
            label='{{ ansible_device_id }}',
        ),
    )
    task = TaskInclude(task_args)
    # identity

# Generated at 2022-06-13 08:23:22.768779
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.plugins.callback import default
    from ansible.vars.manager import VariableManager
    import ansible.constants as C


# Generated at 2022-06-13 08:23:30.137379
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    test_IncludedFile = IncludedFile(filename="test1", args="args1", vars="vars1", task="task1")
    test_IncludedFile2 = IncludedFile(filename="test1", args="args1", vars="vars1", task="task1")

    assert(test_IncludedFile.__eq__(test_IncludedFile) == False)
    assert(test_IncludedFile.__eq__(test_IncludedFile2) == True)

# Generated at 2022-06-13 08:23:40.814899
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from six import iteritems

    # import the class we want to test
    from ansible.playbook.included_file import IncludedFile

    # required variables to init the class
    filename = 'test_filename'
    args = dict()
    vars = dict()

    # create a class instance
    inc_file = IncludedFile(filename, args, vars)

    # create a list of hosts (fixtures)
    hosts = [ 'host1', 'host2', 'host3', 'host4' ]

    # create a list of results (fixtures)

# Generated at 2022-06-13 08:23:48.785074
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import time
    import uuid

    task_1 = TaskInclude()
    task_1._uuid = str(uuid.uuid4())
    task_1._parent = task_1
    task_1._parent._uuid = str(uuid.uuid4())
    task_1._parent._parent = task_1._parent

    time.sleep(0.1)

    task_2 = task_1

    time.sleep(0.1)

    task_3 = TaskInclude()
    task_3._uuid = task_1._uuid
    task_3._parent = task_1
    task_3._parent._uuid = task_1._parent._uuid
    task_3._parent._parent = task_1._parent

    time.sleep(0.1)

    task_4 = TaskIn

# Generated at 2022-06-13 08:23:53.318130
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json

    import pytest

    if pytest is None:
        print("pytest is not installed")
        sys.exit(1)

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ddt import ddt, data

    @ddt
    @data('test_playbook.yaml')
    def test_include_file_record(playbook_file):
        with open(playbook_file) as f:
            test_playbook = f.read()
            test_playbook = json.loads(test_playbook)

        loader = DataLoader()
       

# Generated at 2022-06-13 08:24:09.461411
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.host import Host

    loader = FakeVarsPluginLoader()
    templar = Templar(loader=loader,
                      variables={'ansible_search_path': ['some/search/path'],
                                 'role': 'some_role'}
    )
    variable_manager = VariableManager()
    host = Host(name='some_host')
    host.set_variable_manager(variable_manager)
    iterator = FakePlayIterator()


# Generated at 2022-06-13 08:24:20.852503
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult

    # Args used: were used (but will not be used for testing)
    iterator = None
    loader = None
    variable_manager = None

    # Some valid results

# Generated at 2022-06-13 08:24:31.885582
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    file1 = IncludedFile('/path/to/file.yml', args={'foo': 'bar'}, vars={'meh': 'meh'}, task=None)
    file2 = IncludedFile('/path/to/file.yml', args={'foo': 'bar'}, vars={'meh': 'meh'}, task=None)
    assert file1 == file2
    assert file1 != 'meh'

    file3 = IncludedFile('/path/to/other_file.yml', args={'foo': 'bar'}, vars={'meh': 'meh'}, task=None)
    assert file1 != file3


# Generated at 2022-06-13 08:24:41.281820
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import sys
    import copy
    # Create temporary copies of the test class
    x = IncludedFile('a', 'b', 'c', 'd')
    y = copy.copy(x)
    z = IncludedFile('a', 'b', 'c', 'd')
    z_orig = copy.copy(z)
    z_orig.add_host('e')
    z.add_host('f')

    # Test equal and non-equal objects
    assert x == y, "Failed to test __eq__()"
    assert x != z, "Failed to test __eq__()"
    assert x != z_orig, "Failed to test __eq__()"
    assert z_orig != z, "Failed to test __eq__()"

    # Print success message

# Generated at 2022-06-13 08:24:49.684492
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.six import StringIO

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins import loader as plugin_loader

    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()
    variable_manager.extra_vars = play_context.environment().get_vars

# Generated at 2022-06-13 08:25:22.443291
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')

# Generated at 2022-06-13 08:25:35.439690
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader, variable_manager, host_list=['localhost'])
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 08:25:36.885910
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass


# Generated at 2022-06-13 08:25:46.388606
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    import ansible.playbook.included_file
    import ansible.playbook.role
    import ansible.playbook.play
    import ansible.playbook.play_context
    import ansible.inventory
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.parsing.dataloader
    import ansible.template
    import ansible.vars
    import ansible.vars.manager
    import ansible.vars.hostvars

    def mockansible_vars_hostvars_get_vars(self, play, host, task):
        return {}

    ansible.vars.hostvars.HostVars.get_vars = mockansible_vars_hostvars_get_vars

# Generated at 2022-06-13 08:25:59.174738
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.handler import Handler
    from ansible.playbook.task.include import TaskInclude


# Generated at 2022-06-13 08:26:05.256955
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.plugins.loader import lookup_loader
    import ansible.playbook.play
    import jinja2

    # We'll use the lookup plugin 'setfile' to tell us the results
    # of this test.
    assert 'setfile' in lookup_loader
    setfile = lookup_loader.get('setfile')
    setfile.reset()

    display = Display()

    loader = jinja2.FileSystemLoader('.')
    env = jinja2.Environment(loader=loader)

    # Create the structure we expect
    play_ds = dict(
        name='test',
        hosts=['fake1', 'fake2'],
        tasks=[
            dict(
                include='fake.yml',
                loop='{{ list_of_includes }}'
            )
        ]
    )

# Generated at 2022-06-13 08:26:16.057190
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook.play

    fake_play = ansible.playbook.play.Play()

# Generated at 2022-06-13 08:26:24.033250
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Play
    from ansible.playbook.play import Play as PlayObj
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import action_loader, lookup_loader

# Generated at 2022-06-13 08:26:36.979359
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    #setup
    if1 = IncludedFile(r'C:\Ansible\roles\vmctl\tasks\main.yaml', {'x': '2', 'y': '3'}, {'x': '2', 'y': '3'}, None)
    if2 = IncludedFile(r'C:\Ansible\roles\vmctl\tasks\main.yaml', {'y': '3', 'x': '2'}, {'x': '2', 'y': '3'}, None)
    if3 = IncludedFile(r'C:\Ansible\roles\vmctl\tasks\main.yaml', {'y': '3'}, {'x': '2', 'y': '3'}, None)

    #test
    assert if1 == if2
    assert if1 != if3
   

# Generated at 2022-06-13 08:26:47.619908
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''Test if process_include_results correctly process include_results with ansible_loop
    '''
    # Prepare test data with ansible_loop=["value1","value2"]

# Generated at 2022-06-13 08:27:36.237412
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # test file
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[os.environ['INVENTORY']])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = {}
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:27:50.133683
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class Task:
        def __init__(self, action='include_tasks'):
            self.action = action
            self.loop = False
        def get_search_path(self):
            return ['/var/tmp']
        def _parent(self):
            return self
        def copy(self):
            return Task(action='include_role')

    class Iterator:
        def __init__(self):
            self._play = 1

    class Host:
        def __init__(self, name):
            self.name = name

    class TaskResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    import yaml
    from io import StringIO

# Generated at 2022-06-13 08:27:59.772261
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import json
    import tempfile
    import unittest
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class MyVarsModule(MutableMapping):

        def __init__(self):
            self._d = dict()

        def __getitem__(self, item):
            return self._d[item]

        def __setitem__(self, key, value):
            self._d[key] = value


# Generated at 2022-06-13 08:28:11.639104
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    current_dir = os.path.dirname(os.path.realpath(__file__))
    loader = DataLoader()
    variable_manager = VariableManager()

    all_hosts_inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='')
    all_hosts_group = all_hosts_inventory.get_group('all')
    all_hosts_group.add_host(all_hosts_inventory.get_host('host1'))
    all_hosts_

# Generated at 2022-06-13 08:28:25.663076
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # Setting variable ansible_search_path
    ansible_search_path = ['/home/ansible']
    # Setting variable hostvars
    hostvars = {}
    # Listing content of variable ansible_search_path
    display.debug("ansible_search_path: %s" % ansible_search_path)
    # Listing content of variable hostvars

# Generated at 2022-06-13 08:28:34.951638
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task_include import load_include_tasks
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import os

    basedir = os.path.dirname(__file__)
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=[os.path.join(basedir, 'test_includedfile_inventory')])
    play_context = PlayContext()


# Generated at 2022-06-13 08:28:46.235947
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:28:51.879278
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class MyResult:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

    results = [MyResult('host1', 'task1', {'include': 'filename1', 'include_args': {'k1': 'v1', 'k2': 'v2'}, 'ansible_loop_var': 'loop_var1'})]

    class MyPlay:
        name = 'myplay'

    class MyTask:
        action = 'task1'
        loop = False
        no_log = False

        def __init__(self, uuid, parent):
            self._uuid = uuid
            self._parent = parent

            self.FROM_ARGS = []

            self._from_files = {}


# Generated at 2022-06-13 08:28:58.754040
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.play_iterator import PlayIterator

    playbook_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test_data', 'playbooks', 'include_dir_with_omit.yml')
    playbook = DataLoader().load_from_file(playbook_path)
    vm = VariableManager()
    pi = PlayIterator(playbook, vm)
    t1 = Task()
    t2 = Task()

# Generated at 2022-06-13 08:29:06.194085
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task

    # initialize task and results
    task = Task()
    task.action = 'include_tasks'
    results = list()

    results.append(dict(
        _host='host1',
        _task=task,
        _result=dict(
            ansible_loop=False,
            ansible_index_var=None,
            ansible_loop_var=None,
            include='test1.yml'
        )
    ))
    results.append(dict(
        _host='host1',
        _task=task,
        _result=dict(
            ansible_loop=False,
            ansible_index_var=None,
            ansible_loop_var=None,
            include='test2.yml'
        )
    ))
    results