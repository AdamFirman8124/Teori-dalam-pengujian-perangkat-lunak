

# Generated at 2022-06-13 09:02:50.415404
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    class AttrDict(dict):
        def __getattr__(self, attr):
            return self[attr]
        def __setattr__(self, attr, val):
            self[attr] = val

    class MockBlock:
        _attributes = AttrDict(static=False)

    class MockPlay:
        _base_vars = AttrDict(name="mock_play")

    class MockIncludeTask:
        def __init__(self):
            self._role_name = "mock_role"
            self._parent = self
            self._attributes = AttrDict()

    class MockRole:
        def __init__(self):
            self._role_name = "mock_role"
            self._task_includes = [MockIncludeTask()]
            self._t

# Generated at 2022-06-13 09:03:01.144956
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    import os

    test_path = os.path.join(os.path.dirname(__file__),"ris_test")


# Generated at 2022-06-13 09:03:06.540447
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # create the objects needed by the method
    # myplay = play.Play()
    # loader = DataLoader()
    # variable_manager = VariableManager()
    # blocks, handlers = [],[]
    # p_block = Block()
    # block = Block()

    # create object of class IncludeRole
    my_obj = IncludeRole()

    # call the method
    # result = my_obj.get_block_list(myplay, variable_manager, loader)

    assert (True)

# Generated at 2022-06-13 09:03:17.785462
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    def _task(data):
        # stub task definition to match
        task_def = {
            'include': {
                'name': 'foobar',
            }
        }
        task_def['include'].update(data)

        block = Block(parent_block=role, role=role)
        include = IncludeRole(block, role)
        return IncludeRole(block, role).load(task_def, block, role)

    role = Role()

    # name is needed, or use role as alias
    try:
        task = _task({})
        raise AssertionError("No exception raised")
    except AnsibleParserError:
        pass

    task = _task({'role': 'foobar'})

# Generated at 2022-06-13 09:03:28.019880
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''Test the get_block_list method of class IncludeRole'''
    block_name = 'test_task'
    role = {'name': 'test_role'}
    block = IncludeRole(block=block_name)
    block.vars = {'test_var1': 'test_value1', 'test_var2': 'test_value2'}
    block._from_files = {'tasks': 'test_tasks.yml', 'vars': 'test_vars.yml', 'handlers': 'test_handlers.yml'}
    block._role_name = 'test_role'
    block._role_path = '/etc/ansible/roles/test_role'
    role_block_name = 'test_role_block_1'
    role_block = Block()
    role

# Generated at 2022-06-13 09:03:34.798873
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    from ansible.errors import AnsibleParserError
    from ansible.module_utils._text import to_text
    import yaml


# Generated at 2022-06-13 09:03:46.554871
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play

    # create the role object
    role_name = "test_role"
    role_path = "/tmp/roles/test_role"
    ir = IncludeRole()
    ir._role_path = role_path
    ir._role_name = role_name

    # create the play object
    play_name = "test_play"
    play_hosts = ["localhost"]
    play_path = "/tmp/roles/test_role"
    play_role_names = [role_name]
    p = Play()
    p.name = play_name
    p.hosts = play_hosts
    p.path = play_path
    p.role_names = play_role_names

    # attempt to get the block list, should not raise an exception
    ir.get

# Generated at 2022-06-13 09:03:55.903978
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''Unit test for method get_block_list of class IncludeRole'''
    print('Unit test for method get_block_list of class IncludeRole')

    import ansible.playbook.block as block
    import ansible.playbook.task as task
    import ansible.playbook.role.include as role_include
    import ansible.playbook.role as role

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import loader as plugin_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor


# Generated at 2022-06-13 09:04:02.749822
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook
    # Execute method under test
    include_role_obj = IncludeRole()
    block_list = include_role_obj.get_block_list()
    # Assert result
    assert type(block_list) is tuple
    assert len(block_list) == 2
    block_list_obj1_type = type(block_list[0])
    assert block_list_obj1_type is list
    block_list_obj2_type = type(block_list[1])
    assert block_list_obj2_type is list
    # Execute method under test
    include_role_obj = IncludeRole()
    # Assert result
    assert type(include_role_obj) is IncludeRole


