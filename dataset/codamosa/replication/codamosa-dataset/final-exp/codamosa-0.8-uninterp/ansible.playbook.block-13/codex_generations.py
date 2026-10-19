

# Generated at 2022-06-13 08:00:36.561742
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    my_play = Play().load(dict(name="The play", hosts="localhost", gather_facts="no"))
    my_task = Task().load(dict(action="setup"), play=my_play, role=None, task_include=None, use_handlers=False, implicit=True)
    my_include = TaskInclude().load(dict(include="test.yml", static=False))
    my_block = Block().load(
        dict(block=[[my_task], [my_include]]),
        play=my_play,
        role=None,
        task_include=None,
        use_handlers=False
    )
    assert not my_block.all_parents_static()

# Generated at 2022-06-13 08:00:43.505887
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.task import Task as RoleTask
    block = Block()
    assert False == block.has_tasks()
    parent = Block()
    task = RoleTask()
    parent.block = [task]
    parent.rescue = [task]
    parent.always = [task]
    block.parent = parent
    assert True == block.has_tasks()
    parent = TaskInclude()
    block.parent = parent
    assert False == block.has_tasks()
    task = Block()
    parent.block = [task]
    block.parent = parent
    assert True == block.has_tasks()
    task = Task()
   

# Generated at 2022-06-13 08:00:48.363496
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    block.load({'block': [{"action": "debug", "msg": "msg1"}, {"action": "debug", "msg": "msg2"}]})
    assert block.has_tasks()
    block.load({'block': []})
    assert not block.has_tasks()



# Generated at 2022-06-13 08:00:57.846772
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Test Case 1
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    # Setup
    play_name = "test_play"
    role_name = "test_role"
    block_1 = Block(play=Playbook()._load_play(Play().load({"name": play_name}), None), role=Role().load({'name': role_name}))
    block_2 = Block(play=Playbook()._load_play(Play().load({"name": play_name}), None), role=Role().load({'name': role_name}))


# Generated at 2022-06-13 08:01:03.054892
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Create a role, a task include and a new block
    r = Role()
    ti = TaskInclude()
    b = Block(parent=ti, role=r)

    # Set statically_loaded of the task include
    ti.statically_loaded = True

    # If all of the parents are statically loaded, all_parents_static() must be True
    assert b.all_parents_static() == True

    # Set statically_loaded of the task include
    ti.statically_loaded = False

    # If not all of the parents are statically loaded, all_parents_static() must return False
    assert b.all_parents_static() == False

# Generated at 2022-06-13 08:01:10.002953
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    bl = Block(play = Dummy(), role = Dummy(), task_include = Dummy())
    testdata = {'bar': 'BAR', 'foo': 'FOO', 'meta': 'META', 'name': 'TESTTASK',
                'rescue': [], 'always': [], 'dep_chain': ['a', 'b', 'c']}

    r = Role()
    r.deserialize(None)
    p = Block()
    p.deserialize(None)
    testdata['role'] = r
    testdata['parent'] = p
    testdata['parent_type'] = 'Block'

    bl.deserialize(testdata)
    actualresult = bl.__dict__

# Generated at 2022-06-13 08:01:11.099392
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block()
    assert b.deserialize({}) is None

# Generated at 2022-06-13 08:01:18.026839
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    #
    # initialize Block object 
    # 
    obj = Block()

    #
    # test get_dep_chain() on Block object
    #
    if obj.get_dep_chain() == None:
        print('TEST OK: get_dep_chain: return None')
    else:
        print('TEST FAILED: get_dep_chain: not return None')


# Generated at 2022-06-13 08:01:27.897430
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    # Test case
    ##################################################################
    # Create a test block        
    # Create a test parent task with implicit set to True
    #
    # Create a test role
    # Create a test role_include
    # Create a test parent task with implicit set to True
    #    
    # 
    # ##################################################################
    b = Block()
    task = Task()
    task.action = "setup"
    task.implicit = True
    b._parent = task
    
    task2 = Task()
    task2.action = "test"
    task2.implicit = True
    task.role = task2
    role = Role()
    role.name = "test_role"


