

# Generated at 2022-06-13 08:00:01.740015
# Unit test for method set_loader of class Block
def test_Block_set_loader():

    # Check if below utils is invoked
    if (CalledProcessError):
        pass
    if (check_output):
        pass
    if (StringIO):
        pass
    if (six):
        pass


# Generated at 2022-06-13 08:00:02.331182
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:00:08.962246
# Unit test for method copy of class Block
def test_Block_copy():
    a = AnsibleModule()
    #test case 1
    assert a.copy(exclude_parent=False, exclude_tasks=False).__str__() == """<AnsibleModule(None,None,None,None,None,None,None,None,None,None)>"""
    #test case 2
    assert a.copy(exclude_parent=False, exclude_tasks=False).__str__() == """<AnsibleModule(None,None,None,None,None,None,None,None,None,None)>"""
    #test case 3
    assert a.copy(exclude_parent=False, exclude_tasks=False).__str__() == """<AnsibleModule(None,None,None,None,None,None,None,None,None,None)>"""
    #test case 4

# Generated at 2022-06-13 08:00:11.090966
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    obj_block = Block()
    print(obj_block.has_tasks())
    assert type(obj_block) == Block


# Generated at 2022-06-13 08:00:19.716577
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    b1 = Block(False, False, False, False)
    b2 = Block(False, False, False, False)
    b3 = Block(False, False, False, False)
    b4 = Block(False, False, False, False)
    b1._parent = b2
    b2._parent = b3
    b3._parent = b4

    assert b1.get_first_parent_include() is None
    b3._parent = None
    b4._parent = TaskInclude()
    assert b1.get_first_parent_include() is not None
    assert b1.get_first_parent_include() is b4._parent


# Generated at 2022-06-13 08:00:30.272193
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Testing method deserialize of class Block
    # Testing when data is {}
    # Expecting that AnsibleParserError will be raised:
    #     A malformed block was encountered while loading a block

    data = {}
    try:
        Block().deserialize(data)
        assert False
    except AnsibleParserError:
        pass


    # Testing when data is {'role':'role', 'block':'block'}
    # Expecting that AnsibleParserError will be raised:
    #     A malformed block was encountered while loading a block

    data = {'role':'role', 'block':'block'}
    try:
        Block().deserialize(data)
        assert False
    except AnsibleParserError:
        pass


    # Testing when data is {'block': 'block'}
    # Expecting that

# Generated at 2022-06-13 08:00:33.717677
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # Initialize required variables
    x = {}
    x['loader'] = {}
    # Execute function
    Block.set_loader(x, x['loader'])


# Generated at 2022-06-13 08:00:38.785474
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # Loader input

    # TaskInclude input

    # Role input

    # TaskInclude input

    # Task input

    # TaskInclude input

    # TaskInclude input

    # TaskInclude input

    # Block input

    b = Block(play=_a, parent_block=_a, role=_a, task_include=_a, use_handlers=_a)
    b.set_loader(_a)


# Generated at 2022-06-13 08:00:41.000336
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # FIXME: need to test Block.set_loader
    pass

# Generated at 2022-06-13 08:00:50.405352
# Unit test for method serialize of class Block
def test_Block_serialize():
    loader = DictDataLoader({
        'playbook.yaml': ('''
- hosts: localhost
  tasks:
    - block:
        - name: test task 1
          debug: msg="This is task 1"
        # the block below contains a rescue clause
        - block:
            - name: test task 2
              debug: msg="This is task 2"
            rescue:
              - debug: msg="This is a rescue task"
            always:
              - debug: msg="This is an always task"
    ''')})
    play = Play.load(loader=loader, variable_manager={},
                     use_handlers=True,
                     task_loader=TaskLoader(),
                     variable_manager=VariableManager())
    block = next((x for x in play.tasks if isinstance(x, Block)), None)
    data

# Generated at 2022-06-13 08:01:27.538489
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    def test_data(skip_tags, only_tags, block, filtered_block_expected):
        filtered_block = block.filter_tagged_tasks(all_vars={'tags': []})
        filtered_block_str = filtered_block.serialize()
        filtered_block_expected_str = filtered_block_expected.serialize()

        assert filtered_block_str == filtered_block_expected_str, \
            "expected {0}, actual {1}".format(filtered_block_expected_str, filtered_block_str)


# Generated at 2022-06-13 08:01:28.999009
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    block.set_loader()


