

# Generated at 2022-06-13 08:31:39.389051
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    #
    # Confirm that deserialize works to re-construct a Play object
    #

    # Put members that vary into a dictionary, x_dict
    #
    x_dict = {}
    x_dict['vars'] = dict()
    x_dict['vars']['myvar'] = 'myvalue'

    # Create an instance of Play
    #
    x_play = Play()

    # Load the x_dict values into the instance
    #
    x_play.deserialize(x_dict)

    # Construct the expected output
    #
    y_dict = {}

    # Put members that vary into a dictionary, y_dict
    #
    y_dict['vars'] = dict()
    y_dict['vars']['myvar'] = 'myvalue'

    # Create an instance of Play


# Generated at 2022-06-13 08:31:48.880703
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Init a valid Play object
    play = Play()

    # Test get_vars_files
    play.vars_files = ['/etc/ansible/hosts']
    assert play.get_vars_files() == ['/etc/ansible/hosts']

    play.vars_files = None
    assert play.get_vars_files() == []

    play.vars_files = '../../../../../etc/ansible/main.yml'
    assert play.get_vars_files() == ['../../../../../etc/ansible/main.yml']

# Generated at 2022-06-13 08:31:53.329231
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = {
        'roles': [],
        'connection': 'ssh',
        'hosts': 'all',
        'vars': {},
        'gather_facts': 'yes',
        'max_fail_percentage': 0,
        'serial': 0,
        'name': 'test name',
        'included_path': [],
        'action_groups': {},
        'group_actions': {},
        'strategy': 'linear'
    }
    play = Play()
    play.deserialize(data)
    assert data == play.serialize()


# Generated at 2022-06-13 08:31:57.563937
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    assert p.preprocess_data({'user':'spam'})=={'remote_user':'spam'}
    p.preprocess_data({'user':'spam'})
    assert p.preprocess_data({'remote_user':'spam'})=={'remote_user':'spam'}

# Generated at 2022-06-13 08:32:03.338077
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.tasks.append(Task())
    play.handlers.append(Handler())
    play.roles.append(Role())
    play._loader = DictDataLoader({})
    assert play.compile_roles_handlers() == play.handlers


# Generated at 2022-06-13 08:32:12.377558
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'test_play'
    assert p.get_name() == 'test_play'
    assert p.get_name() == 'test_play'
    p.hosts = ['host']
    assert p.get_name() == 'host'
    assert p.get_name() == 'host'
    p.hosts = None
    assert p.get_name() == ''
    assert p.get_name() == ''

#Unit test for class Play

# Generated at 2022-06-13 08:32:22.249150
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    try:
        Play().preprocess_data(1)
    except:
        pass
    else:
        assert False

    try:
        Play().preprocess_data(None)
    except:
        pass
    else:
        assert False

    try:
        Play().preprocess_data({'name': 'test'})
    except:
        assert False
    else:
        assert True

    try:
        Play().preprocess_data({'name': 'test', 'user': 'test'})
    except:
        assert False
    else:
        assert True

    try:
        Play().preprocess_data({'name': 'test', 'user': 'test', 'remote_user': 'test'})
    except:
        assert True
    else:
        assert False



# Generated at 2022-06-13 08:32:37.441239
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    print("\n\n\n\n")
    print("Start of tests for Play.compile_roles_handlers\n")
    print("-------------------------------------------------------------------------")
    print("\n\n\n\n")
    play = Play()
    play._variable_manager = _VariableManager()
    play.vars = dict()
    play.default_vars = dict()
    play.roles = [Role(name='')]
    # print("play.roles: ", play.roles)
    # print("play.roles[0].get_handler_blocks(play): ", play.roles[0].get_handler_blocks(play))
    result = play.compile_roles_handlers()
    # print("result: ", result)

# Generated at 2022-06-13 08:32:38.751057
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert False, "Add your test here"


