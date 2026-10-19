

# Generated at 2022-06-12 21:30:41.460743
# Unit test for method copy of class HostState
def test_HostState_copy():
    new_state = HostState(self._blocks)
    new_state.cur_block = self.cur_block
    new_state.cur_regular_task = self.cur_regular_task
    new_state.cur_rescue_task = self.cur_rescue_task
    new_state.cur_always_task = self.cur_always_task
    new_state.run_state = self.run_state
    new_state.fail_state = self.fail_state
    new_state.pending_setup = self.pending_setup
    new_state.did_rescue = self.did_rescue
    new_state.did_start_at_task = self.did_start_at_task
    if self.tasks_child_state is not None:
        new_state.tasks_child_

# Generated at 2022-06-12 21:30:48.458906
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    host = MagicMock()
    host.name = 'foo'
    play = Play().load(dict(name='test play', hosts='foo', gather_facts='no', tasks=[dict(action=dict(module='shell', args='ls'))]), variable_manager=MagicMock())
    pitr = PlayIterator(play)
    pitr._host_states[host.name] = HostState(blocks=[MagicMock(rescue=[], always=[])])
    pitr._host_states[host.name].cur_block = 0
    pitr._host_states[host.name].cur_regular_task = 0
    pitr._host_states[host.name].cur_rescue_task = 0
    pitr._host_states[host.name].cur_always_task = 0

# Generated at 2022-06-12 21:30:59.367861
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    # reset loaded plugins
    global _basedir
    import ansible.plugins
    ansible.plugins.reset()
    ansible.plugins.finder = PluginLoader(
        'AnsibleModule',
        'ansible.module_utils',
        C.MODULE_UTILS_PATH,
        'module_utils',
    )
    plugins.add_all_plugin_dirs()

    # FIXME: is there a simpler way to do this?
    # PlayIterator is created using a Play, which needs a TaskQueueManager,
    # which has a HostManager and a Host, which needs a PlayContext, which
    # needs a Runner and a module_loader
    runner = Runner()

    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-12 21:31:11.037601
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    a_task = Mock()
    a_cache = Mock()
    a_task.block_vars = dict()
    a_task.block_vars['ansible_play_hosts'] = 'all'
    a_task.block_vars['play_hosts'] = 'all'
    pi = PlayIterator()
    with patch.object(pi, '_get_task_cache_id') as mock_get_task_cache_id:
        with patch.object(pi, '_task_cache') as mock_task_cache:
            with patch.object(pi, '_play') as mock_play:
                mock_get_task_cache_id.return_value = 'any_id'
                mock_task_cache.get.return_value = a_cache

# Generated at 2022-06-12 21:31:22.323328
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    # Test id: 20
    # test the PlayIterator.get_original_task method
    #
    # setup
    p = Play().load(FIXTURE_PLAYBOOK, variable_manager=VariableManager(), loader=Loader())
    p._role_names = [False]
    i = PlayIterator(p)
    i.host_states = {"host": HostState(host=Host("host"))}
    t1 = Task()
    t1._uuid = '123'
    t1._role = None
    i.host_states["host"].tasks = [t1]

    # test no task
    t = None
    assert None == i.get_original_task("host", t)

    # test the uuid matching
    t = Task()
    t._uuid = '123'
    t._role = None
   

# Generated at 2022-06-12 21:31:29.398702
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    # Parameters
    PlayIterator.TITLE = 'Ansible Playbook'
    PlayIterator.ITERATING_SETUP = 'ITERATING_SETUP'
    PlayIterator.ITERATING_TASKS = 'ITERATING_TASKS'
    PlayIterator.ITERATING_RESCUE = 'ITERATING_RESCUE'
    PlayIterator.ITERATING_ALWAYS = 'ITERATING_ALWAYS'
    PlayIterator.ITERATING_COMPLETE = 'ITERATING_COMPLETE'

    from ansible.parsing.yaml.objects import AnsibleMapping

    state = AnsibleMapping()
    state.run_state = ''
    state.tasks_child_state = None
    state.rescue_child_state = None
    state.always_child_state = None
    state.did

# Generated at 2022-06-12 21:31:38.602137
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    '''
    test_PlayIterator_add_tasks is the testcase for method add_tasks of class PlayIterator.
    '''
    # Initialize a host for the test.
    host = Host('testhost.example.com')
    # Initialize an empty task_list for the test.
    task_list = []

    # Create an instance of class PlayIterator.
    play_iterator = PlayIterator()
    # Execute method add_tasks.
    play_iterator.add_tasks(host, task_list)



