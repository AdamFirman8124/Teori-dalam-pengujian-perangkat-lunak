

# Generated at 2022-06-13 08:21:25.333089
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    filename = '../../examples/playbook.yml'
    with open(filename) as f:
        play = Play.load(f.read(), variable_manager=VariableManager(), loader=DataLoader())
        pb = Playbook.load(play, loader=DataLoader())
    results = pb.run()
    included_files = IncludedFile.process_include_results(results[0], InventoryManager, DataLoader, VariableManager)

# Generated at 2022-06-13 08:21:33.276674
# Unit test for method add_host of class IncludedFile
def test_IncludedFile_add_host():
    included_file = IncludedFile('filename', {}, {}, task=None)

    assert len(included_file._hosts) == 0

    included_file.add_host('host1')

    assert len(included_file._hosts) == 1
    assert included_file._hosts[0] == 'host1'

    try:
        included_file.add_host('host1')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    included_file.add_host('host2')

    assert len(included_file._hosts) == 2

    for host in ['host1', 'host2']:
        assert host in included_file._hosts


# Generated at 2022-06-13 08:21:39.442633
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    i1 = IncludedFile('/etc/ansible/roles/test_role/tasks/main.yml',
                      {'x': 'y'},
                      {'z': 'a'},
                      None)
    i2 = IncludedFile('/etc/ansible/roles/test_role/tasks/main.yml',
                      {'x': 'y'},
                      {'z': 'a'},
                      None)
    i3 = IncludedFile('/tmp/does_not_exist.yml',
                      {'x': 'y'},
                      {'z': 'a'},
                      None)

# Generated at 2022-06-13 08:21:50.776814
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Initialize a iterator
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 08:22:01.131531
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.lookup as lookup_plugins

    orig_host = plugin_loader.get_host_plugin('testhost')
    orig_task = plugin_loader.get_task_plugin('command')
    orig_task._parent = None
    orig_play_context = PlayContext()
    orig_task._play_context = orig_play_context

    results = []
    for loop_idx, host in enumerate(['testhost1','testhost2','testhost3','testhost4','testhost5']):
        for result_idx in [0,1,2,3,4]:
            result = plugin_loader.get_result_plugin()
            result._host = host

# Generated at 2022-06-13 08:22:14.949734
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

    p = Play().load({'name': 'test', 'hosts': 'localhost'}, variable_manager=VariableManager(), loader=None)
    h = Host(name='localhost')

    v = VariableManager()
    v.set_inventory(p.get_variable_manager().get_inventory())

    t = Task().load({'name': 'test1', 'action': 'include', 'args': 'test2.yml'}, variable_manager=v, loader=None)
    tr = TaskResult(host=h, task=t, task_fields=dict())
    tr._

# Generated at 2022-06-13 08:22:26.671217
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # This test case is based on the testing data obtained during execution of the follow test cases of test_playbooks.py
    #  test_role_defaults
    #  test_role_vars
    #  test_playbook_import_playbook
    #  test_playbook_import_role
    #  test_playbook_import_tasks
    #  test_playbook_include_tasks
    #  test_playbook_vars_files
    #  test_playbook_vault_vars_files

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

# Generated at 2022-06-13 08:22:39.350166
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    block1 = Block()
    task1 = Task()
    task2 = Task()

    block1._uuid = 'block1_uuid'
    task1._uuid = 'task1_uuid'
    task2._uuid = 'task2_uuid'

    block1.add_task(task1)
    block1.add_task(task2)
    task1.load(dict(include='1.yml', vars='a=1'))
    task2.load(dict(include='2.yml', vars='a=2'))

    play1 = Play()
    var_manager1

# Generated at 2022-06-13 08:22:40.524284
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # IncludeFile class was tested in this test
    pass

# Generated at 2022-06-13 08:22:54.033372
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:23:12.420933
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # pylint: disable=unused-variable

    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    hosts = ['127.0.0.1']
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)

    # For now we need to create them manually
    variable_manager.set