# Generated at 2022-06-13 08:01:33.071008
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert not block.has_tasks()

    block.block = [1]
    assert block.has_tasks()

    block = Block()
    block.rescue = [1]
    assert block.has_tasks()

    block = Block()
    block.always = [1]
    assert block.has_tasks()
test_Block_has_tasks()

# Generated at 2022-06-13 08:01:41.574414
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:01:42.382121
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    pass

# Generated at 2022-06-13 08:01:49.076272
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=None)

    ds = dict(block='abc')
    assert block.preprocess_data(ds) == ds

    ds = dict(block=[1, 2, 3])
    assert block.preprocess_data(ds) == ds

    ds = dict(a=1)
    assert block.preprocess_data(ds) == ds

    ds = [1, 2, 3]
    assert block.preprocess_data(ds) == {'block': [1, 2, 3]}

    ds = dict()
    assert block.preprocess_data(ds) == ds

    ds = dict(block=[])

# Generated at 2022-06-13 08:01:55.532009
# Unit test for method is_block of class Block
def test_Block_is_block():
    print('Test Block_is_block')
    data1 = {'block':'ds','rescue':'ds','always':'ds'}
    data2 = {'blog':'ds','rescue':'ds','always':'ds'}
    data3 = {'block':'ds','rescue':'ds','ally':'ds'}
    data4 = {1:1}
    data5 = 'ds'

    assert(True == Block.is_block(data1))
    assert(False == Block.is_block(data2))
    assert(False == Block.is_block(data3))
    assert(False == Block.is_block(data4))
    assert(False == Block.is_block(data5))


# Generated at 2022-06-13 08:02:07.381363
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # Test cases
    yield check, Block() # no parent, no role, no dep_chain
    yield check, Block(parent=Block()) # no role, no dep_chain, static parent
    yield check, Block(parent=Block(dep_chain=['dep1'])) # no role, dep_chain, static parent
    yield check, Block(parent=Block(parent=Block())) # no role, no dep_chain, static grandparent, dynamic parent
    yield check, Block(parent=Block(dep_chain=['dep1'], parent=Block())) # no role, dep_chain, static grandparent, dynamic parent
    yield check, Block(role=Role()) # no parent, role, no dep_chain
    yield check, Block(parent=Block(), role=Role()) # static grandparent, static parent, static role, no dep_chain
    yield check

# Generated at 2022-06-13 08:02:13.254176
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    p = Play()
    b = Block()
    assert b.has_tasks() == False
    p.block = [b]
    b.block = [Task()]
    assert b.has_tasks() == True
    b.rescue = [Task()]
    assert b.has_tasks() == True
    b.always = [Task()]
    assert b.has_tasks() == True


# Generated at 2022-06-13 08:02:15.675249
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    if len(b.block) > 0 or len(b.rescue) > 0 or len(b.always) > 0:
        return False
    return True

# Generated at 2022-06-13 08:02:37.783594
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task import Task
    
    # Create a test Block
    b = Block()
    
    # create a parent_data so that Block.deserialize() no longer raises error
    parent_data = {}
    t = Task()
    t.serialize = MagicMock(return_value=parent_data)
    
    # invoke Block.deserialize()
    b.deserialize({'parent':t})


# Generated at 2022-06-13 08:02:51.158432
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    print("Testing Block.get_first_parent_include() ...")
    from ansible.playbook.task_include import TaskInclude
    block = Block(play=Play().load(dict(name="play", hosts=dict(all=[dict(name="all")]), gather_facts="no"), variable_manager=VariableManager(), loader=DataLoader()), use_handlers=True, task_include=TaskInclude())
    assert(block.get_first_parent_include() is block._task_include)
    block2 = Block(play=Play().load(dict(name="play", hosts=dict(all=[dict(name="all")]), gather_facts="no"), variable_manager=VariableManager(), loader=DataLoader()), use_handlers=True, parent_block=block)

# Generated at 2022-06-13 08:02:56.270718
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block()

# Generated at 2022-06-13 08:02:57.892131
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    assert b.get_dep_chain() is None

