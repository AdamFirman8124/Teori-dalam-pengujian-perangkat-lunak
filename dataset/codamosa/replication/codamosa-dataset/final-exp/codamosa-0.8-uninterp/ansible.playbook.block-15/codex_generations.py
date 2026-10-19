

# Generated at 2022-06-13 07:59:58.663191
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from .task import Task
    from .task_include import TaskInclude

    block1 = Block()

# Generated at 2022-06-13 08:00:06.708086
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    b = Block()
    t = Task()
    t._ds = dict(name=dict(x="x"), changed_when="/x/")
    t._parent = b
    b._parent = t
    b._ds = dict(name='x', rescue=dict(x="x"), always=dict(x="x"))
    b._parent = t
    t._ds = dict(x="x")
    t._parent = b
    b._role = Role()
    b._parent = t
    b._ds = dict(name='x', rescue=dict(x="x"), always=dict(x="x"))
    b._parent = t
    b._role = Role()
    b._parent = t
    r = Role()
   

# Generated at 2022-06-13 08:00:17.490566
# Unit test for method serialize of class Block
def test_Block_serialize():
    # Create a test_block
    test_block = Block()
    # Set value for test_block

# Generated at 2022-06-13 08:00:25.755279
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    # The test uses as a data sample a dict object, which is a valid data for the function
    # The function return value is compared with a valid return value
    data_one = {'hosts': 'all', 'tasks': [{'name': 'sample task', 'shell': 'echo hi there'}]}
    data_two = [{'name': 'sample task', 'shell': 'echo hi there'}]
    # The function is called with the sample data
    result_one = Block.preprocess_data(data_one)
    result_two = Block.preprocess_data(data_two)
    # Here are the expected/valid return values. The function return value is compared with these.

# Generated at 2022-06-13 08:00:27.600939
# Unit test for method copy of class Block
def test_Block_copy():
    assert(Block.copy())



# Generated at 2022-06-13 08:00:30.306680
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    block = Block()
    data = dict(block = [])
    block.preprocess_data(data)
    # Todo; assert function call


# Generated at 2022-06-13 08:00:36.284856
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block_obj = Block()
    block_obj.block = [{"action":"include_tasks", "name":"/home/user/playbooks/test.yml"}, {"action":"command","name":"test"}]
    result = block_obj.filter_tagged_tasks(["test"])

    assert result

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 08:00:43.319265
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.task_include
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.play
    import ansible.playbook.playbook
    import ansible.playbook.handler_task

# Generated at 2022-06-13 08:00:52.311361
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    def assert_equals(a, b):
        if a != b:
            raise Exception("assertion failed. a=%s, b=%s" % (a, b))

    b = Block()
    b.tags = ['foo']
    b.block = [
        Task(action='ping')
    ]
    b.rescue = [
        Task(action='ping', tags=['bar'])
    ]
    b.always = [
        Task(action='ping', tags=['baz'])
    ]

    filtered_block = b.filter_tagged_tasks({})
    assert_equals(len(filtered_block.block), 0)

# Generated at 2022-06-13 08:00:54.595885
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    b = Block()
    assert b.all_parents_static() == True
    b._parent == Sentinel
    assert b.all_parents_static() == True
    b._parent = 'S'
    assert b.all_parents_static() == 'S'
    b._parent = Block()
    assert b.all_parents_static() == True


# Generated at 2022-06-13 08:01:46.057484
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    task1 = Task()
    task1._role = None
    task1._parent = None
    task1._play = None
    task1._dep_chain = None
    task1._loader = None
    task1._attributes = {}
    task1._valid_attrs = {}
    result = task1.filter_tagged_tasks(None)
    assert result == None


# Generated at 2022-06-13 08:01:53.680469
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    class_mock = mocker.Mock()
    class_mock2 = mocker.Mock()
    class_mock3 = mocker.Mock()
    b._parent = class_mock
    b._role = class_mock2
    b._dep_chain = [class_mock3]

    b.set_loader(class_mock)
    assert class_mock.mock_calls == [mocker.call.set_loader(class_mock),mocker.call.set_loader(class_mock)]
    assert class_mock2.mock_calls == [mocker.call.set_loader(class_mock)]
    assert class_mock3.mock_calls == [mocker.call.set_loader(class_mock)]


# Generated at 2022-06-13 08:01:58.921328
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # Declaration of test variable block
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False)
    # Verify if the variable block is equals to block
    assert block == block
    # Verify if the variable block is not equals to block
    assert block != block


