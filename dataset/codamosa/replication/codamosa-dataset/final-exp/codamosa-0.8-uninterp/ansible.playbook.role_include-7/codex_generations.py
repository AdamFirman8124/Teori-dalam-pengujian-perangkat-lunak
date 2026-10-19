

# Generated at 2022-06-13 09:02:51.561034
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Test that IncludeRole load a role
    test_role = "test_roles/deprecation_notice_role"
    data = dict(
        name="deprecation_notice_role",
    )
    data_lt_2_9 = dict(
        name="deprecation_notice_role",
        allow_duplicates=True,
    )
    ir = IncludeRole.load(data, loader=C.get_configuration_loader())
    ir_lt_2_9 = IncludeRole.load(data_lt_2_9, loader=C.get_configuration_loader())
    assert ir._role_name == test_role
    assert ir.allow_duplicates == ir_lt_2_9.allow_duplicates
    assert ir.args == data

    # Test that IncludeRole.get_block_

# Generated at 2022-06-13 09:02:55.702779
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Initialize IncludeRole instance
    include_role = IncludeRole(role="rolename")
    # Get name of the task
    name = include_role.get_name()
    assert name == "include_role : rolename"


# Generated at 2022-06-13 09:02:56.706144
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # FIXME: write unit tests
    pass

# Generated at 2022-06-13 09:03:02.962449
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    fake_loader = DictDataLoader({'roles/foo': DictDataLoader(dict(
        meta=dict(
            dependencies=dict(
                roles=['baz']
            ),
        ),
        tasks=dict(
            main=["role/bar", "role/quux"]
        )
    ))})

    fake_play = Play().load({
        'name': 'fakeplay',
        'connection': 'local',
        'hosts': 'all',
        'gather_facts': 'no'
    }, variable_manager=VariableManager())
    fake_

# Generated at 2022-06-13 09:03:03.528757
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    assert True

# Generated at 2022-06-13 09:03:11.921835
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Initialize the object IncludeRole()
    data = dict({'name': 'test_role', 'tags': 'role_tag'})
    block = Block(parent_block=None, role=None, task_include=None, use_handlers=True, always_run=False)
    role = Role()
    task_include = TaskInclude()
    variable_manager = None
    loader = None
    ir = IncludeRole.load(data, block, role, task_include, variable_manager, loader)

    assert ir.get_name() == "include_role : test_role"


# Generated at 2022-06-13 09:03:15.252511
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    test_data = {'name': 'test_name'}
    test_data = IncludeRole.load(test_data)

    assert test_data._role_name == 'test_name'


# Generated at 2022-06-13 09:03:26.529704
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook
    import ansible.template
    import ansible.vars
    play = ansible.playbook.Play()
    templar = ansible.template.Templar(loader=None, variables={})
    variable_manager = ansible.vars.VariableManager()
    block = ansible.playbook.Block(play=play)

    # Build a Block
    new_block = Block(parent=block)
    new_block.block = [
        {
            'name': 'Task 0',
            'action': {'__ansible_module__': 'debug', 'msg': 'Task 0'}
        },
        {
            'name': 'Task 1',
            'action': {'__ansible_module__': 'debug', 'msg': 'Task 1'}
        }
    ]
   

# Generated at 2022-06-13 09:03:37.194533
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import include_role_tasks

    loader = DataLoader()
    variable_manager = VariableManager()

    including_task = {
        'action': 'include_role',
        'args': {
            'name': 'foo'
        }
    }

    IncludingRole = Role()
    IncludingRole._tasks = [IncludeRole.load(including_task)]
    IncludingRole._tasks[0]._parent = IncludingRole
    IncludingRole._tasks[0]._parent_role = None

    resulting_blocks = include_role_tasks(IncludingRole)
    assert resulting_blocks is not None
    assert len(resulting_blocks) > 0

    #

# Generated at 2022-06-13 09:03:39.668183
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    print("testing method get_block_list of class IncludeRole")
    ir = IncludeRole()
    ir._role_name = "test_role"
    ir._parent_role = None
    ir._role_path = None
    ir._from_files = {}
    ir.vars = {}

    res = ir.get_block_list()
    print(res)
    print(ir._role_path)


if __name__ == '__main__':
    test_IncludeRole_get_block_list()