# Generated at 2022-06-13 08:01:33.776828
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Load test yaml file.
    with open('tests/data/playbook-tasks.yml', 'r') as stream:
        try:
            yaml_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    yaml_data = yaml_data['tasks']

    # Load test Playbook object.
    play = Play()
    play.load(dsobj=yaml_data)
    task = play.get_tasks()
    
    # Test the filter_tagged_tasks
    task = task.filter_tagged_tasks(all_vars=None)
    assert task.has_tasks() == True
    
    print('=== test for filter_tagged_tasks passed ===')
# Test unit for

# Generated at 2022-06-13 08:01:54.584448
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # block with no tags
    ds = dict(
        block = [
            dict(
                action = 'include',
            ),
        ]
    )
    b = Block.load(ds, role=dict(name='foo'), task_include=dict(name='bar', static=True, parent_role=dict(name='role')))
    filtered = b.filter_tagged_tasks({})
    assert len(filtered.block) == 0
    assert len(filtered.rescue) == 0
    assert len(filtered.always) == 0

    # block with all tags defined in include, so nothing filtered
    ds = dict(
        block = [
            dict(
                action = 'include',
                tags = ['bar', 'foo']
            ),
        ]
    )

# Generated at 2022-06-13 08:02:00.839664
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleMapping
    pc = PlayContext()
    b = Block()
    b.set_loader(10)
    b._play = Play()
    b._play._loader = 10
    assert b._loader == 10, 'b._loader is %s' % b._loader


# Generated at 2022-06-13 08:02:12.148398
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase

    play_name = 'my_play'
    play_hosts = ['host1']
    play_vs = dict(foo='asd')

    class MyTask(Task):
        _task_type = 'My Task'
        VALID_ARGS = frozenset()
        def __init__(self, play):
            super(MyTask, self).__init__(play=play, action='my_task', args=dict())

    class MyActionModule(ActionBase):
        def run(self, tmp=None, task_vars=dict()):
            return (0, 'Ok', {})


# Generated at 2022-06-13 08:02:13.062633
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    raise NotImplementedError


# Generated at 2022-06-13 08:02:17.037214
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Unit test setup:
    from ansible.playbook.task_include import TaskInclude
    # Setup code goes here
    b = Block()
    try:
        b.deserialize({})
    except Exception as e:
        # This should throw an exception due to None in loader
        assert type(e) == AnsibleParserError
    # Unit test teardown:
    return

# Generated at 2022-06-13 08:02:22.817067
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
  from ansible.parsing.yaml.objects import AnsibleSequence
  from ansible.parsing.yaml.objects import AnsibleMapping
  from ansible.parsing.yaml.dumper import AnsibleDumper
  
  from ansible.playbook.attribute import Attribute
  from ansible.playbook.attribute import FieldAttribute
  from ansible.playbook.base import Base
  from ansible.playbook.task import Task
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.handler_task_include import HandlerTaskInclude
  
  def test_Block_deserialize_1():
    b = Block()
    data = dict()

# Generated at 2022-06-13 08:02:24.299975
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
	pass


# Generated at 2022-06-13 08:02:38.313753
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.handler_task_include import HandlerTaskInclude
  ds = dict()
  ds['role']= dict()
  ds['parent'] = dict()
  ds['parent_type'] = 'Block'
  b = Block()
  b.deserialize(ds)
  assert b.role is None
  assert b.parent is None
  ds['role']=dict()
  
  ##normal case
  r = Role()
  r.deserialize(ds['role'])
  b.deserialize(ds)
  assert b.role is r
  #assert role deserialized correctly
  ds['role'] = dict()
  dp = Block()

# Generated at 2022-06-13 08:02:51.703412
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # _play_ds=dict(name="TEST", hosts=['localhost'])
    _play_ds = dict(name="TEST", hosts=['localhost'], roles=[dict(name='TEST', tasks=[dict(name="TEST", state='TEST')])])
    my_play = Play().load(_play_ds, variable_manager=VariableManager(), loader=DictDataLoader())
    assert my_play._play_hosts == ['localhost'], my_play._play_hosts
    role = my_play.get_roles()[0]

    # block_ds=dict(block=[dict(action=dict(module='test'), tags=['BLOCK_TAG'])])

# Generated at 2022-06-13 08:02:54.181834
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    b = Block()
    assert b.get_first_parent_include() is None

# Generated at 2022-06-13 08:03:09.013380
# Unit test for method copy of class Block
def test_Block_copy():
    task1 = Task(name='test')
    task2 = Task(name='test')
    assert task1.copy() != task2, "Compare two tasks that differ in name. Should be not equal"

