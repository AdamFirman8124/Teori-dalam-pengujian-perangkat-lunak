

# Generated at 2022-06-13 08:31:32.382565
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Instantiate play object
    p = Play()

    # test compile_roles_handlers method
    assert p.compile_roles_handlers() == []


# Generated at 2022-06-13 08:31:37.022461
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    p.preprocess_data([])
    p.preprocess_data({})
    with pytest.raises(AnsibleAssertionError, match=r'ds should be a dict'):
        p.preprocess_data('ds')


# Generated at 2022-06-13 08:31:49.404754
# Unit test for method get_name of class Play
def test_Play_get_name():

    play = Play()
    play.name = 'test'
    assert play.get_name() == 'test'

    play = Play()
    assert play.get_name() == ''

    #Test for Hosts list with strings
    play.hosts = "test"
    play.name = None
    assert play.get_name() == 'test'

    #Test for Hosts list with sequences
    play.hosts = ["test", "test1"]
    play.name = None
    assert play.get_name() == 'test,test1'

    #Test for None
    play.hosts = None
    play.name = None
    assert play.get_name() == ''

    #Test for Hosts list with non string and non sequence data type
    play.hosts = object()
    play.name = None

# Generated at 2022-06-13 08:31:56.763008
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # set up
    def load_roles(ds):
        return []
    def load_role(ds):
        return Role()
    mock_role = Role()
    mock_role.from_include = False
    mock_role.get_handler_blocks = lambda: [Handler()]
    Play.ROLE_CACHE = {}
    Play.ROLE_CACHE['mock_role'] = mock_role
    setattr(Play, '_load_roles', load_roles)
    setattr(Play, '_load_role', load_role)
    play = Play()
    play.role_names = ['mock_role']
    play.roles = [mock_role]
    # test
    handler_blocks = play.compile_roles_handlers()

# Generated at 2022-06-13 08:32:10.406277
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    '''
    Tests Play.preprocess_data method
    '''
    # precondition: test runs under sos/ansible_collections/sos/ansible
    expected_call_lines = [
        "assert(ds is not None)",  # check for ds not being None
        "assert(False) # should never reach this"  # check for error when ds is not a dict
    ]
    expected_assign_lines = [
        "ds = dict()",
        "ds['user'] = 'test_user'",
        "ds['remote_user'] = ds['user']",
        "del ds['user']",
        "ds = 'test_ds'"
    ]

# Generated at 2022-06-13 08:32:10.834139
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
	pass

# Generated at 2022-06-13 08:32:11.873212
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass

# Generated at 2022-06-13 08:32:21.968287
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    # test the user to remote_user change
    ds = {'user': 'root'}
    assert p.preprocess_data(ds) == {'remote_user': 'root'}

    # test preprocess vars

# Generated at 2022-06-13 08:32:37.177995
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Test with empty dict
    data = {}
    p = Play()
    p.deserialize(data)

    # test with data

# Generated at 2022-06-13 08:32:45.415395
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    def run_test(expected_output, input_dict, test_id, collection_search_path=None, fail_on_undefined_errors=False, tags=[], skip_tags=[]):
        play = Play()
        play.ROLE_CACHE = {}
        play._included_conditional = None
        play._included_path = None
        play._removed_hosts = []
        play.only_tags = set(tags) or frozenset(('all',))
        play.skip_tags = set(skip_tags)
        play._action_groups = {}
        play._group_actions = {}
        play.vars = input_dict.get('vars', {})
        play.roles = []
        play.hosts = []
        play.remote_user = None
        play.remote_port

# Generated at 2022-06-13 08:32:57.639528
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():

    with open("/home/kiran/dev/git/ansible-test/test/test_data/test-playbook/test_data/playbooks/test_play/test_play.yml") as f:
        play_data = yaml.load(f)
    for play in play_data:
        play = Play.load(play)
        print(play.get_tasks())