# Generated at 2022-06-13 08:32:49.589749
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    vars_files = play.get_vars_files()
    assert isinstance(vars_files, list)
    assert vars_files == []
    play.vars_files = "/tmp/test_Play_get_vars_files.yml"
    vars_files = play.get_vars_files()
    assert isinstance(vars_files, list)
    assert vars_files == ["/tmp/test_Play_get_vars_files.yml"]
    play.vars_files = ["/tmp/test_Play_get_vars_files.yml", "/tmp/test_Play_get_vars_files-1.yml"]
    vars_files = play.get_vars_files()
    assert isinstance(vars_files, list)

# Generated at 2022-06-13 08:33:09.360824
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # test run
    playbook = Playbook()
    p = Play()
    p.load(None, {'name': 'hostsall', 'hosts': 'all', 'roles': [{'role': 'foo', 'x': 1, 'y':{'z':'bar'}, 'tags':['tagA', 'tagB']}]}, playbook=playbook)
    p.load_vars_prompt(None, [{'name':'foo', 'vars_prompt': 'Are you sure?', 'private': False}])
    h = p.compile_roles_handlers()
    assert(isinstance(h, list))
    assert(len(h) == 4)
    assert(isinstance(h[0], Block))
    assert(h[0].block[0].handler is True)

# Generated at 2022-06-13 08:33:20.488534
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    def test():
        Play_preprocess_data_runs()
    def Play_preprocess_data_runs():
        data = "test"
        obj = Play()
        try:
            obj.preprocess_data(data)
        except AssertionError as e:
            print(e)
        # Test if data is a dictionary
        assert isinstance(data, dict)
        # Test if the data keys have been successfully mapped to the the play attributes
        assert data != obj._valid_attrs.keys()
    test()

# Generated at 2022-06-13 08:33:29.907368
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    """
    Unit test for method get_tasks of class Play
    """
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.hostvars import HostVarsGroup
    from ansible.vars.hostvars import HostVarsGroups
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import ansible.constants as C
    import io
    import os
    import tempfile

    # Create a temporary directory

# Generated at 2022-06-13 08:33:31.566679
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    Play.get_tasks()

# Generated at 2022-06-13 08:33:35.988390
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Create a new role r
    r = Role()
    # Create a new play p
    p = Play()
    # Create a new block b
    b = Block(play=p)
    # Add a new task to r
    r.task = Task()
    r._compile_roles = lambda: [b]
    # Add the role r to p
    p.roles = [r]
    # Test that p.get_tasks returs the task from r
    assert p.get_tasks() == [[b.block + b.rescue + b.always]]

# Generated at 2022-06-13 08:33:51.259203
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = ['./vars_files/test_vars_files.yml']
    assert p.get_vars_files() == ['./vars_files/test_vars_files.yml']
    p.vars_files = './vars_files/test_vars_files.yml'
    assert p.get_vars_files() == ['./vars_files/test_vars_files.yml']
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = "./vars_files/test_vars_files.yml"

# Generated at 2022-06-13 08:33:56.192361
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.hosts = "hosts_value"
    assert play.get_name() == "hosts_value"
    play.name = "name_value"
    assert play.get_name() == "name_value"


# Generated at 2022-06-13 08:34:09.000073
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    assert p.preprocess_data({}) == {}
    assert p.preprocess_data({'tasks': [{'name': 'task', 'become': 'true'}]}) == {'tasks': [{'name': 'task', 'become': True}]}
    assert p.preprocess_data({'tasks': [{'include': 'role', 'role': 'role'}]}) == {'tasks': [{'include': 'role'}]}

# Generated at 2022-06-13 08:34:09.958746
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:34:16.724078
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    my_Play=Play()
    my_Play.vars_files = None
    assert my_Play.get_vars_files() == []

    my_Play.vars_files = ["/tmp/test"]
    assert my_Play.get_vars_files() == ['/tmp/test']

    my_Play.vars_files = ["/tmp/test", "/tmp/test2"]
    assert my_Play.get_vars_files() == ['/tmp/test', '/tmp/test2']


