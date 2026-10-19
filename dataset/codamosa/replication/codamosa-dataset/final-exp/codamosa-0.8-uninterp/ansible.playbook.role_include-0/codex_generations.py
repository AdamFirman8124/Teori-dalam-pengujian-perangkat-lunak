

# Generated at 2022-06-13 09:02:59.119411
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # [TEST: IncludeRole.get_block_list]
   print("------------------------------------------------")
   print("------------------------------------------------")
   print("[TEST: IncludeRole.get_block_list]")
   print("------------------------------------------------")

   from ansible.playbook.play_context import PlayContext
   from ansible.playbook.play import Play
   from ansible.template import Templar

   play_context = PlayContext()
   play_context._play_context_variables = dict()


# Generated at 2022-06-13 09:03:08.131584
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    test_task = dict(
        name="test_role_1",
        role="test_role_2",
        tasks_from="tasks/main.yml",
        handlers_from="handlers/main.yml",
        vars_from="vars/main.yml",
        defaults_from="defaults/main.yml",
        apply=dict(
            ignore_errors=True
        ),
        public=True,
        allow_duplicates=False,
        rolespec_validate=False
    )
    test_IncludeRole = IncludeRole.load(test_task)
    assert test_IncludeRole._role_name == "test_role_2"

# Generated at 2022-06-13 09:03:19.261787
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ast
    import re

    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    modules = ['test_IncludeRole_get_block_list.py']

    # Defined statically include_role object
    include_role._from_files = {'vars': 'test1'}
    include_role.statically_loaded = True
    include_role._parent_role = role
    include_role._role_name = 'testname'
    include_role._role_path = 'testpath'

    # copy include_role and test copy
    assert include_role.copy() == include_role

    # add player, loader, variable_manager

# Generated at 2022-06-13 09:03:20.510191
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    print(IncludeRole.load({'name': 'foo'}))

# Generated at 2022-06-13 09:03:26.551819
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Thoroughly test get_block_list

    # Test get_block_list when the role is statically loaded
    block = Block(role='foo')

    # Create IncludeRole object
    include_role = IncludeRole(block)
    include_role._role_name = 'test_role'
    include_role.statically_loaded = True
    include_role._parent = block

    # Test when role is found
    mock_role = MockRole('test_role')
    mock_role._metadata = MockRoleMetadata()
    mock_role._metadata.allow_duplicates = True
    mock_role.has_tasks = True
    mock_role._parent_role = None
    mock_role._role_path = 'test_role_path'
    mock_role._role_name = 'test_role'
    mock_role

# Generated at 2022-06-13 09:03:33.320672
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    from ansible.playbook.block import Block

    # Set up a Block
    block = Block()

    # Set up IncludeRole with block and role
    role = IncludeRole(block, role = "test_role")

    # get_name should return "include_role : test_role"
    assert(role.get_name() == "include_role : test_role")

    # get_name should return "include_role : test_role"
    assert(role.get_name() == "include_role : test_role")

# Generated at 2022-06-13 09:03:44.613332
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Verify load with no data raises exception
    try:
        IncludeRole.load(data={})
        assert False, 'AnsibleParserError not raised'
    except AnsibleParserError as e:
        pass

    # Verify load with no 'name' raises exception
    try:
        IncludeRole.load(data={}, role=Role(name='foo'))
        assert False, 'AnsibleParserError not raised'
    except AnsibleParserError as e:
        pass

    # Verify load with no 'role' raises exception
    try:
        IncludeRole.load(data={}, role=Role(name='foo'))
        assert False, 'AnsibleParserError not raised'
    except AnsibleParserError as e:
        pass

    # Verify load with no parent raises exception

# Generated at 2022-06-13 09:03:54.574766
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:04:02.361104
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test case when 'name' is a required field
    my_data = {'name': None, 'role': None}
    my_block = Block()
    my_block.role = Role()
    with pytest.raises(AnsibleParserError):
        IncludeRole.load(my_data, my_block)

    # Test case when 'public' is an invalid option
    my_data = {'name': 'test_role', 'public': True}
    with pytest.raises(AnsibleParserError):
        IncludeRole.load(my_data, my_block)

    # Test case when 'apply' is an invalid option
    my_data = {'name': 'test_role', 'apply': {'become': True}}
    with pytest.raises(AnsibleParserError):
        IncludeRole.load

