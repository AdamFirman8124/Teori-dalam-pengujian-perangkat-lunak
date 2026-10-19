

# Generated at 2022-06-13 08:21:11.885403
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile("file1", {}, {}, "task")
    b = IncludedFile("file1", {}, {}, "task")
    c = IncludedFile("file2", {}, {}, "task")
    d = IncludedFile("file1", {"arg1": "1"}, {}, "task")

    assert a == b
    assert a != c
    assert a != d

# Generated at 2022-06-13 08:21:18.595897
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    a = IncludedFile('a', 'a', 'a', 'a')
    b = IncludedFile('a', 'a', 'a', 'a')
    c = IncludedFile('a', 'a', 'a', 'a')
    d = IncludedFile('b', 'a', 'a', 'a')
    e = IncludedFile('a', 'b', 'a', 'a')
    f = IncludedFile('a', 'a', 'b', 'a')
    g = IncludedFile('a', 'a', 'a', 'b')
    h = IncludedFile('b', 'b', 'b', 'b')
    assert a == b
    assert c == a
    assert a != d
    assert a != e
    assert a != f
    assert a != g
    assert a != h
    assert b != d
    assert b != e
   

# Generated at 2022-06-13 08:21:29.478218
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    print("Testing class IncludedFile, method __eq__.\n")
    filename = "/tmp/test.yml"
    args = {
        "arg1": "val1",
        "arg2": "val2"
    }
    vars = {
        "var1": "val1",
        "var2": "val2"
    }
    task = None
    is_role = False
    obj1 = IncludedFile(filename, args, vars, task, is_role)
    obj2 = IncludedFile(filename, args, vars, task, is_role)
    print("Object 1: " + str(obj1))
    print("Object 2: " + str(obj2))
    print("Object 1 __eq__ Object 2? " + str(obj1.__eq__(obj2)))
    print("")


