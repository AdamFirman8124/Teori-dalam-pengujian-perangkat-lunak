

# Generated at 2022-06-13 09:02:50.309606
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    import os
    import sys

    my_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(my_dir, 'data')

    # load up a test play
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    pbex = PlaybookExecutor(playbooks = [os.path.join(data_dir, 'playbook.yml')], inventory = os.path.join(data_dir, 'hosts'), variable_manager = None, loader = None, passwords = None)
    pbex._tqm._stdout_callback = None
    pbex._tqm._stdout_callback = None
    pbex._tqm.send_callback = None

# Generated at 2022-06-13 09:03:01.093064
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude

    dummy_loader = None
    dummy_variable_manager = None
    dummy_play = Play().load({}, loader=dummy_loader, variable_manager=dummy_variable_manager)
    dummy_role_name = 'dummy_role'
    dummy_role_path = 'dummy_role_path'
    dummy_new_blocks = [Block(name='dummy_block')]

    # Execute the code to be tested.
    def monkeypatch(original, myrole):
        original.RoleInclude.load = lambda name, play, dep_chain, variable_manager=None, loader=None: myrole

# Generated at 2022-06-13 09:03:11.421498
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    # load the given role (the content test is not needed as it's tested in a specific unit test)
    path_to_role = 'lib/ansible/roles/test_role'

    # create a dummy play to get the variable_manager and loader
    hosts = ["my_host"]
    myplay = Play().load({}, variable_manager=VariableManager(), loader=DataLoader())
    myplay.hosts = hosts
    myplay.inventory = InventoryManager()
    myplay.inventory.set_playbook_basedir("/tmp")
    myplay.inventory.add

# Generated at 2022-06-13 09:03:21.123710
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager, version_info=C.DEFAULT_ANSIBLE_VERSION_INFO)
    play_context = PlayContext()
    queue_manager = TaskQueueManager(inventory=inv_manager, variable_manager=variable_manager, loader=loader, options=play_context, passwords={})



# Generated at 2022-06-13 09:03:30.307128
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    class MockRole(object):
        def get_name(self):
            return 'name'

        def get_role_params(self):
            return {"key1": "value1", "key2": "value2"}

    class MockBlock(object):
        def __init__(self):
            self._role = MockRole()

    mockblock = MockBlock()
    includerole = IncludeRole(block=mockblock)

    expected_result = {"key1": "value1", "key2": "value2", 'ansible_parent_role_names': ['name'], 'ansible_parent_role_paths': []}
    result = includerole.get_include_params()

    assert result == expected_result

# Generated at 2022-06-13 09:03:36.073533
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Input data for testing
    data = dict(
        name = 'some-role',
        tasks_from = './tasks/main.yml',
        vars_from = './vars/main.yml',
        handlers_from = './handlers/main.yml',
        public = True,
        allow_duplicates = False,
        rolespec_validate = False,
        apply = dict(
            force_handlers = True,
            limit = 'nodes',
        )
    )

    # Unit test - must call load method of class IncludeRole and assert if is instance of class IncludeRole
    include_role = IncludeRole.load(data)
    assert isinstance(include_role, IncludeRole)

    # Unit test - must call load method of class IncludeRole with invalid config and assert exception

# Generated at 2022-06-13 09:03:47.793645
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    playbook = Play()
    playbook.vars = dict(
        a_var=dict(
            b_var=dict(
                c_var=dict(
                    d_var='a',
                    e_var='b'
                )
            )
        )
    )
    role = Role()
    role.vars = dict(
        a_var=dict(
            b_var=dict(
                c_var=dict(
                    d_var='c',
                    e_var='d'
                )
            ),
            f_var=dict(
                g_var=dict(
                    h_var=dict(
                        i_var='i'
                    )
                )
            )
        )
    )


# Generated at 2022-06-13 09:03:56.790783
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play import Play

    from ansible.playbook.role.definition import RoleDefinition

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import MockVarsModule

    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role

    loader = DictDataLoader({
        "/the/path/bar.yaml": """
a: 1
b: 2
        """
    })

    variable_manager = MockVarsModule()

