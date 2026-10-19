

# Generated at 2022-06-13 08:00:32.430723
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block1 = Block()
    block2 = Block()
    block3 = Block()
    block4 = Block()
    block5 = Block()
    block6 = Block()
    block1._dep_chain = [block2]
    block2._dep_chain = [block3]
    block3._dep_chain = [block4]
    block4._dep_chain = [block5]
    block5._dep_chain = [block6]
    assert block1.get_dep_chain() == [block2, block3, block4, block5, block6]


# Generated at 2022-06-13 08:00:37.173275
# Unit test for method is_block of class Block
def test_Block_is_block():
    data = {'block':[{'debug':{'msg':"the value is {{ var }}"}},{'debug':{'msg':"the value is {{ lookup('consul', 'var') }}"}}]}
    ansible.parsing.dataloader.DataLoader = None

    result = Block.is_block(data)
    assert result == True



# Generated at 2022-06-13 08:00:43.813676
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    test_play = Play().load(dict(
        name = "Ansible play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), variable_manager=variable_manager, loader=loader)

    test_block_1 = Block().load(test_play.tasks, play=test_play, role=None, task_include=None, use_handlers=test_play.use_handlers, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:00:52.961680
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():

    def test_result_of_Block_preprocess_data_CASE1():
        data = {'block': 'test'}
        block = Block(implicit=True)
        result = block.preprocess_data(data)
        assert result == {'block': 'test'}
 
    def test_result_of_Block_preprocess_data_CASE2():
        data = {'block': 'test'}
        block = Block(implicit=False)
        result = block.preprocess_data(data)
        assert result == {'block': 'test'}
 
    def test_result_of_Block_preprocess_data_CASE3():
        data = {'block': 'test'}
        block = Block(implicit=True)
        result = block.preprocess_data(data)
       

# Generated at 2022-06-13 08:01:00.292830
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play_context.only_tags = []
    play_context.skip_tags = []

    provider = dict(
        name='local',
        transport='local'
    )

    block_rescue = [
        dict(
            action='debug',
            name='this is rescue debug debug debug debug',
            register='debug_result'
        ),
        dict(
            action='set_fact',
            debug_result="'rescue'",
            name='debug1',
            when='debug_result.rc == 1'
        )
    ]


# Generated at 2022-06-13 08:01:02.118706
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
  block = Task()
  all_vars = {}
  assert type(block.filter_tagged_tasks(all_vars)) == Block


# Generated at 2022-06-13 08:01:04.736544
# Unit test for method is_block of class Block
def test_Block_is_block():
    data=[{'block': ['a']},{'rescue': ['a']},{'always': ['a']}]
    for d in data:
        assert (Block.is_block(d)) == True  

# Generated at 2022-06-13 08:01:11.326214
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    tasks=['Hello World']
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play.load(tasks, variable_manager=variable_manager, loader=loader)
    play.preprocess_data()
    block = play.block_list[0]
    block.preprocess_data(tasks)
    if(block.block==[{'action':'Hello World', 'name':'Hello World'}]):
        print("test_Block_preprocess_data: PASS")

# Generated at 2022-06-13 08:01:14.534187
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = load_fixture('block_ds1.yml')
    b = Block.load(data)
    assert b.serialize() == data, 'failure deserializing a Block'

# Generated at 2022-06-13 08:01:20.120277
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    class MockTask:
        def __init__(self, name):
            self.name = name

    mock_play = None

    # case 1: No implicit block
    mock_implicit = False
    task_1 = MockTask('task 1')
    block = Block(play=mock_play, implicit=mock_implicit)
    data = block.preprocess_data(task_1)
    assert data == {'block': [task_1]}

    # case 2: Implicit block
    mock_implicit = True
    data = block.preprocess_data(task_1)
    assert data == task_1

    # case 3: Implicit block
    task_2 = MockTask('task 2')
    data = block.preprocess_data([task_1, task_2])

# Generated at 2022-06-13 08:01:44.381586
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    # Instantiate a mock object
    pytest.mock_task = Task()

# Generated at 2022-06-13 08:01:51.468659
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import unittest
    import sys
    import os
    import ansible.constants as C
    class FakeLoader(object):
        path_exists = True
        def load_from_file(self, filename, cache=True, unsafe=False,
                           class_name=None, use_module=False):
            from ansible.playbook.task import Task
            from ansible.playbook.block import Block
            block_data = dict()
            block_data['block'] = list()
            block_data['block'].append(dict(action=dict(foo='bar')))
            block_data['block'].append(dict(action=dict(foo='bar')))
            return Block(use_handlers=True).load_data(block_data)

# Generated at 2022-06-13 08:01:52.116915
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:02:02.651499
# Unit test for method copy of class Block
def test_Block_copy():
    # unit test for copy of class Block
    test_play_1 = Play()
    test_play_1._loader = DictDataLoader({'test_role_1': dict(name='test_role_1', tasks=[dict(action='debug', msg="DEBUG task in role_1"), dict(action='debug', msg="DEBUG task in role_1")])})
    test_play_1._variable_manager = VariableManager()
    test_play_1._variable_manager.set_play_context(PlayContext())
    test_play_1._tqm = Mock()
    test_task = Task()
    test_task._role = test_play_1._loader.load_role_definition('test_role_1', 'test_role_1', test_play_1._parent_role)

# Generated at 2022-06-13 08:02:13.184984
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    pb = Playbook.load('/root/ansible-elk/playbooks/install_k8s.yml', variable_manager=VariableManager(), loader=None)
    p = pb.get_plays()[0]
    t = Task()
    t._role = None
    t._task_include = None
    t._parent = None
    t._play = p
    t._loader = None
    t._block = None
    t._use_handlers = False
    t._dep_chain = None
    all_vars = dict()
   

# Generated at 2022-06-13 08:02:20.013545
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    b = Block()

# Generated at 2022-06-13 08:02:24.790461
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    parent_data = {'type': 'block', 'block': []}
    assert_equal(block.deserialize({'parent': parent_data}), None)



# Generated at 2022-06-13 08:02:37.525462
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    block = Block()
    task_include1 = TaskInclude()
    task_include2 = TaskInclude()
    task_include3 = TaskInclude()
    task_include1._parent = block
    task_include2._parent = task_include1
    task_include3._parent = task_include2
    assert(task_include3.get_first_parent_include() == task_include1)
    assert(task_include2.get_first_parent_include() == task_include1)
    assert(task_include1.get_first_parent_include() == task_include1)
    assert(block.get_first_parent_include() is None)


# Generated at 2022-06-13 08:02:43.790837
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    #  def filter_tagged_tasks(self, only_tags=None, skip_tags=None):
    # Nasty way of importing the Block class
    import ansible.playbook.block
    block_cls = getattr(ansible.playbook.block, 'Block')
    block_cls_instance = block_cls(play=None, parent_block=None, role=None, task_include=None,
            use_handlers=False, implicit=False)

    # Create block with tasks

    # Create block with tasks
    # Block(block=block_tasks, rescue=rescue_tasks, always=always_tasks,
    #      self_handler=self_handler, delegate_to=delegate_to,
    #      role=role, loop=loop, loop_args=loop_args)

   

# Generated at 2022-06-13 08:02:55.285720
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
	
    mock_play = 'mock_play'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'
    mock_dep_chain = 'mock_dep_chain'

# Generated at 2022-06-13 08:03:28.480620
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    assert isinstance(block.copy(), Block)


# Generated at 2022-06-13 08:03:39.799876
# Unit test for method copy of class Block
def test_Block_copy():
    # Init a loaded_block with:
    #   loader: None
    #   play: None
    #   use_handlers: False
    #   implicit: False
    #   block: []
    #   rescue: []
    #   always: []
    #   _dep_chain: None
    loaded_block = Block()
    # Test if method copy returns the correct object for the following "data":
    #   exclude_parent: False
    #   exclude_tasks: False
    assert (loaded_block.copy() == loaded_block)


# Generated at 2022-06-13 08:03:42.766725
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # setup
    block = Block()
    block._parent = Block()
    block._parent.statically_loaded = True
    
    # test
    assert block.all_parents_static()

# Generated at 2022-06-13 08:03:49.407819
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    # Init
    b = Block()
    b.block = [Task()]
    b.rescue = [Task()]
    b.always = [Task()]
    b.statically_loaded = True
    b._parent = b
    b._dep_chain = [b, b]
    b.dep_chain = b._dep_chain
    b._ds = AnsibleMapping()

    # End
    assert b.copy()

    # Coverage
    b._ds = Templar(b._ds)
    b.get_dep_chain()
    b.copy()

# Generated at 2022-06-13 08:03:51.162795
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    b.set_loader(None)
    pass


# Generated at 2022-06-13 08:03:53.701721
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    a = Block()

# Generated at 2022-06-13 08:04:06.866148
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    b = Block({"block": "task1"}, task_include=None)
    assert b.all_parents_static() == True

    # set a parent for the block
    b.parent = Block({"block": "task2"}, task_include=None)
    assert b.all_parents_static() == True

    # set a parent for the parent of the block
    b.parent.parent = Block({"block": "task3"}, task_include=None)
    assert b.all_parents_static() == True

    # set a parent for the parent of the parent of the block with statically_loaded = False
    b.parent.parent.statically_loaded = False
    assert b.all_parents_static() == False

    # try to access all_parents_static method with task include
    b.parent.parent.parent = None
    b

# Generated at 2022-06-13 08:04:21.342466
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager

    # Create a variable manager and inventory
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(host_list=['localhost']))

    context = PlayContext()
    variable_manager.set_play_context(context)
    context._var_manager = variable_manager

    # Create a set of tasks to be used in the tests.
    task_one = Task()
    task_one.action = 'foo'
    task_one.tags = ['one']

# Generated at 2022-06-13 08:04:29.463055
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  b = Block()

# Generated at 2022-06-13 08:04:34.530763
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role

    non_TaskInclude_obj = Block()
    non_TaskInclude_obj._parent = Role()
    assert non_TaskInclude_obj.get_first_parent_include() is None

    test_obj = Block()
    test_obj._parent = Task()
    assert test_obj.get_first_parent_include() is None

    test_obj = Block()
    test_obj._parent = TaskInclude()
    assert test_obj.get_first_parent_include() == test_obj._parent

    test_obj = Block()
    test_obj._parent = TaskInclude()
    test_obj._parent._parent = TaskInclude()

# Generated at 2022-06-13 08:04:56.507283
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    my_block = Block()
    my_block.statically_loaded = True
    my_block._parent = Block()
    assert my_block.all_parents_static() == True
    my_block.statically_loaded = False
    assert my_block.all_parents_static() == False
    my_block.statically_loaded = True
    my_block._parent._parent = Block()
    assert my_block.all_parents_static() == True


# Generated at 2022-06-13 08:05:06.623979
# Unit test for method copy of class Block
def test_Block_copy():
    b1 = Block()
    b1.block = []
    b1.dep_chain=[]
    b1.parent=None
    b1.role=None
    b1.always=None
    b1.rescue=None
    b1.use_handlers=False
    b1.implicit=False
    b1.exclude_parent=False
    b1.exclude_tasks=False
    b2 = b1.copy()
    assert b1.__dict__ == b2.__dict__


# Generated at 2022-06-13 08:05:14.841843
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:05:23.970089
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    '''
    function to test all_parents_static of class Block
    '''
    p1 = Block()
    i1 = TaskInclude()
    t1 = Block()
    t2 = Block()
    i1.block = [[p1]]
    p1._parent = i1
    p1._play = Play().load({'name': 'testplay', 'hosts': 'all'}, variable_manager=VariableManager(), loader=DictDataLoader())
    p1.block = [[t1]]
    p1.rescue = [[t2]]
    i1.statically_loaded = False
    assert False == p1.all_parents_static()

    t1.statically_loaded = False
    assert False == p1.all_parents_static()

    i1.statically_loaded = True

# Generated at 2022-06-13 08:05:34.402898
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    debug_model = get_debug_model()
    debug_model.debug = True

    ## Correct Block object
    context = AnsibleContext({})

# Generated at 2022-06-13 08:05:41.248280
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:05:48.561665
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    t1 = Task()
    t2 = Task()
    t3 = Task()
    t4 = Task()
    block_task = Block()
    block_task.block  = [t1, t2]
    block_task.rescue = [t3]
    block_task.always = [t4]
    all_vars = []
    assert block_task.filter_tagged_tasks(all_vars).has_tasks() == True


# Generated at 2022-06-13 08:06:00.946886
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for method filter_tagged_tasks of class Block
    '''

    my_block = Block()
    my_block.block = [{'name': 'task 1', 'tags': ['TAG_1', 'TAG_2']},
                      {'name': 'task 2', 'when': {'condition': 'test'}},
                      Block(),
                      {'name': 'task 3', 'tags': ['TAG_3']}]
    results = [{'name': 'task 1', 'tags': ['TAG_1', 'TAG_2']},
               {'name': 'task 3', 'tags': ['TAG_3']}]

    my_block = my_block.filter_tagged_tasks({'TAG_1': True, 'TAG_2': True, 'TAG_3': False})

# Generated at 2022-06-13 08:06:02.118601
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    o = Block()
    assert o.has_tasks() == False

# Generated at 2022-06-13 08:06:04.190203
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    instance = Block()
    instance.deserialize(['block', 'rescue', 'always', 'block', 'rescue', 'always', 'block', 'rescue', 'always'])

# Generated at 2022-06-13 08:06:22.010873
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    set_loader = block.set_loader
    assert set_loader is not None

# Generated at 2022-06-13 08:06:24.221221
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    b._dep_chain = ["a", "b", "c"]
    assert(b.get_dep_chain() == ["a", "b", "c"])

# Generated at 2022-06-13 08:06:35.919541
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print('Test Block.filter_tagged_tasks()')

    _block_utils = AnsibleModuleUtils(None)
    _validate_attrs = _block_utils.validate_attrs
    _load_list_of_blocks = _block_utils.load_list_of_blocks
    _load_list_of_tasks = _block_utils.load_list_of_tasks
    _load_block = _block_utils.load_block
    _load_rescue = _block_utils.load_rescue
    _load_always = _block_utils.load_always
    _get_parent_attribute = _block_utils.get_parent_attribute

    from ansible.playbook.base import Play

    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

# Generated at 2022-06-13 08:06:43.275741
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    class MockInclude(object):
        def __init__(self):
            self.statically_loaded = True

    class MockBlock(object):
        def __init__(self, block, rescue, always):
            self.block = block
            self.rescue = rescue
            self.always = always

        def has_tasks(self):
            return True if len(self.block) > 0 else False

    class MockTask(object):
        pass

    class MockPlay(object):
        def __init__(self):
            self.statically_loaded = True

    class MockRole(object):
        def __init__(self):
            self.statically_loaded = True
    # block is not empty

# Generated at 2022-06-13 08:06:54.028203
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    _parent = mock.Mock(spec=dict)
    _role = mock.Mock(spec=dict)
    _loader = mock.Mock(spec=dict)
    _variable_manager = mock.Mock(spec=dict)
    _task_vars = mock.Mock(spec=dict)
    _loader = mock.Mock(spec=dict)
    _block_vars = mock.Mock(spec=dict)
    _play = mock.Mock(spec=dict)

    # Instantiate class
    block = Block()

    # Mock block
    block.block = mock.Mock(spec=dict)
    block.rescue = mock.Mock(spec=dict)
    block.always = mock.Mock(spec=dict)
    block._play = mock.Mock(spec=dict)
   

# Generated at 2022-06-13 08:06:56.421930
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    blockObj = Block()
    blockObj.set_loader("test_loader")


# Generated at 2022-06-13 08:07:03.185123
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():

    # Case 1
    # Create a chain of statically loaded blocks.
    # The chain is statically loaded.
    def test_Block_all_parents_static_case_1():
        # Create a mock of Block
        class Mock_Block:
            def __init__(self, statically_loaded=True):
                self.statically_loaded = statically_loaded

            def all_parents_static(self):
                return self.statically_loaded

        block = Block()

        # Create a chain of blocks.
        # The last block is None.
        tail_block = Mock_Block()
        block._parent = tail_block
        while tail_block is not None:
            new_tail_block = Mock_Block()
            tail_block._parent = new_tail_block
            tail_block = new_tail_block

        # Call method all_

# Generated at 2022-06-13 08:07:17.515637
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    # Target class is Block
    block = Block()
    # Test function get_dep_chain with parameters
    # Return value should be None
    assert block.get_dep_chain() == None
    # Test function get_dep_chain with parameters
    # Return value should be None
    assert block.get_dep_chain() == None

    ti = TaskInclude()
    ti._dep_chain = []
    assert block.get_dep_chain() == None
    assert block.get_dep_chain() == None
    block._parent = HandlerTaskInclude()
    assert block.get_dep_chain() == None
    assert block.get_dep_chain() == None
    block._parent._

# Generated at 2022-06-13 08:07:18.684287
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert block.has_tasks() == False

# Generated at 2022-06-13 08:07:25.326583
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    task1= TestTask()
    task1.set_loader(DictDataLoader({}))
    block1 = Block(implicit=True,block=[task1],loader=DictDataLoader({}))
    # Test for condition where block has one task and task has action,as this would make has_tasks return true
    task1.action = 'debug'
    assert (block1.has_tasks() == True)
    # Test for condition where block has one task and task has no action,as this would make has_tasks return false
    task1.action = None
    assert (block1.has_tasks() == False)
    # Test for condition where block has more than one task and at least one task has action,as this would make has_tasks return true
    task2= TestTask()

# Generated at 2022-06-13 08:07:41.219839
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    pass


# Generated at 2022-06-13 08:07:48.880508
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    tasks_block = {"block":[
        {"block":"tests/test_data/tasks/tasks01.yml"},
        {"include":"tests/test_data/tasks/tasks01.yml"}
    ]}

    empty_block = {"block":[]}

    file_block = {"block":[
        {"block":"tests/test_data/tasks/tasks01.yml"},
        {"include":"tests/test_data/tasks/tasks01.yml"},
        {"rescue":["tests/test_data/tasks/tasks01.yml", "tests/test_data/tasks/tasks01.yml"]},
        {"always":["tests/test_data/tasks/tasks01.yml", "tests/test_data/tasks/tasks01.yml"]}
    ]}



# Generated at 2022-06-13 08:07:52.560675
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # Testing init of class Block
    x = Block()
    x._dep_chain = None
    # Testing method get_dep_chain
    y = x.get_dep_chain()
    assert(y == None)

# Generated at 2022-06-13 08:08:07.016336
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # create a Block with 4 tasks
    block = Block()
    block.block = [Block(), Block(), Block(), Block()]
    block.rescue = [Block(), Block(), Block(), Block()]
    block.always = [Block(), Block(), Block(), Block()]
    # test if the task list of block is filtered
    block.filter_tagged_tasks(all_vars={})
    assert len(block.block) == 0
    assert len(block.rescue) == 0
    assert len(block.always) == 0

    # create a Block with 4 tasks
    block = Block()
    block.block = [Block(), Block(), Block(), Block()]
    block.rescue = [Block(), Block(), Block(), Block()]
    block.always = [Block(), Block(), Block(), Block()]
    # test if the task list

# Generated at 2022-06-13 08:08:13.123715
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    r = Role()

    p = Play().load(dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        roles = [
            dict(
                role = "common",
                some_parameter = 5
            ),
            dict(
                role = "other",
                some_parameter = 17,
                tasks = [
                    dict(
                        block=["get uri", "second"],
                    ),
                ],
            ),
        ],
    ))
    l = DataLoader()
    b = Block().load(dict(
        block=["get uri", "second"],
    ), play=p, role=r)
    p.set_loader(l)
    b.set_loader(l)
    assert b._loader.__class__.__

# Generated at 2022-06-13 08:08:15.939186
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    assert b.get_dep_chain() == None



# Generated at 2022-06-13 08:08:27.516186
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook import Role
    from ansible.playbook.task_include import TaskInclude

    block = Block()
    assert block.all_parents_static() is True

    block._parent = block
    assert block.all_parents_static() is True

    block._parent = Role()
    assert block.all_parents_static() is True

    block._parent = TaskInclude()
    assert block.all_parents_static() is False

    block._parent = block
    assert block.all_parents_static() is True

    block._parent = Role()
    assert block.all_parents_static() is True

    block._parent = TaskInclude()
    assert block.all_parents_static() is False


# Generated at 2022-06-13 08:08:38.508559
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    def get_first_parent_include(v):
        if v == 'a':
            return block
        elif v == 'b':
            return role
        elif v == 'c':
            return playbook
        else:
            return None

    block, role, playbook = ['a', 'b', 'c']
    setattr(Block, 'get_first_parent_include', get_first_parent_include)
    assert Block('a').get_first_parent_include() == 'a'
    assert Block('b').get_first_parent_include() == 'b'
    assert Block('c').get_first_parent_include() == 'c'
    assert Block('d').get_first_parent_include() is None
    assert Block('a').get_first_parent_include() == 'a'


# Generated at 2022-06-13 08:08:42.586320
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    Block_obj = Block(0,0)
    assert Block_obj.deserialize() == "Invalid input"

# Generated at 2022-06-13 08:08:51.596552
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template.template import Templar
    from ansible.vars.manager import VariableManager
    import yaml
    test_data = yaml.safe_load("""
        - name: block hide and show
          hosts: localhost
          tasks:
            - name: Test Block
              block:
                - debug: msg="Hello World"
                  tags:
                    - hide_me
                - debug:
                    msg: This task is visible when --tags hide_me
          vars:
            var: visible
    """)
    play_context = PlayContext()
    play_context.become_

# Generated at 2022-06-13 08:09:15.042989
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = dict()
    data['attributes'] = dict()
    data['attributes']['name'] = "/etc/ansible_test/1"
    data['attributes']['hosts'] = "1.2.3.4"
    data['attributes']['gather_facts'] = True
    data['attributes']['connection'] = "ssh"
    data['attributes']['remote_user'] = "adam"
    data['attributes']['sudo'] = True
    data['attributes']['sudo_user'] = "adam"
    data['attributes']['sudo_pass'] = True
    data['attributes']['tags'] = ["1", "2"]
    data['attributes']['when'] = "True"

# Generated at 2022-06-13 08:09:24.823175
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # make a block with a task, a rescue handler and an always handler
    block = Block()
    block.block = [Task().load({'action': {'__ansible_module__': 'ping'}})]
    block.rescue = [Handler().load({'action': {'__ansible_module__': 'ping'}})]
    block.always = [Handler().load({'action': {'__ansible_module__': 'ping'}})]
    # only tags are relevant for filter_tasks
    block.block[0].tags = {'ping'}
    block.rescue[0].tags = {'ping'}
    block.always[0].tags = {'ping'}

    # make a play with only_tags that match the above tags

# Generated at 2022-06-13 08:09:28.000717
# Unit test for method copy of class Block
def test_Block_copy():
    """
    This test the method copy of class Block
    """
    # Check if the right type of object is returned
    result = Block.copy()
    assert isinstance(result, dict)


# Generated at 2022-06-13 08:09:36.533740
# Unit test for method copy of class Block
def test_Block_copy():
    print("Testing method copy of class Block")
    play = Play()
    role = Role()