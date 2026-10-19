

# Generated at 2022-06-13 08:52:18.094439
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    test_loader = DictDataLoader({
        "index.yml": "index_yml_content",
        "index.yaml": "index_yaml_content",
    })

    test_collection_list = [
        FileCollection("foo.bar.baz", ["index.yml"])
    ]

    # Test with data set to a string
    test_data = "foo.bar.baz"
    test_play = None
    test_current_role_path = "/test/Current/Role/Path"
    test_parent_role = None
    test_variable_manager = None
    test_return = RoleInclude.load(test_data, test_play, test_current_role_path, test_parent_role, test_variable_manager, test_loader, test_collection_list)
    assert test_

# Generated at 2022-06-13 08:52:27.484113
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    testkeys = {'description','role','vars','defaults','pre_tasks','tasks','post_tasks','handlers','tags'}
    testplay = {}
    testpath = ""
    testparent = {}
    testvars = {}
    testloader = {}
    testcl = {}

    # Test bad data
    assert RoleInclude.load(None, testplay, testpath, testparent, testvars, testloader, testcl) == None

    # Test bad old style data
    assert RoleInclude.load("badstuff", testplay, testpath, testparent, testvars, testloader, testcl) == None

    # Test good data
    newrole = RoleInclude.load({'role': 'testrole'}, testplay, testpath, testparent, testvars, testloader, testcl)

# Generated at 2022-06-13 08:52:37.706560
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook.play import Play
    from ansible.parsing.mod_args import ModuleArgsParser
    import ansible.constants as C
    from ansible.plugins import module_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host, Group
    from ansible.inventory.group import Group
    from ansible.vars.hostvars import HostVars

    module_loader.add_directory(C.DEFAULT_MODULE_PATH)

    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)

# Generated at 2022-06-13 08:52:47.855798
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook.play_context
    import ansible.inventory.host
    import ansible.vars.manager
    import ansible.loader
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    h = ansible.inventory.host.Host('testhost')
    t = Task()
    b = Block()
    p = Play().load({}, loader=ansible.loader.Loader(), variable_manager=ansible.vars.manager.VariableManager(),
                    block_list=[b])
    b.set_loader(ansible.loader.Loader())
    ri = RoleInclude()
    ri.set_loader(ansible.loader.Loader())

# Generated at 2022-06-13 08:53:00.219146
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.plugins import module_loader
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../test/units/modules'))
    variable_manager = VariableManager()
    loader = DataLoader()
    playbook = Play().load("play_name", dict(
        name="play_name",
        hosts=['all'],
        gather_facts='no',
        tasks=[]
    ), variable_manager=variable_manager, loader=loader)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_

# Generated at 2022-06-13 08:53:10.315067
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    hostvars = dict()
    groups = dict()
    groups['group1'] = ['localhost', '192.168.1.1']
    hostvars['localhost'] = {'ansible_ssh_port': 22}
    hostvars['192.168.1.1'] = {'ansible_ssh_port': 2222}
    new_vm = dict()
    new_vm['hosts'] = ['localhost', '192.168.1.1']
    new_vm['vars'] = {'ansible_ssh_port': 2222}
    result = dict()
    result['hostvars'] = hostvars
    result['groups'] = groups
    result['_meta'] = {'hostvars': hostvars}
    #result['new_vm'] = new_vm
    fake_loader, _, fake_

# Generated at 2022-06-13 08:53:16.728377
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    a = {}
    b = {}
    c = {}
    loader = {}

    # test
    with pytest.raises(AnsibleParserError) as excinfo:
        RoleInclude.load(a, b, current_role_path=None, parent_role=None, variable_manager=None, loader=loader, collection_list=None)
    assert "Invalid role definition:" in str(excinfo.value)

    # test
    with pytest.raises(AnsibleError) as excinfo:
        RoleInclude.load("a,b", b, current_role_path=None, parent_role=None, variable_manager=None, loader=loader, collection_list=None)
    assert "Invalid old style role requirement:" in str(excinfo.value)

