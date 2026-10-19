

# Generated at 2022-06-13 08:31:42.316958
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
	play = Play()
	play.vars_files = ['/etc/ansible/x.yml', '/etc/ansible/a.yml', '/etc/ansible/b.yml']
	result = play.get_vars_files()
	assert result == ['/etc/ansible/x.yml', '/etc/ansible/a.yml', '/etc/ansible/b.yml']
	play.vars_files = None
	result = play.get_vars_files()
	assert result == []
	play.vars_files = '/etc/ansible/x.yml'
	result = play.get_vars_files()
	assert result == ['/etc/ansible/x.yml']

# Generated at 2022-06-13 08:31:48.337679
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'play_name'
    assert p.get_name() == 'play_name'
    p.name = None
    p.hosts = 'hosts'
    assert p.get_name() == 'hosts'
    p.hosts = None
    assert p.get_name() == ''


# Generated at 2022-06-13 08:31:58.699836
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

# Generated at 2022-06-13 08:32:12.379395
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    def get_tasks_func(Play, self):
        return Play.get_tasks(self)
    # Set up mock inventory and task loader
    loader_mock = MagicMock()
    # Specify my_play name
    play_name = "Test Play"
    # Specify my_play hosts
    play_hosts = ['localhost']
    # Specify my_play tasks
    play_tasks = [DummyTask('task1', {})]
    # Specify my_play roles
    play_roles = []
    # Specify my_play vars
    play_vars = {'var_value': 'Some Value'}
    # Specify my_play vars_files
    play_vars_files = ['vars_file.yml']
    # Specify my_play include_roles
   

# Generated at 2022-06-13 08:32:18.192961
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    ds = {   'hosts': 'testhost1',
             'vars': {'testvar': 'testval'},
             'vars_files': ['/user/home/testfile']}
    pl = Play.load(ds, None, None)
    a = pl.deserialize(pl.serialize())
    assert a._ds == ds


# Generated at 2022-06-13 08:32:23.942308
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    def run(data):
        p = Play()
        ds = p.preprocess_data(data)
        return ds
    #### utility function end ####

    with pytest.raises(AnsibleAssertionError):
        run("string")

    with pytest.raises(AnsibleParserError):
        run({'user':'remote_user'})

    with pytest.raises(AnsibleParserError):
        run({'remote_user':'remote_user', 'user':'user'})

    assert run({'user':'user'}) == {'remote_user':'user'}

# Generated at 2022-06-13 08:32:33.462701
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Given
    data = {
        "hosts": "all",
        "roles": [
            "httpd",
            {
                "name": "nginx",
                "vars": {
                    "foo": "bar"
                }
            }
        ]
    }
    play = Play.load(ds=data, loader=None, variable_manager=None)
    result = play.compile_roles_handlers()
    assert result == [], result

# Generated at 2022-06-13 08:32:41.915567
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    host = Host("192.168.1.1")
    hostlist = [host]
    var = C.DEFAULT_HOST_LIST
    variable_mgr = VariableManager(loader=None,host_list=hostlist)
    variable_mgr.set_host_variable(host=host,var=var,value=hostlist)

    play = Play.load(dict(
        name="Test Play",
        hosts='all',
        gather_facts='no',
        roles=["test_role"]
    ), variable_manager=variable_mgr)

    block_list = play.compile_roles_handlers()
    assert len(block_list) > 0

# Generated at 2022-06-13 08:32:52.950350
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:33:01.411201
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Test play compilation
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.role.meta import RoleMeta
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task

    my_play_source = '''
- name: play1
  hosts: localhost
  vars:
    key: value
  roles:
    - test_role1
    - test_role2
    - test_role3
'''
    pb = Play.load(my_play_source, variable_manager=VariableManager(), loader=DataLoader())
   

# Generated at 2022-06-13 08:33:23.274137
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Arrange
    test_play = mock_play(path='./tests/unit/fixtures/roles/include_handler_definition/')

    # Act
    result = test_play.compile_roles_handlers()

    # Assert
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Handlers)
    assert len(result[0].items) == 2
    assert isinstance(result[0].items[0], (Task, Handler))



