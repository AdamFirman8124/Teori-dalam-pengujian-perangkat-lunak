

# Generated at 2022-06-13 08:31:38.720145
# Unit test for method get_name of class Play
def test_Play_get_name():
    from unit.fixture_templates import Template
    p = Play()

    assert p.get_name() == ''

    p.name = 'test1'
    assert p.get_name() == 'test1'

    p.hosts = 'all'
    assert p.get_name() == 'test1'


# Generated at 2022-06-13 08:31:39.608009
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert isinstance(play.compile_roles_handlers(), list)


# Generated at 2022-06-13 08:31:51.258982
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import os.path
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.collections.ansible.aws import aws as myrole
    dataloader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=dataloader, variable_manager=variable_manager,  host_list=[])
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            roles = [
                myrole,
            ]
        )
    play = Play().load(play_source, variable_manager=variable_manager, loader=dataloader)
   

# Generated at 2022-06-13 08:31:59.617251
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    hosts = 'localhost'
    roles = []
    tasks = []
    vars = {
      'name': 'test1'
    }
    path = 'path'
    name = 'test'
    port = 0
    remote_user = 'test1'
    remote_pass = 'test2'
    private_key_file = 'test3'
    become = True
    become_method = 'sudo'
    become_user = 'test4'
    become_pass = 'test5'
    tags = ['test6']
    skip_tags = ['test7']
    any_vars_prompt = {
      'name': 'test8'
    }

# Generated at 2022-06-13 08:32:04.434451
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = 'play_vf1'
    assert p.get_vars_files() == ['play_vf1']

# Generated at 2022-06-13 08:32:05.908689
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass


# Generated at 2022-06-13 08:32:09.321723
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pl = Play()
    # Run the method to test
    res = pl.get_tasks()
    assert res == [], res

# Generated at 2022-06-13 08:32:21.574221
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p=Play()
    data={
    'hosts': 'master',
    'name': 'one',
    'roles': [{'role': {'_role_name': 'kkjjj'}},
              {'role': {'_role_name': 'lljjj'}}]
    }
    p.deserialize(data)
    assert p.deserialize(data)==None
    assert p._included_path==None
    assert p._action_groups=={}
    assert p._group_actions=={}
    assert p.ROLE_CACHE=={}
    assert p.roles==[{'role': {'_role_name': 'kkjjj'}}, {'role': {'_role_name': 'lljjj'}}]


# Generated at 2022-06-13 08:32:23.484638
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import os

    obj = Play()
    obj.get_tasks()

# Generated at 2022-06-13 08:32:24.417537
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    assert False

# Generated at 2022-06-13 08:32:43.299890
# Unit test for constructor of class Play
def test_Play():
    play = Play()
    assert play.deprecated_always_has_vars == True
    assert play.deprecated_always_run == False
    assert play.deprecated_check == False
    assert play.deprecated_gather_facts == 'smart'
    assert play.deprecated_hosts == 'all'
    assert play.deprecated_ignore_errors == False
    assert play.deprecated_remote_user == 'root'
    assert play.deprecated_sudo == False
    assert play.deprecated_sudo_user == None
    assert play.deprecated_tags == []
    assert play.deprecated_vars == {}
    assert play.deprecated_vars_prompt == []
    assert play.deprecated_vars_files == []
    assert play.deprecated_when == None
    assert play.force_handlers

# Generated at 2022-06-13 08:32:51.974226
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play.load(dict(
        name = 'test_play', hosts = 'localhost',
        roles = [
            dict(role = 'should-be-ignored', from_include = True),
            dict(
                role = 'foo',
                handlers = [
                    dict(name = 'bar', tags = ['baz'])
                ],
                vars = dict(
                    c = 1, d = 2
                ),
                tasks = [
                    dict(action = dict(module = 'debug', args = dict(msg = "I've been included!")))
                ]
            )
        ]
    ))
    play.compile_roles_handlers()

