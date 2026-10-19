

# Generated at 2022-06-12 21:30:59.403557
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    from ansible.playbook.play import Play

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    from ansible.playbook.role import Role

    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host

    from ansible.inventory.group import Group

    p = Play()
    p._role_names = ['test1']
    p._start_at_task = None

    h = Host(name='testhost')
    g = Group(name='testgroup')
    g.add_host(h)
    g.vars = dict(hello='world')
    i = Inventory()
    i.add_group(g)
    i.get_vars(h)['inventory_hostname'] = h.name

    test1

# Generated at 2022-06-12 21:31:11.074681
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    PlayIterator.run_module_tasks = mock.MagicMock()
    PlayIterator.get_next_task_for_host = mock.MagicMock()
    
    mock_play = mock.MagicMock()
    mock_play.playbook = None
    mock_play._removed_hosts = None
    mock_play.handlers = None
    mock_play.tasks = None
    mock_play.strategy = None
    mock_play.hosts = None
    mock_play.name = None
    mock_play.dep_chain = None
    mock_play.tags = None
    mock_play.vars = None
    mock_play.roles = None
    mock_play.default_vars = None
    mock_play._included_file_vars = None
    mock_play.post_

# Generated at 2022-06-12 21:31:18.018683
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    Ensure that the get_failed_hosts() method of the PlayIterator returns
    the right results
    '''
    # Given a PlayIterator with an empty list of host states
    play_iterator = PlayIterator()
    play_iterator._host_states = {}

    # When I call get_failed_hosts
    result = play_iterator.get_failed_hosts()

    # Then I should get back an empty dictionary
    assert result == {}, result


# Generated at 2022-06-12 21:31:27.532853
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
  from ansible.playbook.block import Block
  from ansible.playbook.task import Task

  play = MagicMock()
  play.get_roles.return_value = []

  pi = PlayIterator(play)

  # create a simple task list
  task1 = Task()
  task2 = Task()
  task3 = Task()
  task_list = [task1, task2, task3]

  # add a block with 3 tasks
  block = Block()
  block.block = task_list
  pi._play.get_blocks.return_value = [block]

  # create a host and get its state
  host = MagicMock()
  state = pi.get_host_state(host)

  # add tasks to the state
  expected_task_list = [Task(), Task(), Task()]
  state

# Generated at 2022-06-12 21:31:40.139925
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    host = Host("localhost")
    pb = Playbook()
    play_ds = pb._entries[0]
    itr = PlayIterator(play_ds, pb)
    state = HostState(itr._play, host)
    itr._host_states[host.name] = state
    state.run_state = PlayIterator.ITERATING_RESCUE
    assert itr.get_active_state(state) == state
    state.rescue_child_state = HostState(itr._play, host)
    state.rescue_child_state.run_state = PlayIterator.ITERATING_ALWAYS
    assert itr.get_active_state(state) == state.rescue_child_state

# Generated at 2022-06-12 21:31:44.650838
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    # instantiate an iterator
    play = Play.load('myplay', dict(playbook=dict(hosts=[], roles=[]),
                                    hosts=['all'], vars={}, connection='local'), loader=None)
    play._variable_manager = VariableManager()
    iterator = PlayIterator(play)

    # set the host state to the iterator
    host = Host('myhost')
    iterator._host_states[host.name] = HostState(blocks=[dict(block=['one', 'two'])])

    # get the host state
    state = iterator.get_host_state(host)

    # verify the state was returned correctly
    assert state._blocks[0].block == ['one', 'two']



# Generated at 2022-06-12 21:31:53.140313
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    hs = dict(
        _host_states=dict(host1=dict(    # Host state for host1 with no child state
            fail_state=0,
            run_state=1,
            tasks_child_state=None,
        )),
    )
    pi=dict2obj(hs)
    state = pi.get_host_state('host1')
    result = pi.get_active_state(state)
    assert result == state, result
    # Test with a child state

# Generated at 2022-06-12 21:32:01.886231
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    # setup
    play = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='foo', args=dict(one=1))),
            dict(action=dict(module='bar', args=dict(one=1))),
            dict(action=dict(module='baz', args=dict(one=1))),
            dict(action=dict(module='qux', args=dict(one=1))),
            dict(action=dict(module='quz', args=dict(one=1))),
        ]
    ), loader=DummyLoader())

    inventory = Inventory(loader=DummyLoader())

# Generated at 2022-06-12 21:32:07.294862
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play().load(dict(
        name = "Always Test",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    ), loader=play_ds)

    play.post_validate()

    iterator = PlayIterator(play)

    assert len(iterator._play._tasks) == 2

    inventory = Inventory(loader=yaml_inventory_ds, host_list=['localhost', 'otherhost'])
    inventory.set_variable('foo', 'bar')
    host = inventory.get_host('localhost')

# Generated at 2022-06-12 21:32:08.913247
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
	play_iterator= PlayIterator()
	play_iterator.__init__()

# Generated at 2022-06-12 21:32:39.402950
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    '''test the get_original_task function'''

    run_simple_task_tests(PlayIterator, '_insert_tasks_into_state')



# Generated at 2022-06-12 21:32:47.464321
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    host = Host('testhost')
    host.name = 'testhost'
    host.vars['ansible_user'] = 'me'
    host.vars['ansible_host'] = '127.0.0.1'
    host.vars['ansible_port'] = '1234'
    host.vars['ansible_connection'] = 'smart'

# Generated at 2022-06-12 21:32:48.111129
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
  pass

# Generated at 2022-06-12 21:32:56.932981
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    # Test that when we pass a host to mark_host_failed, the host
    # is marked failed ( state.failed == True )

    # Setup
    test_host = Host(name='test_host', port=0)
    test_play = Play()
    test_iterator = PlayIterator(play=test_play)
    test_task = Task()
    test_play._tasks.append(test_task)
    test_block = Block(parent_block=test_play)
    test_play._blocks.append(test_block)
    test_iterator.get_next_task_for_host(test_host)

    # Test
    test_iterator.mark_host_failed(test_host)

    # Verify
    assert test_iterator.is_failed(test_host)



# Generated at 2022-06-12 21:33:08.278169
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    arg0 = get_fixture('play')
    arg1 = get_fixture('play')
    arg2 = get_fixture('play')
    arg3 = get_fixture('play')

    # testing with required args
    # set up args
    args = dict()
    args.update({"play" : arg0})
    args.update({"play" : arg1})
    args.update({"play" : arg2})
    args.update({"play" : arg3})

    get_host_state_args_0 = { 
        'host_name': None,
        'play': None,
    }
    get_host_state_args_0.update(args)
    p = PlayIterator(**get_host_state_args_0)
    return p.get_host_state() # ??


# Generated at 2022-06-12 21:33:16.029331
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    '''
    PlayIterator.is_any_block_rescuing
    '''
    play = Play()
    play.hosts = 'testhost'
    play.name = 'test play'
    play.connection = 'local'
    play.tasks = [
        dict(action=dict(module='shell', args='whoami'))
    ]
    play.handlers = []

    # 1. set up a test PlayIterator
    pi = PlayIterator(play)
    pi._play_name = 'test play'
    pi._play = play
    host_state = HostState(blocks=[play.compile()])
    state = State()
    state._host_states = dict()
    state._host_states['testhost'] = host_state
    state._host_states['testhost']._play = play

   

# Generated at 2022-06-12 21:33:27.359037
# Unit test for constructor of class PlayIterator

# Generated at 2022-06-12 21:33:36.534352
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    p = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        roles = [ 'webserver' ],
        tasks = [
            dict(action=dict(module='shell', args='echo hi'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='hello from the other side')))
        ]
    ))

    hosts = [
        Host(name="server0"),
        Host(name="server1"),
        Host(name="server2")
    ]

    pi = PlayIterator(inventory=Inventory(hosts=hosts), play=p)
    results = list(pi)
    assert(len(results) == len(hosts))
    for result in results:
        assert(hasattr(result, 'task_name'))

# Generated at 2022-06-12 21:33:38.639704
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    '''
    Unit test for method get_host_state of class PlayIterator
    '''
    pass # nothing to test here

# Generated at 2022-06-12 21:33:51.671683
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    play = Play()
    play.playbook = Playbook()
    play.playbook.loader = DataLoader()
    play.playbook.inventory = Inventory("")
    play.playbook.inventory.set_variable("hostvars", {})
    play.hosts = 'localhost'
    play.name = 'TEST'
    play.tasks = [Task() for i in range(1)]
    play.tasks[0].blocks = []
    play.tasks[0].action = "shell"
    play.tasks[0].args = "echo hello"
    play.tasks[0].block = None
    play.tasks[0].rescue = None
    play.tasks[0].always = None
    play.tasks[0].when = None
    play.tasks[0].register = None
   

# Generated at 2022-06-12 21:34:24.274637
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    test_iterator = PlayIterator()
    test_iterator._set_play(Play().load({'name': 'test play', 'hosts': 'all'}, variable_manager=VariableManager(), loader=DummyLoader()))

    my_host = Host(name='test_host')
    test_iterator._play._hosts_cache[my_host.name] = my_host
    test_iterator._play._hosts_cache[my_host.name]._play = test_iterator._play

# Generated at 2022-06-12 21:34:29.181035
# Unit test for method get_original_task of class PlayIterator

# Generated at 2022-06-12 21:34:29.828394
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    iterator = PlayIt

# Generated at 2022-06-12 21:34:33.569415
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    runner = PlayIterator(play=None)
    result = runner._get_failed_hosts()
    assert result is False


# Generated at 2022-06-12 21:34:39.654596
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play().load(dict(
        name = "foobar",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    ), variable_manager=VariableManager(), loader=BaseLoader())

    iterator = PlayIterator()
    iterator.load_play(play)

    host = Host(name="testhost")
    iterator.add_host(host)

    # first task is just a shell
    state, task = iterator.get_next_task_for_host(host, peek=False)
    assert task.action == 'shell'
    assert state.cur_regular

# Generated at 2022-06-12 21:34:49.812439
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    '''
    This tests that the PlayIterator.get_active_state method finds the correct
    active state when there are nested states.
    '''

    p = Play()
    i = PlayIterator(p)
    i._host_states = dict()

    state = HostState(p.get_blocks()[0])
    assert i.get_active_state(state) is state

    state.run_state = i.ITERATING_TASKS
    state.tasks_child_state = HostState(p.get_blocks()[0])
    assert i.get_active_state(state) is state.tasks_child_state

    state = HostState(p.get_blocks()[0])
    state.run_state = i.ITERATING_TASKS
    state.tasks_child_state = HostState

# Generated at 2022-06-12 21:34:59.417288
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''
    For method cache_block_tasks.
    '''

    # this is a test of the code only, so we use the 'automatic' protocol inside the test
    import ansible.inventory.host
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    class Host(ansible.inventory.host.Host):
        def __init__(self, name):
            self.name = name

    class Play(object):
        def __init__(self):
            self.host_list = [Host("localhost")]
            self.remote_user = "foo"
            self.connection = "smart"
            self.callbacks = []
            self._tqm = None

        def basedir(self):
            return "/tmp"

    class Options(object):
        pass

   