# Generated at 2022-06-13 09:04:12.733636
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import ansible.playbook

    display.verbosity = 2
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    variable_manager = ansible.playbook.VariableManager()
    pb = Playbook.load("./test_IncludeRole.yml", variable_manager=variable_manager, loader=loader)
    variable_manager.set_playbook_basedir(os.path.dirname(pb.filename))


# Generated at 2022-06-13 09:04:26.477962
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    display.verbosity = 3
    import os
    import sys
    import pytest

    # Create a role which can be included
    def create_role(role_name, play_dir_name, task_name, task_vars):
        role_dir_name = os.path.join(play_dir_name, 'roles')

        try:
            os.mkdir(role_dir_name)
        except OSError as e:
            if e.errno != 17:
                raise

        role_dir_name = os.path.join(role_dir_name, role_name)

        try:
            os.mkdir(role_dir_name)
        except OSError as e:
            if e.errno != 17:
                raise


# Generated at 2022-06-13 09:04:37.716840
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    my_play = PlayContext()

    ir = IncludeRole()
    ir.action = "include_role"
    ir.args = {
        'name': "myrole"
    }
    (blocks, handlers) = ir.get_block_list(my_play)

    my_play.roles.append(Role())
    my_play.roles[0].name = "myrole"

# Generated at 2022-06-13 09:04:48.080293
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test with no name and no role:
    data = dict(action='include_role')
    ir = IncludeRole().load(data)
    assert ir.args['name'] is None, 'the name field must be None.'
    assert ir.args['role'] is None, 'the role field must be None.'

    # Test with a name but no role:
    data = dict(action='include_role', name='testname')
    ir = IncludeRole().load(data)
    assert ir.args['name'] == 'testname', 'the name must be testname.'
    assert ir.args['role'] is None, 'the role field must be None.'

    # Test with no name but with a role:
    data = dict(action='include_role', role='testrole')
    ir = IncludeRole().load(data)

# Generated at 2022-06-13 09:04:58.558315
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    role1 = Role()
    role1.name = 'role1'
    role1.dep_chain = {'role1', 'role2'}
    role1._params = {'param1': 'value1'}
    role1.repo_dir = 'role1-repo-dir'
    role1.role_path = 'role1-role-path'
    role1.tasks_path = 'role1-tasks-path'
    role1.handlers_path = 'role1-handlers-path'
    role1.vars_path = 'role1-vars-path'
    role1.defaults_path = 'role1-defaults-path'
    role1.meta_path = 'role1-meta-path'
    role1.files_path = 'role1-files-path'

# Generated at 2022-06-13 09:05:06.138621
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()

    # Testing when name is present
    task_include_1 = IncludeRole(block=block, role=role)
    task_include_1._role_name = "Shakespeare"
    assert task_include_1.get_name() == 'include_role : Shakespeare'

    # Testing when name is not present
    task_include_2 = IncludeRole(block=block, role=role)
    task_include_2._role_name = None
    assert task_include_2.get_name() == 'include_role : None'

# Generated at 2022-06-13 09:05:18.401025
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    # build a minimal role definition
    role_definition = RoleDefinition()
    role_definition.role_path = '.'
    role_definition.name = 'with_parent_role'
    role_definition.role_params = dict(param1='value1', param2='value2')

    # build a minimal role
    role = Role()
    role._role_path = '.'
    role._role_params = dict(param1='value1', param2='value2')

# Generated at 2022-06-13 09:05:27.907185
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    This test case is for testing the method get_block_list of class IncludeRole
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError
    ir = IncludeRole()
    try:
        ir.get_block_list()
    except AnsibleParserError:
        a = 1
    assert a == 1
    # block = Block()
    # role = Role()
    # task_include = TaskInclude()
    # ir = IncludeRole(block=block,role=role,task_include=task_include)
    #
    # ir.statically_loaded = True
    # ir

# Generated at 2022-06-13 09:05:34.494936
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.requiremenets import RoleRequirement
    from ansible.playbook.task import Task
    from ansible.playbook.task.include import TaskInclude
    from ansible.template import Templar
    #from ansible.parsing.mod_args import ModuleArgsParser
    from collections import namedtuple

    role_name = 'test_role'
    block = Block()
    role = Role()

    # Create a new instance of class IncludeRole
    ir = IncludeRole(block, role)

    # Create a new instance of class Play
    p = Play()

    # Create a new instance