# Generated at 2022-06-13 08:33:00.664894
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    import __builtin__
    if 'open' in __builtin__.__dict__:
        del __builtin__.__dict__['open']
    import _ast
    ast.open = _ast.open

    def _assert(in_dict, exp_dict):
        play = Play()
        act_dict = play.preprocess_data(in_dict)
        assert(exp_dict == act_dict)

    in_dict = {'hosts': 'all', 'gather_facts': 'no'}
    exp_dict = {'hosts': 'all', 'gather_facts': 'no'}
    _assert(in_dict, exp_dict)

    in_dict = {'user': 'some-user'}
    exp_dict = {'remote_user': 'some-user'}
    _assert

# Generated at 2022-06-13 08:33:08.388863
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = [['task1'], ['task2']]
    play.tasks = [['task3'], ['task4']]
    play.post_tasks = [['task5'], ['task6']]
    assert play.get_tasks() == ['task1', 'task2', 'task3', 'task4', 'task5', 'task6']


# Generated at 2022-06-13 08:33:09.169576
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:33:17.117405
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    """
    Unit test for method preprocess_data of class Play
    """
    play = Play()
    # AssertionError is raised because ds is not a dictionary
    with pytest.raises(AssertionError):
        play.preprocess_data(['foo'])
    # ds is a dictionary
    assert play.preprocess_data({}) is not None


# Generated at 2022-06-13 08:33:27.960971
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    data = dict(
        hosts=["localhost"],
        user="joe",
        pre_tasks=[
            dict(yum=dict(name="httpd"))
        ],
        tasks=[
            dict(debug=dict(msg="hello")),
            dict(debug=dict(msg="world")),
        ],
        roles=[
            dict(role="web", port=80),
            "db",
        ],
    )
    play = Play()
    play.load(data, variable_manager=VariableManager(), loader=DataLoader())


# Generated at 2022-06-13 08:33:29.614864
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()

    # should not throw exception
    play.get_tasks()


# Generated at 2022-06-13 08:33:45.361441
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Create a new Play object
    p = Play()

    # Populate the Play object
    p.vars_files = None
    # Run the method and test that the result is as expected
    # assert p.get_vars_files() == []

    # Populate the Play object
    p.vars_files = "filename"
    # Run the method and test that the result is as expected
    # assert p.get_vars_files() == ["filename"]

    # Populate the Play object
    p.vars_files = ["filename1","filename2"]
    # Run the method and test that the result is as expected
    # assert p.get_vars_files() == ["filename1","filename2"]

    # Print the test results
    print("Test 1 - Successful")
    print("Test 2 - Successful")
   

# Generated at 2022-06-13 08:33:51.627769
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = ['tasks']
    p.pre_tasks = ['pre_tasks']
    p.post_tasks = ['post_tasks']
    p.handlers = ['handlers']
    p.roles = ['roles']
    p.get_tasks()



# Generated at 2022-06-13 08:34:03.539426
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p._name = 'test'
    assert p.get_name() == 'test'



# Generated at 2022-06-13 08:34:07.209320
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = [Play.get_tasks()]
    assert(p.tasks)

# Generated at 2022-06-13 08:34:14.998481
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # initialization
    play = Play()

    ds = {
        'hosts': 'all',
        'gather_facts': 'yes',
        'serial': '0'
    }
    # actual call
    try:
        play = play.preprocess_data(ds)

        # results
        assert play is not None
        assert ds is not None
        assert ds['gather_facts'] is True
        assert ds['serial'] == [0]
    except AnsibleAssertionError as e:
        assert False, e.args

# Generated at 2022-06-13 08:34:19.106037
# Unit test for method get_name of class Play
def test_Play_get_name():
    m = Play()
    m.name = 'A name'
    m.hosts = 'The hosts'
    print((m.get_name()))