# Generated at 2022-06-13 09:04:06.629402
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # test_IncludeRole_load_noattrs - verify IncludeRole throws exception if no attrs provided
    # test_IncludeRole_load_noattr_name - verify IncludeRole throws exception if name/role not provided
    with pytest.raises(AnsibleParserError):
        IncludeRole.load({}, task_include=None)
    with pytest.raises(AnsibleParserError):
        IncludeRole.load({'foo': 'bar'}, task_include=None)

    # test_IncludeRole_load_public_nonrole - verify IncludeRole throws exception if public attr is not a role
    with pytest.raises(AnsibleParserError):
        IncludeRole.load({'name': 'foobar'}, task_include=None)
    with pytest.raises(AnsibleParserError):
        IncludeRole

# Generated at 2022-06-13 09:04:15.541859
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    loader = None
    variable_manager = None
    display = Display()
    options = None
    blk = Block.load({}, None, loader, variable_manager, display, options)
    role = Role()
    role._role_name = 'test'
    ir = IncludeRole({}, role)
    ir.args = {'name': 'foo'}
    assert ir.get_name() == 'foo'
    assert ir.get_name() == 'foo'
    ir.name = 'bar'
    assert ir.get_name() == 'bar'
    ir.action = 'include_role'
    assert ir.get_name() == 'bar'
    assert ir.get_name() == 'bar'
    ir.name = None
    assert ir.get_name() == 'include_role : foo'

# Generated at 2022-06-13 09:04:19.434616
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Create IncludeRole object with default settings and get_block_list()
    display = Display()
    block = Block()
    role = Role(name='test_role')
    task_include = TaskInclude()
    ir = IncludeRole(block, role, task_include)
    ir.name = 'my_include_role'
    ir._role_name = 'my_role'
    #print(ir.get_block_list())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Test IncludeRole
#

# Generated at 2022-06-13 09:04:27.260138
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    action_plugin_loader = ActionModuleLoader(os.path.join(curr_dir, '..', '..'), 'action_plugins')
    action_plugin_loader.set_directory(os.path.join(curr_dir, '..', '..', 'action_plugins'))
    action_plugin_loader.add_directory(C.DEFAULT_ACTION_PLUGIN_PATH)

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:04:38.391695
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    from ansible.plugins.loader import include_role_plugin

    test_task = dict(
        action='include_role',
        name='test_role',
    )

    test_play = ansible.playbook.Play.load(dict(
        name='test_play',
        hosts='all',
        gather_facts=False,
        tasks=dict(vars=dict(foo='bar'), include_role=test_task),
    ), variable_manager=VariableManager(), loader=DataLoader())


# Generated at 2022-06-13 09:04:49.144654
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list(): 
    # test to show the above code is valid 
    from ansible.playbook.play import Play 
    from ansible.template import Templar 
    from ansible.vars.manager import VariableManager 

    pb = Play.load(dict( 
        name="test play", 
        hosts=["foo"], 
        gather_facts="no", 
        roles=[ 
            dict( 
                name='simple', 
                tasks=[ 
                    dict(include_role=dict(name="role1", public=True)) 
                ] 
            ) 
        ] 
    ), variable_manager=VariableManager(), loader=None) 

    ir = IncludeRole.load(dict( 
        name="role1", 
        public=True 
    )) 


# Generated at 2022-06-13 09:04:53.945204
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # setup
    from ansible.playbook.block import Block

    b = Block()
    my_block = IncludeRole(block=b)
    # execute
    mbl = my_block.get_block_list()
    # assert
    assert len(mbl)==0
    assert True

# Generated at 2022-06-13 09:05:01.850601
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager
    curr_dir = C.DEFAULT_LOCAL_TMP
    C.DEFAULT_LOCAL_TMP = "/tmp"
    role_name = "role_name"
    role_dir = "/tmp/role_dir"
    block = Block()
    play = Play()
    task = Task(block=block, role=Role(), task_include=None)

# Generated at 2022-06-13 09:05:15.092436
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.constants as C
    # Create includes and roles objects
    include_task = IncludeRole()
    include_task._role_name = "test_role"

    # Create a Block object to be used by the include_task object
    block = Block()

    # Create a role object
    role = Role()
    role._role_name = "test_role"

    # Create a block object to be used by the role object
    sub_block = Block()
    sub_block._role_name = "test_role"
    sub_block._block = [[{'set_fact': {'fact1': 11}},
                        {'set_fact': {'fact2': 12}},
                        {'set_fact': {'fact3': 13}}]]
    role._blocks = sub_block

    # Create a Play object
   

