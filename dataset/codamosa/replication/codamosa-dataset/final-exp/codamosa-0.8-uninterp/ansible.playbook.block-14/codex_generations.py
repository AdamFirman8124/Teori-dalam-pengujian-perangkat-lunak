

# Generated at 2022-06-13 08:00:14.346632
# Unit test for method copy of class Block
def test_Block_copy():
    b0 = Block()
    b1 = Block()
    b2 = Block()
    b3 = Block()
    b0._play = None
    b1._play = None
    b2._play = None
    b3._play = None
    b0._parent = b1
    b1._parent = b2
    b2._parent = b3
    b0.block = [1]
    b1.block = [2]
    b2.block = [3]
    b3.block = [4]
    b0.rescue = [11]
    b1.rescue = [22]
    b2.rescue = [33]
    b3.rescue = [44]
    b0.always = [111]
    b1.always = [222]

# Generated at 2022-06-13 08:00:17.532508
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.vars.manager import VariableManager
    b = Block()
    vm = VariableManager()
    b.filter_tagged_tasks(vm)


# Generated at 2022-06-13 08:00:25.798998
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    host = AnsibleHost("127.0.0.1", "22")
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()

    play.deserialize(
        {'name': 'test',
        'hosts': 'all',
        'connection': 'local',
        'gather_facts': True,
        'vars': {},
        'tasks': [
            {
                'name': 'setup',
                'action': {
                    '__ansible_module__': 'setup'
                }
            }
        ]})
    play._variable_manager = variable_manager
    play._variable_manager.set_inventory(Inventory(loader=loader, host_list=[host]))
    play._tqm._unreachable_hosts = dict()

# Generated at 2022-06-13 08:00:37.369324
# Unit test for method is_block of class Block

# Generated at 2022-06-13 08:00:42.774332
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:00:51.844396
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    def create_objects():
        play = Play()
        role = Role()
        block = Block(play=play, role=role)
        task = Task(block=block)
        task_include = TaskInclude(block=block)
        block2 = Block(parent=task, role=role)
        # simulate not statically loaded
        task_include.statically_loaded = False
        return play, role, block, task, task_include, block2
    def test_1(play, role, block, task, task_include, block2):
        # task -> block -> role -> play
        assert task.all_parents_static()

# Generated at 2022-06-13 08:00:53.523908
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    ''' Block().filter_tagged_tasks(all_vars) '''
    pass

# Generated at 2022-06-13 08:00:55.008092
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    tmp = block.filter_tagged_tasks()
    assert tmp is not None

# Generated at 2022-06-13 08:00:59.227566
# Unit test for method is_block of class Block
def test_Block_is_block():
    print(Block.is_block({'block': ['hello', 'world']}))
    print(Block.is_block({'rescue': ['hello', 'world']}))
    print(Block.is_block({'always': ['hello', 'world']}))
    print(Block.is_block({'hello': ['hello', 'world']}))
    print(Block.is_block(['hello', 'world']))


# Generated at 2022-06-13 08:01:00.188826
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    assert b.copy()

# Generated at 2022-06-13 08:01:45.939424
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # block = Block()
    pass


# Generated at 2022-06-13 08:01:47.336762
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    bk = Block(loader=None)
    bk.set_loader(None)

# Generated at 2022-06-13 08:01:50.197846
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    import _collect_as_dict
    _collect_as_dict.run_test(Block, 'ansible.parsing.yaml.objects.Block', func_name='deserialize',
                              args=['data'], kwargs={})


# Generated at 2022-06-13 08:01:56.744567
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize(dict(meta=dict(s='s')))
    assert type(block) == Block
    assert block._attribute_class == BlockAttribute
    assert block.block == []
    assert block.rescue == []
    assert block.always == []
    assert block.force_handlers == False
    assert block.loop == []
    assert block.name == []
    assert block.register == []
    assert block.retries == 3
    assert block.until == []
    assert block.loop_args == {}
    assert block.when == []
    assert block.vars == []
    assert block.any_errors_fatal == False
    assert block.changed_when == []
    assert block.failed_when == []
    assert block.ignore_errors == False
    assert block.delegate_