# Generated at 2022-06-13 08:53:17.583836
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:53:31.574435
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = [
        "role1",
        "role1,role2",
        {'role': 'role_with_dict'},
        "role_with_subdict",
        "role_with_subdict:sub_role",
        "role_with_subdict:sub_role2:subsub_role",
        "role_with_subdict:sub_role2:subsub_role,role_with_subdict:sub_role3:subsub_role3",
        "role_with_subdict:sub_role2:subsub_role,subsub_role2",
        ]
    for d in data:
        print(RoleInclude.load(d, None))
    print("All tests passed")

if __name__ == '__main__':
    test_RoleInclude_load()

# Generated at 2022-06-13 08:53:39.492982
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(PlayContext())
    ri1 = RoleInclude.load({"role": "nginx"}, None)
    assert ri1.get_name() == "nginx"
    ri2 = RoleInclude.load({"role": "myrole"}, None)
    assert ri2.get_name() == "myrole"
    ri3 = RoleInclude.load({"role": "testnginx"}, None)
    assert ri3.get_name() == "testnginx"
    ri4 = RoleInclude.load({"role": "testnginxfail"}, None)

# Generated at 2022-06-13 08:53:49.886716
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves import configparser

    o_config = configparser.RawConfigParser()
    o_config.readfp(StringIO(u'[defaults]\nroles_path = /tmp'))

    o_play = Play().load(dict(
        name = u'test play',
        hosts = u'testhost',
        gather_facts = u'no',
        tasks = [
            dict(action=dict(module=u'mymodule', args=u''), register=u'result')
        ]
    ), variable_manager=None, loader=None)


# Generated at 2022-06-13 08:53:59.849906
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class DummyLoader:

        def __init__(self):
            self.paths = []

        # Return fake path
        def path_dwim(self, path):
            self.paths.append(path)
            return os.path.join('path', 'to', 'fake', 'roles')

    class DummyVariableManager:

        def __init__(self):
            self.host_vars = {}
            self.host_vars['host_one'] = None
            self.host_vars['host_two'] = None

        def get_vars(self, loader=None, play=None, host=None, task=None):

            ALL_VARS = {}
            ALL_VARS['all_var'] = 'all_var'

            HOST_TWO_VARS = ALL_VARS.copy

# Generated at 2022-06-13 08:54:06.283428
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import ansible.playbook.role.definition
    from ansible.parsing.dataloader import DataLoader

    # test for data None; assert that this throws a TypeError for the assertion that data is a string
    ri = RoleInclude()
    data = None
    try:
        ri.load(data)
    except TypeError as e:
        assert type(e) == TypeError

    # test for an empty string for data; assert that this throws an AnsibleParserError for the assertion that data is not a string
    ri = RoleInclude()
    data = ""
    try:
        ri.load(data)
    except AnsibleParserError as e:
        assert type(e) == AnsibleParserError

    # test for a string with a value that is a path; assert that this throws an AnsibleError for the

# Generated at 2022-06-13 08:54:08.565421
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # VariableManager and loader are None, since they are not needed for this test
    ri = RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=None)
    data = "test"
    try:
        ri.load(data=data)
    except AnsibleParserError:
        pass
    # Since data is string_type, AnsibleParserError is raised


# Generated at 2022-06-13 08:54:13.077819
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data_dict = { "name": "test" }
    current_role_path = "/test_path"
    variable_manager = None
    loader = None
    collection_list = ""
    play = None
    ri = RoleInclude.load(data=data_dict, play=play, current_role_path=current_role_path, variable_manager=variable_manager,
                          loader=loader, collection_list=collection_list)
    assert ri._role_name == "test"
    assert ri._role_path == "/test_path/test"

# Generated at 2022-06-13 08:54:24.317734
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    my_loader = DataLoader()
    my_inventory = InventoryManager(loader=my_loader, sources=['/etc/ansible/hosts'])
    # Home_dir is needed since it's not set in ansible.cfg

