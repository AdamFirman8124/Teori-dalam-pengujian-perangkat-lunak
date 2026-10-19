

# Generated at 2022-06-13 09:02:50.855219
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    block = Block(None)
    from ansible.playbook.task import Task
    task = Task()
    task._parent = block
    from ansible.playbook.play import Play
    play = Play()
    from ansible.playbook.role.definition import RoleDefinition
    role = RoleDefinition()
    role._play = play
    role._role_name = 'role_name'
    from ansible.playbook.role import Role
    parent_role = Role()
    parent_role._metadata = role
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager(loader=None)
    variable_manager.set_inventory(None)

# Generated at 2022-06-13 09:03:01.652682
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    '''
    Test for method get_include_params of class IncludeRole
    '''

    ir = IncludeRole()

    # role name is known only after load method has been called
    # but role name is needed to take the value of ansible_parent_role_name
    # needed this way because method get_include_params is called before
    # load method is called
    # when a include_role is used in apply block, ansible_parent_role_name variable
    # will be set to a empty list, so it is not enough to check if variable is set
    # but it is also needed to check if role name is the right value
    # when a include_role is used in a role, ansible_parent_role_name variable
    # will be set to a list with only one value of role name, so in this case
    # is it ok to

# Generated at 2022-06-13 09:03:11.265737
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Pretend to be an Ansible task
    include_role_task = IncludeRole()

    # Set it's attributes
    include_role_task._role_name = 'role_name'

    # Call get_block_list()
    result = include_role_task.get_block_list()

    # check the results
    assert(result[0][0].get_name() == 'tasks/main.yml')
    assert(result[0][1].get_name() == 'tasks/test.yml')
    assert(result[1][0].get_name() == 'handlers/main.yml')
    assert(result[1][1].get_name() == 'handlers/test.yml')


# Generated at 2022-06-13 09:03:18.630813
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    '''
    ParentRole does not have a get_role_params() method, testing for other conditions.
    '''

    class ParentRole:
        def __init__(self):
            self._role_path = None

        def get_name(self):
            return 'role1'

    parent_role = ParentRole()
    ir = IncludeRole(block=Block(), role=parent_role)
    assert ir.get_include_params() == {'ansible_parent_role_names': ['role1'], 'ansible_parent_role_paths': [None]}

# Generated at 2022-06-13 09:03:28.817499
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition

    # Test valid role includes
    data = {'name': 'name_1'}
    task = TaskInclude()
    role_definition = RoleDefinition()
    ir = IncludeRole.load(data, task_include=task, role=role_definition)
    assert isinstance(ir, IncludeRole)
    assert ir._from_files == {}
    assert ir.statically_loaded is False
    assert ir._role_name == 'name_1'
    assert ir._role_path is None

    data = {'role': 'name_1'}
    ir = IncludeRole.load(data, task_include=task, role=role_definition)
    assert ir._role_name == 'name_1'

    # Test missing required parameter name
    data = {}

# Generated at 2022-06-13 09:03:40.311186
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.task import Task
    mydata = {'role': 'testdata'}
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'play_hosts': {'hosts': 'localhost'}}
    variable_manager._options_vars = {'roles_path': '/etc/ansible/roles'}

# Generated at 2022-06-13 09:03:46.753123
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()
    include_role = IncludeRole(block, role)

    include_role.name = 'test task name'
    assert include_role.get_name() == 'test task name'

    include_role.name = None
    include_role.action = 'action'
    include_role._role_name = 'test role'
    assert include_role.get_name() == 'action : test role'

# Generated at 2022-06-13 09:03:56.064235
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()

    path = "/Users/vignesht/Downloads/test"
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        roles=[
            dict(
                name="test",
                rolespec_validate=True,
                apply="app/{% set w=7|float/3 %}",
                tasks_from="test1",
                vars_from="test2",
                defaults_from="test3",
                handlers_from="test4"

            )
        ]
    )

    variable_manager = VariableManager()
    variable_manager.set

