

# Generated at 2022-06-13 08:00:12.564087
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert(not block.has_tasks())


# Generated at 2022-06-13 08:00:22.151379
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:00:29.236202
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:00:31.754141
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    t = Block()
    t.block = ['a', 'b', 'c']
    assert t.has_tasks() is True

# Generated at 2022-06-13 08:00:34.995972
# Unit test for method copy of class Block
def test_Block_copy():
    ## Block_copy ##
    # test case insensitif
    block = host_parser.load('test')
    block.copy()
    pass
# test case sensitiif


# Generated at 2022-06-13 08:00:37.663558
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block(parent=Stub(rescue=[]), block=[Stub(action='nop', implicit=False)], rescue=[], always=[])
    assert b.has_tasks() == True


# Generated at 2022-06-13 08:00:43.879126
# Unit test for method copy of class Block
def test_Block_copy():
    parent = Block()
    block = Block(parent=parent)
    assert block.copy() is not None
    try:
        block.copy(exclude_tasks=True)
    except (AnsibleParserError, AnsibleUndefinedVariable) as e:
        assert False, 'Copy should work even if exclude_tasks is True'
    else:
        assert True

# Generated at 2022-06-13 08:00:52.986668
# Unit test for method copy of class Block
def test_Block_copy():
    from datetime import date
    from ansible.playbook.attribute import Attribute, FieldAttribute
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block, BlockVariable
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.template import AnsibleTemplate
    from ansible.utils.unicode import to_unicode



# Generated at 2022-06-13 08:00:54.435558
# Unit test for method copy of class Block
def test_Block_copy():
  my_block = Block(implicit=True)
  my_block.copy()
  my_block.copy(exclude_parent=True, exclude_tasks=True)


# Generated at 2022-06-13 08:00:58.489255
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(None, None, None, None, False)
    assert not block.has_tasks()

    block = Block(None, None, None, None, False, implicit=True)
    assert not block.has_tasks()

    block = Block(None, None, None, None, False, implicit=True)
    block.block = [1]
    assert block.has_tasks()

# Generated at 2022-06-13 08:01:56.814085
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    fake_play = Play.load({
        'name': 'fakeplay',
        'connection': 'local',
        'hosts': 'all',
        'gather_facts': 'no',
    }, variable_manager=variable_manager, loader=loader)

    task0 = Task()
    task0.action = 'shell'
    task0.args = 'echo "first task"'
    task0.role = None
    task0.dep_chain = None

    task1 = Task()
    task1.action = 'shell'
    task1.args = 'echo "second task"'
    task1.role = None
    task1.dep_chain = None

    task2 = Task()
    task2.action = 'shell'


# Generated at 2022-06-13 08:01:57.880478
# Unit test for method copy of class Block
def test_Block_copy():
    assert True

# Generated at 2022-06-13 08:02:09.545997
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    host_name = 'host1'
    loader = None
    paths = None
    variable_manager = None
    templar = None
    blocks = []
    tasks = []
    role = Role()
    role_include = RoleInclude()
    role_include2 = RoleInclude()
    handler_task_include = HandlerTaskInclude()
    handler_task_include2 = HandlerTaskInclude()
    block = Block(blocks, tasks, loader = loader)
    block2 = Block(blocks, tasks, loader = loader)
    block3 = Block(blocks, tasks, loader = loader)
    block4 = Block(blocks, tasks, loader = loader)

# Generated at 2022-06-13 08:02:15.203789
# Unit test for method copy of class Block
def test_Block_copy():
    my_block = Block()
    my_obj = my_block.copy()
    assert_equal(my_obj.__class__.__name__,"Block")
    assert_equal(my_obj.block,None)
    assert_equal(my_obj.always,None)
    assert_equal(my_obj.rescue,None)
    assert_equal(my_obj._role,None)

    my_task_include = TaskInclude()
    my_task_include._role = Role()
    my_obj._parent = my_task_include
    my_obj._dep_chain = None
    my_obj.block = ['my_task']
    my_obj.always = ['my_task']
    my_obj.rescue = ['my_task']
    my_duplicate_obj = my_obj.copy