# Generated at 2022-06-13 08:33:24.326623
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    pass


# Generated at 2022-06-13 08:33:29.834582
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
	play = Play()
	play.roles = [Role(), Role()]
	play.roles[1].get_handler_blocks = lambda: [Handler(), Handler()]
	assert play.roles[0] not in [handler.parent for handler in play.compile_roles_handlers()]
	assert play.roles[1] in [handler.parent for handler in play.compile_roles_handlers()]
	assert 2 == len(play.compile_roles_handlers())
#

# Generated at 2022-06-13 08:33:36.260379
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
    Unit test of method Play.compile_roles_handlers(self)
    '''
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    # Declaration of variables and objects
    file_name='test/unit/playbook/fixtures/playbooks/playbook_for_unit_test.yaml'
    play_name='test_unit_Play_compile_roles_handlers'

    # Declaration of the global variable
    data_loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:33:51.443377
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    #test_Play_compile_roles_handlers()
    test_pass = True

    # test play creation

# Generated at 2022-06-13 08:34:03.649170
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    results = [
        dict(hosts='host1.example.com').items(),
        dict(hosts='host2.example.com').items(),
        dict(hosts='host3.example.com').items()
    ]

    p = Play()
    p.play_hosts = dict(
        host1 = dict(
            hosts = dict(
                    host1 = dict(
                        groups = ['g1']
                    )
                ),
            groups = ['g1']
        ),
        host2 = dict(
            groups = ['g2']
        ),
        host3 = dict(
            groups = ['g1', 'g2']
        )
    )

    results = p.compile_roles_handlers()

# Generated at 2022-06-13 08:34:14.232928
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = playbook.Play()
    play._load_roles(0, [{'import_playbook': '/etc/ansible/main.yml', 'vars': {}},
                         {'import_playbook': '/etc/ansible/common.yml', 'vars': {}},
                         {'import_playbook': '/etc/ansible/host.yml', 'vars': {}}])
    play._variable_manager = VariableManager()
    play._loader = DataLoader()
    play._loader.set_basedir('/etc/ansible')
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:34:26.306587
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    class MockPlay():
        def __init__(self):
            self.pre_tasks = ['a','b']
            self.tasks = ['c','d']
            self.post_tasks = ['e','f']
    fake_play = MockPlay()
    fake_play.get_tasks()
    fake_play.pre_tasks = [1,2]
    fake_play.get_tasks()
    fake_play.tasks = [3,4]
    fake_play.get_tasks()
    fake_play.post_tasks = [5,6]
    fake_play.get_tasks()
    fake_play.tasks = []
    fake_play.get_tasks()
    fake_play.post_tasks = []
    fake_play.get_tasks()
   

# Generated at 2022-06-13 08:34:38.572961
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    my_host = Host("127.0.0.1")

# Generated at 2022-06-13 08:34:45.001775
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    yaml_data = """
---
- debug: var=hostvars[inventory_hostname]['ansible_facts']['kernel_name']
  hosts:
    - all
"""
    loader = DataLoader()
    play = Play.load(yaml_data, loader=loader)
    play.serialize()
    assert play.data == {'hosts': 'all', 'tasks': [{'debug': 'var=hostvars[inventory_hostname][\'ansible_facts\'][\'kernel_name\']'}]}
    assert play.hosts == 'all'
    assert play.tasks == [{'debug': 'var=hostvars[inventory_hostname][\'ansible_facts\'][\'kernel_name\']'}]


# Generated at 2022-06-13 08:34:56.547513
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    pass

# Generated at 2022-06-13 08:35:04.117770
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play._pre_tasks = [['pre_task_1'],['pre_task_2']]
    play._tasks = [['task_1'],['task_2']]
    play._post_tasks = [['post_task_1'],['post_task_2']]
    expected = ['pre_task_1','pre_task_2','task_1','task_2','post_task_1','post_task_2']
    assert play.get_tasks() == expected

# Generated at 2022-06-13 08:35:06.103179
# Unit test for method get_name of class Play
def test_Play_get_name():
    data = dict(hosts='AAAAAAAAAAA')
    pl = Play.load(data)
    assert pl.get_name() == 'AAAAAAAAAAA'

# Generated at 2022-06-13 08:35:09.552128
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'test'
    assert play.get_name() == 'test'
    play.name = None
    play.hosts = ['test']
    assert play.get_name() == 'test'
    play.hosts = None
    assert play.get_name() == ''


# Generated at 2022-06-13 08:35:10.797456
# Unit test for constructor of class Play
def test_Play():
    # The play constructor has no args
    p = Play()
    assert p is not None


# Generated at 2022-06-13 08:35:12.996001
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    p.preprocess_data({"tasks":[], "hosts":"localhost", "vars":{"a":1, "b": "c"}})

    assert p.vars['a'] == 1



# Generated at 2022-06-13 08:35:21.935634
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize({'_action_groups': {'group': [{'action': 'action', 'module': 'module'}], 'group1': [{'action': 'action1', 'module': 'module1'}]}, 'hosts': 'hosts'})
    assert play._action_groups == {'group': [{'action': 'action', 'module': 'module'}], 'group1': [{'action': 'action1', 'module': 'module1'}]}
    assert play.hosts == 'hosts'

# Generated at 2022-06-13 08:35:30.048652
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    #Create a play
    play = Play()
    
    #Create role
    role = Role()
    role.name = "testrole"
    role.path = "test"
    role.role_vars = dict()
    role.default_vars = dict()
    role.role_metadata = dict()
    role.dependencies = list()
    
    #Create block
    block = Block()
    block.block = list()
    block.rescue = list()
    block.always = list()
    block.use_handlers = True
    
    #Add block to test role
    role.get_handler_blocks(play=play).append(block)
    
    #Add role to play
    play.roles.append(role)
    
    # Run the tested method
    block_list = play.compile

# Generated at 2022-06-13 08:35:32.854949
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = "new_play"
    assert p.get_name() == "new_play"

# Generated at 2022-06-13 08:35:36.812347
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    task = Task()
    block = Block()
    block.block = task
    play.pre_tasks = [block]
    assert play.get_tasks() == [task]

# Generated at 2022-06-13 08:35:58.251566
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    tasks = [
            Task(name="first_task"),
            Task(name="second_task"),
            Task(name="thrid_task"),
            Task(name="fourth_task")
        ]
    handlers = [
            Task(name="first_handler")
        ]
    roles = [
            Role(name="first_role", tasks=tasks, handlers=handlers)
        ]
    play = Play(name="Test-Play", hosts="", become_user="", roles=roles)
    print(play.compile_roles_handlers())

# Generated at 2022-06-13 08:36:07.881603
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:36:15.096756
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    data_dict = {'hosts': 'localhost', 'name': 'test', 'tasks': [{ 'action': 'debug', 'msg': 'test' }, { 'action': 'debug', 'msg': 'test2' }]}
    fake_loader = DictDataLoader({'some_file': "{ \"a\": 1 }"})
    fake_variable_manager = VariableManager()
    fake_play = Play()
    fake_play.load_data(data_dict, loader=fake_loader, variable_manager=fake_variable_manager)
    assert fake_play.preprocess_data(fake_play._ds) is not None

# Generated at 2022-06-13 08:36:22.886250
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # test setup
    content =  {'tasks': {'task': {'action': {'module': 'command', 'args': 'echo "hello"'}}}}
    play = Play.load(content, variable_manager=None, loader=None)
    #test
    result = play.get_tasks()
    assert len(result) == 1
    assert result[0].args == "echo \"hello\""



# Generated at 2022-06-13 08:36:31.522005
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.clean import module_response

    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import pytest

    # Test with vars_files = None
    p = Play()
    setattr(p, 'vars_files', None)
    assert p.get_vars_files() == []

    # Test with vars_files = single string
    p = Play()
    setattr(p, 'vars_files', 'hello-world.yml')
    assert p.get_vars_files() == ['hello-world.yml']

    # Test with vars_files = list of strings
    p = Play()

# Generated at 2022-06-13 08:36:43.650776
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:36:53.474390
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

# Generated at 2022-06-13 08:37:05.351481
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:37:07.166766
# Unit test for method get_name of class Play
def test_Play_get_name():
    Play = Play()
    Play.get_name()

# Generated at 2022-06-13 08:37:13.733432
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()

    # Case 1
    play.vars_files = ['1.yml','2.yml','3.yml']
    assert list(play.get_vars_files()) == ['1.yml','2.yml','3.yml']

    # Case 2
    play.vars_files = '1.yml'
    assert list(play.get_vars_files()) == ['1.yml']


# Generated at 2022-06-13 08:37:35.214285
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

    # Testing with an empty parameter
    data = {}

    new_play = play.deserialize(data)

    assert (new_play.name == play.name)
    assert (new_play.hosts == play.hosts)
    assert (new_play.force_handlers == play.force_handlers)
    assert (new_play.max_fail_percentage == play.max_fail_percentage)
    assert (new_play.serial == play.serial)
    assert (new_play.strategy == play.strategy)
    assert (new_play.tags == play.tags)
    assert (new_play.vars == play.vars)
    assert (new_play.vars_files == play.vars_files)

    assert (new_play._ds == data)



# Generated at 2022-06-13 08:37:48.143575
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.hosts="all"
    play.connection="local"
    play.max_fail_percentage=0
    play.gather_facts="no"
    from ansible.playbook.role.include import RoleInclude
    role_include = RoleInclude()
    role_include.role = "test"
    role_include.task_includes = dict()
    from ansible.playbook.block import Block
    block = Block()
    from ansible.playbook.task import Task
    task1 = Task()
    task2 = Task()
    task3 = Task()
    block.block = [task1, task2]
    task3.block = block
    role_include.task_includes['tasks'] = [task3]

# Generated at 2022-06-13 08:37:57.281885
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    import sys
    from io import StringIO
    from ansible.playbook.play import Play

    vpc_playbook_path = "../../ansible-builder/examples/vpc.yml"
    if sys.version_info[0] >= 3:
        import configparser
        orig_stdout = sys.stdout
        f = StringIO()
        sys.stdout = f
        config = configparser.ConfigParser()
        config.read(vpc_playbook_path)
        sys.stdout = orig_stdout
        assert config.sections() == ['vpc_stack']
        vpc_playbook = Play()

# Generated at 2022-06-13 08:38:05.796905
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    p.name = 'play'
    p.connection = 'local'
    p.hosts = 'all'

    # create a single dummy task
    t = Task()
    t.action = 'debug'
    t.args['msg'] = 'foo'

    # create a single dummy handler
    h = Task()
    h.action = 'debug'
    h.register = 'baz'

    # attach the task and handler to the play
    p.tasks = [t]
    p.handlers = [h]

    # serialize the play into a dictionary
    data = p.serialize()

    # create a new play and deserialize it
    p2 = Play()
    p2.deserialize(data)

    # convert the results into a couple of sets, so we can more easily


# Generated at 2022-06-13 08:38:15.510231
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    print("Test Play.deserialize(): ")
    print("test normal: ")
    play.deserialize({
        "name": "test",
        "hosts": "127.0.0.1",
        "user": "root",
        "roles": [
            {"name": "role1"},
            {"name": "role2"}
        ],
        "included_conditional": "",
        "included_path": "",
        "action_groups": {},
        "group_actions": {}
    })

# Generated at 2022-06-13 08:38:23.426195
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # create a play for testing
    play = Play()
    # create a role for testing
    role = Role()
    role.set_dep_chain([['foo', {}]])
    block = Block()
    task = Task()
    task.set_loader(DictDataLoader({}))
    task.set_dep_chain([['foo', {}]])
    block.add_task(task)
    role.add_block(block)
    play.add_role(role)
    # we have only one role with one block with one task
    assert(len(play.compile_roles_handlers()) == 1)
# END - Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:38:26.085155
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize("testing")
    return play.deserialized

# Generated at 2022-06-13 08:38:31.152033
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    # p.preprocess_data([])
    # p.preprocess_data({})
    # p.preprocess_data(None)
    # p.preprocess_data(1)


# Generated at 2022-06-13 08:38:34.475044
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'play_test'
    assert p.get_name() == 'play_test'


# Generated at 2022-06-13 08:38:43.905595
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    from ansible.vars.manager import VariableManager
    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.cli.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    variable_manager = VariableManager()
    variable_manager.options_vars = {}
    variable_manager.extra_vars = {}
    variable_manager.ansible_vars = {}
    variable_manager.host_vars = {}
    variable_manager.group_vars = {}
    variable_manager.group_vars_files = []

    vault_id = DEFAULT_VAULT_ID_MATCH
    vault_secret = VaultSecret('vault_secret', 'test', False, True)
    vault_secret.set_decrypted_value(b'test')
   

# Generated at 2022-06-13 08:39:05.032332
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    playbook_path = 'test_playbook.yml'
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory('localhost', variable_manager)
    variable_manager.set_inventory(inventory)
    play = Play()

# Generated at 2022-06-13 08:39:14.027896
# Unit test for method get_name of class Play
def test_Play_get_name():
  ############################################################################
  # NOTE: This is an autogenerated test, please do not modify it directly.   #
  #       If you have any questions please ask @rhpcooper in the issues       #
  ############################################################################
  module_path = 'ansible.parsing.dataloader'
  p = Play()
  p.name = 'test-name'
  assert p.get_name() == 'test-name'
  p.name = None
  p.hosts = 'test-host'
  assert p.get_name() == 'test-host'
  p.hosts = None
  assert p.get_name() == ''


# Generated at 2022-06-13 08:39:22.403749
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.playbook.play import Play
    from _ast import Dict
    from _ast import Load
    test = Play()
    try:
        test.preprocess_data(Dict(keys=[],values=[]))
    except:
        pass
    try:
        test.preprocess_data(Load())
    except:
        pass
    try:
        test.preprocess_data("foo")
    except:
        pass


# Generated at 2022-06-13 08:39:29.588185
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''Unit test of Play.compile_roles_handlers'''

    import os
    import sys
    import imp
    import bz2
    import base64
    import types
    import zlib
    import json
    import textwrap
    import datetime
    import time
    import pytest
    import tempfile

    from collections import namedtuple
    from ansible_collections.nsbl.test.units.mock.fake_collections_finder import FakeCollectionsFinder
    from ansible_collections.nsbl.test.units.mock.fake_loader import FakeLoader

    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

