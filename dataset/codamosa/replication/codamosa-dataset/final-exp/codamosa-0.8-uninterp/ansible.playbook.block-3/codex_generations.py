

# Generated at 2022-06-13 07:59:46.575704
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 07:59:47.161255
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    pass

# Generated at 2022-06-13 07:59:48.533171
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    block.set_loader('loader')
    assert block._loader == 'loader'


# Generated at 2022-06-13 07:59:57.003144
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager

    host = 'localhost'
    connection = 'local'
    play_context = PlayContext(remote_addr=host, connection=connection)

    main_block = Block()
    main_block._parent = None

    task1 = Task()
    task1._parent = main_block
    task2 = TaskInclude()
    task2._parent = main_block
    task2._parent._parent = main_block

    main_block

# Generated at 2022-06-13 08:00:06.114931
# Unit test for method get_dep_chain of class Block

# Generated at 2022-06-13 08:00:16.969657
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # initialize a Block object
    b = Block()
    b._role = "job1"
    b.block = "job2"
    # create a Task and a TaskInclude object
    t = Task()
    ti = TaskInclude()
    # test the method all_parents_static with the _parent being a Block or a Task/TaskInclude object
    assert b.all_parents_static() == True
    assert t.all_parents_static() == True
    assert ti.all_parents_static() == True
    b._parent = t
    assert b.all_parents_static() == True
    b._parent = ti
    assert b.all_parents_static() == True
    # initialize a Block object with a statically_loaded value
    b2 = Block()
    b2.statically_loaded = False
    b2._

# Generated at 2022-06-13 08:00:21.133199
# Unit test for method serialize of class Block
def test_Block_serialize():
    test_block = Block()
    test_serialized_data = test_block.serialize()

    assert isinstance(test_serialized_data, dict)
    assert test_serialized_data == dict(
        rescue=[],
        block=[],
        always=[],
        dep_chain=None,
    )


# Generated at 2022-06-13 08:00:23.896443
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    b = Block()
    data = b.preprocess_data(dict(block=[dict(action='A'), dict(action='B')]))
    assert data == dict(block=[dict(action='A'), dict(action='B')])



# Generated at 2022-06-13 08:00:25.239143
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    block = Block()
    assert block.statically_loaded is True


# Generated at 2022-06-13 08:00:29.254884
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task_include import TaskInclude

    # No test needed, deserialize is a noop for this class, it only gets called in
    # its parent's deserialize
    pass

# Generated at 2022-06-13 08:01:46.058891
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.mod_args import ModuleArgsParser
    inventory = InventoryManager(loader=DataLoader(), sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()

# Generated at 2022-06-13 08:01:53.681279
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    Unit test for method filter_tagged_tasks of class Block
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory('/root/ansible/test/units/lib/ansible_test/inventory_sample')
    play_context = PlayContext()
    play = Play()
    play_context.network_os = 'ios'

# Generated at 2022-06-13 08:01:59.461602
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    t = TaskInclude()

# Generated at 2022-06-13 08:02:10.960509
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook import Play
    from ansible.template import Templar

    play = Play()
    templar = Templar(loader=None, variables={})
    data = {
        'tasks': [
            {'block': [{'block': [{'debug': 'msg=1'}, {'debug': 'msg=2'}]}, {'debug': 'msg=3'}]},
            {'block': [{'debug': 'msg=4'}, {'debug': 'msg=5'}]},
            {'block': [{'block': [{'debug': 'msg=6'}, {'debug': 'msg=7'}]}, {'debug': 'msg=8'}]}
        ],
        'hosts': 'test',
    }

# Generated at 2022-06-13 08:02:16.547423
# Unit test for method deserialize of class Block

# Generated at 2022-06-13 08:02:22.032408
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block
    # Create test object
    b = Block.load(dict(
            block = [
                dict(
                    action = 'include',
                    args = dict(
                        tasks = '{{ molo_scripts_dir }}/tasks/main.yml',
                        vars = dict(
                            molo_webserver_ssl_certificate = '{{ molo_webserver_ssl_certificate }}',
                            molo_webserver_ssl_certificate_key = '{{ molo_webserver_ssl_certificate_key }}',
                        ),
                    )
                )
            ]
        )
    )

    # Test method get_dep_chain

# Generated at 2022-06-13 08:02:23.558416
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    assert Block().has_tasks()==False

# Generated at 2022-06-13 08:02:38.005648
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    global C
    C = ComparisonModule()

    class FakePlay(object):
        def __init__(self, only_tags, skip_tags):
            self.only_tags = only_tags
            self.skip_tags = skip_tags

    class FakeTask(Task):
        def __init__(self, action, tags, name, implicit=False):
            super(FakeTask, self).__init__()
            self._attributes['action'] = action
            self._attributes['tags'] = tags
            self.name = name
            self.implicit = implicit

    class FakeRole(Role):
        def __init__(self):
            super(FakeRole, self).__init__()

        def _load_role_data(self, ds):
            pass


# Generated at 2022-06-13 08:02:40.047336
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    test_all_parents_static(Block())



# Generated at 2022-06-13 08:02:53.173409
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    import json

    # Empty block

# Generated at 2022-06-13 08:03:08.988160
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass

# Generated at 2022-06-13 08:03:19.359802
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # create a block and add it to the list of blocks
    first_block = Block(implicit=True)
    first_block._attributes['name'] = '/etc/ansible/roles'
    # create an empty block
    second_block = Block(implicit=True)
    # create a task and add it to the list of tasks of the empty block
    task_1 = Task()
    task_1._attributes['name'] = 'TASK - 1'
    second_block.block.append(task_1)
    # add the empty block to the list of blocks of the first block
    first_block.block.append(second_block)

    # result should be True
    # because all parents (only 1) of the empty block are static
    assert second_block.all_parents_static() == True

    # result should

# Generated at 2022-06-13 08:03:24.168537
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    myblock = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=True)
    myblock_has_tasks = myblock.has_tasks()
    # Assert False, by default when init, the block has no tasks
    assert myblock_has_tasks == False