# Generated at 2022-06-13 09:04:03.323238
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    C.HOST_KEY_CHECKING = False

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['./test/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play = Playbook.load('test/playbooks/include_role.yml', variable_manager=variable_manager, loader=loader)
    tqm = None


# Generated at 2022-06-13 09:04:13.118273
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.block
    block = ansible.playbook.block.Block()
    role = ansible.playbook.role.Role()

    role_path = './data/plans/roles'
    role_name = 'ksh/ksh-patch'

    # test with apply
    IncludeRole.load(
        block=block,
        role=role,
        data=dict(
            name=role_name,
            apply=dict(
                become=True
            )
        )
    )

    # test with from_files (tasks_from, vars_from, defaults_from and handlers_from)
    # we don't load the whole role since we don't need it

# Generated at 2022-06-13 09:04:29.356151
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    v = {
        'ansible_role_names': ['foo'],
        'ansible_role_paths': ['foo_role_path'],
    }

    class FakeRole():
        def get_role_params(self):
            return v

        def get_name(self):
            return 'ansible_role_names'

    fake_role = FakeRole()
    fake_role._role_path = 'foo_role_path'

    ir = IncludeRole()
    ir._parent_role = fake_role

    v = ir.get_include_params()

    assert v['ansible_role_names'][0] == 'foo'
    assert v['ansible_role_paths'][0] == 'foo_role_path'

# Generated at 2022-06-13 09:04:39.540678
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:04:50.410670
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Test with name=None, action='include_role', _role_name='RoleName'
    ir_1 = IncludeRole({'name': None, 'action': 'include_role', '_role_name': 'RoleName'})
    assert ir_1.get_name() == "include_role : RoleName"
   
    # Test with name='task name', action='include_role', _role_name=None
    ir_2 = IncludeRole({'name': 'task name', 'action': 'include_role', '_role_name': None})
    assert ir_2.get_name() == "task name"
   
    # Test with name='', action='import_role', _role_name=None
    ir_3 = IncludeRole({'name': '', 'action': 'import_role', '_role_name': None})

# Generated at 2022-06-13 09:04:57.121618
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole(block='block', role='role', task_include='task_include')

    # ir without name
    ir._role_name = 'rolename'
    name_without_name = ir.get_name()
    assert name_without_name == 'include_role : rolename'

    # ir with name and _parent_role with name
    ir.name = 'includerolename'
    ir._parent_role = Role()
    ir._parent_role.name = 'parentrolename'
    name_with_name = ir.get_name()
    assert name_with_name == 'includerolename'

    # ir without name and _parent_role without name
    ir.name = None
    ir._parent_role.name = None
    name_without_name_without_parent_name = ir

# Generated at 2022-06-13 09:05:06.481641
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # local action
    ir = IncludeRole(block=Block(), role=Role(), task_include=TaskInclude(block=Block(), task=Task(), action=None))
    ir.action = 'include_role'
    ir.args = {}
    ir.name = None
    ir._role_name = 'myrole'
    assert "include_role : myrole" == ir.get_name()
    # remote action
    ir = IncludeRole(block=Block(), role=Role(), task_include=TaskInclude(block=Block(), task=Task(), action='include_role'))
    ir.action = 'include_role'
    ir.args = {}
    ir.name = None
    ir._role_name = 'myrole'
    assert "include_role : myrole" == ir.get_name()
    # local action with name

# Generated at 2022-06-13 09:05:14.366005
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # Create a Role
    role_name = 'role_name'
    role_path = 'role_path'
    role = Role(name=role_name)
    role._role_path = role_path

    # Create an IncludeRole
    ir = IncludeRole(role=role)
    assert ir.get_include_params() == {'ansible_parent_role_names': [role_name], 'ansible_parent_role_paths': [role_path]}

# Generated at 2022-06-13 09:05:22.445114
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host, Group

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='localhost,')
    fake_playbook = dict(
        hosts='all',
        gather_facts='no',
        roles=[]
    )
    fake_variable_manager = VariableManager()
    fake_variable_manager.set_inventory(fake_inventory)