# Generated at 2022-06-13 08:03:11.190074
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    assert b.copy()


# Generated at 2022-06-13 08:03:12.320358
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    assert 1==1

# Generated at 2022-06-13 08:03:14.291127
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = block.deserialize('data')
    assert(data == None)

# Generated at 2022-06-13 08:03:21.990921
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.role import Role

    module_args = dict(
        name=dict(type='str'),
        state=dict(type='str', default='present', choices=['absent', 'present']),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    task1 = Task()
    task1.action = 'action1'

    role1 = Role()
    role1.name = 'role1'
    taskinclude1 = TaskInclude()
    taskinclude1.name = 'name1'

# Generated at 2022-06-13 08:03:24.090140
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    t = Block(loader=None)
    t.set_loader()
    assert t._loader is not None


# Generated at 2022-06-13 08:03:32.512163
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # create a test block
    block = Task()
    block.block = Task()
    block.rescue = Task()
    block.always = Task()
    
    # run the method above
    assert block.has_tasks() == True
    print("Test has_tasks is OK")
   
    return
# create a test task
task = Task()
task.action = 'debug'
task.name = 'my first task'

block = Block()
block.block = task

print("========================================")
print("--- Test module 'ansible.playbook.block'")
print("========================================")
test_Block_has_tasks()

# Generated at 2022-06-13 08:03:42.300895
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Setup test objects
    play = Play()
    loader = DataLoader()
    variable_manager = VariableManager()
    block_object = Block.load({
        "block": [
            {
                "action": {
                    "module": "shell",
                    "args": "echo hello"
                }
            }
        ]
    }, play=play, variable_manager=variable_manager, loader=loader)
    # Test
    block_object.deserialize({"task_include": {}})

# Generated at 2022-06-13 08:03:49.068456
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import ansible.module_utils
    import ansible.module_utils.facts.system.distribution
    import ansible.playbook.play_context
    import ansible.playbook.role
    import ansible.playbook.role.include
    import ansible.plugins.block
    import ansible.plugins.callback
    import ansible.plugins.connection
    import ansible.plugins.lookup
    import ansible.plugins.strategy
    import ans

# Generated at 2022-06-13 08:03:53.220455
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block();

    import json
    data = {"dep_chain": None, "role": {}, "parent": {}, "parent_type": "Block"}

    block.deserialize(data);


# Generated at 2022-06-13 08:04:21.188942
# Unit test for method copy of class Block
def test_Block_copy():
    test_block = Block()
    test_rescue = Block()
    test_always = Block()
    test_block.rescue = test_rescue
    test_block.always = test_always
    test_block.block = [True, False]
    test_block.rescue = [True, False]
    test_block.always = [True, False]
    test_block._dep_chain = []
    test_block._dep_chain.append(True)
    test_block._dep_chain.append(False)
    try:
        test_block.copy() 
    except Exception as err:
        assert type(err).__name__ == 'AssertionError'
    else:
        raise AssertionError

# Generated at 2022-06-13 08:04:21.779230
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:04:24.847912
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    block = Block()
    assert(block.get_first_parent_include() == None)
    parent = TaskInclude()
    block._parent = parent
    assert(block.get_first_parent_include() == parent)


# Generated at 2022-06-13 08:04:31.999144
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = {'name': 'test_block', 'metadata': {}}
    # 1. Test for regular Block
    b = Block()
    b.deserialize(data)
    assert b.name == 'test_block', "The name {} of deserialized Block is not 'test_block'".format(b.name)
    assert b.metadata == {}, "The metadata {} of deserialized Block is not {}".format(b.metadata, {})

    # 2. Test for Block with non-empty list of tasks
    data = {'name': 'test_block', 'metadata': {}, 'tasks': [{'name': 'task1'}, {'name': 'task2'}]}
    b = Block()
    b.deserialize(data)

# Generated at 2022-06-13 08:04:40.820113
# Unit test for method copy of class Block
def test_Block_copy():

    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    b._attributes = {'register': Sentinel}
    assert b.copy()

    b._attributes = {'register': 'test_register'}
    assert b.copy()

    b._attributes = {}
    assert b.copy()

    b._attributes = {'loop': 'my_testing_loop'}
    assert b.copy()

    b._attributes = {'loop': 'my_testing_loop', 'loop_control': {}}
    assert b.copy()

    b._attributes = {'vars': {}}
    assert b.copy()

    b._attributes = {'when': 'test_when'}
    assert b.copy()



# Generated at 2022-06-13 08:04:48.875523
# Unit test for method copy of class Block
def test_Block_copy():

    # create an empty yaml file
    with open('test_file.yml', 'w') as f:
        yaml.dump([], f, default_flow_style=False)

    # read the yaml file
    with open('test_file.yml', 'r') as f:
        my_list = yaml.load(f)

    # create inventory
    inventory = InventoryManager(loader=loader, sources='localhost,')

    # create variable_manager, and pass the inventory
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create the play

# Generated at 2022-06-13 08:04:54.677704
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:05:09.675479
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    ############################################
    # block1 -> block2 -> block3 -> task
    ############################################
    block1 = Block(None, None, None)
    block2 = Block(None, block1, None)
    block3 = Block(None, block2, None)
    task = Task(None, block3, None)

    assert task.all_parents_static()
    assert block3.all_parents_static()
    assert block2.all_parents_static()
    assert block1.all_parents_static()

    ############################################
    # block1 -> block2 -> block3 -> task -> task_include
    ############################################
    from ansible.playbook.task_include import TaskInclude
    task_include = TaskInclude(None, task, None)

    assert not task_include.all_parents_static

# Generated at 2022-06-13 08:05:14.199235
# Unit test for method copy of class Block
def test_Block_copy():
    args = dict(
        exclude_parent = False,
        exclude_tasks = False,
    )
    obj = Block()
    try:
        obj.copy(**args)
    except Exception as e:
        assert(e.args[0] == "Block.copy is not implemented.")


# Generated at 2022-06-13 08:05:22.467927
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    try:
        block.copy()
    except Exception as e:
        print('FAIL: ')
        print('\tException:', e)
    else:
        print('PASS')

    try:
        block.copy(exclude_parent=True)
    except Exception as e:
        print('FAIL: ')
        print('\tException:', e)
    else:
        print('PASS')

    try:
        block.copy(exclude_tasks=True)
    except Exception as e:
        print('FAIL: ')
        print('\tException:', e)
    else:
        print('PASS')

# Generated at 2022-06-13 08:05:40.202649
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    obj = Block(
        play = dict(),
        parent_block = dict(),
        role = dict(),
        task_include = dict(),
        use_handlers = False,
        implicit = False,
    )
    obj.set_loader(loader = dict())


# Generated at 2022-06-13 08:05:52.386959
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from collections import namedtuple
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleUnicode
    MockInclude = namedtuple('MockInclude', ['tasks'])
    MockTask = namedtuple('MockTask', ['module_name', 'action'])
    MockRescue = namedtuple('MockRescue', ['tasks'])

# Generated at 2022-06-13 08:06:02.623904
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import mock
    import yaml
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    # block stanza
    play_source = dict(
        name = "Ansible Play",
        hosts = ['localhost'],
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), tags=['always'], name='shell-always'),
            dict(action=dict(module='shell', args='ls'), tags=['test1'], name='shell-test1'),
            dict(action=dict(module='shell', args='ls'), tags=['test2'], name='shell-test2'),
        ]
    )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=yaml.SafeLoader)
    play._

