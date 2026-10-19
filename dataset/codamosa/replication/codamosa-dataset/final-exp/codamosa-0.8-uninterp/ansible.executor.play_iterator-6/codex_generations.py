

# Generated at 2022-06-12 21:30:48.566434
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    # test for is_any_block_rescuing when no rescue block exists
    play = Play().load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='debug', args=dict(msg='hello world')))
        ]
    ), variable_manager=VariableManager(), loader=Loader())
    iterator = PlayIterator(play, play.tasks)
    host = Host(name="testhost")
    state = iterator.get_next_task_for_host(host)
    assert state.run_state == iterator.ITERATING_TASKS
    assert not iterator.is_any_block_rescuing(state)
    state = iterator.get

# Generated at 2022-06-12 21:30:50.261439
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    pass



# Generated at 2022-06-12 21:30:52.241060
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    assert( PlayIterator().is_failed(None) == False )

# Generated at 2022-06-12 21:31:01.020152
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    """
    Test case for PlayIterator.cache_block_tasks

    """


# Generated at 2022-06-12 21:31:09.873903
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    host = Host(name='foo.bar.com')
    iterator = PlayIterator(play=Play(), inventory=None)
    iterator._host_states = {host.name: HostState(blocks=[Block(block=[
        Task(),
        Task()])])}
    iterator.add_tasks(host, [Task()])
    assert_equal(2, iterator._host_states[host.name].cur_regular_task)
    assert_equal([Task(), Task(), Task()], iterator._host_states[host.name]._blocks[0].block)


# Generated at 2022-06-12 21:31:13.150145
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
	p = Play()
	p.vars = dict()
	p.playbook = Playbook()
	pi = PlayIterator()
	pi._play = p
	p._iterator = pi
	p._iterator.cache_block_tasks(Block(), dict())



# Generated at 2022-06-12 21:31:24.169422
# Unit test for method get_failed_hosts of class PlayIterator

# Generated at 2022-06-12 21:31:25.432627
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    pass


# Generated at 2022-06-12 21:31:38.326328
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    '''
    Test get_original_task correctly returns the original task in the play, not the task from an include_tasks
    '''

    # play_source contains the play which will be used for testing
    play_source = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(name = 'test task 1', debug = dict(msg = 'This is a test task')),
            dict(name = 'test task 2', debug = dict(msg = 'This is a test task')),
            dict(name = 'test task 3', debug = dict(msg = 'This is a test task')),
        ],
    )

    # play contains an InMemoryDataLoader object which is used to load the play source
    # and a Play object which is the play itself

# Generated at 2022-06-12 21:31:39.360365
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    assert False

# Generated at 2022-06-12 21:32:22.510014
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block_include import BlockInclude
    from ansible.playbook.handler import Handler

    # Two dummy tasks
    foo_task = Task()
    foo_task.action = 'foo'
    foo_task.name = 'foo task'
    bar_task = Task()
    bar_task.action = 'bar'
    bar_task.name = 'bar task'

    # Creates a block with one task (foo_task)
    foo_block = Block()
    foo_block.block = [foo_task]

    # Creates a block with one task (bar_task

# Generated at 2022-06-12 21:32:24.590668
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    Unit test for method is_failed of class PlayIterator
    '''
    iterator = PlayIterator()

    # Place your test code here
    raise AssertionError('No tests written')


# Generated at 2022-06-12 21:32:25.981407
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    iter = PlayIterator()
    assert iter is not None


# Generated at 2022-06-12 21:32:38.106183
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    p = Play.load(dict(
        name = "foobar",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='debug', args=dict(msg='yay')))
        ],
        handlers = [
            dict(action=dict(module='shell', args='/etc/init.d/apache restart'))
        ]
    ), loader=Mock(), variable_manager=VariableManager())

    inventory = Inventory(loader=Mock())
    inventory.add_group('webservers')
    all_hosts = inventory.get_groups_dict()['webservers']['hosts']
    all_hosts.append('junk')

# Generated at 2022-06-12 21:32:46.581914
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    This is a test method for testing the get_failed_hosts() method of the PlayIterator class.
    '''
    # create an iterator and a host
    iterator = PlayIterator()
    host = Host('testhost', 'testhost')
    # create a block that contains a task, and a task which will fail
    test_block = Block([ ActionTask.load('fail', None) ])
    # append the block to the host state list
    iterator.get_host_state(host)._blocks.append(test_block)
    # run the function
    result = iterator.get_failed_hosts()
    # assert that we have a single host in the results dictionary and that it is our test host
    assert len(result) == 1, 'There should be a single host in the results dictionary.'