# Generated at 2022-06-13 08:03:27.524653
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    o = Block()
    o.deserialize({})
    assert o


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 08:03:42.861292
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Create a task and block with the same name
    test_task = Task()
    test_task._name = 'test_task_name'
    test_block = Block()
    test_block._name = 'test_task_name'

    # Create a task include with a static parent block and assign name
    test_task_include1 = TaskInclude()
    test_task_include1.statically_loaded = True
    test_task_include1._name = 'test_task_include1'

    # Create a task include with a static parent task include and assign name
    test_task_include2 = TaskInclude()
    test_task_include2.statically_loaded = True
    test_task_include2._name = 'test_task_include2'

    # Create a task include with a non static parent task include, then assign

# Generated at 2022-06-13 08:03:49.118989
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # test with an invalid parent_type
    b = Block()
    data = {
        "dep_chain": None,
        "role": None,
        "parent": None,
        "parent_type": "ThisClassDoesNotExist",
    }
    with pytest.raises(AnsibleParserError) as execinfo:
        b.deserialize(data)
    assert "unsupported parent type: ThisClassDoesNotExist" in str(execinfo.value)

    # test valid parent_type
    b = Block()
    data = {
        "dep_chain": None,
        "role": None,
        "parent": None,
        "parent_type": "Block",
    }
    with pytest.raises(AnsibleParserError) as execinfo:
        b.deserialize(data)


# Generated at 2022-06-13 08:04:00.617106
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # 1) Test Block filter_tagged_tasks with implicit=True
    # 2) Test Block filter_tagged_tasks with implicit=False, only_tags=[task_a]
    # 3) Test Block filter_tagged_tasks with implicit=False, skip_tags=[task_a]
    # 4) Test Block filter_tagged_tasks with implicit=False, only_tags=[task_b], skip_tags=[task_a]
    # 5) Test Block filter_tagged_tasks with implicit=False, only_tags=[task_a, task_b], skip_tags=[task_b]
    # 6) Test Block filter_tagged_tasks with implicit=False, only_tags=[task_b]

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