# Generated at 2022-06-13 08:54:35.028764
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    test0 = 'test0'
    print(RoleInclude.load(data=test0))

    print(RoleInclude.load(data=dict()))
#   print(RoleInclude.load(data=AnsibleBaseYAMLObject())) # It's a BaseException!

    from ansible.parsing.yaml.loader import AnsibleLoader
    data = AnsibleLoader(None, None).load_from_file('../../tests/yaml/role_include.yml')
    print(RoleInclude.load(data=data))
    print(RoleInclude.load(data=data, play='test12'))
    print(RoleInclude.load(data=data, play='test12', current_role_path='dir'))

# Generated at 2022-06-13 08:54:38.995141
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Make sure that the load method does not allow comma separated role requirements.
    """

    with pytest.raises(AnsibleError) as exception:
        RoleInclude.load(data="foo,bar", play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert str(exception.value) == "Invalid old style role requirement: foo,bar"


# Generated at 2022-06-13 08:54:40.023481
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Add your unit test here
    pass

# Generated at 2022-06-13 08:54:50.798924
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:54:56.348636
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test invocation with valid data types
    # invocation with string_type should pass
    # invocation with dict should pass
    # invocation with AnsibleBaseYAMLObject should pass

    # exception should be raised if data is not string, dict or AnsibleBaseYAMLObject
    assert True

# Generated at 2022-06-13 08:54:57.403550
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:55:08.580903
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.collection.collection_loader import AnsibleCollectionConfig

    loader = DataLoader()
    collection_loader = AnsibleCollectionConfig.load_collections(loader)
    inventory = InventoryManager(loader, sources='localhost,')
    variable_manager = VariableManager(loader, inventory)

# Generated at 2022-06-13 08:55:17.989975
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test data
    data_all_dict = dict(
        name="foo",
        hosts="host1",
        vars=dict(
            foo="bar",
            baz="boo"
        ),
        tasks=dict(
            main=dict(
                debug=dict(
                    msg="this is a test"
                )
            )
        )
    )
    data_dict = dict(
        name="foo",
        hosts="host1",
        vars=dict(
            foo="bar",
            baz="boo"
        )
    )
    data_none_dict = dict(
        name="foo",
        hosts="host1"
    )
    data_str = dict(
        name="foo",
        hosts="host1"
    )
    # unit test code
    # 1.

# Generated at 2022-06-13 08:55:28.851737
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Mock up the objects needed to call load()
    loader_mock = mock.MagicMock()
    variable_manager_mock = mock.MagicMock()
    ri = RoleInclude(play=None, role_basedir=None, variable_manager=variable_manager_mock, loader=loader_mock)

    # Call load()
    role_def = ri.load({'name': 'test_role_include'},
                       variable_manager=variable_manager_mock, loader=loader_mock)

    # Assert that the load_data() method is called with the data and the keyword
    # arguments returned by the load() method.

# Generated at 2022-06-13 08:55:38.902457
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook
    from ansible.playbook.role.meta import RoleMetadata

    pb = ansible.playbook.Playbook()
    vm = ansible.playbook.Playbook.variable_manager_from_play(pb, pb._loader)

    ri = RoleInclude.load('role', play=pb, variable_manager=vm, loader=pb._loader)
    assert isinstance(ri, RoleInclude)


    ri = RoleInclude.load({'role': 'role', 'meta': 'file'}, pb, vm, pb._loader)
    assert isinstance(ri, RoleInclude)


# Generated at 2022-06-13 08:55:40.901889
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "test"
    ri = RoleInclude.load(data=data)

    assert isinstance(ri, RoleInclude)
    assert ri._role_name == data

# Generated at 2022-06-13 08:55:42.591539
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: Implement test to make sure that provided data is always a string or a dict
    pass


# Generated at 2022-06-13 08:55:53.880966
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars

    class Playbook:
        def __init__(self):
            self.basedir = ''
            self.host_list = []
            self.vars = {'test_key': 'test_val'}
            self.vars_files = {}

    class Options:
        def __init__(self):
            self.connection = 'local'
            self.module_path = []
            self.private_key_file = None
            self.become = False
            self.become_user = ''
            self.become_method = ''
            self.remote_user

# Generated at 2022-06-13 08:56:01.539562
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    variable_manager = DummyVarsModule()
    loader = DummyLoaderModule()
    data = {"requirements":"foo"}
    play = DummyPlayClass()
    current_role_path = "/dir/dir2"
    parent_role = DummyRoleClass()
    collection_list = []

    ri = RoleInclude.load(data=data, play=play, current_role_path=current_role_path,
                          parent_role=parent_role, variable_manager=variable_manager,
                          loader=loader, collection_list=collection_list)

    assert isinstance(ri, RoleInclude)
    assert isinstance(ri.requirements, list)
    assert len(ri.requirements) == 1
    assert isinstance(ri.requirements[0], RoleRequirement)

# Generated at 2022-06-13 08:56:17.189296
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test data
    data = 'test'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    # Expected result
    result = AnsibleError("Invalid old style role requirement: %s" % data)
    # init RoleInclude
    role_include = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    # Test execute
    with pytest.raises(AnsibleError) as excinfo:
        role_include.load(data, variable_manager=variable_manager, loader=loader)
    assert excinfo.value.message == result.message

    # Test data
    data = '123'

# Generated at 2022-06-13 08:56:24.208305
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Making sure that the class RoleInclude loads a RoleInclude with the right properties
    """

    # Setting up data and variable manager
    data = dict(name='role')
    variable_manager = FakeVariableManager()
    loader = FakeLoader()

    # Loading role
    r = RoleInclude.load(data, variable_manager=variable_manager, loader=loader)

    # Checking if the properties are as expected
    assert r.get_name() == 'role'
    assert r.get_role_path() == data['name']
    assert r.get_variable_manager() == variable_manager
    assert r.get_loader() == loader
    assert r._role_params == {}
    assert r._metadata == {}



