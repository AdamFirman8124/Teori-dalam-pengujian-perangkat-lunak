

# Generated at 2022-06-13 08:21:07.343997
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.role.include import RoleInclude
    assert RoleInclude.load(dict(role='Foo'))



# Generated at 2022-06-13 08:21:09.537676
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    raise NotImplementedError



# Generated at 2022-06-13 08:21:17.236141
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    options = Options()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    context = PlayContext(remote_addr='127.0.0.1', port=22)

    class MyPlay(object):
        ''' A mock ansible Play class '''
        def __init__(self, name='test_play', play_context=context):
            self.name = name
            self.play_context = play_context

    play = MyPlay()


# Generated at 2022-06-13 08:21:18.414361
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert 1==1

# }}}


# Generated at 2022-06-13 08:21:25.767258
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test that load_list_of_tasks can handle tasks with options set to None
    # See https://github.com/ansible/ansible/issues/17788
    data = [
        {
            "include": "{{ include_file_path }}",
            "name": "foo",
            "register": None
        }
    ]
    try:
        load_list_of_tasks(data, None)
    except AnsibleParserError:
        assert False

# Generated at 2022-06-13 08:21:31.557131
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    block_ds = dict()
    block_ds['block'] = dict()
    block_ds['block']['rescue'] = []
    block_ds['block']['always'] = []
    block_ds['block']['tasks'] = []
    play = Play()
    role = Role()
    TaskInclude.load(block_ds['block']['tasks'], block=None, role=role, task_include=None, variable_manager=None, loader=None)



# Generated at 2022-06-13 08:21:33.628660
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    # TODO: to be implemented
    pass


# Generated at 2022-06-13 08:21:35.957295
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(None, None) is None
    assert load_list_of_tasks(dict(), None) is None