# Generated at 2022-06-13 09:05:35.936671
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:05:47.885364
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Create the object
    ir = IncludeRole()

    # If a role is not specified, raise an exception
    data = {'name': 'foo'}
    try:
        ir.load(data)
        assert False
    except AnsibleParserError as e:
        assert 'role' in e.message

    # If a files_from option is present, it must be a string
    data = {'name': 'foo', 'role': 'bar'}
    for key in ('tasks_from', 'vars_from', 'defaults_from', 'handlers_from'):
        data[key] = 1
        try:
            ir.load(data)
            assert False
        except AnsibleParserError as e:
            assert 'Expected a string' in e.message
        del data[key]

    # If the 'public

# Generated at 2022-06-13 09:06:05.944183
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block.load(dict(
        tasks=[
            dict(action='include_role', name="test_include_role")
        ]
    ), play=dict())
    assert IncludeRole.load(block.block  # pylint: disable=no-member
                            ['tasks']
                            [0], block=block).get_name() == 'include_role : test_include_role'

    block = Block.load(dict(
        tasks=[
            dict(action='include_role', name="test_include_role", tags=['test'])
        ]
    ), play=dict())
    assert IncludeRole.load(block.block  # pylint: disable=no-member
                            ['tasks']
                            [0], block=block).get_name() == 'include_role : test_include_role'

# Generated at 2022-06-13 09:06:20.545878
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import yaml
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play


    '''setup data'''
    data = {
        'block': None,
        'role': None,
        'task_include': None,
        'variable_manager': None,
        'loader': None,
        'args': {
            'name': './test/test_role',
            'tasks_from': './test/test_role/tasks',
            'vars_from': './test/test_role/vars',
            'handlers_from': './test/test_role/handlers'
        }
    }

# Generated at 2022-06-13 09:06:28.192073
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import callback_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    from units.compat.mock import patch
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import json
    import pytest
    import os

    # mock templar, to leave jinja2-templated names unchanged
    class DummyDefaults(object):
        def __init__(self):
            self.defaults = {}


# Generated at 2022-06-13 09:06:29.514809
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """ this is a stub for automated testing """
    pass

# Generated at 2022-06-13 09:06:41.511625
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.role
    from units.mock.loader import DictDataLoader

    role_name = 'test'
    role_path = os.path.join(os.path.expanduser("~"), 'roles')
    role_vars = {'role_var': 'bar'}
    task_vars = {'task_var': 'foo'}
    blocks = [
        {
            'block': [
                {
                    'do_this': 'true'
                }
            ],
            'block_type': 'task',
            'when': 'when_var' in task_vars,
            'rescue': [],
            'always': [],
        }
    ]

# Generated at 2022-06-13 09:06:49.706364
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block, role, task_include)

    include_role.name = "ExampleName"
    assert include_role.get_name() == "ExampleName"

    include_role.name = None
    include_role._action = "ExampleAction"
    include_role._role_name = "ExampleRoleName"
    assert include_role.get_name() == "ExampleAction : ExampleRoleName"



# Generated at 2022-06-13 09:06:53.533397
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    class TestConfig:
        def __init__(self):
            self.DEFAULT_ROLES_PATH = '/usr/local/ansible/roles'

    config = TestConfig()
    assert IncludeRole.load({'name': 'test'})

# Generated at 2022-06-13 09:07:05.123258
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Basic syntax
    data = {
        "name": "foo",
        "role": "bar"
    }
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    include_role = IncludeRole.load(data, loader=loader, variable_manager=variable_manager)
    assert include_role.action == 'include_role'
    assert include_role.name == 'foo'
    assert include_role._role_name == 'foo'
    assert include_role.args == data
    assert include_role._from_files == {}
    assert include_role._parent_role is None
    assert include_role._role_path is None
    assert include_role.apply == {}

    # Role is deprecated
    data = {
        "role": "foo",
    }

# Generated at 2022-06-13 09:07:08.969524
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():  # noqa
    # Start test
    test = IncludeRole()
    test.name = "foo"
    test.action = "role"
    test._role_name = "bar"
    assert test.get_name() == "foo : bar"
    test.name = None
    assert test.get_name() == "role : bar"

# Generated at 2022-06-13 09:07:10.373979
# Unit test for method get_block_list of class IncludeRole

