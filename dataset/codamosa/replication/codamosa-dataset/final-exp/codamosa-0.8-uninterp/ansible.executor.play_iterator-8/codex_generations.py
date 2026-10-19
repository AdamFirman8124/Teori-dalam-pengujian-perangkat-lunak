

# Generated at 2022-06-12 21:31:02.140503
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    print("Testing PlayIterator.get_active_state")
    # This test finds failures in the function get_active_state of class PlayIterator.
    # get_active_state is a recursive function that finds the active state in a state tree. We test it
    # by generating a random tree and a random path through the tree. We then check that get_active_state
    # finds the correct location.

    # How many times to run (more means more likely to find a failure, if there is one).
    iterations = 100
    for i in range(iterations):
        # Generate a random walk through the tree. State_walk is a list of integers. Each integer is the index
        # of a child state in that state's list of child states.
        state_walk = []
        # Get the number of states in the path.
        num_states = random.rand

# Generated at 2022-06-12 21:31:12.921880
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    host = Host('fake_hostname')
    play_context = PlayContext()
    play = Play().load(dict(
        name = "test play",
        hosts = 'fake_hostname',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='shell', args='false')),
        ]
    ), variable_manager=VariableManager(), loader=DummyLoader())
    play_iter = PlayIterator(play, play_context, variable_manager=VariableManager(), loader=DummyLoader())
    play_iter.get_next_task_for_host(host)
    play_iter.mark_host_failed(host)
    if play_iter.is_failed(host):
        print('Test passed')

# Generated at 2022-06-12 21:31:14.245833
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    pass


# Generated at 2022-06-12 21:31:24.976965
# Unit test for method mark_host_failed of class PlayIterator

# Generated at 2022-06-12 21:31:35.132091
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    data = dict(a=dict(ansible_host='1.1.1.1', ansible_user='a', ansible_port=123))
    inventory = Inventory(loader=DictDataLoader(data))
    play = Play().load({}, variable_manager=VariableManager(), loader=DictDataLoader({}))
    play.hosts = ['a']
    iterator = PlayIterator(inventory, play, play.tasks, None)
    iterator.mark_host_failed(inventory.get_host('a'))
    assert iterator.get_failed_hosts() == {'a': True}


# Generated at 2022-06-12 21:31:45.364728
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():

    fake_play = FakePlay()
    fake_host = FakeHost(name='test_host')
    original_task = Task()
    fake_task = Task()

    # insert fake task after the "original" task
    def _fake_itertasks_return_task(*args, **kwargs):
        return (_task for _task in (original_task, fake_task)).next()

    # When the PlayIterator is created, the Play's itertasks was changed out with
    # a generator that returned a task in the middle of a multi-task play.
    # The original task can be retrieved from the iterator's _itertasks_cache
    def test_get_original_task():
        iterator = PlayIterator(play=fake_play)
        iterator._itertasks_cache[fake_task][0] = original_task
        assert iterator.get

# Generated at 2022-06-12 21:31:53.329592
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    play = Play()
    play.add_block_list([{"name": "first block", "action": ["a", "b", "c"]}, {"name": "second block", "action": ["d", "e", "f"]}])
    block = Block()
    block.add_task({"action": "g", "name": "first task"}, play=play)
    block.add_task({"action": "h", "name": "second task"}, play=play)
    play.add_block_list([block])
    play.add_block_list([{"name": "fourth block", "action": ["i", "j", "k"]}])
    host = Host("localhost")
    iterator = PlayIterator(play)
    host.name = "localhost"
    play.set_variable_manager(VariableManager())
    iterator.get

# Generated at 2022-06-12 21:31:59.485133
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    def test_condition(expected_state, input_state):
        assert expected_state.run_state == play_iterator.PlayIterator.get_active_state(input_state).run_state
        assert expected_state.cur_block == play_iterator.PlayIterator.get_active_state(input_state).cur_block
        assert expected_state.fail_state == play_iterator.PlayIterator.get_active_state(input_state).fail_state

    state1 = play_iterator.HostState()
    state1.run_state = play_iterator.HostState.ITERATING_TASKS
    state1.cur_block = 1
    state1.fail_state = play_iterator.HostState.FAILED_NONE

    state2 = play_iterator.HostState()

# Generated at 2022-06-12 21:32:01.747043
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    class FakePlay(object):
        def __init__(self):
            self._variable_manager = VariableManager()
            self._hosts = ['foo', 'bar']

    class FakeOptions(object):
        def __init__(self):
            self.listhosts = None

    p = FakePlay()
    o = FakeOptions()
    PlayIterator(p, o, None, None)