# Generated at 2022-06-13 08:23:24.033052
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # prepare include result
    result_list = [{'include': './../../test2.yml'}, {'include': './../../test3.yml'}]
    result = {u'results': result_list}
    # prepare mock iterator
    class MockPlay:
        def __init__(self):
            self._play = self
            self._playbook = None
        @property
        def play(self):
            return self._play

    class MockPlayIterator:
        def __init__(self):
            self._play = MockPlay()
            self._playbook = None
        @property
        def play(self):
            return self._play

    # prepare mock loader
    class MockLoader:
        def __init__(self):
            self.base_dir = 'base dir'

# Generated at 2022-06-13 08:23:35.697521
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar

    # mock the objects for the IncludedFile.process_include_results method
    # runtime
    loader = action_loader
    play_context = PlayContext()
    iterator = None
    # runtime.task_result
    res = TaskResult(host=Host(name='127.0.0.1'), task=Task())
    res._host = Host(name='127.0.0.1')
    res._task = Task()
    res._host.set_variable_manager(variable_manager=None)

# Generated at 2022-06-13 08:23:45.346103
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    pass
    #TODO: fix this test
    # from ansible.executor.task_queue_manager import TaskQueueManager
    # from ansible.inventory.manager import InventoryManager
    # from ansible.parsing.dataloader import DataLoader
    # from ansible.playbook.play import Play
    # from ansible.plugins import callback_loader
    # from ansible.vars.manager import VariableManager
    #
    # loader = DataLoader()
    #
    #
    # class Options(object):
    #     def __init__(self):
    #         self.become_method = 'sudo'
    #         self.become_user = 'root'
    #         self.connection = 'local'
    #         self.host_key_checking = False
    #         self.listhosts =

# Generated at 2022-06-13 08:23:56.050380
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class AnsibleTask:
        def __init__(self, uuid, parent):
            self._uuid = uuid
            self._parent = parent

    class AnsibleHost:
        pass

    class AnsibleIterator:
        def __init__(self, play):
            self._play = play

    class AnsibleLoader:
        def __init__(self, basedir):
            self._basedir = basedir

    class AnsibleVariableManager:
        def __init__(self, play, host, task):
            self._play = play
            self._host = host
            self._task = task

        def get_vars(self, play=None, host=None, task=None):
            if self._play == play and self._host == host and self._task == task:
                return self


# Generated at 2022-06-13 08:24:12.143069
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.module_utils.common.collections import ImmutableDict
    import ansible.plugins.loader as plugin_loader
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.target import Target
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:24:24.465609
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Initialize class
    inc_file = IncludedFile("", "", "", "")

    # Prepare empty lists
    results = []
    included_files = []

    # Prepare test data
    file1 = "/etc/ansible/test.yml"
    file2 = "/etc/ansible/test1.yml"

    # Test for two same results
    result = AnsibleResult(host="host1", task="task1", result={"include": file1})
    results.append(result)

    result = AnsibleResult(host="host1", task="task1", result={"include": file1})
    results.append(result)

    results2 = inc_file.process_include_results(results, "", "", "")

# Generated at 2022-06-13 08:24:33.695557
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Right order
    filename = 'file'
    args = 'args'
    vars = 'vars'
    task = 'task'

    inc_file_1 = IncludedFile(filename, args, vars, task)
    inc_file_2 = IncludedFile(filename, args, vars, task)

    assert(inc_file_1 == inc_file_2)

    # Reverse order
    inc_file_1 = IncludedFile(filename, args, vars, task)
    inc_file_2 = IncludedFile(filename, args, vars, task)

    assert(inc_file_2 == inc_file_1)

    # Different keys
    inc_file_1 = IncludedFile('', args, vars, task)
    inc_file_2 = IncludedFile(filename, args, vars, task)


# Generated at 2022-06-13 08:24:42.521208
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    ################################################################
    # Test case 1
    ################################################################
    # 1.1 Prepare environment

# Generated at 2022-06-13 08:24:47.492214
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import unittest

    class TestIncludedFile(unittest.TestCase):

        def test_process_include_results(self):
            results = list()
            class MyResult(object):
                def __init__(self, host, task, result):
                    self._host = host
                    self.task = task
                    self.result = result
                    results.append(self)

            class MyTask(object):
                def __init__(self, action, loop=False, no_log=False, args=None):
                    self.action = action
                    self.loop = loop
                    self.no_log = no_log
                    self.args = args or {}

            class MyIterator(object):
                def __init__(self, play):
                    self._play = play


