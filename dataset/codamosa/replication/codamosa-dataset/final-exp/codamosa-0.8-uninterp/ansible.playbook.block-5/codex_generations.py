

# Generated at 2022-06-13 08:00:16.612397
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import pytest

    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsV2
    from ansible.vars.hostvars import HostVarsV1
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    c = PlayContext()
    v = VariableManager()

# Generated at 2022-06-13 08:00:18.403455
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    assert block.deserialize(dict())
    assert isinstance(block, Block)

# Generated at 2022-06-13 08:00:26.444777
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:00:37.369493
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Values used to test deserialize of Block
    test_dict = {'dep_chain': None, 'name': 'Test', 'always': [], 'loop': '', 'loop_args': {}, 'block': [], 'free_form': None, 'tags': [], 'rescue': [], 'register': '', 'when': '', 'failed_when': '', 'until': '', 'retries': '', 'delay': '', 'with_items': '', 'loop_with_items': '', 'role': {'_role_name': 'Test'}}
    # Setup Block object
    test_object = Block()
    # Call deserialize method
    test_return = test_object.deserialize(test_dict)
    # Return result
    return test_return


# Generated at 2022-06-13 08:00:42.796853
# Unit test for method is_block of class Block
def test_Block_is_block():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.task import Task
    from ansible.utils.sentinel import Sentinel

    # test cases:
    # 1. test_is_block1
    #  input: input_ds = dict(block=[Sentinel.blank('global-variable')])
    #  expect: expect_result = True
    # 2. test_is_block2
    #  input: input_ds = dict(block=[Sentinel.blank('missing-task')])
    # 

# Generated at 2022-06-13 08:00:51.874505
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    f = tempfile.NamedTemporaryFile(delete=False)
    file_name = f.name

# Generated at 2022-06-13 08:00:53.730412
# Unit test for method is_block of class Block
def test_Block_is_block():
    assert Block.is_block({"block": [{"include_tasks": "test.yaml"}]})


# Generated at 2022-06-13 08:01:01.009666
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    my_block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    my_task = Task()
    my_task._attributes['name'] = 'My Task'
    my_task._attributes['tags'] = ['my_tag']
    my_task._attributes['action'] = 'command'
    my_block.block = [my_task]
    my_block._play = Play()
    my_block._play._attributes['tags'] = []
    my_block._play._attributes['skip_tags'] = []

    #test no tags
    my_block._play._

# Generated at 2022-06-13 08:01:02.610093
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Init Block object class
    b = Block()
    # Call test method
    b.filter_tagged_tasks()

# Generated at 2022-06-13 08:01:09.701888
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print("\n==== test_Block_filter_tagged_tasks ====")
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    b = Block(play=Play.load({'name': 'test'}))
    # TODO: investigate what this should be?
    #self.assertEqual(b.get_vars(), {})


# Generated at 2022-06-13 08:01:29.889755
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Initializing 'b_' with some value
    b_ = Block()
    # Initializing 'all_vars' with some value
    all_vars = dict()
    filter_tagged_tasks_ret_value = b_.filter_tagged_tasks(all_vars)

if __name__ == '__main__':
    # Creating an object 'b_obj' of class Block
    b_obj = Block()
    # Testing method 'has_tasks' of class Block
    b_obj.has_tasks()
    # Testing method 'get_include_params' of class Block
    b_obj.get_include_params()
    # Testing method 'all_parents_static' of class Block
    b_obj.all_parents_static()
    # Testing method 'get_first_parent_include' of class

# Generated at 2022-06-13 08:01:30.624497
# Unit test for method set_loader of class Block
def test_Block_set_loader():
      pass

# Generated at 2022-06-13 08:01:36.232579
# Unit test for method copy of class Block
def test_Block_copy():
    host = "localhost"
    connection = "local"
    name = "Ansible"
    task_vars = dict()
    play_context = dict()
    loader = None
    variable_manager = variable_manager.VariableManager()

    block = Block("localhost", "local", variable_manager=variable_manager)

    pb = dict()
    pb['name'] = name
    pb['host'] = host
    pb['connection'] = connection

    test_block = Block(pb, variable_manager, loader)
    test_copy_block = test_block.copy()
    assert test_copy_block.name == name
    assert test_copy_block.host == host
    assert test_copy_block.connection == connection
    assert test_copy_block.parent == None

# Generated at 2022-06-13 08:01:41.964509
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    b = Block(
        task_include=None,
        use_handlers=False,
        implicit=False,
        rescue=None,
        always=None,
        block=[
            {
                'action': 'include'
            },
            {
                'action': 'debug'
            },
            {
                'action': 'meta'
            },
            {
                'action': 'include'
            }
        ],
    )

