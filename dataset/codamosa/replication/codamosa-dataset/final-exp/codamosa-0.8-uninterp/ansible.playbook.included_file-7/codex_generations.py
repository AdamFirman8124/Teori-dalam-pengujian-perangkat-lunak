

# Generated at 2022-06-13 08:21:10.592031
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    import ansible.constants as C

    # Load a fake play, task and dataloader to use in the test
    loader = DataLoader()

# Generated at 2022-06-13 08:21:17.895107
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({
        'orig.yml': "",
        'dir1/dir2/included.yml': "",
        'dir1/dir2/included.j2': "",
        'dir1/dir2/include_role.yml': ""})
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context._run_as_root = True

# Generated at 2022-06-13 08:21:29.055515
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:21:36.584556
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task

    # Set up some data for the test
    results = []
    results.append(TaskResult(host={'name': 'host1'},
                              task={'name': 'task1', 'action': 'include'},
                              result={'skipped': False, 'failed': False, 'rc': 0, '_ansible_parsed': True, 'include_args': {}, 'include': 'includefile.yml'}))

# Generated at 2022-06-13 08:21:47.991687
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeHost:
        pass

    class FakeTask:
        action = 'include'
        loop = False
        no_log = False

        def __init__(self, uuid, parent):
            self._uuid = uuid
            self._parent = parent

        def copy(self):
            return self

        def get_search_path(self):
            return []

    class FakePlaybook:
        pass

    class FakeIterator:
        pass

    class FakeLoader:
        def get_basedir(self):
            return '.'

        def path_dwim(self, file):
            return file

        def path_dwim_relative(self, basedir, path, file, is_role=False):
            if is_role:
                return file

            return basedir + '/' + path + '/' + file



# Generated at 2022-06-13 08:21:59.642069
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    results = [
        {
            "_host": "test",
            "_result": {
                "include": "test.yml"
            },
            "_task": Task(block=Block(parent=Block()), role=Role())
        },
        {
            "_host": "test",
            "_result": {
                "include": "test.yml"
            },
            "_task": Task(block=Block(parent=Block()), role=Role())
        }
    ]


# Generated at 2022-06-13 08:22:14.508519
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.vars import combine_vars

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import mock_inventory

    # mock global stuff that is not relevant to this method, just to make the code
    # in the method execute
    C.DEFAULT_HASH_BEHAVIOUR = 'md5'

    loader = DataLoader()
   

# Generated at 2022-06-13 08:22:16.503192
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    rv = IncludedFile()
    assert rv == rv
    assert not (rv != rv)

    rv2 = IncludedFile()
    assert rv == rv2



# Generated at 2022-06-13 08:22:31.873436
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager

    fake_loader = DictDataLoader({
        "/test/test.yml": """
        - include_tasks: foo.yml
        - include_tasks: bar.yml
          loop:
            - item1
            - item2
        """,
        "/test/foo.yml": """
        - debug:
            msg: foo
        """,
        "/test/bar.yml": """
        - debug:
            msg: bar
        """
    })

    fake_inventory = InventoryManager(loader=fake_loader,
                                      sources="localhost,")

    fake_variable_manager = VariableManager()

    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()


# Generated at 2022-06-13 08:22:39.607983
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DictDataLoader({"/etc/ansible/hosts":
        """
        localhost
        dummyhost ansible_connection=local
        """})
    variables = variable_manager.get_vars(play=None, host=None, task=None)
    filename = "dummyfile"
    args = {"something": "to_override_something"}
    vars = {}
    block_args = {"something": "to_override_something"}
    task_name = "dummytask"
    block_name = "dummyblock"
    is_role=True

    task = Task()