# Generated at 2022-06-13 08:03:06.386573
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook import Playbook

    b1 = Block(play=Playbook())
    t1 = Task()
    t2 = Task()
    t1.only_if = "True"
    t2.only_if = "False"
    b1.block = [t1, t2]
    b2 = Block(play=Playbook())
    b2.block = [b1]

    filtered_b2 = b2.filter_tagged_tasks({})
    assert len(filtered_b2.block) == 1
    filtered_b1 = filtered_b2.block[0]
    assert len(filtered_b1.block) == 1
    filtered_t1 = filtered_b1.block

# Generated at 2022-06-13 08:03:17.202950
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    # source: https://github.com/ansible/ansible/blob/devel/lib/ansible/playbook/block.py
    # ansible/playbook/block.py
    # class Block(Base):
    #    _valid_attrs = frozenset(['block', 'rescue', 'always'])
    #
    #    def __init__(self, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False):
    #        self._play            = play
    #        self._parent          = parent_block
    #        self._role            = role
    #        self._task_include    = task_include
    #        self._use_handlers    = use_handlers
    #        self._implicit

# Generated at 2022-06-13 08:03:19.753373
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    obj = Block()
    try:
        obj.set_loader(loader)
        assert False, "unit test failed"
    except NotImplementedError as e:
        assert True, "unit test succeed"


# Generated at 2022-06-13 08:03:30.041912
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Unit test for method copy of class Block
    '''
    # Testing with block

# Generated at 2022-06-13 08:03:31.771024
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block()
    if not b:
        return False
    return True


# Generated at 2022-06-13 08:03:45.758614
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    b = Block(parent=None)

    assert b.all_parents_static()

    b.statically_loaded = True
    assert b.all_parents_static()

    b.statically_loaded = False
    assert not b.all_parents_static()

    b.statically_loaded = True
    b.parent = Block(parent=None)
    assert b.all_parents_static()

    b.statically_loaded = True
    b._parent.statically_loaded = False
    assert not b.all_parents_static()

    b.statically_loaded = False
    b._parent.statically_loaded = True
    assert not b.all_parents_static()

# Generated at 2022-06-13 08:04:00.435467
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    #from ansible.playbook.block import Block
    Block()

# Generated at 2022-06-13 08:04:03.357825
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    a = AnsibleModule()
    b = Block()
    b._parent = a
    assert b.all_parents_static() == True


# A class for holding the action and task

# Generated at 2022-06-13 08:04:08.566914
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # test with no given arguments
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    assert(b.has_tasks() == False)
    # test with given arguments
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    assert(b.has_tasks() == False)

# Generated at 2022-06-13 08:04:21.121478
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    t1 = Task.load({'name':'task1'})
    t2 = Task.load({'name':'task2'})
    b1 = Block.load({'block':[t1,t2]})
    assert b1.has_tasks() == True
    b1.block = []
    assert b1.has_tasks() == False
    b1.block = [t1,t2]
    b2 = Block.load({'block':b1})
    b1.block = []
    assert b2.has_tasks() == True
    b2.block = []
    assert b2.has_tasks() == False

# Generated at 2022-06-13 08:04:29.295407
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    class MockInclude(TaskInclude):
        def __init__(self):
            pass
    block2 = Block()
    task2 = Task()
    task2.set_loader(MockInclude())
    task2._parent = block2
    block1 = Block()
    task1 = Task()
    task1._parent = block1
    block0 = Block()
    task0 = Task()
    task0._parent = block0
    block0.block.append(task0)
    block1.block.append(task1)
    block2.block.append(task2)

# Generated at 2022-06-13 08:04:32.704887
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    '''
    Unit test for method has_tasks of class Block
    '''
    # Initialization
    # 1. Create an object of class Play
    p = Play()
    # 2. Create an object of class Block
    b = Block(play=p)

    # Positive test case
    # 1. Check if method has_tasks of class Block returns True
    assert b.has_tasks()

# Generated at 2022-06-13 08:04:35.096603
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Unit test for method deserialize of class Block
    '''
    # do something to test deserialize of class Block
    pass

# Generated at 2022-06-13 08:04:43.794411
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:04:50.868579
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task

    b = Block(implicit=False)
    t = Task(antecedent=b, play=b._play)
    t._attributes['name'] = 'test1'
    t._attributes['tags'] = ['test_tag']
    t.validate()
    b.block = [t]
    b.validate()

    b2 = Block(implicit=False)
    t2 = Task(antecedent=b2, play=b2._play)
    t2._attributes['name'] = 'test2'
    t2._attributes['tags'] = ['test_tag']
    t2.validate()
    b2.block = [b, t2]
    b2.validate()