# Generated at 2022-06-12 21:35:07.429109
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    import datetime
    # Initialize a test PlayIterator with empty data structure.
    play_iterator = PlayIterator()
    # Check the number of hosts in the play iterator.
    assert 0 == play_iterator.n_hosts()
    #
    # Create a test host, with ``name`` and ``port`` as attributes.
    host = Host()
    host_name = "test-host-name"
    host.name = host_name
    host_port = 5555
    host.port = host_port
    #
    # Store the host in the play iterator.
    play_iterator.add_host(host)
    # Check the stored host's attributes.
    assert 1 == play_iterator.n_hosts()
    assert host_name == play_iterator.hosts()[0].name
    assert host_port == play_iterator

# Generated at 2022-06-12 21:35:08.120572
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    pass

# Generated at 2022-06-12 21:35:13.201521
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():

    test_PlayIterator = PlayIterator(play=None, inventory=None, variable_manager=None, loader=None, display=None, options=None, passwords=None, run_handlers=None, run_tasks=None, fail_on_undefined_tasks=None)

    host = object()
    result = test_PlayIterator.get_host_state(host)
    assert result is not None


# Generated at 2022-06-12 21:36:03.507359
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    pass

# Generated at 2022-06-12 21:36:13.905709
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    host = MagicMock()
    host.name = 'localhost'
    play = MagicMock()
    play.get_active_hosts.return_value = [host]
    play._play_context = PlayContext()
    play._play_context.retries = [1, 2, 3]
    play.get_variable_manager.return_value = MagicMock()
    play.get_variable_manager().get_vars.return_value = {}
    play.get_variable_manager().get_vars.return_value = {}
    play.get_variable_manager().get_vars.return_value = {}
    play.serialized_data = {'block': {}}
    play.serialized_data['block'][host.name] = []
    play.serialized_data['block'][host.name].append

