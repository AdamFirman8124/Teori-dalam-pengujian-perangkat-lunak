

# Generated at 2022-06-13 08:21:12.339618
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'is_vm': True, 'key1': 'value1'}
    variable_manager.set_available_variables(loader.load_from_file('/usr/local/etc/ansible/host_vars/host1', cache=False))


# Generated at 2022-06-13 08:21:25.203606
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    class Play:
        pass

    play = Play()

    class Host:
        name = 'localhost'

    results = []

# Generated at 2022-06-13 08:21:34.264445
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create a TaskQueueManager instance
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
    )

    # Create fake results
    results = list()
    # First result
    res = tqm._create_result(host=object(), task=object(), return_data=dict(ansible_loop=object(), include='include_file', include_args={}))
    results.append(res)
    # Second result

# Generated at 2022-06-13 08:21:44.075504
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    import yaml
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    filesta = "task_include_file.yml"
    filestb = "task_include_file2.yml"
    filedata = dict(
        connection='local',
        hosts='localhost',
    )

    playbook = Play.load(filedata, variable_manager=VariableManager(), loader=yaml.Loader)
    block = Block()
    block.parent_block = playbook
    task = Task()
    task.action = 'include'
    task.loop = '{{ my_list }}'
    task

# Generated at 2022-06-13 08:21:53.554909
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test __eq__ of class IncludedFile
    """
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude

    pl = Play().load({'name': 'unittest'})
    t1 = Task().load({'action': 'include', 'name': 'unittest'})
    h1 = Handler().load({'action': 'include', 'name': 'unittest'})
    pl.add_task(t1)
    t1.add_task(h1)
    t2 = Task()
    pl.add_task(t2)

    # included_file equals to itself
    # condition 1: self._filename == self._filename
    # condition

# Generated at 2022-06-13 08:22:02.894590
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # test IncludedFile([filename,args,vars,task])
    class Task():
        def __init__(self, uuid):
            self._uuid = uuid
            self._parent = None
    class Playbook():
        def __init__(self, uuid):
            self._uuid = uuid
    class VariableManager():
        def get_vars(self, play=None, host=None, task=None):
            return {}

    a = Task('1')
    b = Task('2')
    p = Playbook('3')
    a._parent = b
    b._parent = p
    v = VariableManager()

    inc1 = IncludedFile('test_file', {}, {}, a)
    inc2 = IncludedFile('test_file', {}, {}, b)

# Generated at 2022-06-13 08:22:15.644899
# Unit test for method __eq__ of class IncludedFile

# Generated at 2022-06-13 08:22:27.385931
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    import os

    class Options(object):
        """
        Options class dummy for tests
        """
        verbosity = 1
        listtags = False
        listtasks = False
        listhosts = False
        syntax = False
        connection = 'ssh'  # Need a connection type "smart" or "ssh"
        module_path = None
        forks = 10
        remote_user = 'root'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None

# Generated at 2022-06-13 08:22:39.786369
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    class Options:
        connection = None
        module_path = None
        forks = 100
        remote_user = 'root'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = None
        become_method = None
        become_user = None
        verbosity = 5
        check = False
        listhosts = None
        listtasks = None

# Generated at 2022-06-13 08:22:41.296535
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # TODO
    pass

# Generated at 2022-06-13 08:23:04.032018
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # create a fake iterator
    class FakeIterator:
        _play = None

    # create a fake loader
    class FakeLoader:
        # fake the method get_basedir, it return a path
        def get_basedir(self):
            return '.'

        # create a fake path_dwim, it return path
        def path_dwim(self, path):
            return path

    # create a fake variable_manager, it return a dict
    class FakeVariableManager:
        # fake the method get_vars, it return a dict
        def get_vars(self, play=None, host=None, task=None):
            return {'some':'var'}


    # create a include result

# Generated at 2022-06-13 08:23:15.086382
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    p = Play()
    p._role_name = "role_1"
    t = Task()
    t._parent = p
    t._uuid = "task_1"
    p._loader = "loader_1"

    f1 = IncludedFile(filename="foo", args={"bar": "baz"}, vars={"qux": "quux"}, task=t)
    f2 = IncludedFile(filename="foo", args={"bar": "baz"}, vars={"qux": "quux"}, task=t)

    p2 = Play()
    p2._role_name = "role_2"
    t2 = Task()
    t2._parent = p2

# Generated at 2022-06-13 08:23:23.008415
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.parsing.loader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import Task

# Generated at 2022-06-13 08:23:34.463402
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult as CollectorTaskResult
    from ansible.executor.task_executor import get_loop_items
    from ansible.utils.vars import combine_vars

    # pylint: disable=abstract-class-instantiated
    from ansible.vars.manager import VariableManager
    from ansible.executor.vars_promoter import VarsPromoter

    from ansible.vars.unsafe_proxy import UnsafeProxy

    # pylint: disable=unused-argument
    class FakePlaybook(object):
        pass

    class FakeTaskInclude(TaskInclude):
        def get_search_path(self):
            return []

    class FakeVariableMgr(VariableManager):
        def __init__(self):
            pass


# Generated at 2022-06-13 08:23:43.112858
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from .__init__ import load_fixture
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    results = load_fixture('test_include')
    results = TaskQueueManager._unpack_results(results, 'testhost', None)

    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = dict()


# Generated at 2022-06-13 08:23:44.511398
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    assert IncludedFile('filename', {}, {}, 'task') == IncludedFile('filename', {}, {}, 'task')


# Generated at 2022-06-13 08:23:55.803124
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Unit test for method __eq__ of class IncludedFile
    """
    # NOTE: Not all properties of IncludedFile are available here
    # and thus a full comparison of objects is not possible
    host1 = 'host1'
    host2 = 'host2'
    filename1 = 'file1'
    filename2 = 'file2'
    args1 = 'args1'
    args2 = 'args2'
    vars1 = 'vars1'
    vars2 = 'vars2'

    # Full comparison of objects
    # Objects are equal (Objects with differnet refs)
    inc_file0 = IncludedFile(filename1, args1, vars1, 'task1')
    inc_file0.add_host(host1)