# Generated at 2022-06-13 08:33:09.850731
# Unit test for method serialize of class Play
def test_Play_serialize():

    # Test playbook data
    ds = {}
    expected_data = {}
    expected_data['roles'] = []
    expected_data['included_path'] = None
    expected_data['action_groups'] = {}
    expected_data['group_actions'] = {}

    # Test constructor without any data
    p = Play()

    # Test serialize method with no data
    data = p.serialize()
    assert(data == expected_data)

    # Test with playbook data
    p.serialize()

    # Test with roles data
    r = Role()
    expected_data['roles'] = [r.serialize()]
    p.roles = [r]
    data = p.serialize()
    assert(data == expected_data)



# Generated at 2022-06-13 08:33:11.037365
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:33:23.798489
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.pre_tasks = [ 'foo', 'bar', 'baz' ]
    p.tasks = [ 'o', 'f', 'u' ]
    p.post_tasks = [ 'b', 'a', 'f', 'o' ]
    
    # Test return value
    a = p.get_tasks()
    b = [ 'foo', 'bar', 'baz', 'o', 'f', 'u', 'b', 'a', 'f', 'o' ]
    
    assert a == b, "Return value of Play.get_tasks() is not as expected."

# Generated at 2022-06-13 08:33:31.998987
# Unit test for method get_name of class Play
def test_Play_get_name():
    '''
    Play: test get_name method
    '''

    print("get name")
    # setup
    vars = {}
    p = Play()
    p.name = None
    p.hosts = "hosts"

    # test
    print("hosts is not a sequence")
    assert p.get_name() == "hosts"

    print("hosts is a sequence")
    p.hosts = [1,2,3]
    assert p.get_name() == "1,2,3"

    print("play name is None, hosts is None")
    p.hosts = None
    assert p.get_name() == ""

    print("play name is not None, hosts is None")
    p.name = "name"
    assert p.get_name() == "name"


# Generated at 2022-06-13 08:33:33.089080
# Unit test for method get_name of class Play
def test_Play_get_name():
    pass


# Generated at 2022-06-13 08:33:49.057441
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    playbook_data = dict(
        name=u'My Playbook',
        hosts=['first_host', 'second_host'],
        gather_facts=False,
        roles=[
            dict(name='first_role',
                 tasks=[
                     dict(name='first task',
                          debug=dict(msg='this is first task'))
                 ],
                 handlers=[
                     dict(name='first_handler',
                          debug=dict(msg='this is first handler')),
                     dict(name='second_handler',
                          debug=dict(msg='this is second handler'))
                 ]
            )
        ],
        handlers=[
            dict(name='first_handler',
                 debug=dict(msg='this is first handler'))
        ]
    )

# Generated at 2022-06-13 08:33:55.522599
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    from argparse import Namespace
    from ansible.config.manager import ConfigManager, ConfigData
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    c = ConfigManager(data=ConfigData(parser=Namespace()))
    loader = DataLoader()
    variable_manager = VariableManager()
    p = Playbook.load(loader.load_from_file('../test/test.yml'), variable_manager, loader).get_plays()[0]
    s = p.serialize()
    new_p = Play.load({}, variable_manager, loader, {})
    new_p.deserialize(s)
    assert new_p.serialize() == s


# Generated at 2022-06-13 08:33:59.613500
# Unit test for method serialize of class Play
def test_Play_serialize():
    # vars
    play_ = dict()

    # Actual execution
    serialize = Play().serialize()
    #print("\nserialize:")
    #print(serialize)
    #print("")

    # test
    assert serialize == play_


# Generated at 2022-06-13 08:34:02.399699
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Create a new Play object
    p = Play()
    # Test the function
    assert p.get_vars_files() == []


# Generated at 2022-06-13 08:34:27.108629
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    test_data = {
        "name": "TestPlay",
        "gather_facts": True,
        "remote_user": "localhost",
        "roles": [{
            "name": "role_1",
            "tasks": [{
                "include": "include_test.yml",
                "action": "include",
                "name": "include role_1"
            }, {
                "action": "debug",
                "name": "test debug",
                "args": {
                    "msg": "hello from task"
                }
            }]
        }]
    }
    test_play = Play()
    test_play.deserialize(test_data)
    assert(test_play.name == "TestPlay")
    assert(test_play.gather_facts == True)