# Generated at 2022-06-13 09:05:22.946844
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    def _create_ir(loader, variable_manager, data, block, role, task_include=None):
        return IncludeRole.load(data, block, role, task_include, variable_manager, loader)
    # this code is outside the class due to the way mock.patch works with objects
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.module_utils.six import string_types

    loader = DataLoader()
    variable_manager = VariableManager()
    role_path = os.path.join(C.DEFAULT_ROLES_PATH, 'subdir', 'example_role')

   

# Generated at 2022-06-13 09:05:44.511121
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.args = dict(name='foo')
    assert ir.get_name() == 'foo'
    ir.action = 'include_role'
    ir.block = Block()
    ir.block.args = dict(name='bar')
    assert ir.get_name() == 'bar'
    ir.action = 'include_tasks'
    assert ir.get_name() == '<include_tasks: foo>'
    ir.block.args = dict(name='bar')
    assert ir.get_name() == '<include_tasks: bar>'

# Generated at 2022-06-13 09:05:53.260256
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    play = Play()
    play._loader = loader
    play._variable_manager = variable_manager
    play._inventory = inventory

    data = {
        'name': 'apache',
        'apply': {
            'tags': 'apache_install',
            'ignore_errors': 'no'
        }
    }
    ir = IncludeRole.load(data, play=play)
    assert ir.args['name'] == 'apache'

# Generated at 2022-06-13 09:06:05.544925
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test with a block that has no tasks
    block_tasks = []
    block = Block(block_tasks)

    # Test with a role that has no tasks
    role_tasks = []
    role = Role(name='test_role', tasks=role_tasks)

    # Test with a task_include that has no tasks
    task_include_tasks = []
    task_include = TaskInclude(name='test_task_include', tasks=task_include_tasks)

    # Test with invalid data
    data = {}
    try:
      IncludeRole.load(data, block, role, task_include)
    except AnsibleParserError as exception:
      assert str(exception) == '\'name\' is a required field for include_role.'

    # Test with valid data, and no variable_manager or loader
   

# Generated at 2022-06-13 09:06:10.684890
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    _block = Block()
    _role = Role()
    _task_include = TaskInclude()
    ir = IncludeRole(block=_block, role=_role, task_include=_task_include)
    blocks = ir.get_block_list(play=_block._play, variable_manager=_task_include._variable_manager, loader=_task_include._loader)
    assert blocks is _block

# Generated at 2022-06-13 09:06:14.247398
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    # init IncludeRole
    ir = IncludeRole()
    ir.name = None
    ir.action = 'include_role'
    ir._role_name = 'load_templates'

    # test get_name
    assert ir.get_name() == 'include_role : load_templates'


# Generated at 2022-06-13 09:06:22.939006
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play_iterator import PlayIterator

    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.task.include_role import IncludeRoleTask
    from ansible.playbook.block import Block

# Generated at 2022-06-13 09:06:35.821885
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """ IncludeRole - load, basic
    """

    play_context = dict(
        port=2222,
        remote_user='root',
        become=False,
        become_method='sudo',
        become_user='root',
        become_ask_pass=False,
        verbosity=3,
        connection='ssh',
        module_path='/foo',
        environment=dict(FOO='bar'),
        ansible_shell_type='csh',
        ansible_python_interpreter='/usr/bin/python',
        private_key_file='/foo/bar.key',
    )

    # success

# Generated at 2022-06-13 09:06:36.229622
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:06:40.453473
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Get a playbook block for testing
    block = Block()

    # Instantiate a Role object
    role = Role()

    # Instantiate a TaskInclude object
    task = TaskInclude()

    # Instantiate an IncludeRole object
    include_role = IncludeRole(block, role, task_include=task)

    # Set include_role attribute
    include_role._parent.action = 'include_role'
    include_role._role_name = '/path/to/role'
    include_role._parent._loader = None
    include_role._parent._variable_manager = None
    includes, handlers = include_role.get_block_list(play=None, variable_manager=None, loader=None)

    assert includes is not None
    assert handlers is not None
    assert include_role._role_path is not None