# Generated at 2022-06-13 08:23:05.143007
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    class FakeLoader():
        def path_dwim(self, _):
            return 'tasks/test.yaml'
    class FakePlaybook():
        pass
    class FakeTask():
        # Needed for Python 2.x, where super.__init__ doesn't work
        def __init__(self):
            self._role_name = None
            self._from_files = {}

    # main file, play0, task0, task1
    iterator = FakePlaybook()
    loader = FakeLoader()
    original_task = FakeTask()

    # The tests will form the actual result of running the included file
    # The 'results' between each test are in the format returned by AnsibleModule.exit_json()

# Generated at 2022-06-13 08:23:16.042554
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import sys
    sys.path.append('../')
    import ansible.playbook.task_include
    import ansible.utils.display
    import ansible.constants
    import os
    import glob

    host1 = 'host1'
    host2 = 'host2'
    host3 = 'host3'

    host1_meta = {'hostvars': {'ansible_search_path': ['/tmp/my_basedir', '/tmp/parent_basedir/foo/bar'], 'omit': 'omit'}}
    host2_meta = {'hostvars': {'ansible_search_path': ['/tmp/parent_basedir/foo/bar'], 'omit': 'omit'}}

# Generated at 2022-06-13 08:23:28.438297
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    hostvars = variable_manager.get_vars(play=dict(name='test'))
    hostvars['my_var'] = "test_value"
    hostvars['my_ip'] = "10.10.10.10"
    original_task = Task()
    original_task._role = None
    results = list()

# Generated at 2022-06-13 08:23:39.566278
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    class FakeHost(object):
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self.name

    class FakeLoader(object):
        def __init__(self, path):
            self.path = path

        def path_dwim(self, include):
            return self.path

    class FakeVariableManager(object):
        def __init__(self):
            self.vars = dict()

        def add_id(self, id):
            self.vars[id] = dict(name=id)

        def get_vars(self, play, host, task):
            return self.vars.get(host.name, dict())


# Generated at 2022-06-13 08:23:48.005715
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    task = Task()
    task_include = TaskInclude()
    task_include._uuid = 1
    task_include._parent = task
    task._uuid = 2

    included_file = IncludedFile('/foo/bar.yml', {}, {}, task_include)
    included_file2 = IncludedFile('/foo/bar.yml', {}, {}, task_include)
    included_file3 = IncludedFile('/foo/bar.yml', {}, {}, task)
    included_file4 = IncludedFile('/foo/bar.yml', {}, {'foo': 'bar'}, task_include)

    assert included_file == included_file2
    assert not included_file == included_file

# Generated at 2022-06-13 08:23:57.654172
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:24:12.939195
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    class Play:
        def __init__(self, **kwargs):
            for (k, v) in kwargs.items():
                setattr(self, k, v)

    original_task = Task()
    original_task._uuid = 'db8b2ad2-6f69-9283-0d58-f85ec51e6d1b'
    original_task._parent = Play(path='/path/to/task')


# Generated at 2022-06-13 08:24:25.416629
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import mock
    import datetime
    import random

    random.seed(datetime.datetime.now())

    original_host = mock.Mock()
    original_task = mock.Mock()

    mock_play = mock.Mock()
    mock_loader = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_iterator = mock.Mock()

    mock_iterator._play = mock_play
    mock_variable_manager.get_vars.side_effect = lambda *a, **b: {}

    result_file = 'test' + str(random.randint(100, 100000))
    result_host = 'testhost' + str(random.randint(100, 100000))


# Generated at 2022-06-13 08:24:34.162134
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    def assertIncludedFilesEqual(first, second):
        for first_key in first:
            for second_key in second:
                assert first_key == second_key

    included_files = []

# Generated at 2022-06-13 08:24:42.810412
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    class TestIncludeFile(unittest.TestCase):
        def setUp(self):
            self.loader = None
            self.iterator = None
            self.variable_manager = VariableManager(loader=self.loader, inventory=InventoryManager(self.loader, []))
            self.variable_manager._extra_vars = {"test_var": "test_value"}
            self.templar = Templar(loader=self.loader, variables=self.variable_manager.get_vars())
            self.test_1 = Task()

