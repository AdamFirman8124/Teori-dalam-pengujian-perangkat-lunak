

# Generated at 2022-06-12 21:30:49.409809
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    _print_result_of_test(PlayIterator.get_original_task)

# Generated at 2022-06-12 21:30:59.697817
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    play = Play().load(dict(
        name = 'test play',
        hosts = 'foobar',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='foo')),
            dict(action=dict(module='shell', args='bar')),
            dict(action=dict(module='shell', args='baz'))
        ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())

    host = Host(name='foobar')
    tqm = None
    play_context = PlayContext(play=play, options=None, variable_manager=VariableManager(), passwords=None)
    loaded_callbacks = []
    iterator = PlayIterator(play, tqm, load_callbacks=loaded_callbacks, play_context=play_context)
    iterator

# Generated at 2022-06-12 21:31:08.380148
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    def build_play(vars):
        play = Play()
        play.vars = vars
        return play

    def build_play_context(play):
        pc = PlayContext(play=play)
        pc._prompt = lambda x,y,z: None
        return pc

    for vars in (VariableManager(), dict_to_safe_dict({})):
        play = build_play(vars)
        pc = build_play_context(play)
        assert isinstance(PlayIterator(play, [], pc), PlayIterator)


# Generated at 2022-06-12 21:31:19.715446
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    for failed in (0, 1, 2, 4, 8, 1 | 2, 1 | 4, 1 | 8, 2 | 4, 2 | 8, 4 | 8, 1 | 2 | 4, 1 | 2 | 8, 1 | 4 | 8, 2 | 4 | 8, 1 | 2 | 4 | 8):
        host_state = HostState([Block([Role(),Role(),Role()])])
        host_state.cur_block = 1
        host_state.cur_regular_task = 2
        host_state.cur_rescue_task = 3
        host_state.cur_always_task = 4
        host_state.run_state = 5
        host_state.fail_state = failed
        host_state.pending_setup = True

# Generated at 2022-06-12 21:31:24.474663
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    test_values = ('HostState(%r)',
                   _run_state_to_string,
                   'ITERATING_SETUP',
                   'ITERATING_TASKS',
                   'ITERATING_RESCUE',
                   'ITERATING_ALWAYS',
                   'ITERATING_COMPLETE',
                   'UNKNOWN STATE',
                   _failed_state_to_string,
                   'FAILED_SETUP',
                   'FAILED_TASKS',
                   'FAILED_RESCUE',
                   'FAILED_ALWAYS',
                   'FAILED_NONE',
                   )
    

# Generated at 2022-06-12 21:31:34.562278
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    print("TESTING HostState test_HostState___str__()")
    a = HostState(["B1", "B2"])
    assert str(a) == "HOST STATE: block=0, task=0, rescue=0, always=0, run_state=ITERATING_SETUP, fail_state=FAILED_NONE, pending_setup=False, tasks child state? (None), rescue child state? (None), always child state? (None), did rescue? False, did start at task? False"
    print("HostState test_HostState___str__() PASSED")
#Unit test for method __eq__ of class HostState

# Generated at 2022-06-12 21:31:45.116046
# Unit test for method __str__ of class HostState

# Generated at 2022-06-12 21:31:53.304398
# Unit test for method add_tasks of class PlayIterator

# Generated at 2022-06-12 21:32:01.946236
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    obj = PlayIterator(play=play())

    # obj.play.get_blocks() == []
    state = HostState(name="test")
    assert obj.is_any_block_rescuing(state) == False

    obj.play.get_blocks().append(block())
    assert obj.is_any_block_rescuing(state) == False

    state = HostState(name="test", blocks=[
        block(rescue=[task()])
    ])
    assert obj.is_any_block_rescuing(state) == False

    state = HostState(name="test", blocks=[
        block(rescue=[task()])
    ], run_state=1)
    assert obj.is_any_block_rescuing(state) == True

    obj.play.get_blocks()[0].rescue.insert