# Generated at 2022-06-12 21:32:54.757400
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    '''
    Unit test for constructor of class PlayIterator
    '''
    def iterate(iterator):
        iterators = []
        for (host, tasks) in iterator:
            iterator = PlayIterator(host, tasks)
            iterators.append(iterator)
        return iterators
    play_source = dict(
        name = "test play",
        hosts = ['foo', 'bar', 'baz'],
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=DictDataLoader())
    iterator = Play

# Generated at 2022-06-12 21:33:05.860795
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    '''
    Unit test function for PlayIterator_get_active_state() method of class PlayIterator
    '''
    play_obj = Play()
    play_iterator_obj = PlayIterator(play_obj)
    #test with value
    a = HostState()
    b = HostState()
    c = HostState()
    d = HostState()
    e = HostState()
    a.tasks_child_state = b
    b.always_child_state = c
    c.tasks_child_state = d
    d.always_child_state = e
    assert play_iterator_obj.get_active_state(a) == a
    assert play_iterator_obj.get_active_state(b) == b


# Generated at 2022-06-12 21:33:15.655804
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block


# Generated at 2022-06-12 21:33:26.992389
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    test_host_state = HostState([0,1,2])
    test_host_state.cur_block = 0
    test_host_state.cur_regular_task = 0
    test_host_state.cur_rescue_task = 0
    test_host_state.cur_always_task = 0
    test_host_state.run_state = 1
    test_host_state.fail_state = 1
    test_host_state.pending_setup = False
    test_host_state.tasks_child_state = None
    test_host_state.rescue_child_state = None
    test_host_state.always_child_state = None
    test_host_state.did_rescue = False
    test_host_state.did_start_at_task = False

# Generated at 2022-06-12 21:33:36.369426
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    PlayIterator.is_failed test cases
    '''
    pi = PlayIterator()

    # Setup Mock Objects
    m_get_host_state = MagicMock(return_value = 'HostState')
    m_check_failed_state = MagicMock(return_value = False)

    # Setup the object under test
    pi._get_host_state = m_get_host_state
    pi._check_failed_state = m_check_failed_state
    pi.play = Play()
    pi.play._play_context = PlayContext()
    pi.play._play_context.remote_addr = 'remote_addr'

    # Exercise the object under test
    host = Host(name='host')
    result = pi.is_failed(host)

    # Ensure the correct results
    m_get_host_

# Generated at 2022-06-12 21:34:47.815973
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    def iterate_get_failed():
        pass
    def get_hosts_remaining():
        pass
    def get_failed_hosts():
        pass
    def mark_host_failed():
        pass
    def mark_host_unreachable():
        pass
    def get_active_state():
        return (None, None)
    def get_host_state():
        pass
    def get_next_task_for_host():
        pass
    def get_original_task():
        pass
    def get_original_var():
        pass
    def add_tasks():
        pass
    host_states = {'INITIAL': HostState()}
    play = Play()
    iterator = PlayIterator(play, host_states)
    iterator._play = object()
    assert iterator._play != play
    iterator

# Generated at 2022-06-12 21:34:57.817273
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

    # create a dummy play to hold the list of hosts
    play = Play()
    play._play_hosts = dict([(host, True) for host in ('host1', 'host2')])

    # create a dummy inventory to hold a host
    inventory = Inventory(loader=DataLoader())
    inventory._hosts_cache = create_hosts_dict(('host1',))
    inventory.parse_inventory(inventory_filename=os.path.join(fixtures_path, 'inventory', 'hosts'))
    assert inventory.get_host('host1')

    # run a simple playbook and verify it ran

# Generated at 2022-06-12 21:34:58.816305
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    '''
    Nothing to test here.
    '''


# Generated at 2022-06-12 21:35:06.654658
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():

    #setup
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    the_host = Host('testhost')
    the_play = Play()
    the_play.name = 'testplay'
    the_play.hosts.add('testhost')
    the_play.gather_facts = 'no'
    the_block = Block()
    the_block.block = [ Task() ]
    the_play.tasks = [ the_block ]
    the_iterator = PlayIterator(the_play)

    # test 1 (normal flow)
    assert the_iterator.is_failed(the_host) is False, 'first iteration should not be failed'
    the_host_state,

# Generated at 2022-06-12 21:35:13.351246
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    test_play = Play()
    test_play.set_loader(Mock())
    test_play.set_variable_manager(Mock())
    test_play.add_host(host=Host(name="otherhost"))
    test_play.add_host(host=Host(name="testhost"))
    test_play.add_task(Task(action=dict(module="test"), register="t1"))
    test_play.add_task(Task(action=dict(module="test"), register="t2"))
    test_play.add_task(Task(action=dict(module="test"), register="t3"))
    test_play.add_task(Task(action=dict(module="test"), register="t4"))
    test_play.add_task(Task(action=dict(module="test"), register="t5"))


# Generated at 2022-06-12 21:35:24.453272
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
  # Test get_active_state with a simple non-nested task block
  # (This test is basically redundant as the get_active_state method is a noop in this case)
  h = Host('host')
  p = Play().load(dict(hosts=['host']), variable_manager=VariableManager(), loader=None)
  i = PlayIterator()
  hs = HostState(blocks=[
      Block(task_list=[
          Task().load(dict(action='test'), variable_manager=VariableManager(), loader=None)
      ])
  ])
  hs.run_state = PlayIterator.ITERATING_TASKS
  hs.cur_block = 0
  hs.cur_regular_task = 0
  assert PlayIterator.ITERATING_TASKS == i.get_active_state(hs)
 

# Generated at 2022-06-12 21:35:36.301167
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    play = dict(
        hosts = 'host1',
        vars = dict(x = 1),
        tasks = [
            dict(action=dict(module='command', args='echo {{x}}'), register='y'),
            dict(action=dict(module='command', args='echo {{y.stdout}}')),
            dict(action=dict(module='command', args='echo {{y.stdout}}'))
        ]
    )
    play = Play().load(play, variable_manager=VariableManager(), loader=DictDataLoader())
    iterator = PlayIterator(play)
    host = Host('host1')
    host.set_variable('x', 1)
    iterator.cache_block_tasks(host, [play._tasks[0]], 0, 0)

# Generated at 2022-06-12 21:35:47.901854
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''
    PlayIterator._cache_block_tasks() Test plan:
        - normal
    '''

    # setup test Play