# Generated at 2022-06-13 09:05:31.277184
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    block = Block()
    role = Role()

    # include_role: a.b.c
    #   tasks_from: d.yml
    #   vars_from: e.yml
    #   defaults_from: f.yml
    #   handlers_from: g.yml

    task_include = IncludeRole(block=block, role=role)
    task_include.args = dict(role='a.b.c', tasks_from='d.yml', vars_from='e.yml', defaults_from='f.yml', handlers_from='g.yml')
    blocks = task_include.get_block_list(play=None)[0]

    for block in blocks:
        for task in block.block:
            print(task.action)


# Generated at 2022-06-13 09:05:43.391827
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import copy
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from io import StringIO


# Generated at 2022-06-13 09:05:44.158680
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:06:06.943879
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    # Some pre-requisites to create an IncludeRole object
    play_context = PlayContext()
    play_context._cur_context = 'include_role'
    playbook_loader = PlaybookExecutor()
    playbook_loader._tqm = TaskQueueManager(playbook_loader._inventory, playbook_loader._variable_manager, playbook_loader._loader, play_context, playbook_loader._options)
    playbook_loader._tqm._final_q = playbook_loader._tqm.get_initial_queue()

# Generated at 2022-06-13 09:06:21.348117
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    # Dummy play and tasks variables
    play_source = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [
            dict(
                role = 'test.role1'
            ),
            dict(
                include_role = dict(
                    name = 'test.role2'
                )
            )
        ]
    )
    play = Play().load

# Generated at 2022-06-13 09:06:33.504986
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    module_name = 'include_role'
    assert IncludeRole.load is not None, "%s class needs a load method" % module_name

    # make an instance without parent object
    context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()
    ir = IncludeRole()

    # make an instance with a parent object
    parent_block = Block()
    context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()
    ir = IncludeRole(block=parent_block)

# Generated at 2022-06-13 09:06:41.986780
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    # Create a test play
    pb = Play()
    pb.vars = dict()

    # Create a test role
    r = Role()

    # Create a test block
    b = Block()

    # Create a task include instance to test
    t = IncludeRole(block=b, role=r)

    # Testing load function
    t.load_data(dict(name='test rolespec', apply={'tags': ['tag1', 'tag2']}), variable_manager=None, loader=None)
    assert t._role_name == 'test rolespec'
    assert t.name == 'test rolespec'
    assert t.statically_loaded is True

# Generated at 2022-06-13 09:06:52.958325
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    mock_data = dict(
        name='test',
        apply=dict(
            ignore_errors=True,
            roles='test2',
            tasks='test3'
        ),
        tasks_from='test4',
        vars_from='test5',
        defaults_from='test6',
        handlers_from='test7',
        public=True,
        allow_duplicates=False,
        rolespec_validate=False,
        tags=['tag1', 'tag2'],
    )

    actual_result = IncludeRole.load(mock_data, block=Block(), task_include=Task())
    assert 'test' == actual_

# Generated at 2022-06-13 09:07:04.407504
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test case 1
    data = dict(
        action='include_role',
        args=dict(
            name='include_role_test',
            tasks_from='/root/ansible/test/roles/include_role_test/tasks/main.yml',
            vars_from='/root/ansible/test/roles/include_role_test/vars/main.yml',
            defaults_from='/root/ansible/test/roles/include_role_test/defaults/main.yml',
            handlers_from='/root/ansible/test/roles/include_role_test/handlers/main.yml',
            public=True,
            tags=['include_role_test'],
        ),
    )

# Generated at 2022-06-13 09:07:11.838741
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.role_include import load_role_definition

    # test without name
    ic = IncludeRole(role=load_role_definition("web", "tasks/main.yml", "/home/somebody/roles/web/"))
    assert ic.get_name() == "include_role: web"

    # test with name
    ic.name = "web include"
    assert ic.get_name() == "web include"