# Generated at 2022-06-13 09:06:51.760754
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Fake the objects
    fake_Block = namedtuple('fake_Block', 'args')
    fake_Role = namedtuple('fake_Role', 'args')
    fake_TaskInclude = namedtuple('fake_TaskInclude', 'args')

    # Create a IncludeRole object
    ir = IncludeRole(fake_Block(args = {'role': 'test_role'}), fake_Role(args = {'name': 'test_role'}), fake_TaskInclude(args = {'role': 'test_role'}))
    ir = ir.load_data({'name': 'test_role'}, variable_manager=None, loader=None)

    # Assert that the role_name has been correctly assigned
    assert ir._role_name == 'test_role'
    # Assert that the role_path is None
   

# Generated at 2022-06-13 09:07:27.393183
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block

    class Role_init(Role):
        def __init__(self):
            self._metadata = dict()
            self.name = "test_name"
            self.path = "/path/to/role"
            self._role_path = "/path/to/role/"
            self._parents = None
            self.dep_chain = list()
            self.vars = dict()
            self.default_vars = dict()
            self.handler_blocks = list()
            self.block  = Block()
            self.collections = list()

        def get_handler_blocks(self, play=None):
            return list()

        def compile(self, play=None, dep_chain=None):
            return list()


# Generated at 2022-06-13 09:07:36.206160
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # create an include_role task for test
    include_role = IncludeRole()
    # set the path of a playbook for test
    playbook_path = os.path.join(os.path.dirname(__file__), "../../playbooks/rolespec_validation.yml")
    # set the path of a role for test
    role_path = os.path.join(os.path.dirname(__file__), "../../playbooks/roles/role_with_bad_rolespec")
    # set the path of a role specification file for test
    rolespec_path = os.path.join(os.path.dirname(__file__), "../../playbooks/roles/role_with_bad_rolespec/meta/test_rolespec.yml")
    # set the path of a role definition

# Generated at 2022-06-13 09:07:36.873953
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:46.522263
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block = Block.load(dict(
        tasks=dict(
            include_role=dict(name='foo',
                              tasks_from='tasks/main.yml',
                              vars_from='vars/main.yml',
                              apply=dict(some_var=42)))))
    ir = IncludeRole.load(data=block.get_attributes(), block=block)
    assert ir.allow_duplicates is True
    assert ir.public is False
    assert ir.rolespec_validate is True
    assert ir._from_files['tasks'] == "main.yml"
    assert ir._from_files['vars'] == "main.yml"
    assert ir.apply == dict(some_var=42)

# Generated at 2022-06-13 09:07:56.405840
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # collect role data
    loader = DictDataLoader({
        'foo.yml': '''
        ---
        - name: testfoo
          block:
            - debug:
                msg: FOO
        ''',
        'bar.yml': '''
        ---
        - name: testbar
          block:
            - debug:
                msg: BAR
        ''',
    })
    variable_manager = VariableManager()
    playbook = Playbook.load('', variable_manager=variable_manager, loader=loader)
    role = Role.load('foo', loader=loader)
    role._role_path = 'foo'
    dep_chain = []
    role.compile(play=playbook, dep_chain=dep_chain)

    # create task and get block

# Generated at 2022-06-13 09:08:02.647322
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    role = Role()

    data = dict(
        name='test',
        foo='bar'
    )

    task = IncludeRole()
    task.load_data(data, variable_manager=None, loader=None)
    task._parent = role
    assert task.get_name() == 'test : test'

# Generated at 2022-06-13 09:08:03.284144
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:08:13.636440
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = {
        "include_role": {
            "name": "foo",
            "tasks_from": "tasks.yml"
        }
    }
    ir = IncludeRole.load(data)
    assert isinstance(ir._from_files, dict)
    assert ir._from_files == {'tasks': 'tasks.yml'}
    assert ir.name == 'foo'

    data = {
        "include_role": {
            "name": "foo",
            "tasks_from": "tasks.yml",
            "vars_from": "vars.yml"
        }
    }
    ir = IncludeRole.load(data)
    assert ir._from_files == {'tasks': 'tasks.yml', 'vars': 'vars.yml'}

# Generated at 2022-06-13 09:08:28.080162
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Play
    from ansible.playbook.play_context import PlayContext

    # Setup

