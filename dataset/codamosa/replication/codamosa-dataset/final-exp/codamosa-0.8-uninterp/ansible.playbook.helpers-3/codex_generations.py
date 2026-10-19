

# Generated at 2022-06-13 08:21:30.604635
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import sys
    import ansible
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    import time
    import json
    import os
    import tempfile
    import datetime
    sys.path.append(os.getcwd()+"/..")
    display = Display()

    def get_temp_file(raw_data):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(raw_data.encode("utf-8"))
            return f.name


# Generated at 2022-06-13 08:21:42.824245
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # empty list
    assert load_list_of_tasks([], None) == []

    # wrong types
    with pytest.raises(AnsibleAssertionError) as e:
        load_list_of_tasks(None, None)
    assert 'should be a list' in to_text(e)
    with pytest.raises(AnsibleAssertionError) as e:
        load_list_of_tasks({'a': None}, None)
    assert 'should be a list' in to_text(e)

    # valid tasks
    assert len(load_list_of_tasks([{}, {}], None)) == 2

    # blocks

# Generated at 2022-06-13 08:21:52.682002
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import tempfile
    import shutil
    import os
    import sys

    # Setup Ansible environment for tests
    if not os.path.exists('/tmp/ansible_test'):
        os.makedirs('/tmp/ansible_test')
    if not os.path.exists('/tmp/ansible_test/test_included'):
        os.makedirs('/tmp/ansible_test/test_included')

    fd, path = tempfile.mkstemp(dir='/tmp/ansible_test', text=True)
    os.close(fd)
    with open(path, 'w') as f:
        f.write('#!/usr/bin/python\nprint("Hello world")\n')
    os.chmod(path, 0o755)

    fd, path

# Generated at 2022-06-13 08:22:02.334260
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #from ansible.playbook.play import Play
    from ansible.playbook.play import play_from_file
    from ansible.playbook.play import Play
    #from ansible.playbook.play import play_from_file
    from ansible.vars import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    practice_loader = DataLoader()
    practice_variable_manager = VariableManager()
    playbook = 'test_playbook.yml'
    #practice_play = play_from_file(practice_loader, playbook, practice_variable_manager)[0]
    practice_play = Play.load(
                            playbook,
                            variable_manager=practice_variable_manager,
                            loader=practice_loader,
                        )
   

# Generated at 2022-06-13 08:22:04.753269
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    try:
        load_list_of_blocks(None)
    except Exception as e:
        print(str(e))

# Generated at 2022-06-13 08:22:16.215582
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars import Variable_Manager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.path import unfrackpath


# Generated at 2022-06-13 08:22:28.137706
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()

    host = Host(name="test_load_tasks.example.com")
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['Tests/_data/load_list_of_tasks/hosts']))
    variable_manager.set_host_variable(host, 'var1', 'value1')
    variable_manager.set_host_variable(host, 'var2', 'value2')

    inventory = variable_manager.get_inventory()
    ctx

# Generated at 2022-06-13 08:22:34.633971
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:22:41.735807
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    # we import here to prevent a circular dependency with imports

    options = OptionParser()
    (options, args) = options.parse_args()
    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(options.extra_vars)
    loader = DataLoader()

    # get current working dir
    current_working_dir = os.path.dirname(os.path.abspath(__file__))
    inventory_file = os.path.join(current_working_dir, "test_inventory")