# Generated at 2022-06-12 21:32:07.341131
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # get_failed_hosts() should always return a dict
    # get_failed_hosts() will return an empty dict if there are no failed hosts
    # get_failed_hosts() will return a dict with hosts set to True in the case that there are failed hosts

    # TODO: Test when hosts are added (w/o a task)

    # Test when no hosts are added
    checker = PlayIterator()
    assert checker.get_failed_hosts() == {}

    # Test when a single host is added
    checker = PlayIterator()
    checker.get_host_state(Host("testhost", play=Play()))
    assert checker.get_failed_hosts() == {}

    # Test when a single host is added and marked failed
    checker = PlayIterator()

# Generated at 2022-06-12 21:32:57.835054
# Unit test for method copy of class HostState
def test_HostState_copy():
    hs_orig = HostState([])
    hs_orig.cur_block = 1
    hs_orig.cur_regular_task = 2
    hs_orig.cur_rescue_task = 3
    hs_orig.cur_always_task = 4
    hs_orig.run_state = 5
    hs_orig.fail_state = 6
    hs_orig.did_rescue = True
    hs_orig.did_start_at_task = True
    hs_orig.tasks_child_state = HostState([])
    hs_orig.rescue_child_state = HostState([])
    hs_orig.always_child_state = HostState([])
    hs_orig.pending_setup = False

    hs_copy = hs_orig.copy()


# Generated at 2022-06-12 21:33:09.093519
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler

    def get_task(name):
        return Task.load(dict(name=name, action=dict(module='debug', args='msg=%s' % name)))


# Generated at 2022-06-12 21:33:16.522855
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    from ansible.playbook.play_context import PlayContext
    p = Play()
    p.hosts = ['localhost', 'otherhost']
    p.tasks = [Task()]
    pb = Playbook()
    pb._entries = [p]

    i = PlayIterator()
    i._play = p

    host_states = {
        'localhost' : HostState(blocks=[Block()], play=p, task_path=None, play_context=PlayContext(play=p)),
        'otherhost' : None,
    }
    i._host_states = host_states

    lh_state = host_states['localhost']
    assert lh_state == i.get_active_state(lh_state)

    lh_state.run_state = PlayIterator.ITERATING_TASKS


# Generated at 2022-06-12 21:33:17.666402
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    pass



# Generated at 2022-06-12 21:33:28.822315
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
  play = Play()
  play.hosts = [
    'localhost',
    ]
  play.roles = [
    'myrole1',
    'myrole2',
    ]
  play.tasks = [
    Task(action='fail',args={u'msg': u'Failed'}),
    Task(action='debug',args={u'msg': u'hello'}),
    ]
  play.roles[0].tasks = [
    Task(action='ping'),
    ]
  play.roles[1].tasks = [
    Task(action='shell',args={u'cmnd': u'/bin/true'}),
    Task(action='setup'),
    ]

# Generated at 2022-06-12 21:33:37.499951
# Unit test for method mark_host_failed of class PlayIterator
def test_PlayIterator_mark_host_failed():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    pb = Play()
    vm = VariableManager()
    inventory = Inventory(host_list=[])
    pi = PlayIterator(pb, vm, inventory)
    class TestTask(Task):
        def __init__(self, task_action):
            self._role = None
            self._ds = None
            self.name = None
            self.action = task_action
            self.loop = None
            self.when = None
            self.changed_when = None
            self.failed_when = None
            self.always_run = False
            self.register = None


# Generated at 2022-06-12 21:33:49.937300
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    import six
    import mock
    import copy
    import os
    import sys
    import ansible
    from ansible.module_utils.six import PY3
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    ansible.__version__ = '2.9.0.0'
    if PY3:
        builtin_module_name = 'builtins'
    else:
        builtin_module_name = '__builtin__'

    builtin_mock = mock.MagicMock(name='builtin_mock')
    sys.modules[builtin_module_name] = builtin_mock
    if PY3:
        builtin_mock.__dict__ = vars(builtins)

