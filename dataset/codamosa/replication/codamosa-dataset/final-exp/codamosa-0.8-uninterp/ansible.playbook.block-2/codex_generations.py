

# Generated at 2022-06-13 08:00:14.578360
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    obj = Block()
    # deserialize is a method of an instance of Block
    assert type(obj.deserialize) == MethodType


# Generated at 2022-06-13 08:00:23.969492
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    my_block = Block()
    my_task = Task()
    my_task2 = Task()
    my_task3 = Task()
    my_task.action = 'debug'
    my_task.tags = ['t1']
    my_task2.action = 'debug'
    my_task2.tags = ['t2']
    my_task3.action = 'debug'
    my_task3.tags = ['t1']
    my_block.block = [my_task, my_task2]
    my_block.rescue = [my_task3]
    my_block.filter_tagged_tasks(dict())
    assert my_block.block == [my_task]
    assert my_block

# Generated at 2022-06-13 08:00:25.275212
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block.deserialize(None)



# Generated at 2022-06-13 08:00:36.679490
# Unit test for method serialize of class Block
def test_Block_serialize():
    print("")
    print("##### Begin tests for Block - serialize #####")

    class TestBlock(Block):

        _valid_attrs = {
            'block': FieldAttribute(isa='list', default=None, include_name=True, exclude_from_print=True,
                                    serialize_when_none=False, listof=BaseTask),
        }

    # Try the serialize function with no values
    myObj = TestBlock()
    myObj._attributes = None
    print("Test 1 - serialize an empty object")
    print("Expected: {}")
    print("Actual  : {}".format(myObj.serialize()))
    print("")

    # Try the serialize function with a populated object
    myObj._attributes = {"block": [1, 2, 3]}

# Generated at 2022-06-13 08:00:38.185046
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    # add some test data
    assert b.copy()
    assert isinstance(b.copy(), Block)


# Generated at 2022-06-13 08:00:42.492991
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    loader = DictDataLoader({
        'test.yml': '',
        'test2.yml': '',
    })
    block = Block()
    block.set_loader(loader)


# Generated at 2022-06-13 08:00:47.969752
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    b = Block(play=None, role=None)
    b.block = [True]
    assert b.has_tasks()
    b.block = []
    b.rescue = [True]
    assert b.has_tasks()
    b.rescue = []
    b.always = [True]
    assert b.has_tasks()
    b.always = []



# Generated at 2022-06-13 08:00:50.439476
# Unit test for method copy of class Block
def test_Block_copy():
    b = Block()
    # copy method need parameter exclude_parent=False, exclude_tasks=False
    # But here we do not test their functionality, so use default value False
    b.copy()


# Generated at 2022-06-13 08:00:51.447484
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    pass


# Generated at 2022-06-13 08:00:59.077177
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.errors import AnsibleParserError

    class MockLoader(AnsibleLoader):
        pass

    loader = MockLoader([], variable_manager=None, loader=None)
    dumper = AnsibleDumper()
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    # Test 1
    data = AnsibleUnsafeText('name: foo')

# Generated at 2022-06-13 08:01:26.488643
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block()
    b.block = ["block0"]
    b.rescue = ["rescue0"]
    b.always = ["always0"]
    b._parent = ["parent0"]
    b._dep_chain = ["dep_chain0"]
    b._role = ["role0"]
    b._play = ["play0"]
    b._valid_attrs = ["valid_attrs0"]
    b._attributes = ["attributes0"]
    b._loader = ["loader0"]
    ans = b.get_dep_chain()
    assert ans == ["dep_chain0"], "Ans {0} should be equal to dep_chain0".format(ans)
    b._dep_chain = None
    ans = b.get_dep_chain()

# Generated at 2022-06-13 08:01:28.127835
# Unit test for method is_block of class Block
def test_Block_is_block():
    pass


