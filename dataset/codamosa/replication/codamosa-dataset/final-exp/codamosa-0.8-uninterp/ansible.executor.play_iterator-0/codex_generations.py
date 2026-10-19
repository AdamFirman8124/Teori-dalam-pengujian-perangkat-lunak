

# Generated at 2022-06-12 21:31:04.436469
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # Setup test data
    inventory = Inventory(host_list=[])
    host_name = 'host_name'
    host = Host(host_name)
    task = Task()
    task_list = ['task_list']
    # Setup mocks
    # Instantiate a mock class using the function _monkey_patch_object()
    # and assigning it a name 'MockPlay'
    MockPlay = _monkey_patch_object(Play, 'MockPlay')
    # Instantiate a mock class using the function _monkey_patch_object()
    # and assigning it a name 'MockTask'
    MockTask = _monkey_patch_object(Task, 'MockTask')
    # Instantiate a mock class using the function _monkey_patch_object()
    # and assigning it a name 'MockInstance'
    MockInstance = _monkey_

# Generated at 2022-06-12 21:31:14.120467
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    def _get_play():
        """Returns an example play"""
        loader = DataLoader()
        play = Play.load(loader=loader, playbooks=[], variable_manager=None, loader_cache=None)
        play.load()
        return play

    def _get_role_task():

        play = _get_play()
        role = play.roles_using_role('role_1')[0]
        return play.get_role_tasks(role)

    play = _get_play()
    loader = DataLoader()
    host = 'localhost'
    host_state = HostState(blocks=[])
    original_task = _get_role_task()[1]

# Generated at 2022-06-12 21:31:24.841218
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    def _create_fake_play():
        FakePlay = namedtuple('FakePlay', [
                    'host_list', 'get_variable_manager', 'get_loader'
                ])
        FakeHostList = namedtuple('FakeHostList', ['get_hosts'])
        FakeHost = namedtuple('FakeHost', ['name'])
        FakeHostList.get_hosts = lambda x: [FakeHost('host1'), FakeHost('host2')]
        FakePlay.get_variable_manager = lambda x: 'fake_variable_manager'
        FakePlay.get_loader = lambda x: 'fake_loader'
        FakePlay.host_list = FakeHostList
        return FakePlay()

    FakePlayContext = namedtuple('FakePlayContext', ['defs'])

# Generated at 2022-06-12 21:31:37.927677
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    host = Host('testhost1')

    # Test to ensure that the active state of a HostState with blocks is the HostState of the currently active block instead
    state = HostState(blocks=[
        Block(
            name='first block',
            task_list=[
                Task(),
                Task(),
                Task(),
            ],
        ),
        Block(
            name='second block',
            task_list=[
                Task(),
            ],
        ),
    ])
    state.cur_block = 0
    state.cur_task = 2
    assert PlayIterator.get_active_state(state) == state
    state.cur_task = 3
    assert PlayIterator.get_active_state(state) == state.tasks_child_state

    # Test to ensure that the active state of a HostState with blocks that are in rescue mode is the Host

# Generated at 2022-06-12 21:31:47.170145
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    mock_play = MagicMock()
    mock_play.serialize = False
    mock_play.post_validate.return_value = Mock()
    mock_play.handlers = []
    mock_play.hosts = 'all'
    mock_play.name = 'play'
    mock_play._variable_manager = Mock()
    mock_play.connection_user = Mock()
    mock_play.connection_password = Mock()
    mock_play.connection_port = Mock()
    mock_play.become_user = Mock()
    mock_play.become = False
    mock_play.no_log = False
    mock_play.check = False
    mock_play.tags = ['all']
    mock_play.roles = ['all']
    mock_play.dep_chain = Mock()

    mock_

