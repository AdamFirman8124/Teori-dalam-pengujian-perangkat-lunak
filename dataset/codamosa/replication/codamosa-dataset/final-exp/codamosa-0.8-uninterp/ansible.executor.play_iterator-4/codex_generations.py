

# Generated at 2022-06-12 21:30:29.995280
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # FIXME: test this method!
    pass


# Generated at 2022-06-12 21:30:37.618296
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
  from collections import namedtuple
  from ansible.playbook.task import Task
  from ansible.playbook.block import Block
  from ansible.playbook.conditional import Conditional
  from ansible.playbook.helpers import load_list_of_tasks
  from ansible.playbook.task import Task
  from ansible.template import Templar


# Generated at 2022-06-12 21:30:42.492840
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    # this is a host-based test, so build up a mock inventory
    group = MagicMock()
    group.get_hosts.return_value = [MagicMock()]
    inventory = MagicMock()
    inventory.get_host.return_value = MagicMock()
    inventory.get_host.return_value.get_groups.return_value = [group]

    # also mock up a play
    play = MagicMock()
    play.get_strategy.return_value.get_hosts.return_value = [inventory.get_host.return_value]

    # and a fake loader and variable manager for the iterator to use
    loader = MagicMock()
    variable_manager = MagicMock()

    # now create the iterator, and run the target method

# Generated at 2022-06-12 21:30:48.957580
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    def test_PlayIterator_get_failed_hosts__empty_data():
        iterator = PlayIterator()

        expected = {}
        actual = iterator.get_failed_hosts()

        assert actual == expected

    def test_PlayIterator_get_failed_hosts__data_with_failure():
        iterator = PlayIterator()
        host = Host()
        host.name = "test_host"
        host_state = HostState()
        host_state.fail_state = PlayIterator.FAILED_TASKS
        iterator._host_states[host.name] = host_state

        expected = {"test_host": True}
        actual = iterator.get_failed_hosts()

        assert actual == expected

    test_PlayIterator_get_failed_hosts__empty_data()
    test_PlayIterator_get_failed_

# Generated at 2022-06-12 21:30:59.573121
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # Create an empty play (play "name" is irrelevant here)
    play = Play()
    # Create the play iterator which we're ultimately testing
    sut = PlayIterator(play=play)
    # Get a sample task
    task = Task()
    # Create a block to wrap the task in
    block = Block(block=[task])
    # Create the state object which we're testing
    state = HostState(blocks=[block])
    # Set up a "active" state
    state.run_state = sut.ITERATING_TASKS
    # Check that the active state is returned in the case of top-level tasks
    # start: HostState
    # expected: HostState
    assert sut.get_active_state(state=state) == state
    # Set the state to not active, but with a child state
    state.run

# Generated at 2022-06-12 21:31:08.553931
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    p = Play().load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [ dict(action=dict(module='shell', args='ls')) ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())
    ti = TaskIterator(p, play_context=PlayContext())
    pi = PlayIterator(p, ti)
    pi.mark_host_failed("test_host")

    assert pi._host_states["test_host"] is not None
    assert pi.is_failed("test_host")



# Generated at 2022-06-12 21:31:16.142406
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    play = Play()
    blocks = [
        Block(
            tasks=[
                Task()
        ])
    ]

    pi = PlayIterator(play, blocks)

    h1 = Host('host1')
    h2 = Host('host2')

    hs1 = HostState(blocks, h1)
    hs2 = HostState(blocks, h2)

    # not using real blocks here, just using tuples
    assert hs1.run_state == "ITERATING_TASKS"
    hs1.tasks_child_state = HostState(tuple(), h1)
    hs1.tasks_child_state.run_state = "ITERATING_TASKS"
    assert pi.get_active_state(hs1) == hs1.tasks_child_state

    assert hs2

# Generated at 2022-06-12 21:31:26.488806
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():

    # this is a list of mocks that we instantiate and build up in the tests here
    # to ensure we don't have to re-create them for each test.  This is just to
    # ensure that the side_effects we set on them get reused between tests
    all_mocks = []

    def _make_mock(obj, attr_name, attr_value):
        mock = Mock()
        mock.return_value = attr_value
        setattr(obj, attr_name, mock)
        all_mocks.append(mock)
        return mock

    ####################################
    # PlayIterator.cache_block_tasks()
    ####################################

    # Test 1:
    # Test the basic case of PlayIterator.cache_block_tasks() with
    # a single block with a single task in it.