# Generated at 2022-06-13 08:01:43.932397
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    block_obj = Block()
    assert block_obj.all_parents_static() == True


# Generated at 2022-06-13 08:01:49.210048
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = dict()
    data['role'] = dict()
    data['role']['id'] = "7e849f40-e7c0-480e-8f3c-6f2309a9e9e9"
    data['role']['name'] = "hello-world"
    data['dep_chain'] = ["7e849f40-e7c0-480e-8f3c-6f2309a9e9e9"]
    block.deserialize(data)


# Generated at 2022-06-13 08:01:52.187392
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.play_context import PlayContext
    c = PlayContext()
    block_obj = Block(play=c)
    assert isinstance(block_obj.all_parents_static(), bool)


# Generated at 2022-06-13 08:02:02.652155
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    # SCENARIO 1: A task is inside a task include
    # The method returns the task include
    t1 = Task()
    i1 = TaskInclude()
    t1._parent = i1
    t2 = t1.get_first_parent_include()
    assert(isinstance(t2, TaskInclude))
    # SCENARIO 2: A block is inside a task include
    # The method returns the task include
    b1 = Block()
    t3 = Task()
    i2 = TaskInclude()
    t3._parent = i2
    b1._parent = t3
    b2 = b1.get_first_parent_

# Generated at 2022-06-13 08:02:04.977977
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    unit test for Block.filter_tagged_tasks()
    '''

    task = Task()
    task.tags = ['test_tag']
    block = Block(block=[task])
    vars = VariableManager(([], []))
    block.filter_tagged_tasks(vars)


# Generated at 2022-06-13 08:02:11.304374
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():

    # create test object
    block_obj_1 = Block()
    block_obj_2 = Block()
    block_obj_1._parent = block_obj_2
    # test method
    assert block_obj_1.all_parents_static() == True
    # test that it returns false when parent is not statically loaded
    block_obj_2.statically_loaded = False
    assert block_obj_1.all_parents_static() == False

# Generated at 2022-06-13 08:02:26.756666
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass


# Generated at 2022-06-13 08:02:39.267548
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # pylint: disable=E0602
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """

# Generated at 2022-06-13 08:02:52.416495
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    play_instance = Play()
    task_instance = TaskInclude()

    test_obj = Block(loader=None, play=play_instance, parent_block=task_instance)
    assert test_obj.get_dep_chain() is None

    test_obj = Block(loader=None, play=play_instance, parent_block=task_instance, dep_chain=[])
    assert test_obj.get_dep_chain() == []

    test_obj = Block(loader=None, play=play_instance, parent_block=task_instance, dep_chain=[1,2,3,4,5])
    assert test_obj.get_dep_chain() == [1, 2, 3, 4, 5]



# Generated at 2022-06-13 08:02:53.273461
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(block=[])
    assert(block.has_tasks()==False)

# Generated at 2022-06-13 08:02:58.907746
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # create a block
    my_block = Block(role=None, use_handlers=False)
    assert repr(my_block) == '<Block>'

    # serialize it and deserialize it
    my_block_dict = my_block.serialize()
    my_block.deserialize(my_block_dict)

    # verify deserialize
    assert repr(my_block) == '<Block>'


# Generated at 2022-06-13 08:03:01.647496
# Unit test for method is_block of class Block
def test_Block_is_block():
    data = dict()
    data['block'] = 'block'
    data['rescue'] = 'rescue'
    data['always'] = 'always'
    assert Block.is_block(data)

# Generated at 2022-06-13 08:03:11.419612
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook import Play


# Generated at 2022-06-13 08:03:20.555439
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task_include_result import TaskIncludeResult
    from ansible.vars.manager import VariableManager
    from ansible.vars.cleaner import TaskVarsCleaner

    # 注意如果用例的变量覆盖了全局变量，那么在测试用例中，全局变量值被覆盖了
    # 所以可以在注册全局变量前测试用例
    #

# Generated at 2022-06-13 08:03:26.037902
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:03:41.029853
# Unit test for method copy of class Block

# Generated at 2022-06-13 08:03:59.309184
# Unit test for method copy of class Block
def test_Block_copy():
   # from ansible.playbook.block import Block
   # block = Block()

   # assert block.copy() == "s"

   # assert block.copy() == "s"
   pass

# Generated at 2022-06-13 08:04:08.878490
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    hosts = { "localhost": { "connection": "local" }, "other": { "connection": "local" } }
    all_vars = { "env": "prod" }
    loader = DataLoader()
    task_vars = {}

# Generated at 2022-06-13 08:04:23.299961
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    host = dict(
        type='ansible',
        extra_args='',
        host='localhost',
        port=0,
        password='pass',
        user='user'
    )

# Generated at 2022-06-13 08:04:28.298843
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    # Create an instance of class Block without actually calling its constructor
    block_obj = Block()

    # Create a mock "obj" for the deserialize function
    mock_obj = MagicMock()
    mock_obj.__class__ = AnsibleMock
    mock_obj.__class__.__name__ = "AnsibleMock"
    
    # Call the deserialize method of class Block on the mock_obj
    block_obj.deserialize(mock_obj)
    


# Generated at 2022-06-13 08:04:29.460210
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    b = Block()
    print("ok")

# Generated at 2022-06-13 08:04:39.607687
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    import ansible.constants as C
    import ansible.inventory.manager
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role
    # initialize inventory
    inventory = ansible.inventory.manager.InventoryManager(loader=None, sources=C.DEFAULT_HOST_LIST)
    # initialize variable_manager
    variable_manager = ansible.variable_manager.VariableManager(loader=None, inventory=inventory)
    # create play with role
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            roles = [
                dict(role='test_role')
                ]

        )

# Generated at 2022-06-13 08:04:48.049431
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():

    # Declare test class
    block = Block()

    # Check if Block.is_block is working
    assert Block.is_block(dict()) == False

    # Check if Block.is_block is working
    assert Block.is_block(dict(block=[1,2,3])) == True
    assert Block.is_block(dict(rescue=[1,2,3])) == True
    assert Block.is_block(dict(always=[1,2,3])) == True

    # Check if class Block is working
    assert block.preprocess_data(dict()) == dict()

    # Check if class Block is working
    assert block.preprocess_data(dict(block=[1,2,3])) == dict(block=[1,2,3])

    # Check if class Block is working
    assert block.preprocess_data

# Generated at 2022-06-13 08:04:53.955566
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test 1:
    # Setup:
    #   Load some datastructure with an implicit block, with a task and
    #   an action_include into a Block object
    # Expect:
    #   _load_data() of the Block object does not raise an exception.
    # Action:
    #   Call _load_data()
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 08:05:05.761523
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    A = Block()
    assert not A.has_tasks()
    B = Block(block=[])
    assert not B.has_tasks()
    C1 = Block(block=[Task(), Task(), Task()])
    assert C1.has_tasks()
    C2 = Block(block=[Task(), Task(), Task()],
               rescue=[Task(), Task(), Task()],
               always=[Task(), Task(), Task()])
    assert C2.has_tasks()
    D = Block(rescue=[Task(), Task(), Task()])
    assert D.has_tasks()


# Generated at 2022-06-13 08:05:12.734844
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = dict(block=[])
    b = Block()
    b.deserialize(data)
    assert b._attributes['block'] == []

# Generated at 2022-06-13 08:05:37.429295
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    b = Block(dep_chain=['a', 'b'], rescue=['a', 'b'], always=['a', 'b'], block=['a', 'b'], task_include=None, role=None, use_handlers=True, parent_block=None, play=None, implicit=True, always_run=True, any_errors_fatal=True, fail_on_undefined_vars=True, vars=None, register=None, ignore_errors=True)
    with pytest.raises(AnsibleParserError):
        b.filter_tagged_tasks(all_vars={'a': 'b'})

# Generated at 2022-06-13 08:05:41.589450
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block()
    b.deserialize({'ignore_errors': True, 'when': 'red', 'any_errors_fatal': False, 'always': '{{always}}', 'rescue': '{{rescue}}'})
    assert b.ignore_errors == True
    assert b.when == 'red'
    assert b.any_errors_fatal == False
    assert b.always == '{{always}}'
    assert b.rescue == '{{rescue}}'


# Generated at 2022-06-13 08:05:56.461367
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    args = dict(
        block=None,
        always=None,
        rescue=None,
        delegate_to='localhost',
        any_errors_fatal=False,
        failed_when=False,
        ignore_errors=False,
        register=None,
        run_once=None,
        when=None,
        until=None,
        retries='-1',
        delay='3',
        first_available_file='/etc/ansible/hosts',
        _parent=None,
        _role=None,
        _dep_chain=None,
        _use_handlers=False,
        _loader=None,
        _variable_manager=None,
        _play=None,
        _ds=None,
        _task_include=None,
    )

    b = Block(**args)

# Generated at 2022-06-13 08:06:05.740364
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    block._attributes["key1"] = "value1"
    block._attributes["key2"] = "value2"
    block._attributes["key3"] = "value3"
    assert hasattr(block,'_attributes')
    new_block = block.copy(exclude_parent=False,exclude_tasks=False)
    assert hasattr(new_block,'_attributes')
    for k,v in new_block._attributes.items():
        assert k in block._attributes.keys()
        assert v == block._attributes[k]

# Generated at 2022-06-13 08:06:11.256638
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    block.rescue = [1, 2, 3]
    block.always = [1, 2, 3]

    assert block.has_tasks() == True

    block = Block()
    block.block = [1, 2, 3]
    block.always = [1, 2, 3]

    assert block.has_tasks() == True

    block = Block()
    block.block = [1, 2, 3]
    block.rescue = [1, 2, 3]

    assert block.has_tasks() == True

    block = Block()

    assert block.has_tasks() == False

    block = Block()
    block.block = [1, 2, 3]

    assert block.has_tasks() == True

    block = Block()

# Generated at 2022-06-13 08:06:14.113849
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Initialize class object
    block = Block()
    # Call method to be tested
    block.filter_tagged_tasks()


# Generated at 2022-06-13 08:06:22.839589
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:06:32.743592
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    class Task:
        def __init__(self, action, implicit, tags, action_meta, action_include, evaluate_tags):
            self.action = action
            self.implicit = implicit
            self.tags = tags
            self.action_meta = action_meta
            self.action_include = action_include
            self.evaluate_tags = evaluate_tags
            self.tags = ['alpha']
    task_1 = Task('action', True, ['alpha'], True, False, True)
    task_2 = Task('action', True, ['alpha'], True, False, False)
    self.assertEqual(block.filter_tagged_tasks(),)

# Generated at 2022-06-13 08:06:37.424677
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    print('Testing filter_tagged_tasks method of class Block...')
    b = Block()
    l = [1, 2, 3, 4]
    b.block = l
    l2 = b.filter_tagged_tasks('all_tag')
    print('l2: ', l2)
    print('l: ', l)
    if l == l2:
        print('test_filter_tagged_tasks: PASS\n')
    else:
        print('test_filter_tagged_tasks: FAIL\n')



# Generated at 2022-06-13 08:06:47.793392
# Unit test for method copy of class Block
def test_Block_copy():
    import six
    from ansible.playbook.base import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.taggable import Taggable
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.vars import Variable

# Generated at 2022-06-13 08:07:13.621510
# Unit test for method copy of class Block
def test_Block_copy():
    t = Block()
    assert t.copy() == t
    assert t.copy() is not t
    assert t.copy()._parent is None
    assert t.copy()._role is None
    assert t.copy(exlcude_parent=False) is not t
    assert t.copy(exlcude_parent=False)._parent is None
    assert t.copy(exlcude_parent=False)._role is None
    assert t.copy(exlcude_parent=False, exclude_tasks=False) is not t
    assert t.copy(exlcude_parent=False, exclude_tasks=False)._parent is not None
    assert t.copy(exlcude_parent=False, exclude_tasks=False)._role is None

# Generated at 2022-06-13 08:07:21.515904
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    '''
    Test to verfiy the all_parents_static method of class Block
    '''
    # create fake tqa, tqb, tqc, tqd and tqe
    tqa = Task()
    tqb = Task()
    tqc = Task()
    tqd = Task()
    tqe = Task()

    # create fake tia, tib, tic and tid
    tia = TaskInclude()
    tib = TaskInclude()
    tic = TaskInclude()
    tid = TaskInclude()

    # create block ba, bb, bc and bd
    ba = Block()
    bb = Block()
    bc = Block()
    bd = Block()

    # set the parent of tqa as ba
    tqa._parent = ba
    # set

# Generated at 2022-06-13 08:07:27.765092
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:07:36.599161
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    pb = Playbook()
    pkg_data_loader.pkg_data_loader.load_inventory_file = lambda x: Inventory(loader=None, variable_manager=VariableManager()).load_from_file(x)
    p = TaskInclude()
    t = Task()
    b = Block()
    b2 = Block()
    b.block = [t]
    t._parent = b
    b2.block = [b]
    b._parent = b2
    p._parent = b2
    p.statically_loaded = False
    assert not b.all_parents_static()
    assert not b2.all_parents_static()
    assert not t.all_parents_static()
    assert p.all_parents_static()

    pb._entries.append(b2)
    pb._ent

# Generated at 2022-06-13 08:07:39.461885
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block(use_handlers=True, task_include=None)
    b.rescue = [1, 2, 3]
    b.block = [4, 5, 6]
    b.always = [7, 8, 9]
    b.other = 'other'
    b.serialize()


# Generated at 2022-06-13 08:07:46.930564
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    assert Block.load({'block': []}).has_tasks() is False
    assert Block.load({'block': []}, use_handlers=True).has_tasks() is False
    assert Block.load({'block': []}).has_tasks() is False
    assert Block.load({'block': ['do something']}).has_tasks() is True
    assert Block.load({'block': ['do something']}, use_handlers=True).has_tasks() is True
    assert Block.load({'block': ['do something'], 'rescue': ['do rescue']}).has_tasks() is True
    assert Block.load({'block': ['do something'], 'rescue': ['do rescue']}, use_handlers=True).has_tasks() is True

# Generated at 2022-06-13 08:07:53.058554
# Unit test for method copy of class Block
def test_Block_copy():
    target = {
        'name': 'Block',
        'members': [
            'block'
            'rescue'
            'always'
        ],
        'methods': [
            'get_child_blocks'
            'get_dep_chain'
            'copy'
            'serialize'
            'deserialize'
            'set_loader'
            '_get_parent_attribute'
            'filter_tagged_tasks'
            'has_tasks'
            'get_include_params'
            'all_parents_static'
            'get_first_parent_include'
        ]
    }

    b = Block()
    for element in target['members']:
        assert hasattr(b, element)

    for element in target['methods']:
        assert hasattr(b, element)


# Generated at 2022-06-13 08:08:07.601558
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.inventory import Inventory

    from ansible.playbook import Play

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Task

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    play_context = PlayContext()

# Generated at 2022-06-13 08:08:13.341542
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:08:18.288979
# Unit test for method deserialize of class Block
def test_Block_deserialize():
	try:
		# test deserialize failure
		Block().deserialize()
	except Exception as e:
		assert type(e) == AnsibleAssertionError

# Generated at 2022-06-13 08:08:46.464665
# Unit test for method copy of class Block
def test_Block_copy():
    Block(block=True, rescue=True, always=True)

# Generated at 2022-06-13 08:08:54.557555
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Initialise MockDataLoader class and its variables
    loader = MockDataLoader()
    loader._loader_plugins = dict()
    test_dir = '~/.ansible/test_dir'
    loader._basedir = test_dir
    loader.set_basedir(test_dir)

    # Initialise MockVariableManager class and its variables
    variable_manager = MockVariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._extra_vars = dict()

    # Initialise Block class and its variables
    block = Block()
    block._play = Play()
    block._use_handlers = False

    dep_chain = []
    variable_manager._fact_cache['hostname'] = 'test_hostname'
    variable_manager._extra_vars['hostname'] = 'test_hostname'

   

# Generated at 2022-06-13 08:09:01.289370
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Setup test data structures
    test_block_1 = {
        'block': [
            {'debug': 'msg="is parent static"'}
        ],
        'rescue': None,
        'always': None,
    }

    test_block_2 = {
        'block': test_block_1['block'],
        'rescue': None,
        'always': None,
    }

    test_block_3 = {
        'block': test_block_1['block'],
        'rescue': None,
        'always': None,
    }

    test_block_4 = {
        'block': test_block_1['block'],
        'rescue': None,
        'always': None,
    }


# Generated at 2022-06-13 08:09:07.295980
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.block import Block
    test_obj = Block()
    # test with empty dep_chain
    assert test_obj.get_dep_chain() == None
    
    # test with dep_chain is not None
    test_obj._dep_chain = [1,2,3]
    assert test_obj.get_dep_chain() == [1,2,3]
    

# Generated at 2022-06-13 08:09:14.687296
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader=DataLoader()

    tasks=['collectd','collectd.conf']
    # case single task test.
    b = Block(loader=loader,tasks=tasks)
    assert b.has_tasks() == True

    # case multiple tasks test.
    t = Task(loader=loader,name='collectd')
    t.action='setup'
    t1 = Task(loader=loader,name='collectd.conf')
    t1.action='copy'
    
    tasks=[t,t1]
    b = Block(loader=loader,tasks=tasks)


# Generated at 2022-06-13 08:09:24.797551
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    import copy
    # create block1
    block1 = Block(play=None, task_include=None, variable_manager=None, loader=None)
    block1.block = "block"
    block1.rescue = "rescue"
    block1.always = "always"
    block1.loop = "loop"
    block1.vars = {}
    block1.dep_chain = ['dep_chain']
    block1._role = 'role'
    block1.ignore_errors = 'ignore_errors'
    block1.any_errors_fatal = 'any_errors_fatal'
    block1.notify

# Generated at 2022-06-13 08:09:34.091348
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='/etc/ansible/hosts')