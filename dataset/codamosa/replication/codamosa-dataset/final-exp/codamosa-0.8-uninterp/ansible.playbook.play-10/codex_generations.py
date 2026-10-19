

# Generated at 2022-06-13 08:31:21.536058
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.set_loader(Mock())
    play.vars_files = 'test_vars_files'
    assert play.get_vars_files() == ['test_vars_files']


# Generated at 2022-06-13 08:31:27.296939
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    #testcase 1
    p = Play()
    p.pre_tasks = [{"test":"test"}]
    p.tasks = [{"test":"test"}, [{"test":"test"}]]
    p.post_tasks = [{"test":"test"}]
    assert p.get_tasks() == [{"test":"test"}, {"test":"test"}, [{"test":"test"}], {"test":"test"}]

# Generated at 2022-06-13 08:31:30.520056
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    assert isinstance(play.get_tasks(), list)


# Generated at 2022-06-13 08:31:32.608469
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.hosts = ["localhost"]
    play.get_name()
    assert play.name == "localhost"


# Generated at 2022-06-13 08:31:44.914124
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play.load(dict(
                name="Test Play",
                hosts="testhost",
                connection="local",
                gather_facts="no",
                tasks=[dict(action=dict(module="shell", args="ls")), dict(action=dict(module="shell", args="pwd"))]))
    data = play.serialize()
    play = Play()
    play.deserialize(data)
    assert isinstance(play, Play)
    assert isinstance(play.tasks[0], Task)
    assert isinstance(play.tasks[0].action, ActionModule)
    assert isinstance(play.tasks[1], Task)
    assert isinstance(play.tasks[1].action, ActionModule)

# Generated at 2022-06-13 08:31:54.301567
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = dict(
        name='foo.yml',
        hosts={'hostname': 'host1'},
        gather_facts={'hostname': 'host1'},
        serial={'hostname': 'host1'},
        max_fail_percentage=1.1,
        vars={'var': 'val'},
        vars_prompt={'var': 'val'},
        vault_password={'hostname': 'host1'},
        roles=['role1', 'role2'],
        environment={'hostname': 'host1'},
        blocks=[],
        handlers=[],
        tasks=[],
        pre_tasks=[],
        post_tasks=[],
        included_path='included_path',
        action_groups={},
        group_actions={}
    )

# Generated at 2022-06-13 08:32:00.405685
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    play.vars_files = []
    assert play.get_vars_files() == []
    play.vars_files = 'a'
    assert play.get_vars_files() == ['a']
    play.vars_files = ['a', 'b']
    assert play.get_vars_files() == ['a', 'b']


# Generated at 2022-06-13 08:32:06.614653
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    #Test when vars_files is None
    play.vars_files = None
    result = play.get_vars_files()
    assert result == [], "get_vars_files() returned: %s" % str(result)

    #Test when vars_files is a list
    play.vars_files = ["file1", "file2"]
    result = play.get_vars_files()
    assert result == ['file1', 'file2'], "get_vars_files() returned: %s" % str(result)

    #Test when vars_files is not a list
    play.vars_files = "file1"
    result = play.get_vars_files()

# Generated at 2022-06-13 08:32:20.359389
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible import errors; from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    ansible_facts = {}
    ansible_facts['ipv4'] = {'address': '1.1.1.1', 'netmask': '255.255.255.255', 'network': '1.1.1.1', 'broadcast': '1.1.1.1', 'interfaces': ['eth0']}
    ansible_facts['ipv6'] = {'address': 'fe80::5054:ff:fe70:f879', 'netmask': 'ffff:ffff:ffff:ffff::', 'network': 'fe80::', 'broadcast': '::', 'interfaces': ['eth0']}

# Generated at 2022-06-13 08:32:35.669780
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Create Play object
    p = Play()

    # Create dictionary for first play
    ds1 = dict(
        name="First play",
        hosts=['localhost', '127.0.0.1'],
        remote_user='root',
        gather_facts=False,
        roles=['role1'],
        tasks=[
            dict(name='First task', action=dict(module='shell', args='echo "First task"'))
        ],
        pre_tasks=[
            dict(name='Second task', action=dict(module='shell', args='echo "Second task"'))
        ],
        post_tasks=[
            dict(name='Third task', action=dict(module='shell', args='echo "Third task"'))
        ]
    )

    # Call preprocess_data on Play
    p.preprocess_data