# Generated at 2022-06-13 08:34:36.413842
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import ansible.utils
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import ansible.playbook.helpers
    from ansible.playbook.task_include import TaskInclude
    import ansible.inventory.host
    from ansible.playbook.role_include import RoleInclude
    import ansible.constants
    import ansible.errors
    from ansible.compat.six import StringIO
    import ansible.playbook.name_utils
    from ansible.vars.manager import VariableManager
    import ansible.parsing.dataloader
    import ansible.playbook.play
    import ansible.template
    import ansible.inventory.group
    import ansible.playbook.play_context
    import ansible.playbook.conditional


# Generated at 2022-06-13 08:34:44.060767
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    """
    Test the Play.preprocess_data() method with a simple data structure.
    """
    from ansible.playbook.play import Play
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    raw_data = {
        'hosts': 'all',
        'user': 'foo',
        'tasks': [
            { 'action': { 'module': 'shell', 'args': 'echo 1', 'user': 'bar' } },
        ]
    }
    p = Play().load(raw_data)
    assert p.user is None
    assert p.remote_user == 'foo'
    assert p.tasks[0].user == 'bar'


# Generated at 2022-06-13 08:34:57.679177
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    """
    Test Play.deserialize()
    """

    my_play = Play()

# Generated at 2022-06-13 08:35:06.011227
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    
    block = Block('block_name', None, None, None, None)
    task = Task('task_name', None, None, None, None)
    
    block_list = [block, task]
    
    play = Play()
    
    play.pre_tasks = block_list
    play.tasks = block_list
    play.post_tasks = block_list
    
    play.get_tasks()



# Generated at 2022-06-13 08:35:11.133148
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Create a test Play object
    play = Play()

    # Create some data structure to test with
    ds = {'name': 'Test',
            'hosts': 'testhosts',
            'user': 'testuser'}

    # Run the preprocess_data method
    return_value = play.preprocess_data(ds)

    # Verify that the correct data structure was returned
    assert return_value == {'name': 'Test',
                            'hosts': 'testhosts',
                            'remote_user': 'testuser'}


# Generated at 2022-06-13 08:35:23.819220
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Test with no tasks in the play
    p = Play()
    p.vars = dict()
    assert p.get_tasks() == []

    # Test with two tasks, no pre_tasks, no post_tasks
    p = Play()

    t1 = Task()
    t1.name = 'task 1'
    t1.action = 'debug'
    t1.args = dict()

    t2 = Task()
    t2.name = 'task 2'
    t2.action = 'debug'
    t2.args = dict()

    p.tasks = [t1, t2]

    assert p.get_tasks() == [t1, t2]

    # Test with no tasks, with two pre_tasks, no post_tasks
    p = Play()
    p.pre_

# Generated at 2022-06-13 08:35:33.983557
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """
    Fake test for Play.compile_roles_handlers
    """
    fake_play = Play()
    fake_play._included_conditional = None
    fake_play._included_path = None
    fake_play._removed_hosts = []
    fake_play.ROLE_CACHE = {}
    fake_play.roles = None
    fake_play.serial = None
    fake_play.tags = frozenset()
    fake_play.vars = {}
    fake_play.when = None
    fake_play.only_tags = set(())
    fake_play.skip_tags = set(())
    fake_play._action_groups = {}
    fake_play._group_actions = {}
    fake_play.handlers = []