# Generated at 2022-06-13 08:01:33.850089
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    block = Block(implicit=False)
    task = Block(implicit=False)
    task._parent = block
    assert task.all_parents_static() == True
    task_include = TaskInclude(task=None, role=None, loop=None)
    block2 = Block(implicit=False)
    task_include._parent = block2
    task2 = Block(implicit=False)
    task2._parent = task_include
    assert task2.all_parents_static() == False
    block3 = Block(implicit=False)
    block3.statically_loaded = False
    task3 = Block(implicit=False)
    task3._parent = block3

# Generated at 2022-06-13 08:01:35.837633
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    res = block.copy(exclude_parent=False)
    assert res is not None

# Generated at 2022-06-13 08:01:44.948890
# Unit test for method is_block of class Block
def test_Block_is_block():
    # block is dict
    block = {}
    assert (Block.is_block(block) == True), 'Block: test_Block_is_block, test_id_1'
    # block is empty list
    block = []
    assert (Block.is_block(block) == False), 'Block: test_Block_is_block, test_id_2'
    # block is list with dicts
    block = [{}]
    assert (Block.is_block(block) == True), 'Block: test_Block_is_block, test_id_3'
    # block is list of dicts
    block = [{}, {}]
    assert (Block.is_block(block) == True), 'Block: test_Block_is_block, test_id_3'
    # block is list of dicts

# Generated at 2022-06-13 08:01:51.877761
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
	block = Block()
	block.block = [
		{
			"block": [
				{
					"block": [],
					"rescue": [],
					"always": []
				}
			],
			"rescue": [],
			"always": []
		},
		{
			"block": [
				{
					"block": [],
					"rescue": [],
					"always": []
				}
			],
			"rescue": [],
			"always": []
		}
	]
	block.rescue = []
	block.always = []


# Generated at 2022-06-13 08:01:53.832030
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    # Create an instance of class Block
    block = Block()

    # Create the obj.
    obj = None

    # Call method deserialize of Block on the created instance
    block.deserialize(obj)



# Generated at 2022-06-13 08:02:04.613990
# Unit test for method has_tasks of class Block

# Generated at 2022-06-13 08:02:06.218005
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
  assert True # TODO: implement your test here


# Generated at 2022-06-13 08:02:15.746087
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    '''
    This test will check the functionality of set_loader method of class Block.
    Method will be tested with the help of following scenario and sample data:
    Scenario 1:
    Loader is set for a block which is not using any role.
    Scenario 2:
    Loader is set for a block which is using one role.
    '''
    # Scenario1:
    # Setting loader for a block which is not using any role.
    play_ds = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[dict(action=dict(module='setup', args=dict()))]
    )
    loader = DataLoader()
    play = Play().load(play_ds, variable_manager=VariableManager(), loader=loader)

# Generated at 2022-06-13 08:02:36.141731
# Unit test for method copy of class Block
def test_Block_copy():
    import ansible.playbook.task
    import ansible.playbook.block
    # object of class Task without any argument
    a = ansible.playbook.task.Task()
    # object of class Block with argument a
    b = ansible.playbook.block.Block(a)
    # call method copy
    b.copy()


# Generated at 2022-06-13 08:02:42.093920
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    test_block = Block()
    assert test_block.get_first_parent_include() == None
    my_block = Block()
    my_task = Task()
    my_task._parent = my_block
    my_task_1 = Task()
    my_task_include = TaskInclude()
    my_task_include.statically_loaded = False
    my_task_include._parent = my_task
    my_block.block = [my_task]
    my_task.block = [my_task_1]
    my_task.rescue = [my_task_include]
    assert test_block.get_first_parent_include() == None



# Generated at 2022-06-13 08:02:54.246182
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    # Input
    obj1 = Block()
    data = {}
    # Output
    obj1._attributes['always'] = obj1._attributes['rescue'] = obj1._attributes['block'] = obj1._attributes['ignore_errors'] = obj1._attributes['register'] = obj1._attributes['when'] = obj1.dep_chain = obj1._parent = obj1._role = obj1.tags = None
    # Implementation
    obj1.deserialize(data)
    # Verification
    assert(json.dumps(obj1.serialize()) == "{\"block\":null,\"rescue\":null,\"always\":null,\"when\":null,\"ignore_errors\":null,\"register\":null,\"dep_chain\":null}")
    # Cleanup