# Generated at 2022-06-13 09:07:19.956986
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    myplay = Play()
    myplay.vars = {'myvar':'myvarvalue'}
    myplay.basedir = 'testdir'
    myplay.collections = []
    myplay.roles = []
    myplay.tasks = []
    myplay.handlers = []

    myrole = Role()
    myrole.name = 'testrole'
    myrole._tasks = []
    myrole._handlers = []
    myrole._role_path = 'testdir'
    myrole._metadata = {}
    myrole._metadata['allow_duplicates'] = True

    task = Task()
    task.name = 'mytask'
    task.when = 'myvar == myvarvalue'
    task.action = 'myaction'

    myrole._tasks = [task]

    ir

# Generated at 2022-06-13 09:07:31.112884
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # defining a class of local variable
    class locals():
        pass

    # create variable to use in test
    variable_manager = dict()
    variable_manager['vars'] = dict()
    variable_manager['defaults'] = dict()

    loader = dict()
    loader['path_loader'] = dict()
    loader['path_loader']['searchpath'] = "/etc/ansible/roles"

    myplay = dict()
    myplay['roles'] = list()

    # test 1
    # define variables for test
    data = dict()
    data['name'] = 'name'
    data['action'] = "action"
    data['block'] = None
    data['role'] = None
    data['loader'] = None
    data['variable_manager'] = None
    data['task_include'] = None
   

# Generated at 2022-06-13 09:07:37.107099
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # simple test to verify we can run get_block_list
    # with minimal args
    ir = IncludeRole()
    
    ir.args = dict(
        name='test_role',
        apply=dict()
    )
    ir._role_name = 'test_role'
    
    ir._parent = Block(parent_block=None, role=None)
    ir.get_block_list()

# Generated at 2022-06-13 09:07:58.856681
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    class TestVars(object):
        def __init__(self):
            self.vars = {}
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    myvars = TestVars()

    display.verbosity = 3
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory(host_list='tests/hosts'))
    variable_manager.set_vars(myvars.vars)

    # Setup

# Generated at 2022-06-13 09:08:09.949577
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.play_context
    import ansible.vars.manager
    import ansible.template.template
    import ansible.utils.vars
    import ansible.inventory.host
    import ansible.parsing.dataloader

    variable_manager = ansible.vars.manager.VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._fact_cache_file = None
    variable_manager._fact_cache_type = 1

    loader = ansible.parsing.dataloader.DataLoader()
    loader.set_basedir('/tmp')

    play_context = ansible.playbook.play_context.PlayContext()
    play_context.remote_addr = "127.0.0.1"
    play_context.connection = "local"


