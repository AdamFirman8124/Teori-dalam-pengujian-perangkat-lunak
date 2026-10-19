

# Generated at 2022-06-13 07:59:54.868371
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    obj = Block()
    obj.deserialize(None)


# Generated at 2022-06-13 07:59:59.394973
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    b.block=[0,1,2,3,4]
    b.rescue=[0]
    b.always=[0]
    b.has_tasks()

# Generated at 2022-06-13 08:00:02.777704
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task import Task
    b = Block()

    b.deserialize({'name': 'foo'})

    assert b._attributes['name'] == 'foo'
    assert b.name == 'foo'

# Generated at 2022-06-13 08:00:09.199452
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Unit test for method deserialize of class Block
    '''
    fake_ansible_module = AnsibleModule(
        argument_spec = dict(
            serialized = dict(required=True, type='dict'),
            loader = dict(required=True, type='dict'),
            variable_manager = dict(required=True, type='dict'),
            play = dict(required=True, type='dict')
        )
    )

    # This is the object that we are testing.
    b = Block()

    # This is the serialized block provided by the FakeModule
    serialized = fake_ansible_module.params['serialized']
    # This is the loader object provided by the FakeModule
    loader = fake_ansible_module.params['loader']
    # This is the variable_manager object provided by the FakeModule
   

# Generated at 2022-06-13 08:00:18.281184
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    assert block.deserialize({'block': [{'module': 'shell', 'args': 'rm -rf /etc/*'}]})
    assert block._play is None
    assert block.include is True
    assert block.loop is False
    assert block.freeze is False
    assert block.vars == {}
    assert block.block == [{'module': 'shell', 'args': 'rm -rf /etc/*'}]
    assert block.rescue == []
    assert block.always == []
    assert block._dep_chain == None
    assert block._role is None
    assert block._parent is None
    assert block._use_handlers == False


# Generated at 2022-06-13 08:00:20.049624
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    block.set_loader(None)
    assert block._loader is None

# Generated at 2022-06-13 08:00:21.289383
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    #Testing filter_tagged_tasks of class Block
    pass

# Generated at 2022-06-13 08:00:28.628899
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():

    # test_block: 
    # test_rescue: 
    # test_always: 
    test_block_include = None
    # test_rescue_include: 
    # test_always_include: 

    # Implicit Block
    ################################################################################
    # block1: 
    # rescue1: 
    # always1: 
    ################################################################################
    # block1: 
    # rescue1: 
    # always1: 
    ################################################################################
    # block1: 
    # rescue1: 
    # always1: 
    ################################################################################
    # block1: 
    # rescue1: 
    # always1: 
    ################################################################################
    # block1: 
    # rescue1: 


# Generated at 2022-06-13 08:00:29.717670
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    # TODO: Add your own assertions here
    return True

# Generated at 2022-06-13 08:00:35.709456
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    # AnsibleBaseYAMLObject is the parent class of Block which is the class under test
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    assert not b.has_tasks()

# Generated at 2022-06-13 08:00:52.285845
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    test_obj = Block()

    assert test_obj.deserialize({'block': [], 'rescue': [], 'always': [], 'dep_chain': None}) is None


# Generated at 2022-06-13 08:00:56.101780
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize({"_attributes": {}, "_parent": None, "_play": None, "_role": None, "_ds": None, "always": [], "block": [], "rescue": [], "_dep_chain": None, "_loader": None, "_variable_manager": None, "use_handlers": True})
    assert block is not None


# Generated at 2022-06-13 08:01:02.751369
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  from ansible.playbook.task import Task
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.handler_task_include import HandlerTaskInclude

  P = DummyPlugin()
  P.add_option( 'a', 1 )
  P.add_option( 'b', 'b' )
  P.add_option( 'c', 'c' )
  P.add_option( 'd', 'd' )

  b = Block()
  b._play = P
  b._role = P
  b._attributes = dict( a = 1, b = 'b', c = 'c', d = 'd', deps = [1,2,3] )

# Generated at 2022-06-13 08:01:05.612755
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
  print ("Test if instance method all_parents_static of class Block can be called")
  obj = Block()
  try:
    obj.all_parents_static()
  except:
    print ("Exception while calling method all_parents_static of class Block")
    raise
  return

# Generated at 2022-06-13 08:01:12.437130
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test data for test case 1
    block = {
        "name": 'Test Block',
        "block": [
            {
                "name": 'Test Task 1',
                "tags": ['tag_1']
            },
            {
                "name": 'Test Task 2',
                "tags": ['tag_2']
            }
        ]
    }

    # Test data for test case 2

# Generated at 2022-06-13 08:01:23.652266
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    print ("Starting test_Block_get_first_parent_include")
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    b1 = Block()

    b2 = Block()
    # b2.block = []
    # b2.rescue = []
    # b2.always = []

    h1 = Handler()

    t1 = Task()
    t1.action = "test"
    t1.name = "test"

    ti1 = TaskInclude()
    ti1.name = "include task1"
    ti1.tasks = [t1]

    # test case 1
    b1.block = [t1]
    b1.rescue = []
    b1.always = []

# Generated at 2022-06-13 08:01:32.057874
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    assert not b.has_tasks()
    # block is list of Task instances
    t1 = Task()
    t2 = Task()
    t3 = Task()
    b.block = [t1, t3]
    b.rescue = [t2]
    b.always = [t3]
    assert b.has_tasks()

    b.block.remove(t1)
    assert b.has_tasks()
    b.block = []
    assert b.has_tasks()

    b.rescue = []
    assert b.has_tasks()

    b.always = []
    assert not b.has_tasks()

    # block is list of Block instances
    bb = Block()
    bb.block = [t1]

# Generated at 2022-06-13 08:01:40.107973
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    import ansible.constants as C
    import ansible.inventory.host
    import ansible.inventory.group
    #input data
    h = ansible.inventory.host.Host(name="127.0.0.1")
    g = ansible.inventory.group.Group(name="all")
    g.add_host(h)

# Generated at 2022-06-13 08:01:46.574771
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert not block.has_tasks()
    block.block = [Task()]
    assert block.has_tasks()
    block.block = []
    block.rescue = [Task()]
    assert block.has_tasks()
    block.rescue = []
    block.always = [Task()]
    assert block.has_tasks()
    block.always = []
    assert not block.has_tasks()
    block.always = [Task()]
    assert block.has_tasks()

# Generated at 2022-06-13 08:01:47.083750
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    pass

# Generated at 2022-06-13 08:02:09.927018
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    B = Block()
    B.statically_loaded = True
    B._parent = Block()
    B._parent.statically_loaded = True
    assert B.all_parents_static() == True

# Generated at 2022-06-13 08:02:12.566566
# Unit test for method copy of class Block
def test_Block_copy():
    playbook = Playbook()
    play = Play().load({},playbook=playbook)
    block = Block().load({})
    copy = block.copy()



# Generated at 2022-06-13 08:02:16.631004
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    data = {'block': [{'include': u'xyz'}, {'action': u'abc'}], 'rescue': [{'action': u'def'}], 'always': [{'action': u'ghi'}]}
    b = Block(implicit=True, data=data)
    result = b.has_tasks()
    assert result == True


# Generated at 2022-06-13 08:02:17.902130
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    b.set_loader(None)
    b.set_loader('loader')

# Generated at 2022-06-13 08:02:19.273124
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    assert b.copy() is not None


# Generated at 2022-06-13 08:02:26.823526
# Unit test for method set_loader of class Block
def test_Block_set_loader():

    A = Block()
    B = Block()
    C = Block()
    B._parent = A
    C._parent = B
    
    assert(C._parent._parent == A)
    assert(A._parent == None)
    C.set_loader(None)
    assert(C._parent._loader == None)
    assert(C._parent._parent._loader == None)

# Generated at 2022-06-13 08:02:32.013124
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block = Block(task_include=None, use_handlers=False, implicit=False)
    block.block = []
    dep_chain = block.get_dep_chain()
    assert dep_chain is None

# Generated at 2022-06-13 08:02:35.783182
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    collection = Mock()
    loader = Mock()
    loader.set_collection = collection
    a = Block()
    assert a.set_loader(loader) == True


# Generated at 2022-06-13 08:02:42.707441
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    test_play = Play().load(dict(
                name = "foobar",
                hosts = "all",
                roles = ["Common", "Web"],
                gather_facts = "no",
                tasks = [
                    {"role": "Common"},
                    {"include": "role:Web"},
                    {"block": [
                        {"name": "first task", "debug": "msg=foo"},
                        {"name": "second task", "debug": "msg=bar"}
                    ]},
                ]
            ), variable_manager=VariableManager(), loader=None)
    test_play.post_validate(variable_manager=VariableManager())
    test_task = test_play.get_block_list()[0].block[1]
    assert test_task.all_parents_static() == True

# Generated at 2022-06-13 08:02:54.879855
# Unit test for method is_block of class Block
def test_Block_is_block():
    data_dict0 = {}
    assert Block.is_block(data_dict0) == True

    data_dict0 = {'block': [], 'rescue': []}
    assert Block.is_block(data_dict0) == True

    data_dict0 = 'the quick brown fox jumps over the lazy dog.'
    assert Block.is_block(data_dict0) == False

    data_dict0 = [
        'the quick brown fox jumps over the lazy dog.',
        'the quick brown fox jumps over the lazy dog.',
        'the quick brown fox jumps over the lazy dog.',
        ]
    assert Block.is_block(data_dict0) == False


# Generated at 2022-06-13 08:03:12.613353
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    try:
        b.has_tasks()
    except Exception as e:
        assert(False)
    else:
        assert(True)


# Generated at 2022-06-13 08:03:21.025263
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
  # Test case 1, filter_tagged_tasks
  if True:
    # Instantiate an object of class Block, with possible values for
    # use_handlers, implicit, and dynamically_loaded, which are all False
    test_obj = ansible.playbook.block.Block(use_handlers=False, implicit=False, dynamically_loaded=False)
    # Instantiate an object of class Play, with possible values for
    # name, hosts, roles, and skip_tags
    test_subject_1 = ansible.playbook.play.Play(name=None, hosts=None, roles=None, skip_tags=None)
    test_subject_2 = None
    test_subject_3 = None
    test_subject_4 = None
    test_subject_5 = None
    test_subject_6 = None
    test_subject

# Generated at 2022-06-13 08:03:24.129336
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    try:
        block.copy("exclude_parent", "exclude_tasks")
    except Exception as exception:
        assert(isinstance(exception, TypeError))


# Generated at 2022-06-13 08:03:28.943702
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    import ansible.playbook.block
    b1 = ansible.playbook.block.Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False)
    assert b1.get_dep_chain() == None
    return

# Generated at 2022-06-13 08:03:36.420161
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    m = mock.mock_open()
    with mock.patch("ansible.parsing.yaml.open", m, create=True):
        d = yaml.safe_load("""
- hosts: localhost
  remote_user: root
  tasks:
  - fail
""")
        b.load_data(d)


# Generated at 2022-06-13 08:03:42.379370
# Unit test for method copy of class Block
def test_Block_copy():
    """ Unit test for `Block.copy` """
    # Fixtures
    block = ansible.playbook.block.Block()
    return ansible.playbook.block.Block.copy(block, exclude_parent=False, exclude_tasks=False)


# Generated at 2022-06-13 08:03:49.122906
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler import Handler
    import ansible
    import sys
    class Block_Test_Class(unittest.TestCase):
        '''
        This is a generic unittest for the filter_tagged_tasks method of the
        Block class.
        '''
        def test_filter_tagged_tasks(self):
            '''
            This test exercises the filter_tagged_tasks method of the
            Block class.
            '''
            # Generic play context used for test
            play_context = PlayContext()
            # Generic play used for test

# Generated at 2022-06-13 08:04:00.616846
# Unit test for method is_block of class Block
def test_Block_is_block():
    def test_loader(loader, path, cache=False):
        if not path.endswith('.yaml'):
            raise AnsibleParserError("the test expects the path to end with .yaml")
        data = dict(
            a=1, b=2
        )
        return data

    filename = 'test_Block.yaml'
    name = 'test_Block'
    role = Role()
    role._role_path = '/path/to/roles/a'

# Generated at 2022-06-13 08:04:09.533062
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    values = {'ds': {'a': 'asdf', 'rescue': 'foo', 'always': 'bar'}}
    b = Block(**values)
    assert b.get_dep_chain() is None, b.get_dep_chain()
    b_table = Table(name='table', parent=b, hostname='192.168.121.11')
    b_table_table = Table(name='table', parent=b_table, hostname='192.168.121.11')
    b._dep_chain = [b_table_table]
    assert b_table._dep_chain == ['table']
    assert b_table_table._dep_chain == ['table']
    assert b.get_dep_chain() == ['table']
    b._dep_chain = None

# Generated at 2022-06-13 08:04:19.329794
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    data = dict(
        block=[
            dict(name='frist task'),
            dict(name='second task'),
            dict(name='third task'),
            dict(name='fourth task'),
            dict(name='fifth task'),
            dict(name='sixth task'),
            dict(name='seventh task')
        ]
    )
    b = Block.load(data)
    assert b.has_tasks() == True

    data1 = dict(
        block=[]
    )
    b = Block.load(data1)
    assert b.has_tasks() == False


# Generated at 2022-06-13 08:04:42.724191
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():

    m = MagicMock
    ans = Block()
    ans.get_dep_chain = m(return_value = None)
    assert ans.get_dep_chain() == None

    mock_type(ans, '_dep_chain', Sentinel)
    mock_type(ans, '_parent', Block)
    ans.get_dep_chain = m(return_value = [])
    ans._parent.get_dep_chain = m(return_value = [])
    assert ans.get_dep_chain() == []

    mock_type(ans, '_dep_chain', Sentinel)
    mock_type(ans, '_parent', Block)
    ans.get_dep_chain = m(return_value = [])
    ans._parent.get_dep_chain = m(return_value = None)
    assert ans.get_

# Generated at 2022-06-13 08:04:50.017929
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for the filter_tagged_tasks method of a Block object.
    '''