# Generated at 2022-06-13 08:02:08.249568
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Creating a role without the default attribute
    role = Role()
    role._role_path = '/root/roles/role1'
    role._name = 'role1'
    role._metadata.name = 'role1'
    role._metadata.tags = ['all']
    # Creating a play
    play = Play()
    try:
        play.load({
            'name': 'testing',
            'hosts': 'all',
            'gather_facts': True
        })
    except Exception as e:
        print(e)
    play.roles.append(role)
    play._role_names = ['role1']

# Generated at 2022-06-13 08:02:16.724778
# Unit test for method copy of class Block
def test_Block_copy():
    # Instantiate a Block
    data = {'block': [{'tasks': [{'name': 'B', 'action': 'shell',
                                  'args': {'chdir': '/home'}}]}]}
    block1 = Block(implicit=False)
    block1.load_data(data)
    
    assert isinstance(block1.block[0], Task)
    assert block1 == block1.block[0]._parent

    # Test for method copy
    block2 = block1.copy(exclude_tasks=False)
    
    assert isinstance(block2.block[0], Task)
    assert block2 == block2.block[0]._parent
    
    # Make sure that block1 == block2    
    assert block1 == block2


# Generated at 2022-06-13 08:02:22.577923
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Setup
    module_loader = DictDataLoader({'a' :dedent('''
        ---
        - hosts: 127.0.0.1
          gather_facts: no

          tasks:
            - include: a
              tags: [ one ]
    '''), 'b' :dedent('''
        ---
        - hosts: 127.0.0.1
          gather_facts: no

          tasks:
            - block:
                - include: b
                  tags: [ two ]
    '''), 'c' :dedent('''
        ---
        - hosts: 127.0.0.1
          gather_facts: no

          tasks:
            - block:
                - import_tasks: c
                  tags: [ three ]
    ''')})


# Generated at 2022-06-13 08:02:37.591722
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    print(">>")
    print("The dep_chain attribute of the Block object is a copy of the parent's dep_chain attribute.")
    print(">>")

    from ansible.playbook.block import Block

    parent = Block()
    child = Block(parent=parent)
    child.__dict__["_dep_chain"] = ["a", "b", "c"]
    parent.__dict__["_dep_chain"] = ["1", "2", "3"]
    print("parent.__dict__: ", parent.__dict__)
    print("child.__dict__: ", child.__dict__)
    print("child.get_dep_chain(): ", child.get_dep_chain())
    assert child.get_dep_chain() == ["1", "2", "3"]

    print(">>")

# Generated at 2022-06-13 08:02:39.136818
# Unit test for method is_block of class Block
def test_Block_is_block():
	pass


# Generated at 2022-06-13 08:02:40.760547
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    pass #TODO

# Generated at 2022-06-13 08:03:19.525203
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    obj = Block.load({'block': [{'action': {'arguments': [{'bar': {'baz': {'description': 'description', 'required': True}}}], 'description': 'description', 'required': True}}, {'name': {'description': 'description', 'required': True}}]})
    assert isinstance(obj.block[0], Task)
    assert isinstance(obj.block[1], Task)

# Generated at 2022-06-13 08:03:25.359970
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # Create a new instance of Block to be used for testing
    block = Block()
    # Check that the value of the property block is an empty list
    assert block.block == []
    # Check that the value of the property rescue is an empty list
    assert block.rescue == []
    # Check that the value of the property always is an empty list
    assert block.always == []
    # Assert that the method has_tasks returns a boolean value
    assert isinstance(block.has_tasks(), bool)
    # Assert that the method has_tasks returns a False value
    assert block.has_tasks() == False
    # Create a new instance of Block to be used for testing
    block = Block(block=['task1', 'task2'])
    # Assert that the method has_tasks returns a True value
    assert block

# Generated at 2022-06-13 08:03:35.443436
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    import ansible.playbook.block

    ansible.playbook.block.C = type('obj', (), {'_ACTION_META': {}, '_ACTION_INCLUDE': {}})

    # testing Block filter_tagged_tasks class value error
    block = Block(play=Play(), parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)

# Generated at 2022-06-13 08:03:39.339691
# Unit test for method set_loader of class Block

# Generated at 2022-06-13 08:03:47.301697
# Unit test for method copy of class Block
def test_Block_copy():
    # Test attribute error for a block that does not have a loader defined
    try:
        b = Block()
    except (AttributeError) as excinfo:
        assert excinfo.args[0] == "missing loader attribute"
    else:
        assert False, "exception not raised"
    pl = Play()
    b = Block(loader=DictDataLoader(), play=pl)

    # Test copying a block with no attributes
    b.copy()

    # Test copying a block with valid attributes
    b = Block(loader=DictDataLoader(), play=pl, rescue='rescue text', always='always text')
    b.copy()

    # Test copying a block with an invalid attributes
    try:
        b = Block(loader=DictDataLoader(), play=pl, invalid='invalid text')
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 08:03:48.948388
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    assert True



