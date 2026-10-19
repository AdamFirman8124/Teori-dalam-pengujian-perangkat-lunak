

# Generated at 2022-06-12 21:30:42.004314
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    host = Host('testhost')
    host.vars = dict(
        test_var='test1',
    )
    play = Play().load(dict(
        name='test play',
        hosts=['testhost'],
        gather_facts='no',
        tasks=[
            dict(action=dict(module='debug', args=dict(
                msg='test task',
            ))),
        ],
    ), variable_manager=VariableManager(), loader=MockLoader())
    pi = PlayIterator()
    pi._play = play
    pi._hosts = [host]
    pi._host_states = dict(
        testhost=HostState(blocks=[play._entries[0]]),
    )
    result = pi.get_host_state(host)

# Generated at 2022-06-12 21:30:48.816822
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    host = Host('localhost')
    play = Play().load(dict(
                name = "test play",
                hosts = 'all',
                gather_facts = 'no',
                tasks = [
                    dict(action=dict(module='debug', args=dict(msg='ok'))),
                ]
            ), loader=DictDataLoader())
    inventory = Inventory(loader=InventoryLoader())
    inventory.add_host(host)
    iterator = PlayIterator()
    iterator._play = play
    iterator._play._hosts = ['localhost']
    iterator._play._need_static_facts = True
    iterator.inventory = inventory
    result = iterator.get_next_task_for_host(host)
    assert result[0].run_state == iterator.ITERATING_TASKS


# Generated at 2022-06-12 21:30:59.508851
# Unit test for method __eq__ of class HostState
def test_HostState___eq__():
    b1 = Block()
    b1.name = "test"
    b2 = Block()
    b2.name = "test2"
    b3 = Block()
    b3.name = "test3"
    b4 = Block()
    b4.name = "test4"

    play = Play()
    play.handlers = [b1]
    play.tasks = [b2]
    play.rescue = [b3]
    play.always = [b4]

    hs1 = HostState(play.get_blocks())
    # Inspect the attribute of hs1 and modify
    hs1.get_current_block().name = "changed"
    hs1.cur_block = 1
    hs1.cur_regular_task = 2

# Generated at 2022-06-12 21:31:11.221822
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
  from ansible.playbook.play import Play
  from ansible.playbook.task import Task
  from ansible.playbook.block import Block
  from ansible.inventory.host import Host

  h = Host(name="test_host")
  t1 = Task()
  t2 = Task()
  b = Block(block=[t1, t2])
  p = Play()
  p.hosts.append(h)
  p.hosts.append(Host(name="test_host2"))
  p.hosts.append(Host(name="test_host3"))
  p.hosts.append(Host(name="test_host4"))
  p.blocks.append(b)
  p.blocks.append(b)
  pit = PlayIterator(p)
  pit.get_next_task_for_host

# Generated at 2022-06-12 21:31:22.565357
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
   # Testing submethods is nasty, but here we go
   pi = PlayIterator()
   pi._play = Play()
   b = Block()
   b._role = Role()
   pi._play._roles = set([b])
   pi.cache_block_tasks()
   assert isinstance(pi._block_task_cache, dict), "cache was not initialized as a dict"
   assert len(pi._block_task_cache) == 1 and pi._block_task_cache.keys()[0] == b, "cache did not contain expected block"
   assert pi._block_task_cache[b] == [], "expected empty list, got: %r" % pi._block_task_cache[b]

   b.block = [Task()]
   pi.cache_block_tasks()

# Generated at 2022-06-12 21:31:29.503721
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    host = MagicMock()
    host.name = 'testhost'
    host.vars = dict()
    task = MagicMock()
    task.get_action_args.return_value = {}
    task.serialize.return_value = {'test': True}
    task.copy.return_value = task
    task.action = 'testaction'
    play = MagicMock()
    play.name = 'testplay'
    play.attributes = dict()
    play.vars = dict()
    play.vars['test_var'] = 'test_value'
    play_iterator = PlayIterator(play=play)
    play_iterator.play = play
    play_iterator.play.iterator = play_iterator
    play_iterator.play.hosts = [host]
    play_iterator._play = play


# Generated at 2022-06-12 21:31:36.922777
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # Setup
    p = Play()
    i = PlayIterator(p)

    # Test symptoms
    host = Host('test_host')
    i.mark_host_failed(host)
    output = i.get_failed_hosts()
    assert output == {'test_host': True}, '''PlayIterator.get_failed_hosts produced unexpected output with input ({}).'''.format('')