# Generated at 2022-06-13 08:04:55.583119
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    """
    Test that the given Block object has a loader object as an attribute.
    """
    # Create a mock object of class Play, give it a dummy inventory
    mock_play = mock.Mock(spec=Play)
    mock_play.inventory = '127.0.0.1'
    # Create a mock object of class PlayContext, give it a dummy variable_manager
    mock_play_context = mock.Mock(spec=PlayContext)
    mock_play_context.variable_manager = 'dummy variable manager'
    # Create a mock object of class Block, give it the mock objects of class Play and PlayContext
    test_block = Block(play=mock_play, role=None, task_include=None, use_handlers=True, implicit=False)
    test_block.set_loader('dummy loader')

# Generated at 2022-06-13 08:05:07.701750
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    block = Block()
    # first case
    task_include = TaskInclude()
    block._parent = task_include
    assert block.get_first_parent_include() == task_include
    # second case
    handler_task_include = HandlerTaskInclude()
    block._parent = handler_task_include
    assert block._parent.get_first_parent_include() == task_include
    block._parent = block
    assert block.get_first_parent_include() == task_include


# Generated at 2022-06-13 08:05:09.262903
# Unit test for method copy of class Block
def test_Block_copy():
    obj = Block()
    obj.copy()
    obj.copy(exclude_parent=True)
    obj.copy(exclude_tasks=True)