# Generated at 2022-06-13 08:34:29.336601
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    results = {
        'Play': {
            '_roles': [],
            'vars': {
                'foo': 'bar',
                'baz': 'blip'
            },
            'name': 'Test Play 1',
            'tasks': [
                {
                    'debug': {
                        'msg': 'foo was {{foo}}, baz was {{baz}}'
                    }
                }
            ],
            '_pre_tasks': [],
            '_post_tasks': [],
            'connection': 'local',
            '_vars': {},
            '_handlers': []
        }
    }

    for key, play in results.items():
        p = Play()
        p.name = key
        p.load_data(data=play)

# Generated at 2022-06-13 08:34:30.888418
# Unit test for method get_name of class Play
def test_Play_get_name():
    pass


# Generated at 2022-06-13 08:34:35.241518
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    ansible_module_args = {
        'hosts': ['192.0.2.2'],
        'roles': ['foo']
    }
    play = Play().load(
        data=ansible_module_args,
        variable_manager=VariableManager(),
        loader=DataLoader()
    )
    actual_tasks = play.get_tasks()
    assert actual_tasks, "Failed to get task list in Play"


# Generated at 2022-06-13 08:34:40.248621
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    args = dict(
        # this key/value pair is not really needed
        _ds = None,
        # this key/value pair is not really needed
        _parent = None,
        # this key/value pair is not really needed
        _play = None,

    )
    obj = Play(**args)
    # test method
    # TODO: test method get_tasks of class Play
    return True

# Generated at 2022-06-13 08:34:45.786170
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = []
    assert p.get_vars_files() == []
    p.vars_files = ["hello"]
    assert p.get_vars_files() == ["hello"]
    p.vars_files = ["hello", "world"]
    assert p.get_vars_files() == ["hello", "world"]
    p.vars_files = "hello"
    assert p.get_vars_files() == ["hello"]
    p.vars_files = "hello world"
    assert p.get_vars_files() == ["hello world"]



# Generated at 2022-06-13 08:34:48.730441
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    Play.compile_roles_handlers()


# Generated at 2022-06-13 08:35:03.853407
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    play.vars_files = None
    assert play.get_vars_files() == []
    play.vars_files = './test/test_file.yaml'
    assert play.get_vars_files() == ['./test/test_file.yaml']

# Generated at 2022-06-13 08:35:05.882871
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = {}
    r = Play()
    assert isinstance(r.preprocess_data(ds), dict)


# Generated at 2022-06-13 08:35:12.873352
# Unit test for method get_name of class Play
def test_Play_get_name():
    # try with no name
    p = Play()
    # Set attribute 'name' of instance 'p' to None
    p.name = None
    # Set attribute 'hosts' of instance 'p' to 'localhost'
    p.hosts = 'localhost'
    assert p.get_name() == ''
    # try with no hosts
    p = Play()
    # Set attribute 'name' of instance 'p' to 'test-play'
    p.name = 'test-play'
    # Set attribute 'hosts' of instance 'p' to None
    p.hosts = None
    assert p.get_name() == 'test-play'
    p = Play()
    # Set attribute 'name' of instance 'p' to 'test-play'
    p.name = 'test-play'
    # Set attribute 'hosts

# Generated at 2022-06-13 08:35:15.372678
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.get_tasks()
    assert 1 == 1


# Generated at 2022-06-13 08:35:16.299709
# Unit test for constructor of class Play
def test_Play():
    pass