# Generated at 2022-06-13 08:39:30.743550
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # test a play with a single role
    p = Play()
    p.compile_roles_handlers()



# Generated at 2022-06-13 08:39:34.730658
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    with pytest.raises(AnsibleAssertionError):
        Play.load(dict(foo="bar")).preprocess_data(2)


# Generated at 2022-06-13 08:39:42.634589
# Unit test for method get_name of class Play
def test_Play_get_name():
    # host is list
    hosts = ["h1", "h2", "h3"]
    p = Play()
    p.hosts = hosts
    name = p.get_name()
    assert name == "h1,h2,h3"
    # host is an empty list
    hosts = []
    p = Play()
    p.hosts = hosts
    name = p.get_name()
    assert name == ","
    # host is string
    hosts = "h1,h2,h3"
    p = Play()
    p.hosts = hosts
    name = p.get_name()
    assert name == "h1,h2,h3"
    # host is None
    hosts = None
    p = Play()
    p.hosts = hosts
    name = p.get_name()


# Generated at 2022-06-13 08:39:51.520343
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()

    play.tasks.extend( [Block().load(data=[Task().load(dict(action=dict(module='foo'), name='one')),
                                           Task().load(dict(action=dict(module='bar'), name='two'))] )] )

    assert isinstance(play.get_tasks()[0], Task)
    assert isinstance(play.get_tasks()[1], Task)

    play.post_tasks.extend( [Block().load(data=[Task().load(dict(action=dict(module='baz'), name='three')),
                                               Task().load(dict(action=dict(module='bat'), name='four'))] )] )

    assert isinstance(play.get_tasks()[2], Task)

