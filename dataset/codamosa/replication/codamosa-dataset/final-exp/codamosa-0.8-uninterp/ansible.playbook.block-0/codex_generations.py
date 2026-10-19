

# Generated at 2022-06-13 08:00:14.024878
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Test 1
    p = Play()
    r = Role()
    r.statically_loaded = True
    b = Block(play=p, role=r)
    assert b.all_parents_static() == True
    # Test 2
    p = Play()
    r = Role()
    r.statically_loaded = False
    b = Block(play=p, role=r)
    assert b.all_parents_static() == False
    # Test 3
    p = Play()
    r = Role()
    r.statically_loaded = False
    b = Block(play=p, role=r)
    r1 = Role()
    r1.statically_loaded = True
    b1 = Block(play=p, role=r1)
    b.parent = b1
    assert b.all_parents_

# Generated at 2022-06-13 08:00:15.779104
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    b.set_loader("loader")



# Generated at 2022-06-13 08:00:17.012576
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass
# unit tests for Block

# Generated at 2022-06-13 08:00:18.025991
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    block = Block()
    assert block.all_parents_static() == True
    
    

# Generated at 2022-06-13 08:00:26.156379
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    block = Block(use_handlers=False)
    block.name = 'Task-1'
    block.block = []
    block.block.append(Task())
    block.block[0].name = "Task-1.1"
    block.block[0].action = 'debug'
    block.block[0].register = 'output'
    block.block[0].args = {'msg': 'Running Task-1.1'}
    block.block.append(Task())
    block.block[1].only_if = "'success' in output.stdout"
    block.block[1].name

# Generated at 2022-06-13 08:00:37.638983
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    p = Play().load(dict(
        name="test play",
        hosts=["testhost"],
        gather_facts="no"
    ), variable_manager=VariableManager(), loader=DataLoader())
    h = Host("testhost")
    t1 = Task().load(dict(action='debug', msg="foo"), play=p)
    t2 = Task().load(dict(action='debug', msg="bar"), play=p)
    t3 = Task().load(dict(action='debug', when="false", msg="baz"), play=p)
    block1 = Block().load(dict(block=[t1, t3]), task_include=None, play=p)

# Generated at 2022-06-13 08:00:42.688681
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    parent = Sentinel
    block = Block(play=Sentinel, parent_block=parent, role=Sentinel, task_include=None, use_handlers=False, implicit=True)
    assert block.has_tasks() == False


# Generated at 2022-06-13 08:00:44.197693
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    assert b.get_dep_chain() is None


# Generated at 2022-06-13 08:00:53.239702
# Unit test for method preprocess_data of class Block

# Generated at 2022-06-13 08:00:54.090631
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass


# Generated at 2022-06-13 08:01:10.885615
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # create a block
    b = Block()
    # method filter_tagged_tasks of b is expected to return a block
    assert(isinstance(b.filter_tagged_tasks([]), Block))


# Generated at 2022-06-13 08:01:22.726158
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:01:31.320203
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()


# Generated at 2022-06-13 08:01:36.617462
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    task1 = AnsibleModule()
    task1.only_tags = ['tag']
    task=[task1]
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False)
    b.block=task
    b._play = AnsiblePlay()
    b._play.only_tags = ['tag']
    b._play.skip_tags = None

    block = b.filter_tagged_tasks('all_vars')
    assert block is not None


# Generated at 2022-06-13 08:01:45.764041
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    b = Block(play=None)
    task1 = Task()
    task1.name = 'task1'
    task1.tags = ['a', 'b']
    task1._include = TaskInclude()
    task1._include.tags = ['c', 'd']
    task2 = Task()
    task2.name = 'task2'
    task2.tags = ['c', 'd']
    task2._include = TaskInclude()
    task2._include.tags = ['a', 'b']
    b.block = [task1, task2]

# Generated at 2022-06-13 08:01:53.343298
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    my_params = dict()
    my_tqm = dict()
    my_variable_manager = dict()

    my_play = Play().load(dict(
        name = "Ansible Play",
        hosts = "all",
        gather_facts = "no",
        tasks = list(),
    ), loader=my_loader, variable_manager=my_variable_manager)
    my_block = Block(
        play=my_play,
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        implicit=False,
    )

    my_block.set_loader(my_loader)

    assert my_block._loader == my_loader
    assert my_block._play._loader == my_loader
    assert my_block._parent._loader == my_