# Generated at 2022-06-13 08:03:53.150971
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    print("Testing Block.get_dep_chain()")
    block = Block()
    dep_chain = block.get_dep_chain()
    assert(dep_chain is None)


# Generated at 2022-06-13 08:03:57.858695
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    assert b._loader is None
    b.set_loader(None)
    assert b._loader is None
    b.set_loader('test')
    assert b._loader == 'test'


# Generated at 2022-06-13 08:04:05.196972
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Block - copy
    '''

    my_block = Block()
    my_block.block = [ 1 ]
    my_block.rescue = [ 1 ]
    my_block.always = [ 1 ]

    my_copy = my_block.copy()
    assert my_block.block == my_copy.block
    assert my_block.rescue == my_copy.rescue
    assert my_block.always == my_copy.always
# ===========================================


# Generated at 2022-06-13 08:04:08.115067
# Unit test for method copy of class Block
def test_Block_copy():
    block1 = Block()
    block2 = block1.copy()
    assert block2 is not block1

# Generated at 2022-06-13 08:05:05.615153
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    block = Block()
    assert block.get_first_parent_include() == None

# Generated at 2022-06-13 08:05:11.210583
# Unit test for method copy of class Block
def test_Block_copy():
    # Test case 1
    block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=not Block.is_block(data))
    assert block.copy(exclude_parent=False, exclude_tasks=False) == ''
    

# Generated at 2022-06-13 08:05:21.262241
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    
    # test case 1: check exception when data does not have main task block
    
    from ansible.playbook import Play
    from ansible.playbook.plays import PlayIterator
    from ansible.playbook.play import Play as Play_object
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    
    
    # mock the play object
    play_iterator = PlayIterator(None)
    play = NextPlay(None, None)
    play._iterator = play_iterator
    play._hostvars = MagicMock()
    play._hostvars.get.return_value = {}
    
    # mock the block object
    block_1 = Block(play=play)
    

# Generated at 2022-06-13 08:05:26.506512
# Unit test for method copy of class Block
def test_Block_copy():
    block1 = Block()
    block1.block = ['block']
    block1.rescue = ['rescue']
    block1.always = ['always']
    block1.dep_chain = [1, 2]
    block1._role = [3, 4]
    block2 = Block()
    block2._use_handlers = True
    block1.parent = block2
    assert block1.copy(exclude_tasks=True) == block1.copy(exclude_tasks=True)


if __name__ == '__main__':
    # Unit test for method copy of class Block
    test_Block_copy()

# Generated at 2022-06-13 08:05:36.036509
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import RoleInclude

    t1 = Task()
    t2 = Task()
    t3 = Task()
    t4 = Task()
    t5 = Task()
    t6 = Task()

    i1 = TaskInclude()
    i2 = TaskInclude()

    ri = RoleInclude()

    b1 = Block()
    b2 = Block()
    b3 = Block()
    b4 = Block()

    t1._parent = b1
    t2._parent = b1
    t3._parent = b2
    t4._parent = b2
    t5._parent = b3
   

# Generated at 2022-06-13 08:05:37.179463
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # TODO implement this unit test
    pass



# Generated at 2022-06-13 08:05:43.303978
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block()
    b.block = 'task1'
    assert b.has_tasks()
    # Test for rescue
    b.rescue = 'task2'
    assert b.has_tasks()
    # Test for always
    b.always = 'task3'
    assert b.has_tasks()
    # Test for all
    b.block = 'task4'
    assert b.has_tasks()
    # Test for none
    b.block = None
    assert not b.has_tasks()
    # Test for empty list
    b.block = []
    assert not b.has_tasks()
    # Test for empty list
    b.block = ['task1']
    assert b.has_tasks()
    # Test for empty list
    b.block = None
    b.res

# Generated at 2022-06-13 08:05:45.535011
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    my_block = Block()
    my_block.set_loader(None)

# Generated at 2022-06-13 08:05:48.228861
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block = Block()

    assert [], block.get_dep_chain()


# Generated at 2022-06-13 08:06:00.842412
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    block = Block()
    assert block.get_first_parent_include() == None
    block._parent = TaskInclude("a")
    block._parent._parent = HandlerTaskInclude("b")
    assert block.get_first_parent_include() == block._parent
# Unit test end

    def run(self, runner, task_vars=dict()):
        '''
        The run method is used by the Runner to execute a block and returns
        the results of the task.
        '''

        if self.statically_loaded:
            return (False, None)


# Generated at 2022-06-13 08:07:18.647890
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block(play=play, parent_block=parent_block, role=role, task_include=None, use_handlers=False, implicit=True)
    block.copy()



# Generated at 2022-06-13 08:07:25.295984
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.taggable import Taggable

    b = Block(implicit=True)
    b._valid_attrs = Taggable._valid_attrs

# Generated at 2022-06-13 08:07:34.918586
# Unit test for method deserialize of class Block
def test_Block_deserialize():
	b = Block()
	data = dict()
	data['serialized_data'] = "aGVsbG8="
	data['dep_chain'] = ['a','b','c']
	data['role'] = "role"
	data['parent'] = "parent"
	data['parent_type'] = 'Block'

	b.deserialize(data)
	assert b._attributes['serialized_data'] == "hello"
	assert b._dep_chain == ['a','b','c']
	assert b._role.name == "role"
	assert b._parent.name == "parent"
	assert b._parent._type == 'Block'
	b._attributes['serialized_data'] = "d29ybGQ="
	assert b.serialized_data == "world"


# Generated at 2022-06-13 08:07:41.787841
# Unit test for method copy of class Block
def test_Block_copy():
    # FIXME: doesn't hit all code paths
    from ansible.playbook.task import Task
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude

    b = Block()
    b._parent = TaskInclude()
    b._parent._parent = Task()
    b.block = [Task(), Task()]
    b.rescue = [Task(), Task()]
    b.always = [Task(), Task()]
    b.dep_chain = [TaskInclude()]
    b.dep_chain[0]._parent = HandlerTaskInclude()
    b.dep_chain[0]._parent._parent = Task()

    c = b.copy()
    assert c._parent._parent == b._parent._parent

# Generated at 2022-06-13 08:07:42.923137
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    print('NOT IMPLEMENTED')

# Generated at 2022-06-13 08:07:50.175404
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    b0 = Block()
    b1 = Block()
    b1._parent = b0
    b2 = Block()
    b2._parent = b1
    b3 = Block()
    b3._parent = b2

    t0 = TaskInclude()
    t1 = TaskInclude()
    t1._parent = t0
    t2 = TaskInclude()
    t2._parent = t1
    t3 = TaskInclude()
    t3._parent = t2

    b0._parent = t0
    b1._parent = t1
    b2._parent = t2
    b3._parent = t3

    assert t0 == b0.get_first_parent_include()
    assert t0 == b1.get_first_parent_include()
    assert t0 == b2.get_first

# Generated at 2022-06-13 08:07:52.697733
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    '''
    Block.deserialize()
    '''
    pass



# Generated at 2022-06-13 08:07:55.326622
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    Block.set_loader(loader='loader')
    assert Block.set_loader == 'loader'

# Generated at 2022-06-13 08:08:08.669362
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    p1 = Play()
    b1 = Block(play=p1)
    assert b1.all_parents_static() == True
    p2 = Play()
    t1 = TaskInclude(play=p2)
    b2 = Block(play=p2, parent=t1)
    assert b2.all_parents_static() == False
    b3 = Block(play=p2, parent=t1)
    t2 = TaskInclude(play=p2, parent=b3)
    assert t2.all_parents_static() == False
    p3 = Play()
    b4 = Block(play=p3)
    t3 = TaskInclude(play=p3, parent=b4)
    assert t3.all_parents_static

# Generated at 2022-06-13 08:08:23.693364
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    from copy import deepcopy
    from ansible.vars import VariableManager

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.get_vars(play=dict(), task_vars=dict())

    b = Block(
        loader=loader,
        variable_manager=variable_manager,
        use_handlers=False,
        task_includes=[],
        role=None,
        task_errors=None,
        default_vars=dict()
    )
    b._role = Role()
    b._role.name = "test"

    # test without TaskInclude
    b._parent = b
    assert b.get_first_parent_include() is None

    # test with TaskInclude
    ti = TaskInclude