# Generated at 2022-06-13 08:34:39.225500
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    p.vars = {"foo": "var"}
    p.vars_prompt = [{"name": "bar", "prompt": "Prompt", "default": "default", "private": False, "confirm": False, "encrypt": None, "salt_size": None, "salt": None, "unsafe": False}]
    p.roles = [{"role": "name", "role_path": "/foo/bar"}]
    p._action_groups = {"role": ["foo", "bar"]}
    p._group_actions = {"foo":["role"]}
    data = p.serialize()
    assert data["vars"] == {"foo": "var"}
    assert data["vars_prompt"][0]["name"] == "bar"

# Generated at 2022-06-13 08:34:51.604761
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    name = play.get_name()
    # print(name)
    assert name == ""
    play.name = "MyPlay"
    name = play.get_name()
    # print(name)
    assert name == "MyPlay"
    play.hosts = "myserver"
    name = play.get_name()
    # print(name)
    assert name == "MyPlay"
    play.name = ""
    name = play.get_name()
    # print(name)
    assert name == "myserver"
    play.hosts = ["server1", "server2"]
    name = play.get_name()
    # print(name)
    assert name == "server1,server2"

# Generated at 2022-06-13 08:35:00.104243
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = [Task(action='action1'), Task(action='action2'), Task(action='action3')]
    play.pre_tasks = [Task(action='action4'), Task(action='action5'), Task(action='action6')]
    play.post_tasks = [Task(action='action7'), Task(action='action8'), Task(action='action9')]
    assert play.get_tasks() == [Task(action='action4'), Task(action='action5'), Task(action='action6'), Task(action='action1'), Task(action='action2'), Task(action='action3'), Task(action='action7'), Task(action='action8'), Task(action='action9')]

# Generated at 2022-06-13 08:35:08.053646
# Unit test for method deserialize of class Play
def test_Play_deserialize():

    # Test with data that deserializes correctly
    data = {"name": "testPlay", "roles": [], "vars": {"key": "value"}}
    play = Play()
    play.deserialize(data)

    for key in data.keys():
        assert play.__dict__.get(key, None) == data[key]

    # Test with missing roles
    data = {"name": "testPlay", "vars": {"key": "value"}}
    play = Play()
    play.deserialize(data)

    for key in data:
        assert play.__dict__.get(key, None) == data[key]


# Generated at 2022-06-13 08:35:13.460524
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Test with a standard datastructure and no legacy data,
    # like the one generated after call to 'serialize'
    p = Play()
    r = Role()
    r.deserialize({'role_name': 'role1', 'role_path': '/foo/bar'})
    p.deserialize({'hosts': 'host1', 'roles': [r.serialize()], 'name': 'play1', 'connection': 'local'})
    # Check that the deserialization worked
    assert p.name == 'play1'
    assert p.connection == 'local'
    assert len(p.roles) == 1



# Generated at 2022-06-13 08:35:16.181521
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    ___tracebackhide__ = True
    ___assertEqual(['1', '2'], Play().get_tasks())

# Generated at 2022-06-13 08:35:17.502773
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks=[1,2,3]
    tasks = play.get_tasks()
    assert tasks == [1,2,3]


# Generated at 2022-06-13 08:35:23.726864
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Create an instance of Play
    p = Play()
    # Initialise attribute
    p.pre_tasks = [Block()]
    p.tasks = [Block()]
    p.post_tasks = [Block()]

    tasks = p.get_tasks()
    assert tasks == [Block()] * 6, 'Compiled tasks should be [Block()] * 6'

# Generated at 2022-06-13 08:35:33.776529
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # '''
    # Test Play.get_tasks method
    # '''
    import unittest
    import sys
    from ansible.module_utils.ansible_release import __version__
    from ansible import context
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display
    # create the global Display object that will be used
    # setup the localhost config