# Generated at 2022-06-13 08:25:01.934022
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filenames = ["foo.yml", "bar.yml"]
    args = [{"_raw_params": "foo.yml"}, {"_raw_params": "bar.yml"}]
    vars = [{}, {}]
    task_uuids = ["FooUUID", "BarUUID"]
    parent_task_uuids = ["fooParentUUID", "barParentUUID"]
    hosts = [[1, 2, 3], [4, 5, 6]]

    included_file1 = IncludedFile(filenames[0], args[0], vars[0], mock_task(task_uuids[0], parent_task_uuids[0], hosts[0]))

# Generated at 2022-06-13 08:25:05.365207
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    i1 = IncludedFile('file.yml', {}, {}, None)
    i2 = IncludedFile('file.yml', {}, {}, None)
    assert(i1 == i2)


# Generated at 2022-06-13 08:25:20.554108
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:25:26.458901
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Set up
    class Host(object):
        def __init__(self, name):
            self.name = name

    from ansible.vars.manager import VariableManager

    parse_host = lambda h: Host(h)

    result_ok = {
        "ansible_job_id": "864584605831.26573",
        "changed": True,
        "content": "Other things here",
        "failed": False,
        "include": "This is the include",
        "include_args": {
            "role": "the-role",
            "task_from": "the-task",
            "static_from": "the-static"
        }
    }


# Generated at 2022-06-13 08:25:39.782027
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # Arrange
    import json
    import unittest
    import ansible.plugins.loader as loader_pkg
    loader = loader_pkg.get("action", "include")

# Generated at 2022-06-13 08:25:51.805282
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import unittest

    loader = DictDataLoader({})
    variable_manager = VariableManager()

    class MockIterator:
        def __init__(self):
            self._play = Play()

    # These tests are adapted from unit tests in test/units/playbook/test_task_include.py
    # Strip off unnecessary data objects

    class MockTaskResult:
        _result = {'include_results': {'127.0.0.1': {'include_results': [{'include': 'foo.yml', 'include_args': {'a': '1'}}]}}}

        def __init__(self, host='127.0.0.1'):
            self._host = host

    class MockTask:
        def __init__(self, action=None):
            self.action = action


# Generated at 2022-06-13 08:25:57.521188
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    module_name = 'include_vars'
    module_args = dict(
        files=[
            dict(
                include='{{ item.name }}',
                with_dict='{{ item.dict }}'
            )
        ],
        _raw_params=['{{ lookup("template", "/tmp/templated_file") }}'],
        name="{{ item.name }}"
    )

# Generated at 2022-06-13 08:26:07.308743
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    '''
    This method tests the process_include_results method of the IncludedFile class.
    It tests the main functionalities of the method.
    '''
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    # Initialize ansible objects
    loader = DataLoader()
    variable_manager = VariableManager()
    play_source = dict(
            name = "Ansible Play",
            hosts = 'all',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='ls'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

    play

# Generated at 2022-06-13 08:26:18.148455
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()


# Generated at 2022-06-13 08:26:25.446646
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.playbook_iterator import PlaybookIterator

    loader = DataLoader()
    variable_manager = VariableManager()
    block = Block()
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    iterator = PlaybookIterator(loader, variable_manager, play, block, None)

    # Test a single task having 'include' and 'loop' specified

# Generated at 2022-06-13 08:26:50.650996
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    play = Play()

# Generated at 2022-06-13 08:27:02.805756
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # import jinja2
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)

    included_files = IncludedFile.process_include_results(
        [
            {
                '_host': 'localhost',
                '_task': 'action',
                '_result': {
                    'include_args': {'a': 'foo', 'b': 'blah'},
                    'include': 'foo.yml',
                    'ansible_loop_var': 'item',
                    'item': 'abc',
                }
            }
        ],
        None,
        loader=loader,
        variable_manager=variable_manager
    )