# Generated at 2022-06-13 09:04:12.338805
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    def check_load_result(ir, expected_result):
        assert ir._role_name == expected_result['role_name']
        assert ir._from_files == expected_result['from_files']
        assert ir._allow_duplicates == expected_result['allow_duplicates']
        assert ir._public == expected_result['public']

    # Create a Play object
    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'roles': [
            'test role'
        ]
    })

    # Test valid option 'name' and value
    ir = IncludeRole.load({'name': 'test role', 'role': 'test role'})

# Generated at 2022-06-13 09:04:37.337209
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import role_loader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.template import Templar
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    mock_loader = role_loader.get('file')


# Generated at 2022-06-13 09:04:47.681975
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
	from ansible.parsing.dataloader import DataLoader
	from ansible.vars import VariableManager
	from ansible.inventory import Inventory
	from ansible.playbook.play import Play
	from ansible.template import Templar
	from ansible.utils.display import Display
	from ansible.utils.vars import load_extra_vars
	from ansible.executor.task_queue_manager import TaskQueueManager
	import os
	import sys
	data_loader = DataLoader()
	variable_manager = VariableManager()
	tqm = TaskQueueManager(
		inventory=Inventory(data_loader),
		variable_manager=variable_manager,
		loader=data_loader,
		display=Display(),
		options=None,
		passwords=None,
	)
	variable

# Generated at 2022-06-13 09:04:58.254516
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    from ansible.inventory.manager import InventoryManager

    from .mock.loader import DictDataLoader


# Generated at 2022-06-13 09:05:02.741010
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    include_role = IncludeRole()
    class Role:
        def __init__(self):
            self.get_name = lambda: 'name'
            self.get_role_params = lambda : {'role_specific_param': 0}

    # test 1: no parent role --> no role specific params
    params = include_role.get_include_params()
    assert params == {}

    # test 2: parent role --> role specific params
    include_role._parent_role = Role()
    params = include_role.get_include_params()
    assert params == {'role_specific_param': 0, 'ansible_parent_role_names': ['name'], 'ansible_parent_role_paths': ['']}

    # test 3: multiple parents --> multiple role specific params

# Generated at 2022-06-13 09:05:16.055533
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Changed Argument 'data' from a dictionary to a raw text string
    data = '''
    - name: Testing rolespec_validate
      hosts: localhost
      roles:
      - { role: role1, public: false, allow_duplicates: true }
    - name: Testing that include_role does not support public
      hosts: localhost
      tasks:
      - include_role:
          name: role1
          public: true
      - include_role:
          name: role1
          allow_duplicates: true
    '''
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader, inventory, variable_manager = Play

# Generated at 2022-06-13 09:05:26.618396
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    load_data = {
        'name': 'test',
        'apply': {
            'foo': 'bar',
        },
        'allow_duplicates': True,
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'handlers_from': 'handlers/main.yml',
        'defaults_from': 'defaults/main.yml',
    }

    with pytest.raises(AnsibleParserError) as error:
        IncludeRole.load(load_data, task_include=None, loader=None)


# Generated at 2022-06-13 09:05:34.258768
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import xrange

    from ansible.module_utils.six.moves import zip


    def add_action(block, action):
        block.append(Block(None, action))

    def add_role(block, role):

        # build dict to pass to role constructor
        role_dict = dict(block='block', args=role)
        # create new role
        r = Role.load(role_dict, block._play, block)
        # add to block
        block._roles.append(r)


# Generated at 2022-06-13 09:05:47.038940
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    test_data = {
        'block': None,
        'role': None,
        'task_include': None,
        'variable_manager': None,
        'loader': None,
        '_allow_duplicates': True,
        '_public': False,
        '_role_name': None,
        '_role_path': None,
        '_from_files': {},
        '_parent_role': None,
        'vars': dict(),
    }
    ret = IncludeRole.load(
        data = dict(
            name = 'this-is-a-role',
            vars = dict(
                r_var = '42',
            ),
        ),
    )