# Generated at 2022-06-13 09:07:33.020896
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    data = dict(
        name='some_role',
        tasks_from='hook.yml',
        vars_from='vars.yml',
        defaults_from='defaults/main.yml',
        handlers_from='handlers.yml',
        apply=dict(
            tags=dict(foo=True),
            only=dict(bar=True)
        ),
        when='true',
        public=True,
        allow_duplicates=False,
        rolespec_validate=False
    )

    role = Role()
    role.searchpath = ['/path/to/my/role/']
    include_role = IncludeRole()
    include_role.action = 'include_role'
    include_role.statically_loaded = True
    include_role._parent_role = role
    include_

# Generated at 2022-06-13 09:07:35.876649
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    role_obj = IncludeRole()
    assert role_obj.get_name() == 'include_role : '


# Generated at 2022-06-13 09:07:41.136028
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    """ inline tests to validate the IncludeRole.get_name method """

    # set up some mock objects
    task_include = TaskInclude()
    ir = IncludeRole(None, None, task_include)

    ir._role_name = 'fake_role'
    assert ir.get_name() == 'fake_role : fake_role'

    ir.name = 'fake_name'
    assert ir.get_name() == 'fake_name'

# Generated at 2022-06-13 09:07:47.033117
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block

    play = Role()
    block = Block.load(dict(
            task = dict(
                meta = dict(
                    name = 'the task name',
                ),
                include_role = dict(
                    name = 'the role name',
                )
            )
        ), play=play)

    # role_name, play, variable_manager, loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()

    block_list, handler_list = block.block._parent.get_block_list(play=play, variable_manager=variable_manager, loader=loader)

    assert block_list
   

# Generated at 2022-06-13 09:07:56.874138
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_vars(loader=loader, play=dict(vars=dict(my_var='my_value')))

    block = Block()
    block.parent = Role()
    data = dict(action='include_role', name='test_role')

    r = IncludeRole.load(data, block, variable_manager=variable_manager, loader=loader)
    assert r._role_name == 'test_role'

    data = dict(action='include_role', role='test_role')
    r = IncludeRole.load(data, block, variable_manager=variable_manager, loader=loader)
    assert r._role_name == 'test_role'


# Generated at 2022-06-13 09:08:09.252352
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class MockRole(Role):
        def __init__(self, collection_name, role_name):
            self._role_path = ''
            self.collection_name = collection_name
            self.name = role_name
            self.role_name = role_name
            self.metadata = {}
            self.tasks = []
            self.default_vars = {}
            self.dependencies = []
            self._parents = []
            self.has_tasks = False
            self.has_handlers = False
            self.has_vars = False
            self.has_default_vars = False
            self.has_meta = False
            self.has_task_includes = False
            self.has_role_includes = False
            self.has_role_dependencies = False
            self.has_role_vars

# Generated at 2022-06-13 09:08:16.631524
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Static test because the test is only valid with a specific set of roles installed

    import tempfile
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils import context_objects as co
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils.six import PY3

    with tempfile.TemporaryDirectory() as tmpdirname:
        roles_path = tmpdirname + "/roles"


# Generated at 2022-06-13 09:08:22.749814
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    # This test is a little tricky because it is difficult to mock a role. So we will
    # make a fake role object and use its methods to validate the results of IncludeRole.get_block_list
    class FakeRole(object):
        def __init__(self):
            self.tasks = []

        def compile(self, play, dep_chain=None):
            return self.tasks

        def get_handler_blocks(self, play):
            return self.tasks

    # Make a fake include object to test the method
    include_object = IncludeRole()
    include_object._role_name = "my_role"
    include_object._from_files = "my_from_file"

    # Create a fake parent role
   

# Generated at 2022-06-13 09:08:25.933421
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    assert IncludeRole.load({'name': 'foo_role'}) # No error is good

# Generated at 2022-06-13 09:08:39.026159
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    testcase = """
---
- hosts: localhost
  gather_facts: no

  roles:
    - testcase_nested_role1
    - testcase_nested_role2

  tasks:
    - meta: clear_host_errors
    - include_role: testcase_nested_role3
      when: hostvars.localhost.meta.hostvars.localhost.meta.hostvars.localhost.meta.hostvars.localhost.hostname == 'asdf'
      apply:
        tags:
          - testcase_nested_role4
"""
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory("localhost", loader=loader, variable_manager=variable_manager)

    play = Play.load(testcase, variable_manager=variable_manager, loader=loader)
    all

