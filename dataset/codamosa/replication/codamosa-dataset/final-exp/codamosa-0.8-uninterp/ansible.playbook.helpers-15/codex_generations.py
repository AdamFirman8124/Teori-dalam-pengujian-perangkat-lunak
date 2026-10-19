

# Generated at 2022-06-13 08:21:30.173905
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    my_list = [{'include': 'test.yml'}, {'action': {'module': 'debug', 'args': {'msg': 'hello'}}}]
    assert isinstance(load_list_of_tasks(my_list, None, None, None, None, False, None, None), list)

    my_list2 = [1, 2, 3]
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(my_list2, None, None, None, None, False, None, None)

    my_list3 = [{'include': 'test.yml'}, 1]

# Generated at 2022-06-13 08:21:37.026733
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test with empty list
    assert load_list_of_tasks([]) == []

    # Test with list of one task
    assert load_list_of_tasks([{'action': {'module': 'shell', 'args': 'echo $SHELL'}}]) != []

    # Test with list of one block (implicit)
    assert load_list_of_tasks([{'action': {'module': 'shell', 'args': 'echo $SHELL'}}]) != []

    # Test with list of one block (explicit)
    assert load_list_of_tasks([{'block': {'name': 'test explicit block', 'tasks': [{'action': {'module': 'shell', 'args': 'echo $SHELL'}}]}}]) != []

    # Test with invalid ds

# Generated at 2022-06-13 08:21:46.014028
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    '''
     Test load list of block
    '''
    ds = None
    play = None
    parent_block = None
    role = None
    task_include = None
    use_handlers = True
    variable_manager = None
    loader = None
    try:
        assert load_list_of_blocks(ds, play, parent_block, role, task_include, use_handlers, variable_manager, loader) == []
        print("test case 1 passed")
    except Exception:
        print("test case 1 failed")

    ds = [{'block': 'block1'}, {'block': 'block2'}]
    play = None
    parent_block = None
    role = None
    task_include = None
    use_handlers = True
    variable_manager = None
    loader = None


# Generated at 2022-06-13 08:21:50.145093
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class MockLoader:
        @staticmethod
        def list_directory(path):
            return []

        @staticmethod
        def path_exists(path):
            return False

        @staticmethod
        def file_exists(path):
            return False

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    display = Display()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    pc = PlayContext()
    pc.set_loader(loader=loader)
    pc.set_variable_manager(variable_manager=variable_manager)
   

# Generated at 2022-06-13 08:22:00.719669
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    loader = DictDataLoader(
        {
            'non-existent-file-in-path': "",
            'a_role': {
                'tasks': {
                    'a_task_file': textwrap.dedent("""
                    - ping:
                    - debug: var=example_variable
                    """)
                },
                'handlers': {
                    'a_handler_file': textwrap.dedent("""
                    - name: a handler
                      ping:
                    """)
                }
            }
        })
    display = Display()
    play = Play()
    block = Block()
    role = Role()
    task_include = TaskInclude()
    use_handlers = False
    variable_manager = VariableManager()

    task_list = list()

# Generated at 2022-06-13 08:22:14.632369
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    module_args = dict(
        name='test',
        state='present'
    )
    task_ds = dict(
        name='test',
        use_action=True,
        action='user',
        args=module_args
    )
    try:
        load_list_of_tasks(ds=task_ds, task_include=False, use_handlers=False)
    except AnsibleAssertionError:
        assert False
    try:
        load_list_of_tasks(ds=task_ds, task_include=False, use_handlers=True)
    except AnsibleAssertionError:
        assert False

# Generated at 2022-06-13 08:22:16.471757
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: write test for this function
    pass


# Generated at 2022-06-13 08:22:28.444304
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    mock_loader = DictDataLoader({
        '/etc/ansible/roles/fakedep/meta/main.yml': 'dependencies: fake'
    })

    mock_inventory = Inventory(loader=mock_loader, host_list=[])
    variable_manager = VariableManager(loader=mock_loader, inventory=mock_inventory)
    play_context = PlayContext()

    playbook_vars_template = '''
---
dependencies:
- "{{ foo }}"
- '{{ bar }}'
    '''
    playbook_vars_yaml = yaml.safe_load(playbook_vars_template)

    # case 1: test _load

# Generated at 2022-06-13 08:22:28.881439
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:22:37.581333
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar

    play = FakePlay()
    role = FakeRole()
    block = None
    variable_manager = FakeVariableManager()
    loader = FakeLoader()

    ds = [{'block': {'block': {'block': {'hosts': 'a'}}, 'hosts': 'b'}, 'hosts': 'c'}]