# Generated at 2022-06-13 08:39:59.119952
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    data = play.serialize()
    assert 'tasks' in data
    assert 'handlers' in data
    assert 'roles' in data
    assert 'included_path' in data
    assert 'action_groups' in data
    assert 'group_actions' in data
    assert type(data['roles']) == list
    assert data['action_groups'] == {}
    assert data['group_actions'] == {}
    assert data['roles'] == []
    assert data['included_path'] == None

# Generated at 2022-06-13 08:40:07.416418
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # create a dummy play to load roles
    p = Play()

    # create dummy roles
    r1 = Role()
    r1.name = "role_1"
    r2 = Role()
    r2.name = "role_2"

    # create a dummy handler for role_1
    handler_1 = Handler()
    handler_1.name = "handler_1"

    # create a dummy handler for role_2
    handler_2 = Handler()
    handler_2.name = "handler_2"

    # get the handlers of role_1 and append the newly created
    # handler_1 to them
    h1 = r1.get_handler_blocks()
    h1.append(handler_1)
    r1.set_handler_blocks(h1)

    # get the handlers of role_2 and append the newly

# Generated at 2022-06-13 08:40:31.609619
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
  # no test, because no function body
  pass

# Generated at 2022-06-13 08:40:41.403163
# Unit test for constructor of class Play
def test_Play():
    p = Play()

    # both _ds and _dependency_loaders are initialized to None
    assert p._ds is None
    assert p._dependency_loaders is None
    assert p.vars is None

    # _validate_roles, _validate_handlers, _validate_tasks and _validate_vars_prompt all return []
    assert p._validate_roles('', '', []) == []
    assert p._validate_handlers('', '', []) == []
    assert p._validate_tasks('', '', []) == []
    assert p._validate_vars_prompt('', '', []) == []

    # get_name always return ''
    assert p.get_name() == ''

    # load function always raise AnsibleParserError