# Generated at 2022-06-13 09:09:07.569324
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # ensure that when include_role is used without allow_duplicates
    # and the include_role path is called more than once, it is skipped
    # for subsequent calls
    # see https://github.com/ansible/ansible/issues/69245
    task_data = dict(apply=dict(),
                     public=True,
                     allow_duplicates=False,
                     when=None,
                     loop=None,
                     loop_control=dict(),
                     name="my_role",
                     rolespec_validate=True,
                     tasks_from="",
                     vars_from="",
                     defaults_from="",
                     handlers_from="")

    loop_over_roles = Block(task_data=task_data)
    loop_var = [0, 1]
    roles_to_include = []

# Generated at 2022-06-13 09:09:18.034524
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """Unit test for method load of class IncludeRole."""
    def get_block(action):
        block = Block()
        block.parent = None
        block.action = action
        block._play = None
        block._role = None
        block._task = None
        block.block = block
        block.statically_loaded = False

        return block

    block = get_block('include_role')
    include_role = IncludeRole.load(dict(include_role='test'), block=block)

    assert include_role.action == 'include_role'
    assert include_role._allow_duplicates is True
    assert include_role._public is False
    assert include_role._rolespec_validate is True
    assert include_role._from_files == {}
    assert include_role._parent_role is None

# Generated at 2022-06-13 09:09:30.784524
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.parsing.dataloader import DataLoader
    my_loader = DataLoader()
    variable_manager = None
    variable_manager_loader = None

    # Creating an IncludeRole object
    ir = IncludeRole()
    # Set the name attribute to none
    ir._role_name = None

    # Testing if the method return a string containing the action and the role name
    assert isinstance(ir.get_name(), str)
    assert 'name' in ir.get_name()
    assert 'role' in ir.get_name()
    assert 'include' in ir.get_name()

    # Testing with a different action name and same role name
    ir.action = 'debug'
    ir.name = 'test'

    expected_result = 'debug : test'
    result = ir.get_name()


# Generated at 2022-06-13 09:09:40.123761
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Create mock ansible block
    block = Block()
    # Create mock role
    role = Role()
    # Create mock task_include
    task_include = TaskInclude()

    # Create IncludeRole object
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    # Assign a name to the include_role object
    include_role.name = "testname"
    #assert method get_name returns the testname
    assert include_role.get_name() == "testname"

    # Create IncludeRole object without assign a name
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    # Assert method get_name returns the correct name
    assert include_role.get_name() == "include_role: None"

# Generated at 2022-06-13 09:09:51.857277
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import role_loader

    t = IncludeRole()

    p = Play().load(dict(
        name ="Test role include",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [
            dict(
                name="Test role include",
                include_role=dict(
                    name="Test include role",
                    tasks_from="tasks/main.yml"
                )
            )
        ]
    ), variable_manager=None, loader=None)

    p._tqm = None
    p._role_loader = role_loader
    p._play_context = PlayContext()
    p._loader = None
    p._variable_manager = None


# Generated at 2022-06-13 09:10:02.243609
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # import the module
    exec("from ansible.playbook.role.include import IncludeRole as UnitTestIncludeRole", globals(), locals())

    # setup a simple role include
    from ansible.playbook.role import Role
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    import ansible.utils.vars as vars_util
    from ansible.parsing.vault import VaultLib
    from ansible import context
    from ansible.module_utils._text import to_native

    role_name = 'test_role'
    role_path = '/tmp/roles/' + role_name
    parent_role_name = 'parent_role'

# Generated at 2022-06-13 09:10:11.377966
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os

    #
    # test:
    #   - include_role:
    #       name: my_role
    #
    my_data = {
        '__ansible_action__': 'include_role',
        '__ansible_arguments__': [
            'name',
            'my_role'
        ],
    }

    #
    # test:
    #   - include_role:
    #       name: my_role
    #       vars_from: some_dir/some_file.yml
    #

# Generated at 2022-06-13 09:10:20.467637
# Unit test for method get_block_list of class IncludeRole

# Generated at 2022-06-13 09:10:26.812490
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    includeRole = IncludeRole()
    includeRole.name = 'bar'
    includeRole._role_name = 'foo'

    assert includeRole.get_name() == 'bar : foo' , "IncludeRole get_name method is not working for includeRole.name not being none."

    includeRole.name = None
    assert includeRole.get_name() == '- include_role : foo' , "IncludeRole get_name method is not working for includeRole.name being none."