# Generated at 2022-06-13 08:02:25.812614
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:02:33.398115
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook import Play
    block = Block(play=Play().load({}), implicit=False)
    assert block.has_tasks() is False
    assert block.has_tasks is False
    block.block = [Task()]
    assert block.has_tasks() is True
    assert block.has_tasks is True

# Generated at 2022-06-13 08:02:41.630311
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    block1 = Block(
        play=None,
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=True,
        implicit=False,
        static=False
    )
    block1._ds = dict()
    block1._attributes = dict({'when': '1'})
    block2 = Block(
        play=None,
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=True,
        implicit=False,
        static=False
    )
    block2._ds = dict()
    block2._attributes = dict({'when': '2'})

    task1 = Task()


# Generated at 2022-06-13 08:02:45.500342
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block_obj = Block()
    res = block_obj.filter_tagged_tasks(None)
    assert res is not None and isinstance(res, Block)
    return True


# Generated at 2022-06-13 08:02:55.920757
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    """
    Method:
        all_parents_static

    Unit:
        Tests that the all_parents_static method returns the static value of the first parent in the chain

    Expected Result:
        All the parent in the chain are static     -> True
        All the parents in the chain are dynamic   -> False
        All the parents in the chain are static except one -> False
    """
    # Create a Block with a parent
    b1 = Block(exclude_parent=True, exclude_tasks=True)
    b1.statically_loaded = True
    b2 = Block(exclude_parent=True, exclude_tasks=True)
    b2.statically_loaded = False

# Generated at 2022-06-13 08:02:58.874934
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Set invalid value for input variable statically_loaded
    block=Block
    block._parent={}
    assert block.all_parents_static()==False,"all_parents_static should return False"
test_Block_all_parents_static()

# Generated at 2022-06-13 08:03:22.717863
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    #1.
    Block_inherit = Block()
    res = Block_inherit.all_parents_static()
    assert res == True



# Generated at 2022-06-13 08:03:25.911781
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:03:40.888625
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:03:48.061859
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    # Create a task
    task = Task()
    
    # Create a block by using Task object
    b = Block(task=task)
    # Test the result of get_dep_chain() method
    dep_chain = b.get_dep_chain()
    assert dep_chain is None
    
    # Create a block with play object
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')

# Generated at 2022-06-13 08:03:59.984209
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    role1 = Role()
    role1.name = 'role1'
    role1.tags = ['role1_tag', 'role1_tag1']
    role2 = Role()
    role2.name = 'role2'
    role2.tags = ['role2_tag', 'role2_tag1']

    play = Play()
    play.name = 'test'
    play.tags = ['test_tag']

# Generated at 2022-06-13 08:04:09.208182
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    class FakePlay():
        pass
    
    class FakeVariables():
        def get_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            return dict()

    class FakeTask():
        _role = None
        _attributes = dict()
        _parent = None
        _dep_chain = None
        _dependencies = list()
        _loader = None
        loader = None
        action = 0
        implicit = None
        loop = None
        loop_args = None
        when = None
        any_errors_fatal = None
        run_once = None
        delegate_to = None
        environment = None
        changed_when = None
        failed_when = None
        register = None

# Generated at 2022-06-13 08:04:23.507332
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # Test if method has_tasks returns True if block, rescue, always all has tasks
    test1_block = Block(None, None, None, None, None)
    test1_block.block = [1,2,3]
    test1_block.rescue = [4,5,6]
    test1_block.always = [7,8,9]
    assert test1_block.has_tasks() == True

    # Test if method has_tasks returns True if block, rescue has tasks
    test2_block = Block(None, None, None, None, None)
    test2_block.block = [1,2,3]
    test2_block.rescue = [4,5,6]
    assert test2_block.has_tasks() == True

    # Test if method has_tasks returns

# Generated at 2022-06-13 08:04:30.066348
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
	# Create a mock task that has a parent set.
	playbook=Playbook()
	play=Play()
	play.vars=callable(Vars)
	play.post_validate=callable(Play)
	play.post_validate_include_delayeds=callable(Play)
	playbook._entries=play
	playbook._basedir='/tmp'
	playbook.set_loader=callable(Playbook)
	playbook.set_basedir=callable(Playbook)
	playbook.post_validate=callable(Playbook)
	loader=None
	task=Task()
	task._role=None
	task._parent=None
	task._variable_manager=None
	task._loader=None
	task.register_include_file=callable(Task)
	task._

