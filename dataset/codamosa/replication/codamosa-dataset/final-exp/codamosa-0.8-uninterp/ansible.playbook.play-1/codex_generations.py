

# Generated at 2022-06-13 08:31:28.282764
# Unit test for method get_name of class Play
def test_Play_get_name():
    '''
    play_test.Play.get_name()
    '''

    # Initialize a fake Play object
    play = Play()
    #Initialize a fake playbook for the Play object
    playbook = Playbook()
    # Setting the value of name attribute to None
    play.name = None

    # Setting the value of the hosts attribute to a string
    play.hosts = "all"
    # Calling the get_name method and check the returned value
    assert play.get_name() == "all"

    # Setting the value of the hosts attribute to an integer
    play.hosts = 1
    # Calling the get_name method and check the returned value
    assert play.get_name() == ""

    # Setting the value of the name attribute to a string
    play.name = "play_name"
    # Calling the get_name

# Generated at 2022-06-13 08:31:38.669747
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    import os
    import sys
    import __builtin__ as builtins
    import tempfile
    from collections import namedtuple
    import ansible
    import yaml
    import ansible.cli
    import ansible.cli.playbook
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.conditional

    from ansible.utils.debug import debug

    # set up objects
    ansible_config = ansible.cli.AnsibleCLI
    playbook_cli = ansible.cli.playbook.PlaybookCLI(ansible_config)

# Generated at 2022-06-13 08:31:50.783282
# Unit test for method get_name of class Play
def test_Play_get_name():
    import os
    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    dl = ansible.parsing.dataloader.DataLoader()
    var_manager = VariableManager()
    inv_manager = InventoryManager(loader=dl, sources=[])

    pb = Playbook()
    pb._inv_manager = inv_manager
    pb._variable_manager = var_manager
    pb._tqm = TaskQueueManager()
    pb.set_data("""\
- hosts: all
  roles:
    - apache
    """)

    p1 = pb.get_plays()[0]
    assert p1.get_name() == 'all'


# Generated at 2022-06-13 08:31:52.053663
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    assert play.get_tasks() == []


# Generated at 2022-06-13 08:31:55.841510
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    def test():
        data = [{"hosts": "localhost"}]
        play = Play.load(data, variable_manager=None, loader=None)
        play.preprocess_data(data=data)
        assert data == [{'hosts': 'localhost'}]



# Generated at 2022-06-13 08:32:08.642640
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    # Role Attributes
    play._roles = ["role1", "role2", "role3"]
    # Flag/Setting Attributes
    play._force_handlers = False
    play._max_fail_percentage = 0
    play._serial = []
    play._strategy = "strategy"
    play._order = "order"
    # Block (Task) Lists Attributes
    block = Block()
    block._block = ["task1", "task2", "task3"]
    play._handlers = [block]
    play._pre_tasks = [block]
    play._post_tasks = [block]
    play._tasks = [block]
    # Play Attributes

# Generated at 2022-06-13 08:32:19.820363
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    assert ([]) == p.get_vars_files()
    p.vars_files = None
    assert ([]) == p.get_vars_files()
    p.vars_files = 'a'
    assert (['a']) == p.get_vars_files()
    p.vars_files = 'b'
    assert (['b']) == p.get_vars_files()
    p.vars_files = ['a', 'b']
    assert (['a', 'b']) == p.get_vars_files()
    p.vars_files = ['a', 'b']
    assert (['a', 'b']) == p.get_vars_files()



# Generated at 2022-06-13 08:32:24.585268
# Unit test for method get_name of class Play
def test_Play_get_name():
    # create a Play
    p = Play()
    # set variable name of Play
    p.name = "test_Play"
    # test method get_name
    assert p.get_name() == p.name


# Generated at 2022-06-13 08:32:31.236824
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert Play.compile_roles_handlers.__doc__ == 'Handles the role handler compilation step, returning a flat list of Handlers\n        This is done for all roles in the Play.\n        '
    assert callable(Play.compile_roles_handlers)