# Generated at 2022-06-13 09:04:00.664923
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    #Create a Include Role Class instance
    ir = IncludeRole.load(dict(role="my_custom_role"))

    #Create a fake Block to pass as a parent block
    fake_block = Block()

    #Test whether the method get_block_list of class IncludeRole returns a list of Blocks
    assert ir.get_block_list(block=fake_block) == ([], [])

# Generated at 2022-06-13 09:04:11.731230
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load({
            'name': 'test',
            'hosts': 'all',
            'vars': {},
            'tasks': [
                {'name': 'test',
                 'include_role': {'name': 'test'},
                }
            ]
        }, loader=loader, variable_manager=variable_manager)

    block = play.get_block_list()[0]
    task = block.get_task_list()[0]
    ir = task.copy()

    # test without passing in any variables

# Generated at 2022-06-13 09:04:39.570052
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:04:50.476903
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # First, test with a simple dictionary, without a variable_manager or loader.
    example = {'name': 'some_role', 'apply': {}}
    ir = IncludeRole.load(example)
    assert ir._role_name == 'some_role'
    assert ir.apply == {}
    assert ir._from_files == {}

    # And with a dangerious option ('foo').
    try:
        example['foo'] = 'bar'
        ir = IncludeRole.load(example)
        assert False
    except AnsibleParserError:
        pass

    # And with a bad option ('tasks_from').
    try:
        del example['foo']
        example['tasks_from'] = []
        ir = IncludeRole.load(example)
        assert False
    except AnsibleParserError:
        pass

    # And with a

# Generated at 2022-06-13 09:04:59.970480
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    f = open("tests/playbooks/include_role_test.yaml")
    playbook = Playbook.load(f, variable_manager=variable_manager, loader=loader)
    play = playbook.get_plays()[0]
    block = play.get_block_list()[0]


# Generated at 2022-06-13 09:05:10.803790
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.playbook.block as block
    import ansible.playbook.task as task
    import ansible.playbook.play_context as play_context
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager

    # 1. Rolespec without "BASE" section

    # 1.1. without blocks
    include_role = IncludeRole()
    include_role._role_name = "some_role"

    context = play_context.PlayContext()
    play = Play().load({}, variable_manager=VariableManager(), loader=None)

    blocks, handlers = include_role.get_block_list(play=play, variable_manager=None, loader=None)
    assert not blocks and not handlers

    # 1.2. with one block
    include_role = IncludeRole()
   

# Generated at 2022-06-13 09:05:19.790680
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.errors import AnsibleAssertionError
    import ansible.constants as C

    # Make a fake play whose tasks list will be reassigned to the new tasks list
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])

