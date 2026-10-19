

# Generated at 2022-06-13 08:00:14.386970
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude

    # Create a valid data structure
    data = dict()
    data['when'] = [True]
    data['block'] = [Task()]
    data['rescue'] = [Task()]
    data['always'] = [Task()]
    data['role'] = dict()
    data['parent'] = dict()
    data['parent']['when'] = [True]
    data['parent']['block'] = [Task()]
    data['parent']['rescue'] = [Task()]
    data['parent']['always'] = [Task()]
    data['parent']['role'] = dict()

# Generated at 2022-06-13 08:00:23.786972
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    BLOCK = "block"
    BLOCK_LIST = "block_list"
    BLOCK_DICT = "block_dict"
    RESCUE = "rescue"
    RESCUE_LIST = "rescue_list"
    RESCUE_DICT = "rescue_dict"
    ALWAYS = "always"
    ALWAYS_LIST = "always_list"
    ALWAYS_DICT = "always_dict"

    # Must be a list of block dictionaries
    result = Block.preprocess_data(BLOCK_LIST)
    assert isinstance(result, dict), "result must be a dictionary"
    assert len(result) == 1, "result must only have one element"
    assert BLOCK in result
    assert isinstance(result[BLOCK], list)
    assert result[BLOCK] == BLOCK_LIST
    #

# Generated at 2022-06-13 08:00:35.197291
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    class_ = Block
    module_name = 'ansible.playbook.block'
    method_name = 'deserialize'
    args = dict(
        self=None,
    )
    # populate the test function args with argument spec from the test case entry
    arguments = inspect.getargspec(class_.deserialize).args
    for arg in arguments[:len(arguments) - len(inspect.getargspec(class_.deserialize).defaults)]:
        if args.get(arg) is None:
            args[arg] = None
    # Override mandatory (positional) arguments with the actual test function args
    args.update(dict(
        self=0,
    ))
    # Run the test method
    # We expect the following exception:
    #     raise AnsibleError(message)

# Generated at 2022-06-13 08:00:42.576426
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    #create a task
    task_1= Task()
    task_1._attributes['name']='task_1'
    task_1._attributes['action']='copy'
    task_1._attributes['args']= {'src':"/test/test_src",'dest': "/test/test_dest"}
    task_1_tags=['test_tags']
    task_1._attributes['tags']= task_1_tags

    #create a task
    task_2= Task()
    task_2._attributes['name']='task_2'
    task_2._attributes['action']='script'
    task_2._attributes['args']= {'src':"/test/test_src",'dest': "/test/test_dest"}

# Generated at 2022-06-13 08:00:47.033300
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    hosts = [{'name': 'localhost', 'connection': 'local'}]
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(Inventory(loader=loader, hosts=hosts))
    b = Block()
    b.set_loader(loader)


# Generated at 2022-06-13 08:00:50.726714
# Unit test for method is_block of class Block
def test_Block_is_block():
  play = None
  parent_block = None
  role = None
  task_include = None
  use_handlers = False
  b = Block(play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers)
  assert  b.is_block()


# Generated at 2022-06-13 08:00:53.876801
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    # from ansible.playbook.block import Block
    # block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=None, implicit=None)
    assert False # TODO: implement your test here



# Generated at 2022-06-13 08:00:56.131677
# Unit test for method is_block of class Block
def test_Block_is_block():
    print('')
    print('UNIT TEST FOR is_block of class Block:')
    print('')
    b = Block()
    a = b.is_block( {} )
    print(a)

# Generated at 2022-06-13 08:00:59.262954
# Unit test for method is_block of class Block
def test_Block_is_block():
    '''
    is_block() return true if the given data structure is a block
    '''
    ds = { "block": [] }
    assert(Block.is_block(ds) == True)

    ds = { "blk": [] }
    assert(Block.is_block(ds)==False)

# Generated at 2022-06-13 08:01:07.041239
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    if __name__ == '__main__':
        '''
        b = Block(
            block=['1', '2', '3'],
            rescue=[{'block': ['a', 'b', 'c']}],
            always=['x', 'y', 'z'],
        )
        '''
        b = Block()
        b._attributes['block'] = ['1', '2', '3']
        b._attributes['rescue'] = [{'block': ['a', 'b', 'c']}]
        b._attributes['always'] = ['x', 'y', 'z']