# Generated at 2022-06-13 08:22:54.967485
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "to implement"

# Generated at 2022-06-13 08:23:05.012733
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class Fakes:
        class FakePlaybook:
            def __init__(self):
                self._entries = dict()

            def set_variable_manager(self, vm):
                self._variable_manager = vm

            def get_variable_manager(self):
                return self._variable_manager
        class FakeVariableManager:
            def __init__(self, vm):
                self.vm = vm

            def get_vars(self, play=None, task=None):
                return {'foo': 'bar'}
        class FakeLoader:
            def path_dwim(self, include_target):
                return include_target
        class FakeRole:
            def __init__(self, name):
                self.name = name
            @property
            def _role_path(self):
                return self.name

    #

# Generated at 2022-06-13 08:23:09.657316
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  print(load_list_of_tasks(['aa','bb']))

print(test_load_list_of_tasks())
'''
if __name__ == '__main__':
  test_load_list_of_tasks()
'''

# load_list_of_tasks()

# Generated at 2022-06-13 08:23:19.625357
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader=None, variable_manager=None, host_list=['127.0.0.1']))
    variable_manager.extra_vars = load_extra_vars(loader=None, options=play_source_vars)
    block = Block()

# Generated at 2022-06-13 08:23:31.234882
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.template import Templar
    data = [
        {'action': 'shell', 'args': 'echo "foo"', 'module_name': 'shell', 'register': 'somevar'},
        {'action': 'set_fact', 'args': {'somevar': 'somevalue'}, 'module_name': 'set_fact', 'register': None},
        {'action': 'include_tasks', 'args': 'include_test.yml', 'module_name': 'include_tasks', 'register': None}
    ]

# Generated at 2022-06-13 08:23:40.671961
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print('testing load_list_of_tasks ')
    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    # TODO:
    # - Implicit blocks are created by bare tasks listed in a play without an explicit block statement
    # - the next in the list
    # - task include and it is statically_loaded

    ds = list()

# Generated at 2022-06-13 08:23:46.959248
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import yaml
    from ansible.playbook import Play
    from ansible.vars import VariableManager

    vars_manager = VariableManager()
    pb = Play.load(dict(
        name = "test play",
        hosts = "all",
        vars = dict(
            var1 = "foo",
            var2 = "bar",
        ),
    ), variable_manager=vars_manager)

    ds = yaml.safe_load('''
- name: test task
  debug:
    var: var1
- name: another test
  debug:
    var: var2
- block:
  - block:
      - debug:
          var: test
''')

    blocks = load_list_of_blocks(ds, pb)

# Generated at 2022-06-13 08:23:57.032002
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.parsing.mod_args import ModuleArgsParser

    class MockLoader:
        def get_basedir(self):
            return '/home/vagrant'

        def load_from_file(self, path):
            if path == '/home/vagrant/path/to/tasks/include.yml':
                return '[{ "include": "path/to/tasks/include2.yml", "static": true }]'

# Generated at 2022-06-13 08:24:09.024463
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    task_ds = dict(
        action=dict(
            module='shell',
            args='echo 1',
            delegate_to='localhost',
            ignore_errors=True
        )
    )


# Generated at 2022-06-13 08:24:09.834207
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:24:40.245789
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    def test():
        return True

    def test_block():
        return True

    def test_task_include():
        return True

    def test_handler_task_include():
        return True

    def test_include_role():
        return True

    def test_task():
        return True

    def test_handler():
        return True

    # import here to prevent circular dependency issues
    # from ansible.playbook.block import Block
    # from ansible.playbook.handler import Handler
    # from ansible.playbook.task import Task
    # from ansible.playbook.task_include import TaskInclude
    # from ansible.playbook.handler_task_include import HandlerTaskInclude

    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole

# Generated at 2022-06-13 08:24:49.243379
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    loader_mock = Mock()
    ds = [{'include': 'test'}]
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.task import Task
    task_mock = Mock()
    task_mock.module_args = True
    task_mock.module_vars = {}
    task_mock.action = 'include'
    loader_mock.load_from_file.return_value = ds
    task_mock.copy.return_value = task_mock
    task_mock.copy.side_effect = lambda x: task_mock

    task_list

# Generated at 2022-06-13 08:25:03.778845
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    play = Play()
    play._variable_manager = VariableManager()
    play._variable_manager.set_inventory(InventoryManager(loader=DataLoader()))


