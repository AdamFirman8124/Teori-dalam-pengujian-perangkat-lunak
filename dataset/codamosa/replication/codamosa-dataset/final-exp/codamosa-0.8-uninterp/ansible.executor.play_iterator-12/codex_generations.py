

# Generated at 2022-06-12 21:31:12.801747
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    #
    # PlayIterator.get_host_state() returns the HostState for a Host
    #

    # Create a Play
    play = Play.load('test/ansible/test_playbooks/foobar.yml', variable_manager=VariableManager(), loader=Loader())

    # Create a Task
    task = Task()

    # Create the PlayIterator
    pi = PlayIterator()

    # Create the HostState for the localhost
    hs = HostState(host=play.hosts[0])

    #
    # Get the HostState from the PlayIterator
    #
    tmp = pi.get_host_state(play.hosts[0])
    assert tmp == hs
    assert tmp.host == hs.host
    assert tmp.run_state == hs.run_state
    assert tmp.cur_block == hs

# Generated at 2022-06-12 21:31:17.964249
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state(): 
    # Setup
    obj = PlayIterator(play=play)
    blocks = []
    state = HostState(blocks=blocks)
    
    # Check return value of get_active_state with one set of arguments
    # TODO: place actual test code here
    #assertEqual(obj.get_active_state(state), expected_result)
    

# Generated at 2022-06-12 21:31:27.504465
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    # Test with a normal task

    host = MagicMock()
    host.name = 'hostname'
    host.host_status_str = 'UNREACHABLE'
    host.get_vars.return_value = dict()
    #host.get_vars.return_value = { "oh_my": "god" }
    #host.get_vars.return_value = { "oh_my": "god", "omg": True }
    play = Play()
    iterator = PlayIterator(play)
    task = MagicMock()
    task._role = None

    # Test with a host in the failed_hosts data structure
    play._removed_hosts = ["hostname"]
    assert iterator.is_failed(host)==True

    # Test with a host not in the failed_hosts data structure
   

# Generated at 2022-06-12 21:31:40.141421
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    '''
    Ensure that the task iterator returns the next task as we expect
    '''

    # Create test collection
    loader = DataLoader()
    hosts = [Host('h1'),Host('h2')]

# Generated at 2022-06-12 21:31:42.158484
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
	"""
	PlayIterator#is_any_block_rescuing()
	"""
	pass


# Generated at 2022-06-12 21:31:49.521217
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    blocks = [Block('test')]
    state = HostState(blocks=blocks)
    assert state.run_state == PlayIterator.ITERATING_SETUP
    assert state.cur_block == 0
    assert state.cur_regular_task == 0
    assert state.cur_rescue_task == 0
    assert state.cur_always_task == 0
    assert state.tasks_child_state == None
    assert state.rescue_child_state == None
    assert state.always_child_state == None
    assert state.did_rescue == False
    # FIXME: how do we create a PlayIterator object?
    #  private constructor, no access to Play class
    # pi = PlayIterator(play=Play())
    # assert pi.get_active_state(state) == state
    # PlayIterator._insert_tasks

# Generated at 2022-06-12 21:32:00.118276
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    def _run_state_to_string(n):
        states = ["ITERATING_SETUP", "ITERATING_TASKS", "ITERATING_RESCUE", "ITERATING_ALWAYS", "ITERATING_COMPLETE"]
        try:
            return states[n]
        except IndexError:
            return "UNKNOWN STATE"

    def _failed_state_to_string(n):
        states = {1: "FAILED_SETUP", 2: "FAILED_TASKS", 4: "FAILED_RESCUE", 8: "FAILED_ALWAYS"}
        if n == 0:
            return "FAILED_NONE"
        else:
            ret = []