# Generated at 2022-06-12 21:31:49.510771
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    unit test for method mark_host_failed of class: PlayIterator
    '''
    # FIXME: write unit test
    pass

# Generated at 2022-06-12 21:32:00.156058
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    """
    Tests for the class PlayIterator
    """

    p = Play().load(FIXTURE_PLAYBOOK, variable_manager=VariableManager(), loader=loader)
    queue = PlayIterator(p, None)
    queue._host_states = dict(foo=HostState(blocks=[]))
    queue._host_states["foo"].run_state = queue.ITERATING_ALWAYS
    queue._host_states["foo"].always_child_state = HostState(blocks=[])
    queue._host_states["foo"].always_child_state.run_state = queue.ITERATING_TASKS
    queue._host_states["foo"].always_child_state.tasks_child_state = HostState(blocks=[])

# Generated at 2022-06-12 21:32:04.756945
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play = Play()
    play.hosts = ['localhost', '127.0.0.1']
    pb = Playbook()
    pb.plays.append(play)
    pi = PlayIterator()
    pi._play = play

    def _check_rescuing(state, result):
        assert result == pi.is_any_block_rescuing(state), "expecting %s got %s" % (result, pi.is_any_block_rescuing(state))

    # test the case where there are no blocks, and state it not rescuing
    state = HostState()
    _check_rescuing(state, False)
    # test the case where there are no blocks, and state is rescuing
    state.run_state = pi.ITERATING_RESCUE

# Generated at 2022-06-12 21:32:16.976594
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():

    PlayIterator = ansible.playbook.PlayIterator
    Host = ansible.inventory.host.Host
    host = Host('local', 'test')
    host_state = PlayIterator._get_host_state(host, [])
    assert host_state is not None
    assert len(host_state._blocks) == 1
    assert host_state.run_state == PlayIterator.ITERATING_SETUP
    assert host_state.cur_block == 0
    assert host_state.cur_regular_task == 0
    assert host_state.cur_rescue_task == 0
    assert host_state.cur_always_task == 0
    assert host_state.fail_state == PlayIterator.FAILED_NONE
    assert host_state.did_rescue == False

    # create a fake Block that we can test with

# Generated at 2022-06-12 21:32:25.729355
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    # Initialize a play object
    play = Play()
    # Initialize a playbook object
    playbook = Playbook()
    # Initialize the PlayIterator
    play_iterator = PlayIterator(play, playbook._tqm, playbook)
    # Create a host state
    state1 = HostState(blocks=[])
    # Initialize a task object
    task = Task()
    # Create a task list
    task_list = [task]
    # Create a host object
    host = Host(name="localhost")
    # Add a task to the play iterator
    play_iterator.add_tasks(host, task_list)




# Generated at 2022-06-12 21:33:02.663139
# Unit test for method is_any_block_rescuing of class PlayIterator

# Generated at 2022-06-12 21:33:11.335430
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    p = Play()
    s = HostState(blocks=[Sibling()])
    b1 = Block()
    b2 = Block()
    b2.rescue = [Sibling()]
    b1.block = [Sibling(), b2]
    s._blocks = [b1]
    pi = PlayIterator()
    pb = Playbook()
    pb.set_vars(dict(pi=pi, p=p, host=FakeHost(), s=s))
    pb.load_playbook(os.path.join(os.path.dirname(__file__), 'playbook-debug.yml'))
    test_pb = pb.get_plays('test')[0]
    test_pb.host_vars_files = []

    # Test the state where we are in a rescue block.
    s

# Generated at 2022-06-12 21:33:22.979541
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    PLAY = Play().load(get_fixture_path('simple_play.yml'), variable_manager=variable_manager, loader=loader)

    play = PLAY()
    play.post_validate()
    play.theather_on()

    itr = PlayIterator(play=play)
    with pytest.raises(AnsibleError) as exc:
        itr.add_tasks(play.hosts[0], [])
    assert exc.value.message == 'Tried to add tasks to a host with no current task'
    itr.next_task_for_host(play.hosts[0])
    assert itr.add_tasks(play.hosts[0], []) == 0
    host_states = itr._host_states[play.hosts[0].name]

# Generated at 2022-06-12 21:33:24.379959
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    pass


# Generated at 2022-06-12 21:33:34.299056
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    # This is a private method so we need to make the class visible
    class PlayIterator(_PlayIterator):
        pass
    # Generate a fake Play object
    play = Play.load(dict(
        name = "fake_play",
        hosts = "all",
        gather_facts = "no",
        tasks = dict(
            task1 = dict(action=dict(module="shell", args="echo hello world")),
            task2 = dict(action=dict(module="shell", args="echo goodbye world")),
        ),
    ), loader=DictDataLoader())
    # Generate a fake TaskResult object
    task_result = TaskResult("fake_task", host="fake_host", task=play.get_tasks()[0], task_fields=play.get_task_fields())
    # The method we are testing is the only public

# Generated at 2022-06-12 21:33:45.428309
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    iterator = PlayIterator()
    assert iterator, "Failed to create PlayIterator object"

    iterator._host_states = dict([("host1", HostState()), ("host2", HostState())])
    iterator._host_states["host1"].fail_state = PlayIterator.FAILED_TASKS
    iterator._host_states["host2"].fail_state = PlayIterator.FAILED_RESCUE

    failed_hosts = iterator.get_failed_hosts()

    assert len(failed_hosts) == 2, "Failed hosts is not of expected length"
    assert failed_hosts["host1"], "Host 1 is missing"
    assert failed_hosts["host2"], "Host 2 is missing"


# Generated at 2022-06-12 21:33:47.479007
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    # FIXME: write a unit test
    pass


# Generated at 2022-06-12 21:33:57.272987
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    host_list = C.HOST_LIST # list of strings
    inventory = Inventory(host_list)
    play = Play().load(dict(
        name = "test play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='shell', args='ls', register='shell_out')),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), variable_manager=inventory.get_variable_manager(), loader=C.DEFAULT_LOADER)
    tqm = None
    # (defensive deep copy of blocks)
    play.copy()

# Generated at 2022-06-12 21:34:07.944450
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    from ansible.playbook.block import Block

    b1 = Block()
    b1.block = [ 't1', 't2' ]
    b1.rescue = [ 'r1' ]
    b1.always = [ 'a1' ]

    play = Play()
    play.hosts = 'hosts'

    pi = PlayIterator(play)

    host = Host('host')
    host.name = 'host'

    state = HostState(play)
    state._host = host
    state._blocks = [ b1 ]
    state.cur_block = 0
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state.run_state = PlayIterator.ITERATING_TASKS

    pi._host_states

# Generated at 2022-06-12 21:34:17.462487
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    '''
    Unit test for method PlayIterator.add_tasks of class PlayIterator
    '''
    # Set up test environment
    host = Host('localhost')
    play = Play()
    block = Block()
    iterator = PlayIterator(play)
    display.verbosity = 3
    display.debug = True

    # Set some initial values for the iterator object
    iterator._tqm = TaskQueueManager()
    iterator._tqm.add_host(host)
    iterator._inventory = Inventory()
    iterator._last_activity_at = 0
    iterator._last_task = None
    iterator._last_task_ok = False
    iterator._failed_hosts = {}
    iterator._processed_hosts = {}
    iterator._play = play
    iterator._play._batched_hosts = []
    iterator._play._iterator

# Generated at 2022-06-12 21:34:52.591083
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # Create a play (to serve as parent of blocks)
    p = Play().load(dict(
        name = 'placeholder',
        hosts = 'none',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='placeholder', args=dict(x=1)), register='test'),
        ]
    ), loader=DictDataLoader())

    # Create play iterator
    i = PlayIterator(p, None, None)
    # Create a block (to serve as child of play)
    b1 = Block().load(dict(
        block = [
            dict(action=dict(module='placeholder', args=dict(x=2)), register='test'),
        ],
    ), play=p, loader=DictDataLoader())
    # Add block to play
    p._add_block(b1)

# Generated at 2022-06-12 21:35:01.614461
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
  play = Play()
  play.name = 'test'
  play.hosts = ['localhost']
  play.tasks = [
    Block(
      name="first block",
      tasks=
        [ Block(
            name="first subblock",
            rescue=[ Task() ],
            tasks=[ Task() ]
          ),
        ]
    ),
    Block(
      name="second block",
      tasks=
        [ Block(
            name="second subblock",
            rescue=[ Task() ],
            tasks=[ Task() ]
          ),
        ]
    ),
    Block(
      name="third block",
      tasks=
        [ Block(
            name="third subblock",
            rescue=[ Task() ],
            tasks=[ Task() ]
          ),
        ]
    ),
  ]

  i = PlayIterator(play, 1)

# Generated at 2022-06-12 21:35:09.429427
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    import ansible.playbook
    import ansible.executor.task_queue_manager
    import ansible.inventory.host
    import ansible.executor.process.worker
    import ansible.utils.shlex
    import ansible.vars.hostvars

    """
    ansible.playbook.Play
    |__ ansible.playbook.PlayIterator
      |__ ansible.playbook.TaskInclude
        |__ ansible.playbook.Block
        |__ ansible.playbook.Block
      |__ ansible.playbook.TaskInclude
        |__ ansible.playbook.Block
        |__ ansible.playbook.Block
    """


# Generated at 2022-06-12 21:35:13.237192
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    parser = PlayParser(loader=None)
    play = parser.parse('test/playbooks/play_iterator.yml')
    iterator = PlayIterator(play)
    assert iterator.itervalues()
    assert iterator.itersets()
    assert iterator.itervalues()
    assert not iterator.itersets()
    assert not iterator.itervalues()
    assert not iterator.itersets()
    assert iterator._play._iterator is iterator

# Generated at 2022-06-12 21:35:24.366474
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    '''
    This tests the PlayIterator.get_next_task_for_host() method, which is responsible for
    providing the next task object from the play to the worker, based on the current play
    and host state.
    '''

    # Generate a host inventory
    hosts = [
        Host(name="host1"),
        Host(name="host2")
    ]
    inventory = Inventory(hosts)

    # Generate a simple task list

# Generated at 2022-06-12 21:35:25.801925
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # TODO: Test for PlayIterator.get_active_state
    raise NotImplementedError

# Generated at 2022-06-12 21:35:31.263138
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    play = Play()
    p = PlayIterator(play)
    p.run_state = PlayIterator.ITERATING_TASKS
    p.cur_regular_task = 0
    p.cur_rescue_task = 0
    p.cur_always_task = 0
    p._blocks = [Block()]
    p.tasks_child_state = None
    p.rescue_child_state = None
    p.always_child_state = None
    task = Task()
    task.action = 'test'
    state = HostState(blocks=[Block(block=[task])])
    p.add_tasks(2, [Task()])

# Generated at 2022-06-12 21:35:43.375605
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    # Test that an actual failure is correctly detected
    state = HostState(blocks=[Block(block=[dict(action='fail')])])
    state.run_state = PlayIterator.ITERATING_TASKS
    assert PlayIterator._check_failed_state(state)

    # Test that a failed rescue is correctly detected
    state = HostState(blocks=[Block(block=[dict(action='fail')], rescue=[dict(action='fail')])])
    state.run_state = PlayIterator.ITERATING_RESCUE
    state.cur_rescue_task = 0
    assert PlayIterator._check_failed_state(state)

    # Test that failed rescue with successful rescue is correctly detected
    state = HostState(blocks=[Block(block=[dict(action='fail')], rescue=[dict(action='fail')])])

# Generated at 2022-06-12 21:35:53.643408
# Unit test for method copy of class HostState
def test_HostState_copy():
    from ansible.playbook.block import Block
    b1 = Block()
    b1.tasks = [Task() for _ in range(4)]
    b2 = Block()
    b2.tasks = [Task() for _ in range(4)]
    b3 = Block()
    b3.tasks = [Task() for _ in range(4)]

    hs = HostState(blocks=[_ for _ in (b1, b2, b3)])
    hs.cur_block = 1
    hs.cur_regular_task = 2
    hs.cur_rescue_task = 1
    hs.cur_always_task = 3
    hs.run_state = PlayIterator.ITERATING_TASKS
    hs.fail_state = PlayIterator.FAILED_TASKS
    h

# Generated at 2022-06-12 21:36:05.348733
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    import lib.ansible.playbook.block as block
    import lib.ansible.playbook.task as task

    t1 = task.Task()
    t1.set_loader(DictDataLoader({}))
    t1.action = 'test1'
    t2 = task.Task()
    t2.set_loader(DictDataLoader({}))
    t2.action = 'test2'
    t3 = task.Task()
    t3.set_loader(DictDataLoader({}))
    t3.action = 'test3'

    b1 = block.Block()
    b1.block  = [t1, t2]
    b1.rescue = [t3]

    s = PlayIterator.HostState(blocks=[b1])
    s.run_state = PlayIterator.ITER

# Generated at 2022-06-12 21:37:18.894453
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    play = Play()
    play.vars = {}
    ti = PlayIterator(play)
    block = Block()
    result = ti._cache_block_tasks(block, play, play.vars)
    assert result == ([], {})


# Generated at 2022-06-12 21:37:29.198081
# Unit test for method copy of class HostState
def test_HostState_copy():
    # empty block list
    blocks = [ ]
    original_state = HostState(blocks)
    original_state.cur_block = 0
    original_state.cur_regular_task = 1
    original_state.cur_rescue_task = 2
    original_state.cur_always_task = 3
    original_state.run_state = 4
    original_state.fail_state = 1
    original_state.pending_setup = True
    original_state.did_rescue = True
    original_state.did_start_at_task = True
    original_state.tasks_child_state = HostState(blocks)
    original_state.rescue_child_state = HostState(blocks)
    original_state.always_child_state = HostState(blocks)

    copy_state = original_state.copy()

# Generated at 2022-06-12 21:37:36.709795
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    # since it's just a pass through to another function, just test with a stub function and assert it gets called
    test_block = MagicMock()
    test_block.name = 'block mock'
    test_host = MagicMock()
    test_host.vars = {}
    test_host.get_vars.return_value = test_host.vars
    pi = PlayIterator(play=MagicMock())
    pi.cache_block_tasks(host=test_host, block=test_block)

    test_host.get_vars.assert_called_once_with(
        play=pi._play, task=None, host=test_host, role=None, use_cache=True,
        variables=pi._play._variable_manager._fact_cache[test_host.name]
        )
    test_

# Generated at 2022-06-12 21:37:46.576110
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    host = Host(name="host1")
    host2 = Host(name="host2")
    host3 = Host(name="host3")
    play = Play().load({
        'name' : 'test play',
        'hosts': 'host1',
        'gather_facts': 'no',
        'tasks': [
            {'action': {'module': 'debug', 'args': {'msg': 'success'}}},
            {'action': {'module': 'fail', 'args': {'msg': 'fail'}}},
        ]
    }, variable_manager=VariableManager(), loader=DictDataLoader())

# Generated at 2022-06-12 21:37:58.922669
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    temp_host = lambda hostname: Host(hostname) if hostname else None
    state = HostState(temp_host('localhost'))
    assert(PlayIterator().is_any_block_rescuing(state) is False)
    state.run_state = PlayIterator.ITERATING_RESCUE
    assert(PlayIterator().is_any_block_rescuing(state) is True)
    state.run_state = PlayIterator.ITERATING_TASKS
    state.tasks_child_state = HostState(temp_host('localhost'))
    state.tasks_child_state.run_state = PlayIterator.ITERATING_RESCUE
    assert(PlayIterator().is_any_block_rescuing(state) is True)


# Generated at 2022-06-12 21:38:07.724250
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play = Play()
    block1 = Block(play)
    block2 = Block(play)
    block3 = Block(play)
    block4 = Block(play)
    block5 = Block(play)
    block6 = Block(play)

    # 1. test for passing
    play_itr = PlayIterator(play, lambda x: None)
    state = HostState(blocks=[block1, block2, block3, block4])
    state.cur_block = 0
    state.run_state = 1

    # test 1
    assert not play_itr.is_any_block_rescuing(state)
    # TODO: test 2

    # 2. test for failing
    # play_itr = PlayIterator(play, lambda x: None)

# Generated at 2022-06-12 21:38:15.983691
# Unit test for method copy of class HostState
def test_HostState_copy():
    blocks = [Block(['tasks'], [Task(['t1'])])]
    blocks[0].tasks[0].block = blocks[0]
    host_state = HostState(blocks)
    host_state.cur_block = 0
    host_state.cur_regular_task = 0
    host_state.cur_rescue_task = 0
    host_state.cur_always_task = 0
    host_state.run_state = 1
    host_state.fail_state = 0
    host_state.pending_setup = False
    host_state.did_rescue = False
    host_state.did_start_at_task = False
    host_state.tasks_child_state = None
    host_state.rescue_child_state = None
    host_state.always_child_

# Generated at 2022-06-12 21:38:21.680361
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    """
    PlayIterator.get_host_state() Test Plan:
        Create a PlayIterator instance with the playbook
        Create an invalid host name
        Assert that the method under test raises a SystemExit exception
    """
    PlaybookCLI(["test_playbook.yml"]).parse()
    pass



# Generated at 2022-06-12 21:38:31.030975
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    Unit test for method mark_host_failed.
    '''
    import ansible.playbook

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    play_context = PlayContext()
    iterator = PlayIterator(play_context)

    host = Mock()
    host.name = "foo"
    host.all_vars = dict()

    block1 = Block.load(dict(block=[]), play=None, task_include=None, role=None, use_handlers=False, variable_manager=None, loader=None)