# Generated at 2022-06-12 21:36:17.793717
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    target = PlayIterator(play=None, inventory=None, variable_manager=None)

    arg1 = None
    arg2 = None
    arg3 = None
    arg4 = None

    # This test needs to be completed
    assert False, "Test not implemented"



# Generated at 2022-06-12 21:36:23.333797
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    host = Host("testhost")
    state = HostState()
    task = Task("testtask")
    iterator = PlayIterator(play=Play("testplay", [Host("testhost")]))
    iterator._host_states[host.name] = state
    assert iterator.add_tasks(host=host, task_list=[task]) == iterator

# Generated at 2022-06-12 21:36:34.592934
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    PlayIterator._create = lambda data, play, play_context, loader, templar, shared_loader_obj: FakePlayIterator(data, play, play_context, loader, templar, shared_loader_obj)
    data = {'hosts':['localhost'], 'gather_facts': 'no', 'tasks':[{'name': 'debug1'}, {'name': 'debug2'}],
            'rescue': [{'name': 'debug3'}], 'always': [{'name': 'debug4'}]}
    play_source = dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [dict(action=dict(module='debug', args=dict(msg='{{foo}}')))]
    )

# Generated at 2022-06-12 21:36:42.084780
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    host = Host(name='foo')

    def test(name, state_dict, expected):
        state = HostState(state_dict)
        iterator = PlayIterator()
        res = iterator.is_failed(host)