# Generated at 2022-06-13 08:33:00.788725
# Unit test for method serialize of class Play
def test_Play_serialize():
    '''
    Test serialize of class Play
    '''
    m_play = Play()
    m_play.gather_facts = 'yes'
    m_play.hosts = '127.0.0.1'
    m_play.name = 'test'
    m_play.max_fail_percentage = '10'
    m_play.vars = {'id': '1'}
    m_play.vars_prompt = {'id': '2'}
    m_play.tags = ['test']
    m_play.tasks = ['127.0.0.1']
    m_play.pre_tasks = ['127.0.0.1']
    m_play.post_tasks = ['127.0.0.1']

# Generated at 2022-06-13 08:33:06.536614
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    # User is not defined in ds
    assert p.preprocess_data(ds={}) == {}

    # User is defined in ds
    assert p.preprocess_data(ds={'user': 'test'}) == {'remote_user': 'test'}

# Generated at 2022-06-13 08:33:08.440109
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # TODO: Lab 2, part 2-d
    pass


# Generated at 2022-06-13 08:33:13.011789
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Initialize a test Play object
    testPlay = ansible.playbook.play.Play()
    # Create a sequence of one task
    testPlay.tasks = [{'name': 'test task'}]
    # Create a sequence of one task
    expected_tasks = testPlay.tasks
    # Test if the method get_tasks returns the expected_tasks
    assert testPlay.get_tasks() == expected_tasks


# Generated at 2022-06-13 08:33:19.643266
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    # test if play.tasks is set properly
    play.tasks = []
    assert play.get_tasks() == []

    # test if play.tasks is set properly
    play.tasks = [2]
    assert play.get_tasks() == [2]


# Generated at 2022-06-13 08:33:29.797655
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing import vault

    pc = PlayContext()
    pc.network_os = 'junos'
    play = Play(
        name = 'test_play',
        play_hosts = 'hosts',
        play_context = pc,
        gather_facts = 'no',
        roles = [],
        tasks = [],
        handlers = []
    )
    role = Role()
    role._role_path = 'path'
    role_name = 'test_role'
    role.name = role_name
    play.roles.append(role)
    task = Task()
    task._role = role

# Generated at 2022-06-13 08:33:31.544010
# Unit test for method get_name of class Play
def test_Play_get_name():
    # TODO: Unit test for Play class. Method Play.get_name()
    assert False # TODO: implement your test here



# Generated at 2022-06-13 08:33:40.888550
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    data = '''---
- hosts: localhost
  pre_tasks:
  - debug:
      msg: "PRE"
  tasks:
  - debug:
      msg: "TASK"
  post_tasks:
  - debug:
      msg: "POST"
'''
    play = Play().load(data, variable_manager=VariableManager(), loader=DataLoader())

    assert len(play.get_tasks()) == 3

# Generated at 2022-06-13 08:33:55.115504
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
        '''
        verifies that the tasks acquired from the play are
        '''
        play_data = {
                "name": "test",
                "hosts": "localhost",
                "become": "True",
                "tasks": [{
                        "name": "Test",
                        "debug": "msg='Checking for the test file'"
                },
                {
                        "name": "Create",
                        "command": "touch /tmp/testfile"
                }]
        }
        play = Play.load(play_data)
        tasks = play.get_tasks()
        assert tasks[0].name == 'Test'
        assert tasks[1].name == 'Create'
        assert tasks[1].args['command'] == 'touch /tmp/testfile'

# Generated at 2022-06-13 08:33:56.909215
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = None
    play = Play()
    assert play.preprocess_data(ds) == None        

# Generated at 2022-06-13 08:34:15.970337
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import ansible.vars.ansible_facts
    from ansible.vars.hostvars import HostVars

    p = Play()
    r = RoleInclude()
    r.role = 'test_role'
    p.roles = [r]
    p.vars = ansible.vars.ansible_facts.AnsibleFacts(HostVars())

    # The assertion statement that we are testing
    assert p.get_tasks() == []

    # Are we testing the private method _compile_roles of class Play?
    p._compile_roles = lambda:[]

    assert p.get_tasks() == []

    # What if p.tasks is a list of blocks and/or tasks?
    b1 = Block()
    b1.block = []
    b2 = Block()


# Generated at 2022-06-13 08:34:25.888285
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    # Test 1 - Get vars_files of Play object when it is None and when it is a list
    play.vars_files = None
    assert play.get_vars_files() == []
    play.vars_files = ['testfile.yml']
    assert play.get_vars_files() == ['testfile.yml']
    # Test 2 - Get vars_files of Play object when it is not None and not a list
    play.vars_files = 'file.yml'
    assert play.get_vars_files() == ['file.yml']