# Generated at 2022-06-13 08:02:04.816078
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Setup
    def evaluate_block(block):
        new_block = block.copy(exclude_parent=True, exclude_tasks=True)
        new_block._parent = block._parent
        new_block.block = evaluate_and_append_task(block.block)
        new_block.rescue = evaluate_and_append_task(block.rescue)
        new_block.always = evaluate_and_append_task(block.always)
        return new_block
    def evaluate_and_append_task(target):
        tmp_list = []
        for task in target:
            if isinstance(task, Block):
                filtered_block = evaluate_block(task)
                if filtered_block.has_tasks():
                    tmp_list.append(filtered_block)

# Generated at 2022-06-13 08:02:06.765390
# Unit test for method is_block of class Block
def test_Block_is_block():
    assert Block.is_block({'block': ['a', 'b']}) == True

# Generated at 2022-06-13 08:02:16.121729
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.playbook_include import PlaybookInclude 
    from ansible.playbook.handler_task_include import HandlerTaskInclude 
    from ansible.playbook.role import Role 
    from ansible.playbook.task import Task 
    pb = PlaybookInclude()
    pb._attributes['vars_files'] = 'var_files'
    pb._attributes['vars'] = 'vars'
    pb._attributes['roles'] = 'roles'
    pb._attributes['tasks'] = 'tasks'
    pb._attributes['handlers'] = 'handlers'
    ht_i = HandlerTaskInclude()
    ht_i._attributes['vars'] = 'Vars'

# Generated at 2022-06-13 08:02:18.146936
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    assert isinstance(block, Block)
    loader = DictDataLoader({})
    block.set_loader(loader)
    assert isinstance(block, Block)


# Generated at 2022-06-13 08:02:40.752653
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:02:43.412227
# Unit test for method copy of class Block
def test_Block_copy():
    b_obj = Block()
    result = b_obj.copy(exclude_tasks=True)
    assert result == "NA"

# Generated at 2022-06-13 08:02:55.135097
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    b = Block()
    assert b.all_parents_static()
    # Case with just one parent that is not static
    b._parent = TaskInclude()
    assert not b.all_parents_static()
    # Chain of 4, one of them is not static
    t1 = Task()
    t1._parent = TaskInclude()
    t2 = Task()
    t2._parent = t1
    t3 = Task()
    t3._parent = t2
    t4 = Task()
    t4._parent = t3
    t4.statically_loaded = True
    assert not t4.all_parents_static()
    # Chain of 4

# Generated at 2022-06-13 08:02:55.757200
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass

# Generated at 2022-06-13 08:03:04.244473
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print('Test Block_filter_tagged_tasks')
    play_context = dict(
            _tqm = None,
            basedir = '/root/workspaces/pyansible/scripts',
            extra_vars = dict(
                a = 1,
                b = 2,
                ),
            inventory = dict(
                _vars = dict(
                    a = 3,
                    b = 4,
                    ),
                _hosts = dict(
                    localhost = dict(
                        ansible_connection = 'local',
                        ansible_host = '127.0.0.1',
                        ansible_user = 'test',
                        ),
                    ),
                ),
            passwords = dict(
                conn_pass = dict(),
                become_pass = dict(),
                ),
            run_once = False,
            )
   

# Generated at 2022-06-13 08:03:15.296311
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    p = Play().load({
        "hosts": "all",
        "name" : "Test question",
        "tasks" : [
            dict(action=dict(module='ansible.builtin.ping'), register='ping_result'),
            dict(action=dict(module='ansible.builtin.debug', msg='Hello from role1')),
            dict(action=dict(module='ansible.builtin.debug', msg='{{ping_result.ansible_facts.discovered_interpreter_python}}', when='ping_result.ansible_facts.discovered_interpreter_python is defined'))
        ]
    }, variable_manager=VariableManager(), loader=DictDataLoader())
    tqm = TaskQueueManager(inventory=Inventory(), variable_manager=VariableManager(), loader=DictDataLoader())

    results

# Generated at 2022-06-13 08:03:16.619598
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert block.has_tasks() == False


# Generated at 2022-06-13 08:03:23.414390
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.vars.hostvars import HostVars
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.executor.task_queue_manager import TaskQueueManager

    options = lambda: None
    options.verbosity = 0
    options.no_log = True
    options.connection