# Generated at 2022-06-13 08:56:34.307472
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath
    from ansible.utils.vars import combine_vars

    variable_manager = VariableManager()
    loader = DictDataLoader({})

    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager, fail_on_undefined=True)
    data = ansible_mock
    #####################################################################################
    # Test for load of RoleInclude
    #####################################################################################
    result

# Generated at 2022-06-13 08:56:44.015276
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class Test(RoleInclude):

        def __init__(self, play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None):
            super(RoleInclude, self).__init__(play=play, role_basedir=role_basedir, variable_manager=variable_manager,
                                              loader=loader, collection_list=collection_list)


# Generated at 2022-06-13 08:56:52.340001
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.abspath(__file__) + '/../'))
    from ansible.playbook.play_context import PlayContext
    a = RoleInclude()
    a.load("ansible-role-test", play = None, current_role_path = None, parent_role = None, variabl_manager = None, loader= None)
    assert a._role_name == 'ansible-role-test'
    assert a.get_name == 'ansible-role-test'
    assert a.get_role_name == 'ansible-role-test'
    assert a._role_path == 'ansible-role-test'
    assert a._role_path_safe == 'ansible-role-test'
    assert a._role

# Generated at 2022-06-13 08:56:57.803700
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {}
    loader = None
    current_role_path = ''
    parent_role = None
    play = None
    variable_manager = None
    collection_list = None
    try:
        RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleParserError:
        return
    assert False
# Unit test: Ends