# Generated at 2022-06-13 08:32:40.273401
# Unit test for constructor of class Play
def test_Play():
    p = Play()
    assert isinstance(p, Play)
    assert isinstance(p.roles, list)
    assert isinstance(p.vars, dict)
    assert isinstance(p.tasks, list)
    assert isinstance(p.handlers, list)
    assert len(p.hosts) == 0
    assert p.name is None
    assert p.max_fail_percentage is None
    assert p.serial == 0
    assert p.strategy == 'linear'
    assert p.force_handlers == context.CLIARGS.get('force_handlers', False)
    assert p.vars == {}

# Generated at 2022-06-13 08:32:57.108894
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:33:02.152613
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.playbook.play import Play
    play = Play()
    play._ds = {'hosts': ['test_play_hosts']}
    assert play.get_name() == 'test_play_hosts'

    play.name = 'test name'
    assert play.get_name() == 'test name'


# Generated at 2022-06-13 08:33:12.893923
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:33:16.359363
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    block_list = play.compile_roles_handlers()
    assert(not block_list)


# Generated at 2022-06-13 08:33:21.903117
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    returns the list of vars_files
    '''
    play = Play()
    play.vars_files = None
    assert play.get_vars_files() == []
    play.vars_files = '../task/test_task.yml'
    assert play.get_vars_files() == ['../task/test_task.yml']
    play.vars_files = ['../task/test_task.yml', '../task/test_task1.yml']
    assert play.get_vars_files() == ['../task/test_task.yml', '../task/test_task1.yml']
    play.vars_files = '../task/test_task.yml'

# Generated at 2022-06-13 08:33:22.834775
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    pass

# Generated at 2022-06-13 08:33:31.775180
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Test when 'ds' is not dict type
    ds_list = [2, 2.0, False, True, 'string', u'unicode string']

    for ds in ds_list:
        try:
            Play().preprocess_data(ds)
        except AnsibleAssertionError as e:
            assert e.args[0] == 'while preprocessing data ({0!s}), ds should be a dict but was a {1!s}'.format(ds, type(ds))



# Generated at 2022-06-13 08:33:37.572809
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    import pytest
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.playbook.play import Play
    import ansible.playbook.play
    import ansible.playbook.role
    ansible.playbook.play.Play = Play
    ansible.playbook.role.Role = Role

    ds = dict(name='test', hosts=['all'], pre_tasks=[], roles=[dict(name='test', tasks=[])], tasks=[])
    play = Play.load(ds=ds, variable_manager=VariableManager(), loader=DataLoader())

# Generated at 2022-06-13 08:33:52.926051
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Play(ds, variable_manager=play_context.variable_manager, loader=play_context.loader, templar=play_context.templar)
    play_context = PlayContext()
    variable_manager = play_context.variable_manager
    variable_manager.extra_vars = load_extra_vars(loader=None, options=None)
    result = Play(ds=None, variable_manager=variable_manager, loader=play_context.loader, templar=play_context.templar)
    data = {'hosts': 'localhost', 'roles': [{'role_name': 'test', 'tasks': [], 'handlers': [], 'default_vars': {}, 'vars': {}, 'var_prompts': [], 'vars_files': []}]}
    result.des

# Generated at 2022-06-13 08:33:53.404868
# Unit test for method get_name of class Play
def test_Play_get_name():
    assert True

# Generated at 2022-06-13 08:34:06.394948
# Unit test for method get_name of class Play
def test_Play_get_name():
    c = Play()
    assert c.get_name() == ''
    assert c.get_name() == ''
    c.name = 'test'
    assert c.get_name() == 'test'


# Generated at 2022-06-13 08:34:17.032602
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:34:19.685568
# Unit test for method get_name of class Play
def test_Play_get_name():

    play = Play()
    assert 'blackbox' == play.get_name()


# Generated at 2022-06-13 08:34:22.278121
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    handlers = p.compile_roles_handlers()
    assert isinstance(handlers, list)



# Generated at 2022-06-13 08:34:25.680939
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    defmock = MagicMock()
    defmock.return_value = ["get_tasks_return_value"]

    play = Play()
    play.get_tasks = defmock

    assert play.get_tasks() == "get_tasks_return_value"

# Generated at 2022-06-13 08:34:38.202092
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import pytest
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.handler import Handler
    rd = RoleDefinition()
    rd.name = "my_role"

# Generated at 2022-06-13 08:34:44.007853
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    obj = Play()
    attrs = {'roles': 'roles', '_included_path': '_included_path', '_action_groups': '_action_groups', '_group_actions': '_group_actions'}
    data = 'data'
    obj.deserialize(data)
    obj.__dict__
    assert_equal(obj.roles, 'roles')
    assert_equal(obj._included_path, '_included_path')
    assert_equal(obj._action_groups, '_action_groups')
    assert_equal(obj._group_actions, '_group_actions')

# Generated at 2022-06-13 08:34:57.679122
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    my_play = Play()

    my_tasks = []
    my_tasks.append('This is a string')

    task1 = Task()
    task1.action = 'collect facts'
    my_tasks.append(task1)

    task2 = Task()
    task2.action = 'install apache'
    my_tasks.append(task2)

    my_play.tasks = my_tasks

    assert my_play.get_tasks()[0] == 'This is a string', "A string was not returned as expected"
    assert my_play.get_tasks()[1][0].action == 'collect facts', "Action collect facts was not returned as expexted"

# Generated at 2022-06-13 08:34:58.693911
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass

# Generated at 2022-06-13 08:35:01.120287
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert play.compile_roles_handlers() == []


# Generated at 2022-06-13 08:35:38.478291
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    class Foo(Play):
        def __init__(self, vars_files=None):
            self.vars_files = vars_files
    play = Foo(vars_files=None)
    assert play.get_vars_files() == []  # None defaults to empty list
    play = Foo(vars_files="/foo/bar.yml")
    assert play.get_vars_files() == ["/foo/bar.yml"]  # Single vars_files is converted to list
    play = Foo(vars_files=["/foo/bar.yml", "/baz/qux.yml"])
    assert play.get_vars_files() == ["/foo/bar.yml", "/baz/qux.yml"]  # Already list is intact

# Generated at 2022-06-13 08:35:52.166821
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    play.name = 'unit test'
    play.hosts = 'localhost'
    play.included_path = 'unit_test'
    play._action_groups = {'instance': 'the_action'}
    play._group_actions = {'the_action': 'instance'}
    data = play.serialize()
    assert data['name'] == 'unit test'
    assert data['hosts'] == 'localhost'
    assert data['included_path'] == 'unit_test'
    assert data['action_groups'] == {'instance': 'the_action'}
    assert data['group_actions'] == {'the_action': 'instance'}


# Generated at 2022-06-13 08:36:03.391564
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import ansible
    assert ansible.__version__ == '2.10.8'

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import ansible.parsing.yaml.objects

    play = Play()
    play.pre_tasks = [Task()]
    play.tasks = [Task()]
    play.post_tasks = [Task()]

    assert play.get_tasks() == [
        play.pre_tasks[0],
        play.tasks[0],
        play.post_tasks[0],
    ]

    play = Play()
    play.pre_tasks = [Block()]
    play.tasks = [Block()]

# Generated at 2022-06-13 08:36:11.166933
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    play.ROLE_CACHE = {"roles": ['1', '2']}
    play._included_conditional = "cond"
    play._included_path = "/path"
    play._action_groups = {"action_groups": ['1', '2']}
    play._group_actions = {"group_actions": ['1', '2']}
    play.roles = [Role()]
    print(play.serialize())

# Generated at 2022-06-13 08:36:16.687477
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_data = dict(
        name='test',
        user='bob'
    )
    play = Play()
    result = play.preprocess_data(play_data)
    assert 'user' not in result, 'user value does not exist'
    assert 'remote_user' in result, 'remote_user has been replaced'
    assert result['remote_user'] == 'bob', 'remote_user has been correctly assigned'


# Generated at 2022-06-13 08:36:28.333187
# Unit test for method get_name of class Play
def test_Play_get_name():
    class Play_inst:
        def __init__(self):
            self.name = "name"
            self.hosts = "hosts"

    log = dict()
    log['monitored_files'] = dict()
    log['monitored_files']['roles_path'] = []
    context.CLIARGS = dict()
    context.CLIARGS['roles_path'] = None
    context.CLIARGS['no_log'] = 'true'
    context.CLIARGS['module_path'] = None
    context.CLIARGS['force_handlers'] = 'false'
    context.CLIARGS['skip_tags'] = list()
    context.CLIARGS['start_at_task'] = None
    context.CLIARGS['step'] = 'false'
    context

# Generated at 2022-06-13 08:36:30.193987
# Unit test for method serialize of class Play
def test_Play_serialize():
    pass


# Generated at 2022-06-13 08:36:44.847972
# Unit test for method serialize of class Play
def test_Play_serialize():
    '''
    Test Play.serialize
    '''
    

# Generated at 2022-06-13 08:36:53.537757
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    """ Test case for deserialize method of Play"""
    new_obj = Play()
    obj = Play()
    assert "deserialize" in dir(obj)
    params = {'vars':{'key1': 'value1'},
              'roles': ['role1', 'role2'],
              'name': 'play1'}
    new_obj.deserialize(params)

    assert new_obj.get_name() == 'play1'
    for key in params.keys():
        if key != 'roles' and key != 'included_path' and key != 'action_groups' and key != 'group_actions':
            assert getattr(new_obj, key, None) == params[key]


# Generated at 2022-06-13 08:37:00.037245
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    p.preprocess_data({})
    p.preprocess_data({
        'name': 'p',
        'hosts': 'localhost',
        'tasks': [
            {
                'name': 'test',
                'debug': 'msg=test'
            }
        ]
    })

# Generated at 2022-06-13 08:37:29.712632
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Initializing the data structures
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    play_ds = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='Hello World'))),
            dict(action=dict(module='debug', args=dict(msg='Hello Earth'))),
            dict(action=dict(module='debug', args=dict(msg='Hello Galaxy')))
        ],
        vars_files=['path_to_vars_file']
    )
    # Creating an instance of play
    play = Play().load(play_ds, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:37:41.078216
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.name = "all"
    p.hosts = "1.1.1.1"
    p.pre_tasks = [{"debug":"var=hostvars['1.1.1.1']['ansible_facts']['default_ipv4']['address']"}]
    p.post_tasks = [{"debug":"var=hostvars['1.1.1.1']['ansible_facts']['default_ipv4']['address']"}]
    p.tasks = [{"debug":"var=hostvars['1.1.1.1']['ansible_facts']['default_ipv4']['address']"}]
    p.get_tasks()
    assert True

# Generated at 2022-06-13 08:37:43.934365
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    obj = Play()
    result = obj.compile_roles_handlers()
    assert result == [], "The result should be []"

# Generated at 2022-06-13 08:37:54.723034
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []
    p._tasks = ['a', 'b', 'c']
    assert p.get_tasks() == ['a', 'b', 'c']
    assert p.get_tasks() == p.get_tasks()
    p._tasks = None
    assert p.get_tasks() == []
    p._tasks = []
    assert p.get_tasks() == []
    p._tasks = ['a', 'b', 'c']
    p._pre_tasks = ['d', 'e', 'f']
    p._post_tasks = ['g', 'h', 'i']

# Generated at 2022-06-13 08:38:05.796081
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    print("### Play_compile_roles_handlers:")
    data = {
        'name': 'test_play',
        'hosts': 'test_host',
        'roles': [{
                    'role': 'test_role_1',
                    'when': 'test_when_cond',
                    'handlers': [{
                                    'name': 'test_handler_1',
                                    'listen': 'test_listen',
                                    'notify': 'test_notify'
                                }]
                }]
    }
    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(loader=None, options=None, passwords=None)
    variable_manager.options_vars = load_options_vars(options)
    loader = DataLoader()

# Generated at 2022-06-13 08:38:13.144742
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play_ = Play()
    play_.vars_files = []
    play_.vars = {}
    play_.vars_files = ['test_vars_files']
    assert play_.get_vars_files() == ['test_vars_files']
    play_.vars_files = None
    assert play_.get_vars_files() == []
    play_.vars_files = ['test_vars_files']
    assert play_.get_vars_files() == ['test_vars_files']

# Generated at 2022-06-13 08:38:17.286779
# Unit test for method get_name of class Play
def test_Play_get_name():
    playbook_name = None
    roles = []
    vars = {}
    hosts = "all_hosts"
    tasks = ["first_task", "second_task"]
    play_1 = Play(name=playbook_name,
        roles=roles,
        vars=vars,
        hosts=hosts,
        tasks=tasks)
    assert play_1.get_name() == "all_hosts"

# Generated at 2022-06-13 08:38:20.962724
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    #GIVEN a play with roles and handlers
    p = Play()

    r = Role()
    r.name = "role1"
    h1 = Handler()
    h2 = Handler()
    l = [h1, h2]
    r.handlers = l

    p.roles = [r]

    #WHEN execute method compile_roles_handlers
    result = p.compile_roles_handlers()

    #THEN result should be [h1, h2]
    assert result == l

# Generated at 2022-06-13 08:38:27.516181
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """
    Test the method compile_roles_handlers of class Play
    """
    import os
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.context import CLIReply
    from ansible.context import CLI
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import set_nonpersistent_facts
    import ansible.constants as C
    block_list = []
    test_roles_

# Generated at 2022-06-13 08:38:37.764606
# Unit test for method get_name of class Play
def test_Play_get_name():
    Play_obj = Play()
    Play_obj.name = 'test_name'
    assert Play_obj.get_name() == 'test_name'
    Play_obj.name = None
    Play_obj.hosts = ['test_hosts_one']
    assert Play_obj.get_name() == 'test_hosts_one'
    Play_obj.hosts = ['test_hosts_one', 'test_hosts_two']
    assert Play_obj.get_name() == 'test_hosts_one,test_hosts_two'
    Play_obj.hosts = None
    assert Play_obj.get_name() == ''

# Generated at 2022-06-13 08:38:57.675194
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # set up args
    args = []
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    # test all valid arg combinations


# Generated at 2022-06-13 08:38:58.359894
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass


# Generated at 2022-06-13 08:39:03.889472
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Testing when data is valid
    play = Play()
    play.deserialize({'name': 'test play', 'id': '123123123', 'connection': 'local', 'gather_facts': 'no',
                    'hosts': 'all', 'become': 'no', 'become_method': 'sudo', 'become_user': 'nobody',
                    'become_ask_pass': 'no', 'vars': {}, 'roles': [], 'included_path': None, 'action_groups': {}, 'group_actions': {}})
    assert play.name == 'test play'
    assert play.id == '123123123'
    assert play.connection == 'local'
    assert play.gather_facts == 'no'
    assert play.hosts == 'all'

# Generated at 2022-06-13 08:39:11.174524
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    dynamic_data = dict(
        name="testPlay",
        hosts="localhost",
        vars="testVars",
        roles="testRoles"
    )
    dynamic_play = Play()
    dynamic_play.preprocess_data(dynamic_data)
    assert dynamic_play.name == "testPlay"
    assert dynamic_play.hosts == "localhost"
    assert dynamic_play.vars == "testVars"
    assert dynamic_play.roles == "testRoles"

# Generated at 2022-06-13 08:39:23.310209
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # get_vars_files is a method of the class Play, instantiating an object p
    p = Play()
    # Check if the attribute vars_files is correctly set to None as default
    assert(p.vars_files == None)
    # set the attribute vars_files to ''
    p.vars_files = ''
    # Check that the method get_vars_files correctly handles the case where vars_files was set to ''
    assert(p.get_vars_files() == [''])
    # set the attribute vars_files to an empty list
    p.vars_files = []
    # Check that the method get_vars_files correctly handles the case where vars_files was set to []
    assert(p.get_vars_files() == [])
    # set the attribute vars_files

# Generated at 2022-06-13 08:39:30.924973
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    fake_role = MagicMock()
    fake_role_compiled_handlers = ['fake_handler','fake_handler','fake_handler']
    play.ROLE_CACHE = {'fake_role':fake_role}
    fake_role.get_handler_blocks.return_value = fake_role_compiled_handlers
    result = play.compile_roles_handlers()
    assert result == fake_role_compiled_handlers


# Generated at 2022-06-13 08:39:35.169026
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.roles = None
    result = play.compile_roles_handlers()
    assert result is not None
    assert result == []

# Generated at 2022-06-13 08:39:49.050702
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play_kv_list = dict2kvlist({"hosts": "all", "tasks": [{"name": "Debian Package Manager", "action": {"module": "apt", "name": "*", "state": "present"},
                                      "register": {"package": "apt_output"}}]})
    play_ds = kvlist2data("hosts:all\ntasks:\n  - name: Debian Package Manager\n    action:\n      module: apt\n      name: *\n      state: present\n    register:\n      package: apt_output")
    play = Play.load(play_ds, variable_manager=None, loader=None, vars=None)

# Generated at 2022-06-13 08:39:55.039421
# Unit test for method serialize of class Play
def test_Play_serialize():
    '''
    Unit test for method serialize of class Play
    '''
    dummy_play = Play()
    import io
    import yaml
    test_file = io.StringIO()
    yaml.safe_dump(dummy_play.serialize(), test_file)
    test_file.seek(0)
    assert test_file.read()
test_Play_serialize()



# Generated at 2022-06-13 08:40:04.656182
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.__init__()
    assert(play.get_name() == '')
    play.name = 'raid'
    assert(play.get_name() == 'raid')
    play.hosts = "10.0.0.2"
    assert(play.get_name() == '10.0.0.2')
    play.hosts = ["10.0.0.1","10.0.0.2"]
    assert(play.get_name() == "10.0.0.1,10.0.0.2")
    assert(play.get_name() == play.name or play.get_name() == ','.join(play.hosts))


# Generated at 2022-06-13 08:40:29.587995
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = [{"action": "shell", "args": '', "name": "print hello"}, {"action": "shell", "args": '', "name": "print hello"}]
    assert play.get_tasks() == play.tasks

# Generated at 2022-06-13 08:40:34.867216
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    data = {}
    data['user'] = 'lol'
    data['remote_user'] = 'lol'
    p.preprocess_data(data)
    print(data)
    assert data['remote_user'] == 'lol' and 'user' not in data


# Generated at 2022-06-13 08:40:43.217834
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = play.pre_tasks = play.post_tasks = []
    assert play.get_tasks() == []

    play = Play()
    play.tasks = [1]
    play.pre_tasks = [3]
    play.post_tasks = [2]
    assert play.get_tasks() == [3, 1, 2]

    play = Play()
    play.tasks = Block.load(data={'block': 'b'})
    play.pre_tasks = Block.load(data={'block': 'c'})
    play.post_tasks = Block.load(data={'block': 'd'})
    assert play.get_tasks() == ['c', 'b', 'd']

    play = Play()
    assert play.get

# Generated at 2022-06-13 08:40:48.348056
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = "roles/app/vars/Config.yml"
    assert_equal(play.get_vars_files(), ["roles/app/vars/Config.yml"])


# Generated at 2022-06-13 08:40:50.363635
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert Play.compile_roles_handlers(Play()) is not None


# Generated at 2022-06-13 08:40:58.099841
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    Unit test for method Play.get_vars_files
    '''
    p = Play()

    # Set vars_files as empty list
    p.vars_files = []
    assert p.get_vars_files() == []

    # Set vars_files as not a list
    p.vars_files = " /test/test.yml"
    assert p.get_vars_files() == [" /test/test.yml"]

    # Set vars_files as a list
    p.vars_files = [" /test/test1.yml", " /test/test2.yml"]
    assert p.get_vars_files() == [" /test/test1.yml", " /test/test2.yml"]