# Generated at 2022-06-13 08:03:33.511291
# Unit test for method copy of class Block
def test_Block_copy():
    data = dict()
    data['block'] = ['junk']
    data['rescue'] = 'rescue'
    data['always'] = 'always'
    data['given_name'] = 'junk'
    data['name'] = 'junk'
    block = Block.load(data, play=None)
    new_block = block.copy(exclude_parent=False, exclude_tasks=False)
    assert new_block.block==['junk']
    assert new_block.rescue=='rescue'
    assert new_block.always=='always'
    assert new_block.given_name=='junk'
    assert new_block.name=='junk'
    assert new_block._dep_chain==None
    assert new_block.parent==None
    assert new_block.role==None

# Generated at 2022-06-13 08:03:46.516516
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.included_file import IncludedFile
    from ansible.executor.task_queue_manager import TaskQueueManager
    
    from ansible.vars.unsafe_proxy import UnsafeProxy
    
    from ansible import context
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    

# Generated at 2022-06-13 08:04:08.081678
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    # create the playbook objects (without a loader)
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.network_os = 'default'
    play_context.remote_addr = '127.0.0.1'
    play_context.port = 0
    play_context.remote_user = 'default'
    # create the playbook objects (without a loader)
    loader = DataLoader()

# Generated at 2022-06-13 08:04:22.192015
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    ansible_play = AnsiblePlay()

    test_block = Block(play = ansible_play)
    assert test_block.statically_loaded

    # test_block => block
    task = Task(play = ansible_play)
    block = Block(play = ansible_play)
    task.block = [block]
    test_block.block = [task]
    assert test_block.all_parents_static() == True

    # test_block => block => task
    block_1 = Block(play = ansible_play)
    task_1 = Task(play = ansible_play)
    block_1.block = [task_1]
    task.block = [block_1]
    test_block.block = [task]
    assert test_block.all_parents_static() == True

    # test

# Generated at 2022-06-13 08:04:26.463498
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    assert block.deserialize() is None

    block = Block()
    data = {'k1': 'v1', 'k2': 'v2'}
    assert block.deserialize(data) is None
    assert block._attributes == {}
    assert block._parent == None
    assert block._role == None
    assert block._dep_chain == None


# Generated at 2022-06-13 08:04:33.201561
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # TODO: mock variable manager, loader and hosts with test data
    variable_manager = mock.Mock()
    loader = mock.Mock()
    host_list = mock.Mock()
    # Create a task1
    task1 = Task()
    task1._attributes = {'tags':['conf']}
    # Create a task2
    task2 = Task()
    task2._attributes = {'tags':['conf','log']}
    # Create a task3
    task3 = Task()
    task3._attributes = {'tags':['conf','write']}
    # Create a task4
    task4 = Task()
    task4._attributes = {'tags':['conf','others']}
    # Create a task5
    task5 = Task()

# Generated at 2022-06-13 08:04:35.512614
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = dict()
    with pytest.raises(AnsibleParserError) as exec_info:
        block.deserialize(data)

# Generated at 2022-06-13 08:04:44.195111
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Create a mock loader object
    # Create a mock variable manager object
    # Create a mock display object
    # Create a mock Host object
    # Create a mock PlayContext object
    # Create a mock play object
    # Create a mock role object
    role_obj = Role()
    # Create a mock block object
    # Create an object of the Tasks class
    tasks_obj = Tasks()
    tasks_obj.statically_loaded = True
    # Create a mock task object
    task_obj = Task()
    task_obj.statically_loaded = True

    block_obj1 = Block()
    block_obj1._parent = tasks_obj
    block_obj1.statically_loaded = True
    assert block_obj1.all_parents_static() == True

    block_obj2 = Block()
    block_obj2._

# Generated at 2022-06-13 08:04:45.068255
# Unit test for method is_block of class Block

# Generated at 2022-06-13 08:04:51.565683
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.unsafe_proxy import UnsafeProxy
    task0 = Task()
    task0._parent = TaskInclude()
    task0._parent._parent = Task()
    task0._parent._parent._parent = TaskInclude()
    task0._parent._parent._parent._parent = task0._parent
    task1 = Task()
    task1._parent = TaskInclude()
    task1._parent._parent = Task()
    task1._parent._parent._parent = TaskInclude()
    task1._parent._parent._parent._parent = task1._parent
    task2 = Task()
    task2._parent = TaskInclude()