# Generated at 2022-06-13 08:02:10.473671
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Test the case where Block has no parent, which should return None
    block = Block()
    if block.get_first_parent_include() is not None:
        raise AssertionError("Block has no parent, but get_first_parent_include did not return None")

    # Test the case where Block has a parent, which should return the parent
    block2 = Block()
    block.parent = block2
    if block.get_first_parent_include() is not block2:
        raise AssertionError("Block's parent is " + str(block2) + ", but get_first_parent_include did not return that")

    # Test the case where the Block's parent is not an include, which should return None
    block3 = Block()
    block2.parent = block3

# Generated at 2022-06-13 08:02:13.184440
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(
                    play=None,
                    parent_block=None,
                    role=None,
                    task_include=None,
                    use_handlers=False,
                    implicit=True
                )
    if block.has_tasks() == 0:
        return True
    else:
        return False


# Generated at 2022-06-13 08:02:14.500618
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    block_obj = Block()
    result = block_obj.all_parents_static()
    assert result == False
    return result

# Generated at 2022-06-13 08:02:19.572342
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    options = Mock()
    options.tags = []
    options.skip_tags = []
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/test_inventories/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:02:34.988796
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    #test block does not have attribute _parent
    b = Block()
    assert b.get_first_parent_include() == None
    #test block does have attribute _parent, but _parent is not task include
    b = Block()
    p = Block()
    b._parent = p
    assert b.get_first_parent_include() == None
    #test block does have attribute _parent which is task include
    b = Block()
    p = TaskInclude()
    b._parent = p
    assert b.get_first_parent_include() == p
    #test block does have attribute _parent which has a parent which is task include
    b = Block()
    p = Block()
    g = TaskInclude()
    p._parent = g
    b._parent = p

# Generated at 2022-06-13 08:02:40.691957
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    obj = Block()
    block = {"block1": [{"task1": "task1"}]}
    task_include = TaskInclude(block, task_include=TaskInclude)
    block_obj = Block(play=None, parent_block=task_include, role=None, task_include=task_include, use_handlers=False, implicit=True, loader=None)
    result = block_obj.get_first_parent_include()
    assert result == task_include


# Generated at 2022-06-13 08:02:53.428182
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    host_vars = dict()
    host_vars["host1"] = dict()
    host_vars["host1"]["tags"] = ["all"]
    host_vars["host2"] = dict()
    host_vars["host2"]["tags"] = ["tag1"]
    host_vars["host3"] = dict()
    host_vars["host3"]["tags"] = ["tag2"]
    host_vars["host4"] = dict()
    host_vars["host4"]["tags"] = ["tag1", "tag2"]
    host_vars["host5"] = dict()
    host_vars["host5"]["tags"] = ["tag1", "tag3"]
    host_vars["host6"] = dict()

# Generated at 2022-06-13 08:03:34.570178
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Create a mock object
    obj = Mock()

    # Create a Block instance and check the filter_tagged_tasks method
    block = Block()
    block.filter_tagged_tasks(obj)

    # Check if the filter_tagged_tasks method was called
    block.filter_tagged_tasks.assert_called_with(obj)

# Generated at 2022-06-13 08:03:36.501721
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
  block = Block()
  assert block.get_dep_chain() is None


# Generated at 2022-06-13 08:03:47.500417
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler import Handler
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role.metadata import RoleMetadata

    b1 = Block()
    b1._play = None
    b1._use_handlers = None
    b1._dep_chain = None
    b1._parent = None

# Generated at 2022-06-13 08:03:59.278984
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    play = {}
    parent = {}
    role = {}
    block = Block(play=play, parent_block=parent, role=role)
    block.name = 'task_1'
    task_1 = {}
    task_1 = {}
    task_1 = {}
    task_1 = {}
    task_1 = {}
    task_1 = {}
    op_1 = {}
    op_1 = {}
    block['__ansible_action__'] = op_1
    block['__ansible_position__'] = 1
    block['__ansible_type__'] = 'task'
    block['__ansible_version__'] = 2
    block['block'] = task_1
    
    all_vars = {}
    result = block.filter_tagged_tasks(all_vars)

# Generated at 2022-06-13 08:04:01.857538
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block.load(dict(block=[]), play=MockPlay(), use_handlers=True)
    b.copy()

# Generated at 2022-06-13 08:04:10.183573
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():

    import json
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()

    # JSON data for a single task without static value
    task1_data = '{"name": "test", "action": "shell"}'

    # JSON data for a single task with static value
    task2_data = '{"name": "test", "static": true, "action": "shell"}'

    # JSON data for a single task with static value at task include
    task3_data = '{"name": "test", "static": true, "action": "shell"}'