# Generated at 2022-06-13 08:35:59.407547
# Unit test for constructor of class Play
def test_Play():
    from units.mock.loader import DictDataLoader

    # Create play from v2
    play_ds_v2 = """
- name: test play
  hosts: testhost
  tasks:
    - debug:
        msg: hello
"""
    play_v2 = Play.load(
        play_ds_v2,
        variable_manager=VariableManager(),
        loader=DictDataLoader({None: play_ds_v2})
    )
    assert len(play_v2.tasks) == 1
    assert play_v2.handlers == []
    assert play_v2.pre_tasks == []
    assert play_v2.post_tasks == []
    assert play_v2.roles == []

    # Create play from v1

# Generated at 2022-06-13 08:36:02.072575
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    PL = Play()
    PL.load_data({
        'name': 'test-play',
        'hosts': 'test-hosts',
    })
    PL.tasks = [1]
    PL.pre_tasks = []
    PL.post_tasks = []
    assert PL.get_tasks() == [1]

# Generated at 2022-06-13 08:36:10.358000
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.hostvars import HostVars
    from io import StringIO

    fake_loader = DataLoader()

    # test get_tasks without tasks
    myPlay = Play()
    assert myPlay.get_tasks() == []

    # test get_tasks with tasks
    task1 = Task()
    task2 = Task()
    tasklist = [task1, task2]
    myPlay = Play()
    myPlay.tasks = tasklist
    assert myPlay.get_tasks() == task

# Generated at 2022-06-13 08:36:17.746986
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = "test_value"
    play.name = "test_name"
    play.hosts = "test_hosts"
    play.become = "test_become"
    play.become_method = "test_become_method"
    play.become_user = "test_become_user"
    play.remote_user = "test_remote_user"
    play.vars = dict()
    play.tags = ["test_tags"]
    play.connection = "test_connection"
    play.transport = "test_transport"
    play.playbook = "test_playbook"
    play.gather_facts = "test_gather_facts"
    play.serialize()



# Generated at 2022-06-13 08:36:28.835970
# Unit test for method serialize of class Play
def test_Play_serialize():
    def TestPlay__load_roles(attr, ds):
        try:
            role_includes = load_list_of_roles(ds, play=self, variable_manager=self._variable_manager,
                                               loader=self._loader, collection_search_list=self.collections)
        except AssertionError as e:
            raise AnsibleParseError("A malformed role declaration was encountered.", obj=self._ds, orig_exc=e)

        roles = []
        for ri in role_includes:
            roles.append(Role.load(ri, play=self))

        self.roles[:0] = roles

        return self.roles
    global_test_data = load_test_data()
    # Test Play
    p = Play()
    # Test global variables
    p.ROLE_C

# Generated at 2022-06-13 08:36:36.602072
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()

    assert p.get_vars_files() == []
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = 1
    assert p.get_vars_files() == [1]
    p.vars_files = [2, 3]
    assert p.get_vars_files() == [2, 3]

# Generated at 2022-06-13 08:36:48.937130
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # test the case when vars_files is not a list
    pl = Play()
    pl.vars_files = "a_file"
    vars_files = pl.get_vars_files()
    if isinstance(vars_files, list):
        raise AssertionError('The returned value of vars_files is a list when it is not a list')
    if vars_files[0] != "a_file":
        raise AssertionError('The returned content of vars_files is not correct')

    # test the case when vars_files is a list
    pl = Play()
    pl.vars_files = ["test1", "test2"]
    vars_files = pl.get_vars_files()
    if not isinstance(vars_files, list):
        raise AssertionError