# Generated at 2022-06-13 09:08:41.607135
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    task = TaskInclude(task_include=None)
    role = Role()
    block = Block()
    task_data = {}
    task_data['include'] = 'some_include'
    task_data['private'] = 'private'
    task_data['allow_duplicates'] = 'allow_duplicates'
    task_data['public'] = 'public'
    task_data['rolespec_validate'] = 'rolespec_validate'

    task_data['apply'] = {}
    task_data['apply']['tags'] = 'my-tags'
    task_data['apply']['always_run'] = 'always_run'
    task_data['apply']['become_enabled'] = 'become_enabled'

# Generated at 2022-06-13 09:09:47.884511
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    pass

# Generated at 2022-06-13 09:09:52.169521
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    block = Block()
    role = Role()
    task_include = TaskInclude()

    ir = IncludeRole(block, role, task_include=task_include)
    ir._role_name = 'test'

    assert ir.get_name() == "include_role : test"



# Generated at 2022-06-13 09:10:02.501573
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.six import PY3
    from ansible.plugins.loader import role_loader

    # initialize necessary data
    loader = DataLoader()
    # inventory = InventoryManager(loader=loader)
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # play_context = PlayContext()

    # initialize mock role
    role_path = C.DEFAULT_ROLES_PATH[0]
    role_name = 'mock-role'
    role_path_str = role

# Generated at 2022-06-13 09:10:11.482956
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    Test loading of a RoleInclude.
    '''

    args_dict = {'name': 'my_role', 'role': 'my_role', 'apply': {'list': [1, 2, 3], 'dict': {'k1': 'v1'}},
                 'tasks_file': 'tasks/main.yml', 'vars_file': 'vars/main.yml', 'defaults_file': 'vars/main.yml',
                 'handlers_file': 'handlers/main.yml'}
    data = [{'include_role': args_dict}]
    myir = IncludeRole.load(data[0]['include_role'])
    assert myir._role_name == args_dict['name']

# Generated at 2022-06-13 09:10:12.681429
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass



# Generated at 2022-06-13 09:10:25.368476
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext

    def role_load(data, block=None, role=None, task_include=None):
        return IncludeRole.load(data, block, role, task_include)

    def role_compile(self):
        # stub method out
        pass

    # -------------------------------------------------------------------------------
    # DUPLICATE BLOCKS
    # -------------------------------------------------------------------------------

    # NOTE: include_role does NOT inherit allow_duplicates from the play
    # this logic is only for _task_include and not for _block_include
    def test_play_allow_duplicates():
        data = dict(name='defaults')
        # play allow_duplicates=True
        p = Play().load(dict(name='play1', hosts='localhost', gather_facts='yes'))
        p.allow_du

# Generated at 2022-06-13 09:10:36.397880
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # include_roles
    ir = IncludeRole().load({'include_roles': {'role': 'common'}})
    assert ir.get_name() == 'include_role : common'

    ir = IncludeRole().load({'include_role': {'role': 'common'}})
    assert ir.get_name() == 'include_role : common'

    ir = IncludeRole().load({'include_roles': {'name': 'common'}})
    assert ir.get_name() == 'include_role : common'

    # import_roles
    ir = IncludeRole().load({'import_roles': {'role': 'common'}})
    assert ir.get_name() == 'import_role : common'

    ir = IncludeRole().load({'import_role': {'role': 'common'}})

# Generated at 2022-06-13 09:10:47.914334
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    inventory = InventoryManager(loader=loader, sources=['../../test/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create play with role
    play_source = dict(
        name="Ansible Play",
        hosts=['localhost'],
        gather_facts='no',
        roles=[dict(role1=dict(name="role1"))]
    )  # Gets

# Generated at 2022-06-13 09:10:56.832370
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import os
    import tempfile
    import ansible.constants as C
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleSequence
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager

    ir = None
    host = '127.0.0.1'
    path = os.path.realpath(__file__).replace('_test.py', '.yml')
    role_name = 'some_role'
    tqm = None
    pb = None
   

# Generated at 2022-06-13 09:11:00.793960
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole(block=dict(task=dict(args=dict(name='test_name'))))
    assert task.get_name() == 'test_name'

    task = IncludeRole(block=dict(task=dict(args=dict(role='test_name'))))
    assert task.get_name() == 'include_role : test_name'