

# Generated at 2022-06-12 21:31:03.229896
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    play = Play()
    inventory = Inventory()

    host1 = Host('testhost')
    host2 = Host('testhost2')
    host3 = Host('testhost3')
    host4 = Host('testhost4')

    play.hosts = [host1, host2, host3, host4]

    inventory.add_host(host1)
    inventory.add_host(host2)
    inventory.add_host(host3)
    inventory.add_host(host4)


# Generated at 2022-06-12 21:31:13.179834
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    display.quiet = True

    display.verbosity = 3
    itr = PlayIterator()
    itr.load_hosts_file()
    itr.load_playbook_file('./test/test_playbooks/playbook_test.yml', inventory_manager=itr.inventory)
    itr.playbook._included_files = ['./test/test_playbooks/playbook_test.yml']
    inventory = itr.inventory

    default_host = inventory.get_host("host1")
    dummy_host = DummyHost(inventory)
    dummy_host.name = 'dummy'
    dummy_host.bound_vars = default_host.vars
    inventory._hosts['dummy'] = dummy_host

    # Test single host, empty blocks

# Generated at 2022-06-12 21:31:24.215887
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    Unit test for method get_failed_hosts of class PlayIterator
    '''

    # Setup the objects needed to test the method get_failed_hosts.
    # Create the class under test
    pitr = PlayIterator()
    # Create a play without a name
    play = Play()
    pitr._play = play
    # Create a task with a name
    task = Task()

    # The method get_failed_hosts should return an empty dict
    # since the play is empty.
    assert pitr.get_failed_hosts() == dict()

    # Add a host to the play and assign a task
    play._tqm.get_host("host1").set_play(play)
    play._tqm.get_host("host1")._tasklist = [task]

    # Now the method get

# Generated at 2022-06-12 21:31:24.872673
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
  pass

# Generated at 2022-06-12 21:31:25.725414
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    pass

# Generated at 2022-06-12 21:31:26.418638
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    pass

# Generated at 2022-06-12 21:31:35.200875
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    host = MagicMock()
    host.name = 'test_host'
    pi = PlayIterator(play=[], play_context=None, variable_manager=MagicMock(), loader=MagicMock())
    s = HostState(blocks=[])
    s.run_state = PlayIterator.ITERATING_COMPLETE
    s.fail_state = PlayIterator.FAILED_NONE
    pi._host_states[host.name] = s
    assert pi.is_failed(host) is False


# Generated at 2022-06-12 21:31:39.078182
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    play = Play().load(load_fixture('async_wrapper'), variable_manager=VariableManager(), loader=loader)
    play_itr = PlayIterator(play)
    play_itr.get_original_task()

# Generated at 2022-06-12 21:31:47.924673
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.hostvars import HostVars


# Generated at 2022-06-12 21:31:48.876440
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    pass


# Generated at 2022-06-12 21:32:26.710570
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    p = Play()
    i = PlayIterator(p)
    h = Host("localhost")
    b = Block().load("""
    - block:
        - foobar:
            action: mymodule
            module: mod
        - block:
            - foobar:
                action: anothermod
                module: mod2
        - foobar:
            action: eep
            module: mod
    """, p, loader=BaseLoader())
    s = HostState(blocks=[b])

    # first find the task we want to test
    while True:
        (s, t) = i._get_next_task_from_state(s, host=h)
        if t:
            break

    # then test the method
    assert i.is_any_block_rescuing(s) == False

    # now try it again,

# Generated at 2022-06-12 21:32:38.838778
# Unit test for method copy of class HostState
def test_HostState_copy():
    class Block:
        def __init__(self):
            self.rescue = False
            self.always = False
            self.block  = []

    blockA = Block()
    blockA.rescue = False
    blockA.always = False
    blockA.block = [0, 1, 2]

    blockB = Block()
    blockB.rescue = True
    blockB.always = False
    blockB.block = [3, 4, 5]

    blockC = Block()
    blockC.rescue = False
    blockC.always = True
    blockC.block = [6, 7, 8]

    blocks = [blockA, blockB, blockC]
    host = HostState(blocks)
    host_copy = host.copy()

    assert isinstance(host_copy, HostState)

# Generated at 2022-06-12 21:32:47.096928
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    host = Mock(name='host')
    tasks = [Mock(name='task1'), Mock(name='task2')]
    state = Mock(name='state')
    state.run_state = PlayIterator.ITERATING_TASKS
    state._blocks = [Mock(name='block')]
    state.cur_block = 0
    state.cur_regular_task = 0
    state.tasks_child_state = None
    state.fail_state = PlayIterator.FAILED_NONE
    iterator = PlayIterator()
    iterator._get_next_task_from_state = Mock(name='_get_next_task_from_state')

# Generated at 2022-06-12 21:32:55.048380
# Unit test for constructor of class PlayIterator
def test_PlayIterator():

    # Test the iterator first
    play_src = dict(
        name = "test play",
        hosts = 'webservers',
        gather_facts = 'no',
        vars = dict(
            a = 1,
            b = 2,
            c = 3,
        ),
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
        ]
    )

    def _create_task(module_name, args):
        task = Task()
        block = Block()
        task.action = Action(block, module_name, args)
        return task

    # Create a play based on play_src

# Generated at 2022-06-12 21:32:57.269234
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play_iterator = PlayIterator()
    assert play_iterator.get_host_state('host') == None

# Generated at 2022-06-12 21:33:08.555235
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host

    host = Host(name="testhost")
    block1 = Block()
    block2 = Block()

    t1 = Task()
    t1._uuid = "11111111111111111111111111111111"
    t2 = Task()
    t2._uuid = "22222222222222222222222222222222"
    t3 = Task()
    t3._uuid = "33333333333333333333333333333333"
    t4 = Task()
    t4._uuid = "44444444444444444444444444444444"

# Generated at 2022-06-12 21:33:11.836871
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    PlayIterator.is_failed
    '''
    iterator = PlayIterator()
    setattr(iterator._failed_hosts, "__contains__", lambda x: True)
    assert iterator.is_failed("127.0.0.1")