# Generated at 2022-06-13 08:01:45.147236
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    copy = None

    # Create a new context object
    context_object = {}

    # Create a new AnsibleModule object
    module = AnsibleModule()

    # Create a new Block object
    block = Block(loader=TestLoader(), variable_manager=TestVariableManager(), play=TestPlay())
    block.deserialize(context_object)

    assert isinstance(copy, Block) is True, 'Block.deserialize() did not return the expected data type'
    assert block._play == (TestPlay()), 'Block.deserialize() did not return the expected data type'
    assert block._use_handlers == (False), 'Block.deserialize() did not return the expected data type'

# Generated at 2022-06-13 08:01:46.467098
# Unit test for method is_block of class Block
def test_Block_is_block():
    block = Block.load(dict(block=[]))
    assert Block.is_block(block) == True


# Generated at 2022-06-13 08:01:54.112510
# Unit test for method get_dep_chain of class Block

# Generated at 2022-06-13 08:02:05.744148
# Unit test for method copy of class Block
def test_Block_copy():
    # Test with keyword arguments
    b = Block()
    b.copy(exclude_parent=True)
    b.copy(exclude_tasks=True)
    b.copy(exclude_parent=True,exclude_tasks=True)
    # Test with kwargs
    b.copy(**{'exclude_parent':True})
    b.copy(**{'exclude_tasks':True})
    b.copy(**{'exclude_parent':True,'exclude_tasks':True})
    b1 = Block()
    b2 = b1.copy(exclude_parent=True)
    b3 = b1.copy(exclude_tasks=True)
    b4 = b1.copy(exclude_parent=True,exclude_tasks=True)
    assert b1 != b

# Generated at 2022-06-13 08:02:14.251201
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    pb1 = Block()
    pb2 = Block()
    t1 = TaskInclude()
    t2 = TaskInclude()
    b1 = Play()

    pb1.statically_loaded = False
    pb1._parent = pb2
    pb2._parent = t1
    t1._parent = t2
    t2._parent = b1

    assert pb1.all_parents_static()
# END Unit test for method all_parents_static of class Block

# Generated at 2022-06-13 08:02:20.496851
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    sp = AnsibleLoader(None, None)
    block = sp.load(to_text("""
- block:
  - name: first block
    shell: echo test1
    tags:
      - tag1
  rescue:
    - name: first rescue
      shell: echo test1
      tags:
        - tag1
  always:
    - name: first always
      shell: echo test1
      tags:
        - tag1
"""), play=None, variable_manager=None, loader=None)

    assert block.all_parents_static()
    assert not block.block[0].all_parents_static()
    assert not block.rescue[0].all_parents_static()
    assert not block.always[0].all_parents_static()



# Generated at 2022-06-13 08:02:24.714718
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    def test_create_block():
        block = Block(block=[]) #@UnusedVariable
        return block
    test_create_block()


# Generated at 2022-06-13 08:02:38.284679
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # create block with empty task block, rescue and always blocks
    block = Block(block=[])
    # assert block has no tasks
    assert not block.has_tasks()

    # create block with empty task block and empty rescue and always blocks
    block = Block(block=[], rescue=[], always=[])
    # assert block has no tasks
    assert not block.has_tasks()

    # create block with task block and empty rescue and always blocks
    block = Block(block=['task'])
    # assert block has no tasks
    assert block.has_tasks()

    # create block with empty task block and rescue and always blocks
    block = Block(block=[], rescue=['rescue'], always=['always'])
    # assert block has no tasks
    assert block.has_tasks()

# Generated at 2022-06-13 08:02:43.006626
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    ds = [{"set_fact": {"test": "value"}}]
    block = Block()
    assert(block.preprocess_data(ds) == {"block": [{"set_fact": {"test": "value"}}]})


# Generated at 2022-06-13 08:02:54.944527
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    context = PlayContext()
    inventory = InventoryManager(loader=loader, sources=yaml.safe_load("""
        all:
          hosts:
            localhost:
        """)
    )
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:03:32.156842
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    T = Task()
    R = Role()
    B = Block()
    T._parent = B
    B._dep_chain = [R]
    assert T.get_dep_chain() == B.get_dep_chain()
    assert T.get_dep_chain() == [R]


# Generated at 2022-06-13 08:03:33.599085
# Unit test for method is_block of class Block
def test_Block_is_block():
    # TODO
    pass