# Generated at 2022-06-13 08:21:45.448589
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import datetime
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 08:21:51.051823
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
    Helper function to get a list of roles to load

    :return: a list of role definitions
    '''
    ds = [{'role': 'role1'}, {'role': 'some-role'}, {'role': 'role3'}]
    play = object()
    current_role_path = object()
    variable_manager = object()
    loader = object()
    collection_search_list = object()

    # unit_test:
    # test for invalid ds type
    if not isinstance(ds, list):
        raise AnsibleAssertionError('ds (%s) should be a list but was a %s' % (ds, type(ds)))

    roles = []

# Generated at 2022-06-13 08:22:23.066393
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "self-test not implemented; please run Ansible with -v and fix any failures"

# Generated at 2022-06-13 08:22:36.869457
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    import sys
    import yaml

    if len(sys.argv) < 2:
        print( "Usage: %s PLAYBOOK" % (sys.argv[0]))
        sys.exit(1)

    pb_path = sys.argv[1]

    if not os.path.exists(pb_path):
        print( "Error: cannot find %s" % (pb_path))

    pb = Playbook.load(pb_path)

    # create inventory, use path to host config

# Generated at 2022-06-13 08:22:48.488515
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from .. import ds

    # Null input
    assert load_list_of_tasks(None, None) == []

    # Empty input
    assert load_list_of_tasks([], None) == []

    # Empty lists/dicts
    assert load_list_of_tasks([{}, []], None) == []

    # List with one task
    assert len(load_list_of_tasks(ds['tasks'][0:1], None)) == 1

    # List with two tasks
    assert len(load_list_of_tasks(ds['tasks'][0:2], None)) == 2

    # List with one block and one task
    assert len(load_list_of_tasks(ds['tasks'][0:3], None)) == 2

    # List with one task, one block and one

# Generated at 2022-06-13 08:23:00.405102
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader

    ds = [
        {'include': 'some_file.yml'},
        {'some_task': 'hello'}
    ]

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}  # do this or you will fail the assert in `set_available_variables`

    task_list = load_list_of_tasks(ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=variable_manager, loader=loader)

    assert len(task_list) == 2

# Generated at 2022-06-13 08:23:07.241292
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    import mock

    # test static include_tasks in a task
    display = Display()
    loader = mock.MagicMock()
    loader.get_basedir.return_value = "/root/ansible-playbook-2.7.0rc1"

    ds = [{'include_tasks': 'include.yaml'}]


# Generated at 2022-06-13 08:23:09.546735
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [1,2,3]
    play = load_list_of_tasks(ds, None , None, None, None, None, None)

# Generated at 2022-06-13 08:23:19.543976
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class FakeVariableManager():
        def get_vars(self, **kwargs):
            return {}


    class FakeBlock():
        def __init__(self):
            self._parent = None
            self.loop = None

        def all_parents_static(self):
            return True

    class FakePlay():
        def __init__(self):
            self.name = 'fake_play'

    class FakeRole():
        @property
        def _role_path(self):
            return 'fake_role_path'

    fake_play = FakePlay()
    fake_block = FakeBlock()
    fake_role = FakeRole()

    # load_list_of_tasks check for a list in the first argument
    # We are checking for the expected error if a non list is provided

# Generated at 2022-06-13 08:23:20.179126
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:23:31.810954
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    data = [
        'shell',
        {'block': 'block'},
        'debug'
    ]
    loader, inventory, variable_manager = (None, None, VariableManager())
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    block_list = load_list_of_

# Generated at 2022-06-13 08:23:41.337196
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import yaml
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    host_vars = {'test_host': {'test_var': 'bar'}}
    loader_mock = MagicMock(path_exists=lambda x: True, is_file=lambda x: True, file_contents=lambda x: b'foo', get_host_vars=lambda x: host_vars)
    variable_manager_mock = MagicMock()

    variable_manager_mock.get_vars.return_value = host_vars
    variable_manager_

# Generated at 2022-06-13 08:24:25.939523
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

    ds = [1, 2, 3, 4]
    try:
        load_list_of_tasks(ds, None)
    except Exception:
        pass
    else:
        assert False

    ds = None
    task_list = load_list_of_tasks(ds, None)
    assert task_list == []

    ds = [{'action': 'copy', }]
    task_list = load_list_of_tasks(ds, None)


# Generated at 2022-06-13 08:24:34.478535
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    import ansible.constants as C
    C.DEFAULT_INVENTORY_PLUGINS = "inventory/plugins"

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    # Create a play

# Generated at 2022-06-13 08:24:42.980370
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([{'block': {'hosts': 'host1'}}], '') == [{'block': {'hosts': 'host1'}}]
    assert load_list_of_tasks([{'block': {'hosts': 'host1', 'tasks': [{'name': 'foobar'}]}}], '') == [{'block': {'hosts': 'host1', 'tasks': [{'name': 'foobar'}]}}]
    assert load_list_of_tasks([{'block': {'hosts': 'host1', 'tasks': [{'action': 'ping'}]}}], '') == [{'block': {'hosts': 'host1', 'tasks': [{'action': 'ping'}]}}]
    assert load

# Generated at 2022-06-13 08:24:50.921526
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  from ansible.errors import AnsibleParserError
  from ansible.playbook.play import Play
  from ansible.playbook.role import Role
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.task_include import TaskInclude
  from ansible.parsing.dataloader import DataLoader

  loader = DataLoader()
  display = Display()
  variable_manager = VariableManager()
  play_ds = {
    'hosts': 'test',
    'tasks': [
      {
        'include': 'test'
      },
      {
        'import_tasks': 'test'
      }
    ]
  }
  play = Play().load(play_ds, variable_manager=variable_manager, loader=loader)
  role = Role()
  task

# Generated at 2022-06-13 08:25:01.952362
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook.play_context
    import ansible.playbook.play
    test_playbook = ['tests/test_playbooks/playbook_3_block.yml']
    loader = DataLoader()
    variable_manager = VariableManager()
    host = FakeHost()
    play_context = ansible.playbook.play_context.PlayContext(variable_manager=variable_manager)
    play = ansible.playbook.play.Play().load(
        test_playbook[0],
        variable_manager=variable_manager,
        loader=loader,
        play_context=play_context,
    )
    play.post_validate(host)
    #print(play.to_pretty_str())

# Generated at 2022-06-13 08:25:12.920738
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Unit tests for ansible.playbook.helpers.load_list_of_tasks
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.block import Block
    playbook_executor = PlaybookExecutor([], [], [], [], {})
    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:25:14.560596
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    pass  # Nothing to test



# Generated at 2022-06-13 08:25:28.340719
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # set up the required objects
    fake_ds = []
    fake_play = Play()
    fake_task_include = TaskInclude()
    fake_block = Block()
    fake_role = Role()

    # test calling it with a null ds
    task_list = load_list_of_tasks(fake_ds, fake_play, fake_block, fake_role,
                                   fake_task_include, use_handlers=False,
                                   variable_manager=None, loader=None)
    assert(isinstance(task_list, list))
    assert(len(task_list) == 0)

    # set up the required objects
    fake_ds = None
    fake_play = Play()
    fake_task_include = TaskInclude()
    fake_block = Block()
    fake_role = Role()



# Generated at 2022-06-13 08:25:34.107852
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import reserved_variables

    from ansible.vars.unsafe_proxy import UnsafeProxy

    from ansible.inventory.manager import InventoryManager

    yaml_str = '''

    - name: task 1
      command: /bin/echo "hello"
    - name: test debug
      debug: var=hostvars['localhost']
    '''

    yaml_list = yaml.load(yaml_str)

    inventory = InventoryManager(loader=None)

    task

# Generated at 2022-06-13 08:25:44.939790
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # Example 1
    # This example replicates an include_tasks call
    # with a single task in it
    yaml_data = """
- include_tasks:
    file: "tasks/demo.yml"
    name: "Run the demo"
"""
    res = load_list_of_tasks(yaml_data, None, None, None, variable_manager=None, loader=None)
    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], TaskInclude)
    assert res[0]._role is None
    assert res[0]._

# Generated at 2022-06-13 08:26:16.940457
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import tempfile
    from ansible.parsing.utils.addresses import parse_address
    from ansible.plugins.loader import action_loader

    """
    test case 1:
    host: localhost
    roles:
      - { role: ansible-modules-core/cloud/azure/azure_rm_publicipaddress }
    """

    task_ds = dict(
        name="test1",
        hosts="localhost",
        roles=[
            { 'role': 'ansible-modules-core/cloud/azure/azure_rm_publicipaddress' },
        ],
    )

    action = action_loader.get('include_role')


# Generated at 2022-06-13 08:26:21.102442
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    #TODO: (Incomplete)
    pass

# Generated at 2022-06-13 08:26:27.169661
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    playbook_file = os.path.join(current_file_path, '..','..','examples','test_collections.yaml')
    #
    #  We need to create a playbook object first to actually test 
    #  load_list_of_tasks
    #
    playbooks = Playbook.load(playbook_file)
    (playbooks, inventory, variable_manager) = Playbook._load_playbook_from_file(playbook_file)
    #
    #  We should have 2 plays now
    #
    assert(len(playbooks) == 2)

    assert(playbooks[0].name == "Play 1")
    assert(playbooks[1].name == "Play 2")
    #

# Generated at 2022-06-13 08:26:39.662417
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:26:40.303992
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:26:50.732684
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()
    block = Block()
    role = None
    task_include = None
    use_handlers

# Generated at 2022-06-13 08:27:02.900638
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from collections.abc import Mapping
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task_include import TaskInclude


# Generated at 2022-06-13 08:27:04.788225
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #FIXME: could not be tested. However, it is unused
    pass

# Generated at 2022-06-13 08:27:11.271617
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # unit tests of load_list_of_tasks() need the following parts of a playbook
    # loader and inventory must be defined
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    play = Play()
    play_context = PlayContext(play=play, options=dict())
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager()

    # test with a dict that is not a list
    ds = dict()
    ds['a'] = 'b'
    task_

# Generated at 2022-06-13 08:27:21.863743
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # check that load_list_of_tasks() can parse its own output
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedString

    ds = [
        dict(
            include_tasks='test1.yml'
        ), {
            'include': 'test2.yml',
            'static': 'yes',
            'when': 'test1.yml'
        }
    ]
    display.verbosity = 2
    list_of_tasks = load_list_of_tasks(
        None,
        ds,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None,
    )

    ds2 = []


# Generated at 2022-06-13 08:28:24.995447
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task

# Generated at 2022-06-13 08:28:36.361205
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
    # from ansible.playbook.task_include import TaskInclude
    # from ansible.playbook.task import Task

    # import logging
    # from ansible.playbook.block import Block
    # logging.basicConfig(level=logging.DEBUG)
    # import sys
    # sys.path.append('/Users/srs/github/ansible')

    # data_list = [
    #     {'block': [
    #                 {'block': [
    #                                 {'block': [
    #                                                 {'include_role': {'name': 'gleaner_java'}},
    #                                                 {'include_role': {'name': 'gleaner_java'}},
    #                                                 {'block': [
    #                                                                 {'include_role

# Generated at 2022-06-13 08:28:47.170539
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.plugins.loader import find_plugin

    B = []
    B.append(dict(action=dict(module='include_role', args=dict(name='foo'))))
    B.append(dict(action=dict(module='include_role', args=dict(name='bar'))))

    C = []
    C.append(dict(action=dict(module='include_role', args=dict(name='foo'))))
    C.append(dict(action=dict(module='include_role', args=dict(name='bar'))))

# Generated at 2022-06-13 08:28:59.386494
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class Play(object):
        def __init__(self):
            self.hosts = 'hosts'
            self.name = 'play'
            self.serial = 10
    class Loader(object):
        def __init__(self):
            self.z = 10
        def get_basedir(self):
            return 'basedir'
    class Block(object):
        def __init__(self):
            self.parent = 'parent'
            self.role = 'role'
            self.task_include = 'task_include'
            self.loop = False
    class HandlerTaskInclude(object):
        def __init__(self):
            self.block = 'block'
            self.role = 'role'
            self.task_include = 'task_include'

# Generated at 2022-06-13 08:29:10.234141
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class DummyVars(dict):
        def get_vars(self, *args, **kwargs):
            return self

    class DummyLoader():
        def path_dwim_relative(self, *args, **kwargs):
            pass

        def path_dwim(self, *args, **kwargs):
            pass

    class DummyBlock():
        def __init__(self, name):
            self.name = name

        def get_vars(self):
            return {}


# Generated at 2022-06-13 08:29:11.729374
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # FIXME: write unit tests for this
    return True

# Generated at 2022-06-13 08:29:13.877057
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  tester = load_list_of_tasks([{'block': 'test_block'}])
  assert tester == []

# Generated at 2022-06-13 08:29:28.717112
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Faking function load_list_of_blocks
    def load_list_of_blocks(ds, play, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
        return "BLOCKS"
    # Faking class Block
    class Block:
        @staticmethod
        def load(ds, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
            return "LOADED_BLOCK"

    # Faking class Task:

# Generated at 2022-06-13 08:29:32.596255
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:29:35.794187
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    print(load_list_of_tasks('/home/kamal/ansible-v2.5.5/lib/ansible/playbook/tasks/main.yml'))
    '''
    pass