# Generated at 2022-06-13 08:57:02.418787
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role = {
        'role1': {
            'hosts': 'host1',
            'vars': {'a': 'b'},
            'roles': [
                {'role': 'role2', 'x': 1},
                {'role': 'role3', 'x': 2},
                {'role': 'role4', 'x': 3},
            ]
        }
    }
    ri = RoleInclude.load(role, None)
    assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:57:10.267705
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.errors import AnsibleParserError, AnsibleError
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.utils.vars import combine_vars
    from sys import version_info

    class SimpleRoleRequirement(object):

        def __init__(self, name, version, scm, src, path):
            self.name = name
            self.role = None
            self.version = version
            self.scm = scm
            self.src = src
            self.path = path

        def get_name(self):
            return self.name

        def get_role(self):
            return self.role


# Generated at 2022-06-13 08:57:21.400360
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    test_data = dict(
        name='test',
        tasks=dict(
            task1=dict(
                name='test task 1',
                debug=dict(
                    msg='test message'
                )
            ),
            task2=dict(
                name='test task 2',
                debug=dict(
                    msg='test message'
                )
            )
        )
    )
    role_basedir = "roles_path"
    ri = RoleInclude(play=None, role_basedir=role_basedir, variable_manager=None, loader=None)
    result = ri.load_data(test_data, variable_manager=None, loader=None)

    assert result is not None
    assert result._role_path == os.path.join(role_basedir, test_data['name'])



# Generated at 2022-06-13 08:57:25.869097
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test method load of class RoleInclude in module role/include.
    """

    ri = RoleInclude()
    ri.load_data('role1')

# Generated at 2022-06-13 08:57:47.083970
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "defaults/main.yml"
    role_basedir = "/current/path"
    ri = RoleInclude.load(data, role_basedir=role_basedir)
    assert isinstance(ri, RoleInclude)
    assert ri.role_basedir == "/current/path"
    assert ri.role_name is None
    assert ri.role_path is None
    assert ri.role_params is None
    data = "name: role_name"
    ri = RoleInclude.load(data, role_basedir=role_basedir)
    assert isinstance(ri, RoleInclude)
    assert ri.role_basedir == "/current/path"
    assert ri.role_name == "role_name"
    assert ri.role_path is None

# Generated at 2022-06-13 08:57:54.500839
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    role_include_string = '''
- role: apache
  when: ansible_os_family == 'RedHat'
  tags:
    - cron
    - foo
- role: ntp
  when: ansible_os_family == 'RedHat'
  tags:
    - cron
    - foo
- role: common
  tags:
    - cron
    - foo
- role: mysql
  tags:
    - db
    - foo
- role: php
  tags:
    - web
    - foo
    - php

'''


# Generated at 2022-06-13 08:57:55.575332
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:58:00.285389
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = "/tmp/foo"
    try:
        ri.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
        assert False
    except AnsibleError:
        pass

# Generated at 2022-06-13 08:58:08.458106
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    fake_data = 'fake_data'
    fake_play = 'fake_play'
    fake_current_role_path = 'fake_current_role_path'
    fake_parent_role = 'fake_parent_role'
    fake_variable_manager = 'fake_variable_manager'
    fake_loader = 'fake_loader'
    fake_collection_list = 'fake_collection_list'

    # Try it with string data that does not contain a comma
    data = 'string_data'
    ri = RoleInclude.load(data=data, play=fake_play, current_role_path=fake_current_role_path,
                          parent_role=fake_parent_role, variable_manager=fake_variable_manager,
                          loader=fake_loader, collection_list=fake_collection_list)

# Generated at 2022-06-13 08:58:15.338944
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Load role include which has valid role definition
    import ansible.playbook
    import ansible.module_utils.six
    import ansible.parsing.yaml.objects
    import ansible.module_utils._text
    import ansible.module_utils.common.collections

    play = ansible.playbook.Play()
    current_role_path = 'path'
    parent_role = None
    variable_manager=None
    loader=None

    data = 'role_def'
    ri_valid = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader)
    assert(ri_valid.role_name == 'role_def')

    # Load role include which has invalid role definition
    data = 'role_def,role_def2'

# Generated at 2022-06-13 08:58:26.232470
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # define test variables
    class Dummy1:
        play = None
        role_basedir = None
        variable_manager = None
        loader = None
        collection_list = None

    class Dummy2:
        name = 'dummy'
    class Dummy3:
        play = None
        role_basedir = None
        variable_manager = None
        loader = None
        collection_list = None
    testvar = 'testvar'
    data = {
        'name': 'test',
        'tasks': [
            {
                'action': {
                    'module': 'test',
                    'name': 'test'
                },
                'name': 'test'
            }
        ]
    }
    test = Dummy1
    # test method
    result = RoleInclude.load(data, test)


# Generated at 2022-06-13 08:58:28.322997
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    m = RoleInclude()
    assert m.load("name") == m

# Generated at 2022-06-13 08:58:43.752604
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    display = Display()
    play = Play().load({}, loader=None, variable_manager=None)
    data = RoleMetadata().load({'name': 'common'}, play=play, loader=None, variable_manager=None)
    role_path = '/home/michael/ansible/roles'
    result = RoleInclude.load(data, play, current_role_path=role_path, parent_role=None, variable_manager=None, loader=None)
    assert result._metadata is not None
    assert result._delegate_to is None
    assert result._delegate_facts is False



# Generated at 2022-06-13 08:58:45.328112
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "TODO"

# Generated at 2022-06-13 08:59:14.155347
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # This test failed with the following error:
    # "AssertionError: exception message != 'Invalid old style role requirement: ansible.builtin.apt,ansible.builtin.yum'"
    # The actual error message was "Invalid old style role requirement: ansible.builtin.apt,ansible.builtin.yum"
    # This test has been fixed to adjust this.
    #
    # The following test errors out with the following error message:
    # "TypeError: __init__() got an unexpected keyword argument 'role_basedir'"
    # This test has been fixed to remove the 'role_basedir' attribute as this is not used in the tested function.
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
   

# Generated at 2022-06-13 08:59:31.335893
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:59:37.997801
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test load method of class RoleInclude
    :return:
    """
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    test_play = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        vars = {
            'package' : 'nginx',
            'state' : 'present'
        },
        roles = [
            'cn.epaylinks.www',
            'cn.epaylinks.www,test=test'
        ]
    )

    inventory = InventoryManager(loader=None, sources=['localhost'])
    variable_manager = VariableManager(loader=None, inventory=inventory)