# Generated at 2022-06-12 21:31:47.620695
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    """
    This is a unit test for the constructor of PlayIterator
    """
    # init objects
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = Play.load(dict(
        name="Ansible Play",
        hosts='local',
        gather_facts='no',
        tasks=[dict(action=dict(module="shell", args="ls"))]
        ), loader=loader, variable_manager=variable_manager)
    play = play_source.copy()

    # create the play iterator

# Generated at 2022-06-12 21:31:54.602540
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    host = Host(name="foo")
    state = HostState(host)
    state.run_state = PlayIterator.ITERATING_TASKS
    state.fail_state = PlayIterator.FAILED_NONE
    state.cur_block = 0
    state.cur_regular_task = 1
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state.tasks_child_state = None
    state.rescue_child_state = None
    state.always_child_state = None
    state.did_rescue = False
    state._blocks = [("x", "y", "z")]
    state._play = Play("test_play")
    pi = PlayIterator("test_play")
    pi._host_states[host.name] = state

    # 1

# Generated at 2022-06-12 21:32:02.795838
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host


# Generated at 2022-06-12 21:33:09.267141
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    fake_play = dict(
        hosts = ['localhost'],
        tasks = [
            dict(action=dict(module='fail', args=dict(msg="failed")))
        ]
    )

    play = Play.load(fake_play, variable_manager=VariableManager())

    ti = PlayIterator()

    ti.host_states = {'localhost': HostState(blocks=[play.compile()])}
    ti.host_states['localhost']._blocks[0]._results.get('failed')
    print(ti.get_failed_hosts())
    assert ti.get_failed_hosts() == {'localhost': True}
    
    

# Generated at 2022-06-12 21:33:16.605227
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    p = Play().load(dict(
        name = "foobar",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='shell', args='whoami')),
            dict(action=dict(module='shell', args='sudo ls')),
        ]
    ), variable_manager=VariableManager())


# Generated at 2022-06-12 21:33:19.746131
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    '''
    Unit test for cache_block_tasks method of class PlayIterator
    '''
    # See test/test_play_iterator.py
    pass