# Generated at 2022-06-13 08:03:02.772612
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    block = Block()
    assert block.has_tasks() == 0

    block.block = [Task()]
    assert block.has_tasks() == 1

    block = Block()
    block.rescue = [Task()]
    assert block.has_tasks() == 1

    block = Block()
    block.always = [Task()]
    assert block.has_

# Generated at 2022-06-13 08:03:13.123254
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude


# Generated at 2022-06-13 08:03:18.580409
# Unit test for method is_block of class Block
def test_Block_is_block():
    ds = {
        'block': [{'include': 'fake_include', 'tags': 'fake_tag'}],
        'rescue': [{'meta': 'fake_meta'}],
        'always': [{'debug': 'msg="fake_debug"'}]
    }
    expected_value = True
    value = Block.is_block(ds)
    print(expected_value)
    print(value)
    assert(value == expected_value)


# Generated at 2022-06-13 08:03:19.685405
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    b = Block()
    assert b.filter_tagged_tasks([]) == b

# Generated at 2022-06-13 08:03:20.626768
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    pass


# Generated at 2022-06-13 08:03:31.117035
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    b = Block()
    assert b.preprocess_data('a') == {'block': ['a']}
    assert b.preprocess_data(['a', 'b']) == {'block': ['a', 'b']}
    assert b.preprocess_data({'block': ['a', 'b']}) == {'block': ['a', 'b']}
    assert b.preprocess_data({}) == {}
    assert b.preprocess_data({'rescue': 'a'}) == {'rescue': ['a']}
    assert b.preprocess_data({'always': 'a'}) == {'always': ['a']}
    try:
        b.preprocess_data('unknown')
        assert False, "Expected error"
    except AnsibleError:
        pass


# Generated at 2022-06-13 08:03:37.637044
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # make sure the method filter_tagged_tasks of class Block
    # can work as expected
    block = Block()
    all_vars = {}
    assert block.filter_tagged_tasks(all_vars) is not None


if __name__ == '__main__':
    test_Block_filter_tagged_tasks()

# Generated at 2022-06-13 08:04:02.474773
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    parent = Block()
    play = Play()
    block = Block(play=play, parent_block=parent)
    data = {}
    loader = DictDataLoader({'parent': data, 'play': data, 'block': data})
    block.set_loader(loader)
    assert block._loader == loader
    assert play._loader == loader
    assert parent._loader == loader


# Generated at 2022-06-13 08:04:10.505832
# Unit test for method serialize of class Block
def test_Block_serialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    t = Templar(loader=DataLoader())

# Generated at 2022-06-13 08:04:20.993283
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    b = Block()
    assert b.all_parents_static()

    # Test case 1. One parent and it is static
    from ansible.playbook.task import Task
    t1 = Task()
    t1.set_loader(DictDataLoader({}))
    t1.register_loader_option('foo', 'bar')
    b.set_loader(DictDataLoader({}))
    b.register_loader_option('foo', 'baz')
    b._parent = t1
    assert b.all_parents_static()

    # Test case 2. One parent and it is not static, so all_parents_static is False
    t1.static_loader = False
    assert not b.all_parents_static()

    # Test case 3. Two parents, first static and second static, so all_parents_static is True

# Generated at 2022-06-13 08:04:23.548292
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    test_Block = Block()

    test_var_loader = VariableLoader()

    test_Block.set_loader(test_var_loader)


# Generated at 2022-06-13 08:04:30.092840
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:04:32.935059
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    block = Block()
    block.rescue = []
    block.always = []
    block.block = []
    return block.filter_tagged_tasks(None)

# Generated at 2022-06-13 08:04:36.619544
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    obj = Block()
    obj.set_loader(loader=None)
    obj = Block()
    obj.set_loader(loader=None)
    obj = Block()
    obj.set_loader(loader=None)
    obj = Block()
    obj.set_loader(loader=None)




