

# Generated at 2022-06-13 08:31:35.354957
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    result = __test_target__.Play._compile_roles_handlers(__test_target__.Play())
    assert type(result) == list
    assert len(result) == 0
    assert result == []

    result = __test_target__.Play().compile_roles_handlers()
    assert type(result) == list
    assert len(result) == 0
    assert result == []

# Generated at 2022-06-13 08:31:38.027148
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()
    p.deserialize({"roles": ["hello"]})

    assert p.roles[0].name == "hello", "Did not deserialize hello"



# Generated at 2022-06-13 08:31:50.210610
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
  from ansible.playbook.play import Play
  from ansible.playbook.task import Task
  from ansible.playbook.block import Block
  p = Play()
  one = Task()
  one.name = 'first task'
  two = Task()
  two.name = 'second task'
  three = Task()
  three.name = 'third task'
  four = Task()
  four.name = 'fourth task'
  p.pre_tasks = [one, two]
  p.tasks = [three, four]
  p.post_tasks = [four]
  print(p.get_tasks())
  b1 = Block()
  b1.attributes = {'name':'first block'}
  b2 = Block()

# Generated at 2022-06-13 08:31:51.985587
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    
    assert play.compile_roles_handlers() == []

# Generated at 2022-06-13 08:31:57.366233
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    old = Play.load({
        'name': 'test',
        'connection': 'local',
        'hosts': ['all'],
        'roles': [{
            'name': 'role1',
            'tasks': [{
                'meta': 'dummy'
            }]
        }]
    })
    new = Play()
    new.deserialize(old.serialize())
    assert old.serialize() == new.serialize()


# Generated at 2022-06-13 08:32:06.445424
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = [('foo', 'bar')]
    p.post_tasks = [('foo2', 'bar2')]
    assert p.get_tasks() == [('foo', 'bar'), ('foo2', 'bar2')]
    p.pre_tasks = [('foo3', 'bar3')]
    assert p.get_tasks() == [('foo3', 'bar3'), ('foo', 'bar'), ('foo2', 'bar2')]

# Generated at 2022-06-13 08:32:20.250548
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import __main__
    setattr(__main__, '__file__', 'test_file')
    import ansible.playbook.play_context as pc
    setattr(pc.PlayContext, 'variable_manager', MagicMock())
    setattr(pc.PlayContext, 'set_options', MagicMock())
    setattr(pc.PlayContext, 'load_options', MagicMock())

    p = Play()
    tasks = [
        Block(),
        Block(),
        Block()
    ]

    setattr(p, 'pre_tasks', tasks)
    setattr(p, 'tasks', tasks)
    setattr(p, 'post_tasks', tasks)

    result = p.get_tasks()
    assert result == tasks * 9, "get_tasks() returned incorrect result"

# Unit test

# Generated at 2022-06-13 08:32:35.578183
# Unit test for method get_name of class Play
def test_Play_get_name():
    role_data = {"name": "test-role", "file": "/etc/ansible/roles/test-role/role.yml"}

    play = Play()
    play.name = "test-play"
    assert play.get_name() == "test-play"

    play = Play()
    play.hosts = "test-host"
    assert play.get_name() == "test-host"

    play = Play()
    play.hosts = ["test-host-1", "test-host-2"]
    assert play.get_name() == "test-host-1,test-host-2"

    play = Play()
    play.name = "test-play"
    play.hosts = ["test-host-1", "test-host-2"]

# Generated at 2022-06-13 08:32:36.323791
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    pass

# Generated at 2022-06-13 08:32:44.802357
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(connection='local', module_path=None, forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False, vault_password=None)
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/hosts')
    variable_manager.set_inventory(inventory)
    play = Play()
    play.vars_prompt = dict()
    play.connection = 'local'
    play.hosts = 'all'
    play.name = "my play"
    play.port = 22
    play.remote_user = 'root'
    play.roles = []
    play.serial = 1

# Generated at 2022-06-13 08:32:59.846243
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Dummy values for unit test
    data = 'dummy'

    # Create an object for testing
    play_test = Play()

    # Unit test default values
    assert play_test.get_roles() == []
    assert play_test._included_path is None
    assert play_test._action_groups == {}
    assert play_test._group_actions == {}

    # Code to exercise
    play_test.deserialize(data)

    # Check results
    assert play_test.get_roles() == []
    assert play_test._included_path is None
    assert play_test._action_groups == {}
    assert play_test._group_actions == {}