# Generated at 2022-06-13 08:35:45.185758
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
        Unit test for method compile_roles_handlers of class Play
        Play class represents a Ansible playbook.
        This method is supposed to compile the handler blocks from the roles
        that are assigned to the play.
    '''

    def mock_play_role_compile(play):
        '''
        Mocked method for compile_roles_handlers
        This is to mock the Role.compile() method,
        and return an empty list.
        '''
        assert isinstance(play, Play), \
            'Parameter play is not from class Play!'
        return []

    play = Play()
    play.roles.append(Role())
    play.roles.append(Role())
    play.roles.append(Role())
    play.roles.append(Role())
    play.roles[0].comp

# Generated at 2022-06-13 08:35:49.192100
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Given
    play_obj = Play()

    # When
    result = play_obj.compile_roles_handlers()

    # Then
    assert result == []

# Generated at 2022-06-13 08:36:00.738000
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()

# Generated at 2022-06-13 08:36:16.776823
# Unit test for method serialize of class Play

# Generated at 2022-06-13 08:36:23.205122
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = {}
    assert Play().preprocess_data(ds) == ds

    ds = 'test'
    assert Play().preprocess_data(ds) == ds

    ds = 0
    assert Play().preprocess_data(ds) == ds

    ds = None
    assert Play().preprocess_data(ds) == ds



# Generated at 2022-06-13 08:36:28.648123
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize({"hosts": None, "name": "show-upgrade", "connection": "local", "vars": {}, "meta": {}})
    assert play.name == "show-upgrade"
    assert type(play.vars) is types.DictType
    assert play.connection == "local"
    assert play.hosts is None


# Generated at 2022-06-13 08:36:30.480810
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

 

# Generated at 2022-06-13 08:36:34.813244
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    vars_files = ['vars_file']
    play._ds['vars_files'] = vars_files

    play.get_vars_files() == vars_files

# Generated at 2022-06-13 08:36:48.311789
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    import pytest
    deserialize_data = dict(  # dict to be deserialized
        example_dict = dict(
            example_item = 7,
            example_item2 = 'seven',
        ),
        example_list = [
            'some',
            'items'
        ]
    )
    p = Play() # Create Play object
    p.deserialize(deserialize_data) # Deserialize dict into Play object
    assert p.example_dict.example_item == 7 # Test deserialization
    assert p.example_dict.example_item2 == 'seven' # Test deserialization
    assert p.example_list == ['some', 'items'] # Test deserialization
    assert p.example_list[0] == 'some' # Test deserialization

# Generated at 2022-06-13 08:36:50.067428
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # TODO after implementing Role.compile()
    pass


# Generated at 2022-06-13 08:36:59.363414
# Unit test for method get_name of class Play
def test_Play_get_name():
    '''
    test get_name method of class Play
    '''
    play = Play()
    play.name = 'all'
    assert play.get_name() == 'all'

    play.name = None
    play.hosts = 'test_host'
    assert play.get_name() == 'test_host'

    play.hosts = ['host1', 'host2']
    assert play.get_name() == 'host1,host2'



# Generated at 2022-06-13 08:37:02.446648
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # == Assert return values
    #  assert()
    # == Assert raise
    #  assert_raises()
    return True

# Generated at 2022-06-13 08:37:04.315219
# Unit test for method get_name of class Play
def test_Play_get_name():
    p=Play()
    assert p.get_name()==''



# Generated at 2022-06-13 08:37:12.641244
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # FIXME: create test case
    return


# Generated at 2022-06-13 08:37:16.079132
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.tasks = []
    # isinstance of class list
    assert isinstance(play.compile_roles_handlers(), list)


# Generated at 2022-06-13 08:37:21.820959
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p1 = '''
- hosts: localhost
  roles:
    - test
- hosts: remotehost
  tasks:
    - name: test
      debug: msg=hello