# Generated at 2022-06-13 08:27:10.460913
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():

    from ansible.playbook.task import Task

    task = Task()
    task._parent = None
    task._role = None
    task._role_name = None
    task._from_files = {}

    inc_file = IncludedFile('/path/to/file', {'arg1': 'value1'}, {'var1': 'value1'}, task)
    assert inc_file == IncludedFile('/path/to/file', {'arg1': 'value1'}, {'var1': 'value1'}, task)

    bad_file = IncludedFile('/another/path/to/file', {'arg1': 'value1'}, {'var1': 'value1'}, task)
    assert inc_file != bad_file


# Generated at 2022-06-13 08:27:21.298242
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    if1 = IncludedFile('/home/vagrant/ansible/playbooks/test.yml', {'var1': 'val1'}, {'var2': 'val2'}, 'task')
    if2 = IncludedFile('/home/vagrant/ansible/playbooks/test.yml', {'var1': 'val1'}, {'var2': 'val2'}, 'task')
    if3 = IncludedFile('/home/vagrant/ansible/playbooks/test.yml', {'var1': 'val1'}, {'var2': 'val2'}, 'task')
    if4 = IncludedFile('/home/vagrant/ansible/playbooks/test2.yml', {'var1': 'val1'}, {'var2': 'val2'}, 'task')


# Generated at 2022-06-13 08:27:27.894416
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename = 'filename'
    args = dict()
    vars = dict()
    task = None

    inc_file1 = IncludedFile(filename=filename, args=args, vars=vars, task=task)
    inc_file2 = IncludedFile(filename=filename, args=args, vars=vars, task=task)
    assert inc_file1 == inc_file2


# Generated at 2022-06-13 08:27:29.921166
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    if __name__ == '__main__':
        test_IncludedFile_process_include_results()

# Generated at 2022-06-13 08:27:43.272231
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # TODO: is it necessary to update this unit test?
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class DummyPlaybook:
        def __init__(self):
            self.path = './'

    class DummyTask:
        def __init__(self):
            self.action = 'include'
            self.no_log = False
            self.get_search_path = lambda: ['_path']

    class DummyLoader:
        def __init__(self, playbook):
            self.path = playbook.path
            self.get_basedir = lambda: '_basedir'

        def path_dwim(self, filename):
            return '_path/%s' % filename


# Generated at 2022-06-13 08:27:53.760693
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    filename1 = "../roles/common/tasks/main.yml"
    filename2 = "../roles/common/tasks/main2.yml"
    filename3 = "../roles/common/tasks/main3.yml"
    args1 = {}
    args2 = {"_raw_params": 'file2'}
    vars1=dict(testvar="testvalue")
    task1=None
    task2=None

    include1 = IncludedFile(filename1, args1, vars1, task1)
    include2 = IncludedFile(filename1, args1, vars1, task1)
    include3 = IncludedFile(filename2, args2, vars1, task2)
    include4 = IncludedFile(filename3, args2, vars1, task2)

# Generated at 2022-06-13 08:28:02.331295
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import sys
    import os
    import inspect

    # Grab the path to the 'test' dir so we can make some assumptions
    # about how the directory structure should look
    test_dir = os.getcwd()
    for i in range(len(inspect.stack())):
        if inspect.stack()[i].function == 'test_IncludedFile_process_include_results':
            new_test_dir = os.path.realpath(os.path.dirname(inspect.stack()[i].filename))
            if new_test_dir.endswith('ansible-base/test/unittests/lib_plugins/loader'):
                test_dir = new_test_dir
                break

    sys.path.append(os.path.join(test_dir, 'module_utils'))


# Generated at 2022-06-13 08:28:08.989438
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    class MockRole(object):
        def __init__(self, role_path=None):
            self._role_path = role_path

    class MockPlay(object):
        def __init__(self, basedir=None):
            self._basedir = basedir

    class MockTask(object):
        def __init__(self, action=None, args=None, vars=None, loop=None, _uuid=None, _parent=None):
            self.action = action
            self.args = args
            self.loop = loop
            self.vars = vars
            self._uuid = _uuid
            self._parent = _parent