# Generated at 2022-06-13 08:21:36.525594
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    unit test for method __eq__ of class IncludedFile
    
    :return: True if the test is successful, otherwise False
    """

    test1 = TaskInclude("{}")
    test2 = TaskInclude("{}")
    
    a = IncludedFile("filename1",
                     ["arg1", "arg2"],
                     {"var1": "val1", "var2": "val2"},
                     test1)
    
    b = IncludedFile("filename1",
                     ["arg1", "arg2"],
                     {"var1": "val1", "var2": "val2"},
                     test1)
    
    c = IncludedFile("filename3",
                     ["arg1", "arg2"],
                     {"var1": "val1", "var2": "val2"},
                     test2)
    
    assert a

# Generated at 2022-06-13 08:21:45.704650
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    loader = DictDataLoader({'roles/common': 'common content', 'etc/motd': 'hello foo'})
    fake_play = dict(name='mockplay')
    fake_tqm = FakeTQM(fake_play)
    fake_itr = FakeIterator(fake_tqm, fake_play)
    fake_var_mgr = VariableManager(loader=loader)
    fake_host = dict(name='thehost')

    fake_task = Task()
    fake_task.name = 'fake'
    fake_task._role = DictObj(dict(role_path='roles/common'))
    fake_

# Generated at 2022-06-13 08:21:54.704031
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:22:03.558245
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class DummyTask:
        def __init__(self, action, loop, _uuid, _parent, _role, filename, search_path):
            self.action = action
            self.loop = loop
            self._uuid = _uuid
            self._parent = _parent
            self._role = _role
            self.filename = filename
            self._from_files = {}
            self.search_path = search_path
            self.FROM_ARGS = ['delegate_to', 'local_action', 'loop_control']

        def get_search_path(self):
            return self.search_path

    class DummyRole:
        def __init__(self, name, _role_path):
            self.name = name
            self._role_path = _role_path


# Generated at 2022-06-13 08:22:11.993600
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    assert IncludedFile.__eq__(IncludedFile('a', 'b', 'c', 'd')) == True
    assert IncludedFile.__eq__(IncludedFile('a', 'b', 'c', 'd', 1)) == False
    assert IncludedFile.__eq__(IncludedFile('a', 'b', 'c', 'd')) == False
    assert IncludedFile.__eq__(IncludedFile('a', 'b', 'c', 'd')) == False


# Generated at 2022-06-13 08:22:19.922533
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    """
    Test if two IncludedFile objects with equals values are equals.
    """
    class TestIncludedFile(object):
        args = {}
        vars = {}
        def __init__(self, filename, task):
            self._filename = filename
            self._task = task

    class TestIncludedFile2(TestIncludedFile):
        pass

    class TestTask(object):
        parent = None
        def __init__(self, uuid):
            self._uuid = uuid

    class TestTask2(object):
        parent = None
        def __init__(self, parent, uuid):
            self._parent = parent
            self._uuid = uuid
            if parent is not None:
                self._parent._uuid = parent

    task = TestTask('1234567890')
    task2 = TestTask

# Generated at 2022-06-13 08:22:34.922792
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    import ansible.executor.task_queue_manager
    import ansible.playbook.task
    import ansible.playbook.role

    temp_filename = 'temp_filename'
    temp_args = dict()
    temp_vars = dict()

    role = ansible.playbook.role.Role()
    task = ansible.playbook.task.Task()
    task._role = role
    task._uuid = '1234-1234-1234-1234'
    task._parent = 'parent'

    minus_filename = IncludedFile(None, None, None, None)
    minus_filename._filename = None
    minus_filename._args = None
    minus_filename._vars = None

    minus_filename_args = IncludedFile(temp_filename, None, None, None)
    minus_filename_args._

# Generated at 2022-06-13 08:22:58.780545
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys

    # temporary bypass while fixing include result tests
    if sys.version_info[0] > 2:
        return

    run = IncludedFile.process_include_results

    # single host, single include
    results = [dict(
        _host=dict(name='localhost'),
        _task=dict(),
        _result=dict(
            included=dict(
                include='tasks/common.yml'
            )
        )
    )]
    assert run(results, None, None, None) == [
        # task, vars
        dict(
            _filename='tasks/common.yml',
            _args=dict(),
            _vars=dict(),
            _hosts=['localhost'],
            _task=dict(),
        )
    ]

    # single host, multiple includes

# Generated at 2022-06-13 08:23:07.179526
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ta = TaskInclude()
    ta._args = {'owner': 'root', 'file': 'roles/newrole/tasks/main.yml'}
    ta._parent = 'test'
    ta._role_name = 'test'
    ta._role = 'test'
    ta._role_path = 'test'
    ta._from_files = {'owner': 'root', 'file': 'roles/newrole/tasks/main.yml'}

    tb = TaskInclude()
    tb._args = {'owner': 'root', 'file': 'roles/newrole/tasks/main.yml'}
    tb._parent = 'test'
    tb._role_name = 'test'
    tb._role = 'test'
    tb._role_path = 'test'

# Generated at 2022-06-13 08:23:17.644652
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    import ansible.playbook
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    
    # Test classes
    class MyTask(Task):
        def __init__(self, action='noop', parent=None):
            super(MyTask, self).__init__(action, parent)
    
            # Set up test attributes
            self.action = action
            self.parent = parent
            self.loop = False

# Generated at 2022-06-13 08:23:29.916895
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    hosts = ['localhost', '127.0.0.1']

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    task = Task()
    task._uuid = '2'
    host1 = TaskResult(host='localhost', task=task, return_data={'return': 0, 'action': 'include'})

# Generated at 2022-06-13 08:23:40.613535
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    t1 = TaskInclude.load(
        dict(
            name='test',
            include='test.yml'
        ),
        load_from_file=False,
    )
    t1._parent = None
    f1 = IncludedFile('test.yml', dict(), dict(), t1, False)

    t2 = TaskInclude.load(
        dict(
            name='test',
            include='test.yml'
        ),
        load_from_file=False,
    )
    t2._parent = None
    f2 = IncludedFile('test.yml', dict(), dict(), t1, False)

    t3 = TaskInclude.load(
        dict(
            name='test2',
            include='test.yml'
        ),
        load_from_file=False,
    )


# Generated at 2022-06-13 08:23:48.669158
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
  incFile1 = IncludedFile('file1', 'args1', 'vars1', 'task1', 'isrole1')
  incFile2 = IncludedFile('file1', 'args1', 'vars1', 'task1', 'isrole1')
  incFile3 = IncludedFile('file1', 'args1', 'vars1', 'task2', 'isrole1')
  incFile4 = IncludedFile('file1', 'args1', 'vars1', 'task1', 'isrole2')
  incFile5 = IncludedFile('file1', 'args1', 'vars1', 'task1', 'isrole2')
  incFile6 = IncludedFile('file1', 'args2', 'vars1', 'task1', 'isrole1')

# Generated at 2022-06-13 08:23:58.025502
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Setup
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.utils.vars
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    play = ansible.playbook.play.Play()
    parent_task = ansible.playbook.task.Task()
    play.set_loader(ansible.parsing.dataloader.DataLoader())
    templar = Templar(loader=play.get_loader(), variables=combine_vars(play.get_variable_manager().get_vars(play=play)))

    # Check with a simple import_playbook
    task = ansible.playbook.task.Task()
    task.action = 'import_playbook'
    task

# Generated at 2022-06-13 08:24:09.656134
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources='/dev/null')
    variable_manager = VariableManager(loader=data_loader, inventory=inventory)

    play = Play()
    play._variable_manager = variable_manager
    play.basedir = '.'
    play._loader = data_loader
    play._iterator = None

    task = dict(
        action=dict(
            module='include_tasks',
            args=dict(
                _raw_params='foo.yml',
            )
        )
    )


# Generated at 2022-06-13 08:24:16.755559
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeTask:
        def __init__(self, _uuid, _parent, action, loop, no_log, _role_name=None, _from_files=None, _raw_params=None):
            self._uuid = _uuid
            self._parent = _parent
            self.action = action
            self.loop = loop
            self.no_log = no_log
            self._role_name = _role_name
            self._from_files = {} if _from_files is None else _from_files
            self._raw_params = _raw_params

        def copy(self):
            return FakeTask(self._uuid, self._parent, self.action, self.loop, self.no_log, self._role_name, self._from_files, self._raw_params)


# Generated at 2022-06-13 08:24:28.665778
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    Testing for method process_include_results of class IncludedFile
    '''
    from ansible.module_utils.six import string_types

    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    # Create play

# Generated at 2022-06-13 08:25:10.972559
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.playbook_iterator import TaskIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import filter_loader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    class MockLookupModule:
        def run(self, terms, variables=None, **kwargs):
            return '../sub/subsub/'
        def get_options(self): return {}

    lookup_loader.add_directory('./lookups')

# Generated at 2022-06-13 08:25:25.522110
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Create a fake play
    play = Play()

    # Create fake tasks
    include_task1 = TaskInclude()
    include_task1._role_name = 'role1'
    include_task1._from_files = {'handlers': 'handlers/main.yml', 'tasks': 'tasks/main.yml', 'vars': 'vars/main.yml', 'defaults': 'defaults/main.yml'}

    include_task2 = TaskInclude()
    include_task2._role_name = 'role2'
    include_task2._from_files = {'tasks': 'tasks/main.yml', 'vars': 'vars/main.yml'}

    # Create fake hosts
    host1 = Host('127.0.0.1')
    host2

# Generated at 2022-06-13 08:25:40.433792
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    loader = DictDataLoader({
        "first.yml": """
        - debug:
            msg: task 1
        - include: second.yml
        """,
        "second.yml": """
        - debug:
            msg: task 2
        """,
    })
    play = {
        'name': 'TestPlay',
        'playbook_dir': '/tmp',
        'hosts': ['first'],
        'vars': {},
        'tasks': [],
    }
    host1 = FakeHost(name='first')
    tqm = FakeTaskQueueManager(loader, host1)
    pm = FakePlaybookManager(loader, play)
    host1_vars = dict()
    host1_vars['playbook_dir'] = '/tmp'

# Generated at 2022-06-13 08:25:48.173935
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task_include import get_handler_path
    from ansible.vars import VariableManager

    module_utils_path = to_text(os.path.join(os.path.dirname(__file__), '..', 'module_utils'))


# Generated at 2022-06-13 08:26:01.068735
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    Test case for method process_include_results of class IncludedFile

    '''

    import json
    import tempfile
    import os
    import shutil

    from ansible.inventory import Inventory
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    test_base = tempfile.mkdtemp()

# Generated at 2022-06-13 08:26:09.188572
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    included_file_1 = IncludedFile('file1', {'role': 'role1'}, '', '')
    included_file_2 = IncludedFile('file1', {'role': 'role1'}, '', '')
    assert included_file_1 == included_file_2
    included_file_2 = IncludedFile('file1', {'role': 'role2'}, '', '')
    assert not included_file_1 == included_file_2
    included_file_2 = IncludedFile('file2', {'role': 'role1'}, '', '')
    assert not included_file_1 == included_file_2
    included_file_2 = IncludedFile('file1', {'role': 'role1'}, '', '', True)
    assert not included_file_1 == included_file_2

# Generated at 2022-06-13 08:26:19.222317
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Results():
        def __init__(self, filename, args, vars, parent_uuid, uuid):
            self._filename = filename
            self._args = args
            self._vars = vars
            self._task = Task()
            self._task._uuid = uuid
            self._task._parent = parent

        def __eq__(self, other):
            return (self._filename == other._filename and
                    self._args == other._args and
                    self.vars == other._vars and
                    self._task._uuid == other._task._uuid)

    class Task():
        def __init__(self):
            self.action = C.ACTION_INCLUDE_TASK
            self.loop = True

# Generated at 2022-06-13 08:26:25.710444
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Test for equality with different instance of same class
    ifh = IncludedFile('filename1', {'arg1': 'value1'}, {'var1': 'var_value1'}, 'task1')
    ih = IncludedFile('filename1', {'arg1': 'value1'}, {'var1': 'var_value1'}, 'task1')
    assert ifh.__eq__(ih)

    # Test for equality with different instance of different class
    ifh = IncludedFile('filename1', {'arg1': 'value1'}, {'var1': 'var_value1'}, 'task1')
    ih = 'different_instance'
    assert not ifh.__eq__(ih)

    # Test for inequality with different instance of same class

# Generated at 2022-06-13 08:26:38.510383
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader as plugin_loader
    import ansible.template as template
    import jinja2
    os.environ['USER'] = 'test_IncludedFile_process_include_results'
    my_loader = plugin_loader.PluginLoader( None, 'action_plugins', 'cache', 'callback_plugins',
      'connection_plugins', 'lookup_plugins', 'shell_plugins', 'strategy_plugins',
      'vars_plugins', 'filter_plugins', 'test_plugins', 'terminal_plugins',
      'inventory_plugins')
    my_loader.add_directory(os.path.join(os.path.dirname(__file__), 'fixtures', 'action_plugins'), with_subdir=True)

# Generated at 2022-06-13 08:26:49.071501
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.executor.task_result import TaskResult
    fake_results = []
    for i in range(0, 5):
        fake_results.append(TaskResult(host=None, task=None, task_fields=dict(action=''),
                                       result=dict(include='foo', include_args=dict(arg1=1, arg2=2))))
    fake_results.append(TaskResult(host=None, task=None, task_fields=dict(action=''),
                                   result=dict(include='bar', include_args=dict(arg1=1, arg2=2))))


# Generated at 2022-06-13 08:27:52.793889
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play

    loader = DataLoader()
    hosts = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = hosts.get_variable_manager()
    play_context = PlayContext()
    play_context._hostvars = hosts.get_hosts()

# Generated at 2022-06-13 08:28:01.696017
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader
    # Test case 1

# Generated at 2022-06-13 08:28:12.271448
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor import module_common as mc


# Generated at 2022-06-13 08:28:25.935986
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook.role
    import ansible.playbook.play
    import ansible.playbook.task

    # import the required modules to create an iterator
    import ansible.executor.task_queue_manager
    from ansible.inventory import Inventory
    import ansible.parsing.dataloader
    from ansible.plugins.loader import find_vars_loader

    # import the required modules for variable manager
    from ansible.vars import VariableManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

    # import the required modules for result
    from ansible.executor.task_result import TaskResult

    # module to generate a random file name
    import tempfile

    # create a temporary file to be used as the host file
    fd, host_file = temp

# Generated at 2022-06-13 08:28:39.281696
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class Host:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

        def __eq__(self, other):
            return self.name == other.name

    class Task:
        def __init__(self, uuid, parent=None):
            self._uuid = uuid
            self._parent = parent

        def __eq__(self, other):
            return self._uuid == other._uuid

    class Results:
        def __init__(self, host, task, result):
            self._host = host
            self._task = task
            self._result = result

        def __repr__(self):
            return "%s @ %s: %s" % (self._task, self._host, self._result)


# Generated at 2022-06-13 08:28:47.699741
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    # Setup initial data
    class OriginalTask:
        def __init__(self, uuid):
            self._uuid = uuid
    original_task = OriginalTask('test_uuid')

    included_file1 = IncludedFile(filename='test_filename', args='test_args', vars='test_vars', task=original_task)
    included_file2 = IncludedFile(filename='test_filename', args='test_args', vars='test_vars', task=original_task)

    # Assert initial data is correct
    assert included_file1 is not included_file2

    # Test __eq__ magic method
    assert included_file1 == included_file2


# Generated at 2022-06-13 08:28:59.712046
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook._base import CLICommand
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.hostvars import HostVarsGroup
    from ansible.vars.hostvars import HostVarsGroups

    # Create a dummy context for testing this
    # create a dummy loader
    loader

# Generated at 2022-06-13 08:29:10.683372
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    display.verbosity = 4
    vars = dict(yesterday='yesterday', today='today', tomorrow='tomorrow')
    from ansible.executor.task_result import TaskResult
    results = [TaskResult(host=dict(name='localhost'), task=dict(action='include', loop=['yesterday', 'today', 'tomorrow'], args=dict(_raw_params='test.yml')), _result=dict(ansible_loop='{{ item }}', include='test.yml', include_args=dict(role='test'), skipped=False))]
    from ansible.executor.task_iterator import TaskIterator

# Generated at 2022-06-13 08:29:18.505989
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Testing template the name of included role
    included_files = IncludedFile.process_include_results(
        [
            {
                "_host": "foo",
                "_task": {
                    "_role_name": "foo_role",
                    "action": "include_role",
                    "FROM_ARGS": [],
                    "FROM_FILES": ["tasks/main.yml"],
                    "_from_files": {},
                    "_role": "foo_role",
                },
                "_result": {
                    "include_args": {
                        "name": "{{ name }}",
                    },
                },
            },
        ],
        None,
        None,
        {
            "name": "bar_role",
        },
    )
    assert included_files[0]._filename == "bar_role"
   

# Generated at 2022-06-13 08:29:32.502327
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager

    results = []

    host = 'localhost'
    block = Block(loader=None, parent_block=None, role=None, task_include=None, use_handlers=False, always_run=False, loop=None)
    task = Task()
    task._uuid = '1'
    task._role = 'role'
    task._role_name = 'role'
    task._parent = block
    task._role_path = '.'
    task._from_files = {}
    task._terms = {}
    task._role_params = {}
    task._search_path = '.'
    task.action