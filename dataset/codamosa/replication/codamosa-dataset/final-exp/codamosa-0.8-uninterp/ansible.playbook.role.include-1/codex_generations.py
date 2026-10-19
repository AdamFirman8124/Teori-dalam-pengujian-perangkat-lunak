

# Generated at 2022-06-13 08:52:15.353410
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    if 'ANSIBLE_ROLES_PATH' in os.environ:
        role_path = ''
    elif os.path.isfile('/etc/ansible/roles'):
        role_path = '/etc/ansible/roles'
    elif os.path.isfile('/etc/ansible/roles'):
        role_path = '/etc/ansible/roles'
    elif os.path.isfile('/usr/share/ansible/roles'):
        role_path = '/usr/share/ansible/roles'
    elif os.path.isfile('/etc/ansible/roles'):
        role_path = '/etc/ansible/roles'


# Generated at 2022-06-13 08:52:20.398028
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """This is a basic test of method load of class RoleInclude.
    """
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    from ..unit_test import AnsibleExitJson
    from ..loader import DictDataLoader
    from ..yaml import AnsibleYamlModule, YAML_MODULE_PATH

    from .common import AnsibleCollectionRef
    from .artifact import AnsibleArtifact

    from ..galaxy_data import GalaxyData

    from ..module_utils.common.collections import ImmutableDict
    import os
    import sys

    # load requirements just like Ansible-galaxy would do

# Generated at 2022-06-13 08:52:28.177137
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    import ansible.playbook.play
    import ansible.playbook.role.definition
    import ansible.parsing.yaml.data
    ansible.playbook.play.Play = Play
    ansible.playbook.role.definition.RoleDefinition = RoleDefinition
    ansible.parsing.yaml.data.AnsibleUnicode = AnsibleBaseYAMLObject

    play_context = PlayContext()

# Generated at 2022-06-13 08:52:36.139086
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print("test_RoleInclude_load")
    data_test = {
        u'include': u'myRole_test',
        u'roles': ['myRole_test'],
        u'name': u'myRole_test',
        u'tasks': [],
        u'vars': {u'any_errors': u'False'},
        u'when': u'',
        u'become': u'false'
    }
    ri = RoleInclude()
    ri.load_data(data_test)
    print("done")

# Generated at 2022-06-13 08:52:46.866313
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    ri = RoleInclude.load({
        'name': 'test',
        'tasks': [
            {
                'name': 'Debug',
                'debug': 'var=hostvars'
            }
        ],
        'handlers': [
            {
                'name': 'Copy',
                'copy': 'src=a dest=b'
            }
        ]
    }, None)
    assert ri.name == 'test'
    assert isinstance(ri.tasks, list)
    assert isinstance(ri.handlers, list)
    assert ri._role_path == None
    assert ri._parent_role == None
    assert ri._update_changed_when() == False

# Generated at 2022-06-13 08:52:53.758176
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()

    test_dir = os.path.dirname(os.path.dirname(__file__))
    roles_path = os.path.join(test_dir, '../lib/ansible/roles')

    if not isinstance(roles_path, list):
        roles_path = [roles_path]

    inventory = InventoryManager(loader=loader, sources=['localhost,', 'other'])
    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()

    # Test loading role from

# Generated at 2022-06-13 08:53:04.335350
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class TestObject(object):
        pass

    test_obj = TestObject()

    test_obj.path = "roles/x/tasks/main.yml"
    test_obj.role_name = "x"
    test_obj.task = "TaskInclude(path=roles/x/tasks/main.yml role_name=x)"
    test_obj.play = "Play(name=None)"
    test_obj.tasks = [test_obj.task]

    test_obj.data = "y"

    test_obj.loader = "Loader()"
    test_obj.current_role_path = "roles/x"
    test_obj.variable_manager = "VariableManager()"
    test_obj.parent_role = "Role()"


# Generated at 2022-06-13 08:53:10.254676
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role = RoleInclude.load({
        "name":"test",
        "molecule": {
          "platforms": [
            {
              "name": "centos",
              "image": "centos:latest"
            }
          ]
        },
        "dependencies": [
            "role1"
        ],
        "molecule": {
          "platforms": [
            {
              "name": "centos",
              "image": "centos:latest"
            }
          ]
        }
    })

    print("role.dependencies=", role.dependencies)
    assert len(role.dependencies) == 1