# Generated at 2022-06-13 08:03:46.571109
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    '''
    Block.set_loader
    '''
    # pylint: disable=protected-access
    # pylint: disable=too-many-lines
    # pylint: disable=line-too-long
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-locals
    # pylint: disable=unused-variable
    # pylint: disable=invalid-name
    # pylint: disable=too-many-nested-blocks
    # pylint: disable=too-many-return-statements
    # pylint: disable=too-many-arguments
    ########################################################
    # mock objects:

# Generated at 2022-06-13 08:03:55.372564
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Block.copy()
    '''
    b = Block(use_handlers=True)
    b.block = [ 'b' ]
    b.rescue = [ 'r' ]
    b.always = [ 'a' ]

    b2 = b.copy()
    assert b2.block == b.block
    assert b2.rescue == b.rescue
    assert b2.always == b.always


# Generated at 2022-06-13 08:04:06.844898
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    assert block is not None
    assert block.hosts == 'all'
    assert block.block == []
    assert block.rescue == []
    assert block.always == []
    assert block.tags == []
    assert block.name == ''
    assert block.when == ''
    assert block.changed_when == ''
    assert block.failed_when == ''
    assert block.dep_chain == None
    assert block.any_errors_fatal == False
    assert block.any_unreachable_fatal == False
    assert block.had_task_run == False
    assert block.has_tasks() == False
    assert block.always_run == False
    assert block.implicit == False
    assert block.implicit_block == False
    assert block.implicit_rescue == False

# Generated at 2022-06-13 08:04:21.269333
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

# Generated at 2022-06-13 08:04:24.706443
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
	block = Block(play=None,parent_block=None,role=None,task_include=None, implicit=None, static_task_include=None, use_handlers=None)
	return isinstance(block.has_tasks(),bool)


# Generated at 2022-06-13 08:04:31.856933
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    def helper(block_str, only_tags, skip_tags, expected_output_str):
        from ansible.playbook.task_include import TaskInclude
        # Helper method to create a TaskInclude object

        # Create a Block object with the data specified in block_str
        block = Block.load(ds=block_str)
        assert isinstance(block, Block)

        # Create a TaskInclude object
        first_parent_include = TaskInclude()
        first_parent_include.statically_loaded = True

        # Create a play object that contains the only_tags and skip_tags
        class FakePlay(object):
            def __init__(self, only_tags, skip_tags):
                self.only_tags = only_tags
                self.skip_tags = skip_tags

# Generated at 2022-06-13 08:04:40.686026
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:04:42.540481
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    assert block.deserialize(block) is None


# Generated at 2022-06-13 08:05:16.442584
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Tests that an empty Block object returns an empty object
    b = Block()
    new_b = b.filter_tagged_tasks({})
    assert not new_b.has_tasks()



# Generated at 2022-06-13 08:05:22.357162
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Unit test for method deserialize of class Block
    '''

    import pprint

    # initialize object
    b = Block()

    # handle success case
    data = dict()

    try:
        #pdb.set_trace()
        b.deserialize(data)
        pprint.pprint('Success')
    except Exception as e:
        pprint.pprint('Failed')
    finally:
        pprint.pprint('End')



# Generated at 2022-06-13 08:05:31.243599
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    #Creating a block object to test the all_parents_satic method
    b = Block(play=play, parent_block=parent_block, role=role, task_include=task_include, use_handlers=use_handlers, implicit=implicit)
    #case 1: when parent is not present
    if(b._parent):
        if isinstance(b._parent, TaskInclude):
            assert(b._parent.all_parents_static() == b._parent.statically_loaded)
        else:
            assert(b._parent.all_parents_static())
    #case 2:when parent is present
    else:
        assert(True)


# Generated at 2022-06-13 08:05:37.815163
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    import sys
    import io
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    data = dict(
        block=dict(
            tasks=[
                dict(action=dict(module="debug", args=dict())),
                dict(action=dict(module="debug", args=dict()))]
        )
    )
    block = Block.load(data, variable_manager=VariableManager(), loader=None)
    block.set_loader(None)


# Generated at 2022-06-13 08:05:39.266644
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    pass

# Generated at 2022-06-13 08:05:42.310151
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # unit test for method all_parents_static of class Block
    a = AnsibleVaultEncryptedUnicode('ASN1.1 DEF')
    assert Block(a).all_parents_static() == True

# Generated at 2022-06-13 08:05:57.231262
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task_include import TaskInclude

    loader = Data

