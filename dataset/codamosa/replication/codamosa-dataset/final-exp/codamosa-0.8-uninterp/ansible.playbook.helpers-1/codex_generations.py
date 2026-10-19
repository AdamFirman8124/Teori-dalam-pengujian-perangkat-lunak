

# Generated at 2022-06-13 08:21:17.375234
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True


# Generated at 2022-06-13 08:21:28.708402
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # setup
    from ansible.playbook.task import Task
    from ansible.compat import mock

    class TmpMock(object):
        def __init__(self):
            self.var1 = 'val1'
        def __getitem__(self, key):
            return self.var1
        def __setitem__(self, key, val):
            self.var1 = val

    vmanager = mock.MagicMock()

    # test tasks

# Generated at 2022-06-13 08:21:29.324126
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:21:36.808167
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources=["localhost"])
    variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)

# Generated at 2022-06-13 08:21:40.621471
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    a = load_list_of_tasks(ds, play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    print(a)

# This is a test function

# Generated at 2022-06-13 08:21:46.003999
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # Check when task is list
    assert load_list_of_tasks([], None, None) == []

    # Check with AnsibleAssertionError
    # Check when task is list
    assert load_list_of_tasks(['sample'], None, None) == []

# Generated at 2022-06-13 08:21:47.094977
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: add test
    pass

# Generated at 2022-06-13 08:21:59.512878
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:22:14.442508
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # AnsibleUndefinedVariable
    task_ds = [
        {'action': 'include', 'include': '{{ var1 }}'},
        {'action': 'include', 'include': '{{ var2 }}'},
        {'name': 'test'}
    ]
    play = dict()
    block = None
    role = None
    task_include = None
    use_handlers=False
    variable_manager = MagicMock()
    variable_manager.get_vars = MagicMock()
    templar = MagicMock()
    templar.is_template = MagicMock(return_value=True)
    loader = MagicMock()

# Generated at 2022-06-13 08:22:19.417074
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    context = PlayContext()
    context._variable_manager = variable_manager
    context._loader = loader
    tasks = load_list_of_tasks([], context)
    assert isinstance(tasks, list)

# Generated at 2022-06-13 08:22:50.675384
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_data = []
    for i in range(10):
        ds = {'block':{'name':'test_block','tasks':[]}}

# Generated at 2022-06-13 08:23:01.718443
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    t1 = Task()
    t2 = TaskInclude()
    t3 = HandlerTaskInclude()
    t4 = Block()

    t1.module_name = 'test_module'
    t2.module_name = 'test_module'
    t3.module_name = 'test_module'
    t4.module_name = 'test_module'

    t1.loop = None
    t2.loop = None
    t3.loop = None
    t4.loop = None


# Generated at 2022-06-13 08:23:11.515351
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    test_play = {
        'name': 'test play',
        'hosts': 'all',
        'roles': [
            {'role': 'some_role'},
        ]
    }
    assert type(load_list_of_roles(ds=test_play['roles'], play=Play().load(test_play, loader=DictDataLoader()))) == list
    assert len(load_list_of_roles(ds=test_play['roles'], play=Play().load(test_play, loader=DictDataLoader()))) == 1

    return True


# Generated at 2022-06-13 08:23:20.862437
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.module_utils._text import to_bytes, to_text

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()


# Generated at 2022-06-13 08:23:32.526201
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
  import inspect
  import sys
  import os

  path_curfolder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
  path_test_utils = os.path.realpath(os.path.abspath(os.path.join(path_curfolder,"../../utils")))
  if path_test_utils not in sys.path:
    sys.path.insert(0, path_test_utils)

  print ("load_list_of_blocks")
  #print (load_list_of_blocks(ds, play, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
  # load_list_of_blocks(ds,

# Generated at 2022-06-13 08:23:41.844778
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:23:49.416539
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    #### Test Cases
    ## case 1
    print("case 1")
    ds = "test"

    try:
        load_list_of_tasks(ds, None)
        assert False, "AssertionError is not raised"
    except AnsibleAssertionError as e:
        assert e is not None

    ## case 2
    print("case 2")
   

# Generated at 2022-06-13 08:23:58.428358
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude


# Generated at 2022-06-13 08:24:09.961036
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    result = load_list_of_tasks(None,None,None,None,None,None,None,None)
    assert result == []
    result = load_list_of_tasks("sdfsdfsdfsdfsdfs",None,None,None,None,None,None,None)
    assert result == "sdfsdfsdfsdfsdfs"
    result = load_list_of_tasks(1234,None,None,None,None,None,None,None)
    assert result == 1234
    result = load_list_of_tasks([],None,None,None,None,None,None,None)
    assert result == []


# Generated at 2022-06-13 08:24:10.622667
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False



# Generated at 2022-06-13 08:24:54.030054
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.errors import AnsibleAssertionError
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    a = load_list_of_tasks((1,2), [], [])
    assert a[1] is None
    a = load_list_of_tasks(1, [], [])
    assert a[1] is None
    try:
        a = load_list_of_tasks(1, [], [])
    except AnsibleAssertionError:
        pass

# Generated at 2022-06-13 08:25:04.190262
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import IncludeRole
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.recursive import action_plugins as recursive_action_plugins
    from ansible.plugins.recursive import connection_plugins as recursive_connection

# Generated at 2022-06-13 08:25:19.464462
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.base import Base

    class MyBase(Base):
        _load_name = 'base'

        def get_name(self):
            return self._load_name

    class MyTask(MyBase):
        pass

    class MyInclude(MyBase):
        pass

    class MyBlock(MyBase):
        pass

    class MyPlay(MyBase):
        def serialize(self):
            return dict()

    class MyRole(MyBase):
        def serialize(self):
            return dict()

    class ModuleArgsParser(object):
        def __init__(self, data):
            self.data = data

        def parse(self, skip_action_validation=False):
            return self.data['action'], self.data, None


# Generated at 2022-06-13 08:25:25.627480
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    ds =[
            {'include_tasks': '/test/test.yaml'},
            {'include_tasks': '/test/test.yaml'},
            'a'
    ]
    if not isinstance(ds, (list, type(None))):
        raise AnsibleAssertionError('%s should be a list or None but is %s' % (ds, type(ds)))

    task_list = []
    if ds:
        count = iter(range(len(ds)))
        for i in count:
            task_ds = ds[i]
            # Implicit blocks are created by bare

# Generated at 2022-06-13 08:25:39.141955
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # foo.yml
    ds = [
        {'debug': 'msg=play-1'},
        {'include_tasks': 'bar.yml'},
        {'block': [
            {'debug': 'msg=block-1'},
            {'include_tasks': 'baz.yml'},
            {'debug': 'msg=block-2'},
            {'block': [
                {'debug': 'msg=block-1-1'},
            ]},
        ]},
        {'include_tasks': 'bar.yml'},
    ]

    # bar.yml

# Generated at 2022-06-13 08:25:47.489468
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play.load(
        dict(
            name="Ansible Play",
            hosts='all',
            gather_facts='no',
            roles=[dict(name='common', tasks=[dict(action=dict(module='shell', args='whoami'))])]
        ),
        variable_manager=variable_manager,
        loader=loader,
    )

# Generated at 2022-06-13 08:25:48.637261
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # TODO: Implement unit test for load_list_of_roles
    pass


# Generated at 2022-06-13 08:26:01.453351
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    run tests for load_list_of_tasks function
    :return:
    '''

    import os, sys
    import tempfile
    import types
    import copy

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    from units.compat import unittest

    # prep
    loader, inventory, variable_manager = AnsibleModuleTest.get_loader()

# Generated at 2022-06-13 08:26:09.503892
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-13 08:26:19.498339
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    from ansible.errors import AnsibleParserError
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    obj = AnsibleMapping(None)
    obj._data = [('name', AnsibleUnicode('debug')), ('delegate_to', AnsibleUnicode('localhost')), ('register', AnsibleUnicode('debug_result'))]

# Generated at 2022-06-13 08:27:19.828801
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_ds1 = {'action': 'copy', 'src': 'test.txt','dest': 'test2.txt'}
    task_ds2 = {'block': [{'action': 'copy', 'src': 'test.txt', 'dest': 'test2.txt'}]}
    task_ds3 = {'action': 'import_tasks', 'include': 'test.yml'}
    task_ds4 = {'action': 'include_tasks', 'static': 'yes'}

    task_ds_list = [task_ds1, task_ds2, task_ds3, task_ds4]
    try:
        assert load_list_of_tasks(task_ds_list, task_ds1, task_ds2, 'role')
    except Exception as e:
        print(e)

# Generated at 2022-06-13 08:27:31.570768
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print("TESTING LOAD LIST OF TASKS")
    print("TESTING LOAD LIST OF TASKS: LOAD_LIST_OF_TASKS_1")
    # TESTING LOAD LIST OF TASKS: LOAD_LIST_OF_TASKS_1
    # Empty data structure
    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    ds = None
    play = Play().load({}, {}, variable_manager=VariableManager(), loader=DataLoader())
    block = None
    role = None
    task_include = None
    use_handlers = False
    #variable_manager = None
    loader = DataLoader()
    #assert load_list

# Generated at 2022-06-13 08:27:35.554688
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(ds=[], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) == []

# Generated at 2022-06-13 08:27:48.418405
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [
        {
            'include_role': {
                'name': 'test'
            }
        },
        {
            'include_tasks': 'test.yml'
        },
        {
            'name': 'test'
        }
    ]
    play = Play()
    play._ds = ds
    try:
        load_list_of_tasks(ds, play)
    except AnsibleAssertionError as e:
        if 'should be a dict but was a' in str(e):
            assert True
        else:
            assert False
    except:
        assert False

    ds = {
            'name': 'test'
    }

# Generated at 2022-06-13 08:27:58.906648
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  assert(load_list_of_tasks([{
    "include_role": {
        "name": "test",
        "tasks_from": "main"
    }
  }]) == [{
    "include_role": {
        "name": "test",
        "tasks_from": "main"
    }
  }])

  assert(load_list_of_tasks([{
    "include_role": {
        "name": "test",
        "tasks_from": "main"
    }
  },{
    "name": "testing"
  }]) == [{
    "include_role": {
        "name": "test",
        "tasks_from": "main"
    }
  }])


# Generated at 2022-06-13 08:28:05.561505
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
        load_list_of_roles test
    '''
    fake_loader = DictDataLoader()
    fake_loader.set_basedir(os.path.join(os.path.dirname(__file__), '../fixtures/role_source/'))
    my_collection_list = collections.CollectionsSearchList()
    my_collection_list.add_collections_from_list([
        'ansible_collections.community.general',
        'ansible_collections.my_namespace.my_collection'
    ])
    my_collection_list.add_collections(os.path.join(os.path.dirname(__file__), '../fixtures/role_source/ansible_collections/my_namespace/my_collection'))
    my_collection_list.add_

# Generated at 2022-06-13 08:28:10.737644
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook
    import ansible.vars.manager
    import ansible.constants
    ds = ''
    play = None # TODO: implement load_play
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = ansible.vars.manager.VariableManager()
    loader = ansible.parsing.dataloader.DataLoader()
    ret = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(ret, list)
    #assert len(ret) >= 1

# Generated at 2022-06-13 08:28:24.800669
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:28:36.260443
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.template import Templar
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible import context
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    # Setup test data
    context._init_global_context(['fake_bin_path'])
    loader = DataLoader()
    # host = Host(name="fake_host")
    # group = Group(name="fake_group")
    # group.add_host(host)
    inventory = MockInventory()

# Generated at 2022-06-13 08:28:47.145817
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role_include import IncludeRole

    playbook = Playbook.load("../../test_playbooks/playbook.yml", variable_manager=None, loader=None)
    play = Play().load(playbook.get_plays_dict()['all'], variable_manager=None, loader=None)

    role_name = 'foo'
    ds = [{'include_role': {'name': role_name}}]