# Generated at 2022-06-13 08:53:17.326746
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = {'hosts': 'localhost', 'version': '2.0'}

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.playbook.role.requirement import RoleRequirement

    current_role_path = '/etc/ansible/playbook/roles'
    play_context = PlayContext()
    play

# Generated at 2022-06-13 08:53:30.517735
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    
    inventory = InventoryManager(loader=None, sources=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    loader = DataLoader()
    play_context = PlayContext()

# Generated at 2022-06-13 08:53:33.289783
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: please add tests if add methods in class RoleInclude
    pass

# Unit test class RoleInclude

# Generated at 2022-06-13 08:53:40.722885
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:53:49.843610
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Unit test for method load of class RoleInclude

    :return:
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()

    context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager)
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    import tempfile
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:53:59.816482
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import unittest

    role_name = 'test_role'
    role_path = test_role_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "test_data", "test_roles", role_name)
    expected_description = 'Description of the test_role'
    expected_dependencies_path = os.path.join(role_path, 'meta', 'main.yml')
    expected_dependencies_dict = {'test_role_dependency' : 'tested.com'}
    expected_dependencies = [('test_role_dependency', expected_dependencies_dict)]
    expected_pre_tasks_path = os.path.join(role_path, 'tasks', 'main.yml')
    expected_t

# Generated at 2022-06-13 08:54:08.217262
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Initialize class
    ri = RoleInclude()
    # Initialize data
    data = 'foo'
    play = {'hosts': '', 'user': '', 'gather_facts': '', 'vars': '', 'roles': [{'include': 'role1', 'role2': 'bar'}]}
    current_role_path = '.'
    parent_role = {'include': 'role1', 'role2': 'bar'}
    variable_manager = '.'
    loader = '.'
    collection_list = [{'include': 'role1', 'role2': 'bar'}]

    # Test exception:  Invalid role definition: foo
    #assert False
    # Test exception:  Invalid old style role requirement: foo,bar
    #assert False

# Generated at 2022-06-13 08:54:19.112780
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import sys
    import unittest
    import ansible.module_utils.six as six

    role_def = {
        "role1": {
            "name": "role1",
            "version": "1.0",
            "vars": {
                'item1': 'value1'
            }
        }
    }

    class MockLoader(object):
        def __init__(self):
            self.mock_data = role_def
        def load_from_file(self, role_path, role_name):
            for role_name, role_data in six.iteritems(role_def):
                return role_data['vars']

    class MockTask(object):
        def __init__(self):
            self.name = 'role name'
            self.use_role_vars = True



# Generated at 2022-06-13 08:54:22.422428
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "Not implemented"

    # Test scenario when data is not a string, dict or AnsibleBaseYAMLObject object
    # Test scenario when data is a string and data contains a comma