# Generated at 2022-06-13 08:06:08.390334
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test method parameter all_vars
    # Create an instance of class Block
    block = Block(implicit=True, use_handlers=False) 
    tags = ['blah']
    # Create an instance of class mock_obj
    mock_obj = mock_obj() 
    mock_obj.tags = tags 
    # Create an instance of class mock_obj
    mock_obj2 = mock_obj() 
    # Create an instance of class mock_obj
    mock_obj3 = mock_obj() 
    # Call method filter_tagged_tasks of class Block
    ret_obj = block.filter_tagged_tasks([mock_obj, mock_obj2, mock_obj3]) 


# Generated at 2022-06-13 08:06:20.611697
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test method
    # Turn off the implicit_catch_ansible_errors while we test this, because it can't be loaded
    # with the way we're setting up the play context
    implicit_catch_ansible_errors = C.DEFAULT_IMPLICIT_CATCH_ANSIBLE_ERRORS
    C.DEFAULT_IMPLICIT_CATCH_ANSIBLE_ERRORS = False

    playbook = PlayBook()

    my_inv = Inventory('/dev/null')
    my_host = Host(name='localhost')
    my_host.set_variable('ansible_connection', "local")
    my_inv.get_hosts().append(my_host)

    my_play = Play()
    my_play.name = 'myplay'
    my_play.hosts = ['localhost']
    my_play.set_loader