# Generated at 2022-06-13 08:33:06.058122
# Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:33:09.265645
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play_object = Play()
    actual_output = play_object.get_vars_files()
    expected_output = []
    assert expected_output == actual_output


# Generated at 2022-06-13 08:33:10.638200
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    pass # test is delayed to play.py

# Generated at 2022-06-13 08:33:26.770992
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()

# Generated at 2022-06-13 08:33:36.737965
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Setup
    ds = {'hosts': 'hostname', 'vars_files': ['/path/to/vars_file.yml', 'path/to/other_vars_file.yml']}
    p=Play.load(ds, variable_manager=None, loader=None, vars=None)
    r = []
    # Test
    if p.get_vars_files() != r:
        print("Expected: %s but got %s" % (r, p.get_vars_files()))
        exit()
    else:
        print("Test passed")


# Generated at 2022-06-13 08:33:38.988621
# Unit test for constructor of class Play
def test_Play():
    p = Play()
    assert isinstance(p, Play)

# Generated at 2022-06-13 08:33:39.890712
# Unit test for method serialize of class Play
def test_Play_serialize():
    pass

# Generated at 2022-06-13 08:33:41.331044
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    assert True

# Generated at 2022-06-13 08:33:49.286647
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    # __doc__ (as of 2016-03-03) for ansible.playbook.play.Play.preprocess_data:

    #     preprocess_data handles internal play-specific quirks and transforms play data
    #     into a form which can be consumed directly by the Play class.
    assert p.preprocess_data('data') == 'data'