# Generated at 2022-06-13 08:37:03.679474
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    """
    Test preprocess_data with the following cases:
    - ds should be a dict
    - ds is a dict and has a key 'user', which is deprecated.
    """
    play_me = Play()
    try:
        play_me.preprocess_data(list())
        assert False, "Test should have thrown an exception"
    except AnsibleAssertionError:
        assert True
    ds1 = {'user': 'ansi'}
    try:
        play_me.preprocess_data(ds1)
        assert False, "Test should have thrown an exception"
    except AnsibleParserError as e:
        assert 'user' in str(e)
        assert True
    ds2 = {'remote_user': 'ansi'}

# Generated at 2022-06-13 08:37:08.609680
# Unit test for constructor of class Play
def test_Play():
    '''
    >>> p = Play()
    >>> p.__class__.__name__
    'Play'
    '''

    '''
    >>> p.vars = dict(foo='bar')
    >>> p.vars
    {'foo': 'bar'}
    '''


# Generated at 2022-06-13 08:37:16.295514
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # play = Play()
    # play.vars_files = None
    # assert play.get_vars_files() == []
    # play.vars_files = ['vars_files']
    # assert play.get_vars_files() == ['vars_files']
    # play.vars_files = ['vars_files1', 'vars_files2']
    # assert play.get_vars_files() == ['vars_files1', 'vars_files2']
    pass

# Generated at 2022-06-13 08:37:33.356322
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
	play = Play()
	play.__init__()
	play._load_roles = mock.MagicMock()
	play.serialize = mock.MagicMock()
	play.deserialize = mock.MagicMock()
	play.copy = mock.MagicMock()
	play.compile = mock.MagicMock()
	play.compile_roles_handlers()


# Generated at 2022-06-13 08:37:35.320042
# Unit test for method get_name of class Play
def test_Play_get_name():
    obj = Play()
    assert obj.get_name() == ''


# Generated at 2022-06-13 08:37:41.340243
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = [1, 2, 3]
    play.tasks = [4, 5, 6]
    play.post_tasks = [7, 8, 9]
    assert play.get_tasks() == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Generated at 2022-06-13 08:37:43.249026
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []

# Generated at 2022-06-13 08:37:52.860803
# Unit test for method serialize of class Play
def test_Play_serialize():

    collection_loader = C.collection_loader
    collection_loader._collected_paths = ['/tmp/test']

    test = '''
        - name: Play 1
          hosts: localhost
          roles:
            - test_role
        '''

    data = yaml.safe_load(test)

    ############################# Test 'roles'
    # Test '' in 'roles'
    data['roles'] = ''
    p = Play.load(data, variable_manager=variable_manager, loader=loader)
    assert p.serialize() == {'roles': [], 'name': 'Play 1', 'deprecated_tags': ['meta', 'tasks', 'handlers'], 'hosts': 'localhost', 'included_path': None, 'action_groups': {}, 'group_actions': {}}
    #

# Generated at 2022-06-13 08:37:54.081881
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # assert role_handler
    assert True

# Generated at 2022-06-13 08:38:03.681836
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Test if compile_roles_handlers returns a list of handlers
    # in the case where self.roles is not empty
    play = Play()
    play.roles = ['test']
    assert isinstance(play.compile_roles_handlers(), list)
    assert isinstance(play.compile_roles_handlers()[0], Handler)
    # Test if compile_roles_handlers returns an empty list
    # in the case where self.roles is empty
    play1 = Play()
    play1.roles = []
    assert isinstance(play1.compile_roles_handlers(), list)
    assert len(play1.compile_roles_handlers()) == 0


# Generated at 2022-06-13 08:38:08.877080
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    data = {'user': 'root', 'hosts': 'all'}
    play.preprocess_data(data)
    assert 'user' not in data and 'hosts' in data and 'remote_user' in data