# Generated at 2022-06-13 08:05:04.304608
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    def preprocess_data(ds, is_block=True):
        if is_block:
            return ds
        elif isinstance(ds, dict) and len(ds) == 1:
            # if 'name' in ds:
            #     name = ds['name']
            # else:
            #     name = None

            if 'block' in ds:
                return dict(block=[ds['block']])
            elif 'rescue' in ds:
                return dict(rescue=[ds['rescue']])
            elif 'always' in ds:
                return dict(always=[ds['always']])

        # simplified
        return dict(block=ds)
        

# Generated at 2022-06-13 08:05:14.130305
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    print("Test method: has_tasks()")

    # Empty list task
    ds = dict(
        block = [
        ])
    b = Block.load(ds)
    assert not b.has_tasks()

    # Single list task
    ds = dict(
        block = [
            dict(action='include'),
        ])
    b = Block.load(ds)
    assert b.has_tasks()

    # Multiple list task
    ds = dict(
        block = [
            dict(action='include'),
            dict(action='include'),
        ])
    b = Block.load(ds)
    assert b.has_tasks()

    # Empty rescue task
    ds = dict(
        block = [
        ],
        rescue = [
        ])
    b = Block.load(ds)

# Generated at 2022-06-13 08:05:38.112719
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:05:43.961167
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # Instantiation of a block with a task
    block = Block(block=[dict(action=dict(module='ping', args=dict(data='pong')))])
    assert block.has_tasks() is True
    # Instantiation of a block with an empty dict
    block = Block()
    assert block.has_tasks() is False
    # Instantiation of a block with a task and an empty dict
    block = Block(block=[dict(action=dict(module='ping', args=dict(data='pong')))], rescue=[])
    assert block.has_tasks() is True
    # Instantiation of a block with an empty list
    block = Block(block=[])
    assert block.has_tasks() is False
    # Instantiation of a block with an empty list and a task

# Generated at 2022-06-13 08:05:45.974667
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # TODO
    raise NotImplementedError()

# Generated at 2022-06-13 08:06:00.025334
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print("\nEntered unit test for method test_Block_filter_tagged_tasks()")
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    import sys
    print("\nCalling Block.load()")

# Generated at 2022-06-13 08:06:04.695446
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block(play=MagicMock())

    block_copy = block.copy()

    assert isinstance(block_copy, Block)
    assert block_copy._play == block._play
    assert block_copy._use_handlers == True
    assert block_copy._dep_chain == None
    assert block_copy._parent == None
    assert block_copy.block == None
    assert block_copy.rescue == None
    assert block_copy.always == None
    assert block_copy._role == None

# Generated at 2022-06-13 08:06:10.441607
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        vars = dict(
            a = 1,
            b = 2,
            c = 3,
        ),
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='a is {{ a }}'))),
            dict(action=dict(module='debug', args=dict(msg='b is {{ b }}'))),
            dict(action=dict(module='debug', args=dict(msg='c is {{ c }}'))),
            dict(action=dict(module='debug', args=dict(msg='d is {{ d }}'))),
        ]
    )

    from ansible.playbook.play import Play
    from ansible.vars import Variable

# Generated at 2022-06-13 08:06:21.060101
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    import random
    import string

    random_tag = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print("Testing with random tag '%s'" % random_tag)
    filtered_block = Block.load({'block': [
        {'name': 'included_task', 'tags': [random_tag, 'included_tag']},
        {'name': 'excluded_task', 'tags': ['excluded_tag']},
    ]}).filter_tagged_tasks({})

    assert len(filtered_block.block) == 1
    assert filtered_block.block[0].name == 'included_task'



# Generated at 2022-06-13 08:06:31.934006
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    # test empty block
    block = Block()
    assert block.all_parents_static()
    # mock task to use
    task1 = Task()
    task1.action = 'setup'
    # test with non-static parent
    block.parent = TaskInclude()
    block.parent.statically_loaded = False
    assert block.all_parents_static() == False
    # test with non-static grandparent
    block.parent.parent = TaskInclude()
    block.parent.parent.statically_loaded = False
    assert block.all_parents_static

# Generated at 2022-06-13 08:06:32.757737
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    pass

# Generated at 2022-06-13 08:06:37.640278
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert block.has_tasks() == False
    block.block = [1, 2]
    assert block.has_tasks() == True
    block.block = []
    assert block.has_tasks() == False
    block.rescue = [3, 4]
    assert block.has_tasks() == True
    block.rescue = []
    assert block.has_tasks() == False
    block.always = [5, 6]
    assert block.has_tasks() == True
    block.always = []
    assert block.has_tasks() == False