# Generated at 2022-06-13 08:28:37.516552
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    # TODO: Add this test back after it is possible to run a bunch of tests without actually performing
    # a run (the test wont work if inventory is empty)
    pass

# Generated at 2022-06-13 08:28:47.791388
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    
    # The included file in role 'test_role' in file './roles/test_role/tasks/main.yml' is 
    # included with 'include_tasks'
    filename = './roles/test_role/tasks/main.yml'
    args = {'_raw_params': '../../../test_roles/test_role/tasks/main.yml'}
    vars = {'ansible_role_name': 'test_role'}
    task = TaskInclude(action='include_tasks', args=args, deps=[], lineno=1)
    is_role = False
    result_inc_file_1 = IncludedFile(filename, args, vars, task, is_role)

    # The included file in role 'test_role' in file './test

# Generated at 2022-06-13 08:28:59.805125
# Unit test for method process_include_results of class IncludedFile

# Generated at 2022-06-13 08:29:10.682820
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():

    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_iterator import PlaybookIterator

    class TaskResult():
        def __init__(self):
            self._host = None
            self._task = None

    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, source='[local]\nlocalhost\n')
    play_context = PlayContext(remote_addr='localhost', remote_user='vagrant')
    variable_manager.set_inventory(inventory)
    variable_manager.extra_

# Generated at 2022-06-13 08:29:21.743739
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    '''
    A test for method __eq__ of class IncludedFile
    '''
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block
    #from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.block import include_role_tasks
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 08:29:34.013674
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager()

    play = Play()
    task = Task()
    results = []

    play._variable_manager = variable_manager
    play._variable_manager.set_inventory(inventory)

    # Test basic include
    task.action = 'include'
    task.args['_raw_params'] = 'test.yaml'
    result = Result(host='foo', task=task, result=dict(include='test.yaml'))
    results.append(result)

# Generated at 2022-06-13 08:29:40.887575
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.plugins.loader
    import ansible.vars.manager

    results = []

    # in Ansible 2.8 and higher, we use to_text instead of to_unicode, so change the test to match
    if not hasattr(results, 'to_text'):
        results.to_text = lambda x: x

    results.append({'item': 'a', 'failed': False, 'include': 'b.yml'})
    results.append({'item': 'x', 'failed': False, 'include': 'y'})
    results.append({'item': '1', 'failed': False, 'include': '2'})
    results.append({'item': '1', 'failed': False, 'include': '3', 'include_args': {'include_vars': {'key': 'value'}}})

# Generated at 2022-06-13 08:29:49.216286
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    from ansible import cli
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars

    loader = cli.CLI.setup_loader()
    inventory = InventoryManager(loader=loader, sources=b'tests/inventory')
    virt_inventory = InventoryManager(loader=loader, sources=b'tests/inventory')
    play_context = PlayContext(loader=loader)


# Generated at 2022-06-13 08:29:59.770756
# Unit test for method __eq__ of class IncludedFile
def test_IncludedFile___eq__():
    ifs = []

    ifs.append(IncludedFile('/etc/ansible/foo.yml', {}, {}, 'task1'))
    ifs.append(IncludedFile('/etc/ansible/foo.yml', {}, {}, 'task2'))
    ifs.append(IncludedFile('/etc/ansible/foo.yml', {}, {'a': 1}, 'task1'))
    ifs.append(IncludedFile('/etc/ansible/foo.yml', {}, {'a': 2}, 'task2'))
    ifs.append(IncludedFile('/etc/ansible/foo.yml', {'a': 1}, {}, 'task1'))

# Generated at 2022-06-13 08:30:10.743073
# Unit test for method process_include_results of class IncludedFile
def test_IncludedFile_process_include_results():
    import ansible.playbook.play_context