# Generated at 2022-06-13 09:10:34.536719
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()
    task_include = TaskInclude()
    action = "include_role"
    name = "test_name"
    from_files = {}
    ir = IncludeRole(block, role, task_include)
    ir.action = action
    ir.args['name'] = name
    ir._from_files = from_files
    result = ir.get_name()
    assert result == "%s : %s" % (action, name)

# Generated at 2022-06-13 09:11:31.075519
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for the given role
    assert IncludeRole.load == RoleInclude.load
    # Ensure load is called for

# Generated at 2022-06-13 09:11:39.447549
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.module_utils.six import PY3

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.required_file import RoleRequiredFile
    from ansible.playbook.role.scope import RoleScope
    from ansible.playbook.role.task_include import RoleTaskInclude
    from ansible.playbook.role.task_list import TaskList
    from ansible.playbook.role.task_role_include import TaskRoleInclude
    from ansible.playbook.task import Task

    if not PY3:
        # Python 2.x
        import __builtin__ as builtins
    else:
        # Python 3.x
        import builtins

    display = Display()
    display.column

# Generated at 2022-06-13 09:11:46.536873
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import unittest

    from ansible.errors import AnsibleError
    from ansible.playbook import Playbook

    from ansible.template import Templar

    from ansible.utils.vars import combine_vars

    from ansible.vars import VariableManager

    from ansible.playbook.play_context import PlayContext


    class AnsibleModule:
        _ARGS = {
            'name': 'foo_role',
            'rolespec_validate': False,
        }

        def __init__(self, args=None):
            if args is None:
                self.args = self._ARGS.copy()
            else:
                self.args = args


# Generated at 2022-06-13 09:11:53.915444
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    new_ir = IncludeRole()

    # Set value of name
    new_ir_name = "java"

    # Load value for name
    new_ir.name = new_ir_name

    # Get value for name
    new_ir_name_value = new_ir.get_name()

    # Check if the values are equal
    assert new_ir_name_value == new_ir_name


# Generated at 2022-06-13 09:12:03.670714
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Play

    play = Play.load(dict(
        name = "test",
        hosts = "all",
        roles = [
            dict(name='role1'),
            dict(name='role2',
                tasks = [
                    dict(action = 'debug', args = dict(msg="TEST1"))
                ]
            ),
        ],
        tasks = [
            dict(include_role = dict(name='role1'))
        ]
    ), loader=None, variable_manager=None)

    t = play.get_tasks()[0]
    blocks, handlers = t.get_block_list()
    assert len(blocks) == 1
    assert len(handlers) == 0

    # Task 2 are present in blocks
    assert blocks[0]._parent is t

# Generated at 2022-06-13 09:12:10.091178
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    inventory = InventoryManager(loader=DataLoader(), sources='./tests/unittests_data/inventory')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    loader = DataLoader()

    basedir = './tests/unittests_data/'

# Generated at 2022-06-13 09:12:20.830645
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block

    block = Block()
    role = None
    task_include = None

    data = dict(name='test')
    ir = IncludeRole.load(data, block, role, task_include)
    assert ir._role_name == 'test'
    assert ir._role_path is None

    data = dict(role='test')
    ir = IncludeRole.load(data, block, role, task_include)
    assert ir._role_name == 'test'
    assert ir._role_path is None

    data = dict(include='test')
    try:
        ir = IncludeRole.load(data, block, role, task_include)
    except AnsibleParserError as e:
        assert "`- include` is not a valid action for IncludeRole" == str(e)

# Generated at 2022-06-13 09:12:22.480030
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    hostvars = dict()
    new_include = IncludeRole()
    assert new_include.get_name() == 'include_role : '

# Generated at 2022-06-13 09:12:32.945677
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # create display object
    display = Display()

    # create a fake block
    b = Block()
    b.collections = ['namespace.collection']

    # create fake blocklist
    bl = [Block(), Block()]

    # create a fake loader
    l = None

    # create another block
    b2 = Block()
    b2.collections = ['namespace.collection']

    # create another blocklist
    bl2 = [Block()]

    # create fake connection
    c = None

    # create fake variable manager
    vm = None

    # create a fake play
    p = Play()

    # create a fake object of type IncludeRole
    i = IncludeRole()
    i._role_name = 'fake-role'
    i._parent_role = b
    i._parent = b2
    i.statically