# Generated at 2022-06-13 08:04:24.059562
# Unit test for method has_tasks of class Block

# Generated at 2022-06-13 08:04:31.351816
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # init a fake env
    p = Play.load(dict(name='test_play', hosts='test_hosts',
                       gather_facts='no', tags=['test_tag'],
                       vars=dict(yay='yes')))
    b = Block.load(dict(name='test_block', vars=dict(zap='zop')), play=p)

# Generated at 2022-06-13 08:04:40.332489
# Unit test for method copy of class Block
def test_Block_copy():
    def _dupe_task_list(task_list, new_block):
        new_task_list = []
        for task in task_list:
            new_task = task.copy(exclude_parent=True)
            if task._parent:
                new_task._parent = task._parent.copy(exclude_tasks=True)
                if task._parent == new_block:
                    # If task._parent is the same as new_block, just replace it
                    new_task._parent = new_block
                else:
                    # task may not be a direct child of new_block, search for the correct place to insert new_block
                    cur_obj = new_task._parent
                    while cur_obj._parent and cur_obj._parent != new_block:
                        cur_obj = cur_obj._parent

                    cur_obj._parent

# Generated at 2022-06-13 08:04:42.856508
# Unit test for method copy of class Block

# Generated at 2022-06-13 08:05:12.536134
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

    def get_list_of_tags(tasks, tag_list=None):
        if tag_list is None:
            tag_list = []
        for task in tasks:
            if isinstance(task, Task):
                tag_list.extend(task.tags)
            elif isinstance(task, Handler):
                tag_list.extend(task.tags)
            elif isinstance(task, TaskInclude):
                get_list_of_tags(task.tasks, tag_list)

# Generated at 2022-06-13 08:05:22.208168
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Create block 1
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    my_block = Block()
    my_block.block = list()
    my_block.rescue = list()
    my_block.always = list()
    my_block.statically_loaded = True

    # Create Tasks t1, t2, t3
    t1 = Task()
    t2 = Task()
    t3 = Task()

    # Create Iclude task t4
    my_task_include = TaskInclude()
    my_task_include.statically_loaded = True

    # Create Block my_block2
    my_block2 = Block()
    my

# Generated at 2022-06-13 08:05:32.599380
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=None)
    b._valid_attrs = {'a': None, 'b': None}
    b._attributes = {'a': 1, 'b': 2}
    b._dep_chain = None
    b._parent = None
    b._role = None

    b.deserialize({'a': 1, 'b': 2, 'dep_chain': None, 'parent': None, 'role': None, 'parent_type': None})

    b._valid_attrs = {'a': None, 'b': None}
    b._attributes = {'a': 1, 'b': 2}
    assert b._dep_chain is None
    assert b._parent is None
    assert b

# Generated at 2022-06-13 08:05:34.067085
# Unit test for method deserialize of class Block
def test_Block_deserialize():
	# Create an instance of class Block without any required fields
	a = Block()

	# deserialize the data
	a.deserialize(None)


# Generated at 2022-06-13 08:05:35.241614
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    obj = Block()
    assert obj.all_parents_static() == True


# Generated at 2022-06-13 08:05:36.109488
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    raise NotImplementedError

# Generated at 2022-06-13 08:05:37.536853
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    r = b.copy()

    assert check_equal(r, b)


# Generated at 2022-06-13 08:05:49.723272
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    assert b.has_tasks() == False

    b1 = Block()
    b1.block = [
        {'tasks': [{'action': {'module': 'debug', 'args': 'msg=test', 'name': 'test'}}]},
        {'tasks': [{'action': {'module': 'shell', 'args': 'echo test', 'name': 'test2'}}]}
    ]
    assert b1.has_tasks() == True

    b2 = Block()

# Generated at 2022-06-13 08:06:01.497335
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block


# Generated at 2022-06-13 08:06:09.152951
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    role = Role.load(dict(name='test_role', tasks=[dict(action='foo', loop='{{ range(1, 5) }}', when='{{ x == \'test\' }}')]))
    hostvars = dict(test_host=dict(x='test'))
    play_context = dict(name='test_play', remap_vars=dict(x='test_host.x'))

    # simple test to ensure that a block can be copied without errors
    block = Block.load(dict(block=role.tasks), play=play_context, loader=loader, variable_manager=VariableManager(loader=loader, host_vars=hostvars))

    assert isinstance