# Generated at 2022-06-13 09:08:17.125525
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.errors import AnsibleParserError
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    inventory = InventoryManager(loader=DataLoader(), sources=['localhost'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()


# Generated at 2022-06-13 09:08:23.233613
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Load a small block of YAML into a data structure.

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    block_YAML = """
- include_role:
    name: include_role_test
    apply:
      tags:
        - include_role_test_tag
    vars:
      variable_included_into_role: variable_included_into_role
"""

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.mod_args import ModuleArgsParser

# Generated at 2022-06-13 09:08:36.682871
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    Test to ensure that the IncludeRole.get_block_list() static method works as expected.
    '''
    from ansible.playbook import Play
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    # Create an instance of the IncludeRole class
    include_role = IncludeRole()

    # Create a new role
    role = Role()

    # Set the _parent variable of our include_role class
    include_role._parent = role

    # Set the _play variable of our role variable
    role._play = Play()

    # Set the inventory variable of our role variable

# Generated at 2022-06-13 09:08:40.014151
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    #include_role_obj = IncludeRole()
    #block_list = include_role_obj.get_block_list()
    pass

# Generated at 2022-06-13 09:08:47.154673
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    """
    Unit test for method get_name of class IncludeRole
    """
    # initialize a IncludeRole class
    ir = IncludeRole()

    ir.name = "task name"
    ir._role_name = "role name"

    assert ir.get_name() == "task name"

    ir.action = "include"
    ir.name = None

    assert ir.get_name() == "include : role name"


# Generated at 2022-06-13 09:08:58.544845
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    print('>>> IncludeRole.load (valid)')
    role = Role()
    ir_load = IncludeRole.load({'name': 'foo', 'tasks_from': 'bar'}, role=role)
    assert ir_load._from_files['tasks'] == 'bar'
    assert ir_load._parent_role is role
    assert ir_load._role_name == 'foo'
    assert ir_load._role_path is None
    assert ir_load.statically_loaded is False

    # using 'role' alias for name
    ir_load = IncludeRole.load({'role': 'foo', 'tasks_from': 'bar'}, role=role)
    assert ir_load._role_name == 'foo'

    print('>>> IncludeRole.load (invalid)')

# Generated at 2022-06-13 09:09:00.426861
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    assert IncludeRole.load({'name':'test_role'})

# Generated at 2022-06-13 09:09:09.352927
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    invalid_scenarios = [
        {},
        {'role': 'mjumbe.wakanda'},
        {'include_tasks': 'tasks/main.yml'},
        {'include_vars': 'vars/main.yml'},
    ]

# Generated at 2022-06-13 09:09:42.632945
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    print("Test get_block_list")
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources="localhost")
    variable_manager = VariableManager(loader=loader, inventory=inv)
    tqm = TaskQueueManager(
        inventory=inv,
        variable_manager=variable_manager,
        loader=loader,
        passwords={}
    )
    filename = 'test_files/test.yml'

# Generated at 2022-06-13 09:09:54.531579
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Create a fake args dict
    args = dict(include_role="test")
    # Create a fake blocks
    blocks = [Block(
        parent=None,  # noqa: E741
        role=None,  # noqa: E741
        task_include=None,  # noqa: E741
        always=None,  # noqa: E741
        delegate_to=None,  # noqa: E741
        run_once=None,  # noqa: E741
        loop=None,  # noqa: E741
        loop_args=None,  # noqa: E741
    )]
    # Create a fake block

# Generated at 2022-06-13 09:10:00.157098
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    """
    Return the name of the task with apply_filters
    """
    ir = IncludeRole()
    ir.action = 'include_role'
    ir.name = 'task1'

    ir._parent = Mock()
    ir._parent._play = Mock()
    ir._parent._play.ROLE_CACHE = Mock()

    assert ir.get_name() == "task1"


# Generated at 2022-06-13 09:10:07.972006
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Create a host
    host = Host(name="localhost")

    # Create a play
    play = Play()
    play.set_loader(DictDataLoader())

    # Create a block of task and play
    play_block = Block( parent_block=play)

    # Create a task named test_task
    task_include = IncludeRole(parent_block=play_block)

    # Create a list of data
    data = [{'include_role': 'test_role'},{'name': 'test_role'}]

    # Create a task loader
    loader = DataLoader()

    # Create a variable manager
    variable_manager = VariableManager()

    # Create a role
    role = Role()

    # Test the method load()

# Generated at 2022-06-13 09:10:22.457317
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    import ansible.constants as C
    import os
    display = Display()

    # a.b.yml
    file_name1 = os.path.join(C.DEFAULT_LOCAL_TMP, 'a.b.yml')
    file1 = '''
    - debug: msg="vars from a.b.yml"
    '''

    # b.yml
    file_name2 = os.path.join(C.DEFAULT_LOCAL_TMP, 'b.yml')

# Generated at 2022-06-13 09:10:34.167236
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook import Play
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.vars.manager import VariableManager

    play_context = Play().set_variable_manager(VariableManager())

    # role_path is mocked but we need a non-empty path
    temp_dir = AnsibleModuleTest.tempdir()
    role_path = temp_dir.path + '/some/role/path'

    # Not a real role but these are attribute we need
    role = Role()
    role.get_name = lambda: "some-role"
    role.get_role_params = lambda: {'blah': 'boo'}
    role._role_path = role_path
    role._role_params = {'blah': 'boo'}

# Generated at 2022-06-13 09:10:45.280842
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.task_include import TaskInclude

    data = dict(
        name='some_role',
        tasks_from='a_tasks_file',
        vars_from='a_vars_file',
        defaults_from='a_defaults_file',
        handlers_from='a_handlers_file',
        allow_duplicates=False,
        public=True,
        apply=dict(
            block='',
            filters=dict(
                key1='key1',
                key2='key2'
            )
        )
    )

    # Test all valid keys
    IncludeRole.load(data)

    # Test invalid key
    data['invalid_key'] = 'invalid_key'

# Generated at 2022-06-13 09:10:52.112062
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    ir = IncludeRole.load(dict(action='include_role', name='foo'), block=Block())
    assert isinstance(ir, IncludeRole)

    # dictionary conversion of this object
    rep = ir.get_data()

    assert 'static' in rep
    assert rep['static'] is True

    ir = IncludeRole.load(dict(action='include_role', name='foo', static=False), block=Block())

    # dictionary conversion of this object
    rep = ir.get_data()

    assert 'static' in rep
    assert rep['static'] is False

# Generated at 2022-06-13 09:10:53.698939
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass


# Generated at 2022-06-13 09:11:00.920332
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition

    res = IncludeRole.load(dict(name="test_role"), block=Block(), role=RoleDefinition())
    assert isinstance(res, IncludeRole)

    try:  # load a IncludeRole without name
        res = IncludeRole.load(dict(role="test_role"), block=Block(), role=RoleDefinition())
        assert False  # IncludeRole.load must throw a AnsibleParserError exception in this case
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 09:11:53.644610
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''Unit test for method load of class IncludeRole'''

    return



# Generated at 2022-06-13 09:12:03.417677
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # Base class is a RoleDefinition
    assert issubclass(IncludeRole, RoleDefinition)

    # role is the combination of RoleDefinition and RoleMetadata
    r = RoleDefinition()
    r._role_name = 'common'
    r._role_path = '/test/common/'
    r._metadata = RoleMetadata()

    # block is a Block
    b = Block()
    b._

# Generated at 2022-06-13 09:12:07.596912
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    action = 'include_role'
    data = {'name': 'test', 'private': True, 'apply': {'test_attr': 'yes'}}
    role = Role()
    ir = IncludeRole.load(data, role=role)
    assert isinstance(ir, IncludeRole)
    assert isinstance(ir.role, Role)
    assert ir.name == 'test'
    assert ir.private is True
    assert ir.apply == {'test_attr': 'yes'}

# Generated at 2022-06-13 09:12:09.983213
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
	import pdb
	pdb.set_trace()
	pass

# Generated at 2022-06-13 09:12:20.795398
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    task_include = TaskInclude()
    role = Role()
    task_include.set_loader(role._loader)

    # test with our without name parameter
    for name in (None, 'foo'):
        ir = IncludeRole(task_include=task_include, role=role)
        ir.name = name
        ir._role_name = 'role_name'
        assert ir.get_name() == "include_role : role_name"
        assert ir.get_name() == ir._task.get_name()

    # test with our without action parameter
    for action in (None, 'action'):
        ir = IncludeRole(task_include=task_include, role=role)
        ir.name = None
        ir._role_name = 'role_name'
        ir.action = action
        assert ir.get

# Generated at 2022-06-13 09:12:22.166588
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''Unit test for method load of class IncludeRole'''

    # TODO: implement test
    pass


# Generated at 2022-06-13 09:12:32.643431
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    data = dict(
        name="test1",
        tasks_from="tasks1.yml",
        vars_from="vars1.yml",
        defaults_from="defaults1.yml",
        handlers_from="handlers1.yml",
        public="yes",
        allow_duplicates="no",
        rolespec_validate="no")

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=None, sources='./tests/utils/inventory'))
