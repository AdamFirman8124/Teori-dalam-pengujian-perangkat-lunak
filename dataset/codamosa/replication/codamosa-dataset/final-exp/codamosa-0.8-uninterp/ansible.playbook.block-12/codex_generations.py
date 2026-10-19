

# Generated at 2022-06-13 08:00:01.855450
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Block data
    block_ = {'block':[{'when':'True', 'tasks':[{'name':'Task1', 'tags':['a']}, {'name':'Task2', 'tags':['a', 'b']}]}, {'rescue':[{'name':'Task3', 'tags':['a']}, {'name':'Task4', 'tags':['b']}]}], 'when':'True', 'register':'event'}
    block_data = block_['block']
    block_rescue = block_data[1]['rescue']
    assert block_data[0]['tasks'][1].tags == ['a', 'b']
    assert block_data[1]['rescue'][0].tags == ['a']

    # Call method filter_tagged_tasks of class

# Generated at 2022-06-13 08:00:05.506553
# Unit test for method copy of class Block
def test_Block_copy():
    obj = Block()
    obj2 = obj.copy()
    assert obj.block == obj2.block
    assert obj.rescue == obj2.rescue
    assert obj.always == obj2.always
    obj3 = obj.copy(exclude_parent=True)
    assert obj3._parent == None


# Generated at 2022-06-13 08:00:06.573803
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    pass