# Generated at 2022-06-13 09:06:00.525792
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # load with invalid args
    data = dict(
        action='include_role',
        name="some_name",
        role="some role",
        invalid_option='should be invalid'
    )
    try:
        IncludeRole.load(data)
    except AnsibleParserError:
        pass
    else:
        assert False, "AnsibleParserError not raised"

    # load with valid args

# Generated at 2022-06-13 09:06:08.382198
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = {
        '__role_name': 'app',
        '__role_path': '/path/to/roles/app',
        '__parent_role__': Role(),
        'vars': {
            'redis_port': 1234,
        }
    }

    expected = {
        'action': 'include_role',
        '_role_name': 'app',
        '_role_path': '/path/to/roles/app',
        '_parent_role': data['__parent_role__']
    }

    ir = IncludeRole.load(data, **data)
    actual = dict(ir.__dict__)
    actual.pop('vars')
    actual.pop('_parent')

    assert actual == expected

    # invalid options

# Generated at 2022-06-13 09:06:34.755691
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    results = []

    def _loader(path, become_context=None, variable_manager=None, loader=None):
        return {
            'path': path
        }

    class _VariableManager(object):
        def __init__(self, loader=None, inventory=None, version_info=None):
            pass

        def get_vars(self, play=None, task=None):
            return {}

        def set_host_variable(self, host, varname, value):
            pass

        def set_nonpersistent_facts(self, host, facts):
            pass

    class _Play(object):
        def __init__(self, loader=None, variable_manager=None, options=None):
            pass


# Generated at 2022-06-13 09:06:42.422480
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    x1 = IncludeRole()
    data1 = {'name': 'apt', 'role': 'cis.cis_ubuntu_linux_16.04'}

    x2 = IncludeRole()
    data2 = {'name': 'apt', 'role': 'cis.cis_ubuntu_linux_16.04', 'apply': {'var1': '1', 'var2': 'c'}}

    assert x1.load(data1).to_json() == {'name': 'apt', 'role': 'cis.cis_ubuntu_linux_16.04', 'args': {'name': 'apt', 'role': 'cis.cis_ubuntu_linux_16.04'}}

# Generated at 2022-06-13 09:06:48.141236
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task import Task
    options = PlaybookExecutor.load_options()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    data = '''
    - include_role:
        name: test
        public: yes
        allow_duplicates: yes
    '''

# Generated at 2022-06-13 09:06:56.256184
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext

    class Play:
        pass

    class TaskInclude:
        pass

    class Role:
        pass

    class RoleInclude:
        pass

    class TemplateMock:
        def __init__(self, *args, **kwargs):
            pass

        def template(self, *args, **kwargs):
            return

    class VariableManagerMock:
        def __init__(self, *args, **kwargs):
            pass

        def get_vars(self, *args, **kwargs):
            return


# Generated at 2022-06-13 09:07:06.926137
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Load a role (definition of 'webapp' in roles/webapp/meta/main.yml)
    ri = RoleInclude.load('webapp')
    ri.vars.update({'webapp_docroot': '{{ webapp_docroot|default(\'/var/www/html\') }}'})
    actual_role = Role.load(ri)
    actual_role.vars.update({'webapp_docroot': '/var/www/html'})

    # Build an IncludeRole
    include_role = IncludeRole()
    include_role._role_name = 'webapp'
    include_role._from_files.update({'vars': 'role.yml'})

    # Build the list of blocks
    block_list = include_role.get_block_list()[0][0]

   

# Generated at 2022-06-13 09:07:17.228201
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.errors import AnsibleParserError
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    data = {'name': 'test'}
    loader = None
    variable_manager = VariableManager()
    role = Role()
    role._role_name = 'test'
    task_include = None


# Generated at 2022-06-13 09:07:17.838977
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:18.458778
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:19.542061
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # TODO: Unit test not implemented
    return