# Generated at 2022-06-12 21:35:56.085048
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    '''
    get_active_state(state)
    '''
    # we have some setup to do here to make the test runable
    class FakeHost():
        def __init__(self, name, task_state=None):
            self.name = name
            self.task_state = task_state
    class FakePlay():
        def __init__(self):
            self._removed_hosts = []
        def _remove_host(self, host):
            self._removed_hosts.append(host)

# Generated at 2022-06-12 21:36:06.997089
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    host = MagicMock(name="host")
    host.name = "testhost"
    host.get_vars.return_value = {}

    play_ds = create_autospec(Play())
    play_ds.hosts = [host]

    iterator = PlayIterator(play_ds, None)
    iterator._host_states[host.name] = MagicMock(name="host_state")
    iterator._host_states[host.name].fail_state = 0
    iterator._host_states[host.name]._blocks = []
    iterator._host_states[host.name]._blocks.append(MagicMock(name="block1"))
    iterator._host_states[host.name]._blocks.append(MagicMock(name="block2"))

# Generated at 2022-06-12 21:38:31.428999
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    host = FakeHost(name="test_host")
    play_ds = dict(
        name="test_play",
        hosts='all',
        gather_facts='no',
        tasks=[
        ]
    )
    play = Play().load(play_ds, variable_manager=VariableManager(), loader=Loader())
    iterator = PlayIterator(play)

    # Case 1.
    debug("case 1: current block is tasks")
    state = HostState(host, task_blocks=[
        TaskBlock(
            block=["t1", "t2"],
            rescue=[],
            always=[]
        ),
        TaskBlock(
            block=["t3", "t4"],
            rescue=[],
            always=[]
        ),
    ])
    state.run_state = PlayIterator.ITERATING_TASKS

# Generated at 2022-06-12 21:38:37.593284
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():

    # test_PlayIterator_cache_block_tasks() of TestPlayIterator.test_play_iterator()
    # Test the PlayIterator with a simple play and make sure it reports the correct number of handlers
    def get_handler_tasks(play):
        itr = PlayIterator()
        handler_call_counts = itr.get_handler_call_counts(play)
        assert handler_call_counts['t1'] == 1
        assert handler_call_counts['t2'] == 2
        assert handler_call_counts['t3'] == 1

    def get_task_list(play):
        itr = PlayIterator()
        task_list = itr.get_task_list(play)
        assert len(task_list) == 4
        assert task_list[0] == 't1'
        assert task