# Generated at 2022-06-13 08:38:16.659702
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
        play = Play()
        block = Block(exc=['test1', 'test2'],res=['test3','test4'],alw=['test5','test6'])
        play.pre_tasks = ['test0']
        play.tasks = [block]
        play.post_tasks = ['test7']
        result = play.get_tasks()		
        assert result == ['test0', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7']


# Generated at 2022-06-13 08:38:18.665903
# Unit test for method serialize of class Play
def test_Play_serialize():
    """
    Test serialize method of Play class
    """
    assert True


# Generated at 2022-06-13 08:38:43.920731
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # initialize ansible
    ansible.initialize()
    
    # use AnsibleModule to emulate ansible module argument parsing
    module_instance = AnsibleModule(argument_spec={})
    module_args = {}
    module_instance.params = module_args
    
    # initialize empty play with args
    play_instance = Play()
    play_instance.vars_files = []
    
    # call get_vars_files and check the result
    play_instance.get_vars_files()


# Generated at 2022-06-13 08:38:58.952734
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import yaml
    play = Play.load(yaml.load("""---
    - hosts: localhost
      gather_facts: yes
      tasks:
        - name: test
          command: /bin/false
          changed_when: false
          failed_when: true
          notify:
            - test_1
            - test_2
            - test_3
          tags: [foo, bar]
          when: false
          with_items:
            - 1
            - 2
          with_file: foo
          with_fileglob: bar
          with_my_test: baz
          with_random_choice: bar
          with_sequence: foo
          with_subelements:
            - 1
            - 2
          with_together:
            - 1
            - 2
"""))

# Generated at 2022-06-13 08:39:02.062821
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    p.name = 'test_Play_serialize'
    p.hosts = 'hosts1'
    p_dict = p.serialize()
    p2 = Play()
    p2.deserialize(p_dict)
    p2_dict = p2.serialize()
    assert p_dict == p2_dict


# Generated at 2022-06-13 08:39:13.703732
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.parsing.dataloader import DataLoader

    import pytest

    # Unnamed Example, show in docs
    p = Play()
    ds = [
        {'name': 'example', 'hosts': 'hosts'},
        {'hosts': 'hosts', 'gather_facts': 'no'},
        {'name': 'another_example', 'hosts': 'hosts', 'gather_facts': 'no'}
    ]

    Play.preprocess_data(ds[0])
    Play.preprocess_data(ds[1])
    Play.preprocess_data(ds[2])

    # Named Example

# Generated at 2022-06-13 08:39:22.450719
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pre_tasks = [{'name': 'first'}]
    tasks = [{'name': 'second'}]
    post_tasks = [{'name': 'third'}]
    play_obj = Play(pre_tasks=pre_tasks, tasks=tasks, post_tasks=post_tasks)
    assert play_obj.get_tasks() == [{'name': 'first'}, {'name': 'second'}, {'name': 'third'}]

# Generated at 2022-06-13 08:39:29.607979
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play(
        name='test',
        hosts='localhost',
        tasks=[
            dict(
                name='test 1',
                ping='pong'
            ),
            dict(
                test_task_2=dict(
                    name='test 2',
                    ping='pong'
                )
            ),
            dict(
                test_task_3=dict(
                    name='test 3',
                    ping='pong'
                )
            ),
            dict(
                name='test 4',
                ping='pong'
            )
        ]
    )
    tasks = p.get_tasks()
    assert isinstance(tasks[0], Task)
    assert tasks[1].block[0].name == 'test 2'
    assert tasks[2].block[0].name == 'test 3'

# Generated at 2022-06-13 08:39:37.336511
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    pre_tasks = [Block(), Block()]
    tasks = [Block(), Block()]
    post_tasks = [Block(), Block()]
    play.set_loader(DataLoader())

    play._pre_tasks = pre_tasks
    play._tasks = tasks
    play._post_tasks = post_tasks

    real_tasks = play.get_tasks()
    assert real_tasks[0] == pre_tasks[0].block + pre_tasks[0].rescue + pre_tasks[0].always
    assert real_tasks[1] == pre_tasks[1].block + pre_tasks[1].rescue + pre_tasks[1].always

    assert real_tasks[2] == tasks[0].block + tasks[0].rescue

# Generated at 2022-06-13 08:39:38.403726
# Unit test for method get_name of class Play
def test_Play_get_name():
    v = Play()
    assert v.get_name() == ''



# Generated at 2022-06-13 08:39:50.088600
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    role1 = Role()
    role1.name = "role1"
    role2 = Role()
    role2.name = "role2"
    role3 = Role()
    role3.name = "role3"

    handler1 = Handler()
    handler1.name = "handler1"
    handler1.task = Mock()
    handler1.block = [handler1.task]
    handler2 = Handler()
    handler2.name = "handler2"
    handler2.task = Mock()
    handler2.block = [handler2.task]
    handler3 = Handler()
    handler3.name = "handler3"
    handler3.task = Mock()
    handler3.block = [handler3.task]
    handler4 = Handler()
    handler4.name = "handler4"
    handler4.task = Mock

# Generated at 2022-06-13 08:40:01.076300
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()

# Generated at 2022-06-13 08:40:21.003718
# Unit test for method serialize of class Play
def test_Play_serialize():
    hn  = Host('hostname')
    hn2 = Host('hostname')
    v = variable_manager.VariableManager()
    p = Play()
    p.hosts = 'hostname'
    p.vars = {'key': 'value'}
    data = p.serialize()
    assert 'variables' in data
    assert 'roles' in data
    assert 'action_groups' in data
    assert 'group_actions' in data


# Generated at 2022-06-13 08:40:24.088424
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    result = p.get_tasks()
    assert (result == [])


# Generated at 2022-06-13 08:40:32.896999
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Setup play
    play_ds = dict(
        name="TESTPLAY",
        hosts=None,
        pre_tasks=list(),
        tasks=list(),
        post_tasks=list()
    )
    play = Play()
    play.vars = dict()
    play.load_data(data=play_ds)

    # Test against empty list
    expected = list()
    result = play.get_tasks()
    assert result == expected



# Generated at 2022-06-13 08:40:43.914340
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import os
    from ansible.cli.playbook import PlaybookCLI
    from ansible.utils.vars import combine_vars

    pb = PlaybookCLI(['--list-tasks', 'test/ansible/playbook/test_playbook.yml'])
    pb.parse()
    pb.basedir = os.path.abspath(os.path.curdir)
    playbook = pb.load_playbook_file()
    # Load playbook
    for play in playbook.get_plays():
        if play.name == 'test_play':
            test_play = play
    # Set vars
    vars_manager = pb.variable_manager
    vars_manager._extra_vars = combine_vars(pb.extra_vars, ignore_errors=True)
   

# Generated at 2022-06-13 08:40:50.703362
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Test the method when the value of variables 'pre_tasks', 'tasks' and 'post_tasks' is None
    p = Play()
    p.pre_tasks = None
    p.tasks = None
    p.post_tasks = None
    assert p.get_tasks() == []
    # Test the method when the value of variables 'pre_tasks', 'tasks' and 'post_tasks' equals to an empty list
    p = Play()
    p.pre_tasks = []
    p.tasks = []
    p.post_tasks = []
    assert p.get_tasks() == []
    # Test the method when the value of variables 'pre_tasks', 'tasks' and 'post_tasks' equals to a list contains tasks
    p = Play()
    p.pre

# Generated at 2022-06-13 08:40:55.435283
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create a Play object
    p = Play()
    # Set value for private attribute '_roles' of Play object
    p._roles = [ 'role1', 'role2' ]
    # Call method compile_roles_handlers of Play object
    result = p.compile_roles_handlers()
    # Assertion
    assert result == None

# Generated at 2022-06-13 08:40:56.713503
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    pass


# Generated at 2022-06-13 08:41:11.566946
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = None
    assert play.get_vars_files() == []
    play.vars_files = "a.yml"
    assert play.get_vars_files() == ["a.yml"]
    play.vars_files = ["a.yml", "b.yml"]
    assert play.get_vars_files() == ["a.yml", "b.yml"]
    play.vars_files = ["a.yml", "b.yml", "c.yml"]
    assert play.get_vars_files() == ["a.yml", "b.yml", "c.yml"]