# Generated at 2022-06-13 09:07:30.757465
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.plugins.loader as plugin_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    # Load the collection from path
    collection_name, collection_path = 'test_collections/local_collection', 'test/resources/collections/ansible_collections/local_collection'
    loader = plugin_loader.PluginLoader(collection_list=[collection_path], collections_paths=[])
    loader.all(class_only=True, include_contrib=True)
    collection_loader = AnsibleCollectionLoader(collections=[collection_name])
    collection_loader.load()



# Generated at 2022-06-13 09:08:18.703559
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Test successful load when role_path is specified
    ir = IncludeRole(role=None,
                     from_files={'tasks': 'tasks/main.yml'},
                     role_name='foo',
                     role_path='/a/b/c',
                     task_include=None)
    r = Role.load(ir)

# Generated at 2022-06-13 09:08:24.171442
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    def check(name, args, expected):
        block = Block(None)
        include_role = IncludeRole(block=block)
        include_role.action = 'include_role'
        include_role.name = name
        include_role.args = args
        assert include_role.get_name() == expected

    check(None, {'role': 'name'}, 'include_role : name')
    check('include_role2', {'role': 'name'}, 'include_role2')

# Generated at 2022-06-13 09:08:36.987337
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    filename = 'test_IncludeRole_get_name.yml'
    loader = DictDataLoader({filename: """---
- hosts: localhost
  tasks:
    - include_role:
        name: testrole"""
                             })

    # get_name() -> "name: <name_attribute>" if name is specified
    pb = Playbook.load(filename, loader=loader)
    play = pb.get_plays()[0]
    assert len(play.get_tasks()) == 1
    assert play.get_tasks()[0].get_name() == 'include_role: testrole'

    # get_name() -> "name: <name_attribute>" if role is specified

# Generated at 2022-06-13 09:08:49.253377
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    my_block = Block()
    my_block.args = {}
    my_block.vars = {}
    my_role = Role(dict(name='n1'))
    my_role2 = Role(dict(name='n2'))
    my_block.parent = my_role
    my_role.parent = my_role2

    my_role_include = RoleInclude()
    my_role_include.include_tasks = []
    my_role_include.include_handlers = []
    my_role_include.include_vars = []
    my_role_include.include_defaults

# Generated at 2022-06-13 09:09:01.691478
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager

    role_name = 'role_name'
    role_path = 'path/to/role'

    def mock_load(self, attrib, play=None, variable_manager=None, loader=None, collection_list=None, **kwargs):
        if self.__class__ == RoleInclude:
            self._metadata = RoleDefinition()

    class MockRoleInclude(RoleInclude):
        # overriding load() to mock out the RoleDefinition
        load = mock_load

    # setup mock objects
    mock_playbook = Playbook()
    mock_variable_manager = VariableManager()
    mock_loader = object()

    # we have a RoleInclude, so let's

# Generated at 2022-06-13 09:09:10.016152
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:09:19.373924
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # input
    data = dict(
        name="myrole"
    )

    # data loader
    loader = DataLoader()
    # variable manager
    variable_manager = VariableManager()

    # create object
    obj = IncludeRole(loader=loader, variable_manager=variable_manager)
    obj.load(data)

    try:
        data = dict()
        obj = IncludeRole(loader=loader, variable_manager=variable_manager)
        obj.load(data)
        assert False, "should not reach here"
    except AnsibleParserError as e:
        assert "name" in str(e)


# Generated at 2022-06-13 09:09:26.564921
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.parsing.yaml.loader import AnsibleLoader
    import json
    import os

    kwargs = dict(
        block=Block(),
        role=Role(),
        task_include=TaskInclude(),
        loader=AnsibleLoader(None, variable_manager=None, search_paths=C.DEFAULT_ROLES_PATH),
    )

    # case 1: valid ansible.cfg
   

# Generated at 2022-06-13 09:09:35.797572
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # test normal operation with / without role
    block = Block()
    role = Role().load({'name': 'test_role'})
    task_data = {'include_role': dict(name='test_role')}
    ir_1 = IncludeRole.load(task_data, block=block, role=role, variable_manager=None, loader=None)
    assert ir_1._role_name == "test_role"
    task_data = {'include_role': dict(name='test_role')}
    ir_1 = IncludeRole.load(task_data, block=block, role=None, variable_manager=None, loader=None)
    assert ir_1._role_name == "test_role"

    # test exception for lack of role name
    task_data = {'include_role': dict()}
   