# Generated at 2022-06-13 08:59:47.107201
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    variable_manager = DummyVariableManager()
    variable_manager._options = DummyOptions()
    variable_manager._options.roles_path = ['./']
    loader = DataLoader()
    ri = RoleInclude(variable_manager=variable_manager, loader=loader)
    data = {'role': 'role.name', 'name': 'Role name'}
    r = ri.load_data(data, variable_manager=variable_manager, loader=loader)
    assert type(r) is RoleInclude
    assert r._role_name == 'role.name'
    assert r._role_path is None


# Generated at 2022-06-13 08:59:57.457975
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import os
    import sys
    import unittest
    import tempfile
    import shutil

    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    from ansible.playbook.base import Base
    from ansible.playbook.role import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.template import Templar

    from ansible.plugins.loader import add_all_plugin_dirs


# Generated at 2022-06-13 09:00:06.264815
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Easy test.
    data = '''
- hosts: webserver
  vars_files:
    - foo.yml
  roles:
    - my-role
    - { role: my-role, when: something }
    - { role: foo, tasks_from: my-tasks.yml }
    - { role: foo, tasks_from: "{{ foo_var.bar }}" }
    - my-role-1
  tasks:
    - debug: msg="test"
'''

    def exec_test_RoleInclude_load(test_data):
        from ansible.playbook.play import Play
        from ansible.vars import VariableManager
        from ansible.inventory import Inventory
        from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:00:09.233543
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    x = ri.load('foo')
    assert x.role_name == 'foo'

    import pdb; pdb.set_trace()
    x = ri.load("foo:")
    assert x.role_name == 'foo'