# Generated at 2022-06-13 08:04:31.949200
# Unit test for method copy of class Block
def test_Block_copy():
  block = Block([])
  block.copy()
  pass

# Generated at 2022-06-13 08:04:35.226671
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    result = b.filter_tagged_tasks(None)
    assert result == None


# Generated at 2022-06-13 08:05:03.840851
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block(parent_block=None, role=None, task_include=None, use_handlers=False, implicit= True)
    b._attributes = {}
    b._loader = DictDataLoader({})
    b._variable_manager = VariableManager()
    assert b.has_tasks() == False
    b._attributes["block"] = "test"
    assert b.has_tasks() == True

# Generated at 2022-06-13 08:05:13.941754
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    block.rescue = []
    assert (block.filter_tagged_tasks(None).rescue == [])

    block = Block()
    block.always = []
    assert (block.filter_tagged_tasks(None).always == [])

    block = Block()
    block.block = []
    assert (block.filter_tagged_tasks(None).block == [])

    # creating block with parent

    class Playbook(object):
        def __init__(self):
            self._attributes = dict()

    class Role(object):
        def __init__(self):
            self._attributes = dict()

    class HandlerTaskInclude(object):
        _attributes = dict()
        _parent = None
        def __init__(self):
            self._attributes = dict

# Generated at 2022-06-13 08:05:23.457427
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import ansible.template as templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(loader=None, options=None, variables=None)
    variable_manager.options_vars = load_options_vars(loader=None, options=None, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory=None)
    variable_manager.set_playbook_basedir(loader.get_basedir())
    templar._add_host_vars_from_inventory(variable_manager, host=None)


# Generated at 2022-06-13 08:05:27.111219
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude

    block1 = Block()
    TaskInclude().copy(exclude_parent=True)

    assert block1.get_first_parent_include() == None


# Generated at 2022-06-13 08:05:35.414450
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    # setup
    block = Block()
    block.task_list = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]

    # actual
    result = block.task_list

    # expected
    expect = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]

    assert result == expect


# Generated at 2022-06-13 08:05:36.862052
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    '''
    since Block is a subclass of Task, we test the Task class
    '''
    pass


# Generated at 2022-06-13 08:05:43.101707
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    b = Block()
    b._play = Play()
    b._play._variable_manager = VariableManager()
    b._play._variable_manager.extra_vars = dict()
    b._play.only_tags = []
    b._play.skip_tags = []
    b.vars = dict()
    b.tags = []
    play_context = PlayContext()
    play_context._search_paths = []
    b._loader = DictDataLoader({})
    b2 = Block()
    b2._play = Play()
    b2._play._variable_manager = VariableManager()
    b2._play._variable_manager.extra_vars = dict()

# Generated at 2022-06-13 08:05:49.875412
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    parent = Mock()
    role = Mock()
    loader = Mock()
    block = Block(parent=parent, role=role)
    block.set_loader(loader)
    # Assert
    parent.set_loader.assert_called_with(loader)
    role.set_loader.assert_called_with(loader)


# Generated at 2022-06-13 08:06:01.434633
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    # create new

# Generated at 2022-06-13 08:06:04.258065
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    task_block = Block()
    task_block.block = [Task(), Task()]
    task_block.rescue = [Task(), Task()]
    task_block.always = [Task(), Task()]
    task_block.filter_tagged_tasks(None)


# Generated at 2022-06-13 08:06:30.982721
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Create a Block with a TaskInclude as parent
    block = Block()
    task_include = TaskInclude()
    block._parent = task_include    
    assert(block.get_first_parent_include() == task_include)


# Unit tests for the Block class