# Generated at 2022-06-12 21:36:48.235513
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    from ansible import constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager

    t1 = Task()
    t1.action = 'debug'
    t1.args = 'var=foo'

    ti1 = TaskInclude()
    ti1.task = t1
    ti1.static = 1

# Generated at 2022-06-12 21:36:55.876263
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    play = Play()
    play.hosts = ['host1']
    play.name = 'something'
    play.tasks = [dict(action='setup')]
    play.vars_prompt = dict()

    # gather_facts was not set, this is normal behaviour
    result = PlayIterator(play)
    assert result._play.gather_facts == 'smart'

    # gather_facts was set to smart
    result = PlayIterator(play, gather_facts='smart')
    assert result._play.gather_facts == 'smart'

    # gather_facts was set to explicit False
    result = PlayIterator(play, gather_facts=False)
    assert result._play.gather_facts == False

# Generated at 2022-06-12 21:36:57.578177
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    '''
    PlayIterator.is_any_block_rescuing() Test method
    '''
    pass

# Generated at 2022-06-12 21:37:07.806894
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    '''
    Unit test for method get_host_state of class PlayIterator
    '''
    # No inventory was specified, this could be any host
    host = Mock()

    #
    # The new_state argument is optional, the default is False
    #

    # Initialize a state object
    state = HostState(blocks=[
        Block(
            role=Role(name='role1'),
            block=[]
        ),
        Block(
            role=Role(name='role2'),
            block=[]
        )
    ])

    # Initialize a PlayIterator object
    play_iterator = PlayIterator(play=Mock(), inventory=Mock())

    # The host state is not initialized
    play_iterator._host_states = dict()
    assert play_iterator.get_host_state(host=host) is None

    #

# Generated at 2022-06-12 21:38:51.610638
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # ensure that we're dealing with an iterator
    myIterator = PlayIterator
    result = myIterator.get_failed_hosts(myIterator)
    assert result == None