# Generated at 2022-06-13 08:06:32.701275
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    b = Block()
    ti = TaskInclude()
    ti.name = 'ti'
    b.name = 't'
    assert b.get_first_parent_include() == None
    ti.block = [b]
    assert b.get_first_parent_include() == ti


# Generated at 2022-06-13 08:06:41.361578
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block(play=None, parent_block=None, role=None,  task_include=None, use_handlers=False, implicit=None)
    block._ds = None
    loader = None

# Generated at 2022-06-13 08:06:52.368764
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    # ansible 2.7 has updated the signature of Task.evaluate_tags()
    if LooseVersion(__ansible_version__) >= LooseVersion("2.7.0"):
        # ansible 2.7 version is evaluated
        # ansible 2.7 has updated the signature of Task.evaluate_tags()
        def evaluate_tags(self, only_tags, skip_tags, all_vars=None):
            return super(Task, self).evaluate_tags(all_vars, only_tags, skip_tags)
    else:
        # ansible < 2.7 version is evaluated
        def evaluate_tags(self, only_tags, skip_tags, all_vars=None):
            return super(Task, self).evaluate_tags(only_tags, skip_tags)

    Task.evaluate_tags = evaluate_tags

    #

# Generated at 2022-06-13 08:07:02.322788
# Unit test for method copy of class Block
def test_Block_copy():
    loader = DataLoader()
    tasks_include = TaskInclude()
    tasks_include.meta = dict()
    tasks_include._play = Play()
    tasks_include.name = "TAGGED_TASKS"
    tasks_include.tasks = []
    tasks_include.role = Role()
    tasks_include._loader = loader
    tasks_include.tags = ["tag1", "tag2"]
    tasks_include.block = Block()
    tasks_include.block._role = Role()
    tasks_include.block.name = "TAGGED_TASKS"
    tasks_include.block.block = [Task()]
    tasks_include.block.block[0].action = 'debug'
    tasks_include.block.block[0].become = True
    tasks_include.block.block[0].name

# Generated at 2022-06-13 08:07:17.114520
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()

    t1 = Task()
    t2 = Task()
    t3 = Task()
    t4 = Task()
    t5 = Task()
    t6 = Task()
    t7 = Task()
    t8 = Task()
    t9 = Task()
    t10 = Task()
    t11 = Task()
    t12 = Task()
    t13 = Task()
    t14 = Task()
    t15 = Task()
    t16 = Task()
    t17 = Task()
    t18 = Task()
    t19 = Task()
    t20 = Task()
    t21 = Task()
    t22 = Task()
    t23 = Task()
    t24 = Task()
    t25 = Task()
    t26 = Task()
    t27 = Task()

# Generated at 2022-06-13 08:07:17.988739
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass


# Generated at 2022-06-13 08:07:24.487040
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from test.lib.stubs import MockTask
    parent_block = Block()
    parent_task_include = TaskInclude()
    parent_task_include.set_loader(DummyLoader())
    parent_task_include.static_tasks = [parent_block]
    block = Block()
    print(block.get_first_parent_include())
    block.set_loader(DummyLoader())
    task = MockTask()
    block.block = [task]
    task.set_loader(DummyLoader())
    task.block = [block, parent_task_include]
    print(block.get_first_parent_include())
    block.reset_loader()
# test for get_first_parent_include ends here


# Generated at 2022-06-13 08:07:25.764310
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize(dict())



# Generated at 2022-06-13 08:07:27.105605
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    Block.has_tasks()
    pass

# Generated at 2022-06-13 08:07:36.018259
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    PlayContext.load()
    loader = DataLoader()
    variable_manager = VariableManager()
    vars_dict = dict(test1='test1',test2='test2')
    
    block_dict = dict()
    block_dict['tasks'] = [dict(action=dict(module="debug", args=dict(msg="debug1")), tags=['debug'])]
    block_dict['block'] = [block_dict['tasks'][0]]
    block_dict['rescue'] = [dict(action=dict(module="debug", args=dict(msg="rescue1")), tags=['rescue'])]
    block_dict['always'] = [dict(action=dict(module="debug", args=dict(msg="always1")), tags=['always'])]
    block_dict['vars'] = v

# Generated at 2022-06-13 08:07:55.811357
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize({})