# Generated at 2022-06-12 21:32:05.792846
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    Unit test for method PlayIterator.mark_host_failed
    '''
    p = Play()
    p._removed_hosts = []
    itr = PlayIterator(p)
    h = Host('test', None)
    h_state = itr.get_host_state(h)
    assert h_state.run_state == itr.ITERATING_SETUP
    assert h_state.cur_block == 0
    assert h_state.cur_regular_task == 0
    assert h_state.cur_rescue_task == 0
    assert h_state.cur_always_task == 0
    assert not itr.is_failed(h)
    assert not itr._check_failed_state(h_state)
    itr.mark_host_failed(h)
    assert h_state

# Generated at 2022-06-12 21:32:17.655424
# Unit test for method __str__ of class HostState
def test_HostState___str__():
	from ansible.playbook.task import Task
	from ansible.playbook.task_include import TaskInclude
	from ansible.playbook.block import Block
	from ansible.playbook.role_include import IncludeRole
	from ansible.playbook.handler_task_include import HandlerTaskInclude
	from ansible.playbook.conditional import Conditional
	from ansible.playbook.play_context import PlayContext
	
	play_context = PlayContext()
	play_context.remote_addr = '192.168.122.1'
	play_context.remote_user = 'root'
	play_context.connection = 'ssh'
	play_context.port = 22
	play_context.become = True
	play_context.become_method = 'sudo'
	play_context.become_user

# Generated at 2022-06-12 21:32:27.626770
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    host = 'localhost'

    # create the mock Play object
    play = Play()
    play.hostvars = dict()
    play.hostvars[host] = dict()

    # create the mock Task object
    task_vars = dict(a=1,b=2,c=3)
    task = Task()
    task._role = None
    task._role_name = None
    task._parent = play
    task._block = None
    task._role_params = dict()
    task._task_vars = task_vars

    # create the PlayIterator object
    pi = PlayIterator(play=play)

    # make sure we get the right task back using the PlayIterator.get_original_task method
    assert pi.get_original_task(host, task) == (None, task_vars)

    #

# Generated at 2022-06-12 21:33:07.116144
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play_iterator = PlayIterator(play=Play().load(dict(name="test", hosts="all", tasks=[]), loader=DictDataLoader()))
    mock_state = Mock(spec=HostState)
    mock_state.run_state = PlayIterator.ITERATING_TASKS
    assert False == play_iterator._is_any_block_rescuing(mock_state)

    mock_state.tasks_child_state = Mock(spec=HostState)
    mock_state.tasks_child_state.run_state = PlayIterator.ITERATING_RESCUE
    assert True == play_iterator._is_any_block_rescuing(mock_state)

    mock_state.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
    mock_state.tasks

# Generated at 2022-06-12 21:33:12.576793
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    b = Block()
    b.task(object())
    p = Play().block(b)
    pi = PlayIterator(p)
    pi.mark_host_failed(Host("bogus"))
    failed = pi.get_failed_hosts()
    assert failed.keys() == [ 'bogus' ]
    for i in failed.items():
        assert i[1]

# Generated at 2022-06-12 21:33:23.731405
# Unit test for method get_next_task_for_host of class PlayIterator

# Generated at 2022-06-12 21:33:31.859141
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    host_state = HostState([Block(None, [Task()])])
    host_state.fail_state = PlayIterator.FAILED_SETUP
    host_state.run_state = PlayIterator.ITERATING_TASKS
    assert str(host_state) == 'HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_TASKS, fail_state=FAILED_SETUP, pending_setup=False, tasks child state? (None), rescue child state? (None), always child state? (None), did rescue? False, did start at task? False'


# Generated at 2022-06-12 21:33:33.952857
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    my_iterator = PlayIterator(iter([], []));
    assert my_iterator.get_original_task(None, None) == (None, None)

# Generated at 2022-06-12 21:33:45.567424
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    '''
    Test the method is_any_block_rescuing of class PlayIterator
    '''

# Generated at 2022-06-12 21:33:50.404900
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    iterator = PlayIterator()
    state = HostState()
    state.run_state = PlayIterator.ITERATING_COMPLETE
    state.fail_state = PlayIterator.FAILED_TASKS
    assert iterator.is_failed(state)



# Generated at 2022-06-12 21:33:57.905293
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    play = Play()
    play.hosts = ('foo', 'bar', 'baz')
    iterator = PlayIterator(play=play, play_context=PlayContext())
    iterator.mark_host_failed('foo')
    assert iterator.get_failed_hosts() == dict({'foo': True})


    iterator._host_states['bar'] = HostState(None)
    iterator._host_states['bar'].fail_state = HostState.FAILED_SETUP
    assert iterator.get_failed_hosts() == dict({'foo': True, 'bar': True})


    iterator._host_states['baz'] = HostState(None)
    iterator._host_states['baz'].fail_state = HostState.FAILED_SETUP | HostState.FAILED_RESCUE
    assert iterator.get_

# Generated at 2022-06-12 21:34:08.784962
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''
    Unit test for method cache_block_tasks of class PlayIterator
    '''
    print("Test PlayIterator - cache_block_tasks")

    block_nested_1 = Block()
    block_nested_1.block = [10,11,12]
    block_nested_1.rescue = [13]
    block_nested_1.always = [14]

    block_nested_2 = Block()
    block_nested_2.block = [20,21]
    block_nested_2.rescue = [22]
    block_nested_2.always = [23]

    block_nested_3 = Block()
    block_nested_3.block = [30,31,32]
    block_nested_3.rescue = [33]
    block

# Generated at 2022-06-12 21:34:09.447945
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    pass