# Generated at 2022-06-12 21:33:52.261434
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    p = Play().load(os.path.join(fixtures_path, 'playbooks', 'play_with_roles.yml'), variable_manager={}, loader=loader)
    h = Host('test_host')
    p.add_host(h)

    pl = PlayIterator(p)
    assert pl.get_next_task_for_host(h) == None

# Generated at 2022-06-12 21:34:02.940901
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    hosts = [Host(name='foo')]
    play = Play().load(dict(
        name = "test play",
        hosts = 'foo',
        gather_facts = 'no',
        roles = [],
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
        ],
    ), variable_manager=VariableManager(), loader=MockLoader())

    tqm = TestTaskQueueManager(hosts=hosts, play=play)
    tqm._host_states[hosts[0].name] = HostState(host=hosts[0], blocks=[play.compile()])
    state = tqm.get_host_state(hosts[0])
    active_state = tqm.get_active_state(state)

    assert active_state.run

# Generated at 2022-06-12 21:34:05.387065
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    """pretty print HostState instance"""
    HOST_STATE = HostState([])
    print("HostState(%r)" % HOST_STATE._blocks)


# Generated at 2022-06-12 21:34:45.819675
# Unit test for method get_failed_hosts of class PlayIterator
def test_PlayIterator_get_failed_hosts():
    # test that we get a dict of failed hosts back with a single failed host
    host1 = Host('host1')
    host2 = Host('host2')
    hosts = [host1, host2]
    play = Play().load({}, variable_manager=VariableManager(), loader=DummyLoader())
    iterator = PlayIterator(play)
    iterator.mark_host_failed(host1)
    assert iterator.get_failed_hosts() == {host1: True}, "iterator.get_failed_hosts() should have returned a dict containing only host1"


# Generated at 2022-06-12 21:34:56.510117
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    from ansible.playbook import Play
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    blocks = [ Block(
        play=Play().load({
            'name': 'test play 3',
            'hosts': 'all',
            }),
        block=[
            Task().load({
                'action': 'check test 1',
                }),
            Task().load({
                'action': 'check test 2',
                }),
            ]
        )
    ]


# Generated at 2022-06-12 21:34:57.700775
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    pass



# Generated at 2022-06-12 21:34:58.303476
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
  pass

# Generated at 2022-06-12 21:35:06.003949
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    class MockVariableManager():
        def __init__(self):
            self.vars_cache = dict()
        def get_vars(self,play=None,host=None,task=None):
            return self.vars_cache
        def set_host_variable(self,host,var,value):
            self.vars_cache['hostvars'][host.name][var] = value
    class MockPlay():
        class MockStrategy():
            def get_hosts(self,pattern):
                return [host1,host2]
        def __init__(self,hosts):
            self.hosts = hosts
            self.basedir = '/playbasedir'
            self.roles_path = ['/playrolespath']
            self.role_path = '/playrolepath'

# Generated at 2022-06-12 21:35:15.821632
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():

    # Create an empty PlayIterator
    pi = PlayIterator()
    # Create an empty Play
    p = Play()
    # Create an empty PlayContext
    pc = PlayContext()
    # Create an empty Host
    h = Host()

    # Create an empty Task
    t = Task()

    # Set up the host state data
    pi._host_states = HostStates()
    hs = HostState(blocks=[])
    pi._host_states.add(h, hs)

    # Call the method with an empty task_list
    (hs_new, t_new) = pi.get_original_task(h, t)

    # Check the resulting HostState
    assert hs.run_state == hs_new.run_state
    assert hs._blocks == hs_new._blocks
    assert hs.cur_block