# Generated at 2022-06-12 21:31:46.495968
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    play = Play().load(dict(name='test', hosts='all', gather_facts='no', tasks=[dict(action='shell', args='foo'), dict(action='shell', args='bar')]), loader=None, variable_manager=VariableManager())
    hostvars = {'foo': 'bar', 'somevar': 'somevalue'}

    iterator = PlayIterator()
    iterator.play = play
    iterator.play_context = PlayContext()
    iterator.play_context.variable_manager = VariableManager()
    iterator.play_context.variable_manager.set_host_variable('testhost', hostvars)
    iterator.set_hosts('testhost')
    iterator.host_states = {'testhost': HostState()}
    iterator.host_states['testhost'].cur_block = 0

# Generated at 2022-06-12 21:31:53.782552
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    '''
    Ensure that the state returned by is_any_block_rescuing is expected
    '''
    play_source =  dict(
        name = "foobar",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')), when='shell_out.rc == 0'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stderr}}')), when='shell_out.rc != 0', rescue=[]),
            dict(action=dict(module='debug', args=dict(msg='always'))),
        ]
    )


# Generated at 2022-06-12 21:31:57.634234
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    Ensure we properly mark modules as failed in the PlayIterator class
    '''
    #######################################################################
    # 
    # 
    #######################################################################
    p = hosts.Host('127.0.0.1')
    iter = PlayIterator()
    iter.get_next_task_for_host(p)
    iter.mark_host_failed(p)
    assert iter.is_failed(p) == True


# Generated at 2022-06-12 21:32:54.035493
# Unit test for method cache_block_tasks of class PlayIterator

# Generated at 2022-06-12 21:33:06.346688
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    Unit test for method is_failed of class PlayIterator
    '''
    iterator = PlayIterator()
    host = Mock()
    host.name = 'host'
    block = Block(task_include='task', rescue='rescue', always='always')
    iterator._host_states[host.name] = HostState(blocks=[block])
    host_state = iterator._host_states[host.name]
    host_state.cur_block = 0
    host_state.run_state = iterator.ITERATING_TASKS
    host_state.fail_state = iterator.FAILED_TASKS
    assert iterator.is_failed(host) == True

    host_state.fail_state = iterator.FAILED_NONE
    host_state.run_state = iterator.ITERATING_TASKS


# Generated at 2022-06-12 21:33:13.265109
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    host = Host(name='fake_host')
    block = Block(None, None, None, None)
    assert PlayIterator._cache_block_tasks(host, block, []) == ([], {})
    assert PlayIterator._cache_block_tasks(host, block, [1, 2, 3, 4]) == ([1, 2, 3, 4], {'fake_host': {}})
    task = Task()
    task._role = 'role1'
    task2 = Task()
    task2._role = 'role2'
    assert PlayIterator._cache_block_tasks(host, block, [task, task2]) == ([task, task2], {'fake_host': {'role1': task, 'role2': task2}})

# Generated at 2022-06-12 21:33:17.036833
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    p = Play()
    p._tqm = None
    pi = PlayIterator(p)
    p._iterator = pi
    pi._play = p
    assert pi.play == p
    assert pi._play == p
    assert not pi._play._iterator


# Generated at 2022-06-12 21:33:28.404229
# Unit test for method get_failed_hosts of class PlayIterator

# Generated at 2022-06-12 21:33:29.474313
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    obj = PlayIterator()
    assert obj is not None

# Generated at 2022-06-12 21:33:31.245015
# Unit test for method copy of class HostState
def test_HostState_copy():
    state = HostState([])
    new_state = state.copy()
    assert new_state != state


# Generated at 2022-06-12 21:33:40.274185
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    # Method cache_block_tasks of class PlayIterator
    #
    # Configuration:
    # No all_vars, no templar, no all_group_vars
    # one host, no var setup
    # no connection
    #
    # Tested:
    # - check caching of tasks (including block)
    # - check caching of results
    # - ensure connection and templar are not used

    # test caching of tasks with block:
    iterator = PlayIterator()

# Generated at 2022-06-12 21:33:52.807826
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play = Play().load(dict(
        name = "foo",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='1st task'))),
            dict(action=dict(module='debug', args=dict(msg='2nd task'))),
            dict(action=dict(module='debug', args=dict(msg='3rd task'))),
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())

    play_iterator = PlayIterator(play)
    play_iterator.next()
    play_iterator.next()
    play_iterator.next()
    play_iterator.next()

    play_iterator.mark_host_failed(play.hosts[0])