# Generated at 2022-06-12 21:38:33.615842
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    hs = HostState()
    assert hs.get_host_state() == None
    hs.set_host_state(1)
    assert hs.get_host_state() == 1


# Generated at 2022-06-12 21:39:32.946667
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    #
    # PlayIterator.get_active_state(state) method unit test
    #
    # (The PlayIterator class isn't exported here and
    # was copied into this file to allow running
    # the unit test)
    #

    # initialize PlayIterator class dependencies

    class Parser(object):
        pass

    class Play(object):
        pass

    # initialize class instance
    play = Play()
    play.playbook = Parser()
    play.playbook.basedir = './test/integration/'
    play.playbook_basedir = './test/integration/'
    play_iterator = PlayIterator(play=play)

    # initialize state
    state = HostState()
    state.run_state = PlayIterator.ITERATING_COMPLETE

# Generated at 2022-06-12 21:39:43.945875
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    from ansible.playbook import Play
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Inventory

    play = Play().load(dict(
        name = "Test Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    ), loader=DictDataLoader())

    inventory = Inventory(loader=DictDataLoader())
    inventory.add_host('localhost')

    itr = PlayIterator(inventory, play)
    itr._play = play

    host = inventory.get_host('localhost')

# Generated at 2022-06-12 21:39:51.813509
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    mock_play = MagicMock()
    mock_play.post_validate.return_value = True
    mock_play.post_validate_data = {}
    fake_loader = DictDataLoader({})
    fake_variable_manager = VariableManager()
    mock_play._ds = Playbook()
    mock_host_name = 'host123'
    mock_host = Host(mock_host_name)
    mock_block = Block()
    mock_block._role_name = None
    mock_block._dep_chain = None
    mock_block._role = None
    mock_iterator = PlayIterator(mock_play, fake_loader, fake_variable_manager)
    mock_iterator._tqm = MagicMock()
    mock_iterator._play = mock_play
    mock_iterator._play._dep_chain

# Generated at 2022-06-12 21:40:03.242383
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    def compare_tasks(tasks1, tasks2):
        if not isinstance(tasks1, list) or not isinstance(tasks2, list):
            return False
        if len(tasks1) != len(tasks2):
            return False