# Generated at 2022-06-12 21:35:09.461439
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    host = Host('localhost')
    play = Play()
    iterator = PlayIterator(play)
    state = HostState(blocks=[])
    state.run_state = PlayIterator.ITERATING_TASKS
    state.cur_block = 0
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state._blocks = [Block(
        block = [
            Task(action='test1', args={}),
            Task(action='test2', args={}),
            Task(action='test3', args={}),
        ],
    )]

    iterator._host_states[host.name] = state

# Generated at 2022-06-12 21:35:10.018203
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    pass

# Generated at 2022-06-12 21:35:16.092408
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    Test that PlayIterator.get_failed_hosts finds the expected hosts if they failed during
    setup tasks
    '''

# Generated at 2022-06-12 21:35:26.970448
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    p = Play()
    p.name = "test"
    p.hosts = ['dummy1', 'dummy2']
    i = PlayIterator(p)

    # This test code presents a case where there are three blocks in the play.
    # The blocks are:
    #
    # block 1
    #     task 1a
    #     task 1b
    #     task 1c
    #
    # block 2
    #     task 2a
    #     task 2b
    #     task 2c
    #
    # block 3
    #     task 3a
    #     task 3b
    #     task 3c

    # It then performs the following operations:
    #
    # 1. runs task 1a
    # 2. starts running task 1b
    #    - interrupts task 1b to run block 1a


# Generated at 2022-06-12 21:35:39.521522
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    '''
    Test is_any_block_rescuing method of PlayIterator
    '''
    # create a play to iterate over
    play = Play.load(dict(
        name = 'foobar',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), loader=DummyLoader())

    # create a play iterator to work with
    pi = PlayIterator()
    pi._play = play

    state = HostState(blocks=play.compile())

    # test case with state in setup state
    state.run_state = pi.ITERATING_SETUP


# Generated at 2022-06-12 21:35:50.598832
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():

    # play iterator type is used as a base class
    class __PlayIterator(PlayIterator):

        def __init__(self):
            self._play = Mock(Play)
            self._play._play_context = Mock(PlayContext)
            self._play._play_context.become = False
            self._play._play_context.become_method = None

            self._host_states = {}
            display.verbosity = 3
            self._tqm = None
            self._last_task_banner = None

    # host type is used to instantiate the Host object
    class __Host(object):

        def __init__(self):
            self.name = 'test_play_iterator_host'

    # module type is used to instantiate AnsibleModule objects that are returned when instantiating the Task object

# Generated at 2022-06-12 21:36:01.140727
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    play = Play()
    play.name = "test play"
    play.hosts = 'localhost'
    play.vars = {}
    play.vars_prompt = {}
    play.handlers = []
    play.tasks = []
    play.tags = []
    play.role_names = []
    play.default_vars = {}
    play.dep_chain = []
    play.blocks = []
    play.batch = 0

    inventory = Inventory()
    inventory.set_variable("foo", "bar")
    inventory.set_variable("ansible_ssh_host", "127.0.0.1")
    inventory.set_variable("nested", {"a": "b"})

    host = Host()
    host.name = 'localhost'
    host.vars = {}

# Generated at 2022-06-12 21:36:04.495153
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    my_play_iterator = PlayIterator()
    my_play_iterator._host_states = {'some host': 'some state'}
    assert my_play_iterator.get_host_state('some host') == 'some state'
    

# Generated at 2022-06-12 21:36:11.436399
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():

    class FakeHost:
        def __init__(self, name):
            self.name = name

    class FakeScheduler:
        def __init__(self):
            self.queue         = list()
        def next_to_run(self):
            return self.queue.pop(0)
        def schedule(self, host, task):
            self.queue.append((host, task))
    #
    # There are 5 test cases:
    #   1. only tasks are run, no failures
    #   2. only setup is run, no failures
    #   3. setup and tasks are run, no failures
    #   4. setup, tasks and handlers are run, no failures
    #   5. Each of 1-4 with failures
    # These are simulated by the following:
    #   1. fake_host_check_compiled

# Generated at 2022-06-12 21:36:19.685413
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # Test get_failed_hosts when there is no failure
    play = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())
    iterator = PlayIterator(play)
    assert iterator.get_failed_hosts() == dict()
    # Test get_failed_hosts when there is a failure

# Generated at 2022-06-12 21:38:27.306436
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
	
	# Dummy classes for testing purposes
	class MockPlay(object):
		def __init__(self, name=''):
			self.name = name

	class MockHost(object):
		def __init__(self, name=''):
			self.name = name

	class MockTask(object):
		def __init__(self, name=''):
			self.name = name

	# Setting inputs
	pi = PlayIterator()
	pi._play = MockPlay()
	pi._host_states = dict()
	host = MockHost()
	host.name = 'localhost'
	task_list = [MockTask(), MockTask()]
	for i in range(len(task_list)):
		task_list[i].name = 'Task ' + str(i)


# Generated at 2022-06-12 21:38:29.344486
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    play_iterator = PlayIterator()
    assert play_iterator.get_next_task_for_host('test_host') == None

# Generated at 2022-06-12 21:38:38.719403
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    mock_play = unittest.mock.MagicMock()
    mock_play._included_roles = []
    mock_play._included_file_includes = []
    mock_play.get_vars = dict()
    mock_host = unittest.mock.MagicMock()
    mock_host.name = 'localhost'
    mock_block = unittest.mock.MagicMock()
    mock_block.filters = dict()
    mock_block.rescue.return_value = False
    mock_block.always.return_value = False
    mock_block.role = None
    mock_block.block = [unittest.mock.MagicMock()]
    mock_block.rescue = []
    mock_block.always = []
    mock_iterator = PlayIterator.PlayIterator

# Generated at 2022-06-12 21:38:46.468733
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    play = Play.load(dict(
        name = "test play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [ dict(action=dict(module='shell', args='ls'), register='shell_out'),
                  dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))) ]
    ))

    play_context = PlayContext(play=play)
    inventory = Inventory(loader=None)
    inventory.hosts = dict((h, None) for h in play.hosts)
    runner = PlayIterator(inventory=inventory, play=play, play_context=play_context)

    host = play.hosts[0]
    host_state = runner._get_host_state(host)
    host_state.cur_block = 1


# Generated at 2022-06-12 21:38:56.487584
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    # create a task list
    my_task_list = [
        dict(
            action=dict(
                module='command',
                args=dict(
                    cmd='echo 123',
                )
            ),
            name='task 1'
        )
    ]
    # Create a PlayIterator
    my_iterator = PlayIterator('my_iterator',None,None,None,None,None)
    # Create a HostState
    my_host_state = HostState(blocks=[])
    # Initialize the HostState
    my_host_state.run_state = PlayIterator.ITERATING_TASKS
    my_host_state.fail_state = PlayIterator.FAILED_NONE
    my_host_state._blocks = []

# Generated at 2022-06-12 21:39:06.730301
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    PlayIterator.is_failed
    '''
    
    # From test/units/test_playiterator.py:306
    
    # Setup
    mock_host = Host()
    mock_host.name = 'foo'
    mock_play_context = MagicMock()
    
    # Test with no failed states
    pi = PlayIterator()
    pi._play = Play()
    pi.get_host_state(mock_host)
    assert pi.is_failed('foo') == False
    
    # Test with task failed state
    pi = PlayIterator()
    pi._play = Play()
    pi._host_states['foo'] = HostState(blocks=[Block()])
    pi._host_states['foo'].fail_state = pi.FAILED_TASKS
    assert pi.is_failed