# Generated at 2022-06-13 08:34:14.446793
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''Unit test for method compile_roles_handlers of class Play
    '''

    from ansible.playbook.block import Block # pylint: disable=unused-variable
    from ansible.playbook.handler import Handler # pylint: disable=unused-variable
    from ansible.playbook.role import Role # pylint: disable=unused-variable
    from ansible.playbook.task import Task # pylint: disable=unused-variable

    # We should have a list of 1 handler
    p = Play()
    h1 = Handler()
    h1.action = 'test1'
    h2 = Handler()
    h2.action = 'test2'
    blocks = [Block(handlers=[h1,h2])]

# Generated at 2022-06-13 08:34:26.454545
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p1 = Play()
    try:
        p1.get_tasks()
    except Exception as e:
        assert type(e) == AttributeError
    assert p1.get_tasks() == []

    p2 = Play()
    p2.pre_tasks = ['pre']
    p2.tasks = ['middle']
    p2.post_tasks = ['end']
    assert p2.get_tasks() == ['pre','middle','end']

    p3 = Play()
    p3.pre_tasks = ['pre']
    p3.tasks = ['middle']
    assert p3.get_tasks() == ['pre','middle']

    p4 = Play()
    p4.pre_tasks = ['pre']
    p4.tasks = ['middle']
    p4.post

# Generated at 2022-06-13 08:34:33.987823
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = '1'
    assert play.get_vars_files() == ['1']
    play.vars_files = [1]
    assert play.get_vars_files() == ['1']
    play.vars_files = [1, 2]
    assert play.get_vars_files() == ['1', '2']


# Generated at 2022-06-13 08:34:39.565945
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    raw_data = {
        'user': 'root',
        'roles': [
            'role_1',
            'role_2',
        ],
    }
    expected_data = {'roles': ['role_1', 'role_2'], 'remote_user': 'root'}
    p = Play()
    data = p.preprocess_data(raw_data)
    assert(data == expected_data)

# Generated at 2022-06-13 08:34:45.762737
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.errors import AnsibleParserError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import add_all_plugin_dir

# Generated at 2022-06-13 08:34:58.970620
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import IncludeTask
    from ansible.playbook.task.include import TaskInclude
    from ansible.playbook.task.task import Task
    from ansible.vars.hostvars import HostVars
    #from ansible.vars.manager import VariableManager
    #from ansible.template import Templar
  
    # Set up the Play context
    play_name = u'test_play'
    tasks = [Task()]
    handlers = [Task()]
    vars_prompts = []
    roles = []
    defaults = task_vars = []
    #var_manager = VariableManager()
    #var_manager.extra_vars = HostVars

# Generated at 2022-06-13 08:35:08.538622
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:35:14.715428
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    
    # Create fake data for the class
    #   Loader
    _loader = None
    #   Data
    data = dict(
        #   Attributes
        connections=dict(network_cli=dict(connection=dict(host='127.0.0.1'))),
        hosts=['127.0.0.1'],
        name='Play 1',
        gather_facts='no',
        roles=[]
    )
    #   Variables
    variables = dict(
        ansible_python_interpreter='/usr/bin/python3'
    )
    #   Self
    play = Play()
    
    
    # Create a fake Role
    role = Role()
    # Add the fake role to the fake data
    data['roles'].append(role)
    # Create a fake handler
    fake_

# Generated at 2022-06-13 08:35:15.501588
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass

# Generated at 2022-06-13 08:35:17.191544
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    assert Play().get_vars_files() == []

# Generated at 2022-06-13 08:35:41.394815
# Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:35:56.411531
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    play_ds = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        roles=[
            dict(
                name='abc',
                handlers=[dict(name='xyz', tags=["tag1"])],
            ),
            dict(
                name='def',
                handlers=[dict(name='pqr', tags=["tag2"])],
            ),
            dict(
                include_role=dict(name='mno', tasks_from="main")
            ),
        ]
    )
    p = Play.load(play_ds, loader=loader, variable_manager=variable_manager)
    p.compile()
    assert p.compile_roles_handlers() == p.hand

# Generated at 2022-06-13 08:35:59.876165
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    if not hasattr(Play, '_Play__compile_roles_handlers'):
        Play._Play__compile_roles_handlers = Play.compile_roles_handlers


# Generated at 2022-06-13 08:36:06.664208
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    
    play = Play()
    
    play.pre_tasks = ['a']
    
    play.tasks = ['b']
    
    play.post_tasks = ['c']
    
    task_list = play.get_tasks()
    
    assert task_list[0] == 'a' , 'Not expected tasks'
    
    assert task_list[1] == 'b' , 'Not expected tasks'
    
    assert task_list[2] == 'c' , 'Not expected tasks'


# Generated at 2022-06-13 08:36:09.992397
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    assert p.get_vars_files() == []

    p.vars_files = 1
    assert p.get_vars_files() == [1]

    p.vars_files = [1,2]
    assert p.get_vars_files() == [1,2]

# Generated at 2022-06-13 08:36:12.992391
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    data = {'name': 'test-play',
            'user': 'test-user',
            'hosts': 'test-hosts'}
    assert play.preprocess_data(data) == {'name': 'test-play',
                                          'remote_user': 'test-user',
                                          'hosts': 'test-hosts'}


# Generated at 2022-06-13 08:36:14.914211
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = "Test Play"
    assert play.get_name() == "Test Play"

# Generated at 2022-06-13 08:36:19.813391
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create a Play object.
    play = Play()

    # Create a Set object.
    roles = Set()

    # Create a Role object.
    role = Role()

    # Create a Handler object.
    handler = Handler()

    handler.name = 'test_handler'
    handler.block = [{'tasks': [{'action': {'__ansible_module__': 'debug', 'msg': 'I have been to test_handler'}, 'name': 'debug'}], 'name': 'Main'}]
    handler.include_roles = []
    handler.include_tasks = []
    handler.local_action = None
    handler.local_action_args = {}
    handler.loop = []
    handler.notify = []
    handler.register = None
    handler.rescue = []
    handler.tags

# Generated at 2022-06-13 08:36:29.914755
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    Function to test get_vars_files method of class Play.
    '''
    from ansible.config.manager import ConfigManager
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 08:36:44.540591
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # We need to init the class, so we can run the compile_roles_handlers method
    play = Play()
    play.load({}, variable_manager=VariableManager(), loader=DataLoader())

    # We should get an empty list of handlers, if we have no roles.
    assert play.compile_roles_handlers() == []

    # Add a list of roles with handlers, and check that we get the correct
    # list of handler blocks back.
    for role_data in [{'handlers': [{'name': 'test_handler_1'}]}, {'handlers': [{'name': 'test_handler_2'}]}]:
        role = Role()
        role.load(role_data, variable_manager=VariableManager(), loader=DataLoader())
        play.get_roles().append(role)

   

# Generated at 2022-06-13 08:37:02.853212
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()

    play.pre_tasks = ["test"]
    assert play.get_tasks() == ["test"]

    play.post_tasks = ["test"]
    assert play.get_tasks() == ["test"]

    play.tasks = ["test"]
    assert play.get_tasks() == ["test"]