# Generated at 2022-06-13 08:22:55.400150
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    basic test of load_list_of_tasks
    '''
    try:
        load_list_of_tasks('test')
        raise AssertionError('load_list_of_tasks did not receive a list and raise an AnsibleAssertionError')
    except AnsibleAssertionError:
        pass

    try:
        load_list_of_tasks([])
        raise AssertionError('load_list_of_tasks did not raise an AnsibleAssertionError for an empty list')
    except AnsibleAssertionError:
        pass


# Generated at 2022-06-13 08:23:18.777942
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.vars import VariableManager


# Generated at 2022-06-13 08:23:30.547389
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    play_ds = dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = False,
        roles = [
            dict(
                name = 'parent',
                tasks = [
                    dict(
                        include_tasks = 'foo.yml',
                    ),
                    dict(
                        include_tasks = 'foo2.yml',
                        static = True,
                    ),
                ],
            ),
            dict(
                name = 'child',
                tasks = [
                    dict(
                        import_tasks = 'foo.yml',
                    ),
                ],
            ),
        ],
    )

# Generated at 2022-06-13 08:23:41.165124
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = []
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = object
    def __init__(self, *args, **kwargs):
        return args, kwargs
    class Task(object):
        load = __init__
    class TaskInclude(object):
        load = __init__
    class HandlerTaskInclude(object):
        load = __init__
    class IncludeRole(object):
        load = __init__
        get_block_list = __init__
    class AnsibleParserError(object):
        __init__ = __init__
    class Handler(object):
        load = __init__
    class AnsibleUndefinedVariable(object):
        __init__ = __init__
   

# Generated at 2022-06-13 08:23:49.008643
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.taggable import Taggable
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from ansible.utils._text import to_native
    from ansible.errors import AnsibleParserError, AnsibleUnd

# Generated at 2022-06-13 08:23:58.228376
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    yaml = """
    - name: Hello world
      debug:
        msg: Hello world!
    - name: Populate a hostvar
      set_fact:
        my_hostvar: "Set by task"
    - name: Hello world
      debug:
        msg: "Value set by earlier task: {{my_hostvar}}"
    """
    
    #import pdb; pdb.set_trace()
    play = Play().load({'name': 'Playbook to test load_list_of_blocks',
                        'hosts': 'localhost',
                        'gather_facts': False,
                        'tasks': yaml},
                        variable_manager=VariableManager(), loader=DataLoader())

    assert play.tasks[0].args['msg'] == 'Hello world!'

# Generated at 2022-06-13 08:24:09.835567
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    vars = {'hostvar': 'variable_set_by_host'}
    var_manager = VariableManager(loader=None, inventory=None, version_info=None, host_vars=vars)
    host = Host('testhost')
    var_manager.set_host_variable(host, None, 'hostvar', 'variable_set_by_host')
    var_manager.set_host_variable(host, None, 'hostvar2', 'variable_set_by_host2')
    var_manager.set_host_variable(host, None, 'var1', 'variable_set_by_host3')
    var_manager.set_host_variable(host, None, 'var2', 'variable_set_by_host4')

# Generated at 2022-06-13 08:24:16.923737
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:24:18.230391
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks('', '', '', '') is None


# Generated at 2022-06-13 08:24:19.605988
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "Unit tests not yet implemented!"

# Generated at 2022-06-13 08:24:30.800962
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    ds = [
        {'debug': {'msg': 'foo'}}
    ]
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    task_list = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert(isinstance(task_list[0], Task))

    ds = [
        {'include_tasks': 'bar.yml'}
    ]

# Generated at 2022-06-13 08:25:03.192763
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import ansible.constants as C
    ds1 = [{'block': {'block': {'handler': 'testhandler', 'tasks': []}}},
           {'include_role': {'name': 'test_role_include'}},
           {'include_tasks': {'name': 'test_include'}},
           {'import_role': {'name': 'test_role_import'}}]

# Generated at 2022-06-13 08:25:13.275239
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test setup
    class MockPlay(object):
        def __init__(self, variable_manager=None):
            self.variable_manager = variable_manager
    class MockVariableManager(object):
        def get_vars(self, play=None, task=None):
            return {'test_var': 'test_value'}
    class MockBlock(object):
        def __init__(self, role=None):
            self._role = role
        def get_vars(self):
            return {'block_var': 'block_value'}
    class MockRole(object):
        def __init__(self, _role_path):
            self._role_path = _role_path
    class MockLoader(object):
        def path_dwim(self, path):
            return path

    # tests using normal tasks

# Generated at 2022-06-13 08:25:27.059504
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # Test Variables
    from ansible.playbook.role import RoleInclude

    # Fixtures
    fixture_file = open("test/unit/fixtures/test_load_list_of_roles.yml", "r")
    fixture_data = fixture_file.read()
    fixture_file.close()
    fixture_data_ds = yaml.safe_load(fixture_data)

    # Test Configuration
    role = load_list_of_roles(fixture_data_ds['1'], str("test"), str("test_current_role_path"),
                              variable_manager=str("test_variable_manager"), loader=str("test_loader"),
                              collection_search_list=str("test_collection_search_list"))

    role_test_1 = RoleInclude()
    role_test_1

# Generated at 2022-06-13 08:25:29.869367
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    class Play:
        pass

    class Block:
        pass

    class Role:
        pass

    class VariableManager:
        def get_vars(self, play, task):
            return {}

    # No tasks
    result = load_list_of_tasks([], Play(), Block(), Role(), None, False, VariableManager(), None)
    assert result == []



# Generated at 2022-06-13 08:25:42.573318
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.task import Task

    ds= [
        ImmutableDict({
            'name': AnsibleUnicode('foo'),
            'action': AnsibleUnicode('bar'),
            'notify': [AnsibleUnicode('baz')]})
    ]
    play=None
    block=None
    role=None
    task_include=None
    use_handlers=False
    variable_manager=None
    loader=None

    task_list=load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    #print(task_list

# Generated at 2022-06-13 08:25:43.246189
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:25:56.222946
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    DEFAULT_TESTING_INVENTORY = """
[test01]
www[1:2].example.com
"""

# Generated at 2022-06-13 08:26:06.488471
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    import ansible.playbook
    import ansible.template
    import ansible.utils.unsafe_proxy
    import six
    import ansible.errors
    import ansible.parsing.yaml.objects

    play = Play()
    block = Block()
    role = Role()
    task_include = TaskInclude()
    use_handlers = False
    variable_manager = VariableManager()
    loader = DataLoader()

    ds=[]
    ds

# Generated at 2022-06-13 08:26:11.832317
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([]) == []
    assert load_list_of_tasks([{}]) == []
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(None)
    assert load_list_of_tasks(1) == []


# Generated at 2022-06-13 08:26:26.750743
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:26:51.120912
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([
        {'block': [
            {'include_tasks': '../tasks/main.yml'},
            {'include_tasks': '../tasks/debug.yml'}
        ]}
    ], block=None, use_handlers=False)



# Generated at 2022-06-13 08:26:52.025048
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:27:04.276745
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play


# Generated at 2022-06-13 08:27:10.987798
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    task_ds = dict(action=dict(module='shell', args='ls'))
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = dl
    task = load_list_of_tasks(task_ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=dl)
    print(task)

    print('-' * 50)
    task_ds = dict(action=dict(module='shell', args='ls'))
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = dl


# Generated at 2022-06-13 08:27:21.607895
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    # prepare arguments
    # ds = ['debug: msg="{{ item }}"', {'debug': 'msg="{{ item }}"'}]
    ds = [
        {'debug': 'msg="{{ item }}"'},
        'include_tasks: test.yml',
        'include_role: test'
    ]
    loader = DataLoader()
    inventory = InventoryManager([loader], sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context._variable_manager = variable_manager
    # run function


# Generated at 2022-06-13 08:27:32.804759
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    loader = DictDataLoader({
        'play_thingy.yml': '''