# Generated at 2022-06-12 21:39:15.991256
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    
    playbook = Playbook()
    
    play = Play()
    
    host = Host("testhost")
    host.set_variable("state", "ok")
    host.set_variable("failed_when_result", False)
    
    play.add_host(host)
    
    playbook.add_play(play)
    
    inventory = Inventory()
    inventory.add_host(host)
    
    runner = PlayIterator(playbook)
    
    runner.get_failed_hosts()
    fail_result = runner.get_failed_hosts()

    assert fail_result['testhost'] == False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-12 21:39:27.486812
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    '''
    Test the get_active_state method of PlayIterator.
    '''
    def test_get_active_state(s, expected_result, child_state=None, child_child_state=None):
        result = PlayIterator(play=None).get_active_state(s)
        assert result == expected_result, 'get_active_state(%s) expected %s, got %s' % (s, expected_result, result)

    s = HostState(blocks=[])
    s.run_state = PlayIterator.ITERATING_SETUP
    test_get_active_state(s, s)

    s = HostState(blocks=[])
    s.run_state = PlayIterator.ITERATING_TASKS
    test_get_active_state(s, s)


# Generated at 2022-06-12 21:39:34.845458
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    play = Play()
    play.post_validate()
    inventory = Inventory(host_list=[])
    play.hosts = inventory.get_hosts()
    play.vars = dict()
    play.vars_prompt = dict()
    play.default_vars = dict()
    # PlayIterator constructor with different argument types and numbers
    pi = PlayIterator()
    pi = PlayIterator(inventory=inventory)
    pi = PlayIterator(play=play)
    pi = PlayIterator(play=play, inventory=inventory)
    pi = PlayIterator(play=play, inventory=inventory, variable_manager=None)
    pi = PlayIterator(play=play, inventory=inventory, variable_manager=VariableManager(loader=None, inventory=inventory), all_vars=dict())

# Generated at 2022-06-12 21:39:36.464920
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    '''
    None
    '''
    pass