# Generated at 2022-06-12 21:33:59.976472
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play()
    play._play_hosts = dict((x, True) for x in 'abcdefgh')
    myplay = PlayIterator(play)
    task1 = Task()
    task1._uuid = 'first'
    task2 = Task()
    task2._uuid = 'second'
    task3 = Task()
    task3._uuid = 'third'
    task4 = Task()
    task4._uuid = 'fourth'
    block = Block()
    block.block = [task1, task2, task3, task4]
    myplay._play_blocks[0] = block

    for host in play._play_hosts:
        myplay.get_host_state(host = Host(name = host))


# Generated at 2022-06-12 21:34:30.396439
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    h = AnsibleHost('localhost')
    s = PlayIterator()
    s.get_active_state(h)

test_PlayIterator_get_active_state()


# Generated at 2022-06-12 21:34:33.904832
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
	obj = PlayIterator()

# Generated at 2022-06-12 21:34:36.174222
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # not sure how to test this yet, since it's not realistic to create a HostState
    # to test it with.  It's also not really an Ansible public API.

    pass


# Generated at 2022-06-12 21:34:46.430412
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    # Create two plays
    play1 = Play()
    play2 = Play()
    # Create two host lists
    host1 = []
    host2 = [Host(), Host(), Host(), Host()]
    # Create play iterator objects
    test_play_iter1 = PlayIterator(play1, host1)
    test_play_iter2 = PlayIterator(play2, host2)
    # Verify that get_play method returns appropriate play object
    assert(test_play_iter1.get_play() == play1)
    assert(test_play_iter2.get_play() == play2)
    # Verify that get_play_hosts method returns appropriate host list
    assert(test_play_iter1.get_play_hosts() == host1)