# Generated at 2022-06-12 21:33:23.242169
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    foo = Play()

    host_states = {}

    host_1 = FakeHost('host_1')
    host_2 = FakeHost('host_2')

    role_1 = FakeRole('role_1')
    role_2 = FakeRole('role_2')

    hosts = [host_1, host_2]
    roles = [role_1, role_2]

    task_1_1 = FakeTask('task_1_1')
    task_1_2 = FakeTask('task_1_2')
    task_1_3 = FakeTask('task_1_3')
    task_2_1 = FakeTask('task_2_1')
    task_2_2 = FakeTask('task_2_2')

    block_1 = Block(['tasks'])

# Generated at 2022-06-12 21:33:28.681051
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
  from ansible.playbook import Playbook

  def tests(dummy):
    # set up some test data
    play = Play().load_from_file()
    # play.handlers = [{'name': 'first'}, {'name': 'second'}]
    play.handlers = play.compile_roles_handlers()

# Generated at 2022-06-12 21:33:37.402092
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play().load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = dict(
            name = "test task",
            debug = dict(
                msg = "test msg"
            )
        )
    ), variable_manager=VariableManager(), loader=None)

    iterator = PlayIterator(play)

    host = Host(name='test_host')
    host.set_variable('test_var', 'testval')

    assert iterator.get_host_state(host) is None

    task = Task().load(dict(
        name = "test task",
        debug = dict(
            msg = "test msg"
        )
    ), play=play)

    iterator.get_next_task_for_host(host, peek=True)

    assert len

# Generated at 2022-06-12 21:34:43.385422
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    p = Play().load({
        'name' : "test play",
        'hosts': 'test_hosts',
        'tasks': [
            { 'action': 'shell', 'args': "echo hi" },
            { 'action': 'shell', 'args': "echo hi2" }
        ]
    }, variable_manager=dict(), loader=None)

    h = Host(name="test_host")
    h.groups = [ Group(name="test_hosts") ]
    g = Group(name="test_hosts")
   