# Generated at 2022-06-13 09:09:47.026600
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Test 1
    print("Test 1")
    ansible_module_path = "ansible/module_utils/basic.py"
    options_path = "ansible/playbooks/library/include_role.yml"
    myIncludeRole = IncludeRole()
    myIncludeRole.args = {'role': 'ansible.builtin.include_role', 'name': 'include_role'}
    myIncludeRole.action = 'include_role'

    blocks = myIncludeRole.get_block_list(play=None, variable_manager=None, loader=None)

    assert(blocks[0][0].name == 'include_role')
    assert(blocks[0][0].module_name == "include_role")
    assert(blocks[0][0].action == "include_role")

# Generated at 2022-06-13 09:10:51.718835
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Declare some classes
    class Block(object):
        def __init__(self, parent=None, loader=None, role=None, task_include=None, use_handlers=True):
            self._parent = parent
            self._loader = loader
            self._role = role
            self._task_include = task_include
            self.use_handlers = use_handlers
            self.collections = {}

        def get_dep_chain(self):
            return self._dep_chain

    class Role(object):
        def __init__(self, *args, **kwargs):
            self.name = 'name_of_role'
            self._metadata = {'allow_duplicates': True}
            self.handlers = []
            self.tasks = []

# Generated at 2022-06-13 09:11:02.117067
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Test setup
    collection_list = ['my_collection']
    loader = None
    variable_manager = None
    play = None
    test_case=1
    
    if test_case==1:
        # Test 1
        # Test execution
        # Create an IncludeRole object
        ir = IncludeRole(role=None)
        # Test the get_block_list method
        blocks, handlers = ir.get_block_list(play=play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
        # Test assertions
        # Handling not implemented. It will return a list of blocks and a list of handlers.
        # They are None as the method is not implemented
        assert blocks is None
        assert handlers is None

# Generated at 2022-06-13 09:11:14.477976
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    # create temp dir for roles
    #create_directory('./test_roles')
    #for name, roledefs in roles.items():
    #    create_directory(os.path.join('./test_roles', name))
    #    with open(os.path.join('./test_roles', name, 'meta', 'main.yml'), 'wb') as f:
    #        f.write(roledefs)

    loader = DictDataLoader({'./test_roles': {}})

    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader=loader))

    play_context = PlayContext()

# Generated at 2022-06-13 09:11:24.486760
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:11:25.200733
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:11:35.201083
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop, mock_unfrackpath_success
    from units.mock.parser import parse_from_yaml

    from copy import deepcopy
    from yaml import safe_dump

    # args loaded from yaml
    yaml_args = dict(
        name="myrole",
        tasks_from="main.yml",
        vars_from="vars/main.yml",
        defaults_from="defaults/main.yml",
        handlers_from="handlers/main.yml",
        apply=dict(
            when="check_mode",
            with_items="item",
            with_subelements="subelement",
            static="static",
        ),
    )

   

# Generated at 2022-06-13 09:11:38.789971
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.action = 'include_role'
    ir._role_name = 'test_role'
    assert ir.get_name() == 'include_role : test_role'

# Generated at 2022-06-13 09:11:40.421971
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """Testing get_block_list method of class IncludeRole"""

    # TODO: To be implemented
    pass

# Generated at 2022-06-13 09:11:45.446672
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    import ansible.playbook.role
    loader = DataLoader()
    play_context = PlayContext()
    play_context.loader = loader
    play_context.vars = {}
    role = ansible.playbook.role.Role()
    role._role_path = './../tests/'
    coldata = {'name': 'test'}
    ir = IncludeRole.load(coldata, role = role, variable_manager = None, loader = loader)
    assert ir.name == 'test'
    assert ir._role_name == 'test'
    assert ir._role_path == './../tests/'
    assert ir._parent_role == role

# Generated at 2022-06-13 09:11:59.241963
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import unittest

    import ansible.constants as C
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader
    from ansible.plugins.loader import resolve_ansible_playbook_path
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