# Generated at 2022-06-13 08:37:07.212258
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():  # unit test for method get_vars_files of class Play
    p = Play()
    p.vars_files = ["file1", "file2"]
    assert p.get_vars_files() == ["file1", "file2"]

# Generated at 2022-06-13 08:37:18.735530
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.plugins import filter_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    # Instantiate an instance of class Play
    p = Play()
    assert p.get_name() == ''
    p.name = 'testing'
    assert p.get_name() == 'testing'
    # p.tasks contains a dict of test data
    p.tasks = [{'register': 'output_of_debug', 'debug': {'var': 'hostvars'}}]
    # Instantiate an instance of class VariableManager
    v = VariableManager()
    # Now filter is tested
    f = filter_loader.get('to_nice_json')
    # Instantiate an instance of class Templar
    t = Templar(loader=None, variables=v)

# Generated at 2022-06-13 08:37:30.509500
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:37:41.177906
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    a = AnsibleFileLoader(loader, variable_manager, file_name='somefile')
    p = Play()
    p.vars_files = 'some_file'
    assert(p.get_vars_files() == ['some_file'])

    p.vars_files = None
    assert(p.get_vars_files() == [])

    p.vars_files = ['a', 'b', 'c']
    assert(p.get_vars_files() == ['a', 'b', 'c'])

# Generated at 2022-06-13 08:37:46.855546
# Unit test for method get_name of class Play
def test_Play_get_name():
    """
    .........

    """
    # print('-------In test_Play_get_name()-------')
    _self = Play()
    _self.name = 'my_name'
    assert _self.get_name() == 'my_name'
    # print('-------Out test_Play_get_name()-------')


# Generated at 2022-06-13 08:37:47.720405
# Unit test for method get_name of class Play
def test_Play_get_name():
    pass

# Generated at 2022-06-13 08:37:51.246338
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Creation of play object
    p1= Play()
    # Calling method compile_roles_handlers of class Play
    p1.compile_roles_handlers()

# Generated at 2022-06-13 08:38:01.486360
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass


if __name__ == '__main__':
    # generate synthetic data
    data = {
        'hosts': 'host1:host2',
        'user': 'testuser'
    }

    # create an object
    play = Play()
    current_dir = os.path.dirname(__file__)
    data_dir_path = os.path.join(current_dir, '../data')
    include_dir_path = os.path.join(data_dir_path, 'playbook_include')
    file_paths = [os.path.join(include_dir_path, 'playbook.yaml')]
    vars_manager = VariableManager()
    vars_manager.extra_vars = dict()

    loader = DataLoader()

# Generated at 2022-06-13 08:38:07.580449
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    class data(object):
        pass

    data = data()
    data.name = "test"
    data.path = "path"
    play = Play()
    play._ds = data
    play._loader = None
    play._variable_manager = None
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:38:43.569248
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize(
        data = {
            'name': '1234567890',
            'roles': [
                {
                    '_role_path': '/path/to/role',
                    'name': 'rolename',
                    'vars': {'a': 'b'}
                }
            ],
            'options': {'option1': 'value1'},
            'included_path': 'path to include',
            'action_groups': {'group1': [1, 2, 3]},
            'group_actions': {1: 'group1', 2: 'group2'}
        }
    )
    assert play.name == '1234567890'
    role = play.get_roles()[0]
    assert role.name == 'rolename'

# Generated at 2022-06-13 08:38:46.588522
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import ansible.playbook.play
    play = ansible.playbook.play.Play()
    play.compile_roles_handlers()

# Generated at 2022-06-13 08:38:59.222887
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.module_utils._text import to_bytes
    import json
    #for the test we remove possible ansible.cfg file so that to not use config from that file
    import os
    import os.path
    old_ansible_cfg_path = os.path.join(os.getcwd(), 'ansible.cfg')
    if os.path.isfile(os.path.join(os.getcwd(), 'ansible.cfg')):
        os.remove(old_ansible_cfg_path)

    hosts_data = json.loads(to_bytes("{\"hosts\": [\"foo\", \"bar\"]}"))
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play()
    play.preprocess_data(hosts_data)

    hosts_data1 = json.loads

# Generated at 2022-06-13 08:38:59.929073
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # TODO
    pass