# Generated at 2022-06-13 08:04:45.138711
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.attribute import Attribute
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.task.task import Task
    import numpy
    testobj = Block()
    data = {"block": "block", "fail_when": "", "when": "when", "rescue": "rescue", "any_errors_fatal": "any_errors_fatal", "always": "always", "dep_chain": "dep_chain", "role": "role", "parent": "parent", "parent_type": "Block"}

# Generated at 2022-06-13 08:04:51.606068
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    def test_data(block):
        return [task for task in block.block if hasattr(task, 'action') and task.action == 'debug' and hasattr(task, 'args') and task.args.get('msg') == 'block_msg']

    """
    - name: block_1
      debug:
        msg: block_msg
      block:
      rescue:
      always:
    """

    task = Task()
    task.action = 'debug'
    task.args = {'msg': 'block_msg'}
    block_1 = Block(task_include=task)

    assert test_data(block_1.get_dep_chain()) == [task]
    assert test_data(block_1.get_dep_chain()) == [task]


# Generated at 2022-06-13 08:04:52.768338
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    Block.deserialize()

# Generated at 2022-06-13 08:05:23.721570
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    from ansible.playbook.play_context import PlayContext

    test_args = {
        'tags': [],
        'skip_tags': [],
        'only_tags': []
    }
    # test for only_tags

    test_args['only_tags'] = [ 'tag1', 'tag2' ]
    test_args['skip_tags'] = []
    pc = PlayContext(**test_args)
    play = Play().load({}, pc, loader=DictDataLoader())


# Generated at 2022-06-13 08:05:31.426434
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    obj = Block()
    block_data = {"block": [{"debug": "msg=\"{{ foo }}\""}], "always": [{"meta": {"end_play": True}}], "rescue": []}
    obj.deserialize(block_data)
    assert obj.block[0].action == "debug"
    assert obj.block[0].args["msg"] == "{{ foo }}"
    assert obj.always[0].action == "meta"
    assert obj.always[0].args["end_play"] == True
    assert obj.rescue == []

# Generated at 2022-06-13 08:05:39.443105
# Unit test for method filter_tagged_tasks of class Block

# Generated at 2022-06-13 08:05:51.231021
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Objective:
    #   To test that task_include does not put the tag of parent of the task include
    #   when the block is being dynamically included.
    # Pre-requisites:
    #   - $ANSIBLE_CONFIG to point to a valid ansible.cfg file
    #   - Check if ansible.cfg has the 'roles_path' pointing to a valid directory
    #   - $ANSIBLE_LIBRARY to point to a valid directory
    #   - Check if the following files are present in $ANSIBLE_LIBRARY directory
    #       - test_Block_get_first_parent_include.yml
    #       - file_block_test.yml

    # Setup
    if "ANSIBLE_CONFIG" not in os.environ:
        raise Exception("ANSIBLE_CONFIG environment variable not set")

# Generated at 2022-06-13 08:05:53.594486
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    block = Block()
    chain = block.get_dep_chain()
    assert chain is None

# Generated at 2022-06-13 08:05:55.277422
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    b = Block()
    assert b.all_parents_static() == True



# Generated at 2022-06-13 08:06:05.706583
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # No blocks provided as input
    b = Block()
    assert b.filter_tagged_tasks(all_vars={})==None
    # No tasks provided in the block
    assert b.filter_tagged_tasks(all_vars={}).has_tasks()==False
    # Test all features of the Block class
    b = Block()
    # test role
    b.role={}
    assert b.role==None
    # test first_parent_include
    b.first_parent_include={}
    assert b.first_parent_include==None
    # test parent
    b.parent=None
    assert b.parent==None
    b.parent={"task":""}
    assert b.parent==None
    # test parents_static
    b.parents_static=None
    assert b.parents_