# Generated at 2022-06-13 08:06:40.202604
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for method filter_tagged_tasks of class Block
    '''

    import sys
    import inspect
    import re

    target_class = Block

    class_attributes = vars(target_class)

    # list of non private class attributes
    attributes = [
        (
            k,
            v,
        )
        for k, v in class_attributes.items()
        if (
            not k.startswith('_')
        )
    ]

    # list of non private class attributes methods
    methods = [
        (
            k,
            v,
        )
        for k, v in class_attributes.items()
        if (
            inspect.isfunction(v) and not k.startswith('_')
        )
    ]

    # list of class attributes methods

# Generated at 2022-06-13 08:06:45.155450
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    assert b.get_dep_chain() is None
    b._dep_chain = ['a', 'b']
    assert b.get_dep_chain() is not None
    assert b.get_dep_chain() == ['a', 'b']
    _parent = mock.Mock()
    _parent.get_dep_chain.return_value = ['c', 'd']
    b._parent = _parent
    assert b.get_dep_chain() != ['a', 'b']
    assert b.get_dep_chain() == ['c', 'd']


# Generated at 2022-06-13 08:06:49.420012
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(
        play=Play(),
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        implicit=False)
    assert block.has_tasks() == False



# Generated at 2022-06-13 08:06:59.791136
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # create a block
    b = Block()

    assert b.all_parents_static() == True
    assert b._attributes['all_parents_static'].value == True

    # create a parent block and assign it to the child one
    bb = Block()
    b.parent = bb

    assert b.all_parents_static() == True
    assert b._attributes['all_parents_static'].value == True

    bp = Block(statically_loaded=False)
    bb.parent = bp

    assert b.all_parents_static() == False
    assert b._attributes['all_parents_static'].value == False

    bp.statically_loaded = True

    assert b.all_parents_static() == True
    assert b._attributes['all_parents_static'].value == True



# Generated at 2022-06-13 08:07:12.608446
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    b = Block()

# Generated at 2022-06-13 08:07:14.448392
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    b.set_loader('loader')


# Generated at 2022-06-13 08:07:17.460898
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    block = Block(parent_block = Block(parent_block = Block(parent_block = Block(parent_block = Block(parent_block = Block(parent_block = TaskInclude(name = 'name', static = False)))))))
    assert block.all_parents_static() == False

# Generated at 2022-06-13 08:07:18.647622
# Unit test for method copy of class Block
def test_Block_copy():
    block_obj = Block()
    block_obj.copy()

# Generated at 2022-06-13 08:07:21.552702
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block = Block()
    assert block.get_dep_chain() == None
    test_dep_chain = [Task()]
    block._dep_chain = test_dep_chain
    assert block.get_dep_chain() == test_dep_chain


# Generated at 2022-06-13 08:07:46.191417
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    raise NotImplementedError()
##
# END - test_Block_filter_tagged_tasks
##


###
# Helper class for Task/Handler
###

# Generated at 2022-06-13 08:07:52.513534
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test 0
    # Test with only conditional tasks in the block
    b = Block()
    b.block = [
        dict(when='1'),
        dict(when='2'),
        dict(when='3'),
    ]
    b.rescue = [
        dict(when='1'),
        dict(when='2'),
        dict(when='3'),
    ]
    b.always = [
        dict(when='1'),
        dict(when='2'),
        dict(when='3'),
    ]

    all_vars = dict()

    new_block = b.filter_tagged_tasks(all_vars)

    assert new_block.block == [
        dict(when='1'),
        dict(when='2'),
        dict(when='3'),
    ]
    assert new_block.res

# Generated at 2022-06-13 08:08:02.699186
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  data = {u'role': {u'role_path': u'/path/to/my/role'}, u'loop': u'{{ myvar }}', u'name': u'test this please'}
  b = Block(implicit=True)
  b.deserialize(data)
  assert data[u'role'] == b._role.serialize()
  assert data[u'loop'] == b._attributes[u'loop']
  assert data[u'name'] == b._attributes[u'name']


# Generated at 2022-06-13 08:08:09.441945
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = {'dep_chain': ['role', 'include'], 'name': 'block', 'block': ['block'], 'always': 'always', 'rescue': 'rescue', 'when': 'when', 'loop': 'loop', 'with_items': 'with_items', 'loop_control': 'loop_control', 'role': 'role', 'parent': 'parent', 'parent_type': 'parent_type'}
    role_data = data.get('role')
    parent_data = data.get('parent')
    if parent_data:
        parent_type = data.get('parent_type')
        if parent_type == 'Block':
            p = Block()
        else:
            p = TaskInclude()
        p.deserialize(parent_data)

# Generated at 2022-06-13 08:08:22.097522
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    #testing for block with no task
    Block_test=Block()
    assert Block_test.has_tasks()==False
    #testing for block with one task
    task=Task()
    Block_test.block.append(task)
    assert Block_test.has_tasks()==True
    #testing for block with one task and one rescue
    Block_test.rescue.append(task)
    assert Block_test.has_tasks()==True
    #testing for block with one task and one always
    Block_test.block.remove(task)
    Block_test.always.append(task)
    assert Block_test.has_tasks()==True
    #testing for block with one rescue and one always
    Block_test.rescue.remove(task)
   

# Generated at 2022-06-13 08:08:28.406376
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    _play = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='setup', args=dict())),
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())

    block = Block().deserialize(dict(
        tasks = [
            dict(action=dict(module='shell', args=dict(foo='bar'))),
        ]
    ))
    assert block.block[0].args['foo'] == 'bar'


# Generated at 2022-06-13 08:08:39.333685
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # Test with block, rescue and always task list being empty
    empty_block1 = Block()
    assert empty_block1.has_tasks()
    # Test with only block task list is empty
    empty_block2 = Block(block=[],rescue=[{"name":"rescue_task"},{"name":"rescue_task2"}],always=[{"name":"always_task"}])
    assert empty_block2.has_tasks()
    # Test with only rescue task list is empty
    empty_block3 = Block(block=[{"name":"block_task1"},{"name":"block_task2"}],rescue=[],always=[{"name":"always_task"}])
    assert empty_block3.has_tasks()
    # Test with only always task list is empty

# Generated at 2022-06-13 08:08:47.352582
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
  """
      This function tests whether or not the method filter_tagged_tasks of class Block works
  """
  from ansible.parsing.yaml.loader import AnsibleLoader
  from ansible.playbook.block import Block
  from ansible.playbook.play import Play
  from ansible.playbook.task import Task
  from ansible.playbook.task_include import TaskInclude


# Generated at 2022-06-13 08:08:55.130967
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block(
        role=Role(),
        statically_loaded=False,
        )
    block.block = [
        Task(), 
        Host(), 
        Block(
            role=Role(),
            statically_loaded=False,
            ), 
        SetupTask(), 
        TaskInclude(
            role=Role(),
            statically_loaded=False,
            ), 
        Task(), 
        Task(), 
        Block(
            role=Role(),
            statically_loaded=False,
            ), 
        Task(), 
        ]
    block.rescue = [
        Task(), 
        Task(), 
        ]
    block.always = [
        Task(), 
        Task(), 
        ]
    block._loader = DataLoader()

# Generated at 2022-06-13 08:08:57.739122
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False)
    assert block.has_tasks() is False


# Generated at 2022-06-13 08:09:22.008891
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  block=Block()
  block.deserialize(data = '')

# Generated at 2022-06-13 08:09:25.469846
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    args = {"play":None, "block":None, "role":None, "task_include":None, "use_handlers":False, "implicit":False}
    block = Block(**args)
    assert block.get_dep_chain() == None


# Generated at 2022-06-13 08:09:28.399180
# Unit test for method copy of class Block
def test_Block_copy():
    # example execution: Block.copy(exclude_parent=Sentinel(False), exclude_tasks=Sentinel(False))
    assert True # implement your test here


# Generated at 2022-06-13 08:09:34.705924
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Test the when self._parent is None
    block = Block()
    assert block.get_first_parent_include() == None
    # Test the when self._parent is not None and self._parent is not TaskInclude
    block = Block(parent=Play())
    assert block.get_first_parent_include() == None
    # Test the when self.parent is not None and self._parent is TaskInclude
    block = Block(parent=TaskInclude(statically_loaded=False))
    assert isinstance(block.get_first_parent_include(), TaskInclude)