# Generated at 2022-06-12 21:35:26.601063
# Unit test for method __str__ of class HostState
def test_HostState___str__():
    blocks = []
    for name in ('block1', 'block2', 'block3'):
        block = Block()
        block.vars = {}
        block.vars['name'] = name
        blocks.append(block)

    state = HostState(blocks)
    state.cur_block = 1
    state.cur_regular_task = 2
    state.cur_rescue_task = 3
    state.cur_always_task = 4
    state.run_state = PlayIterator.ITERATING_SETUP
    state.fail_state = PlayIterator.FAILED_SETUP | PlayIterator.FAILED_TASKS
    state.pending_setup = False
    state.did_rescue = False
    state.did_start_at_task = False


# Generated at 2022-06-12 21:35:31.435806
# Unit test for method get_original_task of class PlayIterator
def test_PlayIterator_get_original_task():
    '''
    PlayIterator.get_original_task() expects:
    1 args: host
    2 args: host, task
    '''
    obj = PlayIterator()
    raises(Exception, obj.get_original_task, 'arg1')


# Generated at 2022-06-12 21:35:42.200588
# Unit test for method get_active_state of class PlayIterator
def test_PlayIterator_get_active_state():
    stats = dict()
    iterator = PlayIterator()
    state = HostState()
    state._blocks = [Block(rescue=None, always=None, block=[])]
    state.cur_block = 0
    state.cur_regular_task = 0
    state.cur_rescue_task = 0
    state.cur_always_task = 0
    state.did_rescue = False
    state.fail_state = 0
    state.run_state = iterator.ITERATING_TASKS
    state.tasks_child_state = None
    state.rescue_child_state = None
    state.always_child_state = None
    assert iterator.get_active_state(state)


# Generated at 2022-06-12 21:35:52.916101
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    class Block(object):
        def __init__(self, block, rescue=None, always=None):
            object.__setattr__(self, '_block', block)
            object.__setattr__(self, '_rescue', rescue)
            object.__setattr__(self, '_always', always)
        @property
        def block(self):
            return self._block
        @property
        def rescue(self):
            return self._rescue
        @property
        def always(self):
            return self._always
        def __getstate__(self):
            return self._block, self._rescue, self._always
        def __setstate__(self, state):
            (self._block, self._rescue, self._always) = state
        def __copy__(self):
            return self.__

# Generated at 2022-06-12 21:36:55.631771
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    pass

# Generated at 2022-06-12 21:37:06.129739
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # Create an instance of a dummy callback plugin
    results_callback_plugin = DummyCallbackModule()

    results_callback_plugin.on_setup()

    # Create an inventory with hosts, groups and variables using the inventory parser
    # InventoryManager has a default cache directory and cache filename but in this unit test we disable the cache
    inventory_manager = InventoryManager(loader=C.DEFAULT_LOADER, sources='localhost,')

    # Create a variable manager and add inventory and variable data
    variable_manager = VariableManager(loader=C.DEFAULT_LOADER, inventory=inventory_manager)

    # Create a play with a play strategy of linear and a play context of make_extra_global_vars

# Generated at 2022-06-12 21:37:13.778308
# Unit test for method add_tasks of class PlayIterator
def test_PlayIterator_add_tasks():
    host_name = "foo"
    play_name = "bar"
    play_hosts = [host_name]
    play_iterator = PlayIterator(play=dict(name=play_name, hosts=play_hosts), inventory=Inventory(hosts=[host_name]),
                                 loader=None, variable_manager=None, is_playbook=False, settings=C(None))
    assert not play_iterator._host_states
    play_iterator.add_tasks(Host(host_name), [dict(action=dict(module="ping", args=""), first_available_host=False)])
    assert not play_iterator._host_states
    play_iterator.get_next_task_for_host(Host(host_name))
    assert play_iterator._host_states[host_name]

# Generated at 2022-06-12 21:37:21.756420
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    play_ = Play()
    play_._play_hosts = dict()
    play_iterator = PlayIterator(play_)

    ansible_hosts = dict()
    ansible_hosts['host_1'] = Host(name='host_1')
    ansible_hosts['host_2'] = Host(name='host_2')
    play_iterator._hosts = ansible_hosts

    host_state_ = HostState()
    host_state_._play = play_
    host_state_._blocks = list()
    host_state_._blocks.append(Block())

    block_ = Block()
    block_.block = list()
    task_ = Task()
    task_.action = 'action_1'
    block_.block.append(task_)
    block_.rescue = list()