# Generated at 2022-06-12 21:31:29.566227
# Unit test for method __eq__ of class HostState
def test_HostState___eq__():
    '''
    unit test for HostState.__eq__()
    '''
    # TODO
    pass

# end of test: test_HostState___eq__()



# Generated at 2022-06-12 21:31:33.701128
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    ensure the mark_host_failed method of the PlayIterator class properly marks the host
    as failed in the _host_states dict.
    '''
    play = Play().load("test.yml", variable_manager=VariableManager(), loader=loader)
    play_iterator = PlayIterator(play)
    play_iterator._tqm = Mock()

    host = Host("testhost")

    play_iterator.get_next_task_for_host(host)
    play_iterator.mark_host_failed(host)
    assert play_iterator.is_failed(host)


# Generated at 2022-06-12 21:32:08.516239
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    pass

# Generated at 2022-06-12 21:32:20.228413
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    # Define some test data
    play = Play()
    play._role_name = 'common'
    play._block = Block()
    play._block.block = [(Task(),),(Task(),),(Task(),),]
    play._blocks = [play._block,]
    host = Host()
    host.name = 'testhost'
    play._hosts = [host,]
    host_state = HostState(play=play, host=host)
    host_state._blocks = [play._block,]
    host_state.play = play
    host_state.host = host
    host_state.cur_block = 0
    host_state.cur_regular_task = 0
    host_state.cur_rescue_task = 0
    host_state.cur_always_task = 0
    host_state.run

# Generated at 2022-06-12 21:32:23.599590
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    test_PlayIterator = PlayIterator()

    assert isinstance(test_PlayIterator.is_failed, types.MethodType)
    assert test_PlayIterator.is_failed(host) is False

# Generated at 2022-06-12 21:32:30.309015
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    '''
    ansible.playbook.PlayIterator - constructor test
    '''

    ## Inventory test, empty
    inv = Inventory(host_list=[])
    play = Play.load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), variable_manager=VariableManager(), loader=None)

    print("---")
    print("Testing PlayIterator with empty inventory")
    pi = PlayIterator(inventory=inv, play=play, play_context=None, all_vars=dict())
    for host in pi:
        print

# Generated at 2022-06-12 21:32:42.192144
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # Get a playable PlayIterator with a Play and a list of roles
    p = PlaybookInclude()
    p._play = Play()
    mock_play = p._play
    mock_play._roles = []
    mock_play._role_names = ['role1', 'role2']
    mock_play._role_blocks = []
    mock_play._handlers = [mock_task() for i in range(6)]
    mock_play_iterator = PlayIterator(p, None)
    mock_play_iterator.get_next_task_for_host = mock_play_iterator_get_next_task_for_host

    # Create a mock HostState
    state = HostState(blocks=[])
    state.run_state = PlayIterator.ITERATING_TASKS
    state.cur_block = 0

# Generated at 2022-06-12 21:32:51.727079
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    test_play = Play().load(dict(
        name = "test play",
        hosts = "all",
        gather_facts = "no",
        tasks = [
            dict(action=dict(module="shell", args="ls")),
            dict(action=dict(module="shell", args="ls", register="myoutput")),
            dict(action=dict(module="debug", args=dict(msg="{{myoutput}}"), when="myoutput|failed"),
                 tags=['always']),
            dict(action=dict(module="shell", args="ls", when="not myoutput|failed"),
                 tags=['always'])
        ]
    ), variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-12 21:33:04.417638
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''test cache_block_tasks'''
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.handler
    import ansible.inventory.host

    # Test PlayIterator.cache_block_tasks()
    #
    # Arguments:
    #  (None)
    #
    # Returns:
    #  (None)
    #
    # Raises:
    #  (None)

    # test_PlayIterator_cache_block_tasks: mapping to role: test_role
    # test_PlayIterator_cache_block_tasks: mapping to handler: test_handler
    # test_PlayIterator_cache_block_tasks: role: test_role: path:

# Generated at 2022-06-12 21:33:15.297855
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    p = Play().load(
        dict(
            name = 'test play',
            hosts = 'somenode',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='first task'))),
                dict(action=dict(module='debug', args=dict(msg='second task'))),
                dict(action=dict(module='debug', args=dict(msg='third task'))),
                dict(action=dict(module='debug', args=dict(msg='fourth task'))),
                dict(action=dict(module='debug', args=dict(msg='fifth task'))),
            ]
        )
    )

    host = 'somenode'
    host_states = HostState(blocks=[])