'''
    p = Play.load(p1, variable_manager=VariableManager())
    data = p.serialize()
    p2 = Play()
    p2.deserialize(data)
    p2.serialize()

# Generated at 2022-06-13 08:37:26.843855
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    p.name = 'test_play'
    p.hosts = 'test_host'
    p.roles = [Role()]
    new_p = p.copy()
    assert p.serialize() == new_p.serialize(), "serialize should be the same"


# Generated at 2022-06-13 08:37:33.129160
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Create a fake play
    p = Play()
    # Create data structure to be preprocessed
    # In this case, the data structure will be not modified
    ds = {'hosts': 'localhost'}
    # Create a expected data structure
    expected = {'hosts': 'localhost'}
    # Call and assert the preprocess_data method
    assert p.preprocess_data(ds) == expected


# Generated at 2022-06-13 08:37:36.726209
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    test_play = Play()
    test_play._load_roles(None)
    assert test_play.compile_roles_handlers() is not None

# Generated at 2022-06-13 08:37:43.623633
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # FIXME(tzumainn): this needs to be rewritten.
    # the code currently being tested requires a call to serialize,
    # which is not needed here.
    # reload(ansible.playbook.play)
    # play_c = ansible.playbook.play.Play()
    # assert isinstance(play_c.compile_roles_handlers(), list)
    pass



# Generated at 2022-06-13 08:37:52.690915
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Loads the play dictionary
    play_data = load_playbook_data_from_file('/home/aman/Automation/ansible/ansible-2.7.2/test/unit/test_playbook/test_plays/get_tasks/get_tasks.yml')

    # Loads the play class
    play_class = Play()

    # Loads the play
    play_class.load(play_data[0])

    # Prints the stored tasks
    for task in play_class.tasks:
        print(task.serialize())


# Generated at 2022-06-13 08:37:57.407151
# Unit test for method deserialize of class Play
def test_Play_deserialize():    
    class Fake_Play(Play):
        def __init__(self):
            self.name = ""
            self.vars = {}
            self.roles = []
    obj = Fake_Play()
    data = dict(roles=[dict(name="", tasks=list())])
    obj.deserialize(data=data)

# Generated at 2022-06-13 08:38:09.229269
# Unit test for constructor of class Play

# Generated at 2022-06-13 08:38:25.704572
# Unit test for method deserialize of class Play
def test_Play_deserialize():

    play = Play()
    play.deserialize({"_ds": {}, "_included_path": None})
    assert play.serialize()["included_path"] == None
    play.deserialize({"_ds": {}, "_included_path": ""})
    assert play.serialize()["included_path"] == ""
    play.deserialize({"_ds": {}, "_included_path": "Some path"})
    assert play.serialize()["included_path"] == "Some path"

    play.deserialize({"_ds": {}, "_action_groups": {}})
    assert play._action_groups == {}
    play.deserialize({"_ds": {}, "_action_groups": "string"})
    assert play._action_groups == "string"
    play.deserialize

# Generated at 2022-06-13 08:38:40.533829
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansiblelint.rules.DeprecatedModuleRule import DeprecatedModuleRule
    p = Play()
    p.pre_tasks = ['printf "The current date and time is: %s %s\n" "$(date +%Y-%m-%d)" "$(date +%H:%M:%S)"']
    p.post_tasks = ['printf "The current date and time is: %s %s\n" "$(date +%Y-%m-%d)" "$(date +%H:%M:%S)"']
    rule = DeprecatedModuleRule()
    results = rule.matchplay(p)
    assert len(results) == 2
    assert results[0].linenumber == 0
    assert results[0].data['deprecated_module'] == 'command'
    assert results[1].linenumber

# Generated at 2022-06-13 08:38:52.690887
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    """
    `test_Play_get_tasks` is used to unit test the `get_tasks` method of class `Play`
    """
    tasks = []
    task1 = {'hosts': 'host1', 'roles': ['role1', 'role2']}
    task2 = {'hosts': 'host2', 'roles': ['role3', 'role4']}
    tasks.append(task1)
    tasks.append(task2)
    play = Play.load(tasks, variable_manager=None, loader=None, vars=None)
    assert isinstance(play.get_tasks(), list)


# Generated at 2022-06-13 08:39:03.016949
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from collections import namedtuple

    test_inventory = """
        [local]
        localhost ansible_connection=local
        [local:vars]
        ansible_python_interpreter=/usr/bin/python3
    """


# Generated at 2022-06-13 08:39:03.966837
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:39:14.411896
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    p = Play()
    p.deserialize(data={'roles': [{'name': 'test_role', 'default_vars': {'a': 'b'}}, {'name': 'test_role2', 'default_vars': {'a': 'b'}}]})
    assert isinstance(p.roles, list)
    assert isinstance(p.roles[0], Role)
    assert isinstance(p.roles[1], Role)
    assert p.roles[0].name == 'test_role'
    assert p.roles[1].name == 'test_role2'


# Generated at 2022-06-13 08:39:17.790687
# Unit test for method get_name of class Play
def test_Play_get_name():
    myPlay = Play()
    myPlay.name = "MyPlay"
    assert myPlay.get_name() == "MyPlay"


# Generated at 2022-06-13 08:39:24.109753
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """Returns a list of handlers for a given play"""
    play_ds = dict(
        name = "test_play",
        hosts = ["localhost"],
        roles = "test_role"
    )
    play = Play()
    play.load(
        play_ds,
        variable_manager=None,
        loader=None
    )
    assert play.compile_roles_handlers() == list()

# Generated at 2022-06-13 08:39:34.211678
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    '''
    Unit test for method deserialize of class Play
    '''
    import sys
    import tempfile

    # Setup logging handlers if required
    # Ansible-test will inject its own handlers here, since this test uses logging
    # and we want to capture the logs for use in debugging.
    if not logging._handlers:
        logging.basicConfig(filename="test_log", level=logging.DEBUG)

    # Create temporary file for use for testing purposes
    fd, tfile = tempfile.mkstemp(text=True)

    # Create playbook contents

# Generated at 2022-06-13 08:39:34.787705
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass

# Generated at 2022-06-13 08:39:43.000649
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    assert True, "Untested"

# Generated at 2022-06-13 08:39:43.966620
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass #TODO: Write unit test

# Generated at 2022-06-13 08:39:47.193880
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    fh = open("./test/unittests/test_play_preprocess_data.yml", "r")
    data = fh.read()
    p = Play()
    data = p.preprocess_data(data)
    print(data)


# Generated at 2022-06-13 08:39:53.384414
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    pre_tasks = []
    post_tasks = []
    play._tasks = play._load_tasks('tasks', {})
    play._pre_tasks = play._load_pre_tasks('pre_tasks', pre_tasks)
    play._post_tasks = play._load_post_tasks('post_tasks', post_tasks)
    result = play.get_tasks()
    assert result == [play._tasks, pre_tasks, play._post_tasks]


# Generated at 2022-06-13 08:40:02.329050
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Test with no hosts nor name set
    p     = Play()
    name  = p.get_name()

    assert name == ''

    # Test with hosts set
    p     = Play()
    name  = p.get_name()

    assert name == ''

    # Test with hosts set
    p.hosts = ''
    name  = p.get_name()

    assert name == ''

    # Test with name set
    p     = Play()
    name  = p.get_name()

    assert name == ''

    # Test with name set
    p.name = 'play_name'
    name  = p.get_name()

    assert name == 'play_name'

# Generated at 2022-06-13 08:40:14.449862
# Unit test for method serialize of class Play
def test_Play_serialize():
    _role = {'foo': 'bar'}
    _roles = [_role]
    _included_path = '/path/to/something'
    _action_groups = {'greet': [1, 2]}
    _group_actions = {1: 'hello', 2: 'hi'}

# Generated at 2022-06-13 08:40:20.333525
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    play.vars_files = []
    assert play.get_vars_files() == []
    play.vars_files = [1]
    assert play.get_vars_files() == [1]
    play.vars_files = None
    assert play.get_vars_files() == []



# Generated at 2022-06-13 08:40:25.665708
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    vars_files = [1, 2]
    p = Play()
    p.vars_files = vars_files
    result = p.get_vars_files()
    assert result == [1, 2]


# Generated at 2022-06-13 08:40:38.868685
# Unit test for method get_name of class Play
def test_Play_get_name():

    # EXCEPTION SHORTCUT TESTING 'get_name' method
    short_exception_test = False
    try:
        # This should be impossible, but let's make sure it doesn't get through
        instance = Play()
        instance.get_name()
    except AnsibleParserError:
        short_exception_test = True
    assert short_exception_test is True

    # EXCEPTION SHORTCUT TESTING 'get_name' method
    short_exception_test = False
    try:
        # This should be impossible, but let's make sure it doesn't get through
        instance = Play()
        instance.hosts = False
        instance.get_name()
    except AnsibleParserError:
        short_exception_test = True
    assert short_exception_test is True

    # EXCEPTION

# Generated at 2022-06-13 08:40:43.836528
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    # variable 'p' not in scope
    # so, break into 3 lines
    p1 = p.compile_roles_handlers()
    # p1 = p.compile_roles_handlers()
    assert p1 == []


# Generated at 2022-06-13 08:41:11.451054
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    test_play = Play()
    test_play.vars = {}