# Generated at 2022-06-13 08:39:00.635097
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    assert True

# Generated at 2022-06-13 08:39:01.222524
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:39:06.962559
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    strip_cache_dir = '/tmp/ansible_test_Play_get_tasks_%s' % random.randint(1, 1000)

# Generated at 2022-06-13 08:39:09.203231
# Unit test for method get_name of class Play
def test_Play_get_name():
    obj = Play()
    assert obj.get_name() == "localhost"



# Generated at 2022-06-13 08:39:11.122852
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:39:23.264158
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Normal case
    p = Play()
    p.name = 'test'
    assert p.get_name() == 'test'

    # Boundary case: hosts is empty
    p = Play()
    p.hosts = []
    assert p.get_name() == ''

    # Normal case: hosts is a list with one element
    p = Play()
    p.hosts = ['host']
    assert p.get_name() == 'host'

    # Normal case: hosts is a list with 2 element
    p = Play()
    p.hosts = ['host1', 'host2']
    assert p.get_name() == 'host1,host2'

    # Normal case: hosts is a string
    p = Play()
    p.hosts = 'host'
    assert p.get_name() == 'host'

# Generated at 2022-06-13 08:39:51.596825
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play1 = Play()
    res = play1.compile_roles_handlers()
    assert_equals(res, [])

# Generated at 2022-06-13 08:40:02.051184
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.vars.manager
    import ansible.vars.hostvars
    from ansible.utils.vars import combine_vars

    # Requires that test_get_vars() is passing
    p = Play()

    # Default to empty list
    assert p.get_vars_files() == []

    # vars_files as a single file
    p.vars_files = 'file.yml'
    assert p.get_vars_files() == ['file.yml']

    # vars_files as a list of files
    p.vars_files = ['file1.yml', 'file2.yml']

# Generated at 2022-06-13 08:40:03.409925
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()

# Generated at 2022-06-13 08:40:10.137706
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    collection_search_list = []
    print("\n")
    print("Print the role objects")
    print("\n")

    # Create a list of roles to load
    roles_list = ['role1', 'role2']

    # Create a list of roles
    roles = []
    for role in roles_list:
        # Create a role object
        # Role object has three attributes: collection_name, name, from_include
        role = Role(collection_name = 'collection1', name = role, from_include = False)

        # Set up role.tasks and role.handlers
        role.tasks = [1, 2, 3]
        #role.handlers = [4, 5, 6]
        role.handlers = None

        # Add the role object to the list of roles
        roles.append(role)

   

# Generated at 2022-06-13 08:40:21.006461
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    '''
    Unit test for method preprocess_data of class Play
    '''
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.template
    testcase = dict()
    testcase['bogus'] = dict()
    testcase['name'] = 'playtest'
    testcase['hosts'] = 'all'
    testcase['roles'] = ['role1', 'role2']
    testcase['connection'] = 'local'
    play = ansible.playbook.play.Play()
    assert play.preprocess_data(testcase)
    assert play.vars == {}, "Expect empty dictionary"
    assert play.hosts == ["all"], "Expect hosts to be ['all']"

# Generated at 2022-06-13 08:40:24.630246
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'mockhost'
    assert play.get_name() == 'mockhost'

# Generated at 2022-06-13 08:40:30.189259
# Unit test for method get_name of class Play
def test_Play_get_name():
    host = '127.0.0.1'
    play_name = 'test_play'
    play = Play()
    play.name = play_name
    play.hosts = host
    assert play.get_name() == play_name


# Generated at 2022-06-13 08:40:41.970424
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import ast
    import tempfile
    from collections import namedtuple
    from ansible.module_utils.common._collections_compat import MutableSequence
    from ansible.plugins.loader import connection_loader, filter_loader, lookup_loader, module_loader, module_utils_loader, test_loader, ys_loader, strategy_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_iterator import PlaybookIterator
    from ansible.playbook.play import Play
    from ansible.parsing.plugin_docs import read_vault_docs
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 08:40:48.180109
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    """
    Unit: Play._validate_hosts

    This method is used by the _validate_hosts method.
    """
    with pytest.raises(Exception) as exception_info:
        play = Play()
        play._validate_hosts(None, None, None)
    assert 'Requires a non-' in str(exception_info.value)


# Generated at 2022-06-13 08:40:49.883633
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    assert play.get_name() == ''