# Generated at 2022-06-13 08:40:54.122984
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    assert p.preprocess_data(None) is None

    ds = {'user': 'remote_user'}
    assert p.preprocess_data(ds) is None
    assert ds['remote_user'] == 'remote_user'

    ds = {'hosts': ['hosts']}
    assert p.preprocess_data(ds) is None
    assert ds['hosts'] == 'hosts'

    ds = {'vars_files': 'vars_files'}
    assert p.preprocess_data(ds) is None
    assert ds['vars_files'] == 'vars_files'

    ds = {'vars_prompt': ('vars_prompt',)}
    assert p.preprocess_data(ds) is None

# Generated at 2022-06-13 08:40:55.084020
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    assert True

# Generated at 2022-06-13 08:40:59.129056
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """
    Test copy method of Play class
    """
    play = Play(name='play')
    assert play.compile_roles_handlers() == []


# Generated at 2022-06-13 08:41:12.885196
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansiblelint.rule import RulesCollection
    from ansiblelint.runner import Runner
    from ansiblelint import AnsibleLintConfig
    from ansible.parsing.mod_args import ModuleArgsParser

    play_path = 'test/parser_yaml/'
    runner = Runner(RulesCollection(), play_path, [], None, AnsibleLintConfig([]))

    ds = runner._get_parsed_results(play_path)
    play = Play.load(ds[0], variable_manager=None, loader=None)
    tasks = play.get_tasks()
    assert len(tasks) == 4
    assert tasks[0][0].name == 'Yum Security Update'
    assert tasks[0][0].tags == ['yum']