# Generated at 2022-06-12 21:34:56.956473
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    Test if is_failed() correctly detects if host has failed
    '''
    play = Play().load(dict(
        name = 'test play',
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='ok'))),
            dict(action=dict(module='debug', args=dict(msg='not ok'))),
            dict(action=dict(module='debug', args=dict(msg='ok'))),
            dict(action=dict(module='debug', args=dict(msg='ok'))),
        ]
    ), variable_manager=VariableManager())

    play_context = PlayContext()
    play_context.become = False

    iterator = PlayIterator(play, play_context)
    iterator._host

# Generated at 2022-06-12 21:35:04.641236
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    # Setup test
    playbook =[dict(
        hosts='webservers',
        vars=dict(
            http_port=80,
            maxRequestsPerChild=200,
        ),

        tasks=[
            dict(action=dict(module='apache', args='name=foo state=present'), register='webvars'),
        ]
    )]
    play = Play().load(playbook[0], load_vars=False, variable_manager=VariableManager())
    play_iterator = PlayIterator(play=play, inventory=InventoryManager(loader=None, sources='localhost,'), variable_manager=VariableManager())

    # Execute method under test
    with pytest.raises(NotImplementedError):
        play_iterator.get_original_task(host=None, task=None)

# Generated at 2022-06-12 21:35:11.701354
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host

    class StubModule(object):
        def __init__(self):
            pass

    b1 = Block()
    t1 = Task()
    t1._task = StubModule()
    b1.block.append(t1)
    p = Play()
    p.hosts = ['host1']
    p.vars = {'a': '1', 'b': '2'}
    p.blocks = [b1]
    i = PlayIterator(p)
    h = Host('host1')
    # get_host_state was called here, so the block is setup
    s = i.get_host_state(h)
   

# Generated at 2022-06-12 21:35:18.993112
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    host = 'fake_host'
    host = Host(host)
    task = 'fake_task'
    task = Task()
    task._role = None
    task._parent = None
    play = 'fake_play'
    iterator = PlayIterator(play)
    # test with hosts=[], blocks=[], blocks[].block=[], blocks[].block[].tasks=[], blocks[].block[].rescue=[]
    state = HostState()
    result = iterator.mark_host_failed(host)
    assert state == result

# Generated at 2022-06-12 21:35:23.744861
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    print('Testing method is_any_block_rescuing of class PlayIterator ...')
    # TODO: Write unit tests for method is_any_block_rescuing of class PlayIterator
    # PlayIterator
    #def is_any_block_rescuing(self, state):


# Generated at 2022-06-12 21:35:29.342954
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    h = get_host("test")
    p = Play().load(dict(), loader=MockLoader({}), variable_manager=MockVariableManager())
    i = PlayIterator(p)
    s = i.get_host_state(h)
    assert s.run_state == i.ITERATING_SETUP
    assert s.cur_block == 0
    assert s.cur_regular_task == 0
    assert s.cur_rescue_task == 0
    assert s.cur_always_task == 0

# Generated at 2022-06-12 21:36:10.299178
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    '''
    Unit test for method is_failed of class PlayIterator
    '''
    # Test with no hosts in play.
    with pytest.raises(AnsibleError):
        play = Play().load({}, variable_manager={}, loader=None)
        iterator = PlayIterator(play)
        iterator.is_failed(None)

    # Test with one host in play.
    test_host = MagicMock(name='host1')
    test_host.name = 'host1'
    play = Play().load({'hosts': 'host1'}, variable_manager={}, loader=None)
    iterator = PlayIterator(play)
    # Test with host not in hosts_states.
    assert not iterator.is_failed(test_host)

# Generated at 2022-06-12 21:36:15.053743
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    play = Play().load("test_playbooks/constructor.yml", variable_manager=dict(), loader=Loader())
    inventory = Inventory(loader=Loader(), variable_manager=VariableManager())
    itr = PlayIterator(inventory, play)

    assert itr.play == play

    assert len(itr._task_cache) == 5


# Generated at 2022-06-12 21:36:27.001688
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible import play
    from ansible import playbook
    from ansible import inventory
    from ansible.playbook.block import Block

    iterator = PlayIterator()
    iterator._host_states = dict()
    pb = playbook.Playbook()
    play_ds = dict(
        name        = 'foobar',
        hosts       = 'all',
        gather_facts= 'no',
        tasks       = [
            dict(action=dict(
                module ='ping'
            )),
            dict(action=dict(
                module ='debug',
                args = 'msg="{{inventory_hostname}}"',
            )),
            dict(action=dict(
                module ='debug',
                args = 'msg="{{inventory_hostname}}"',
            )),
        ]
    )
    play_ds.update

# Generated at 2022-06-12 21:36:37.416085
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # create a play, and add three blocks to it
    p = Play()
    p.add_block(Block([]))
    p.add_block(Block([]))
    p.add_block(Block([]))

    # make an iterator and load it with the play
    itr = PlayIterator()
    itr._load_blocks(p)

    # make a fake host and get the host state to play with
    h = Host('localhost')
    hs = itr.get_host_state(h)

    # set the play iterator to only set up, then test is_active_state
    hs.run_state = itr.SETTING_UP
    itr._host_states[h.name] = hs
    assert itr.get_active_state(hs).run_state == itr.SETTING_

# Generated at 2022-06-12 21:36:47.412985
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
	play = Play()
	play.load('', loaders=[MockDataLoader()])
	play_iterator = PlayIterator(play)
	play_iterator._cache_block_tasks(play.get_tasks())
	play_iterator._cache_block_tasks(play.get_tasks())
	play_iterator._cache_block_tasks(play.get_tasks())
	play_iterator._cache_block_tasks(play_iterator._tasks_cache)
	play_iterator._cache_block_tasks(play_iterator._tasks_cache)
	play_iterator._cache_block_tasks(play_iterator._tasks_cache)
	play_iterator._cache_block_tasks(play_iterator._tasks_cache)

# Generated at 2022-06-12 21:36:56.114462
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    import ansible.playbook
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.vars.manager import VariableManager


    host = Host(name='myhostname')

# Generated at 2022-06-12 21:37:06.210216
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    # create a play with a single task in it,
    # and a single host in the inventory
    play = dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='foo')))
        ]
    )

    inv_data = 'localhost'

    # create the play and the inventory
    loader = DataLoader()
    loader.set_basedir(os.getcwd())
    play = Play.load(play, loader=loader)
    play._included_file_parents = dict()
    play._included_files = dict()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=inv_data)

    # create the play iterator, which should advance to

# Generated at 2022-06-12 21:37:06.937975
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    pass

# Generated at 2022-06-12 21:37:12.294128
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    import __main__
    setattr(__main__, '__file__', '/path/to/ansible/playbook.py')
    from ansible.playbook import Play

    class Options: pass
    Options.connection = 'smart'

    p = Play.load(dict(
        name = "test play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    ), loader=None)

    i = PlayIterator()
    i.setup(p, Options())

    host1 = Host('webserver1')

# Generated at 2022-06-12 21:37:13.538770
# Unit test for method copy of class HostState
def test_HostState_copy():
    hs = HostState([Block()])
    hs_c = hs.copy()



# Generated at 2022-06-12 21:37:58.248038
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    play = Play()
    play.hosts = ['localhost', 'otherhost']
    play.vars = {}
    play.vars['foo'] = 'bar'
    play.vars['ansible_ssh_user'] = 'root'

    # test for a play without any blocks, to ensure the HostState objects are
    # initially set up correctly
    runner = PlayIterator(play=play)
    host = Host('localhost')
    empty_host_state = HostState(blocks=[])
    assert runner.get_host_state(host) == empty_host_state

    # create a play with 2 blocks to test
    play = Play()
    play.hosts = ['localhost', 'otherhost']
    play.vars = {}
    play.vars['foo'] = 'bar'

# Generated at 2022-06-12 21:38:00.839822
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    #Get the object of HostState class with argument "Block"
    hs = HostState([Block(None, None)])
    hs.__str__()



# Generated at 2022-06-12 21:38:09.128116
# Unit test for method copy of class HostState
def test_HostState_copy():
    h1 = HostState([])
    h2 = h1.copy()
    print(h1)
    print(h2)
    h1.cur_block = 100
    h1.cur_regular_task = 100
    h1.cur_rescue_task = 100
    h1.cur_always_task = 100
    h1.run_state = 100
    h1.fail_state = 100
    h1.pending_setup = True
    h1.did_rescue = True
    h1.did_start_at_task = True
    h1.tasks_child_state = 'tasks child state'
    h1.rescue_child_state = 'rescue child state'
    h1.always_child_state = 'always child state'
    print(h1)

# Generated at 2022-06-12 21:38:16.061848
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    '''
    The get_active_state method should find the active state, recursively if necessary
    when there are child states.
    '''
    # Create a PlayIterator context.
    play_iterator = PlayIterator(pattern=None)
    host = ansible.inventory.host.Host(name='fake_name')
    # Create a HostState with no blocks.
    state = HostState(blocks=[])
    # Method get_active_state should return the same host state.
    active_state = play_iterator.get_active_state(state)
    assert active_state is state
    # Create a child block and add it to the original host state.
    child_block = Block(block=[])
    child_state = HostState(blocks=[child_block])
    state.tasks_child_state = child_state
    # Method

# Generated at 2022-06-12 21:38:27.309230
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    # Load test PlayIterator module
    module = _load_module_source(os.path.dirname(sys.argv[0]), 'lib/ansible/playbook/play_iterator')
    # Load test PlayIterator module
    cls = getattr(module, 'PlayIterator')
    # Some initialization
    host=Mock()
    host.name = 'localhost'
    play=Mock()
    iterator = cls(play)
    host.name = 'localhost'
    block = Block()
    block.rescue = []
    block.always = []
    state = HostState(blocks=[block])
    state.run_state = 'ITERATING_TASKS'
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    iterator

# Generated at 2022-06-12 21:38:31.794427
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    """
    Perform unit test for get_host_state method of class PlayIterator
    """
    # data
    # play
    play = Play()
    play._hosts = [Host(name='host1'), Host(name='host2')]
    play._tasks = [Task(), Task()]
    play._block = Block()
    play._block.block = [play._tasks[0], play._tasks[1]]
    # play iterator
    play_iterator = PlayIterator(play)
    # tests
    for host in play._hosts:
        host_state = play_iterator.get_host_state(host)
        assert host_state, "Cannot retrieve host state for host %s" % host
        assert host_state.cur_block == 0, "Block of current task is not 0 for host %s" % host


# Generated at 2022-06-12 21:38:37.830204
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    my_play = Play().load(dict(
        name = 'myplay',
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [],
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='shell', args='whoami')),
            dict(action=dict(module='shell', args='id')),
        ],
    ), variable_manager=VariableManager(), loader=None)
    my_play._included_paths = ['/etc/ansible/roles']
    hosts = my_play.get_variable_manager().get_inventory().get_hosts()

# Generated at 2022-06-12 21:38:41.944292
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    my_play = Play()
    my_play._removed_hosts = ["1", "2"]
    my_play._tqm = TaskQueueManager(None, None, None, None, None)
    my_play_iterator = PlayIterator(my_play)
    print(my_play_iterator.get_failed_hosts())



# Generated at 2022-06-12 21:38:52.888859
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    inventory = Inventory(loader=None, variable_manager=None, host_list=['localhost'])

# Generated at 2022-06-12 21:39:01.847916
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    target_block = Block()
    target_block.block = [dict(action='test2')]
    state = HostState(blocks=[target_block])
    state.run_state = PlayIterator.ITERATING_TASKS
    assert PlayIterator.get_active_state(state).cur_regular_task == 0
    state.cur_regular_task = 1
    state.tasks_child_state = HostState(blocks=[target_block])
    state.tasks_child_state.run_state = PlayIterator.ITERATING_TASKS
    state.tasks_child_state.cur_regular_task = 2
    assert PlayIterator.get_active_state(state).cur_regular_task == 2