# Generated at 2022-06-13 09:00:15.602927
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = AnsibleBaseYAMLObject.__new__(AnsibleBaseYAMLObject)
    data.data = dict()
    data.data['name'] = 'example_role'
    data.data['tasks'] = 'a'
    data.data['vars'] = 'b'
    data.data['defaults'] = 'c'
    data.data['meta'] = 'd'
    data.data['handlers'] = 'e'
    data.data['pre_tasks'] = 'f'
    data.data['post_tasks'] = 'g'
    data.data['tasks_from'] = 'h'
    data.data['vars_from'] = 'i'

    ri = RoleInclude.load(data)

    assert ri.name == data.data['name']
   

# Generated at 2022-06-13 09:00:25.439555
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars


    data = '''
    - hosts: all
      vars:
        foo: bar
      tasks:
        - name: hello
          debug: msg="Hello world"
    '''

    loader_mock = MagicMock()
    loader_mock._get_basedir = MagicMock(return_value='/tmp')
    play = Play().load(data, loader=loader_mock, variable_manager=VariableManager())
    default_vars = VariableManager()

# Generated at 2022-06-13 09:00:35.220732
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_queue_manager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.utils.vars import combine_vars
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.errors import AnsibleParserError
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_native
    import collections

    variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-13 09:01:30.757795
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.vault.vault import VaultLib
    import ansible.parsing.vault as vault
    import ansible.playbook.role.requirement as req
    import ansible.playbook.play as play
    import ansible.playbook.playbook as playbook
    import ansible.playbook.role as role
    import ansible.template as template
    from ansible.module_utils.six import iteritems, string_types
    import ansible.inventory.manager as manager
    import ansible.plugins.loader as loader
    import ansible.parsing.yaml.objects as objects

    v = VaultLib([])
    data = 'tests/data/vault/vault-id.yml'
    vdata = v.load_vault_id_file(data)
    vault.V

# Generated at 2022-06-13 09:01:39.991910
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    mock_play = {}
    mock_role_basedir = ''
    mock_variable_manager = {}
    mock_loader = {}
    mock_collection_list = {}

    with pytest.raises(AnsibleParserError) as excinfo:
        RoleInclude.load('', mock_play, mock_role_basedir, None, mock_variable_manager, mock_loader, mock_collection_list)

    assert excinfo.value.message == "Invalid role definition: ''"


# Generated at 2022-06-13 09:01:47.748405
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Unit test for method load of class RoleInclude
    # Given a playbook variable manager, a fake loader and a variable_manager
    variable_manager = None
    loader = ''
    variable_manager = ''
    # When a role is created with a None play and a None variable_manager
    ri = RoleInclude(play=None, role_basedir=None, variable_manager=variable_manager, loader=loader)
    # Then a AttributeError exception is raised, because the method load of class RoleDefinition need
    # that a play is not None
    if ri:
        raise AttributeError("The play for this RoleInclude must not be None.")

# Generated at 2022-06-13 09:01:57.864732
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.module_utils._text import to_bytes
    play = Play.load(dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    ), variable_manager=None, loader=None)

    role_path = os.path.abspath(os.path.dirname(__file__))

# Generated at 2022-06-13 09:01:58.385009
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 09:02:04.558652
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    ####################################################################################################################
    #   Test code for method load of class RoleInclude                                                                 #
    ####################################################################################################################

    loader_obj = DataLoader()

# Generated at 2022-06-13 09:02:08.297067
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    ri.load({'role': 'web-server'}, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None)


# Generated at 2022-06-13 09:02:16.297923
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    #Test1: Test load
    role = RoleInclude()
    role = role.load("role_definition", play = None, current_role_path = "current_role_path", parent_role = None, variable_manager=None, loader=None, collection_list=None)
    assert role._role_path == "current_role_path"
    assert role._role_params == {}

    #Test2: Test load for old style role requirement