# Generated at 2022-06-13 08:35:27.255761
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
    [ansible-test multiverse] $ python3.6 -m test.units.callback.v2.test_Play_compile_roles_handlers

    test_Play_compile_roles_handlers ... ok
    test_Play_compile_roles_handlers_parsing_the_main_handler ... ok

    [ansible-test multiverse] $
    '''
    import os
    from ansible.module_utils.six.moves import builtins

    from units.compat.mock import call, patch
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueue

# Generated at 2022-06-13 08:35:32.380465
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)

# Generated at 2022-06-13 08:35:42.682738
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play.load(dict(
        name="test play",
        hosts="localhost",
        gather_facts=None,
        roles=[dict(
            name="test role",
            handlers=["test handler"],
        )],
        handlers=[dict(
            name="test handler",
            debug=dict(msg="test handler"),
        )],
    ), variable_manager=VariableManager())
    role = play.get_roles()[0]
    handler = play.get_handlers()[0]
    assert_equal(handler, role.get_handler_blocks(play)[0].block[0])
    assert_equal(handler, play.compile_roles_handlers()[0])


# Generated at 2022-06-13 08:35:45.747782
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'Test Play Name'
    assert play.get_name() == 'Test Play Name'


# Generated at 2022-06-13 08:35:59.302962
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # TODO: add tests
    from ansible.plugins.loader import callback_loader, connection_loader, module_loader, shell_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    # PlayContext(play=self, options=variable_manager.get_vars(), passwords=passwords)
    # self.loader, self.variable_manager, self.host_manager
    # variable_manager.extra_vars = load_extra_vars(loader=self._loader, options=options)
    # variable_manager.options_vars = load_options_

# Generated at 2022-06-13 08:36:14.900340
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Test case 1
    p = Play()
    p.name = "Test Play"
    assert p.get_name() == "Test Play"

    # Test case 2
    p = Play()
    p.hosts = "Test Hosts"
    assert p.get_name() == "Test Hosts"

    # Test case 3
    p = Play()
    p.name = ""
    p.hosts = ""
    assert p.get_name() == ""
    print("PASS: Play testing for get_name ")



# Generated at 2022-06-13 08:36:27.262195
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:36:29.900212
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = "test play"
    assert play.get_name() == "test play"

# Generated at 2022-06-13 08:36:44.540980
# Unit test for method serialize of class Play
def test_Play_serialize():
    host = 'localhost'
    play_serialize = Play()
    play_serialize._variable_manager = VariableManager()
    play_serialize._loader = DataLoader()
    play_serialize.hosts = host
    play_serialize.name = "Ansible Play"
    play_serialize.vars = {'var': 'hi'}
    play_serialize.tags = ['always', 'never']
    play_serialize.roles = [{"role_some": {"role_name": "http://github.com/ansible/ansible-examples.git"}}]
    play_serialize.tasks = [{"task_some": {"var1": "task1_var", "var2": "task1_var"}}]

# Generated at 2022-06-13 08:36:53.863260
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # A dict to initialize a Play
    raw_dict = {
        'play': {
            'hosts': 'localhost',
            'name': 'a test play name',
            'user': 'a test play user',
        }
    }

    # Create the Play instance
    play = Play()

    # Initialize the Play
    play.deserialize(raw_dict)

    # Check if the attribute 'user' exists in the Play
    assert 'user' in play._attributes

    # Edit the dict and remove 'user'
    raw_dict['play'].pop('user')

    # Call the preprocess_data method
    assert play.preprocess_data(raw_dict)

    # Check if the attribute 'user' does NOT exist in the Play
    assert 'user' not in play._attributes



# Generated at 2022-06-13 08:36:58.612432
# Unit test for method get_name of class Play
def test_Play_get_name():
    try:
        x = Play()
        x.get_name()
    except Exception as e:
        print(e)
        assert False
    assert True
# Execute unit_test for method get_name of class Play

# Generated at 2022-06-13 08:37:07.804362
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # No roles is empty
    play = Play()
    play.roles = []
    assert play.compile_roles_handlers() == []

    # Role with no handlers is empty
    role = Role()
    role.handlers = []
    play = Play()
    play.roles = [role]
    assert play.compile_roles_handlers() == []

    # Role with handlers is returned
    role = Role()
    handler = Handler()
    handler.name = 'test'
    role.handlers = [handler]
    play = Play()
    play.roles = [role]
    assert play.compile_roles_handlers() == [handler]

# Generated at 2022-06-13 08:37:19.385512
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    '''
    Test method preprocess_data of class Play.

    '''
    play = Play()

# Generated at 2022-06-13 08:37:25.523462
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    mock_host = MagicMock(Host)
    mock_block = MagicMock(Block)
    mock_block.block = ['block']
    mock_role = MagicMock(Role)
    mock_role.get_handler_blocks.return_value = [mock_block]
    p = Play()
    p.roles = [mock_role]
    result = p.compile_roles_handlers()
    assert isinstance(result, list)
    assert result == [mock_block]
    assert mock_role.get_handler_blocks.called == True


# Generated at 2022-06-13 08:37:34.011372
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    PLAY = Play()
    PLAY._ds = dict({'vars_files': {}})
    assert PLAY.get_vars_files() == [{}]

    PLAY = Play()
    PLAY._ds = dict({'vars_files': [{'a_vars_file': '/path/to/file'}, {'another_vars_file': '/path/to/another_file'}]})
    assert PLAY.get_vars_files() == [{'a_vars_file': '/path/to/file'}, {'another_vars_file': '/path/to/another_file'}]



# Generated at 2022-06-13 08:38:01.799494
# Unit test for method serialize of class Play
def test_Play_serialize():
    data = {
        'name': 'hello world',
        'max_fail_pct': 0.0,
        'user': 'testuser',
        'remote_user': 'me',
        'strategy': 'teststrategy',
        'hosts': ['host1', 'host2'],
        'vars': {'a': 1},
        'remote_port': 1000,
        'connection': 'testconnection',
        'roles': [],
        'included_path': 'included_path',
        'action_groups': [],
        'group_actions': {},
    }
    play = Play().load(data, variable_manager=None)
    new_data = play.serialize()
    assert data == new_data

# Generated at 2022-06-13 08:38:04.816636
# Unit test for method serialize of class Play
def test_Play_serialize():
    # instantiate class Play, for the test
    play = Play()
    # test method (function) serialize of class Play
    play.serialize()

# Generated at 2022-06-13 08:38:14.917433
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play1 = Play()
    first_role = Role()
    first_role.name = 'first_role'

    first_role_handler = Handler()
    first_role_handler_task = Task()

    first_role_handler.block = [first_role_handler_task, first_role_handler_task]
    first_role.handlers.append(first_role_handler)

    second_role = Role()
    second_role.name = 'second_role'
    second_role_handler = Handler()
    second_role_handler_task = Task()
    second_role_handler.block = [second_role_handler_task, second_role_handler_task]
    second_role.handlers.append(second_role_handler)

    play1.roles.append(first_role)

# Generated at 2022-06-13 08:38:20.301893
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():

    # Arrange
    load_data = {'vars_files': ""}
    variable_manager = None
    loader = None
    vars = None

    # Act
    play = Play.load(load_data, variable_manager=variable_manager, loader=loader, vars=vars)
    vars_files = play.get_vars_files()

    # Assert
    assert vars_files == []


# Generated at 2022-06-13 08:38:23.450848
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    p.preprocess_data(Play.load(dict(hosts=['localhost', '127.0.0.1'], tasks=[dict(action='setup')])))
    try:
        p.preprocess_data(Play.load(dict(hosts=[], tasks=[dict(action='setup')])))
    except AnsibleParserError as e:
        print(e)



# Generated at 2022-06-13 08:38:29.059233
# Unit test for method serialize of class Play
def test_Play_serialize():
    test_play = Play()
    yaml_dict = test_play.serialize()
    assert "action_groups" in yaml_dict
    assert "group_actions" in yaml_dict
    assert "roles" in yaml_dict
    assert "tasks" in yaml_dict


# Generated at 2022-06-13 08:38:32.682814
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    mock_play = Play()
    assert type(mock_play.get_tasks()) == list
    assert mock_play.get_tasks() == []


# Generated at 2022-06-13 08:38:40.794375
# Unit test for constructor of class Play
def test_Play():
    play_instance = Play()
    assert not play_instance.handlers
    assert not play_instance.post_tasks
    assert not play_instance.pre_tasks
    assert not play_instance.tasks
    assert not play_instance.roles
    assert not play_instance.vars
    assert not play_instance.vars_prompt
    assert not play_instance.vars_files
    assert play_instance.suicide



# Generated at 2022-06-13 08:38:47.111109
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # P1 init
    p1 = Play()
    # P2 init
    p2 = Play()
    # Expected
    # Result
    result = p1.compile_roles_handlers()
    # Assert
    assert result == p2.compile_roles_handlers()



# Generated at 2022-06-13 08:39:00.526495
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import os
    import sys
    import collections
    import copy
    import re
    import imp
    filePath = os.path.dirname(__file__) + '/code/playbook/play_compile_roles_handlers_code.py'
    module = imp.load_source('modulename', filePath)
    #  Unit test for method compile_roles_handlers of class Play
    # Prepare test data
    args = collections.namedtuple('args', ['listtags', 'listtasks', 'listhosts', 'syntax', 'module_path'])
    args.listtags = False
    args.listtasks = False
    args.listhosts = False
    args.syntax = False
    args.module_path = None
    args.connection='ssh'
    args.remote_user=None


# Generated at 2022-06-13 08:39:43.262884
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    def get_tasks(pre_tasks, tasks, post_tasks):
        p = Play()
        p.pre_tasks = pre_tasks
        p.tasks = tasks
        p.post_tasks = post_tasks
        return p

    pre_tasks = [1]
    tasks = [2]
    post_tasks = [3]
    test = get_tasks(pre_tasks, tasks, post_tasks)
    assert test.get_tasks() == [1, 2, 3]


# Generated at 2022-06-13 08:39:52.043206
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.vars import HostVars
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    import jinja2

    context.CLIAR

# Generated at 2022-06-13 08:40:02.596806
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    mock_loader = DictDataLoader({
        "/etc/ansible/roles/role/tasks/main.yaml": """
        - shell: echo "I am a task"
        """,
        "/etc/ansible/roles/role/handlers/main.yaml": """
        - shell: echo "I am a handler"
        """
    })

    mock_variable_manager = MagicMock()
    mock_inventory = MagicMock()

    # mock_variable_manager.get_vars.return_value = {}


# Generated at 2022-06-13 08:40:08.260565
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = [1,2,3]
    p.pre_tasks = [4,5,6]
    p.post_tasks = [7,8,9]

    assert p.get_tasks() == [4,5,6,1,2,3,7,8,9]



# Generated at 2022-06-13 08:40:11.710868
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = {"hosts": "all"}
    from ansible.playbook import Play
    a = Play()
    actualResult = a.preprocess_data(ds)
    assert actualResult == ds

# Generated at 2022-06-13 08:40:14.696094
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = [Task(), Task()]
    assert p.get_tasks() == [Task(), Task()]


# Generated at 2022-06-13 08:40:23.954066
# Unit test for method serialize of class Play
def test_Play_serialize():
    hostvars = HostVarsVars({u'a': u'a', u'b': {u'b': u'b'}}, hostvars=HostVarsVars({u'd': u'd', u'c': {u'c': u'c'}}))

# Generated at 2022-06-13 08:40:28.227030
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    #Input
    play = Play()
    play.vars_files = 'a'
    #Expected Output
    result = ['a']
    assert play.get_vars_files() == result

# Generated at 2022-06-13 08:40:33.563529
# Unit test for constructor of class Play
def test_Play():
    p = Play()
    assert p.name == '', "Default Play name should be empty string"
    p = Play('Test Play')
    assert p.name == 'Test Play', "Play name should be 'Test Play'"
    print("Done")


# Generated at 2022-06-13 08:40:42.381495
# Unit test for method compile_roles_handlers of class Play