# Generated at 2022-06-13 08:00:11.199636
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Test if the copy function of Block returns a copy of the object.
    '''
    from ansible.playbook.task import Task
    block = Block(parent=Block(), role=Role(), task_include=HandlerTaskInclude())
    assert block.copy() != block


# Generated at 2022-06-13 08:00:21.042191
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    args = dict(
        play=dict(),
        parent_block=dict(),
        role=dict(),
        task_include=dict(),
        use_handlers=bool(),
        variable_manager=dict(),
        loader=dict()
    )

    block = Block(**args)

    with pytest.raises(TypeError) as error:
        block.set_loader(loader=None)
    assert_that(str(error.value), equal_to("loader should be an instance of Loader, got <class 'NoneType'> instead"))

    with pytest.raises(AssertionError) as error:
        block.set_loader(loader=dict())
    assert_that(str(error.value), equal_to("only accepts Loader objects"))


# Generated at 2022-06-13 08:00:28.455619
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()

# Generated at 2022-06-13 08:00:38.535820
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    play = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
          dict(action=dict(module='shell', args='ls'), register='shell_out'),
          dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    b = Block(play=play, role=role, task_include=task_include, use_handlers=use_handlers, implicit=implicit)
    assert b.has_tasks() == True
    play = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [],
    )

# Generated at 2022-06-13 08:00:41.397086
# Unit test for method copy of class Block
def test_Block_copy():
    block_obj = Block()
    assert isinstance(block_obj.copy(), Block)



# Generated at 2022-06-13 08:00:46.849322
# Unit test for method copy of class Block
def test_Block_copy():
    block = Block()
    parent_block = Block(block=["exclude_tasks"])
    block.parent = parent_block
    new_block = block.copy(exclude_tasks=True)
    assert new_block is not block
    assert block.parent is parent_block
    assert new_block.parent is not parent_block
    assert new_block.parent is None

# Generated at 2022-06-13 08:00:47.807134
# Unit test for method copy of class Block
def test_Block_copy():
    pass


# Generated at 2022-06-13 08:01:07.041081
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=False)
    b.block = [{ "block": [ {"name": "task1"}, {"name": "task2"} ] }]
    b.rescue = [{ "block": [ {"name": "task3"}, {"name": "task4"} ] }]
    b.always = [{ "block": [ {"name": "task5"}, {"name": "task6"} ] }]
    # dep_chain = self.get_dep_chain() is empty
    assert b.get_dep_chain() == None


# Generated at 2022-06-13 08:01:09.411184
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    # create TaskInclude object
    ret_obj = TaskInclude()
    # create Block object
    b = Block()
    # invoke get_dep_chain method
    b.get_dep_chain()


# Generated at 2022-06-13 08:01:14.549603
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.playbook import Play
    play = Play()
    play._ds = dict()
    play._loader = None
    play._variable_manager = None
    play.statically_loaded = True
    play.post_validate = post_validate.copy()
    play.vars_prompt = dict()
    play.vars_files = list()
    play.post_validate = dict()
    play.dependencies = list()
    play.role_names = list()
    play.roles = list()
    Play._valid_attrs = dict()
    play._valid_attrs = dict()
    play._valid_attrs['name'] = dict(default=None)
    play._valid_attrs['hosts'] = dict(default='all')

# Generated at 2022-06-13 08:01:20.097782
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    _logger = logging.getLogger("ansible_playbook.block")
    _logger.setLevel(logging.INFO)
    #_logger.setLevel(logging.DEBUG)

    logger = logging.getLogger("ansible_task")
    logger.setLevel(logging.INFO)
    #logger.setLevel(logging.DEBUG)

    all_vars = {}

    #----------------------
    # Test implicit blocks
    #----------------------
    logger.debug("Testing implicit blocks")
    # Test with one task
    playbook = dict(block=dict(tasks=dict(action="debug", msg="implicit")))
    b = Block.load(playbook, variable_manager=VariableManager(), loader=DataLoader())
    logger.debug("loaded block: %s", b)
    filtered = b.filter

# Generated at 2022-06-13 08:01:24.704377
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    # Setting up mocks, fakes and stubs
    class Mock_TaskInclude():
        """
        Imitates a TaskInclude object
        """
        def __init__(self):
            self.is_task_include = True
        def get_first_parent_include(self):
            """
            Mock method
            """
            return self
    class FakeBlock():
        """
        Fake Block class
        """
        def __init__(self):
            self._parent = None
        def get_first_parent_include(self):
            """
            Fake method
            """
            return None

    def name():
        """
        Used as a mock method
        """
        return "name"

    def add_tasks(self):
        """
        Used as a mock method
        """
        pass


# Generated at 2022-06-13 08:01:27.435030
# Unit test for method get_first_parent_include of class Block
def test_Block_get_first_parent_include():
    #test 1
    b = Block(play=None)
    assert b.get_first_parent_include() == None
    #test 2
    b.get_first_parent_include()

# Generated at 2022-06-13 08:01:33.576414
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    import ansible.constants as C
    def setattr_statically_loaded(parent, val):
        parent.statically_loaded = val

    # unit test for _all_parents_static() for TaskInclude
    C.DEFAULT_TASK_INCLUDE_PARAMS = dict(
        static=False,
        _raw_params=dict(
            static='yes'
        )
    )

# Generated at 2022-06-13 08:01:42.327048
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    pb = PlaybookBase()
    t = Block(play=pb)
    assert t.has_tasks() == False
    t = Block(play=pb, block=[
        dict(
           action="shell",
           args="echo 'Hello world!'",
           register="shell_out"
        )
    ])
    assert t.has_tasks() == True
    t = Block(play=pb, rescue=[
        dict(
           action="shell",
           args="echo 'Hello world!'",
           register="shell_out"
        )
    ])
    assert t.has_tasks() == True
    t = Block(play=pb, always=[
        dict(
           action="shell",
           args="echo 'Hello world!'",
           register="shell_out"
        )
    ])
    assert t.has_

# Generated at 2022-06-13 08:01:45.460916
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    bl = Block()
    assert len(bl.block) == 0
    assert len(bl.rescue) == 0
    assert len(bl.always) == 0
    assert bl.has_tasks() == False


# Generated at 2022-06-13 08:01:47.956864
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    test_obj = Block()
    test_obj.deserialize(data)
    assert test_obj.block is None
    assert test_obj.rescue is None
    assert test_obj.always is None


# Generated at 2022-06-13 08:02:15.711551
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test 2 conditions:
    # 1. if only_tags and skip_tags is set in the play,
    #    then skip_tags should not be used as a criteria and only_tags should
    #    be used as a criteria
    # 2. if only_tags are set in the play,
    #    then only_tags should be used as a criteria

    # set up for the test
    b = Block()
    # 1. Test if only_tags are set as a criteria and skip_tags are ignored

# Generated at 2022-06-13 08:02:27.659364
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # Given
    ### I create a block
    block = Block()
    ### I create a role
    role = Role()
    block._role = role
    ### I create a fake loader
    loader = "fake_loader"
    ### I set the attribute static_loaded of the next block to false
    block._parent = Block()
    block._parent.statically_loaded = False
    ### I set the attribute statically_loaded of the block at the end of the loop to false
    block._parent._parent = Block()
    block._parent._parent.statically_loaded = False
    ### I set the attribute statically_loaded of the block at the end of the loop to true
    block._parent._parent._parent = Block()
    block._parent._parent._parent.statically_loaded = True
    ### I set the attribute statically_loaded of the block at the end

# Generated at 2022-06-13 08:02:37.454338
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # Create an instance of class Block
    b1 = Block()
    b1.statically_loaded = True
    b2 = Block()
    b2.statically_loaded = True
    b1.dep_chain = [b2]
    assert b1.all_parents_static()
    b2.statically_loaded = False
    assert not b1.all_parents_static()
    b1.statically_loaded = False
    assert not b2.all_parents_static()


# Generated at 2022-06-13 08:02:40.566596
# Unit test for method copy of class Block
def test_Block_copy():
    host = Mock()
    task = Task()
    task._role = Mock()
    task_list = [Task()]
    block = Block(play=host, task_list=task_list)
    block._parent = task
    block._role = Mock()
    block.copy()


# Generated at 2022-06-13 08:02:47.583336
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    # Initialize a Block
    b = Block(play=None, parent_block=None, role=None, task_include=None, use_handlers=False, implicit=None)
    # Initialize a loader
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    # Then set loader to Block
    b.set_loader(loader)



# Generated at 2022-06-13 08:02:53.207731
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    # create an instance of the class Block
    block = Block()

    # set the value of block and rescue
    block.block = [1, 2, 3]
    block.rescue = [4, 5]

    # test the method has_tasks and the value of block and rescue
    assert block.has_tasks()


# Generated at 2022-06-13 08:02:55.347215
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    '''Unit test for method set_loader of class Block'''
    print('Testing Block set_loader')
    raise NotImplementedError


# Generated at 2022-06-13 08:02:55.956582
# Unit test for method set_loader of class Block

# Generated at 2022-06-13 08:02:57.702464
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    # The statement below will be covered in test case: test_use_assert_deprecation
    assert False

# Generated at 2022-06-13 08:03:06.201564
# Unit test for method is_block of class Block

# Generated at 2022-06-13 08:03:59.819838
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    my_block = Block()
    my_block.deserialize(None) 
    my_block.deserialize({}) 


# Generated at 2022-06-13 08:04:01.429732
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():

    from ansible.playbook.block import Block

    a = Block()


# Generated at 2022-06-13 08:04:09.929522
# Unit test for method copy of class Block
def test_Block_copy():
    class BuiltInModule(object):
        def __init__(self):
            self.PARAM_COMPATIBLE = ['statically_loaded']

    class Base(object):
        def __init__(self):
            self._attributes = {}
            self._valid_attrs = set(['statically_loaded'])

    class Parent(object):
        def __init__(self):
            self._attributes = {}
            self._valid_attrs = set(['statically_loaded'])
            self.statically_loaded = True

    class Play(object):
        def __init__(self):
            self._attributes = {}
            self._valid_attrs = set(['statically_loaded'])

    class Role(object):
        def __init__(self):
            self._attributes = {}
            self._

# Generated at 2022-06-13 08:04:23.906119
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():

    from ansible.parsing.dataloader import DataLoader

    def get_loader():
        return DataLoader()

    # Test 1
    play = AnsiblePlay()
    bl = Block(play=play)

# Generated at 2022-06-13 08:04:26.243267
# Unit test for method preprocess_data of class Block
def test_Block_preprocess_data():
    data = {'block':[{'task': 'test', 'action': '/bin/echo'}]}
    b = Block()
    obj = b.preprocess_data(data)
    assert obj == data

# Generated at 2022-06-13 08:04:27.134389
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    return None

# Generated at 2022-06-13 08:04:33.675349
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    block = Block()
    block._valid_attrs = {
        'block': Attribute(required=False),
        'name': Attribute(required=False),
        'loop': Attribute(required=False),
        'rescue': Attribute(required=False),
        'always': Attribute(required=False),
        'vars': Attribute(required=False, default=dict()),
        'vars_prompt': Attribute(required=False, default=dict()),
        'vars_files': Attribute(required=False, default=list()),
        'when': Attribute(required=False),
        'tags': Attribute(required=False),
        'register': Attribute(required=False),
    }
    data = {}
    expected = None
    block.deserialize(data)
    actual = None

# Generated at 2022-06-13 08:04:37.663488
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    data = dict()

    # Set up test object
    B = Block()

    # Test deserialize with no data raises exception
    with pytest.raises(AnsibleParserError, message="deserialize with no data should raise exception"):
        B.deserialize(data)

# Generated at 2022-06-13 08:04:39.958390
# Unit test for method deserialize of class Block
def test_Block_deserialize():
  block = Block()
  data = dict()
  data['role'] = dict()
  block.deserialize(data)



# Generated at 2022-06-13 08:04:48.243560
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    def get_playbook_and_include(playbook_dir):
        #Load the playbook and a role we will use in the test
        playbook_path = "%s/../../../test/integration/files/pbs/simple_playbook.yml" % os.path.dirname(__file__)
        if playbook_dir:
            playbook_path = "%s/%s" % (playbook_dir, os.path.basename(playbook_path))

        pb = PlayBook.load(playbook_path, loader=DictDataLoader(), variable_manager=VariableManager())

        play = pb.get_plays()[0]

        #get the first task of the play
        t = play.tasks[0]

        #get the first task of the first include
        t = t._parent.tasks[0]

# Generated at 2022-06-13 08:05:38.517320
# Unit test for method copy of class Block
def test_Block_copy():
    _data = dict(
        nocopy='nocopy',
        nocopy2='nocopy2',
    )
    _data2 = dict(
        copy='copy',
    )
    obj = Block.load(_data)
    obj2 = Block.load(_data2)
    obj.block.extend(obj2.block)
    # print(str(obj._attributes))
    # print(str(obj.block._attributes))
    # print(str(obj2.block._attributes))
    obj.nextblock = obj2.block
    # obj2.block.extend(obj.block)
    # print(str(obj._attributes))
    # print(str(obj.block._attributes))
    # print(str(obj2.block._attributes))

# Generated at 2022-06-13 08:05:49.901501
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    b = Block()

# Generated at 2022-06-13 08:06:01.575061
# Unit test for method set_loader of class Block
def test_Block_set_loader():
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = { "current_host": "localhost" }
    loader = DataLoader()

    inventory = InventoryManager(loader=loader,
                                 sources=['/etc/ansible/hosts']
                                 )
    play_context = PlayContext()
    play_context.remote_addr = 'localhost'
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    ds = static_data('Block')
    ds['block'][1] = static_data('Task')

# Generated at 2022-06-13 08:06:09.153759
# Unit test for method deserialize of class Block
def test_Block_deserialize():

    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    class Block(Base):
        _parent = None
        _play = None
        _dep_chain = None
        _role = None
        _loader = None
        _attributes = {}
        _block_name = ''

# Generated at 2022-06-13 08:06:20.840049
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    collection = {'tasks': [{'action': 'shell', 'name': 'this is a test', 'tags': ['always']}, {'action': 'debug', 'name': 'this is a test', 'tags': ['always']}, {'action': 'debug', 'name': 'this is a test', 'tags': ['always']}, {'action': 'debug', 'name': 'this is a test', 'tags': ['always']}]}

# Generated at 2022-06-13 08:06:31.704595
# Unit test for method copy of class Block
def test_Block_copy():

    # AnsibleModule checks for parameters so it needs to run first
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.urls import open_url
    from ansible.module_utils._text import to_text
    import json
    import sys
    import unittest

    if sys.version_info[:2] == (2, 6):
        import simplejson as json

    # make sure we do not get a SSLv3 error
    import imp
    imp.reload(urllib)
    import urllib
    h = urllib.HTTPHandler()
    h.set_http_debuglevel(1)
    o = urllib.build_opener(h)

# Generated at 2022-06-13 08:06:40.696634
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    # Test 1:
    # Initiate a block object
    # Assign block with one task having tags and the other without tags
    # Assign all_vars to values of different tags
    # Evaluate whether filter_tagged_tasks return a block with task having tags
    # Expect Result: filter_tagged_tasks return a block with task having tags

    # Initiate a block object
    block = Block()

    # Assign block with one task having tags and the other without tags
    block.block = [Task(), Task()]
    block.block[1].tags = ['test']

    # Assign all_vars to values of different tags
    all_vars = dict()
    all_vars['tags'] = ['test', 'test2']

    # Evaluate whether filter_tagged_tasks return a block with task having tags


# Generated at 2022-06-13 08:06:51.885720
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    obj = Block()
    assert obj.has_tasks() == False
    obj.block = []
    obj.rescue = []
    obj.always = []
    assert obj.has_tasks() == False
    obj.block = [0, 1, 2]
    obj.rescue = []
    obj.always = []
    assert obj.has_tasks() == True
    obj.block = [0, 1]
    obj.rescue = []
    obj.always = []
    assert obj.has_tasks() == True
    obj.block = [0, 1, 2, 3]
    obj.rescue = [0, 1]
    obj.always = [0, 1, 2]
    assert obj.has_tasks() == True
    obj.block = [0, 1, 2, 3]
    obj

# Generated at 2022-06-13 08:07:00.452731
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    TaskInclude.use_static_include = False
    block1 = Block()
    block2 = Block()
    block2._parent = block1
    block3 = Block()
    block3._parent = block2
    block4 = Block()
    block4._parent = block3
    block5 = Block()
    block5._parent = block4
    assert True == block5.all_parents_static()
    include = TaskInclude()
    include._parent = block1
    block2._parent = include
    assert False == task.all_parents_static()
# Class PlayContext

# Generated at 2022-06-13 08:07:14.840342
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from io import StringIO
    # test cases
    # the value of _dep_chain is None
    '''
    find the corresponding include task, and return the value of dep_chain
    '''
   

# Generated at 2022-06-13 08:08:31.553306
# Unit test for method filter_tagged_tasks of class Block
def test_Block_filter_tagged_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'somehost': {}}}

    variable_manager._fact_cache = {}
    variable_manager._fact_cache['somehost'] = {'ec2_tags': {'bar': 'baz', 'foo': 'qux'}}
    variable_manager.set_inventory(Inventory(loader=loader, sources=['localhost']))


# Generated at 2022-06-13 08:08:39.841960
# Unit test for method copy of class Block
def test_Block_copy():
    '''
    Unit test for method copy of class Block
    '''
    obj = Block()
    obj.block = [
        {'block': [
            {'assert': [
                {'eq': [
                    {'var': 'x'},
                    {'var': 'y'}
                ]},
                'comment'
            ]},
            {'import_tasks': 'a.yaml'}
        ]},
        {'include': 'b.yaml'},
    ]
    obj.rescue = [{'import_tasks': 'a.yaml'}]
    obj.always = [{'import_tasks': 'a.yaml'}]
    obj._play = []
    obj._use_handlers = False
    obj._dep_chain = None
    obj._parent = None


# Generated at 2022-06-13 08:08:45.265523
# Unit test for method copy of class Block
def test_Block_copy():
	block = Block()
	block.block = [{'when': 'False'}, {'when': 'True'}]
	copy = block.copy(exclude_parent=True, exclude_tasks=False)
	assert isinstance(copy.block[0], Task)
	assert copy.block[0].when == 'False'
	assert isinstance(copy.block[1], Task)
	assert copy.block[1].when == 'True'
	assert copy._parent == None


# Generated at 2022-06-13 08:08:49.667422
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    from ansible.playbook.task_include import TaskInclude
    block = Block()
    task_include = TaskInclude()
    block.static_load(task_include)
    task_include.static_load(block)
    assert False == block.all_parents_static()
    assert True == task_include.all_parents_static()



# Generated at 2022-06-13 08:08:50.313877
# Unit test for method deserialize of class Block
def test_Block_deserialize():
    pass

# Generated at 2022-06-13 08:08:57.092023
# Unit test for method copy of class Block
def test_Block_copy():

    v = Block(
        play=None,
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        implicit=False,
    )
    assert isinstance(v, Block)
    v.block = Sentinel  # list
    v._dep_chain = None  # list
    v._play = Sentinel  # Play
    v.rescue = Sentinel  # list
    v.always = Sentinel  # list
    v._role = Sentinel  # Role
    v._parent = Sentinel  # Base

    new_me = v.copy(exclude_parent=False,exclude_tasks=False)
    assert isinstance(new_me, Block)
    assert new_me._play == v._play
    assert new_me._use_handlers == v._use_

# Generated at 2022-06-13 08:09:02.054613
# Unit test for method all_parents_static of class Block
def test_Block_all_parents_static():
    # static, static
    play1 = Play()
    block1 = Block(parent=play1)
    assert block1.all_parents_static() == True

    # dynamic, static
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    p1 = Task()
    p1.statically_loaded = False
    block2 = Block(parent=p1)
    assert block2.all_parents_static() == False

    # static, dynamic, static
    p2 = Task()
    p3 = Handler()
    p2.statically_loaded = False
    p2.parent = p3
    block3 = Block(parent=p2)
    assert block3.all_parents_static() == False

    # dynamic, dynamic, static
    p4 = Task()
    p5

# Generated at 2022-06-13 08:09:09.797971
# Unit test for method has_tasks of class Block
def test_Block_has_tasks():
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load(dict(
          name = "Ansible Play",
          hosts = 'localhost',
          gather_facts = 'no',
          tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='debug', args=dict(msg='{{a_var}}'))),
          ]
        ), loader=loader, variable_manager=variable_manager)
    assert play.blocks[0].has_tasks()

# Generated at 2022-06-13 08:09:11.269682
# Unit test for method get_dep_chain of class Block
def test_Block_get_dep_chain():
    print ("Start test_Block_get_dep_chain")
    print ("End test_Block_get_dep_chain")

# Generated at 2022-06-13 08:09:22.520777
# Unit test for method copy of class Block
def test_Block_copy():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory


    block = Block()
    task = Task()
    task._parent = block
    #dupe_task_list
    #copy
    block.copy()
    task.copy()


    role = Role()
    role.set_loader('loader')
    #dupe_task_list
    block.copy()
    task.copy()


    PlayContext()
    Inventory()

    #dupe_task_list
    block.copy()
    task.copy()

    #copy
    block.copy()
    task.copy()
    #filter_tagged_tasks