# Generated at 2022-06-13 08:07:03.288754
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    block = Block(
        use_handlers=True,
        block=[
            TaskInclude(action='first', tags=['include', 'tasks']),
            TaskInclude(action='second', tags=['include', 'tasks']),
        ],
    )
    all_vars = dict(tags=['include'], all_tags=[])
    block.filter_tagged_tasks(all_vars) == [
        TaskInclude(action='first', tags=['include', 'tasks']),
        TaskInclude(action='second', tags=['include', 'tasks'])
    ]


# Generated at 2022-06-13 08:07:09.140949
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  import copy
  # Create an object of the class.
  obj = Block()

  # Create a mock "module" for ansible.playbook.task_include.TaskInclude
  class MockTaskInclude:
    def __init__(self, *args, **kwargs):
      pass

    def __call__(self, *args, **kwargs):
      return 'ansible.playbook.task_include.TaskInclude'

  # Create a mock for ansible.playbook.task_include.TaskInclude.
  TaskInclude = MockTaskInclude()

  # Create a mock "module" for ansible.playbook.handler_task_include.HandlerTaskInclude
  class MockHandlerTaskInclude:
    def __init__(self, *args, **kwargs):
      pass


# Generated at 2022-06-13 08:07:10.262009
# Unit test for method copy of class Block
def test_Block_copy():
    play = Play()
    block = Block(play)
    assert copy(block) == block


# Generated at 2022-06-13 08:07:15.842201
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    import json
    import os
    import sys
    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    # create a task object
    task = Task()

    # create a task_include object
    task_include = TaskInclude()

    # create a block object
    block = Block()

    # create a first task_include object
    first_task_include = TaskInclude()

    # create a second task_include object
    second_

# Generated at 2022-06-13 08:07:21.074808
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block(
        loader=DictDataLoader(
            {'playbook.yml': "", "tasks/main.yml": """\
- name: A
"""}
        ),
        variable_manager=VariableManager(),
        use_handlers=False,
    )
    block = b.load(
        data={'include': 'playbook.yml'},
    )
    try:
        block.set_loader(DictDataLoader({}))
    except AnsibleError:
        assert False
    assert True
# end unit tests

# Generated at 2022-06-13 08:07:27.408868
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.base import Base
    from ansible.playbook.helpers import load_list_of_blocks
    block=Block.load({
		"block": [
			{"get_url": {"url": "https://foo.com/bar", "dest": "/tmp/bar"}}
		]
	})
    assert block.has_tasks()==True
    block=Block.load({
		"block": [
            {"get_url": {"url": "https://foo.com/bar", "dest": "/tmp/bar"}},
            {"get_url": {"url": "https://foo.com/bar", "dest": "/tmp/bar"}}
		]
	})
    assert block.has_tasks()==True
    block