# Generated at 2022-06-13 08:54:25.945234
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    obj = RoleInclude.load(data='test', play={}, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert obj.role_name == 'test'
    assert obj.get_unprefixed_name() == 'test'

# Generated at 2022-06-13 08:54:30.710377
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # unit tests in this function are not complete yet
    # basic examples are provided here

    # define the key variables
    current_role_path = os.getcwd()

    # create the data
    data = 'role-name'
    data = {'role': 'role-name'}
    data = {'role': 'role-name', 'tags': ['role-tags']}
    data = {'role': 'role-name', 'become': True}
    data = {'role': 'role-name', 'vars': {'var1': 'val1'}}
    data = {'role': 'role-name', 'vars': {'var1': 'val1'}, 'include_role': {'name': 'some-other-role'}}

# Generated at 2022-06-13 08:54:41.786246
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import RoleRequirement
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from io import StringIO
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop


# Generated at 2022-06-13 08:54:51.004326
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # FIXME: make a proper unit test here
    data = "test"
    play = []
    current_role_path = None
    parent_role = None
    variable_manager= None
    loader = None
    collection_list = None
    r = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert r.get_name() == "test"
    assert r.get_role_path() == os.path.join(os.path.dirname(__file__), os.pardir, "lib", "ansible", "roles", "test")

# Generated at 2022-06-13 08:54:59.706775
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class FakeRole():
        def __init__(self, name, collection_list=None):
            self.name = name
            self.collection_list = collection_list

    ri = RoleInclude()
    # Not string
    list1 = [1, 2 ,3]
    try:
        ri.load(data=list1)
    except AnsibleParserError:
        pass
    else:
        assert False, "should have failed"

    # Not dict
    list2 = [{'name': 'test_role_1'}]
    try:
        ri.load(data=list2)
    except AnsibleParserError:
        pass
    else:
        assert False, "should have failed"

    # RoleDefinition dict

# Generated at 2022-06-13 08:55:11.255076
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role import Role
    import json
    import unittest

    test_datas = {
        "test data 1": {
            "data": "passing a string",
            "result": "raise AnsibleError"
        },
        "test data 2": {
            "data": {"key1": "value1", "key2": "value2"},
            "result": True
        },
        "test data 3": {
            "data": {"key1": "value1", "key2": "value2"},
            "result": True
        }
        # TODO: more test data 
    }

    for d in test_datas:
        test_data = test_dat

# Generated at 2022-06-13 08:55:11.836271
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:55:12.813536
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test passing valid data as string and dict
    pass

# Generated at 2022-06-13 08:55:20.469711
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    data = 'myrole'
    ri = RoleInclude()
    role = ri.load(data, None, None, None, None, None)
    assert isinstance(role, RoleDefinition)

    data = 'myrole,vars'
    try:
        ri = RoleInclude()
        role = ri.load(data, None, None, None, None, None)
        assert False
    except AnsibleError:
        assert True

    data = 'myrole,somebranch'

# Generated at 2022-06-13 08:55:22.944179
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO:
    # 1. invoke load and test the return value
    pass

# Generated at 2022-06-13 08:55:26.842611
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    Unit test for method load of class RoleInclude
    '''
    RoleInclude.load(play=[], current_role_path=[], parent_role=[], variable_manager=None, loader=None, collection_list=None)

# Generated at 2022-06-13 08:55:37.657403
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role_dependency import RoleDependency

    p = Play().load({
        'hosts': 'all',
        'roles': [
            {
                "name": "test_name",
                "some_attr": "some_val",
                "some_other_attr": "some_other_val"
            },
        ]
    }, variable_manager={}, loader=None)

    play_deps = p.get_dependencies()

    assert(len(play_deps) == 1)
    assert(isinstance(play_deps[0], RoleDependency))
    assert(play_deps[0]._role_name == 'test_name')

# Generated at 2022-06-13 08:55:44.522679
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Play(object):
        def __init__(self):
            self.vars = dict()
            self.vars['name'] = 'test_play'

    class Task(object):
        def __init__(self):
            self.vars = dict()

    class RoleInclude(object):
        def __init__(self):
            self.vars = dict()

    play = Play()
    task = Task()
    role_include = RoleInclude()

    # data is of type string
    data = 'test_role'
    ri = RoleInclude.load(data, play)
    assert ri is not None

    # data is of type dict
    data = dict()
    data['role'] = 'test_role'
    ri = RoleInclude.load(data, play)
    assert ri

# Generated at 2022-06-13 08:55:50.848663
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    test_RoleInclude_load
    """
    def _data(rq):
        _data = RoleInclude()
        _data.load_data(rq)
        return _data.get_info()
    assert _data('test') == 'test'
    assert _data({'role': 'test'}) == 'test'

# Generated at 2022-06-13 08:55:51.851974
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:56:00.687132
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.cli.playbook.play_context import PlaybookCLI
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.utils.display import Display
    display = Display()
    pbcli = PlaybookCLI(parser=PlayContext(meta=dict(connection='local')), run_once=True, inventory=InventoryManager(loader=DataLoader()), variable_manager=VariableManager(), loader=DataLoader())
    pbcli.options = pbcli.read_cli_vals

# Generated at 2022-06-13 08:56:02.526175
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: Add unit tests
    print("RoleInclude Test")

# Generated at 2022-06-13 08:56:16.829417
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import __main__ as main
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.yaml import YAML
    from ansible.module_utils._text import to_bytes
    varmanager = VariableManager(loader=None, inventories=InventoryManager())
    play_context = PlayContext()
    play_context.connection = 'ssh'
    play_context.network_os = 'ios'
    play_context.remote_addr = '192.168.1.1'
    play_context.port = 22
    play_context.remote_user = 'test'
    play_context.password = 'password'
    play_context.become = False
    play_context.bec

# Generated at 2022-06-13 08:56:24.438022
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.galaxy.collection.manager import CollectionsManager

    class TestCallbackModule(CallbackBase):
        """
        CallbackBase subclass used in unit testing
        """
        def __init__(self, *args, **kwargs):
            super(TestCallbackModule, self).__init__(*args, **kwargs)

    def test_loader(path):
        """
        Fake a loader
        """
        return dict(foo="bar")


# Generated at 2022-06-13 08:56:34.465477
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    loader = action_loader.ActionModuleLoader()

    p = Play.load({'name': 'test', 'hosts': 'all'}, loader=loader)
    p.set_loader(loader)

    c = PlayContext()
    c._options = {'become': False, 'become_method': None, 'module_path': None, 'check': False}
    c._special_context = True
    p.set_context(c)  # export the play context to the role include

    ri = RoleInclude.load({"role": "test"}, play = p)
    assert({'role': 'test'} == ri.get_info(), 'bad role info')

# Generated at 2022-06-13 08:56:44.477924
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:56:45.782995
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert not ri.load('bad_data')

# Generated at 2022-06-13 08:56:53.339835
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import unittest
    import mock
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext, TaskOverride
    from ansible.playbook.play import Play
    from ansible.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    # Test for old style role requirement
    with mock.patch.object(RoleRequirement, "__init__", return_value=None):
        with mock.patch.object(RoleRequirement, "load_data") as mock_load_data:
            try:
                RoleInclude.load("role[get_a_role]", Play(), variable_manager=VariableManager())
            except AnsibleError as e:
                assert str(e) == "Invalid old style role requirement: role[get_a_role]"

# Generated at 2022-06-13 08:56:56.644639
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:56:58.971778
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    ri = RoleInclude()
    ri.load('/opt/roles/xyz')
    print(ri.get_name())
    assert ri.name == 'xyz'
    print('Test RoleInclude_load PASS')

# Generated at 2022-06-13 08:57:10.601311
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Opts:
        connection = 'local'
        module_path = None
        forks = 100
        remote_user = 'root'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = 'sudo'
        become_user = 'root'
        verbosity = 0
        check = False
        diff = False

    class Provider:
        no_log = False

    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager

    play_path = os.path.join(os.path.dirname(__file__), 'test_play.yml')

# Generated at 2022-06-13 08:57:26.787526
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """ This is a test for the method load of class RoleDefinition  """

    # Define the class under test
    class_under_test = RoleInclude()

    # Create a Mock for argument play
    mock_play = "MOCK"

    # Create a Mock for argument current_role_path
    mock_current_role_path = "MOCK"

    # Create a Mock for argument parent_role
    mock_parent_role = "MOCK"

    # Create a Mock for argument variable_manager
    mock_variable_manager = "MOCK"

    # Create a Mock for argument loader
    mock_loader = "MOCK"

    # Create a Mock for argument collection_list
    mock_collection_list = "MOCK"

    # Try to call the method

# Generated at 2022-06-13 08:57:34.671970
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from copy import deepcopy
    import os
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from io import StringIO
    from ansible.utils.vars import combine_vars
    import ansible.constants as constants
    from ansible.module_utils.six import iteritems, string_types
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils._text import to_native

    BASE_DIR = os.getcwd()

    TEST_INVALID_ROLE_DEFINITION = "C:/User/Username/ansible_projects/ansible/test_invalid_role_definition"
    TEST_ROLE_DEFINITION

# Generated at 2022-06-13 08:57:50.233753
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.role.definition import ROLE_CACHE
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = None


# Generated at 2022-06-13 08:57:53.980840
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load('foobar', None, None, None, None).name == 'foobar'
    assert RoleInclude.Load({'role': 'foobar'}, None, None, None, None).name == 'foobar'
    assert RoleInclude.load(RoleRequirement('foobar'), None, None, None, None).name == 'foobar'



# Generated at 2022-06-13 08:57:54.570081
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:57:57.193079
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert ri.load("test-role") == ri.load({"role": "test-role"})

# Generated at 2022-06-13 08:57:58.057537
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:58:10.338185
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.plugins.loader import role_loader

    role_definition_obj1 = RoleDefinition()
    role_definition_obj1.get_path = MagicMock(return_value="path1")

    role_definition_obj2 = RoleDefinition()
    role_definition_obj2.get_path = MagicMock(return_value="path2")

    role_definition_obj3 = RoleDefinition()
    role_definition_obj3.get_path = MagicMock(return_value="path3")

    loader_obj = role_loader

# Generated at 2022-06-13 08:58:16.426581
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    my_var_manager = VariableManager()
    my_loader = None
    data = dict(
        name = "franklin",
        my_additional_vars = dict(
            name = "george"
        )
    )

    ri = RoleInclude(play=None, role_basedir=None, variable_manager=my_var_manager, loader=my_loader)

    my_var_manager.set_variable('role_names', 'franklin')
    my_var_manager.set_variable('additional_vars', dict(name = "george"))

# Generated at 2022-06-13 08:58:26.939867
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    for data in ['test_role', 'role']:
        play = Play().load({'name': 'test', 'hosts': 'all', 'roles': [data]}, loader=DataLoader())
        ri = RoleInclude.load(data, play, collection_list=role_collections)

        assert isinstance(ri, RoleInclude)
        assert ri.get_name() == 'test_role'

    data = 'test_role,role'

# Generated at 2022-06-13 08:58:35.778512
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'test_role_name'
    play = None
    current_role_path = '/root/roles/'
    parent_role = 'parent_role_name'
    variable_manager = None
    loader = None
    collection_list = None
    assert RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert RoleInclude.load('test_role_name,' + current_role_path, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert RoleInclude.load('test_role_name,' + current_role_path, play, current_role_path, parent_role, variable_manager, loader, collection_list)


# Generated at 2022-06-13 08:58:40.673345
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # create a fake test object
    ri = True

    # create a fake play
    play = True

    # create a fake variable manager
    variable_manager = True

    # create a fake loader
    loader = True

    # test that no error is thrown when an expected good file is passed to load
    data = { 'role1' : {'some' : 'data'} }
    ri.load(data,play,variable_manager,loader)

    # test that an error is thrown when an unknown file is passed to load
    data = { 'role1' : {'some' : 'data'} }
    ri.load(data,play,variable_manager,loader)

# Generated at 2022-06-13 08:58:41.612202
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert(False)

# Generated at 2022-06-13 08:58:44.911969
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load(data=None, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None) is None


# Generated at 2022-06-13 08:58:49.565461
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    roleInclude = RoleInclude()
    data1 = 'deploy_login'
    data2 = 'deploy:deploy_login'
    data3 = {'role':'deploy_login'}
    data4 = {'role':'deploy:deploy_login'}
    data5 = {'role':'deploy'}
    data6 = {'role':'deploy',
             'include':'deploy_login'}

    # test case 1 - RoleInclude string type with one value
    role1 = roleInclude.load(data1, None)
    if not isinstance(role1, RoleInclude) :
        raise Exception('test case 1 - RoleInclude.load failed with one value')

    # test case 2 - RoleInclude string type with two values

# Generated at 2022-06-13 08:59:00.341268
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    host = Host(name="localhost")
    group = Group(name="all")
    inventory.add_host(host)
    inventory.add_group(group)
    inventory.add_child

# Generated at 2022-06-13 08:59:05.341714
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play

    play = Play.load('', dict(name='foo', hosts=''))

    assert isinstance(play, Play)
    assert hasattr(play, '_name')
    assert hasattr(play, '_hosts')

    data = dict(name='foo', hosts='')

    ri = RoleInclude.load(data, play=play)

    assert isinstance(ri, RoleInclude)

    data = dict(name='foo', hosts='', tasks=[])

    ri = RoleInclude.load(data, play=play)

    assert isinstance(ri, RoleInclude)

    data = dict(name='foo', hosts='', roles=[])

    ri = RoleInclude.load(data, play=play)

    assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:59:33.837005
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.mod_args import ModuleArgsParser

    display = Display()

    yaml_str = '''
    - hosts: localhost
      roles:
        - test
        - { role: test,
            delegate_to: localhost,
            delegate_facts: yes,
            tags: [ 'test'] }
        - test
    '''

    playbooks = list(Playbook.load(yaml_str, variable_manager=VariableManager(), loader=AnsibleLoader(ModuleArgsParser(None))))

# Generated at 2022-06-13 08:59:44.523151
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class DummyRoleDefinition(RoleDefinition):
        def __init__(self, data):
            self.data = data

    class DummyPlay(object):
        def __init__(self, roles_path, variable_manager, loader):
            self.roles_path = roles_path
            self.variable_manager = variable_manager
            self.loader = loader

    class DummyVariableManager(object):
        def __init__(self, loader, inventory):
            self.loader = loader
            self.inventory = inventory

    class DummyInventory(object):
        pass

    class DummyLoader(object):
        def __init__(self, path):
            self.path = path

    # simple-string-role-name
    roles_path = 'path'
    data = 'simple-string-role-name'
    variable_

# Generated at 2022-06-13 08:59:51.487308
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = 'test_case_test'
    play = dict(hosts='all')
    current_role_path = None
    parent_role = 'base'
    variable_manager = None
    loader = None
    obj = ri.load(data, play, current_role_path, parent_role, variable_manager, loader)
    assert obj._role_name == 'test_case_test'
    assert obj._role_path == 'test_case_test'



# Generated at 2022-06-13 08:59:52.448903
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "Test not implemented"

# Generated at 2022-06-13 09:00:02.398322
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.utils.vars import load_extra_vars

    # Create a play

# Generated at 2022-06-13 09:00:09.693044
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    print("\n\nTest method load of class RoleInclude")

    import os
    import inspect
    import sys
    import types
    import ast

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.plugins.loader import filter_loader
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 09:00:15.845085
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import sys
    import unittest
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.parsing.yaml.data import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import vars_loader
    from ansible.utils.vars import combine_vars

    def test_case_load_1():
        data = 'A'
        play = Play()
        result = RoleInclude.load(data, play)
        assert result.get_name() == data
        assert result.get_role_path() == play.get_role_path()

   

# Generated at 2022-06-13 09:00:24.989141
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import pytest

    class Obj(object):pass

    play = Obj()
    play.basedir = ''

    data = '''
    - name: test
      hosts: all
      roles:
        - { role: test, something: test}
    '''

    with pytest.raises(AnsibleParserError) as excinfo:
        ri = RoleInclude(play=play)
        ri.load(data)
    assert 'Invalid role definition' in to_native(excinfo.value)

    data = '''
    - name: test
      hosts: all
      roles:
        - { role: test }
    '''

    ri = RoleInclude(play=play)
    ri.load(data)

    pass

# Generated at 2022-06-13 09:00:31.495729
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test init
    play = {'hosts': 'host1,host2', 'name': 'role_name'}
    current_role_path = '/ansible/roles/role_1'
    role_var_manager = {}
    loader = ''
    collection_list = {}

    ri = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=role_var_manager, loader=loader, collection_list=collection_list)

    # test with load_data
    data = 'role1'
    role = ri.load_data(data, variable_manager=role_var_manager, loader=loader)
    assert isinstance(role, RoleRequirement)

    # test with load function

# Generated at 2022-06-13 09:00:41.266938
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader

    cwd = os.path.dirname(os.path.realpath(__file__))
    mock_loader = AnsibleLoader(None, None)
    context = PlayContext()
    variable_manager = VariableManager()

    ri = RoleInclude(collection_list=['foo.bar'])

    # if data is not a string,dict,AnsibleBaseYAMLObject,raise AnsibleParserError
    data = object()

# Generated at 2022-06-13 09:01:16.281434
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = AnsibleLoader(None, None)

    # define data to load
    data = '''
    - include: test_task_include.yml
      delegate_to: localhost
      delegate_facts: yes
    '''

    # set the role_basedir to the appropriate path of the test files
    current_role_path = os.path.dirname(os.path.abspath(__file__))

    # create the variables
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'localhost': {}}}

    # create the inventory

# Generated at 2022-06-13 09:01:25.189113
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.plugins.callback import CallbackBase

    class EmptyCallback(CallbackBase):
        pass

    class EmptyTaskQueueManager(TaskQueueManager):
        pass

    class EmptyPlayContext(PlayContext):
        pass

    class EmptyVaultSecret:
        pass

    class EmptyVariableManager:
        pass

    # Create new PlayContext
    pc = EmptyPlayContext()

    # Create new VariableManager
    vm = EmptyVariableManager()

    # Create new VaultSecret
    vs = EmptyVaultSecret()

    # Create new TaskQueueManager

# Generated at 2022-06-13 09:01:30.293663
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Verify that the correct error is thrown when loading an old style role requirement.
    """
    # Setup fixture
    data = "role1, role2"
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    assert_error(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)

    # Teardown fixture
    data = None
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None


# Generated at 2022-06-13 09:01:44.264094
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils import context_objects as co


# Generated at 2022-06-13 09:01:50.567676
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Construct playbook with play(s)
    playbook = Playbook()
    play = Play()
    play.name = "test"
    playbook._entries.append(play)
    play.post_validate(playbook)

    # Construct task, handler and block
    task = Block()
    handler = Block()
    block = Block()
    play.block = block

    # set ansible environment varibles for testing

# Generated at 2022-06-13 09:01:59.375572
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory_simple'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    # test string input
    try:
        data = 'foo'
        RoleInclude.load(data, play_context, variable_manager)
    except AnsibleParserError as e:
        assert "Invalid role definition" in str(e)

    # test dict input