# Generated at 2022-06-13 08:06:03.537865
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Test for non-static parent
    block1 = Block()
    block1.statically_loaded = False
    task = Task()
    task.block = block1
    block1.block = task
    assert not block1.all_parents_static()
    # Test for non-static parent
    block1 = Block()
    block1.statically_loaded = True
    task = Task()
    task.block = block1
    block1.block = task
    assert block1.all_parents_static()


# Generated at 2022-06-13 08:06:09.562031
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.base import Base
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.constants import DEFAULTS

    base = Base()
    p = Play()
    p_context = PlayContext()
    p.context = p_context
    b = Block()
    b._loader = base._loader
    b._variable_manager = base._variable_manager
    b._tqm = base._tqm
    b._play = p

    # Block without tasks
    result = b.filter_tagged_tasks(DEFAULTS)
    assert result._attributes == {'block': [], 'always': [], 'rescue': []}
    assert result._parent is None

    # Block with only tasks

# Generated at 2022-06-13 08:06:20.997236
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.task_include import TaskInclude

    # all_parents_static() is true
    my_block = Block(dep_chain=[])
    my_block.statically_loaded = True
    assert my_block.get_dep_chain() is None

    my_block = Block(dep_chain=[])
    my_block._parent = Block()
    my_block._parent.statically_loaded = True
    assert my_block.get_dep_chain() is None

    my_block = Block(dep_chain=[])
    my_block._parent = TaskInclude(dep_chain=[])
    my_block._parent.statically_loaded = True
    assert my_block.get_dep_chain() is None

    # all_parents_static() is false

# Generated at 2022-06-13 08:07:00.957631
# Unit test for method is_block of class Block
def test_Block_is_block():
    from ansible.parsing.yaml.objects import AnsibleMapping
    Block.is_block(dict())
    Block.is_block(AnsibleMapping(dict()))
    Block.is_block([])
    Block.is_block({'block':[]})
    Block.is_block({'block':[],'rescue':[],'always':[]})
    Block.is_block({'block':[],'rescue':[],'always':[], 'other':[]})


# Generated at 2022-06-13 08:07:15.355862
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    '''Tests the get_dep_chain method of class Block'''
    ds = {}
    assert not Block.is_block(ds)
    ds = {'block': [ { 'tasks': 'foobar' }] }
    assert Block.is_block(ds)
    b=Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False)
    b.load_data(ds)
    assert not b._attributes['block']
    assert not b._rescue
    assert not b._always
    assert not b._dep_chain
    assert not b._role
    assert not b._parent
    assert not b._use_handlers
    assert b._implicit
    ds = {'hosts': 'foobar'}

# Generated at 2022-06-13 08:07:22.718975
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    task = Block()
    assert not task.has_tasks()
    task = Block()
    task.block = []
    task.rescue = []
    task.always = []
    assert not task.has_tasks()
    task = Block()
    task.block = ['foo']
    task.rescue = []
    task.always = []
    assert task.has_tasks()
    task = Block()
    task.block = []
    task.rescue = ['foo']
    task.always = []
    assert task.has_tasks()
    task = Block()
    task.block = ['foo']
    task.rescue = ['foo']
    task.always = []
    assert task.has_tasks()
    task = Block()
    task.block = ['foo']

# Generated at 2022-06-13 08:07:25.131306
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # Test:Create expected values
    expected = None
    # Test:Create actual values
    loader = None
    block = Block()
    actual = block.set_loader(loader)
    # Test:Evaluate the actual vs expected.
    assert expected == actual

# Generated at 2022-06-13 08:07:34.631447
# Unit test for method copy of class Block
def test_Block_copy():
	h = dict(
		x = Host(),
		y = Host(),
		z = Host()
	)
	t = Task()
	t.action = 'setup'
	p = Play()
	assert p.load(dict(
		name = 'test play',
		hosts = 'all',
		gather_facts = 'no',
		tasks = [t]
	)).serialize() == dict(
		name = 'test play',
		hosts = 'all',
		gather_facts = False,
		tasks = [t.serialize()]
	)

# Generated at 2022-06-13 08:07:36.205611
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    #### PUT YOUR CODE HERE
    b = Block()
    b.set_loader('loader')