test_Play_get_vars_files()

# Generated at 2022-06-13 08:34:27.779265
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    assert Play()
    assert Play().get_vars_files() == []

# Generated at 2022-06-13 08:34:31.815065
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    a = {}
    a['hosts'] = 'hosts'
    a['name'] = 'name'
    a['vars'] = 'vars'
    p = Play()
    p.vars = a['vars']
    p.name = a['name']
    p.hosts = a['hosts']
    p.block = [{'a': 'b'}]

    assert p.get_tasks() == [{'a': 'b'}]


# Generated at 2022-06-13 08:34:41.607214
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    data1 = dict(name = 'play1', hosts = 'all', connection = 'local', vars=dict(a=1, b=2), roles=dict())
    data1['roles'].append(dict(role = 'foo'))
    ds1 = dict(
        name = 'play1',
        hosts = 'all',
        connection = 'local',
        vars = dict(a=1, b=2),
        vars_prompt = dict(name=1),
        user = 'root',
        roles = [dict(role = 'foo')]
    )
    data2 = dict(name = 'play2', hosts = 'all', connection = 'local', vars=dict(a=1, b=2), tasks=[])

# Generated at 2022-06-13 08:34:55.490664
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    play.hosts = 'all'
    play.name = 'test'
    play.vars = dict(v1="v1", v2="v2")
    play.vars_files = [dict(path="path")]
    play.vars_prompt = [dict(prompt="prompt")]
    play.tags = ["tag"]
    play.roles = [dict(name="test_role")]
    play.tasks = [dict(action=dict(module="debug", name="test_task", args=dict(msg="test_msg")))]
    play.post_tasks = [dict(action=dict(module="debug", name="test_task", args=dict(msg="test_msg")))]

# Generated at 2022-06-13 08:35:06.212554
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax',
                                     'connection','module_path', 'forks', 'remote_user',
                                     'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                                     'sftp_extra_args', 'scp_extra_args', 'become', 'become_method',
                                     'become_user', 'verbosity', 'check','diff'])


# Generated at 2022-06-13 08:35:15.440485
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # TESTING ONLY
    # No need to test that all play attributes are being set correctly
    # That would require playing the entire playbook, which is outside
    # of the scope of this unit test
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    host_list = ['localhost', 'otherhost']

    inventory = InventoryManager(
        loader=loader,
        sources=host_list
    )

    variable_manager = VariableManager(
        loader=loader,
        inventory=inventory
    )


# Generated at 2022-06-13 08:35:26.815670
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    host= 'test_host'
    play= Play()
    play.hosts= [host]
    # compile_roles_handlers expects a role object in play.roles and it can be
    # created as follows
    role= Role()
    play.roles= [role]
    # call without giving a handler, so the default handler is called and the
    # tasks of the handler are returned
    import tasks
    tasks= play.compile_roles_handlers()
    for t in tasks:
        assert(t == tasks.meta_flush_handlers)

    # call giving a handler task and the tasks of the handler is returned
    handlerblock= Block()
    handlerblock.block= [tasks.copy]
    role.handlers= [handlerblock]
    tasks= play.compile_roles_handlers()


# Generated at 2022-06-13 08:35:27.473583
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert True == False

# Generated at 2022-06-13 08:35:47.523172
# Unit test for method get_name of class Play
def test_Play_get_name():
    sn = Play()
    sn._ds = {'hosts': 'test', 'name': 'test-1'}
    sn._validate_hosts = MagicMock(return_value=None)

    assert sn.get_name() == 'test-1'
    assert sn.hosts == 'test'


# Generated at 2022-06-13 08:35:55.228078
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    play._ds = {'hosts' : 'all', 'name' : 'test'}
    role = Role()
    role._name = 'test'
    role._role_path = '../module_utils'
    role._role_name = 'name'
    role._role_path = 'path'
    role._metadata = {'test' : 'test'}
    role._default_vars = {'test1' : 'test1'}
    role._default_vars_files = [{'name' : 'test1'}]
    role._vars = {'test2' : 'test2'}
    role._vars_files = [{'name' : 'test2'}]
    role._tags = {'test3' : 'test3'}
    role._tasks