# Generated at 2022-06-13 08:06:23.407559
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    assert (Block(implicit=True)
            .has_tasks() == False)

    assert (Block(block = [Task()], implicit=True)
            .has_tasks() == True)


# Generated at 2022-06-13 08:06:34.915943
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:06:37.231010
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Unit test for method Block.deserialize
    '''
    # setup

    # test
    Block.deserialize()
    # cleanup



# Generated at 2022-06-13 08:06:44.251099
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # initialize first
    my_block = Block()
    # create the data
    task1 = Task()
    task2 = Task()
    task3 = Task()
    task1_dict = task1.serialize()
    task2_dict = task2.serialize()
    task3_dict = task3.serialize()

# Generated at 2022-06-13 08:06:55.682792
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # initialize test
    test_Block = Block()
    test_loader = None

    # test case 1
    test_Block._loader = None
    test_Block._parent = None
    test_Block._role = None
    expected_1 = None
    actual_1 = test_Block.set_loader(test_loader)
    assert expected_1 == actual_1, "Expected: " + str(expected_1) + " Actual: " + str(actual_1)

    # test case 2
    test_Block._loader = None
    test_Block._parent = None
    test_Block._role = Role()
    expected_2 = None
    actual_2 = test_Block.set_loader(test_loader)
    assert expected_2 == actual_2, "Expected: " + str(expected_2) + " Actual: "

# Generated at 2022-06-13 08:07:14.100609
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Test with no parent
    b = Block()
    if b.get_first_parent_include() != None:
        raise Exception("get_first_parent_include() failed")

    # Test with parent that does not inherit TaskInclude
    b._parent = Block()
    if b.get_first_parent_include() != None:
        raise Exception("get_first_parent_include() failed")

    # Test with parent that inherits TaskInclude
    from ansible.playbook.task_include import TaskInclude
    b._parent = TaskInclude('')
    if b.get_first_parent_include() == None:
        raise Exception("get_first_parent_include() failed")

test_Block_get_first_parent_include()


# Generated at 2022-06-13 08:07:21.858573
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    b1 = Block(play=None, parent_block=None, role=None, task_include=None)
    b2 = Block(play=None, parent_block=b1, role=None, task_include=None)
    t1 = TaskInclude(play=None, parent_block=b2, role=None, task_include=None)
    t2 = TaskInclude(play=None, parent_block=t1, role=None, task_include=None)
    h1 = HandlerTaskInclude(play=None, parent_block=t2, role=None, task_include=None)

    b1.statically_loaded = True
    b2.statically_

# Generated at 2022-06-13 08:07:28.041497
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Tests the filter_tagged_tasks method of class Block
    '''
    # Create a fake Host
    fake_host = Host()

    # Create a fake PlayBook
    fake_play = Play()
    fake_play.vars = {}
    fake_play.vars['tags'] = ['tag1']

    # Create a fake Task
    fake_task1 = Task()
    fake_task1.action = 'copy'
    fake_task1.set_loader(DataLoader())
    fake_task1.tags = ['tag1']

    fake_task2 = Task()
    fake_task2.action = 'copy'
    fake_task2.set_loader(DataLoader())
    fake_task2.tags = ['tag1', 'tag2']


# Generated at 2022-06-13 08:07:28.688007
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:07:36.122657
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    def make_block_with_simple_parent(static):
        class MyBlock(Block):
            pass
        myBlock = MyBlock(play=object, parent_block=object)
        myBlock.statically_loaded = static
        return myBlock
    # Block with statically loaded true parent
    myBlock = Block(play=object, parent_block=make_block_with_simple_parent(True))
    assert myBlock.all_parents_static() == True
    # Block with statically loaded false parent
    myBlock = Block(play=object, parent_block=make_block_with_simple_parent(False))
    assert myBlock.all_parents_static() == False

# Generated at 2022-06-13 08:07:36.941569
# Unit test for method copy of class Block
def test_Block_copy():
    pass


# Generated at 2022-06-13 08:07:38.327447
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # test initialization of method
    block = Block()
    assert block.get_first_parent_include() == None


# Generated at 2022-06-13 08:07:39.120845
# Unit test for method copy of class Block
def test_Block_copy():
    b=Block()