# Generated at 2022-06-13 08:07:42.770315
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = {'dep_chain': ['some string']}
    block.deserialize(data)
    # test if attribute dep_chain has the correct value after deserialization
    assert(block._dep_chain == 'some string')
    data = {'role': {'_role_path': 'some string'}}
    block.deserialize(data)
    # test if attribute _role has the correct value after deserialization
    assert(block._role._role_path == 'some string')
    data = {'parent': {'statically_loaded': True}, 'parent_type': 'Block'}
    block.deserialize(data)
    # test if attribute _parent has the correct value after deserialization
    assert(block._parent.statically_loaded == True)


# Generated at 2022-06-13 08:07:43.325552
# Unit test for method is_block of class Block
def test_Block_is_block():
    pass

# Generated at 2022-06-13 08:07:50.507086
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # create an instance of Block
    block = Block()
    # create an instance of TaskInclude
    taskinclude = TaskInclude()
    # create an instance of Role
    role = Role()
    # create an instance of Play
    play = Play()
    # create an instance of Playbook
    playbook = Playbook()
    # create an instance of PlayContext
    playcontext = PlayContext()
    # create an instance of Play
    play = Play()
    # call method set_loader of object block
    block.set_loader([])
    # set attribute _parent of object block
    block._parent = role
    # call method get_first_parent_include of object block
    result = block.get_first_parent_include()
    assert result is None
    # set attribute _parent of object block
    block._parent = taskinclude
   

# Generated at 2022-06-13 08:08:04.913293
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    t1 = Task.load(dict(action='debug', msg='boom', tags=['foobar']),
                   play=None,
                   block=None,
                   role=None,
                   task_include=None,
                   variable_manager=None,
                   loader=None)
    t2 = Task.load(dict(action='debug', msg='boom2', tags=['foobar2']),
                   play=None,
                   block=None,
                   role=None,
                   task_include=None,
                   variable_manager=None,
                   loader=None)

# Generated at 2022-06-13 08:08:43.819180
# Unit test for method copy of class Block
def test_Block_copy():
    Block.load(dict(block=dict(block=[dict(block=dict(name='first'))])))
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    block.copy(exclude_parent=False, exclude_tasks=False)


# Generated at 2022-06-13 08:08:52.463588
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    block.block = [1, 2, 3]
    block.rescue = []
    block.always = []
    assert block.has_tasks() is True, 'test_Block_has_tasks assert#1 has failed.'
    block.block = [1, 2, 3]
    block.rescue = [4]
    block.always = [5]
    assert block.has_tasks() is True, 'test_Block_has_tasks assert#2 has failed.'
    block.block = []
    block.rescue = [4]
    block.always = []

# Generated at 2022-06-13 08:08:59.993414
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block=Block()
    block._parent=Block()
    block._parent._parent=Block()
    block._parent._parent._dep_chain=None
    block._parent._parent._parent=Block()
    block._parent._parent._parent._dep_chain=None
    answer=None
    assert block.get_dep_chain()==answer
    block._parent._parent._parent._dep_chain=[Block()]
    block._parent._parent._parent._dep_chain[0]._dep_chain=None
    answer=[Block()]
    assert block.get_dep_chain()==answer
    block._parent._parent._dep_chain=[Block()]
    block._parent._parent._dep_chain[0]._dep_chain=[Block()]
    answer=[Block(),Block()]
    assert block.get_dep_chain()==answer

# Generated at 2022-06-13 08:09:11.205689
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role_dependency import RoleDependency
    c = PlayContext()
    p = Play()
    p._play_context = c
    b = Block(play=p)
    assert b.all_parents_static() == True
    t = Task()
    t._parent = b
    assert t.all_parents_static() == True
    t2 = Task()
    t2._parent = t
    assert t2.all_parents_static() == True


# Generated at 2022-06-13 08:09:12.256943
# Unit test for method copy of class Block
def test_Block_copy():
    pass

# Generated at 2022-06-13 08:09:22.927238
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.parsing.splitter import parse
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    loader = DictDataLoader({})
    host_vars = {'testhost': {}}
    inventory = Inventory(loader=loader)
    inventory.add_host(Host('testhost'), 'all')
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.VersionInfo(gitinfo=False))
    variable_manager.set_inventory

# Generated at 2022-06-13 08:09:29.536339
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    assert not b.has_tasks()
    b.block = []
    b.rescue = []
    b.always = []
    assert not b.has_tasks()
    b.rescue = ['rescue']
    assert b.has_tasks()
    b.rescue = []
    b.always = ['always']
    assert b.has_tasks()
    b.always = []
    b.block = ['task']
    assert b.has_tasks()