# Generated at 2022-06-13 08:25:26.046958
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableModule
    from ansible.module_utils.six import iteritems
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.plugins.loader import action_loader

    hosts = [
        Host(name="127.0.0.1"),
        Host(name="127.0.0.2"),
        Host(name="127.0.0.3"),
        Host(name="127.0.0.4")
    ]

    group = Group(name="test_group")


# Generated at 2022-06-13 08:25:39.505052
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    my_loader = plugin_loader.find_plugin(None, ["./test/units/modules"])
    inventory = InventoryManager(['127.0.0.1'], loader=my_loader)
    variable_manager = VariableManager(loader=my_loader, inventory=inventory)

    results = []

# Generated at 2022-06-13 08:25:51.125775
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import lookup_loader, filter_loader, module_loader
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.loader = loader
    inventory_manager = InventoryManager(loader=loader, sources=['/dev/null'])
    variable_manager.set_inventory(inventory_manager)
    my_host = Host()
    my_host.name = 'localhost'

    my_group = Group()

# Generated at 2022-06-13 08:26:03.265378
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # setup the objects needed to call the process_include_results method
    play = Play().load({u'name': u'Common',
                        u'hosts': u'localhost',
                        u'roles': []}, variable_manager={}, loader=None)
    iterator = play.get_iterator()
    loader = None
    variable_manager = {}

    # simple task where include_file is a string
    include_file = [u'/home/test1']
    task1_result = {u'include_args': {},
                    u'include': include_file}
    task1_result_obj = TaskResult(host=None, task=Task(), result=task1_result)

# Generated at 2022-06-13 08:26:13.306283
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    #Create an empty list
    results = []

    #Create an empty dictionary
    args = {}

    #Create an empty dictionary
    variable_manager = {}

    #Create an empty dictionary
    play = {}

    #Create an empty dictionary
    host = {}

    #Create an empty iterator
    iterator = {}

    #Create an empty loader
    loader = {}

    #Create an empty task
    task = {}

    #Include dictionary of first result
    result1 = {}
    result1['include'] = 'include_first.yml'

    #Include dictionary of second result
    result2 = {}
    result2['include'] = 'include_second.yml'

    #Include dictionary of third result
    result3 = {}
    result3['include'] = 'include_third.yml'

    #Include dictionary of fourth result

# Generated at 2022-06-13 08:26:27.745997
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manger import TaskQueueManager
    from ansible.executor.stats import AggregateStats
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='')
    all_hosts = inventory.get_hosts()
    test_host = all_hosts[0]


# Generated at 2022-06-13 08:26:39.934758
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import random
    random.seed(100)
    results = []
    for i in range(100):
        result = FakeResult()
        result._host = random.randint(0, 3)
        result._task = random.randint(0, 3)
        result._result = { 'include': random.randint(0, 9), 'include_args': { 'one': random.randint(0, 9) }}
        results.append(result)
    included_files = IncludedFile.process_include_results(results, None, None, None)
    #print(included_files)
    #[1 (args={'one': 5} vars={}): [2], 0 (args={'one': 1} vars={}): [3], 2 (args={'one': 4} vars={}): [2], 4 (args

# Generated at 2022-06-13 08:26:48.258290
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = "/etc/ansible/roles/role1/tasks/main.yaml"
    filename2 = "/etc/ansible/roles/role1/tasks/main2.yaml"

    # Different file, same args and vars
    task = None
    include_file1 = IncludedFile(filename, {}, {}, task)
    include_file2 = IncludedFile(filename2, {}, {}, task)
    assert include_file1 != include_file2

    # Same file, different args
    include_file2 = IncludedFile(filename, {"arg_key": "arg_value"}, {}, task)
    assert include_file1 != include_file2

    # Same file, same args, different vars
    include_file2 = IncludedFile(filename, {}, {"var_key": "var_value"}, task)