# Generated at 2022-06-13 08:24:05.081381
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile("a", None, None, None)
    b = IncludedFile("b", None, None, None)
    c = IncludedFile("a", None, None, None)
    if not a == b:
        print("method __eq__ of class IncludedFile failed: 'a' == 'b'")
    if not a == c:
        print("method __eq__ of class IncludedFile failed: 'a' == 'c'")
    if a == b == c:
        print("method __eq__ of class IncludedFile failed: a == b == c")

# Generated at 2022-06-13 08:24:15.282512
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import copy
    import textwrap

    results = []
    loader = None
    variable_manager = None
    iterator = None

    #Case 1:
    #include: stuff.yaml
    #The included file is in the tasks directory of the same role
    #The role is a dependency role
    #Results:
    #IncludedFile: stuff.yml (args={} vars={}): ['test-dependency1.example.com', 'test-dependency1.example.com', 'test-dependency1.example.com', 'test-dependency2.example.com', 'test-dependency2.example.com', 'test-dependency2.example.com', 'test-dependency1.example.com', 'test-dependency1.example.com', 'test-dependency1.example.com', 'test-dependency2

# Generated at 2022-06-13 08:24:27.257542
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.strategies import LinearStrategy
    from ansible.utils.plugin_docs import get_docstring
    from ansible.utils.vars import combine_vars
   

# Generated at 2022-06-13 08:25:03.553325
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class MyTaskInclude:
        def __init__(self):
            self._uuid = 'uuid'
            self._parent = MyPlay()

    class MyPlay:
        def __init__(self):
            self._uuid = 'another uuid'

    included_file_a = IncludedFile('filename', 'args', 'vars', MyTaskInclude())
    included_file_b = IncludedFile('filename', 'args', 'vars', MyTaskInclude())
    included_file_c = IncludedFile('other filename', 'args', 'vars', MyTaskInclude())
    included_file_d = IncludedFile('other filename', 'other args', 'vars', MyTaskInclude())
    included_file_e = IncludedFile('other filename', 'other args', 'other vars', MyTaskInclude())
    included_file

# Generated at 2022-06-13 08:25:08.584688
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.task import Task

    results = [
    ]

    included_files = IncludedFile.process_include_results(results, None, None, None)

    assert 0 == len(included_files)



# Generated at 2022-06-13 08:25:23.438433
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Obj:
        pass

    obj = Obj()
    obj.action = "include_tasks"
    obj._parent = None
    obj.loop = False
    obj._uuid = "test_playbook"
    obj.no_log = False

    obj2 = Obj()
    obj2.action = "include_tasks"
    obj2._parent = None
    obj2.loop = False
    obj2._uuid = "test_playbook2"
    obj2.no_log = False

    obj3 = Obj()
    obj3.action = "include_tasks"
    obj3._parent = obj
    obj3.loop = False
    obj3._uuid = "test_playbook3"
    obj3.no_log = False

    obj4 = Obj()

# Generated at 2022-06-13 08:25:38.447353
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.playbook_iterator import PlaybookIterator
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    display.verbosity = 4
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext

# Generated at 2022-06-13 08:25:47.135893
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        loader = DataLoader()
        inventory = InventoryManager(loader=loader, sources=["%s/hosts" % t])
        # Create the hosts file
        with open("%s/hosts" % t, "w") as f:
            f.write("[all:vars]\n")
            f.write("ansible_connection=local\n")
            f.write