# Generated at 2022-06-13 08:36:05.995987
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Setup
    data = {}
    data['name'] = "Ansible Play"
    data['hosts'] = "all"
    data['pre_tasks'] = "pre tasks"
    data['roles'] = "roles"
    data['tasks'] = "tasks"
    data['post_tasks'] = "post tasks"
    data['handlers'] = "handlers"
    data['vars_prompt'] = "vars_prompt"
    data['block'] = "block"
    data['ignore_errors'] = "ignore_errors"
    data['max_fail_percentage'] = "max_fail_percentage"
    data['serial'] = "serial"
    data['strategy'] = "strategy"
    play = Play()
    play.load_data(data)
    #

# Generated at 2022-06-13 08:36:15.321132
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

# Generated at 2022-06-13 08:36:19.315341
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Test attribute 'roles'
    # Test attribute 'included_path'
    # Test attribute 'action_groups'
    # Test attribute 'group_actions'
    pass

# Generated at 2022-06-13 08:36:26.101097
# Unit test for method get_name of class Play
def test_Play_get_name():
    print('Testing play.get_name()')
    play = Play()
    play.name = 'test'
    assert play.get_name() == play.name

# test 2: no name field
    play2 = Play()
    play2.hosts = 'test, test2'
    assert play2.get_name() == play2.hosts

if __name__ == '__main__':
    test_Play_get_name()

# Generated at 2022-06-13 08:36:31.591948
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    current_play = play
    play_ds = {}
    current_play._ds = play_ds
    test_input = {}
    expected_result = {} 
    actual_result = play.preprocess_data(test_input)

    assert  actual_result == expected_result


# Generated at 2022-06-13 08:36:37.456820
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    assert p.serialize() == {'roles': []}
    p._action_groups = {"test_group": ['task1', 'task5']}
    p._group_actions = {'task5': 'test_group'}
    # If a variable is not defined the value it has doesn't matter
    assert p.serialize() == {'roles': [], 'action_groups': {"test_group": ['task1', 'task5']},
                             'group_actions': {'task5': 'test_group'}}
    assert p.serialize() == {'roles': [], 'action_groups': {"test_group": ['task1', 'task5']},
                             'group_actions': {'task5': 'test_group'}}

# Generated at 2022-06-13 08:36:49.107239
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    m = mock.mock_open()
    with mock.patch('ansible.plugins.loader.find_plugin', return_value=m),\
            mock.patch('os.path.exists', return_value=True),\
            mock.patch('ansible.parsing.utils.load_list_of_roles', return_value=[]):
        variable_manager = VariableManager()
        loader = DataLoader()
        variable_manager.set_vault_secrets(['secret_one', 'secret_two'])
        play_source = dict(
            name="foobar",
            hosts='all',
            gather_facts='no',
            roles=[
                dict(role="first_role"),
                dict(role="second_role")
            ]
        )

# Generated at 2022-06-13 08:36:54.489153
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    ans_play = Play()

    ans_play.vars_files = ""
    assert ans_play.get_vars_files() == []

    ans_play.vars_files = "test1"
    assert ans_play.get_vars_files() == [ans_play.vars_files]

    ans_play.vars_files = ["test1", "test2"]
    assert ans_play.get_vars_files() == ans_play.vars_files


# Generated at 2022-06-13 08:37:12.187098
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()

    p.vars_files = ['/tmp/test_Play_get_vars_files/1', '/tmp/test_Play_get_vars_files/2']

    assert p.get_vars_files() == p.vars_files

# Generated at 2022-06-13 08:37:23.135536
# Unit test for method get_name of class Play
def test_Play_get_name():
    print("\n\n\nTest get_name\n")
    p = Play()
    p.name = None
    p.hosts = None
    print("Test get_name - 1: ")
    print("input:", p.name, p.hosts)
    print("output:", p.get_name())
    assert p.get_name() == ''

    p.hosts = "host1"
    p.name = None
    print("Test get_name - 2: ")
    print("input:", p.name, p.hosts)
    print("output:", p.get_name())
    assert p.get_name() == 'host1'

    p.name = "name1"
    print("Test get_name - 3: ")

# Generated at 2022-06-13 08:37:34.074429
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    block_1 = Block(parent_block=p)
    task_1 = Task()
    task_2 = Task()
    task_3 = Task()
    task_4 = Task()
    task_5 = Task()
    block_1.block.append(task_1)
    block_1.block.append(task_2)
    block_2 = Block(parent_block=p)
    block_2.block.append(task_3)
    block_2.block.append(task_4)
    block_3 = Block(parent_block=p)
    block_3.block.append(task_5)
    p.pre_tasks.append(block_1)
    p.post_tasks.append(block_2)