# Generated at 2022-06-12 21:38:53.764081
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    test_iterator = PlayIterator()
    assert test_iterator.get_next_task_for_host(None) == (None, None)



# Generated at 2022-06-12 21:38:55.810663
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    a = PlayIterator()
    b = a.get_original_task()
    print(b)
    assert b == (None, None)

# Generated at 2022-06-12 21:39:05.020854
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
  play = Play()
  ti = TaskIterator(play)
  hs = HostState(None)
  hs.run_state = PlayIterator.ITERATING_TASKS
  assert ti.is_any_block_rescuing(hs) == False
  hs.run_state = PlayIterator.ITERATING_RESCUE
  assert ti.is_any_block_rescuing(hs) == True
  hs.tasks_child_state = HostState(None)
  hs.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
  assert ti.is_any_block_rescuing(hs) == True


# Generated at 2022-06-12 21:39:14.364939
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    from ansible.playbook import Play
    from ansible.task import Task
    from ansible.inventory.host import Host

    inventory = Mock(spec=InventoryManager)
    play = Play.load(dict(
        name = "test play",
        hosts = 'all',
        tasks = [
            dict(action=dict(module='shell', args='ls'))
        ]
    ), variable_manager=variable_manager, loader=loader)

    iterator = PlayIterator(inventory, play, loader=loader, variable_manager=variable_manager)

    host = Host("test_host")
    task = Task.load(dict(action=dict(module="shell", args="ls")))
    new_task = Task.load(dict(action=dict(module="shell", args="ls")))

    # add tasks to an empty state
    state

# Generated at 2022-06-12 21:39:21.077862
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    name = 'name'
    variable_manager = 'variable_manager'
    loader = 'loader'
    variable_manager = 'variable_manager'
    passwords = 'passwords'
    play = Play().load(dict(
        name = name,
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Message in block 1'))),
            dict(action=dict(module='debug', args=dict(msg='Message in block 2')))
        ]
    ), variable_manager=variable_manager, loader=loader)

    iterator = PlayIterator()
    iterator.load_play(play)
    iterator.next_task_for_host(Host('A'))

    state = iterator._host_states[Host('A').name]
   

# Generated at 2022-06-12 21:39:30.996960
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    pi = PlayIterator()

    hs = HostState(blocks=[])
    # start in tasks section
    hs.run_state = PlayIterator.ITERATING_TASKS
    hs.tasks_child_state = HostState(blocks=[])
    hs.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
    hs.tasks_child_state.tasks_child_state = HostState(blocks=[])
    hs.tasks_child_state.tasks_child_state.run_state = PlayIterator.ITERATING_RESCUE
    assert pi.is_any_block_rescuing(hs) == True
    hs.tasks_child_state.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
   

# Generated at 2022-06-12 21:39:42.436834
# Unit test for method get_next_task_for_host of class PlayIterator

# Generated at 2022-06-12 21:39:47.108822
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    Basic test to verify the PlayIterator.is_failed method returns False when called on a new PlayIterator
    instance.
    '''
    mock_play = Mock(Play)
    mock_play._iterator = PlayIterator(play=mock_play)
    mock_play._iterator.get_host_state = Mock(return_value=None)
    mock_play._iterator._check_failed_state = Mock(return_value=False)

    assert mock_play._iterator.is_failed('hostname') == False
    mock_play._iterator.get_host_state.assert_called_with('hostname')
    assert mock_play._iterator._check_failed_state.called == False

    mock_play.reset_mock()
    # Test that PlayIterator._check_failed_state is called correctly
    mock_play._iterator

# Generated at 2022-06-12 21:39:53.637497
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    host = Sentinal()
    host.name = 'testhost'
    pi = PlayIterator()
    pi.get_host_state(host)
    assert pi._host_states[host.name].fail_state == pi.FAILED_NONE
    assert pi._host_states[host.name].run_state == pi.ITERATING_SETUP
    assert pi._check_failed_state(pi._host_states[host.name]) == False
    pi.mark_host_failed(host)
    assert pi._host_states[host.name].fail_state == pi.FAILED_SETUP
    assert pi._host_states[host.name].run_state == pi.ITERATING_COMPLETE
    assert pi._removed_hosts == ['testhost']