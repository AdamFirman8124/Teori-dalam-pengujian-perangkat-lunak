

# Generated at 2022-06-13 08:00:49.503771
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = '''{}'''
    # This test should raise an exception as the 'role' attribute is missing.
    try:
        Block.deserialize(data)
    except AnsibleParserError as exc:
        assert exc.message == "the field 'role' is missing from the task"


# Generated at 2022-06-13 08:00:57.879575
# Unit test for method is_block of class Block
def test_Block_is_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import action_loader
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar
    from ansible.utils.sentinel import Sentinel

    # blocks can be dictionaries, but must have a 'block', 'rescue', or
    # '

# Generated at 2022-06-13 08:01:06.090612
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for method filter_tagged_tasks of class Block
    '''
    fake_data = dict()
    fake_data['play'] = dict()
    fake_data['play']['some_key'] = fake_data['play']['some_value']
    fake_data['play']['only_tags'] = ['test_task']
    fake_data['play']['skip_tags'] = []
    fake_data['block'] = [{'action': 'some_action'}]
    fake_data['block'].append({'action': 'some_action', 'tags': ['test_task']})
    fake_data['rescue'] = [{'action': 'some_action'}]

# Generated at 2022-06-13 08:01:06.784398
# Unit test for method copy of class Block
def test_Block_copy():
    pass

# Generated at 2022-06-13 08:01:09.411190
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    data = { 'test' : 'test' }
    block = Block.load(data)
    return block.preprocess_data(data) == { 'block' : [{ 'test' : 'test' }] }


# Generated at 2022-06-13 08:01:11.011753
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    '''
    Unit test for method preprocess_data of class Block
    '''
    pass

# Generated at 2022-06-13 08:01:21.027262
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    import ansible.playbook.block
    import ansible.playbook.task
    import ansible.playbook.role
    block = Block(task = 'foo')
    block.deserialize(block.serialize())
    assert block.task == 'foo'
    assert isinstance(block.block[0], ansible.playbook.task.Task)
    assert isinstance(block.parent, ansible.playbook.role.Role)
    assert block.parent_type == 'Role'
    assert block.dep_chain == ['role_name']
    assert block._loader == None


# Generated at 2022-06-13 08:01:23.949769
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    block = Block()
    assert( not Block.is_block(["a task"]) )
    assert( Block.is_block({"a task": ""}) )
    assert( Block.is_block({"block": "NA"}) )


# Generated at 2022-06-13 08:01:27.928904
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    org_block=Block()
    dep_chain=["dep_chain_01","dep_chain_02","dep_chain_03"]
    org_block._dep_chain = dep_chain
    new_block = org_block.get_dep_chain()
    assert new_block==dep_chain[:]


# Generated at 2022-06-13 08:01:33.786045
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Create an include
    task_include1 = TaskInclude()
    # Task include should have all_parents_static true by default
    assert task_include1.all_parents_static() == True
    # Create another include
    task_include2 = TaskInclude()
    # Use a block with a parent to make sure that it is skipped
    task_include2.set_loader(DictDataLoader({}))
    task_include2.load(dict(tasks=[]))
    task_include1.set_loader(DictDataLoader({}))
    task_include1.load(dict(tasks=[task_include2]))
    # Set the parent of task_include2 to be task_include1
    task_include2._parent = task_include1
    # Since task_include1 is not statically loaded and it is a parent

# Generated at 2022-06-13 08:02:11.060071
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    b=Block()
    assert Block.is_block([])==False
    assert b.preprocess_data([]) == {'block': []}

    assert Block.is_block({})==False
    assert b.preprocess_data({}) == {'block': []}

    assert Block.is_block({'block':[], 'rescue':[]})==True
    assert b.preprocess_data({'block':[], 'rescue':[]}) == {'block': [], 'rescue': []}

    #This should test the case of a simple task given, which should be wrapped into a block
    assert Block.is_block("ls")==False
    assert b.preprocess_data("ls") == {'block': ['ls']}
    assert Block.is_block(['ls'])==False
    assert b.preprocess_

# Generated at 2022-06-13 08:02:16.648632
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert block.has_tasks() == False
    block.block = [
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task()
    ]
    assert block.has_tasks() == True
    block.rescue = [
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task(),
        Task()
    ]
    assert block.has_tasks() == True

# Generated at 2022-06-13 08:02:22.507955
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    import ansible.parsing.dataloader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.playbook.play import Play
    from ansible.utils.path import unfrackpath
    from ansible.utils.vars import combine_vars
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:02:37.524446
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    class TestBlock(Block):
        def __init__(self):
            super(test_Block_filter_tagged_tasks, self).__init__()
            self.block = ['_task1', '_task2']
            self.rescue = ['_task3', '_task4']
            self.always = ['_task5', '_task6']

    # Test for when play.only_tags is empty
    class TestPlay(Base):
        def __init__(self):
            super(test_Block_filter_tagged_tasks, self).__init__()
            self.only_tags = ['tag1', 'tag2', 'tag3']
            self.skip_tags = ['']


# Generated at 2022-06-13 08:02:46.888544
# Unit test for method is_block of class Block
def test_Block_is_block():
    data = {'block':[{'name':'test'},{'name':'test2'}],
            'rescue':None}
    assert Block.is_block(data) == True
    data = {'block':[{'name':'test'},{'name':'test2'}],
            'rescue':None,
            'always':None}
    assert Block.is_block(data) == True
    data = {'name':'test2'}
    assert Block.is_block(data) == False


# Generated at 2022-06-13 08:02:48.900175
# Unit test for method copy of class Block
def test_Block_copy():
    copy = Block.copy()
    assert copy == True

# Generated at 2022-06-13 08:02:55.001083
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Test for Block.deserialize method
    block = Block()
    block.deserialize({
        'dep_chain': None,
        'parent': None,
        'name': None,
        'loop': None,
        'loop_control': None,
        'when': None,
        'changed_when': None,
        'failed_when': None,
        'always_run': False})
    assert block



# Generated at 2022-06-13 08:03:00.051638
# Unit test for method is_block of class Block
def test_Block_is_block():
    ds1 = {"block": [{"action": {"__ansible_module__": "ping"}}]}
    ds2 = {"rescue": [{"action": {"__ansible_module__": "ping"}}]}
    ds3 = {"always": [{"action": {"__ansible_module__": "ping"}}]}
    ds4 = {"action": {"__ansible_module__": "ping"}}
    ds5 = [{"action": {"__ansible_module__": "ping"}}]

    assert Block.is_block(ds1) is True
    assert Block.is_block(ds2) is True
    assert Block.is_block(ds3) is True
    assert Block.is_block(ds4) is False
    assert Block.is_block(ds5) is False

# Generated at 2022-06-13 08:03:02.007806
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    Block_obj = Block()
    assert Block_obj.get_first_parent_include() == None
    

# Generated at 2022-06-13 08:03:06.350851
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    my_block = Block(
        implicit=False,
        block=[{'rescue': [{'ansible.builtin.debug': {'msg': 'rescue'}}]}, {'always': [{'ansible.builtin.debug': {'msg': 'always'}}]}]
    )
    assert my_block.has_tasks()

# Generated at 2022-06-13 08:03:31.991252
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    import os
    import sys
    import json

    class ResultCallback(CallbackBase):
        def v2_runner_on_ok(self, result, **kwargs):
            host = result._host
            print(json.dumps({host.name: result._result}, indent=4))

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['../../production'])
    context = PlayContext()

# Generated at 2022-06-13 08:03:42.661589
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    tmp_all_vars = dict(hostvars=dict(host1=dict(ansible_connection='test')))
    tmp_play_context = PlayContext()
    tmp_play = Play().load(dict(
        hosts=['host1'],
        gather_facts='no',
        tasks=[
            dict(
                include='some_include',
                some_var='some_value',
            ),
        ]
    ), variable_manager=VariableManager(), loader=Mailbox())

    tmp_task_include = TaskInclude().load(
        dict(
            include='seconcluded_include',
            when='True',
        ),
        play=tmp_play,
    )

    tmp_task_include._parent = tmp_task_include
    tmp_task_include._final_done = False
    tmp_task_include

# Generated at 2022-06-13 08:03:44.031011
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    test_Block_instance = Block()
    # test_Block_instance.get_first_parent_include()


# Generated at 2022-06-13 08:03:46.515306
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.base import Base
    from ansible.playbook.task_include import TaskInclude
    b = Block()
    TaskInclude.set_loader(b)


# Generated at 2022-06-13 08:04:01.507954
# Unit test for method copy of class Block
def test_Block_copy():
    import ansible.playbook.block
    import ansible.playbook.task

    # Test with parameters: exclude_parent=False, exclude_tasks=False
    block_instance = ansible.playbook.block.Block()
    block_instance.block = [ansible.playbook.task.Task()]
    block_instance.rescue = [ansible.playbook.task.Task()]
    block_instance.always = [ansible.playbook.task.Task()]
    result = block_instance.copy()
    assert isinstance(result, ansible.playbook.block.Block)

    # Test with parameters: exclude_parent=True, exclude_tasks=False
    block_instance = ansible.playbook.block.Block()
    block_instance.block = [ansible.playbook.task.Task()]


# Generated at 2022-06-13 08:04:08.632959
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    global loader, play, block
    if block is None:
        play = Play().load({'hosts': 'hosts', 'tasks': [{'name': 'a', 'local_action': 'debug'}, {'name': 'b', 'local_action': 'debug'}]})
        loader = DataLoader()
        play.set_loader(loader)
        block = play.compile()

    block.set_loader(loader)
    assert block._loader == loader
    assert block.block[0]._loader == loader
    assert block.block[1]._loader == loader


# Generated at 2022-06-13 08:04:23.148402
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:04:24.355748
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    print(block.copy())



# Generated at 2022-06-13 08:04:27.013958
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Test when data is an empty dict()
    # assertEqual(first, second, msg=None)
    # Test when data is not an empty dict()
    # assertEqual(first, second, msg=None)
    pass

# Generated at 2022-06-13 08:04:27.559618
# Unit test for method copy of class Block
def test_Block_copy():
    pass

# Generated at 2022-06-13 08:04:52.906674
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    # block -> block -> block
    play_context = PlayContext()
    play_source = dict(name="Test Play", hosts=['all'], gather_facts='no', tasks=[])
    p = Play().load(play_source, play_context, variable_manager=None, loader=None)
    block1 = Block(play=p)
    block2 = Block(parent_block=block1)
    block3 = Block(parent_block=block2)
    assert block3.all_parents_static()

    # block -> block -> TaskInclude -> block
    play_context = PlayContext()

# Generated at 2022-06-13 08:05:08.232944
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook import Role

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

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
                    cur

# Generated at 2022-06-13 08:05:10.742840
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    block.set_loader('none')


# Generated at 2022-06-13 08:05:20.801160
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.block import Block

# Generated at 2022-06-13 08:05:21.478949
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass

# Generated at 2022-06-13 08:05:27.689993
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.base import Base
    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    B = Block
    T = Task
    H = Handler
    R = Role
    I = RoleInclude
    HostVars = Base.get_config
    Playbook = Play.load
    RoleDefinition = Role

# Generated at 2022-06-13 08:05:37.006177
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    hosts = set(['localhost', 'otherhost'])
    play = Play().load(dict(
        name="Ansible Play",
        hosts=list(hosts),
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args=dict())),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    ))
    block = play.get_blocks()[0]
    block.deserialize(block.serialize())
    assert block._loader is None
    assert block._play is play
    assert block._task_include is None
    assert block._use_handlers is False
    assert block._dep_chain == []
    assert block._variable_manager is None
    assert block._parent is None

# Generated at 2022-06-13 08:05:43.206168
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

# Generated at 2022-06-13 08:05:49.400384
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
  from ansible.parsing.dataloader import DataLoader
  from ansible.vars import VariableManager

  b = Block()
  # We don't need to check the returned value, the test is to check if
  # the method gets called
  b.get_dep_chain()


# Generated at 2022-06-13 08:05:59.966070
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    my_block = Block(block=[], rescue=[], always=[])
    assert my_block.has_tasks() == False
    my_block = Block(block = [1,2,3], rescue=[], always=[])
    assert my_block.has_tasks() == True
    my_block = Block(block = [], rescue=[1,2,3], always=[])
    assert my_block.has_tasks() == True
    my_block = Block(block = [], rescue=[], always=[1,2,3])
    assert my_block.has_tasks() == True



# Generated at 2022-06-13 08:06:24.922484
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:06:36.564027
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print("\nBegin AnsibleTestCase: _test_Block_filter_tagged_tasks")

    class AnsiblePlaybookTestPlay(object):

        def __init__(self):
            self.inventory = None
            self.vars = dict()
            self.only_tags = []
            self.skip_tags = []

            self._variable_manager = None

        def __getattr__(self, item):
            if item not in self.vars and item.startswith('vars'):
                return {}
            else:
                return self.vars.get(item, {})

    class AnsiblePlaybookTestInventory(object):

        def __init__(self):
            self.vars = dict()


# Generated at 2022-06-13 08:06:41.523144
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    task_include = TaskInclude()
    task_include.statically_loaded = False
    task_include.all_parents_static()
    handler_task_include = HandlerTaskInclude()
    handler_task_include.statically_loaded = False
    handler_task_include.all_parents_static()

# Test case for class Block

# Generated at 2022-06-13 08:06:52.408208
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook.task import Task
    from ansible.module_utils._text import to_bytes

    # Instantiate Task object
    Task_object = Task()

    # Instantiate Block object
    Block_object = Block()

    # Instantiate loader object
    loader = DataLoader()
    # Check the return type of method 'set_loader'
    # of class Block on object Block_object
    if isinstance(Block_object.set_loader(loader), None.__class__):
        print('Test Successfully !!!')
    else:
        print('Test Failure !!!')

    # Check the return type of method 'set_loader'
    # of class Block on object Task_object
    if isinstance(Task_object.set_loader(loader), None.__class__):
        print('Test Successfully !!!')
   

# Generated at 2022-06-13 08:07:00.291691
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    deserialized = block.deserialize({'block': [], 'rescue': [], 'always': [], 'when': '{{ foo }}', 'dep_chain': None, 'role': 'test'})
    assert(deserialized.block == [])
    assert(deserialized.rescue == [])
    assert(deserialized.always == [])
    assert(deserialized.when == '{{ foo }}')
    assert(deserialized._dep_chain == None)
    assert(deserialized._role.get_name() == 'test')

# Generated at 2022-06-13 08:07:04.795757
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    # Create test object
    obj = Task()

    # Create test data
    data = {}

    # Execute method deserialize
    obj.deserialize(data)

    # Evaluate test results
    assert True

# Generated at 2022-06-13 08:07:19.062032
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    block1 = Block()
    assert not block1.has_tasks()

    block2 = Block()
    block2.block = [ Task(action='shell', args='echo hello world') ]
    assert block2.has_tasks()

    block3 = Block()
    block3.rescue = [ Task(action='shell', args='echo hello world') ]
    assert block3.has_tasks()

    block4 = Block()
    block4.always = [ Task(action='shell', args='echo hello world') ]
    assert block4.has_tasks()

    block5 = Block()

# Generated at 2022-06-13 08:07:19.689010
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:07:22.007438
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    data = { 'block':'block' }
    block = Block.load(data=data, play=None, role=None, variable_manager=None, loader=None)
    assert block._dep_chain == None

# Generated at 2022-06-13 08:07:29.534113
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    debug = 0
    results = []
    # BEGIN_PARSE
    #

    # test1

# Generated at 2022-06-13 08:08:05.039096
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    one = '''
    - hosts: localhost
      tasks:
        - ping:
            data: pong
        - debug:
            msg: 1
    '''
    two = '''
    - hosts: localhost
      tasks:
        - ping:
            data: pong
        - debug:
            msg: 1
    rescue:
        - debug:
            msg: 2
    '''
    three = '''
    - hosts: localhost
      tasks:
        - ping:
            data: pong
        - debug:
            msg: 1
    always:
        - debug:
            msg: 2
    '''

# Generated at 2022-06-13 08:08:07.527949
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # since the method will return None, so there is no need for test case
    pass

# Generated at 2022-06-13 08:08:08.854409
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    test_obj = Block()
    test_obj.deserialize(None)


# Generated at 2022-06-13 08:08:23.888022
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:08:24.674446
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    pass


# Generated at 2022-06-13 08:08:26.927361
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(block=[])
    assert block.has_tasks() == len(block.block) > 0 or len(block.rescue) > 0 or len(block.always) > 0


# Generated at 2022-06-13 08:08:37.838906
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    def mock_get_variables(self, loader, path):
        if path == 'block_tags_test.yml':
            return {'only_tag': 'tag1'}
        else:
            return {}

    def mock_load_file(self, path):
        if path.endswith('block_tags_test.yml'):
            with open(path, 'rb') as f:
                return f.read().strip()

# Generated at 2022-06-13 08:08:45.712476
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # Create a sample block
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=not Block.is_block(data))

    # Check the dep_chain attribute before calling method get_dep_chain
    assert b._dep_chain == None

    # Call method get_dep_chain
    assert b.get_dep_chain() == None

    # Set a dep_chain for the block
    dep_chain = []
    b._dep_chain = dep_chain

    # Call method get_dep_chain again
    assert b.get_dep_chain() == dep_chain



# Generated at 2022-06-13 08:08:53.913637
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.conditional import Conditional
    # block.parent points to a static TaskInclude object
    block = Block()
    task_include = TaskInclude()
    block._parent = task_include
    assert block.all_parents_static() == False
    # block.parent points to a static Conditional object, which points to a static TaskInclude object
    block = Block()
    task_include = TaskInclude()
    conditional = Conditional()
    conditional._parent = task_include
    block._parent = conditional
    assert block.all_parents_static() == False
    # block.parent points to a static Conditional object,
    # which points to a static Conditional object,
    # which points

# Generated at 2022-06-13 08:08:54.967188
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # Block.get_dep_chain(self)
    pass


# Generated at 2022-06-13 08:09:15.647915
# Unit test for method copy of class Block
def test_Block_copy():
	pass

# Generated at 2022-06-13 08:09:22.270337
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Create source Block() obj to be copied
    parent = Block()
    parent._parent = 'Block() Parent'
    parent.block = ['Block']

    # Create copy of parent
    block = Block()
    block = block.copy()

    # Assign values to newly created Block() obj
    block._parent = parent._parent
    block.statically_loaded = True

    assert block.filter_tagged_tasks(all_vars) == block

# Generated at 2022-06-13 08:09:28.426593
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Setup
    tf = Task()
    tf.action = 'fail'
    bf = Block(block=[tf])
    b = Block(block=[tf, bf])
    all_vars = dict(tags=[])
    # Act
    actual = b.filter_tagged_tasks(all_vars)
    # Verify
    assert actual.block == []
    assert actual.rescue == []
    assert actual.always == []
    # Cleanup - done automatically