# Generated at 2022-06-13 08:06:11.292743
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    import collections
    import sys
    import os

    from ansible.template import Templar

    class __MockPlay(object):
        def __init__(self):
            self.vars_file = []
            self.vars_prompt = []
            self.vars_source = []
            self.inventory = None
            self.only_tags = ['tag1']
            self.skip_tags = []
            self.basedir = ''

        def get_vars(self, task=None):
            return dict(foo=1, bar=2)

        @property
        def variables(self):
            return collections.defaultdict(lambda: None, dict(foo=1, bar=2))


# Generated at 2022-06-13 08:06:21.481154
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    # case 1, all parents' statically_loaded is True
    b1 = Block()
    b2 = Block(parent=b1)
    b3 = Block(parent=b2)
    assert b3.all_parents_static()
    # case 2, parent's statically_loaded is False
    b2.statically_loaded = False
    assert not b3.all_parents_static()
    # case 3, ListMixin's statically_loaded is False
    b2.statically_loaded = True
    i1 = TaskInclude()
    b3.parent = i1
    assert not b3.all_parents_static()
    # case 4, HandlerTaskInclude's statically_loaded

# Generated at 2022-06-13 08:06:32.352816
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins import module_loader
    module_loader.add_directory(C.DEFAULT_MODULE_PATH)
    display = Display()


# Generated at 2022-06-13 08:07:01.317091
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import os

    block1 = Block(task_include=None)
    role = Role()
    role._parent = block1
    task = Task()
    task._role = role
    dep_chain = task.get_dep_chain()
    assert dep_chain == [block1]

    file_name = 'test.yaml'

# Generated at 2022-06-13 08:07:15.793117
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    '''
    [RequestTag, always_run=False] -> load_tasks -> [LoadTag, always_run=True] -> filter_tagged_tasks -> Resulting Block
    [RequestTag, always_run=True] -> load_tasks -> [LoadTag, always_run=False] -> filter_tagged_tasks -> Resulting Block
    '''
    import os
    import sys
    import tempfile
    import shutil

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook import PlayBook
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext

    temp_dir = tempfile.mkdtemp

# Generated at 2022-06-13 08:07:16.912785
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    assert isinstance(b, Block)


# Generated at 2022-06-13 08:07:24.059611
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    class Test_Block():
        def test_set_loader_loader_is_not_None(self, request):
            block = Block(loader = None)
            block.set_loader(loader = None)
            assert block._loader is None

        def test_set_loader_loader_is_None_role_is_not_None(self, request):
            class Test_Role():
                def test_set_loader(self):
                    self._loader = None
                def get_loader(self):
                    return self._loader
            #
            class Test_Loader():
                def get_basedir(self):
                    return 'role'
            #
            loader = Test_Loader()
            role = Test_Role()
            block = Block(loader = None, role = role)
            block.set_loader(loader = loader)
            assert block

# Generated at 2022-06-13 08:07:33.137766
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    try:
        from ansible.playbook.role import Role
    except ImportError:
        Role = None

    from ansible.playbook.play_context import PlayContext

    b = Block()
    data = dict(name='foo', handlers=[], when='', tags=[], register='', ignore_errors='', run_once='', always=[], rescue=[], block=[], any_errors_fatal='', delegate_to='', delegate_facts='', failed_when='', changed_when='', ignore_errors='', always_run='', retries=0, delay=0, until='', poll=0)
    # Initialize variable manager
    variable_manager = VariableManager()
    variable_manager._extra_vars = load_extra_vars(loader=None, options=dict(tags=[], skip_tags=[]))
    variable_manager._

# Generated at 2022-06-13 08:07:40.417446
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    variable_manager = VariableManager()
    variable_manager.set_inventory(HostVars(inventory=None, loader=None, variable_manager=None))
    play_context = PlayContext(remote_addr='127.0.0.1', port=22)
    play_context.become = None
    play_context.become_method = None
    play_context.become_user = None
    host = Host()
    task = Task()
    task.block = True
    task._variable_manager = variable_manager
    task._play_context

# Generated at 2022-06-13 08:07:41.404058
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    b = Block()
    assert b.set_loader() == None


# Generated at 2022-06-13 08:07:49.087753
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:08:00.518596
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    source_json = '{"block": [], "dep_chain": null, "rescue": [], "always": [], "implicit": false}'
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='local_hosts')