# Generated at 2022-06-12 21:34:53.706123
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    pa_mock = Mock()
    play_mock = Mock()
    play_mock._context = dict(play=play_mock)
    play_mock._play_context = Mock()
    play_mock._fqcn = 'ansible.playbook.play.Play'
    play_mock._id = 1
    play_mock.hosts = ['localhost']
    play_mock.tasks = [Task.load(dict(action='action', args=dict(x=1)), parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None)]
    play_mock.post_validate = Mock()

    block_mock = Mock()


# Generated at 2022-06-12 21:35:02.379093
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''
    Ensure the cache_block_tasks returns the right thing
      1. no data dir
      2. data dir without cache file
      3. data dir with valid cache file
      4. data dir with invalid cache file
    '''
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host

    # set up some mock data
    myplay = Play()
    myplay.hosts = ['localhost']
    myblock = Block()
    myblock.block = [Task()]
    myplay.block = [myblock]

    # data dir doesn't exist
    host = Host('localhost')
    play_iterator = PlayIterator(myplay, host=host)
    play_iterator._load_

# Generated at 2022-06-12 21:35:09.818159
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    '''
    This unit test validates that the get_original_task method of class PlayIterator
    returns the original task given a task from a different host.
    This is used when the action plugin delegate_to is used to execute actions
    on a different host.
    '''
    test_host = Host(name='test_host')
    test_host.vars = dict()
    test_host.groups = []
    test_host.vars['ansible_connection'] = 'local'
    test_host.vars['ansible_python_interpreter'] = '/usr/bin/python'
    test_host.vars['ansible_ssh_common_args'] = '-F /dev/null'
    test_host.vars['ansible_ssh_host_key_checking'] = False
    test_host.vars

# Generated at 2022-06-12 21:35:10.671088
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    assert True == False

# Generated at 2022-06-12 21:35:12.697740
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    play = Play()
    play.post_validate(Mock())
    play.compile()

    # We simply test here that the constructor is not throwing any exceptions
    p = PlayIterator(play)

# Generated at 2022-06-12 21:35:20.122765
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
  host = MockHost()
  iterator = PlayIterator(
      play=MockPlay(),
      inventory=MockInventory(host),
      loader=MockLoader(),
      variable_manager=MockVariableManager(),
      all_vars={},
  )
  _ = iterator._task_cache

  # test with no arguments
  iterator.cache_block_tasks(None)
  if isinstance(iterator._task_cache, dict):
    return
  raise AssertionError("Failed to assert that dict is dict")


# Generated at 2022-06-12 21:35:29.328033
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():

    play = Play().load('test/playbooks/playiterator_get_active_state.yml', variable_manager=VariableManager())
    play.post_validate(play.basedir)

    iterator = PlayIterator(play)

    # test that when a block has a rescue section, it will return the rescue block once the
    # regular block is finished
    host = Host(name='127.0.0.1')
    is_done = False
    block = None
    rescue_block = None
    state = iterator.get_next_task_for_host(host, peek=True)

# Generated at 2022-06-12 21:35:41.480296
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():

    display.verbosity = 3
    options = Options()
    loader = DataLoader()
    inventory = Inventory(loader, sources=['localhost,'])
    play_source =  dict(
            name = "Test play",
            hosts = 'all',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='setup', args='')),
                dict(action=dict(module='debug', args=dict(msg='hello world')))
            ]
        )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=loader)
    tqm = None
    p = PlayIterator(inventory, play, tqm, options)

    for host in inventory.get_hosts():
        print(p.get_next_task_for_host(host))

#
# Unit

# Generated at 2022-06-12 21:35:52.373466
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    hs = HostState(blocks=[Block().load({'name': 'test block', 'hosts': 'localhost', 'tasks': [{'action': {'module': 'foo'}}]}),
                           Block().load({'name': 'test block 2', 'hosts': 'localhost', 'rescue': [{'action': {'module': 'foo'}}]}),
                           Block().load({'name': 'test block 3', 'hosts': 'localhost', 'always': [{'action': {'module': 'foo'}}]}),])
    hs.run_state = PlayIterator.ITERATING_TASKS
    hs.cur_block = 0
    hs.fail_state = PlayIterator.FAILED_NONE
    hs.tasks_child_state = None
    hs.rescue_child_state

# Generated at 2022-06-12 21:37:50.832082
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
  host = "host_name"
  iterator = PlayIterator()
  iterator.play = Mock()
  iterator._play_forks = {
    0: 2,
    1: 4,
    2: 7,
    3: 0,
    }
  result = iterator.get_host_state( host )
  assert len(result._blocks) == 2


# Generated at 2022-06-12 21:37:57.936304
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    pl = Play().load(dict(
        hosts='all',
        tasks=[
            dict(action=dict(module='command', args='echo hi')),
        ]
    ), loader=Mock())
    batch = pl.get_iterator()
    host = Host(name='test_host')
    assert not batch.is_any_block_rescuing(batch.get_host_state(host))

# Generated at 2022-06-12 21:38:07.010652
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    '''
    Play:
    - block:
      - action: fail
        fail_msg: Test Fail
    - block:
      - action: ok
        ok_msg: Test OK
    '''
    play_context = FakePlayContext()

# Generated at 2022-06-12 21:38:14.437075
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    from ansible.playbook import Play, Playbook
    from ansible.inventory import Inventory, Host, Group

    # create a simple inventory
    inventory = Inventory(host_list=[])

    # create a simple play
    play = Play()
    play.name = "all"
    play.hosts = "all"
    play.gather_facts = "no"
    play.serial = 1
    play.any_errors_fatal = True
    play.roles = []

    # create a simple play
    pb = Playbook()
    pb.set_plays(dict(pb=[play]))

    play_iter = PlayIterator(pb)
    assert play_iter.num_hosts() == 0

    # create a simple inventory
    inventory = Inventory(host_list=[])
    inventory.subset('all')
   

# Generated at 2022-06-12 21:38:24.672451
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():

    # The PlayIterator class is a bit complicated, and we're not trying to
    # have 100% coverage here. We'll just ensure that the two codepaths
    # which are mostly likely to be executed (getting a task, and marking
    # a host as failed) work.

    # a fake Host to use in the tests below
    class FakeHost(object):
        pass

    # a fake PlayContext to use in the tests below
    class FakePlayContext(object):
        pass

    # a fake Task to use in the tests below
    class FakeTask(object):
        def __init__(self, name):
            self.name = name

    # a fake PlayObject to use in the tests below
    class FakePlayObject(object):
        def __init__(self):
            self.vars = dict()

    # the first thing we need is a

# Generated at 2022-06-12 21:38:33.739033
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
  loader = DataLoader()
  variable_manager = VariableManager()
  variable_manager.set_loader(loader)
  variable_manager.set_inventory(Inventory(loader=self.loader, variable_manager=self.variable_manager, host_list=['localhost']))

  def test_play_1():
    yield {
      'hosts': 'localhost',
      'name': 'test_task',
      'gather_facts': 'no'
    }
    yield {
      'name': 'setup',
      'gather_facts': 'no'
    }
    yield {
      'name': 'test_semantic_task',
      'gather_facts': 'no', 'when': False
    }

# Generated at 2022-06-12 21:38:43.051405
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    play = Play('name', dict(
        role = 'test',
        become = True,
        gather_facts = 'no',
        connection = 'ssh'
    ))

    task = Task.load(dict(
        action = 'test1',
        loop = 'test2'
    ))

    play.add_task(task)
    host = Host('testhost')
    # the host setup will happen here automatically
    task = Task.load(dict(
        action = 'test3'
    ))
    play.add_task(task)
    iterator = PlayIterator(play)
    host_state = iterator.get_next_task_for_host(host)
    assert host_state == (None, task)

    task = Task.load(dict(
        action = 'test4'
    ))
    play.add_task

# Generated at 2022-06-12 21:38:54.597295
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    class Task(object):
        name = 'test task'

    class Block(object):
        def __init__(self, block):
            self.block = block

# Generated at 2022-06-12 21:39:00.367359
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    host, task = object(), object()
    play_iterator = PlayIterator(object())
    play_iterator._hosts_cache = dict()
    play_iterator._hosts_cache[host] = dict()
    play = object()
    play_iterator._hosts_cache[host][task] = (play, task)
    assert (play_iterator.get_original_task(host, task) == (play, task))


# Generated at 2022-06-12 21:39:01.055246
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    assert True is True