# Generated at 2022-06-13 08:37:38.978160
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = '/tmp/a'
    assert get_vars_files(p) == ['/tmp/a']
    p.vars_files = None
    assert get_vars_files(p) == []



# Generated at 2022-06-13 08:37:40.951706
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []

# Generated at 2022-06-13 08:37:53.259794
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Initialization
    from ansible.playbook.role.definition import RoleDefinition
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # run the code to be tested
    p = Play()
    p.vars = {}
    RoleDefinition.load = MagicMock(return_value=RoleDefinition())

# Generated at 2022-06-13 08:37:59.079212
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # In this unit test, we would like to test the method compile_roles_handlers of class Play
    # The following input arguments are prepared:
    block_list = []
    if len(self.roles) > 0:
        for r in self.roles:
            if r.from_include:
                continue
            block_list.extend(r.get_handler_blocks(play=self))

    return block_list


# Generated at 2022-06-13 08:38:04.522851
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()
    data = {'roles': [{'tasks': [{'data': {'name': 'dummy task', 'args': {}}, 'type': 'task'}, {'data': {'name': 'dummy handler', 'args': {}, 'when': 'changed'}, 'type': 'handler'}], 'meta': {'name': 'dummy role'}, 'type': 'role'}]}
    p.deserialize(data)
    print(p.serialize())


# Generated at 2022-06-13 08:38:14.771754
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible import context
    from ansible.plugins.loader import vars_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.utils.collection_loader import AnsibleCollectionRequirement
    from ansible.utils.collection_loader import AnsibleFileRequirement

    # vars_files_get_vars_files_returns_str_when_str
    # vars_files_get_vars_files_returns_str_when_str
    context_ = context
    context_._vars_plugins = vars_loader
    context_._collection_loader = None
    context_._collections_paths = []
    context_._fact_cache = {}
    context_._host_vars_plugins = vars_loader
    context_._options = None
    context_._cache_

# Generated at 2022-06-13 08:38:23.629313
# Unit test for method serialize of class Play
def test_Play_serialize():
    '''
    unit test for serialize
    '''
    p = Play()
    p.vars = {'var1': 'val1', 'var2': 'val2'}
    p.remote_user = 'test_remote_user'
    p.gather_facts = False
    p.tags = ['tag1', 'tag2']
    p.post_tasks = ['post_task1', 'post_task2', 'post_task3']
    p.roles = ['role1', 'role2']
    p.pre_tasks = ['pre_task1']
    p.tasks = ['task1', 'task2']
    p.handlers = ['handler1', 'handler2', 'handler3']
    p.hosts = ['hosts']
    p.name = 'test_name'

   

# Generated at 2022-06-13 08:38:43.380160
# Unit test for constructor of class Play

# Generated at 2022-06-13 08:38:57.128566
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.executor.process.worker import WorkerProcess
    ds = 'vagrant'
    play = Play()
    play.post_valid

# Generated at 2022-06-13 08:39:04.281964
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    _play = Play.load({
        'name': 'a play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
            {'name': 'task A', 'debug': 'msg="This is task A"'},
            {'name': 'task B', 'debug': 'msg="This is task B"'},
            {'name': 'task C', 'debug': 'msg="This is task C"'},
        ]
    })
    assert len(_play.get_tasks()) == 3

test_Play_get_tasks()