# Generated at 2022-06-12 21:37:31.247879
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    # setup
    p = Play().load(dict(
        name = "test play",
        hosts = "all",
        gather_facts = "no",
        tasks = [
            dict(action=dict(module="shell", args="ls /")),
            dict(action=dict(module="shell", args="ls /"), when="False"),
            dict(action=dict(module="shell", args="whoami")),
            dict(action=dict(module="shell", args="whoami"), register="shell_whoami")
            ]
        ), variable_manager=VariableManager(), loader=None)

    # get the first task, ensure it is correct
    (host, task) = p._iterator.get_next_task_for_host(p.hosts[0])
    assert isinstance(task, Task)
    assert task.action.action

# Generated at 2022-06-12 21:37:38.111018
# Unit test for method copy of class HostState
def test_HostState_copy():
    play_iter = PlayIterator()
    play_iter.load_playbook_from_file(data="""\
- hosts: localhost
  gather_facts: no
  tasks:
    - name: task1
    - name: task2
      rescue:
        - debug: msg="rescue task"
      always:
        - debug: msg="always task"
        - debug: msg="always task2"
    - name: task3
      rescue:
        - debug: msg="rescue task2"
      always:
        - debug: msg="always task3"
    - name: task4
""")
    play_iter.playbook._tasks = [t for t in play_iter.playbook._tasks if t.name != 'meta']

# Generated at 2022-06-12 21:37:48.541089
# Unit test for method get_host_state of class PlayIterator
def test_PlayIterator_get_host_state():
    '''
    Unit test for method get_host_state of class PlayIterator
    '''
    host_states = {'example_host1': HostState(blocks=[
            Block(role='example_role1', tasks=['task1', 'task2']),
            Block(role='example_role2', tasks=['task3', 'task4']),
            Block(role='example_role1', tasks=['task5', 'task6'])
        ]),
        'example_host2': HostState(blocks=[
            Block(role='example_role1', tasks=['task1', 'task2']),
            Block(role='example_role2', tasks=['task3', 'task4']),
            Block(role='example_role1', tasks=['task5', 'task6'])
        ])
    }
    host_

# Generated at 2022-06-12 21:38:00.935483
# Unit test for method get_next_task_for_host of class PlayIterator
def test_PlayIterator_get_next_task_for_host():
    host = MagicMock()
    iterator = PlayIterator()

    play = Play().load(dict(
        name = 'test play',
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='ok'))),
        ]
    ), variable_manager=VariableManager(), loader=DictDataLoader())

    iterator._play = play
    iterator._play._variable_manager = VariableManager()
    iterator._play._variable_manager.set_inventory(Inventory(host_list=[host]))
    iterator._play._hosts_remaining = [host]
    iterator._play._hosts_cache[host.name] = Host(name=host.name)

    host_state = MagicMock()
    host_state.fail_state = iterator

# Generated at 2022-06-12 21:38:06.895989
# Unit test for constructor of class PlayIterator
def test_PlayIterator():
    my_vars = dict(a=1, b=2)
    my_hosts = [1, 2, 3]
    my_play = dict(name='test-play', hosts='hosts', vars=my_vars)
    my_inventory = Inventory(hosts=my_hosts, play=my_play, vars=my_vars)

    iterator = PlayIterator(inventory=my_inventory)

    assert iterator._play.name == my_play['name']
    assert iterator.hosts == my_hosts

# Generated at 2022-06-12 21:38:09.521350
# Unit test for method is_any_block_rescuing of class PlayIterator
def test_PlayIterator_is_any_block_rescuing():
    printJsonData('Test PlayIterator is_any_block_rescuing()')
    it = PlayIterator()
    state = HostState(blocks=[])
    assert it.is_any_block_rescuing(state) == False