# Generated at 2022-06-13 09:05:28.898327
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    :param IncludeRole
    check:
        -validate options
        -role name (name ot role)
        -validate bad options
        -build options for role includes
        -apply (dict)
        -manual list as otherwise the options would set other task parameters we don't want.
    :return:
    '''

    ir=IncludeRole()
    ir._role_name=u'role1'
    ir.args={u'name': u'role1'}
    assert ir.args=={u'name': u'role1'}

    ir.args={u'name':u'role'}
    ir._role_name=ir.args.get('name', ir.args.get('role'))
    assert ir._role_name==u'role'


# Generated at 2022-06-13 09:05:29.908638
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:05:41.878587
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import tempfile
    import os
    import shutil
    import sys
    import imp
    from ansible.module_utils._text import to_bytes

    galaxy_path = tempfile.mkdtemp(prefix='ansible_galaxy_for_unittests')
    paths = [galaxy_path]
    role_path = tempfile.mkdtemp(prefix='ansible_role_for_unittests', dir=galaxy_path)
    name = 'foo'
    path = os.path.join(role_path, name)
    os.mkdir(path)
    os.mkdir(os.path.join(path, 'tasks'))

    task_path = os.path.join(path, 'tasks', 'main.yml')

# Generated at 2022-06-13 09:05:51.911916
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import os

    # pylint: disable=too-many-nested-blocks, too-many-statements, too-many-locals, too-many-branches
    # pylint: disable=too-many-arguments, too-many-instance-attributes

    import pytest
    from ansible.utils.path import unfrackpath
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    from ansible.module_utils._text import to_text

    # create a test role in a temporary directory

# Generated at 2022-06-13 09:06:04.052989
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Set up mock Block
    import ansible.playbook.block
    block = ansible.playbook.block.Block()
    tasks = []
    block.block = tasks
    block.role = None

    # Set up mock TaskInclude
    import ansible.playbook.task_include
    import ansible.playbook.role
    role = ansible.playbook.role.Role()
    role._metadata = {}
    task_include = ansible.playbook.task_include.TaskInclude()
    task_include._parent = block
    task_include._role = role
    task_include.vars = {}
    task_include.args = {}
    data = {}
    task_include.load_data(data)

    # Populate IncludeRole object ir

# Generated at 2022-06-13 09:06:17.406889
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    test_obj = IncludeRole()
    result = test_obj.get_include_params()
    assert not result

# Generated at 2022-06-13 09:06:22.497782
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(
        role_path=dict(
            role_name='role_name',
            role_vars_path='role_vars_path'
        )
    )

    loader = None
    play_context = PlayContext()
    play = Play()

    ir = IncludeRole()
    result = ir.get_block_list(play=play, variable_manager=variable_manager, loader=loader)

    assert result[0].get_vars()['role_name'] == 'role_name'
    assert result[0].get_vars()['role_vars_path']

# Generated at 2022-06-13 09:06:35.117059
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    include_role = IncludeRole()
    assert not include_role._allow_duplicates
    assert not include_role._public
    assert include_role._rolespec_validate

    require_args = dict(
        role='base'
    )
    require_role = IncludeRole().load(dict(action='include_role', **require_args))
    assert require_role._role_name == require_args['role']
    assert require_role._allow_duplicates
    assert not require_role._public
    assert require_role._rolespec_validate

    require_args = dict(
        role='base',
        _allow_duplicates='no'
    )
    require_role = IncludeRole().load(dict(action='include_role', **require_args))
    assert require_role._role_name == require

# Generated at 2022-06-13 09:06:39.094463
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole(None)
    task.name = "my-name"
    task._role_name = "my-role-name"
    assert task.get_name() == "my-name : my-role-name"


# Generated at 2022-06-13 09:06:50.780727
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.playbook
    import ansible.playbook.role
    from units.mock.loader import DictDataLoader


    # prepare mock data
    data = dict(
        hosts='all',
        name='mockinclude',
        gather_facts='no',
        tasks=[
            {'include_role': {'name': 'mockrole',
                              'extra_vars': {'foo': 'bar'},
                              'tasks_from': 'main.yml',
                              'apply': {'ignore_errors': True}
                              }
             }
        ],
    )

    # prepare mock role

# Generated at 2022-06-13 09:06:54.194258
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
  _test_get_block_list: simulate a call the get_block_list method of the class IncludeRole

  Parameters: none
  
  Returns: nothing
  """
    # Set up objects and mocks needed for this unit test
    # ...
    # Do the test
    # ...

# Generated at 2022-06-13 09:07:05.270862
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # arrange
    class MockParentRole():
        def __init__(self):
            self._role_name = 'parent_role_name'
            self._role_path = 'parent_role_path'
            self.get_role_params = lambda : {'key':'value'}
            self.get_name = lambda : self._role_name
    role = IncludeRole()
    role._parent_role = MockParentRole()
    # add some params to the IncludeRole
    role.vars = {'key':'value'}
    # act
    result = role.get_include_params()
    # assert
    assert result['key'] == 'value'
    assert result['ansible_parent_role_names'] == ['parent_role_name']

# Generated at 2022-06-13 09:07:15.805601
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook import Play
    from ansible.playbook.play import Play as pl
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    data = {}
    block = Block()
    role = Role()
    task_include = Task()
    play = Play()
    play.hosts = "localhosst"

    ir = IncludeRole(block=block, role=role, task_include=task_include)
    ir.vars = {}
    ir.args = {}
    ir.collections = {}
    blocks, handlers = ir.get_block_list(play=play)
    assert isinstance(blocks, list), "Blocks: %r is not of type list" % blocks

# Generated at 2022-06-13 09:07:17.353581
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    role = IncludeRole.load({})
    assert role.name is None

# Generated at 2022-06-13 09:07:17.979911
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:53.367106
# Unit test for method get_block_list of class IncludeRole

# Generated at 2022-06-13 09:08:01.142837
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.template import Templar
    from ansible.vars.reserved import Reserved

    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'gather_facts': False,
        'roles': [
            {'role': 'includerole_role'}
        ]
    }, variable_manager=None, loader=None)
    play_context = PlayContext()

# Generated at 2022-06-13 09:08:11.835378
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    import os
    import sys

    _blocks = [
        {
            'name': 'main',
            'block': [
                {'include_role': {'name': 'foo', 'apply': {'vars': {'foo_var1': 'foo_var1_value'}}}}
            ]
        }
    ]

    include_role_obj = IncludeRole.load({'include_role': {'name': 'foo', 'apply': {'vars': {'foo_var1': 'foo_var1_value'}}}}, block=Block.load(block=_blocks[0], role=None))
    assert include_role_obj.get_include_params()['ansible_role_name'] == 'foo'

# Generated at 2022-06-13 09:08:26.243596
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    play_context = PlayContext()
    role_path = os.path.join(os.path.dirname(__file__), 'data/test_include_role_data/')
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
    blocks = None

    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        roles = role_path,
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='{{ foo }}')))
        ]
    )

    # Test with invalid include_role syntax
    task = [dict(include_role=dict(name='foo'))]


# Generated at 2022-06-13 09:08:26.934639
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:08:39.723986
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Test load method of IncludeRole class
    """
    # setup
    data = {
        'name': 'include_role_module',
        'include_role': 'include_role_module',
        'include': 'include_module'
    }
    include_role = IncludeRole(block=None, role=None, task_include=None).load_data(data)
    # test
    assert include_role._role_name == 'include_role_module'
    assert include_role._parent.get_name() == 'include_role_module : include_module'
    assert include_role._block._name == 'include_module'
    assert include_role._block._parent.get_name() == 'include_role_module : include_module'


# Generated at 2022-06-13 09:08:50.784592
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    host = Host(name='test_host_name')
    host.set_variable('inventory_hostname', 'test_host_name')

# Generated at 2022-06-13 09:09:02.934307
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from units.mock.loader import DictDataLoader

    # Test data
    data1 = dict(
        name="test1",
        tasks=[
            dict(include_role=dict(name="role1"), name="task1"),
            dict(include_role=dict(name="role2"), name="task2")
        ]
    )

    data2 = dict(
        name="test2",
        tasks=[
            dict(include_role=dict(name="role3"), name="task3")
        ]
    )

    # Prepare fake loader

# Generated at 2022-06-13 09:09:10.533841
# Unit test for method get_block_list of class IncludeRole

# Generated at 2022-06-13 09:09:19.567624
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    mock_loader = {
        '_basedirs': ['test/test_roles/role_a'],
        '_load_name_to_path': {'role_a': 'test/test_roles/role_a'},
        '_get_directory_name': 'role_a'
    }
    data = {
        'name': 'include_role_test',
        'include_role': 'role_a',
        'vars': {'include_var': 1}
    }
    include_role = IncludeRole.load(data, loader=mock_loader)
    blocks, handlers = include_role.get_block_list()
    assert(len(blocks) == 4)
    assert(blocks[0].module_name == 'include_role')

# Generated at 2022-06-13 09:10:22.463827
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    # Test with name and action
    data = dict(
        name='foo.yml',
        action='include_role',
    )

    include = IncludeRole.load(
        data=data,
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )
    assert include.get_name() == 'foo.yml : foo.yml'

    # Test with name but no action
    data = dict(
        name='foo.yml',
        action='import_role',
    )

    include = IncludeRole.load(
        data=data,
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )
    assert include.get_name

# Generated at 2022-06-13 09:10:34.166707
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.module_utils.six as six
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    tqm = None
    play = DummyPlay()
    templar = Templar(loader=loader, variables=play.get_variable_manager().get_vars(play=play))
    #test test_name
    path = '/home/users/roles/role1'
    task = IncludeRole(loader=loader, play=play, role=DummyRole(path=path))
    play.roles = [task]
    task.name = 'test_name'

# Generated at 2022-06-13 09:10:41.290778
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block(play=None)
    role = Role()
    role.name = "test role"
    role.action = "include_role"
    task_include = TaskInclude()
    ir = IncludeRole(block=block, role=role, task_include=task_include)
    ir.name = None
    ir.action = "include_role"
    ir._role_name = "new role"
    assert ir.get_name() == "include_role : new role"


# Generated at 2022-06-13 09:10:51.912720
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import include_role_loader, include_tasks_loader, lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    import ansible.constants as C
    import copy
    import os

    # Some default variables
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Generated at 2022-06-13 09:10:52.266236
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    assert False

# Generated at 2022-06-13 09:11:02.938007
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition

    # Instantiate a role definition
    rdef = RoleDefinition()

    # Create data to feed to method load
    data = {'name': 'test include role'}

    # Test the load method without rdef
    # Test expected result is different from actual result
    actual_result = IncludeRole.load(data)
    expected_result = IncludeRole(role=None, task_include=None)
    expected_result.name = 'test include role'
    expected_result._role_name = 'test include role'
    if actual_result == expected_result:
        assert False

    # Test the load method with rdef
    # Test expected result is different from actual result
    actual_result = IncludeRole.load(data, role=rdef)

# Generated at 2022-06-13 09:11:14.748973
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class FakeBlock:
        def __init__(self, name):
            self.name = name
            self._parent = None

    class FakeParentRole:
        def __init__(self, name):
            self.name = name
            self._parents = []

    class FakeTask:
        def __init__(self, name):
            self.name = name


    class FakePlay:
        def __init__(self, name):
            self.handlers = []
            self.roles = []
            self.name = name

    class FakeVariableManager:
        def get_vars(self, play, task):
            return {}

    class FakeLoader:
        def get_basedir(self):
            return "/some/path"

    # Test with fake parent role
    fr = FakeRole(name="fake_parent")
   

# Generated at 2022-06-13 09:11:19.417339
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    ####################################################################################################################
    # Test for load method with normal args
    ####################################################################################################################

    # Test with normal args
    data_normal = {
        u'include_role': {
            'name': 'bar',
            'allow_duplicates': False,
            'apply': {
                'tags': 'role-bar'
            },
            'become': True
        }
    }
    block_normal = Block()
    role_normal = Role()
    task_include_normal = TaskInclude()
    variable_manager_normal = VariableManager()
    loader_

# Generated at 2022-06-13 09:11:23.064260
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    t1 = IncludeRole.load(dict(name='foo.yml'))
    assert t1._role_name == 'foo.yml'
    t1 = IncludeRole.load(dict(role='foo.yml'))
    assert t1._role_name == 'foo.yml'


# Generated at 2022-06-13 09:11:33.551112
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    def __test(action, data, expected):
        try:
            IncludeRole.load(data, action=action)
        except Exception as e:
            found = type(e)
        else:
            found = 'OK'
        assert(expected == found)

    # invalid options
    __test('test action', {'invalid': 'OK'}, AnsibleParserError)
    __test('test action', {'name': 'test', 'invalid': 'OK'}, AnsibleParserError)

    # name is needed
    __test('test action', {}, AnsibleParserError)

    # name and role are aliases
    __test('test action', {'name': 'test'}, 'OK')
    __test('test action', {'role': 'test'}, 'OK')

    # only name is accepted for this action