# Generated at 2022-06-13 08:39:06.249953
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    ds = 'test'
#Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:39:14.061342
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''test the method compile_roles_handlers of class Play'''
    # pylint: disable=protected-access
    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=unused-variable

    # set up test values
    play = Play()
    block = Block()
    play.roles = [block]

    # invoke the method being tested
    result = play.compile_roles_handlers()

    # verify the results
    assert result == [block]
    assert play.roles == [block]


# Generated at 2022-06-13 08:39:23.219951
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    tasks = [Task()]
    pre_tasks = [Task()]
    post_tasks = [Task()]
    play.set_loader(DictDataLoader({}))
    play._variable_manager = VariableManager()
    play.tasks = tasks
    play.pre_tasks = pre_tasks
    play.post_tasks = post_tasks
    assert play.get_tasks() == [pre_tasks[0], tasks[0], tasks[0], post_tasks[0]]

# Generated at 2022-06-13 08:39:27.930203
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    vars_files = "host_vars/hostname.yml"
    play.vars_files = vars_files
    assert play.get_vars_files() == [vars_files]

    vars_files = ["host_vars/hostname.yml", "var2.yml"]
    play.vars_files = vars_files
    assert play.get_vars_files() == vars_files


# Generated at 2022-06-13 08:39:33.566583
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    a = Play()
    assert a.get_vars_files() == []
    a.vars_files = 'a.yml'
    assert a.get_vars_files() == ['a.yml']
    a.vars_files = ['a.yml', 'b.yml']
    assert a.get_vars_files() == ['a.yml', 'b.yml']


# Generated at 2022-06-13 08:39:44.448155
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'foobar'
    assert p.get_name() == 'foobar', 'Test failed: name() should return value of assigned name'
    p.name = None
    p.hosts = 'foobar'
    assert p.get_name() == 'foobar', 'Test failed: name() should return value of hosts if name is None'
    p.name = None
    p.hosts = None
    assert p.get_name() == '', 'Test failed: name() should return empty string if both name and hosts are None'



# Generated at 2022-06-13 08:39:53.056698
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()

    # test without roles
    res = p.compile_roles_handlers()
    assert res == []

    # test with one role
    r1 = Role()
    r2 = Role()
    r1.set_handlers([
        Handler.load({'name': 'handler1', 'tags': ['test']}),
        Handler.load({'name': 'handler2', 'tags': ['test']})
    ])

    r2.set_handlers([
        Handler.load({'name': 'handler3', 'tags': ['test']}),
        Handler.load({'name': 'handler4', 'tags': ['test']})
    ])

    p.roles = [r1, r2]

    res = p.compile_roles_handlers()

# Generated at 2022-06-13 08:40:18.212564
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    # Create roles and generate handlers from those roles
    class Role(object):
        def __init__(self):
            self.ROLE_CACHE = {}
            self.role_path = None

            self._default_role_name = None
            self._metadata = None
            self._role_name = None
            self._name_set_by_user = False

            self.role_vars = {}
            self.tasks = []
            self.vars = {}
            self.default_vars = {}
            self.handlers = []
            self.meta = None
            self.library = []
            self.module_utils = []
            self.import_playbook = []
            self.block = []
            self.dependencies = []


# Generated at 2022-06-13 08:40:25.003205
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.inventory.manager import InventoryManager
    factory = AnsibleFactCollectorFactory()
    inventory = InventoryManager(loader=CLIConfigLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=CLIConfigLoader(), inventory=inventory)
    pb = Playbook.load(LOAD_PLAYBOOK, variable_manager=variable_manager, loader=CLIConfigLoader())
    play = pb.get_plays()[0]
    try:
        assert(play.compile_roles_handlers() != None)
    except: 
        print('test_Play_compile_roles_handlers Exception')
        assert(False)
    return


# Generated at 2022-06-13 08:40:38.457272
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    class PlayTest(Play):
        pass

    class BlockTest(Block):
        pass


# Generated at 2022-06-13 08:40:44.895404
# Unit test for method get_name of class Play
def test_Play_get_name():
    play1 = Play()
    assert play1.get_name() == ''
    play1.name = 'new_name'
    assert play1.get_name() == 'new_name'
    play2 = Play()
    play2.hosts = ['host1', 'host2']
    assert play2.get_name() == 'host1,host2'

# Generated at 2022-06-13 08:40:46.011820
# Unit test for method get_name of class Play
def test_Play_get_name():
    pass


# Generated at 2022-06-13 08:40:54.543252
# Unit test for constructor of class Play
def test_Play():
    # no option
    play = Play()
    assert play.get_name() == ''

    # explicit name
    play_name = 'The name of the Play'
    play = Play(name=play_name)
    assert play.get_name() == play_name

    # name from host
    play = Play(hosts='hostname')
    assert play.get_name() == 'hostname'

    # name from host list
    play = Play(hosts=['host1', 'host2'])
    assert play.get_name() == 'host1,host2'

# Generated at 2022-06-13 08:41:09.377316
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # test for single file
    play = Play()
    play.vars_files = "./dir/file.yml"
    assert play.get_vars_files() == ["./dir/file.yml"]

    play.vars_files = "./dir/file.yml"
    assert play.get_vars_files() == ["./dir/file.yml"]

    # test for list
    play = Play()
    play.vars_files = ["./dir/file1.yml", "./dir/file2.yml"]
    assert play.get_vars_files() == ["./dir/file1.yml", "./dir/file2.yml"]