# Generated at 2022-06-13 08:07:33.775123
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Unit test for method copy of class Block
    '''
    print('Testing copy method of class Block')

    # initialize vars
    b = Block()

    # set a value for attribute 'block'
    block_forward_ref = ForwardRef('block_forward_ref')
    b.block = block_forward_ref

    # set a value for attribute 'rescue'
    rescue_forward_ref = ForwardRef('rescue_forward_ref')
    b.rescue = rescue_forward_ref

    # set a value for attribute 'always'
    always_forward_ref = ForwardRef('always_forward_ref')
    b.always = always_forward_ref

    # set a value for attribute 'when'
    b.when = 'when_value'

    # set a value for attribute 'changed_when'

# Generated at 2022-06-13 08:07:40.979361
# Unit test for method copy of class Block
def test_Block_copy():
    data = dict(
        block = [
            dict(
                module = 'foo',
                when = 1,
                register = 'bar',
                fail_when_missing = True,
                always_run = True
            ),
            dict(
                module = 'foo',
                when = 1,
                register = 'bar',
                fail_when_missing = True,
                always_run = True
            )
        ]
    )
    b = Block()
    b.load(data)

    b2 = b.copy()

    # Check that the attributes where copied correctly
    assert b.block is b2.block, 'Block.copy() has failed to copy the attribute [block] correctly.'
    assert b.always is b2.always, 'Block.copy() has failed to copy the attribute [always] correctly.'
    assert b.res

# Generated at 2022-06-13 08:07:45.580460
# Unit test for method copy of class Block
def test_Block_copy():
    # create object Block
    block_obj = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=None, implicit=None)
    assert block_obj is not None

    # test method copy

    # Invoke method
    copy_result = block_obj.copy()

    # Check the result
    assert isinstance(copy_result, Block)
    assert copy_result is not None


# Generated at 2022-06-13 08:07:53.774166
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    from mock import Mock
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.template import Templar

    b_no_tag = Block()
    b_tag_1 = Block()
    b_tag_2 = Block()
    b_tag_all = Block()
    b_tag_1_not_always = Block()

    b_no_tag.block = [Mock(tags=[], action="notify", args={}, only_if=False, notify=["test_handler"])]
    b_no_tag.rescue = [Mock(tags=[], action="notify", args={}, only_if=False, notify=["test_handler"])]

# Generated at 2022-06-13 08:08:14.338374
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    foo = Block()
    print(foo._attributes)
    try:
        foo.all_parents_static()
        print('True')
    except:
        print('False')


# Generated at 2022-06-13 08:08:27.224527
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()

    assert block.has_tasks() == False

    task1 = Task()
    task2 = Task()

    task1.block = [task2]
    block.block = [task1]

    assert block.has_tasks() == True

    block1 = Block()
    task3 = Task()
    block1.block = [task3]
    block.always = [block1]

    assert block.has_tasks() == True

    block2 = Block()
    block.always = [block2]

    assert block.has_tasks() == False

    task4 = Task()
    task5 = Task()
    block.block = [task4, task5]
    block.always = [block2]

    assert block.has_tasks() == True

    block.block = []
    block

# Generated at 2022-06-13 08:08:38.152741
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:08:46.712364
# Unit test for method copy of class Block
def test_Block_copy():
    #
    # 'playbook to_json script'
    #
    playbook_content = '''
    name:
    hosts: localhost
    tasks:
      - name: test
        shell: /bin/true
        with_items:
          - a
          - b
        register: result
      - debug: var=result
    '''
    task_content = '''
    - name: test
      shell: /bin/true
      with_items:
        - a
        - b
      register: result
    '''
    #
    # 'playbook to_json script'
    #
    pb = Playbook.load(playbook_content, variable_manager=VariableManager(), loader=DataLoader())
    task = Task.load(task_content)
    assert False == pb.copy().statically_loaded


# Generated at 2022-06-13 08:08:54.742931
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    task1 = Task()
    task1.action = 'shell'
    task1.name = 'Shell Command'
    task1.tags = ['Shell', 'Command']

    task2 = Task()
    task2.action = 'command'
    task2.name = 'Command'
    task2.tags = ['Shell', 'Command']

    task3 = Task()
    task3.action = 'command'
    task3.name = 'Command'
    task3.tags = ['Command']

    task4 = Task()
    task4.action = 'command'
    task4.name = 'Command'
    task4.tags = ['Shell', 'Command']

    task5 = Task()
    task5.action = 'command'
    task5.name = 'Command'
    task5.tags = ['Shell', 'Command']

   

# Generated at 2022-06-13 08:08:57.723571
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    if len(Block().block) != 0:
        return False
    if len(Block().rescue) != 0:
        return False
    if len(Block().always) != 0:
        return False
    return True

# Generated at 2022-06-13 08:09:02.988798
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # no dep_chain
    b1 = Block()
    assert b1.get_dep_chain() is None
    
    # dep_chain exists
    b1 = Block()
    b1._dep_chain = [1,2,3]
    assert b1.get_dep_chain() == [1,2,3]
    
    

# Generated at 2022-06-13 08:09:12.560553
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Tests method deserialize of class Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    block = Block()
    role_data = {}
    role_data['_search_paths'] = []
    role_data['_role_name'] = 'some role name'
    role_data['_vars'] = {}
    role_data['_default_vars'] = {}
    role_data['_metadata'] = {}
    role_data['_parent_role'] = None
    role_data['_role_path'] = 'some path'
    role_data['_loaded_role_names'] = []
    role_data['_dependencies'] = []
    role_data['_tasks'] = []
    role_data

# Generated at 2022-06-13 08:09:17.396116
# Unit test for method copy of class Block
def test_Block_copy():
    arguments = [{'exclude_parent': True, 'exclude_tasks': False}]
    block0 = Block()
    block1 = block0.copy(*arguments[0]['exclude_parent'], **arguments[0]['exclude_tasks'])
    assert type(block1) == Block


# Generated at 2022-06-13 08:09:20.843573
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # test set_loader
    b = Block()
    l = DataLoader()
    b.set_loader(l)
    assert(b._loader == l)