# Generated at 2022-06-13 08:26:59.217648
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Setup
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)

    # Mock objects
    class MockIterator:
        _play = None

    class MockPlay:
        pass

    class MockHost:
        pass

    class MockTask:
        def __init__(self):
            self._uuid = 'Task_uuid'
            self._parent = MockIncludeTask()

    class MockIncludeTask:
        def __init__(self):
            self._uuid = 'IncludeTask_uuid'

# Generated at 2022-06-13 08:27:08.768206
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile('a', 'b', {'c': 'd'}, 'e')
    a2 = IncludedFile('a', 'b', {'c': 'd'}, 'e')
    b = IncludedFile('a', 'b', {'c': 'd'}, 'z')
    c = IncludedFile('a', 'b', {'c': 'z'}, 'e')
    d = IncludedFile('a', 'z', {'c': 'd'}, 'e')
    e = IncludedFile('z', 'b', {'c': 'd'}, 'e')

    assert a == a
    assert a == a2
    assert not a == b
    assert not a == c
    assert not a == d
    assert not a == e


# Generated at 2022-06-13 08:28:11.373191
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    # Create two instances of task_include.TaskInclude
    # test_task_include1
    test_task_include1 = TaskInclude(play=None, play_ds=None, play_basedir="play_basedir", basedir='basedir', play_context=None,
                                     task_include=None, role=None, task_vars=None, task_ds=None, parent_block=None,
                                     role_params=None, loader=None, shared_loader_obj=None, variable_manager=None)
    test_task_include1._parent = None
    test_task_include1._task = None
    test_task_include1._ds = None
    test_task_include1._uuid = "test_task_include1"
    test_task_include1.action = "include"
    test

# Generated at 2022-06-13 08:28:25.455792
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    
    """
    TaskInclude Object _ansible_item_result "results"
    TaskInclude Object _ansible_item_result ["ansible_item_result"]
    IncludeRole Object _ansible_item_result "results" 
    IncludeRole Object _ansible_item_result ["ansible_item_result"]

    """
    
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.vars.manager
    import ansible.parsing.dataloader
    import ansible.executor.task_result
    
    loader = ansible.parsing.dataloader.DataLoader()
    play_context = ansible.playbook.play_context.PlayContext()

# Generated at 2022-06-13 08:28:36.678290
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader, lookup_loader, filter_loader
    from ansible.template import Templar
    from ansible.galaxy import Galaxy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.errors import AnsibleError
    from ansible.utils.display import Display
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C

    display = Display()
    loader = DataLoader()

# Generated at 2022-06-13 08:28:47.388836
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import utils


# Generated at 2022-06-13 08:28:59.480637
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 08:29:10.505053
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import imp
    import os
    import sys
    import uuid

    from ansible.errors import AnsibleParserError, AnsibleUndefinedVariable
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.callback import CallbackBase

    class CallbackModule(CallbackBase):
        def __init__(self):
            super(CallbackModule, self).__init__()


# Generated at 2022-06-13 08:29:18.398857
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    # initialize some mocks
    class Host: pass
    class Task:
        def __init__(self, action="", loop=None, parent=None, role=None):
            self._uuid = "unique_id"
            self.action = action
            self.loop = loop
            self._parent = parent
            self._role = role

    class LoopResult:
        def __init__(self, include, results=None):
            self.results = results or [LoopResult(include)]
            self.include = include
            self.ansible_loop_var = 'item'

        def __iter__(self):
            return self.results.__iter__()

    class Play:
        def __init__(self):
            self._ds = dict()


# Generated at 2022-06-13 08:29:32.474889
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:29:40.168378
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    from ansible.vars.manager import VariableManager

    fake_loader = plugin_loader.get(None, '_fake_', 'fake_loader')
    var_manager = VariableManager()

    task_included_file = IncludedFile('/a/b/c', {}, {}, None)
    task_included_file2 = IncludedFile('/a/b/c', {}, {}, None)
    assert task_included_file == task_included_file2
    task_included_file3 = IncludedFile('/a/b/d', {}, {}, None)
    task_included_file4 = IncludedFile('/a/b/c', {'a': 'b'}, {}, None)

# Generated at 2022-06-13 08:29:42.521054
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    result = IncludedFile("filename", "args", "vars", "task")
    assert result == IncludedFile("filename", "args", "vars", "task")