# Generated at 2022-06-13 08:08:08.854985
# Unit test for method copy of class Block
def test_Block_copy():
    data1 = str()
    data2 = str()
    data3 = str()
    data4 = bool()
    data5 = str()
    data6 = str()
    data7 = bool()
    data8 = bool()
    data9 = bool()
    data10 = int()
    data11 = bool()
    data12 = bool()
    data13 = bool()
    data14 = bool()
    data15 = bool()
    data16 = bool()
    data17 = bool()
    data18 = bool()
    data19 = bool()
    data20 = bool()
    data21 = bool()
    data22 = bool()
    data23 = bool()
    data24 = bool()
    data25 = bool()
    data26 = bool()
    data27 = bool()
    data28 = bool()
    data29

# Generated at 2022-06-13 08:08:23.878642
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():    
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    
    # The value when using the Block method.
    value = {'block': [Task(dict(action='setup'))]}
    block = Block.load(value)
    assert(block.filter_tagged_tasks({}) == Block.load(value))
    assert(block.filter_tagged_tasks({},) == Block.load(value))
    assert(block.filter_tagged_tasks({},) == Block.load(value))
    assert(block.filter_tagged_tasks(None,) == Block.load(value))

    # The value when using the Block method with non empty list.

# Generated at 2022-06-13 08:08:28.023597
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    block = Block()
    task_include = TaskInclude()
    task_include.statically_loaded = True
    block._parent = task_include
    assert block.get_first_parent_include() == task_include
    block.statically_loaded = True
    assert block.get_first_parent_include() == task_include


# Generated at 2022-06-13 08:08:35.199165
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    b1 = Block()
    b2 = Block()
    b1.set_loader(DictDataLoader({}))
    b2.set_loader(DictDataLoader({}))
    b2._parent = b1
    assert b2.all_parents_static()
    b1._statically_loaded = False
    assert not b2.all_parents_static()
    b2._parent = None
    b1._statically_loaded = True
    assert b2.all_parents_static()


# Generated at 2022-06-13 08:08:41.944596
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    import ansible.playbook
    import ansible.playbook.block
    import ansible.playbook.task
    import ansible.playbook.handler
    from ansible.template import Templar
    # Create a new Block object with one attribute, and a simple task
    b = ansible.playbook.block.Block()
    b._attributes['name'] = "My block"
    t = ansible.playbook.task.Task()
    t._attributes['name'] = "My task"
    b._block.append(t)

    # Serialize the block to a string, then deserialize it into a new object
    data = b.serialize()
    new_b = ansible.playbook.block.Block()
    new_b.deserialize(data)

    # Ensure the new Block has the same name attribute and the

# Generated at 2022-06-13 08:08:50.935720
# Unit test for method copy of class Block
def test_Block_copy():
    import copy

    # Data that will be used to test Block.copy
    data = [
        {
            # Test 1: Ensure copy is being called by the copy method
            'block': [],
            'name': 'Test1'
        },
        {
            # Test 2: Ensure that immutables are being copied by the copy method
            'block': [task1],
            'name': 'Test2'
        },
        {
            # Test 3: Ensure mutables are being copied by the copy method
            'block': [task2],
            'name': 'Test3'
        }
    ]

    # Setup the mocks
    copy.deepcopy = Mock(return_value=data[0])
    task1.copy = Mock(return_value=task1)
    task2.copy = Mock(return_value=task2)

# Generated at 2022-06-13 08:08:52.535564
# Unit test for method copy of class Block
def test_Block_copy():
    c = Block()
    with pytest.raises(AttributeError):
        c.copy()

# Generated at 2022-06-13 08:08:53.805883
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    block.copy()


# Generated at 2022-06-13 08:08:59.598806
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible import constants as C
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role_path import RolePath
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.play_context import PlayContext

    # Create the tasks
    tags = ['tag1', 'tag2']
    tags2 = ['tag1', 'tag3']

    task1 = Task()
    task1.action = 'debug'
    task1.tags = tags

    task2 = Task()
    task2.action = 'debug'
    task2.tags = tags

    task3 = Task()

# Generated at 2022-06-13 08:09:35.966810
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    b = Block()
    parent_block = Block()
    parent_block._parent = None
    b._parent = parent_block
    assert b.get_first_parent_include() is None
    parent_block = Block()
    parent_block._parent = Task()
    b._parent = parent_block
    assert b.get_first_parent_include() is None
    parent_block = Block()
    parent_block._parent = TaskInclude()
    b._parent = parent_block
    assert b.get_first_parent_include() is parent_block._parent
    parent_block = Block()
    parent_block._parent = TaskInclude()
    b._parent = parent_block
    assert b.get