# Generated at 2022-06-13 08:08:07.396829
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    assert not block.has_tasks()
    block.block = ['foo']
    assert block.has_tasks()
    block.block = []
    block.rescue = ['foo']
    assert block.has_tasks()
    block.rescue = []
    block.always = ['foo']
    assert block.has_tasks()


# Generated at 2022-06-13 08:08:44.670084
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block(loader=DataLoader(), role=Role(), use_handlers=False, implicit=False)
    assert block.has_tasks() == False


# Generated at 2022-06-13 08:08:50.290414
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    block = Block()
    block.block = [1]
    assert(block.has_tasks())
    block.block = []
    assert(not block.has_tasks())
    block.rescue = [2]
    assert(block.has_tasks())
    block.rescue = []
    assert(not block.has_tasks())
    block.always = [3]
    assert(block.has_tasks())
    block.always = []
    assert(not block.has_tasks())

# Generated at 2022-06-13 08:08:52.208900
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    data = {}
    block.deserialize(data)
    assert block._valid_attrs == {}


# Generated at 2022-06-13 08:08:57.265596
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    ans_vars = AnsibleVars(play=None,
                           vars_files=['./test/unittest_vars/test_vars_files/test_vars_file1.yml',
                                       './test/unittest_vars/test_vars_files/test_vars_file2.yml'],
                           extra_vars=['./test/unittest_vars/test_vars_files/test_vars_file1.yml',
                                       'var1=t1var1val', 'var2=t1var2val'],
                           all_vars={'var1': u't1var1val', 'var2': u't1var2val'})

# Generated at 2022-06-13 08:09:02.602443
# Unit test for method set_loader of class Block
def test_Block_set_loader():

    # Test that set_loader is called on dep_chain of Block object
    # Test that Block._loader is set correctly
    
    # Initialize Block object
    block = Block()

    # Prepare mock objects
    block.get_dep_chain = lambda: [1]
    block._parent = object()
    block._parent.set_loader = lambda x: None
    block._parent._parent = None
    block._role = None
    block._delegate_to = None
    
    # Initialize loader
    loader = object()
    
    # Test
    block.set_loader(loader)
    assert block._loader == loader

    # No dep_chain
    block._dep_chain = None
    block._loader = None
    block.get_dep_chain = lambda: None
    block.set_loader(loader)
    assert block

# Generated at 2022-06-13 08:09:03.265610
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    pass

# Generated at 2022-06-13 08:09:07.918128
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  data = {'rescue': [], 'always': [], 'dep_chain': None, 'block': [], 'vars': {'c': 'a'}}
  block = Block()
  block.deserialize(data)
  assert block.vars == {'c': 'a'}


# Generated at 2022-06-13 08:09:11.851488
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    from ansible.playbook.task_include import TaskInclude

    class test_Block(Block):
        pass

    class test_TaskInclude(TaskInclude):
        pass

    t1_task_include = test_TaskInclude()
    t2_task_include = test_TaskInclude()
    b = test_Block()
    b._parent = t1_task_include
    t1_task_include._parent = t2_task_include

    assert b.get_first_parent_include() == t2_task_include


# Generated at 2022-06-13 08:09:22.726836
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    myBlock = Block()
    myBlock.deserialize({'block': [{'action': 'command', 'args': 'echo test', 'delegate_to': False, 'name': '', 'register': 'shell_out', 'when': True}], 'always': [], 'delegate_to': False, 'failed_when': False, 'ignore_errors': False, 'loop': {}, 'register': 'test_block', 'rescue': [], 'vars': {}})
    assert 'block' in myBlock._attributes
    assert myBlock.block == [{'action': 'command', 'args': 'echo test', 'delegate_to': False, 'name': '', 'register': 'shell_out', 'when': True}]
    assert 'rescue' in myBlock._attributes
    assert myBlock.rescue == []


# Generated at 2022-06-13 08:09:24.677808
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    print('Test unit for method get_dep_chain of class Block')
    pass