# Generated at 2022-06-13 08:25:18.880344
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import tempfile
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import plugins
    from ansible.vars.manager import VariableManager
    from ansible.playbook import Playbook

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Playbook()

    # Fake the file being parsed
    fake_file = tempfile.NamedTemporaryFile()
    fake_file.write(b"""
- name: test
  include_role: foo
""")
    fake_file.flush()
    fake_file.seek(0)

    def test_case(action):
        fake_file.seek(0)

# Generated at 2022-06-13 08:25:32.161607
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole

    display = Display()
    play = Play().load({
        'name': 'test_load_list_of_tasks',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    }, variable_manager=VariableManager(), loader=DictDataLoader())

# Generated at 2022-06-13 08:25:33.954151
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True == load_list_of_tasks()



# Generated at 2022-06-13 08:25:41.920860
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    yaml_from_doc = [{'action': 'shell', 'name': 'Include a role'}]
    task_list = load_list_of_tasks(yaml_from_doc, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert isinstance(task_list, list)
    assert len(task_list) == 1
    assert task_list[0].action == 'shell'



# Generated at 2022-06-13 08:25:55.088296
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import json
    import sys
    import types
    import unittest
    sys.path.insert(0, os.path.join(os.getcwd(), 'lib'))

    # Mock out the __init__ function
    class MockeInclude(types.ModuleType):
        def __init__(self):
            self.all_includes = dict()

    module = MockeInclude("ansible.playbook.include")
    sys.modules['ansible.playbook.include'] = module

    # Mock out the __init__ function
    class MockModuleArgsParser(types.ModuleType):
        def __init__(self):
            pass

    module = MockModuleArgsParser("ansible.parsing.module_args")
    sys.modules['ansible.parsing.module_args'] = module

    # Mock out

# Generated at 2022-06-13 08:25:55.781118
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:26:06.125452
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def check_different_load_spec(spec, result):
        assert load_list_of_tasks(spec, None, None, None, None, False, None, None) == result

    # Empty list
    check_different_load_spec([], [])
    # List with one item in it
    check_different_load_spec(
        [
            {'debug': {'msg': "Inside bar loop"}}
        ],
        [
            {'debug': {'msg': "Inside bar loop"}}
        ]
    )
    # List with multiple items

# Generated at 2022-06-13 08:26:39.440369
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar

    def load_list_of_blocks_mocking_block_load(ds, play, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
        print(type(ds))
        print(type(play))
        print(type(parent_block))
        print(type(role))
        print(type(task_include))
        print(type(use_handlers))
        print(type(variable_manager))
        print(type(loader))

        if not isinstance(ds, (list, type(None))):
            raise

# Generated at 2022-06-13 08:26:47.436325
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # loads a playbook
    pb = Playbook.load("./test/unit/modules/check_users/test_static_import.yml", loader=DictDataLoader({}))
    # gets the first play
    play = pb.get_plays()[0]
    # gets the first block of the play
    block = play.compile()[0]
    # gets the list of tasks of the block
    task_list = load_list_of_tasks(block, play)
    # checks the number of tasks
    assert len(task_list) == 3

# Generated at 2022-06-13 08:26:54.778062
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    fixture = [
        {'block': [{'include_role': {'name': 'common'}}]},
        {'include_role': {'name': 'common', 'static': True}},
        {'include_role': {'name': 'common'}},
        {'include_role': {'name': 'common'}},
        {'include_tasks': 'common/tasks/main.yml'},
        {'include_playbook': 'new/playbook.yml'},
        {'import_tasks': 'common/tasks/main.yml'},
        {'import_role': {'name': 'common'}},
        {'import_playbook': 'new/playbook.yml'}
    ]
    # https://stackoverflow.com/a/51592261

# Generated at 2022-06-13 08:27:06.733492
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    ds = [{
        'include': 'dummy',
        'static': True,
        'block': 'Dummy Block',
        'task': 'Task1'
    }, {
        'include': 'dummy',
        'static': False,
        'block': 'Dummy Block',
        'task': 'Task1'
    }]
    play = 'dummy'
    block = Block(play)
    role = 'dummy_role'
    task_include = Task()
    task_list = load_list_of_tasks(ds, play, block, role, task_include)
    assert task_list[0].statically_loaded is True
    assert task_list[1].statically_loaded is False

# Generated at 2022-06-13 08:27:18.834855
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    host = {
        "hostname" : "127.0.0.1"
    }

    inventory = InventoryManager(loader=DataLoader(), sources=host)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    pb = Playbook.load([], variable_manager=variable_manager, loader=DataLoader())

# Generated at 2022-06-13 08:27:19.827453
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  # No tests
  pass



# Generated at 2022-06-13 08:27:27.124380
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

    # list of dicts

# Generated at 2022-06-13 08:27:36.079478
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader
    yaml_ds = '''
- name: ping
  ping:
- name: shell
- raw: echo
- block:
    - name: serve
      service:
        name: httpd
        state: started
        enabled: True
        regexp: 'foo'
- block:
    - name: serve
      service:
        name: httpd
        state: started
        enabled: True
        regexp: 'foo'
- rescue:
    - name: rescue something
      ping:
- always:
    - name: something
      ping:
- include: foo.yml
- include_tasks: foo.yml
- import_tasks: foo.yml
    '''
    data = load_list_of_

# Generated at 2022-06-13 08:27:41.282293
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(ds=None, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) == None


# Generated at 2022-06-13 08:27:52.480522
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    # AnsibleParserError

    ds = [{"block": "This block should return None"},
          {"include_tasks": "file"}]

    task = load_list_of_tasks(ds=ds,
                              play=None,
                              block=None,
                              role=None,
                              task_include=None,
                              use_handlers=False,
                              variable_manager=None,
                              loader=None)
    assert len(task) == 2
    assert isinstance(task[0], TaskInclude)
    assert isinstance(task[1], Task)

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 08:28:27.162003
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''unit test for the load_list_of_tasks() function'''

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.included_file import IncludedFile

    # test a list with a task and a block

# Generated at 2022-06-13 08:28:31.118205
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    display.verbosity = 0
    assert load_list_of_tasks([], object()) == []
    assert load_list_of_tasks(set(), object()) == []



# Generated at 2022-06-13 08:28:43.341771
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = []

    # Test nothing passed
    tasks = load_list_of_tasks(ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert tasks == []

    # Test empty list
    tasks = load_list_of_tasks([], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert tasks == []

    # Test list with one item
    ds = [{'test': 'something'}]

# Generated at 2022-06-13 08:28:50.464032
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ..module_utils._text import to_text
    import pytest
    from ansible.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play, PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 08:29:01.866095
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({
        "foo.yml": """
        - name: do this
          foo: bar
        """
    })
    inventory = InventoryManager(loader=loader, sources=["localhost,"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.network_os = 'junos'

    # first we load a list of bare tasks
    # and assert that they map to new implicit blocks


# Generated at 2022-06-13 08:29:14.026237
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    import ansible.playbook.play_context as play_context

    # Setup test environment

    # setup a fake play
    p = Play().load(
        dict(
            name="test play",
            hosts=['all'],
            gather_facts='no',
            tasks=[
                dict(action=dict(module='test'))
            ],
        ),
        variable_manager=VariableManager(),
        loader=DictDataLoader(),
    )

    # setup an empty block
    b = Block()

    # setup role

# Generated at 2022-06-13 08:29:28.770749
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    my_task_ds = {
        "name": "ANSIBLE_INVENTORY",
        "block": 2,
        "ignore_errors": True,
        "block": 2
        }

    variable_manager = VariableManager()
    loader = DataLoader()


# Generated at 2022-06-13 08:29:38.240143
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    import sys
    import imp
    from subprocess import Popen, PIPE

    # Test module
    import ansible.module_utils.basic
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.reserved import *

    dirname = os.path.dirname(__file__)
    sys.path.append(dirname)
    sys.path.append(dirname + '/../test/lib')

    import test_playbook_data as DATA

    # vars
    from ansible.vars.manager import VariableManager
    import ansible.inventory.manager
    variable_manager

# Generated at 2022-06-13 08:29:47.424898
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    data = [
        {'include': 'foo'},
        {'include': 'bar'},
        {'include': 'baz'},
        {'include': 'bat'},
        {'static': 'bar'},
        {'static': 'foo'},
    ]
    result = load_list_of_tasks(data)
    if not isinstance(result[0], TaskInclude):
        raise AssertionError("result[0] isn't TaskInclude object")
    else:
        if result[0].statically_loaded:
            raise AssertionError("result[0].statically_loaded is True")
    if not isinstance(result[1], TaskInclude):
        raise Ass

# Generated at 2022-06-13 08:29:53.573260
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="inventory_test1.ini")
    variable_manager = VariableManager(loader=loader, inventory=inventory)