# Generated at 2022-06-13 08:04:56.174096
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    x = Block()

# Generated at 2022-06-13 08:05:28.918662
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    blk = Block()
    blk.set_loader('loader')


# Generated at 2022-06-13 08:05:37.609510
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = {
        'rescue': [],
        'always': [],
        'no_log': False,
        'name': 'foo',
        'when': 'False',
        'other_attribute': 'ignore_me',
        'dep_chain': None,
        'role': {
            'name': 'test',
            'static': True,
        },
        'parent': {
            'name': 'test',
            'static': False,
        },
        'parent_type': 'TaskInclude',
    }
    block.deserialize(data)
    assert block._name == 'foo'
    assert block._parent
    assert block._role
    assert block._dep_chain is None
    assert isinstance(block._parent, TaskInclude)

# Generated at 2022-06-13 08:05:49.724914
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.base import Base
    b = Block()
    task = Task()
    task.attribute1 = 10
    role = Role()
    role.attribute1 = 20
    play = Play()
    play.attribute1 = 30
    b._attributes['tasklist'] = [task]
    b.role = role
    b.play = play
    b._valid_attrs['tasklist'] = [task]
    data = b.serialize()
    b1 = Block()
    b1.deserialize(data)
    # Test for equality
    print(b1.tasklist == b.tasklist)

# Generated at 2022-06-13 08:05:57.169637
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Instantiating the class
    data = dict(block=[dict(action="debug", args=dict(msg="{{ ansible_all_ipv4_addresses }}"))])
    b = Block.load(data)

    data = b.serialize()
    print(data)
    assert 'block' in data
    assert 'rescue' not in data
    assert 'always' not in data
    


# Generated at 2022-06-13 08:06:06.629912
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    # FIXME: the old Block was initialized with 'implicit=True', but the new Block with 'implicit = not Block.is_block(data)', which changes the behavior.
    # FIXME: the old Task was initialized with 'has_triggered=False', but the new Task with 'self._has_triggered = False', which changes the behavior.
    # FIXME: the old Task used 'self._attributes[name] = value', but the new Task used 'setattr(self, name, value)', which changes the behavior.
    # FIXME: the old Task used 'hasattr(self, attr)', but the new Task used 'attr in self._valid_attrs', which changes the behavior.

# Generated at 2022-06-13 08:06:20.051430
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Test attributes at instantiation.
    obj = Block()
    assert obj._load_roles == False
    assert obj._play == None
    assert obj._role == None
    assert obj._tasks == []
    assert obj._parent == None
    assert obj._dep_chain == None
    assert obj._loader == None
    assert obj._use_handlers == False
    assert obj._block == []
    assert obj._always == []
    assert obj._rescue == []
    assert obj._when == None
    assert obj._notify == []
    assert obj._listen == []
    assert obj._loop == []
    assert obj._error_on_undefined_vars == True
    # Test __eq__() method
    obj1 = Block()
    obj2 = Block()
    assert obj1 == obj2
    # Test get_

# Generated at 2022-06-13 08:06:31.037054
# Unit test for method copy of class Block
def test_Block_copy():
    loader_mock = MagicMock()
    tmp = dict(
        _loader=loader_mock,
        _attributes=dict(attr2='attr2_value', attr1='attr1_value'),
        _play=MagicMock(),
    )
    b = Block(**tmp)
    b._parent = MagicMock()
    b.validate()
    assert b._loader == loader_mock
    assert b._attributes == dict(attr2='attr2_value', attr1='attr1_value')
    assert b._play == MagicMock()
    new_b = b.copy()
    assert new_b._loader == loader_mock
    assert new_b._attributes == dict(attr2='attr2_value', attr1='attr1_value')

# Generated at 2022-06-13 08:06:40.240539
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    test_Block = Block()

# Generated at 2022-06-13 08:06:51.272013
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    class Block1(Block):
        def __init__(self):
            super(Block1, self).__init__()
        def all_parents_static(self):
            return False

    class Block2(Block):
        def __init__(self):
            super(Block2, self).__init__()
            self.block = []
            self.rescue = []
            self.always = []

    class TaskInclude(object):
        def __init__(self):
            super(TaskInclude, self).__init__()
        def all_parents_static(self):
            return False

    b2 = Block2()
    b1 = Block1()
    b1._parent = b2
    b2._parent = TaskInclude()

    assert b1.all_parents_static() == False