- hosts: all
  tasks:
  - name: test
    debug:
      msg: "test"
    tags:
    - test_tag
  - name: test2
    debug:
      msg: "test2"
    tags:
    - test_tag2
  - name: test3
    debug:
      msg: "test3"
    tags:
    - test_tag3
    ''',
    })

# Generated at 2022-06-13 08:27:46.471269
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # We create an object of class ModuleArgsParser and Task to construct
    # ds,play,block,role,task_include,variable_manager,loader
    # These are the seven necessary parameters to satisfy the
    # function load_list_of_tasks

    # create an object of class ModuleArgsParser
    args_parser = ModuleArgsParser({
        'shell': 'ls -la',
        'register': 'shell_out',
    })

    # create an object of class Task
    task_ds = Task({
        'name': 'hello world',
        'shell': 'ls -la',
        'register': 'shell_out',
    })

    # create a mock object of class VariableManager
    variable_manager = Mock()


# Generated at 2022-06-13 08:27:57.416822
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.template.vars import AnsibleVariable
    from ansible.vars.manager import VariableManager

    # test plain task
    ds_plain_task = {"include_role": {"name": "somename", "static": "yes"}}
    assert isinstance(load_list_of_tasks([ds_plain_task], None)[0], IncludeRole)
    assert isinstance(load_list_of_tasks([ds_plain_task], None)[0].task_include, TaskInclude)
    assert not load_list_of_tasks([ds_plain_task], None)[0].task_

# Generated at 2022-06-13 08:28:04.529666
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    class Options(object):
        pass
    options = Options()
    options.connection = 'local'
    options.module_path = '/home/stack'
    options.forks = 5
    options.remote_user = 'stack'
    options.private_key_file = None
    options.ssh_common_args = None
    options.ssh_extra_args = None
    options.sftp_extra_args = None
    options.scp_extra_args = None
    options.become = False
    options.become_method = None
    options.become_user = None
    options.verbosity = 3
    options.check = False

    variable_manager = VariableManager()
    loader = Data

# Generated at 2022-06-13 08:28:06.472453
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # load_list_of_roles is not being tested as this is just a wrapper around RoleInclude.load,
    # and RoleInclude.load is already being tested by test_role.py
    pass

# Generated at 2022-06-13 08:28:42.514547
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play import Play
    coll_mock1 = MagicMock()
    coll_mock1.get_collection_info.return_value = {
        "namespace": "ansible_namespace",
        "name": "collection_name",
        "version": "1.0.0",
        "dependencies": {},
        "binary_compatibility": True,
        "python_compatibility": "2.7",
    }

    coll_mock2 = MagicMock()

# Generated at 2022-06-13 08:28:50.121252
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    assert load_list_of_blocks(None) is None
    assert load_list_of_blocks([]) == []
    assert load_list_of_blocks({}) == []
    assert load_list_of_blocks([{'foo': 'bar'}]) == [{'foo': 'bar'}]
    assert load_list_of_blocks([{'block': 'foo'}, {'block': 'bar'}]) == [{'block': 'foo'}, {'block': 'bar'}]
    # Implicit blocks

# Generated at 2022-06-13 08:29:01.631922
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
  # Setup: create a list of tasks, blocks, and list of blocks
  from ansible.playbook.block import Block
  from ansible.playbook.task import Task
  from ansible.playbook.role_include import IncludeRole
  from ansible.playbook.play_context import PlayContext
  from ansible.vars.manager import VariableManager

  ds_list = [
    'all',
    '- hosts: all',
    '  tasks:',
    '  - name: test',
    '    ping:',
    '- name: test2',
    '  ping:'
  ]
  ds_block = [
    '- name: test',
    '  ping:',
    '  rescue:',
    '  - name: test2',
    '    ping:'
  ]
  ds_

# Generated at 2022-06-13 08:29:07.095960
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{"include_tasks": "test.yml", "name": "load_list_of_tasks"}]
    task_list = load_list_of_tasks(ds)
    assert isinstance(task_list[0], TaskInclude)

# Generated at 2022-06-13 08:29:08.213624
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    assert load_list_of_roles.__doc__ is not None

# Generated at 2022-06-13 08:29:17.189979
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.parsing.dataloader import DataLoader

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

# Generated at 2022-06-13 08:29:18.693337
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO
    pass

# Generated at 2022-06-13 08:29:32.610270
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    # GIVEN a playbook and a list of tasks
    playbook = Playbook.load("../../../test/sanity/playbooks/test.yml", loader=DataLoader(), variable_manager=VariableManager(), inventory=Inventory("../../../test/sanity/inventory"))

# Generated at 2022-06-13 08:29:37.786295
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(
        [{'block':
          {'block': {'name': 'End'}},
          'name': 'Start of Day'}],
        play=None,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None
    ) == None
    assert load_list_of_tasks(
        [{'block': {'block': {'name': 'End'}}, 'name': 'Start of Day', 'block': {}}],
        play=None,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None
    ) == None
#

# Generated at 2022-06-13 08:29:47.067545
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    try:
        load_list_of_roles("", None)
    except Exception as e:
        assert str(e) == 'ds ( ) should be a list but was a <class \'str\'>'
        print("SUCCESS: Function load_list_of_roles(): Exception is raised")
    else:
        print("FAIL: Function load_list_of_roles(): Exception is not raised")
    try:
        load_list_of_roles("test", None)
    except Exception as e:
        assert str(e) == 'ds (test) should be a list but was a <class \'str\'>'
        print("SUCCESS: Function load_list_of_roles(): Exception is raised")
    else:
        print("FAIL: Function load_list_of_roles(): Exception is not raised")