# Generated at 2022-06-12 21:33:24.332756
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    play = dict(name="test", hosts=None, gather_facts="no", remote_user="user", tasks=None, become="yes", become_user="super")
    p = Play().load(play, variable_manager=variable_manager, loader=loader)
    pi = PlayIterator(p, load=None)
    pi._host_states = dict([(k, bool(v)) for k, v in {"host1": True, "host2": False, "host3": True}.items()])
    assert pi.get_failed_hosts() == {"host1": True, "host3": True}


# Generated at 2022-06-12 21:33:31.356173
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    Unit test for PlayIterator.get_failed_hosts()
    '''
    class TestHost(object):
        pass
    test_host = TestHost()
    test_host.name = 'localhost'

    class TestPlay(object):
        pass
    test_play = TestPlay()
    test_play._removed_hosts = ['localhost']

    p = PlayIterator(test_play, [test_host])
    assert p.get_failed_hosts() == {'localhost': True}


# Generated at 2022-06-12 21:34:27.642397
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    '''
    Unit test for method add_tasks of class PlayIterator
    '''
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(loader=loader, options=Options())
    variable_manager.options_vars = load_options_vars(options=Options())
    iterator = PlayIterator(play=None, variable_manager=variable_manager, all_vars=dict())

    block = Block({"name": "test block", "rescue": "", "always": "", "block": ""})
    state = HostState(blocks=[block])

    # case 1: failing state
    state.fail_state = iterator.FAILED_TASKS

# Generated at 2022-06-12 21:34:28.224164
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    print("")

# Generated at 2022-06-12 21:34:40.592674
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    import mock
    from ansible.playbook.block import Block
    block = Block()
    block.rescue = [mock.Mock(), mock.Mock()]
    block.always = [mock.Mock()]

    s = PlayIterator._HostState()
    assert not PlayIterator(mock.Mock()).is_any_block_rescuing(s)

    s = PlayIterator._HostState()
    s.run_state = PlayIterator.ITERATING_TASKS
    assert not PlayIterator(mock.Mock()).is_any_block_rescuing(s)

    s = PlayIterator._HostState()
    s.run_state = PlayIterator.ITERATING_RESCUE
    assert PlayIterator(mock.Mock()).is_any_block_rescuing(s)



# Generated at 2022-06-12 21:34:50.788521
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    from ansible import inventory
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    ##################################
    ## Setup for the following tests
    ##################################
    test_play_1 = Play()
    test_play_1.name = 'test play 1'
    test_play_1._entries = ['test_task_1', 'test_task_2', 'test_task_3', 'test_task_4', 'test_task_5']
    test_task_1 = Task()
    test_task_1.name = 'test_task_1'
    test_task_2 = Task()
    test_task_2.name = 'test_task_2'
    test

# Generated at 2022-06-12 21:35:00.226068
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    # variables
    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load(dict(name = "Ansible Play", hosts='localhost', gather_facts = 'no', tasks=[dict(action=dict(module='shell', args='ls'))]), variable_manager=variable_manager, loader=loader)
    play_iterator = PlayIterator(inventory, play, None)
    assert InventoryManager == type(play_iterator._inventory)
    assert Play == type(play_iterator._play)
    assert dict == type(play_iterator._last_task_banner)
    assert defaultdict == type(play_iterator._host_states)

if __name__ == '__main__':
    test_PlayIterator()

# Generated at 2022-06-12 21:35:06.040358
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    '''
    >>> import ansible.playbook
    >>> pb = ansible.playbook.PlayBook(
    ...     playbook     = '/dev/null',
    ...     inventory    = '/dev/null',
    ...     callbacks    = ansible.playbook.PlayBookCallbacks(),
    ...     runner_callbacks = ansible.playbook.PlayBookRunnerCallbacks(),
    ...     stats            = ansible.playbook.PlayBookStats(),
    ... )
    >>> pb.get_plays()
    []
    '''


# Generated at 2022-06-12 21:35:08.062963
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    '''
    Unit test for method mark_host_failed of class PlayIterator
    '''
    pass

# Generated at 2022-06-12 21:35:18.331130
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import IncludeRole
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    t1 = Task()
    t1.name = 'test1'
    t2 = Task()
    t2.name = 'test2'
    t3 = Task()
    t3.name = 'test3'
    t4 = Task()
    t4.name = 'test4'
    t5 = Task()
    t5.name = 'test5'
    t6 = Task()
    t6.name = 'test6'


# Generated at 2022-06-12 21:35:21.675427
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
	host = Host(name = "testhost")
	s = PlayIterator(play = Play()).get_active_state(block=None, host=host)
	assert s == (None, None)

# Generated at 2022-06-12 21:35:30.063024
# Unit test for method get_next_task_for_host of class PlayIterator

# Generated at 2022-06-12 21:37:09.785316
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    from tempfile import NamedTemporaryFile
    from ansible.template import Templar

    def _load_hosts(hosts):
        # Create some hosts and put them into a group
        loader = DataLoader()
        variable_manager = VariableManager()
        inventory = InventoryManager(loader=loader, sources='')
        t = Templar(loader=loader, variable_manager=variable_manager)

        for host in hosts:
            inventory.add_host(t.template(host))

# Generated at 2022-06-12 21:37:19.200659
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    p = Play().load(dict(
        name = "pb",
        hosts = 'webservers',
        roles = ['common', 'web'],
        gather_facts = 'no',
    ), variable_manager=VariableManager(), loader=None)

    i = PlayIterator(p, lambda h: Host(h, p))
    assert len(i._hosts) == 2
    assert i._host_states[i._hosts[0].name]._blocks == p.compile()
    assert i._host_states[i._hosts[1].name]._blocks == p.compile()
    assert len(i._host_states) == 2

    i2 = i.copy()
    assert len(i2._hosts) == 2
    assert i2._hosts[0].name == i2._hosts[0].name

# Generated at 2022-06-12 21:37:20.907829
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():

    # TODO
    pass

# Generated at 2022-06-12 21:37:30.410062
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.task.task import Task
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader

    hosts = ["host1", "host2"]
    host1 = Host(name="host1")
    host2 = Host(name="host2")
    group1 = Group("group1")
    group2 = Group("group2")
    group3 = Group("group3")
    group1.add_host(host1)
   

# Generated at 2022-06-12 21:37:33.404951
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    h = Host('localhost')
    pi = PlayIterator()
    hs = HostState(h, task=Task(), play=pi._play)
    pi._host_states[h.name] = hs
    assert hs == pi.get_host_state(h)


# Generated at 2022-06-12 21:37:39.623277
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude

    from units.compat import unittest
    import ansible.playbook.play

    ansible.playbook.play.Task = Task
    ansible.playbook.play.Block = Block
    ansible.playbook.play.RoleInclude = RoleInclude

    class TestPlayIterator(unittest.TestCase):
        def setUp(self):
            self.pi = PlayIterator()
        def test_is_any_block_rescuing(self):
            t1 = Task()
            t1._

# Generated at 2022-06-12 21:37:50.556779
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    loader = DictDataLoader({
        "playbook.yml": """
        - hosts:
            - alpha
            - beta
            - gamma
            - delta
            - epsilon
        tasks:
        - debug:
            msg: '1'
        tasks:
        - debug:
            msg: '2'
        rescue:
        - debug:
            msg: '3'
        always:
        - debug:
            msg: '4'
        """,
    })

    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    inventory._hosts_cache = {
        "alpha": Host("alpha"),
        "beta": Host("beta"),
        "gamma": Host("gamma"),
        "delta": Host("delta"),
        "epsilon": Host("epsilon")
    }

# Generated at 2022-06-12 21:37:55.554932
# Unit test for method copy of class HostState
def test_HostState_copy():
    blocks = [Block(1, "block1", "task"), Block(2, "block2", "task"), Block(3, "block3", "task")]
    test_state = HostState(blocks)
    print(test_state.copy())


# Generated at 2022-06-12 21:38:05.617418
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    host = Mock()
    host.get_name.return_value = "test host"
    host.name = "test host"
    inventory = Mock()
    inventory.get_host.return_value = host
    inventory.get_hosts.return_value = [host]
    play = Mock()
    play.get_vars.return_value = dict()
    play.get_roles.return_value = []
    play.get_tasks.return_value = []
    play.get_handler.return_value = None
    play.get_low_level_tasks.return_value = []
    play.get_dependencies.return_value = dict()
    play.name = "test play"
    play.hosts = "test host"
    play.get_hosts.return_value = [host]


# Generated at 2022-06-12 21:38:13.441579
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    host = 'localhost'
    play = AnsiblePlay()
    play.post_validate()
    play_iterator = PlayIterator(play)

    task_0 = Task()
    task_1 = Task()
    task_2 = Task()
    block_0 = Block()
    block_0.block = [task_0]
    block_1 = Block()
    block_1.block = [task_1]
    block_2 = Block()
    block_2.block = [task_2]
    play.block = [block_0, block_1, block_2]
    play_iterator.update_state(host)

    # active state is the initial state
    active_state = play_iterator.get_host_