# test with instance

# Generated at 2022-06-13 08:07:01.439288
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    assert Block(name='test_block', block=[dict(action='set_fact', args=dict(a=1))]).has_tasks() is True
    assert Block(name='test_block', block=[dict(action='set_fact', args=dict(a=1)), dict(action='block', block=[dict(action='pause', seconds=1)])]).has_tasks() is True
    assert Block(name='test_block', block=[dict(action='pause', seconds=1)]).has_tasks() is True
    assert Block(name='test_block', block=[]).has_tasks() is False
    assert Block(name='test_block').has_tasks() is False
    assert Block(name='test_block', block=[dict(action='block', block=[dict(action='pause', seconds=1)])]).has_t

# Generated at 2022-06-13 08:07:42.875981
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    play = Play()
    block = Block(play=play, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    block.set_loader(loader=None)

# Generated at 2022-06-13 08:07:50.193010
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # This is a test for the method all_parents_static of class Block
    # Test data loading
    t1 = TestTask()
    bi = TestBlockInclude()
    bi.task = t1
    bi.task_list = [t1]
    bi._parent = None # t1._parent
    ti = TestTaskInclude()
    ti.statically_loaded = True
    ti.task_list = [bi]
    ti._parent = None
    b = TestBlock()
    b.block = [bi]
    b._parent = ti
    # Unit test
    x = b.all_parents_static()
    assert x is False
    ti.statically_loaded = False
    x = b.all_parents_static()
    assert x is False
    ti.statically_loaded = True
    b = TestBlock

# Generated at 2022-06-13 08:08:04.668529
# Unit test for method copy of class Block
def test_Block_copy():
    my_play = Play()
    my_play_task = Task()
    my_play._tasks = [my_play_task]
    my_play_role = Role()
    my_play._included_roles = [my_play_role]
    my_play_var_man = VariableManager()
    my_play_loader = DataLoader()
    my_play_var_man.set_loader(my_play_loader)
    my_play.set_variable_manager(my_play_var_man)
    my_play_task._parent = my_play
    my_play_role._parent = my_play
    my_block = Block(play = my_play, parent = my_play_task)
    my_block_rescue = Task()
    my_block_always = Task()
    my_

# Generated at 2022-06-13 08:08:08.543529
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Instantiate a Block object, test the deserialize method
    '''

    data = {}
    block = Block()
    block.deserialize(data)
    assert block.serialize() == {}


# Generated at 2022-06-13 08:08:23.578900
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 08:08:32.210681
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    assert Block(name='test1', parent=Block(parent=Block(name='test2'))).get_first_parent_include() == None
    assert Block(name='test1', parent=Block(parent=Block(name='test2', parent=Block(parent=Block(name='test3'))))).get_first_parent_include() == None
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    test_loader = DataLoader()

# Generated at 2022-06-13 08:08:36.966096
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
	parent_task_include = TaskInclude()
	parent_task_include.name = 'parent_task_include'
	task_include = TaskInclude()
	task_include.name = 'task_include'
	parent_task_include.tasks.append(task_include)
	assert parent_task_include.get_first_parent_include() == parent_task_include

# Generated at 2022-06-13 08:08:41.518858
# Unit test for method copy of class Block
def test_Block_copy():
    block=Block()
    block.load({'block':[]})
    assert block.copy().block==[]
    assert block._parent==None
    assert block._validate_always==block._validate_rescue



# Generated at 2022-06-13 08:08:50.905643
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Test with a class that has public attributes
    test_playbook_object = Playbook.load(dict(
        name = 'a name',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [],
    ), variable_manager=VariableManager(), loader=DataLoader())
    test_task_include_object = TaskInclude()
    test_task_include_object._ds = dict(
        name = 'a name',
        static = 0,
        mode = '644',
    )
    test_task_include_object._attributes = test_task_include_object._ds.copy()
    test_task_include_object._parent = test_playbook_object
    test_role_object = Role()

# Generated at 2022-06-13 08:08:57.521835
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.include import Include
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({})

    t1 = Task()
    t1._role = None
    t1._block  = None
    t1._task_include = None
    t1._parent = None
    t1._play = Play()
    t1._loader = loader
    t1._role_name = None
    t1._static_include = None

    tinc = TaskInclude()
    tinc._role = None
    tinc._block  = None
    tinc._task_