# Generated at 2022-06-12 21:38:45.553758
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    '''
    Unit test for method get_host_state of class PlayIterator
    '''
    # Create a new PlayIterator object
    pi = PlayIterator()
    # Get a HostState
    hs = pi.get_host_state(host='localhost')
    assert hs._blocks == [], 'Expected hs._blocks == []; got {0}'.format(hs._blocks)
    assert hs.cur_block == 0, 'Expected hs.cur_block == 0; got {0}'.format(hs.cur_block)
    assert hs.cur_regular_task == 0, 'Expected hs.cur_regular_task == 0; got {0}'.format(hs.cur_regular_task)

# Generated at 2022-06-12 21:38:55.982311
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    ansible_playbook_dir = sys.path[0]
    config_file = os.path.join(ansible_playbook_dir,'ansible.cfg')
    inventory_file = os.path.join(ansible_playbook_dir,'hosts')
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,host_list=inventory_file)
    variable_manager.set_inventory(inventory)
    passwords = dict(vault_pass='secret')
    pi = PlayIterator(loader,  inventory, variable_manager,passwords)
    pi.play = Play().load(play_ds,'test_play',variable_manager=variable_manager,loader=loader)
    pi.play._variable_manager._fact_cache = dict()

# Generated at 2022-06-12 21:39:06.307079
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    '''
    Test the get_next_task_for_host method of the PlayIterator
    '''
    # Create an instance of a dummy subclass of PlayIterator
    play = Play().load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='command', args=dict(cmd="false"))),
            dict(action=dict(module='command', args=dict(cmd="true"))),
            dict(action=dict(module='command', args=dict(cmd="false"))),
        ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())
    play_iterator = PlayIterator(play)
    assert play_iterator._play is play

    # Create an instance of a host

# Generated at 2022-06-12 21:39:15.632524
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    ####
    # Test the method without the optional argument 'host'
    ####
    # Test when state.tasks_child_state is not None
    iterator = PlayIterator()
    play = iterator.play
    state = PlayIterator.HostState(blocks=play.compile())
    state.tasks_child_state = PlayIterator.HostState(blocks=play.compile())
    state.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
    result = iterator.get_active_state(state)
    assert result == state.tasks_child_state
    # Test when state.rescue_child_state is not None
    iterator = PlayIterator()
    play = iterator.play
    state = PlayIterator.HostState(blocks=play.compile())
    state.rescue_child_

# Generated at 2022-06-12 21:39:27.232788
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    class MyTask(object):
        def __init__(self):
            pass

    class MyBlock(object):
        def __init__(self):
            self.tasks = [MyTask(),MyTask(),MyTask()]
            self.rescue = [MyTask(),MyTask()]
            self.always = [MyTask(),MyTask()]

    class MyPlay(object):
        def __init__(self):
            self.hosts = ['host1', 'host2', 'host3']
            self.block_list = [MyBlock(),MyBlock()]
            self.serialized_blocks = []

    myplay = MyPlay()
    myplay_iterator = PlayIterator(myplay)
    hosts = ['host1', 'host2', 'host3']

# Generated at 2022-06-12 21:39:27.950534
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
	pass

# Generated at 2022-06-12 21:39:31.285062
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
  expected = False
  actual = PlayIterator(play=None, play_context=None, variable_manager=None, loader=None).is_failed(host=None)
  assert actual == expected, 'Expected: %s, Actual: %s' % (expected, actual)

# Generated at 2022-06-12 21:39:42.958218
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    # test as though "foo" is a member of the play's hosts
    assert p._play_hosts['foo'] is not None

    # set up iterator and some test data
    p._play_hosts['foo'].vars = dict(a=1, b=2)
    test_host = p._play_hosts['foo']
    test_iterator = PlayIterator(p)

    # pretend some tasks have been run
    test_iterator.get_next_task_for_host(test_host)
    test_iterator.get_next_task_for_host(test_host)
    test_iterator.get_next_task_for_host(test_host)

    # do a get_host_state()/mark_host_failed()/is_failed() cycle to test that this is accurate