# Generated at 2022-06-13 08:04:09.507855
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block(parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    # Testing if an exception is raise when deserialize is called with wrong parameter types
    # TypeError expected
    
    # Wrong type for role
    
    data1 = dict(
        role = Block
    )
    # Testing if an exception is raise when deserialize is called with wrong parameter types
    # TypeError expected
    
    # Wrong type for parent
    
    data2 = dict(
        parent = Block
    )
    # Testing if an exception is raise when deserialize is called with wrong parameter types
    # TypeError expected
    
    # Wrong type for parent_type
    
    data3 = dict(
        parent_type = Block
    )
    # Testing if an exception is raise when

# Generated at 2022-06-13 08:04:15.303279
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude
    b = Block()
    r = Block()
    r._parent = b
    p = TaskInclude()
    p._parent = r
    a = Block()
    a._parent = p
    assert a.get_first_parent_include() is p

# Generated at 2022-06-13 08:04:17.026471
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass


# Generated at 2022-06-13 08:04:43.954139
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = ansible.parsing.dataloader.DataLoader().load_from_file("ansible/playbooks/block_test.yml").get_single_data()
    linput = ansible.playbook.play.Play().load(block, variable_manager=ansible.vars.VariableManager(), loader=ansible.parsing.dataloader.DataLoader())
    ansible.playbook.play.Play().load(block, variable_manager=ansible.vars.VariableManager(), loader=ansible.parsing.dataloader.DataLoader())
    
    test_chain = []
    for k in linput.keys():
        if k.startswith("test_"):
            test_chain.append(k)

# Generated at 2022-06-13 08:04:45.905735
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    r = b.copy()
    assert r._attributes == {'always': None, 'block': None, 'rescue': None}


# Generated at 2022-06-13 08:04:52.324077
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Create a block object
    b = Block(
        block = [
            Task(
                name = 'bar',
                tags = [
                    'foo',
                    'bam',
                ],
            ),
            Task(
                name = 'bar',
                tags = [
                    'foo',
                    'bam',
                ],
            ),
        ],
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Create a block object

# Generated at 2022-06-13 08:05:03.367887
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    b1 = Block()
    b1.block = [Task()]
    b2 = Block()
    b2.block = [b1]
    b3 = Block()
    b3.block = [b2]
    b3.filter_tagged_tasks(PlayContext(tags=[])).serialize()
    return b3.filter_tagged_tasks(PlayContext(tags=[]))



# Generated at 2022-06-13 08:05:13.765066
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    def test_target(target):
        tmp_list = []
        for task in target:
            if isinstance(task, Block):
                filtered_block = evaluate_block(task)
                if filtered_block.has_tasks():
                    tmp_list.append(filtered_block)
            elif ((task.action in C._ACTION_META and task.implicit) or
                    (task.action in C._ACTION_INCLUDE and task.evaluate_tags([], play.skip_tags, all_vars=all_vars)) or
                    task.evaluate_tags(play.only_tags, play.skip_tags, all_vars=all_vars)):
                tmp_list.append(task)
        return tmp_list

    # filter_tagged_tasks(self, all_vars):
    play

# Generated at 2022-06-13 08:05:23.288798
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block=Block()

# Generated at 2022-06-13 08:05:33.270608
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Ensure that we are getting deep copies of a basic block
    '''
    b = Block.load(dict(block=[dict(t1='t1')]), None, None, 'test_role_copy', None, False, None, None)
    b2 = b.copy()

    assert b != b2
    assert b.block[0].serialize() == b2.block[0].serialize()
    assert id(b.block) != id(b2.block)
    assert id(b.block[0]) != id(b2.block[0])
    assert id(b.block[0]._parent) != id(b2.block[0]._parent)
    assert id(b.block[0]._parent._parent) != id(b2.block[0]._parent._parent)

# Unit

# Generated at 2022-06-13 08:05:40.786877
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    hostvars = dict(
        loop1=[1, 2],
        loop2=[3, 4],
        var1=1,
        var2=2,
        )

# Generated at 2022-06-13 08:05:41.854340
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    assert Block().all_parents_static()

# Generated at 2022-06-13 08:05:56.784466
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test Data for the unit test
    data = dict(
        block=dict(
            block=dict(
                block=dict(
                    block=dict(
                        block=dict(
                            block=dict(block=[dict(action='action')]),
                            rescue=[dict(action='action')],
                            always=[dict(action='action')]),
                        rescue=[dict(action='action')],
                        always=[dict(action='action')]),
                    rescue=[dict(action='action')],
                    always=[dict(action='action')]),
                rescue=[dict(action='action')],
                always=[dict(action='action')]),
            rescue=[dict(action='action')],
            always=[dict(action='action')]),
        rescue=[dict(action='action')],
        always=[dict(action='action')]
    )
   

# Generated at 2022-06-13 08:06:40.419672
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    b.block = [1, 2, 3, 4, 5]
    b.rescue = [5, 4, 3, 2, 1]
    b.always = [6, 7, 8, 9, 0]
    assert b.block == b.copy().block
    assert b.rescue == b.copy().rescue
    assert b.always == b.copy().always
    assert b.block == b.copy(exclude_tasks=True).block
    assert b.rescue == b.copy(exclude_tasks=True).rescue
    assert b.always == b.copy(exclude_tasks=True).always
    b2 = Block()
    b2.block = [6, 7, 8, 9, 0]
    b.copy_data(b2)
    assert b.block

# Generated at 2022-06-13 08:06:51.509399
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    b = Block(loader=loader, role=None, task_include=None)

    # Add a new task (self.block)
    b.block = [Task() for x in range(2)]
    b.rescue = [Task() for x in range(2)]
    b.always = [Task() for x in range(2)]

    # Set the loader
    loader = DataLoader()
    b.set_loader(loader)

    # Parent block
    parent_block = Block(loader=loader, role=None, task_include=None)

    # Set the parent of each task
    for i in range(2):
        b.block[i]._parent = parent_block


# Generated at 2022-06-13 08:06:52.755394
# Unit test for method copy of class Block
def test_Block_copy():
    """Test for copying the class Block"""
    pass

# Generated at 2022-06-13 08:06:54.778152
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    block = Block()
    assert block.all_parents_static() == True

# Generated at 2022-06-13 08:07:03.588629
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    block.block = [dict(action=dict(module='debug', args=dict(msg='This is a test')))]
    assert block.has_tasks() == True

    block.block = [dict(action=dict(module='debug', args=dict(msg='This is a test'))),
                   dict(action=dict(module='debug', args=dict(msg='This is a another test')))]
    assert block.has_tasks() == True

    block.rescue = [dict(action=dict(module='debug', args=dict(msg='This is a test')))]
    assert block.has_tasks() == True

    block.always = [dict(action=dict(module='debug', args=dict(msg='This is a test')))]

# Generated at 2022-06-13 08:07:17.775777
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block (
        use_handlers = "use_handlers",
        name = "name",
        rescue = "rescue",
        loop = "loop",
        play = "play",
        role = "role",
        tags = "tags",
        implicit = "implicit",
        register = "register",
        variables = "variables",
        vars_prompt = "vars_prompt",
        until = "until",
        when = "when",
        always = "always",
        block = "block",
        task_include = "task_include",
        parent_block = "parent_block",
        variable_manager = "variable_manager",
        loader = "loader",
        static_include = "static_include"
    )
    b.get_dep_chain()


# Generated at 2022-06-13 08:07:25.002610
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    no_tasks_block = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=not Block.is_block(1))
    block_has_tasks = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=not Block.is_block([1]))
    assert no_tasks_block.has_tasks() == False
    assert block_has_tasks.has_tasks() == True
if __name__ == "__main__":
    test_Block_has_tasks()


# Generated at 2022-06-13 08:07:34.484085
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader, cache_loader, callback_loader, connection_loader, lookup_loader, module_loader, strategy_loader, test_loader, vars_loader, filter_loader

    # Create a test inventory
    dummy_loader = DataLoader()

# Generated at 2022-06-13 08:07:37.196590
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  data = dict(name=u'ApiGateway',
              rescue=[],
              always=[u'Notify Ansible'],
              block=[u'Configure Instance', u'Create Instance'])

  obj = Block()
  obj.deserialize(data)
  assert obj.__dict__ == data

# Generated at 2022-06-13 08:07:42.089581
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.template import Templar

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 08:08:24.378839
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  from ansible.playbook.block import Block
  from ansible.playbook.handler_task_include import HandlerTaskInclude
  from ansible.playbook.task_include import TaskInclude
  block = Block()
  data = dict(task1="test1", task2="test2")
  block.deserialize(data)
  assert data == block._attributes
  return

# Generated at 2022-06-13 08:08:33.366729
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    '''
    unit tests to check the proper setting of the Block _loader property
    '''
    
    t = Task()
    b = Block()
    loader = DataLoader()
    b.set_loader(loader)
    assert b._loader == loader, '_loader property did not get set!'
    
    b._parent = t
    b.set_loader(loader)
    assert b._parent._loader == loader, 'loader in the parent task did not get set!'
    
    dep_chain = [t, t, t]
    b._parent = t
    b._dep_chain = dep_chain
    b.set_loader(loader)
    for dep in dep_chain:
        assert dep._loader == loader, 'loader in the dependancy chain did not get set!'
    
    r = Role()

# Generated at 2022-06-13 08:08:40.882028
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.base import Base
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 08:08:44.475347
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    #from ansible.playbook.task_include import TaskInclude
    #from ansible.playbook.role_include import IncludeRole
    #def __init__(self, task):
    #B = Block(task=TaskInclude(None))
    assert True == False

# Generated at 2022-06-13 08:08:52.872808
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    class Mock_Play():
        def __init__(self):
            self.only_tags = ["test"]
            self.skip_tags = []
    
    class Mock_Parent():
        def __init__(self):
            pass

    class Mock_Role():
        def __init__(self):
            self.share = "share"

    class Mock_Task():
        def __init__(self, action, tags, _parent, implicit):
            self.action = action
            self.tags = tags
            self.implicit = implicit
            self._parent = _parent

    class Mock_Block(Block):
        def __init__(self, *_, **__):
            super(Mock_Block, self).__init__()
            self.block = []

        def copy(self, *_, **__):
            return Mock

# Generated at 2022-06-13 08:09:00.215553
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    import sys
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.callback import CallbackBase
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import callback_loader, module_loader

   

# Generated at 2022-06-13 08:09:04.108785
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize(dict(value='foo', key='bar'))
    assert block._attributes['key'] == 'bar'
    assert block._attributes['value'] == 'foo'



# Generated at 2022-06-13 08:09:13.349573
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:09:14.856549
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    with pytest.raises(TypeError):
        Block().get_first_parent_include()

# Generated at 2022-06-13 08:09:24.797946
# Unit test for method filter_tagged_tasks of class Block