# Generated at 2022-06-12 21:32:05.937364
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    class a:
        pass
    def x():
        return 'a'
    class b(x):
        pass
    state = a()
    state.a = 1
    state.b = 2
    state.c = 3
    state.d = 4
    state.e = 5
    state._blocks = [a(),b()]
    state.cur_block = 0
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state.run_state = PlayIterator.ITERATING_SETUP
    state.fail_state = PlayIterator.FAILED_NONE
    state.pending_setup = False
    state.tasks_child_state = None
    state.rescue_child_state = None
    state.always_child

# Generated at 2022-06-12 21:32:42.773847
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    Ensure mark_host_failed() sets the correct states
    '''
    def _run_block_test(block_type, error_state):
        p = Play().load(dict(
            name="test",
            hosts="all",
            gather_facts="no",
            tasks=[
                dict(action=dict(module="debug", args=dict(msg="first step"))),
                dict(action=dict(module="fail", fail_host=True, args=dict(msg="test"))),
                dict(action=dict(module="debug", args=dict(msg="third step"))),
            ]
        ), loader=DictDataLoader())
        ti = PlayIterator()
        h = Host(name="test")
        ti._play = p
        ti._play._iterator = ti
        ti.get_next_task_

# Generated at 2022-06-12 21:32:51.769204
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():

    # first, the simple case
    start_state = HostState(blocks=[])
    simple_state = start_state.copy()
    simple_state.run_state = PlayIterator.ITERATING_SETUP
    simple_state.cur_block = 1
    simple_state.cur_task = 2
    ansi_start = PlayIterator.HOST_STATE_FIELDS[:-1] + ['HOST_STATE_COLOR', PlayIterator.HOST_STATE_FIELDS[-1]]
    ansi_end = ['HOST_STATE_COLOR', PlayIterator.HOST_STATE_FIELDS[-1]]

    # set up for the more complicated tests
    parent_state = HostState(blocks=[])
    child_state = HostState(blocks=[])
    child_state.cur_task = 2

# Generated at 2022-06-12 21:33:04.509377
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    host = Host(name='foo')
    play = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), variable_manager=VariableManager(), loader=BaseLoader())
    tqm._initialize_processes(3)

# Generated at 2022-06-12 21:33:08.814034
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # FIXME: write unit test for
    raise Exception("not implemented")

# Generated at 2022-06-12 21:33:16.359940
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    p = Play()
    i = PlayIterator(p)
    h = Host("testhost")
    # No blocks
    state = HostState(blocks=[])
    assert i.is_any_block_rescuing(state) == False
    # No tasks in block
    state = HostState(blocks=[Block()])
    assert i.is_any_block_rescuing(state) == False
    # Rescue block in the tasks
    state = HostState(blocks=[Block(rescue=[Block()])])
    assert i.is_any_block_rescuing(state) == False
    # Rescue block in the tasks, with a child

# Generated at 2022-06-12 21:33:19.417555
# Unit test for method get_next_task_for_host of class PlayIterator

# Generated at 2022-06-12 21:33:30.366986
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    """
    PlayIterator: add_tasks
    """
    test_IterationState()
    test_HostState()
    test_Block()
    test_Task()
    test_Play()
    test_Inventory()

    # test case 1
    ds = iter(range(0,10))
    ds.next()

    # test case 2
    iter1 = PlayIterator()
    assert iter1 != None

    # test case 3
    iter1 = PlayIterator()
    iter1.add_tasks('', [])
    assert iter1 != None

    # test case 4
    iter1 = PlayIterator()
    assert iter1 != None

    # test case 5
    iter1 = PlayIterator()
    iter1.add_tasks('', [])
    assert iter1 != None


# Generated at 2022-06-12 21:33:38.458187
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    p = Play().load(dict(name="test play", hosts='all', gather_facts='no',
        tasks=[dict(action='debug', msg='Hello, world')]
    ), loader=DictDataLoader({}))
    play = PlayIterator(p)
    assert(play._play is p)
    assert(play._play_basedir is None)
    assert(isinstance(play._hosts, list))
    assert(len(play._hosts) == 0)
    assert(isinstance(play._hosts_left, list))
    assert(len(play._hosts_left) == 0)
    assert(isinstance(play._hosts_cache, dict))
    assert(len(play._hosts_cache) == 0)
    assert(isinstance(play._host_states, dict))

# Generated at 2022-06-12 21:33:51.433737
# Unit test for constructor of class PlayIterator

# Generated at 2022-06-12 21:33:59.142660
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():

    # The test fixture has three tasks.  The second is a handler.  The
    # third has been modified in some way (its action has been changed
    # to 'debug' and a new property ('msg') has been added).

    t1 = Task()
    t1._uuid = '1234'
    t1.action = 'command'
    t1._role = None
    t1._block = None

    t2 = Task()
    t2._uuid = '5678'
    t2.action = 'shell'
    t2._role = None
    t2._block = None

    t3 = Task()
    t3._uuid = 'abcd'
    t3.action = 'debug'
    t3.msg = 'xyzzy'
    t3._role = None
    t3._block = None



# Generated at 2022-06-12 21:34:57.001252
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    module_utils.basic._ANSIBLE_ARGS = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': {'one': 'foo', 'two': 'bar', 'three': 'baz', 'four': 'qux'}}))

    def func(*args, **kwargs):
        return True

    fake_loader = DictDataLoader({})
    fake_variable_manager = VariableManager()
    fake_inventory = Inventory(loader=fake_loader, variable_manager=fake_variable_manager, host_list='localhost,127.0.0.1')

# Generated at 2022-06-12 21:34:58.261274
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    pass

test_PlayIterator_is_failed.stub = True


# Generated at 2022-06-12 21:35:06.003195
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    # set up test variables
    play = Play()

    host = Host(name='host.example.com')
    host.set_variable('foo', 'bar')
    state = HostState(host=host)
    state._play = play
    state._tqm = None
    state.run_state = PlayIterator.ITERATING_SETUP
    state.cur_block = 0
    state._blocks = [Block(role=None)]
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state.fail_state = PlayIterator.FAILED_NONE
    state.did_rescue = False
    state.tasks_child_state = None

    # call mark_host_failed of PlayIterator
    obj = PlayIterator()
   

# Generated at 2022-06-12 21:35:09.106315
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    test__PlayIterator = PlayIterator("foo")
    assert test__PlayIterator.cache_block_tasks("foo", "foo", "foo") == ({"foo", "foo"}, {"foo"})


# Generated at 2022-06-12 21:35:18.748327
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    host = MagicMock()
    host.get_vars.return_value = dict()
    block = Block()
    play = MagicMock()
    play.hosts = dict()
    play.hosts[host.name] = host
    pi = PlayIterator(play=play)
    pi.get_next_task_for_host(host, block) == (None, None)
    block.add_task(MagicMock())
    task = pi.get_next_task_for_host(host, block)
    assert task == (HostState(blocks=[block]), block.block[0])
    play.hosts = dict()
    pi.get_next_task_for_host(host, block) == (None, None)


# Generated at 2022-06-12 21:35:28.463964
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # AnsibleModule argument spec for the module
    module_args = dict()

# Generated at 2022-06-12 21:35:40.715819
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    mock_play = dict(
        play=dict(
            name='the play',
            hosts='the_hosts',
            gather_facts=False,
            tasks=[
                dict(action=dict(module='debug', args=dict(msg='task1'))),
                dict(action=dict(module='debug', args=dict(msg='task2'))),
                dict(action=dict(module='debug', args=dict(msg='task3'))),
                dict(action=dict(module='debug', args=dict(msg='task4')))
            ]),
        pattern='the_hosts',
        name='the task',
        vars={ 'test' : 'test1' },
        )

# Generated at 2022-06-12 21:35:47.582311
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play()
    play.name = 'host_state_play'
    play.hosts = 'HOST1'
    hosts = set()
    hosts.add('HOST1')
    host_state = PlayIterator.get_host_state(play,
                                             hosts,
                                             Host('HOST1'),
                                             Host('HOST1'),
                                             'host_state_play')
    
    assert host_state == 'not started'


# Generated at 2022-06-12 21:35:55.968834
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    runner = Mock()
    host = Mock()
    tasks = [dict(name='task1'), dict(name='task2'), dict(name='task3')]
    block = Block(runner=runner, host=host, tasks=tasks)
    new_play = Mock()
    new_play._tqm = None
    new_play.serial = 0
    new_play.hosts = ['foo']
    new_play.get_vars.return_value = dict()
    new_play._variable_manager = Mock()
    new_play._variable_manager.get_vars.return_value = {}
    new_play._variable_manager.add_playbook_vars.return_value = {}
    new_play._variable_manager.extra_vars = {}
    new_play._variable_manager.set_nonpers

# Generated at 2022-06-12 21:35:57.754190
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
  #FIXME: implement a unit test for PlayIterator.is_failed
  assert False


# Generated at 2022-06-12 21:36:53.991851
# Unit test for method get_next_task_for_host of class PlayIterator

# Generated at 2022-06-12 21:37:04.483999
# Unit test for method cache_block_tasks of class PlayIterator

# Generated at 2022-06-12 21:37:10.971352
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    """
    为 PlayIterator 类的 get_host_state() 方法编写单元测试
    """
    print("Starting test_PlayIterator_get_host_state ... ")
    # 对 get_host_state 方法进行单元测试
    hosts = [ Host('localhost') ]
    play = Play()
    iterator = PlayIterator(play, hosts)
    iterator.get_host_state(hosts[0])
    print("test_PlayIterator_get_host_state finished.")


# Generated at 2022-06-12 21:37:13.226797
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    pi = PlayIterator()
    check_obj_is_immutable(pi, 'test_PlayIterator_get_original_task')

# Generated at 2022-06-12 21:37:21.537017
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    PlayIterator.ITERATING_RESCUE = 'ITERATING_RESCUE'

# Generated at 2022-06-12 21:37:31.063068
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    MOCK_PLAY = object()
    pi = PlayIterator(MOCK_PLAY, [], {})
    empty_state = HostState(blocks=[])
    active = pi.get_active_state(empty_state)
    assert active == empty_state
    # Create a state with blocks and call again
    state = HostState(blocks=[Block(u'testblock', [], [], [])])
    active = pi.get_active_state(state)
    assert active == state
    # Add a child to the tasks section and call again
    state.tasks_child_state = HostState(blocks=[Block(u'testblock2', [], [], [])])
    active = pi.get_active_state(state)
    assert active != state
    assert state.tasks_child_state == active
    # Add a child to the

# Generated at 2022-06-12 21:37:38.020793
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    # data setup
    host = Host('testhostname')
    host.set_variable('ansible_python_interpreter', '/usr/bin/python')
    task = Task()
    task._role_name = 'rolename'
    task._role_path = '/path/to/rolename'
    task._ds = dict(
            task_name='mytaskname',
            action='mymodule',
            args=dict(
                key1='value1',
                key2='value2'
                )
            )

    module_name = 'mymodule'

    task._role = RoleDefinition('rolename', '/path/to/rolename', [], [], [], [], task)

    # method under test
    play_iterator = PlayIterator()
    (real_task, role_result) = play_iterator.get_original

# Generated at 2022-06-12 21:37:42.500006
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    host = MagicMock(name='host')
    task = MagicMock(name='task')
    play_iterator = PlayIterator(play=MagicMock(name='play'), hosts=MagicMock(name='hosts'))
    play_iterator.get_original_task(host, task)

# Generated at 2022-06-12 21:37:54.236305
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    play = Play()
    play._hosts_cache = [Host(name='testhost')]
    play._removed_hosts = []
    play_context = PlayContext()
    play_context._ds = {'some_var': 'foo'}
    play_context.variables = {}
    play_context.update_vars = lambda d: None
    play_iterator = PlayIterator(play, play_context, [], [], 0)
    play_iterator.get_next_task_for_host(Host(name='testhost'))
    assert play_iterator.is_failed(Host(name='testhost')) == False
    play_iterator.mark_host_failed(Host(name='testhost'))
    assert play_iterator.is_failed(Host(name='testhost')) == True
    play._removed

# Generated at 2022-06-12 21:38:04.622576
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    play = Play().load(dict(
        name = "foobar",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    ), variable_manager=dict(), loader=None)
    iterator = PlayIterator(play)
    host = 'jdoe'
    state = iterator.get_host_state(host)
    assert state.run_state == PlayIterator.ITERATING_SETUP

# Generated at 2022-06-12 21:39:40.252859
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    pass
# vim: set expandtab ts=4 sw=4:

# Generated at 2022-06-12 21:39:45.356648
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    play = Play().load(dict(
        name = "some play",
        hosts = 'webservers',
        gather_facts = 'no',
        roles = []
    ), variable_manager=variable_manager, loader=loader)
    iterator = PlayIterator(play)
    assert len(iterator._play.get_tasks()) == 0
    assert len(iterator._play.get_roles()) == 0



# Generated at 2022-06-12 21:39:50.252452
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    target = PlayIterator()
    host_states = {}
    host_states['host1'] = HostState(blocks=[])
    target._host_states = host_states
    target.mark_host_failed('host1')
    assert host_states['host1'].fail_state == target.FAILED_TASKS
    assert host_states['host1'].run_state == target.ITERATING_COMPLETE


# Generated at 2022-06-12 21:39:52.954982
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # Setup test values
    state = HostState()
    # Run method
    result = p.get_active_state(state)
    assert result == state



# Generated at 2022-06-12 21:40:04.049135
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():

    class MockHost:
        def get_name(self):
            return 'localhost'

    class MockCurrentTask:
        def get_name(self):
            return 'bad_task'

    class MockTask:
        def get_name(self):
            return 'good_task'

    class MockTaskList:
        def __getitem__(self, key):
            return MockTask()

    class MockPlay:
        name = 'test_play'
        hosts = ['localhost']
        _removed_hosts = []

    class MockRole:
        name = 'test_role'

    class MockBlock:
        def __init__(self, risk=TaskRisk.HIGH):
            self.role = MockRole()
            self.risk = risk