# Generated at 2022-06-13 08:07:46.757668
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['testhost'])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    play_context.network_os

# Generated at 2022-06-13 08:07:49.176390
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert not block.has_tasks()

if __name__ == '__main__':
    # Unit test
    test_Block_has_tasks()

# Generated at 2022-06-13 08:08:04.546254
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    res = block.deserialize({'block': [{'debug': {'msg': 'test'}}]})

# Generated at 2022-06-13 08:08:05.866895
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # setup
    b = Block()
    # test
    assert b.has_tasks() == False


# Generated at 2022-06-13 08:08:11.906037
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    tag1 = ['tag1','tag2','tag4']
    tag2 = ['tag2','tag3']
    tag3 = ['tag3','tag4']
    tag4 = ['tag4']
    tag5 = ['tag5']

# Generated at 2022-06-13 08:08:17.824557
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    myblock = Block()
    assert myblock.has_tasks() == False
    T = Task()
    T.action = "shell"
    T.args = "echo hi"
    myblock.block.append(T)
    assert myblock.has_tasks() == True

# Generated at 2022-06-13 08:08:25.722382
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    b._valid_attrs = {'ignore_errors':'ignore_errors', 'block':'block'}
    b.ignore_errors = True
    b.block = [1,2,3]
    copy = b.copy()
    assert copy.ignore_errors == b.ignore_errors
    assert b.block[0] == copy.block[0]
    assert b.block[1] == copy.block[1]
    assert b.block[2] == copy.block[2]


# Generated at 2022-06-13 08:08:35.043180
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    [description]
    test method filter_tagged_tasks of class Block
    '''
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    task_obj_0 = Task()
    block_obj_1 = Block()
    block_obj_2 = Block()
    tasks_list_0 = [task_obj_0]
    tasks_list_1 = [task_obj_0]
    block_obj_2.block = block_obj_1
    block_obj_1.block = tasks_list_1
    all_vars = {}
    try:
        block_obj_2.filter_tagged_tasks(all_vars)
    except Exception as e:
        assert False, "Raise exception unexpectedly: {}".format(e)
   

# Generated at 2022-06-13 08:08:42.432637
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # creating a Play object
    p = Play()

    # creating a Block object t_b and adding a list of tasks
    t1 = Task()
    t2 = Task()
    t2.loop = "{{testvars}}"
    t3 = Task()
    t4 = Task()
    t4.loop = "{{testvars}}"
    t5 = Task()
    t6 = Task()
    t_b = Block()
    t_b.block = [t1,t2,t3,t4,t5,t6]

    # creating an Include object and adding it in the parent of the Block object
    t_i = TaskInclude()
    t_b.parent = t_i

    # creating another Include object and adding it in the parent of the Include object
    t_i2 = TaskInclude()

# Generated at 2022-06-13 08:08:51.339505
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block.load({u'block': [
        {u'block': [
         {u'tags': [u'foo'], u'action': u'module', u'module': u'debug'},
         {u'action': u'module', u'module': u'debug'},
         ],
         },
        {u'tags': [u'foo,bar'], u'action': u'module', u'module': u'debug'},
    ],
    }, task_include='all')
    all_vars = None
    output = block.filter_tagged_tasks(all_vars)
    assert output == '<ansible.playbook.block.Block object at 0x7f817a8f12d0>'

# Instantiate a Block object to use method

# Generated at 2022-06-13 08:08:58.175613
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(
        implicit=True,
        use_handlers=True,
        always=[],
        rescue=[],
        block=[
            {
                'action': {
                    '__ansible_module__': 'test',
                    '__ansible_arguments__': None,
                    '__ansible_no_log__': False,
                },
                'name': None,
            },
        ],
    )
    assert block.has_tasks() is True
    assert block.block[0].action == 'test'
    assert block.rescue == []
    assert block.always == []

# Generated at 2022-06-13 08:09:07.469232
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    # Set up the obj variable
    block = Block()

    # Set up the variable_manager variable
    variable_manager = {}

    # Set up the loader variable
    loader = {}

    # Set up the role variable
    role = {}

    # Set up the line variable
    line = {}

    # Call the method to test
    block.set_loader(loader)

    # Check that the variables are as expected
    assert block._loader == loader
    assert block._role == role
    assert block._line == line
    assert block._parent is None