# Generated at 2022-06-12 21:33:30.635106
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # setup
    play = Play().load(dict(
        name = "test play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='false')),
            dict(action=dict(module='shell', args='false')),
            dict(action=dict(module='shell', args='false')),
        ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())
    iterator = PlayIterator(play)

    # test
    iterator.mark_host_failed(play.get_hosts()[0])
    iterator.mark_host_failed(play.get_hosts()[1])
    assert len(iterator.get_failed_hosts()) == 2, iterator.get_failed_hosts()



# Generated at 2022-06-12 21:33:31.418410
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
  pass



# Generated at 2022-06-12 21:33:39.113798
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    '''
    Test all of the different states and different combinations of states.
    '''

# Generated at 2022-06-12 21:33:51.958665
# Unit test for method __str__ of class HostState

# Generated at 2022-06-12 21:34:01.865247
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    fake_play = dict(
        name = "foobar",
        hosts = "all",
        gather_facts = "no",
        user = "test",
        sudo = "yes",
        sudo_user = "user1",
        become = "yes",
        become_user = "user2",
        become_method = "sudo",
        check = "yes",
        gather_subset = ["all"],
        roles = []
    )

    test_play = Play().load(fake_play, variable_manager=VariableManager(), loader=DictDataLoader())

    fake_host = Host(name="testhost")
    fake_host.set_variable('ansible_connection', "local")
    fake_host.set_variable('ansible_python_interpreter', "/usr/bin/python")
    fake_host.set_

# Generated at 2022-06-12 21:34:05.970519
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # Random test to get a crash
    # This was enough to crash on python 2.6
    assert PlayIterator(play=None, play_context=None, variable_manager=None, all_vars=None, loader=None).get_failed_hosts() == {}

# Generated at 2022-06-12 21:34:15.576006
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    '''
    unit test for method get_host_state of class PlayIterator
    '''

    # Example of a full state for a host that has completed all of the tasks and all blocks
    '''
    play (id=1):
        pattern: ['127.0.0.1', '127.0.0.2']
        name: test play
        roles: []
        user: None
        vars: []
        handler_blocks: []
        tasks:
        - name: first task
        block:
        - name: outer block
          tasks:
          - name: inner task
    '''

# Generated at 2022-06-12 21:35:29.102053
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    display.quiet = True

# Generated at 2022-06-12 21:35:41.339346
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play = Play()
    iterator = PlayIterator(play)

    # Tested method: is_any_block_rescuing()
    block = Block().load(dict(rescue=[dict(name="rescue")],
                              always=[dict(name="always")]))
    host = Host(name="127.0.0.1")
    state = HostState(host, block)
    state.run_state = PlayIterator.ITERATING_TASKS
    iterator._host_states = {host.name: state}

    # First test case
    # Check the result of is_any_block_rescuing(state) when state.run_state is ITERATING_TASKS
    assert iterator.is_any_block_rescuing(state) is False

    # Second test case
    # Check the result of is_any

# Generated at 2022-06-12 21:35:52.249516
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    p = Play().load("test/test_playbooks/pre_tasks.yml", variable_manager=VariableManager(), loader=Loader())
    play = p[0]
    assert play.name == 'test play'
    play._tqm = PlayIterator(p, None, None, "ok", [], False, False)
    play._tqm._inventory = Inventory(loader=None, variable_manager=None, host_list="test/test_playbooks/hosts")

    def iterate():
        for host in play.get_hosts():
            for task in play.get_tasks():
                print("host: %s task: %s" % (host.name, task))
                yield task

    generator = iterate()

    assert isinstance(play._tqm, PlayIterator)
    # Two hosts running two tasks

# Generated at 2022-06-12 21:35:56.927382
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    dt = PlayIterator(play=None, play_context=None)
    block = Block([])
    tasks = ()

    # Error: expected tuple of variables, received NoneType
    # dt.cache_block_tasks(block=block, tasks=tasks)
    pass



# Generated at 2022-06-12 21:36:07.764696
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    '''
    Test method get_failed_hosts of class PlayIterator.
    '''
    from collections import namedtuple
    from ansible.playbook import Play, Playbook, Task, Role
    from ansible.inventory.manager import InventoryManager

    Options = namedtuple('Options', ['become', 'become_method', 'become_user'])
    inventory = InventoryManager(['localhost'])

# Generated at 2022-06-12 21:36:16.343065
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    test_HostState = HostState(["Block1", "Block2", "Block3"])
    test_HostState.cur_block = 1
    test_HostState.cur_regular_task = 1
    test_HostState.cur_rescue_task = 1
    test_HostState.cur_always_task = 1
    test_HostState.run_state = PlayIterator.ITERATING_RESCUE
    test_HostState.fail_state = PlayIterator.FAILED_ALWAYS
    test_HostState.pending_setup = True
    test_HostState.did_start_at_task = True
    test_HostState.did_rescue = True
    test_HostState.tasks_child_state = HostState(["Block1", "Block2", "Block3"])
    test_HostState.tasks

# Generated at 2022-06-12 21:36:27.797283
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    # Setup a PlayIterator object to test the method is_any_block_rescuing
    play = Play().load(dict(
        name = "test play",
        hosts = "all",
        gather_facts = "no",
        tasks = [
            dict(action=dict(module="debug", args=dict(msg="foo")))
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())

    hosts = [Host(name='hostname')]
    play_iterator = PlayIterator()
    play_iterator._play = play
    play_iterator._play._included_file_stashes['hostvars'] = dict()

    # Iterate of the blocks and add them to the PlayIterator. It should not fail

# Generated at 2022-06-12 21:36:35.332137
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    try:
        host = C.Host(name='8.8.8.8')
        play = C.Play()
        iterator = PlayIterator(play, [host])
        iterator.get_next_task_for_host(host)
        iterator.mark_host_failed(host)
        task = iterator.get_next_task_for_host(host)
        assert task is None
    except AssertionError as e:
        display.error("test_PlayIterator_mark_host_failed assertion failed")
        raise

# Generated at 2022-06-12 21:36:41.040158
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    import mock
    mock_play = mock.Mock()
    mock_play.serial = 0
    mock_play.playbook = None
    mock_play.play_context = mock.Mock()
    mock_play.play_context.module_vars = dict()
    mock_play.play_context.module_name = 'setup'
    fake_host_1 = Mock()
    fake_host_1.name = 'host_1'
    fake_host_2 = Mock()
    fake_host_2.name = 'host_2'
    fake_host_3 = Mock()
    fake_host_3.name = 'host_3'
    fake_host_4 = Mock()
    fake_host_4.name = 'host_4'
    # test 1
    # host_1 - succeeded
    # host

# Generated at 2022-06-12 21:36:44.765371
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    # State object
    state = PlayIterator._HostState(blocks=[])
    
    # Tests
    assert state.is_any_block_rescuing(state) is False

# Generated at 2022-06-12 21:39:03.973333
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    iterator = PlayIterator()
    assert iterator.is_any_block_rescuing(iterator.get_host_state(None)) == False
    iterator.set_failed_state(iterator._get_current_state(None))
    assert iterator.is_any_block_rescuing(iterator.get_host_state(None)) == False

# Generated at 2022-06-12 21:39:13.484904
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    host = Host('example.org')
    iterator = PlayIterator(play=None, inventory=None, play_context=None)
    iterator.get_next_task_for_host(host)
    play = Play()
    iterator = PlayIterator(play=play, inventory=None, play_context=None)
    iterator.get_next_task_for_host(host)
    play._included_file = 'included_file'
    play.get_handler = lambda x: None
    iterator.get_next_task_for_host(host)
    iterator.on_unreachable(host, None)
    iterator._play.set_variable_manager(VariableManager())
    iterator.get_next_task_for_host(host)
    iterator._play.set_variable_manager(VariableManager())
    iterator._play.get

# Generated at 2022-06-12 21:39:14.447614
# Unit test for method cache_block_tasks of class PlayIterator
def test_PlayIterator_cache_block_tasks():
    pass


# Generated at 2022-06-12 21:39:20.343055
# Unit test for method is_failed of class PlayIterator
def test_PlayIterator_is_failed():
    p = Play().load(dict(
        name = 'myplay',
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='/usr/bin/false')),
            dict(action=dict(module='shell', args='/usr/bin/false')),
        ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())
    iterator = PlayIterator(p)
    iterator._host_states['foo'] = HostState(host=Host(name='foo'))
    assert not iterator.is_failed('foo')
    assert not iterator.is_failed('bar')


# Generated at 2022-06-12 21:39:22.537300
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    # Tests currently disabled
    pass
import unittest


Test_get_original_task=unittest.TestCase()


# Generated at 2022-06-12 21:39:32.033225
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    """Runs tests on the constructor of class PlayIterator"""
    # When a PlayIterator is initiliazed it should have a play object and an inventory object
    a_play = dict(
        name = "a play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )
    play = Play().load(a_play, variable_manager=VariableManager(), loader=DataLoader())
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list='test/units/inventory/hosts')
    inventory.get_host('foobar').set_variable

# Generated at 2022-06-12 21:39:43.685775
# Unit test for method copy of class HostState
def test_HostState_copy():
    h = HostState([Block([Task()])])
    h.cur_block = 2
    h.cur_regular_task = 3
    h.cur_rescue_task = 4
    h.cur_always_task = 5
    h.run_state = 1
    h.fail_state = 2
    h.pending_setup = 3
    h.tasks_child_state = 4
    h.rescue_child_state = 5
    h.always_child_state = 6
    h.did_rescue = 7
    h.did_start_at_task = 8
    h2 = h.copy()
    assert h == h2
    assert h is not h2
    assert h._blocks is not h2._blocks
    assert h._blocks == h2._blocks



# Generated at 2022-06-12 21:39:51.618011
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible import play
    from ansible import task
    from ansible import host
    from ansible import playbook
    from ansible import inventory
    from ansible import callbacks
    from ansible.callbacks import ResultCallback
    from ansible import vault
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar


    res_cb = ResultCallback()
    host_inst = host.Host('127.0.0.1')
    host_inst2 = host.Host('127.0.0.2')
    host_inst3 = host.Host('127.0.0.3')
    host_inst4 = host.Host('127.0.0.4')
    task_inst = task.Task()
    task_inst.name = 'test_task_1'
   

# Generated at 2022-06-12 21:39:56.158853
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    iterator = PlayIterator()
    iterator._play = Play()
    iterator._play._included_paths = ['/var/lib/awx/projects/test-project/16/']


# Generated at 2022-06-12 21:39:57.043484
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    pass