# Generated at 2022-06-13 08:05:20.031847
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    # Create a block with the required fields
    block = Block()
    setattr(block, '_role', None)
    setattr(block, '_valid_attrs', ['a'])
    setattr(block, '_attributes', {'a': '1'})
    setattr(block, '_dep_chain', None)
    setattr(block, '_parent', 'parent')
    setattr(block, '_play', 'play')
    setattr(block, '_ds', {'a': '1'})
    setattr(block, '_loader', 'loader')
    setattr(block, '_variable_manager', 'variable_manager')

    # Create a role
    role = Role()
    setattr(role, '_role_name', 'name')

# Generated at 2022-06-13 08:05:22.672843
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # setup
    from ansible.playbook.block import Block
    b = Block()
    assert b.get_first_parent_include() is None
    # test
    # teardown



# Generated at 2022-06-13 08:05:32.720664
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    import tempfile
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.errors import AnsibleParserError
    from ansible.plugins.loader import lookup_loader
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_no

# Generated at 2022-06-13 08:05:42.321850
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    inventory = InventoryManager(loader=DataLoader(), sources=['localhost'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    play_context = PlayContext()

# Generated at 2022-06-13 08:05:57.231742
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    task_list = [
        Task(action='a'),
        Task(action='a', tags=['a', 'b']),
    ]
    block_list = [
        Block(block=task_list),
        Task(action='a', tags=[['a']]),
        Task(action='a')
    ]
    parent = Block(block=block_list)

    # Test whether only tasks are filtered
    generated_list = parent.filter_tagged_tasks([])
    for task in generated_list.block:
        assert not isinstance(task, Block)
    generated_list = generated_list.block
    assert generated_list[0].action == 'a'

    # Test whether only tasks are filtered

# Generated at 2022-06-13 08:06:47.619158
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for method filter_tagged_tasks of class Block
    '''

    import json
    import os

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.playbook import Playbook

    with open(os.path.join(os.path.dirname(__file__), 'datastore.json')) as f:
        datastore = json.load(f)


# Generated at 2022-06-13 08:06:58.121692
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    ## Setup the role and variable manager
    role = Role()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(v1='value1')
    variable_manager.options_vars = dict(v2='value2')
    ## Setup the block
    parent_block = Block(playbook=Playbook().load(dict(name='parent')), role=role, variable_manager=variable_manager)

# Generated at 2022-06-13 08:07:04.545174
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:07:06.583472
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize({})


# Generated at 2022-06-13 08:07:17.581839
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 08:07:24.636359
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    [Unit test for Block class]
    '''
    import json
    import os
    import sys

    # Playbook containing block with tasks
    playbook = '''
        - hosts: localhost
          connection: local
          gather_facts: false

          tasks:

          - name: block with task
            block:
              - debug:
                  msg: "This task should be executed"
              - debug:
                  msg: "This task should be executed"
              - block:
                  - debug:
                      msg: "This task should be executed"
                  - debug:
                      msg: "This task should be executed"
            tags:
              - block

        '''
    sys.argv.append('-')
    sys.argv.append('-e')
    sys.argv.append('{}')
    sys.arg

# Generated at 2022-06-13 08:07:26.126055
# Unit test for method set_loader of class Block
def test_Block_set_loader():

    m = Block()
    m.set_loader(None)
    m.set_loader('loader')



# Generated at 2022-06-13 08:07:35.279804
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    import copy
    import __main__
    import sys
    setattr(__main__,'__file__',sys.argv[0])
    b=Block()
    b._dep_chain=["deps","dep_chain"]
    assert b.get_dep_chain() == ["deps","dep_chain"]
    dep_chain = b.get_dep_chain()
    # assert dep_chain[1] == 'dep_chain'
    # assert dep_chain[0] == 'deps'

    b = Block()
    b.parent = 'parent'
    p = Block()
    p.parent = 'grandparent'
    gp = Block()
    b._parent = p
    p._parent = gp
    assert b.get_dep_chain() is None

    b = Block()
    b.parent = 'parent'

# Generated at 2022-06-13 08:07:42.096816
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert block.has_tasks() == False

    class Task(object):
        def __init__(self, action):
            self.action = action

    task1 = Task(1)
    task2 = Task(1)
    task3 = Task(1)
    task4 = Task(1)
    task5 = Task(1)

    block.block = [task1]
    block.rescue = [task2]
    block.always = [task3]

    assert block.has_tasks() == True

    block.block = []
    assert block.has_tasks() == False

    block.block = [task1, task2]
    block.rescue = []
    assert block.has_tasks() == True

    block.always = [task3, task4, task5]


# Generated at 2022-06-13 08:07:49.701453
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    import ansible.playbook
    import ansible.inventory
    import ansible.constants as C
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    hosts = [
        Host(name="hostname1", port=22),
        Host(name="hostname2", port=22),
        Host(name="hostname3", port=22),
        Host(name="hostname4", port=22),
        Host(name="hostname5", port=22)
    ]

    inventory = ansible.inventory.Inventory(hosts)
    variable_manager

# Generated at 2022-06-13 08:08:41.534065
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    data = dict()
    data['always'] = dict()
    data['block'] = dict()
    data['rescue'] = dict()
    data['block'] = [dict(asdf=True), dict(blah=True)]
    block = Block.load(data)
    assert block._ds == dict(block=[dict(asdf=True), dict(blah=True)])

# Generated at 2022-06-13 08:08:43.318274
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    assert b.has_tasks() == False

# Generated at 2022-06-13 08:08:52.101875
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.base import Base
    from ansible.playbook import Play
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.block import Block
    from ansible.utils.vars import combine_vars
    b = Block()
    p = Play().load('- hosts: all')

    # test without setting loader

    try:
        b.set_loader()
    except AnsibleParserError as exception:
        assert exception.message == 'No loader found for the block'

    # test with play

    b._play = p

    try:
        b.set_loader()
    except AnsibleParserError as exception:
        assert exception.message == 'No loader found for the block'

    # test with loader


# Generated at 2022-06-13 08:08:53.183793
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    assert True # TODO: implement your test here


# Generated at 2022-06-13 08:08:59.356406
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
  block = Block(parent_block=None)
  block.statically_loaded = True
  parent = Block(parent_block=None)
  parent.statically_loaded = True
  parent1 = Block(parent_block=parent)
  parent1.statically_loaded = True
  parent2 = Block(parent_block=parent)
  parent2.statically_loaded = True
  parent3 = Block(parent_block=parent1)
  parent3.statically_loaded = True
  child = Block(parent_block=parent3)
  child.statically_loaded = True
  child.all_parents_static()



# Generated at 2022-06-13 08:09:01.883730
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # - Setup
    # - Exercise
    # - Verify
    # - Cleanup
    pass


# Generated at 2022-06-13 08:09:11.915145
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.include_role import IncludeRole


# Generated at 2022-06-13 08:09:18.020019
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    block_no = b.has_tasks()
    assert not block_no
    b = Block(rescue=[])
    block_yes = b.has_tasks()
    assert block_yes
    b = Block(always=[])
    block_yes = b.has_tasks()
    assert block_yes
    b = Block(block=[])
    block_yes = b.has_tasks()
    assert block_yes

# Generated at 2022-06-13 08:09:26.128159
# Unit test for method copy of class Block
def test_Block_copy():
    # Set up test environment
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='tests/inventory')
    variable_manager.set_inventory(inventory)
    #testdeps = [dict(name='bob'), dict(name='joe')]
    testdeps = [dict(name='bob')]
    testblock = Block()
    testblock._dep_chain = testdeps
    testblock.when = 'test'
    testrole = Role()
    testrole.name = 'testrole'
    testblock._role = testrole
    testblock.block = [dict(name='first'), dict(name='second')]
    testblock.rescue = [dict(name='rescue')]
    testblock.always

# Generated at 2022-06-13 08:09:35.066863
# Unit test for method has_tasks of class Block