# Generated at 2022-06-13 08:25:59.886200
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
        Unit test for method process_include_results of class IncludedFile
    '''


# Generated at 2022-06-13 08:26:08.578385
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = '/tmp/file.txt'
    args = {'param1' : 'value1', 'param2' : 'value2'}
    vars = {'var1' : 'value1', 'var2' : 'value2'}
    task = 'task'
    is_role = False

    # Test equal
    file1 = IncludedFile(filename, args, vars, task, is_role)
    file2 = IncludedFile(filename, args, vars, task, is_role)
    assert file1 == file2

    # Test the attributes of class IncludedFile
    for attribute in ('_filename', '_args', '_vars', '_task', '_hosts', '_is_role'):
        assert getattr(file1, attribute) == getattr(file2, attribute)

    # Test inequal


# Generated at 2022-06-13 08:26:19.133488
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop, mock_unfrackpath_noop_with_warning
    from units.mock.plugins import mock_action_plugins, mock_lookup_plugins
    from units.mock.vars import MockVarsModule

    loader = DictDataLoader({})
    mock_unfrackpath_noop(loader, 'ansible.utils.display')
    mock_unfrackpath_noop(loader, 'ansible.plugins.loader')
    mock_unfrackpath_noop(loader, 'ansible.plugins.action')
    mock_unfrackpath_noop(loader, 'ansible.plugins.lookup')

# Generated at 2022-06-13 08:26:25.654066
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    all_vars = variable_manager.get_vars(play=play)

    results = []

# Generated at 2022-06-13 08:26:38.465628
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:27:30.415146
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Creating example data
    results = [0, [1, 2], 3, [4, 5, 6]]
    iterator = [7, 8]
    loader = [9, 10]
    variable_manager = [11, 12]

    # Execute the method
    included_files = IncludedFile.process_include_results(results, iterator, loader, variable_manager)

    # Check results
    assert included_files == 0


# Generated at 2022-06-13 08:27:44.034855
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # pylint: disable=too-many-locals
    task_executor_class = 'ansible.executor.task_executor.TaskExecutor'
    connection_class = 'ansible.connection.accelerate.Accelerate'
    play_context_class = 'ansible.playbook.play_context.PlayContext'
    display_class = 'ansible.utils.display.Display'
    loader_class = 'ansible.parsing.dataloader.DataLoader'
    variable_manager_class = 'ansible.vars.variable_manager.VariableManager'
    inventory_class = 'ansible.inventory.manager.InventoryManager'

    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 08:27:54.129387
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved

    loader = DataLoader()

    play_context = PlayContext()
    play

# Generated at 2022-06-13 08:28:02.590269
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    Unit test for method process_include_results of class IncludedFile
    '''
    import os
    import shutil
    import tempfile
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.plugins.loader import get_all_plugin_loaders

    # TODO: Replace with call

# Generated at 2022-06-13 08:28:11.186031
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Case 1: success
    r1 = IncludedFile("f1", "a1", "v1", "t1")
    r2 = IncludedFile("f1", "a1", "v1", "t1")
    result = r1.__eq__(r2)
    assert result

    # Case 2: failure
    r1 = IncludedFile("f1", "a2", "v1", "t2")
    r2 = IncludedFile("f1", "a1", "v1", "t1")
    result = r1.__eq__(r2)
    assert result is False

# Generated at 2022-06-13 08:28:25.257727
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Create an empty inventory, play and task
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Hello Ansible!'))),
            dict(action=dict(module='debug', args=dict(msg='Hello play!')))
        ]
    )

# Generated at 2022-06-13 08:28:36.634171
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    task_include_1 = TaskInclude('include.yml', None, None)
    task_include_2 = TaskInclude('include.yml', None, None)
    inc_file_1 = IncludedFile('include.yml', None, None, task_include_1)
    inc_file_2 = IncludedFile('include.yml', None, None, task_include_1)
    inc_file_3 = IncludedFile('include.yml', None, None, task_include_2)
    inc_file_4 = IncludedFile('include2.yml', None, None, task_include_1)

    assert inc_file_1 == inc_file_2
    assert inc_file_2 == inc_file_1
    assert not (inc_file_1 == inc_file_3)

# Generated at 2022-06-13 08:28:47.357578
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    fake_loader = DataLoader()

    import ansible.constants as C
    C.DEFAULT_DEBUG = False

    from ansible.vars.manager import DefaultVariableManager
    fake_inventory = InventoryManager(loader = fake_loader, sources = 'localhost,')
    fake_variable_manager = VariableManager(loader = fake_loader, inventory = fake_inventory)
    fake_variable_manager._extra_vars = dict(omit='secret')

# Generated at 2022-06-13 08:28:59.481252
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from jinja2 import Template

    mock_host = "testhost"
    mock_play = Play()
    mock_play.name = "testplay"

    # A mock IncludeRole Task
    class MockIncludeRole(IncludeRole):
        def __init__(self, role_name=None, include_args=None, special_vars=None, task=None, is_role=None):
            # Use the real superclass init
            IncludeRole.__init__(self, role_name, include_args, special_vars, task)
            self.is_role = is_role


# Generated at 2022-06-13 08:29:10.516917
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_executor import TaskResult
