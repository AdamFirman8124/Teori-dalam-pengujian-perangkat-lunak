

# Generated at 2022-06-13 08:31:22.174401
# Unit test for method deserialize of class Play
def test_Play_deserialize():
  # test for method deserialize of class Play
  # returns str which is True
  # this test works without additional code
  return True

# Generated at 2022-06-13 08:31:27.511566
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    
    # play
    pl = Play()
    pl._ds = dict(vars_files=['/path/to/varfile1.yml','/path/to/varfile2.yml'])
    print(pl.get_vars_files())
   

# Generated at 2022-06-13 08:31:32.792074
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = "my_name"
    assert p.get_name() == "my_name"
    p.name = None
    p.hosts = "host1, host2"
    assert p.get_name() == p.hosts


# Generated at 2022-06-13 08:31:41.985771
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler

    # First we need to create a handler block
    handler_block = Block()

    # Then we need to create a handler that is added to the handler_block
    handler_1 = Handler()
    handler_1.name = 'a handler'

    handler_block.block.append(handler_1)

    role_1 = Role()
    role_1.run_handlers = True
    role_1._handlers = [handler_block]

    play = Play()
    play.roles = [role_1]

    handler_block_copy = play.compile_roles_handlers()

    assert len(handler_block_copy) == 1
    assert isinstance(handler_block_copy[0], Block)

# Generated at 2022-06-13 08:31:52.818604
# Unit test for method get_name of class Play
def test_Play_get_name():
    import ansible.playbook
    host_list = ['localhost', '127.0.0.1', '127.0.0.1']
    # Case 1: empty host list
    host_list = []
    playbook = ansible.playbook.PlayBook(loader=None, variable_manager=None, options=None, passwords=None)
    play = ansible.playbook.Play(playbook=playbook, name='test_play', loader=None, variable_manager=None, options=None, passwords=None)
    play.vars = {'hosts':host_list}
    assert play.get_name() == ''
    # Case 2: non-empty host list
    host_list = [u'localhost', u'127.0.0.1', u'127.0.0.1']

# Generated at 2022-06-13 08:32:01.005708
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create Play object.
    p = Play()

    # Create Role objects and assign to Play.roles.
    p.roles = []
    for i in range(0, 3):
        r = Role()
        p.roles.append(r)

    # Add handler, meta, and task blocks to the roles.
    for r in p.roles:
        # Create Block object, assign handler tasks, and append to Role.
        b1 = Block()
        b1.block = [{'action': {'__ansible_action__': 'handler', '__ansible_arguments__': 'test_handler'}}]
        r.handlers = [b1]

        # Create Block object, assign meta task, and append to Role.
        b2 = Block()

# Generated at 2022-06-13 08:32:02.013617
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:32:14.801214
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = "test_play"
    assert play.name == "test_play", "The name of the play is not 'test_play'"
    play.name = None
    play.hosts = "localhost"
    assert play.name == "localhost", "The name of the play is not 'localhost'"
    play.name = None
    play.hosts = ["localhost"]
    assert play.name == "localhost", "The name of the play is not 'localhost'"
    play.hosts = ["localhost, ", "127.0.0.1"]
    assert play.name == "localhost, 127.0.0.1", "The name of the play is not 'localhost, 127.0.0.1'"

# Generated at 2022-06-13 08:32:17.672414
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.tasks = [{'foo': 'bar'}]
    assert p.get_tasks() == [{'foo': 'bar'}]



# Generated at 2022-06-13 08:32:24.694750
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    from ansible.plugins.action import ActionBase

    # Data
    class DummyModule(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return super(DummyModule, self).run(task_vars=task_vars)


    # Creating a single play
    p = Play()
    p.name = 'Single Play'
    p.hosts = 'local'
    p.connection = 'local'

    # Adding a role
    r = Role()
    r.name = 'test'

# Generated at 2022-06-13 08:32:49.184876
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    playbook = """
    - name: test
      hosts: localhost
      connection: local
      gather_facts: no

      tasks:
        - name: debug1
          debug: msg='executing task 1'
        - name: debug2
          debug: msg='executing task 2'
        - name: debug3
          debug: msg='executing task 3'
          when: not failed_when
        - name: debug4
          debug: msg='executing task 4'
    """
    play = Play.load(data=yaml.safe_load(playbook), variable_manager=VariableManager(), loader=DataLoader())
    tasks = play.get_tasks()
    assert len(tasks) == 4
    assert tasks[0].name == 'debug1'
    assert tasks[1].name == 'debug2'

# Generated at 2022-06-13 08:32:57.504025
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    class MockRole(Role):
        def _getattr_handler(self, name):
            return self._handlers

    play = Play()
    play.handlers = [{'name': 'handler_1'}, {'name': 'handler_2'}, {'name': 'handler_3'}]
    role = MockRole()
    role._handlers = [{'name': 'handler_4'}, {'name': 'handler_5'}, {'name': 'handler_6'}]
    role.from_include = False
    play.roles = [role]

    result = play.compile_roles_handlers()
    expect = [{'name': 'handler_4'}, {'name': 'handler_5'}, {'name': 'handler_6'}]

    assert result == expect

# Generated at 2022-06-13 08:33:10.022677
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    
    # loaders
    loader = DataLoader()
    variable_manager = VariableManager()
    
    # inventory
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    
    # action
    action_loader.add_directory('./tests/fixtures/action_plugins')
    
    # install display
    display = Display()
    display.verbosity = 2
    

    
    # blocks
    pre_tasks

# Generated at 2022-06-13 08:33:26.072221
# Unit test for method deserialize of class Play
def test_Play_deserialize():
  from ansible.parsing.dataloader import DataLoader
  from ansible.inventory.manager import InventoryManager
  from ansible.vars.manager import VariableManager
  from ansible.playbook.play import Play
  from ansible.plugins.loader import action_loader
  from ansible.inventory.host import Host
  from ansible.inventory.group import Group
  from ansible.plugins.loader import module_loader
  from ansible.plugins.loader import lookup_loader
  from ansible.plugins.callback import CallbackBase
  from ansible.module_utils._text import to_bytes
  import json
  # Get the object.
  sample_data = "./sample_play.json"

# Generated at 2022-06-13 08:33:39.109851
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    VARS = {
        u'foo': u'bar'
    }

    PLAYBOOK = u'''
- hosts: localhost
  roles:
    - role: role1
      vars:
        baz: biz
    - role: role2  
    - role: role3
    - name: include_role
      import_role:
        name: role4
        vars:
          baz: biz
    - name: include_role
      include_role:
        name: role5
        vars:
          baz: biz
'''
    FROM_INCLUDE = {
        u'role2': False,
        u'role4': True,
        u'role5': True,
        u'role1': False,
        u'role3': False
    }

    ROLE_

# Generated at 2022-06-13 08:33:50.440468
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.playbook.base import Base
    from ansible.playbook.block import Block

    play = Play()

    assert 'remote_user' not in play._ds
    play._ds = {'user': 'foobar'}
    assert 'user' in play._ds
    assert 'remote_user' not in play._ds
    play.preprocess_data(play._ds)
    assert 'user' not in play._ds
    assert 'remote_user' in play._ds
    assert play._ds['remote_user'] == 'foobar'


# Generated at 2022-06-13 08:33:51.485463
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass



# Generated at 2022-06-13 08:33:58.604123
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    """
    make sure the special case of a single vars_file works
    """
    p = Play()

    # non-string should be treated as a list
    p.vars_files = ['/dev/null']
    assert p.get_vars_files()
    p.vars_files = '/dev/null'
    assert p.get_vars_files()
    p.vars_files = '/dev/null2'
    assert p.get_vars_files()

# Generated at 2022-06-13 08:34:12.164647
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Test with a valid Play
    play = Play()
    play.vars = {'test': 'value'}
    task1 = Task()
    task1_block1 = Task()
    task2 = Task()
    task2_block2 = Task()
    task1_block1.set_loader(Mock())
    task2_block2.set_loader(Mock())
    task1_block1.post_validate({'debug': 'msg="{{ test }}"'}, Mock(), play=play)
    task2_block2.post_validate({'debug': 'msg="{{ test }}"'}, Mock(), play=play)
    task1.action = Task.LOAD_TASK_META_ACTION
    task1.post_validate(dict(meta='flush_handlers'), Mock(), play=play)
    task

# Generated at 2022-06-13 08:34:19.706010
# Unit test for method preprocess_data of class Play

# Generated at 2022-06-13 08:34:39.980702
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    play.vars = {'var_name' : 'value'}
    play.roles = [{'role_name' : 'value'}]
    play._included_path = 'some/path'
    play._action_groups = {'group_name' : ['action_name']}
    play._group_actions = {'action_name' : ['group_name']}
    data = play.serialize()
    assert data.get('vars') == dict(var_name='value')
    assert len(data.get('roles')) == 1
    assert data.get('included_path') == 'some/path'
    assert data.get('action_groups') == dict(group_name=['action_name'])

# Generated at 2022-06-13 08:34:45.477742
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Initialize a play module object
    play_obj = Play()
    # Call its method deserialze
    return_data = play_obj.deserialize(data={})
    # Assert
    assert return_data == {'included_path': None, 'group_actions': {}, 'action_groups': {}}


# Generated at 2022-06-13 08:34:55.496140
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    block_list = []
    block_list.append(Block(name='test1', play=play))
    block_list.append(Block(name='test2', play=play))
    block_list.append(Block(name='test3', play=play))

    play._pre_tasks = block_list
    play._post_tasks = block_list
    play._tasks = block_list

    tasklist = play.get_tasks()

    assert tasklist == block_list
    assert len(tasklist) == 3



# Generated at 2022-06-13 08:35:06.010713
# Unit test for method serialize of class Play

# Generated at 2022-06-13 08:35:09.490433
# Unit test for method get_name of class Play
def test_Play_get_name():
    with open("../../../test/unit/parse/test_data/test_play_json.json", "r") as json_data:
        data = json.load(json_data)

    p = Play()
    p.load_data(data)
    assert p.get_name() == 'all'


# Generated at 2022-06-13 08:35:10.255106
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    pass



# Generated at 2022-06-13 08:35:12.185673
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    result = play.get_tasks()
    assert result == [], 'Expected empty list'

# Generated at 2022-06-13 08:35:24.657525
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

# Generated at 2022-06-13 08:35:28.087493
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
  vars_files = ['var1', 'var2']
  p = Play()
  p.vars_files = vars_files
  assert p.get_vars_files() == vars_files, 'get_vars_files returns the wrong vars_files list'


# Generated at 2022-06-13 08:35:37.127803
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():

    vars_files_1 = "my_vars_files_1"
    vars_files_2 = "my_vars_files_2"

    p = Play()
    p.vars_files = vars_files_1
    assert p.get_vars_files() == [vars_files_1]

    p.vars_files = [vars_files_1, vars_files_2]
    assert p.get_vars_files() == [vars_files_1, vars_files_2]



# Generated at 2022-06-13 08:35:55.414689
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    test_Play_object = Play()
    test_Play_object.pre_tasks = [1,2,3]
    test_Play_object.tasks = [1,2,3]
    test_Play_object.post_tasks = [1,2,3]

    assert test_Play_object.get_tasks() == [1,2,3, 1,2,3, 1,2,3]


# Generated at 2022-06-13 08:36:01.394212
# Unit test for method serialize of class Play
def test_Play_serialize():
    import ansible.playbook
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.parsing.dataloader

    p = Play()
    pb = ansible.playbook.PlayBook()
    pb.set_loader(ansible.parsing.dataloader.DataLoader())
    pb.set_variable_manager(ansible.vars.manager.VariableManager())
    pb.set_inventory(ansible.inventory.manager.InventoryManager(pb._loader, pb._variable_manager))
    assert pb is not None
    assert p is not None

    data = p.serialize()
    assert data is not None
    p2 = Play()
    assert p2 is not None
    p2.deserialize(data)


# Generated at 2022-06-13 08:36:02.537862
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass


# Generated at 2022-06-13 08:36:09.391371
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Test Play.get_vars_files.
    # Play.get_vars_files takes list and return the list
    vars_files = ['one.yml', 'two.yml']
    play = Play()
    play.vars_files = vars_files
    assert vars_files == play.get_vars_files()
    # Play.get_vars_files takes string and return the list
    vars_files = 'one.yml'
    play = Play()
    play.vars_files = vars_files
    assert [vars_files] == play.get_vars_files()

Play = Play()

# Generated at 2022-06-13 08:36:12.550366
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p.roles = ['sample']
    p.compile_roles_handlers()
    assert p is not None, "code should not fail"
    assert p.roles[0]._handlers == [{'name': 'Test', 'include': 'somefile.yaml', 'tags': ['debug', 'handler']}], "code should not fail"


# Generated at 2022-06-13 08:36:22.274900
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():

    pb_data = dict(
        name = 'Test Playbook',
        hosts = 'localhost',
        gather_facts = 'no',
        pre_tasks = [],
        tasks = [],
        post_tasks = [],
        handlers = [],
        vars = {},
        roles = []
    )

    #play = Play()
    play = Play().load(pb_data, variable_manager=None)
    print(play.get_tasks())
    print(play.serialize())
    print(play._ds)


if __name__ == '__main__':
    test_Play_get_tasks()

# Generated at 2022-06-13 08:36:27.173140
# Unit test for method get_name of class Play
def test_Play_get_name():
    class Play_test(Play):
        _name = FieldAttribute(isa='string', default='test_play', always_post_validate=True)

    obj = Play_test()
    assert obj.get_name() == 'test_play'
    assert obj._Play__repr__() == 'test_play'


# Generated at 2022-06-13 08:36:40.412962
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible import context
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:36:45.010895
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    ds = {'name': 123, 'hosts': 'all', 'user': 'root'}
    p.preprocess_data(ds)
    assert isinstance(ds, dict) and 'user' not in ds

# Generated at 2022-06-13 08:36:47.445285
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.hosts = 'group_name'
    assert play.get_name() == 'group_name'


# Generated at 2022-06-13 08:36:57.854704
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    obj = Play()
    data = dict()
    obj.deserialize(data)


# Generated at 2022-06-13 08:37:06.778455
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    #
    # Unit test for method get_vars_files of class Play
    #
    play = Play()
    play.vars_files = 'var/files'
    assert play.get_vars_files() == ['var/files']
    #
    # test when vars_files is a list
    #
    list_play = Play()
    list_play.vars_files = ['var/files', '/etc/passwd']
    assert list_play.get_vars_files() == ['var/files', '/etc/passwd']
    #
    # test when vars_files is None
    #
    play_none = Play()
    play_none.vars_files = None
    assert play_none.get_vars_files() == []
    #
    # test when vars_files is

# Generated at 2022-06-13 08:37:18.263500
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    temp_play = Play()
    temp_play.compile()
    expected_list = ['task_1', 'task_2', 'task_3']
    actual_list = temp_play.get_tasks()
    assert(expected_list == actual_list)
    # Sample test using unittest
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    # Sample test using unittest
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

# Test if Play.get_tasks method returns an output
# Test if Play.get_tasks method returns the expected output

# Generated at 2022-06-13 08:37:29.985496
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    def test_case():
        class Task:
            def __init__(self, block, always, rescue):
                self.block = block
                self.always = always
                self.rescue = rescue
        pre_tasks = [Task(None, None, None) for _ in range(1, 3)]
        tasks = [Task(None, None, None) for _ in range(1, 3)]
        post_tasks = [Task(None, None, None) for _ in range(1, 4)]
        p = Play()
        p.pre_tasks = pre_tasks
        p.tasks = tasks
        p.post_tasks = post_tasks
        tasks_ = p.get_tasks()
        __logger__.debug(str(tasks_))
    test_case()


# Generated at 2022-06-13 08:37:39.900107
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():

    test_play = AnsiblePlay().load(dict(
        name="test_play",
        hosts="test_play_hosts",
        tasks=[]
    ))

    test_play.pre_tasks = [AnsibleTask().load(dict(
        name="test_pre_task",
        action="test_pre_task_action"
    ))]

    test_play.tasks = [AnsibleTask().load(dict(
        name="test_task",
        action="test_task_action"
    ))]

    test_play.post_tasks = [AnsibleTask().load(dict(
        name="test_post_task",
        action="test_post_task_action"
    ))]

    assert len(test_play.get_tasks()) == 3

# Generated at 2022-06-13 08:37:51.586014
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    '''Unit test for method preprocess_data of class Play'''

# Generated at 2022-06-13 08:38:02.210635
# Unit test for method deserialize of class Play

# Generated at 2022-06-13 08:38:06.548889
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    preprocess_data_result = Play.preprocess_data({'user': 'root'})
    assert preprocess_data_result == {'remote_user': 'root'}

# Unit tests for method _load_vars_prompt of class Play

# Generated at 2022-06-13 08:38:15.874611
# Unit test for constructor of class Play
def test_Play():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    ds = dict(
        name='foobar',
        hosts='all',
    )
    loader = DataLoader()
    inv_mgr = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inv_mgr)

    p = Play().load(ds=ds, variable_manager=variable_manager, loader=loader)

    assert p.name == 'foobar'
    assert p.hosts == 'all'
    assert p.connection == 'smart'
    assert p.port == None
    assert p.gather_facts == C.DEFAULT_GATHER_FACTS

# Generated at 2022-06-13 08:38:24.469989
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():

    vars_data = dict(a=1,b=1,c=1)
    post_tasks = [dict(name='post_task1', a=1), dict(name='post_task2', b=2)]
    tasks = [dict(name='task1', c=1), dict(name='task2', d=2)]
    pre_tasks = [dict(name='pre_task1', e=1), dict(name='pre_task2', f=2)]
    roles = ['role1', 'role2']
    play = Play(name='name', vars=vars_data, hosts='hosts', post_tasks=post_tasks, tasks=tasks, pre_tasks=pre_tasks, roles=roles)

# Generated at 2022-06-13 08:38:57.325737
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Arrange
    test_play = Play()

    test_play_data = dict(
        name="test_play_name",
        hosts="test_play_hosts",
        roles=["test_play_roles"],
        handler_roles=["test_play_handler_roles"],
        handlers=[dict(test_handler_data)]
    )

    test_role_data = dict(
        name="test_role_name",
        tasks=["test_role_tasks"],
        handlers=[dict(test_handler_data)],
        include_role=dict(include_role_data)
    )

    test_handler_data = dict(
        name="test_handler_name",
        tags="test_handler_tags",
        tasks=["test_handler_tasks"]
    )

    test_block

# Generated at 2022-06-13 08:39:00.529995
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    class MyPlay(Play):
        def compile_roles_handlers(self):
            print("compile_roles_handlers called from test")
            return super(MyPlay, self).compile_roles_handlers()
    p = MyPlay()
    p.compile_roles_handlers()


# Generated at 2022-06-13 08:39:10.885951
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    def compile_roles_handlers():
        block_list = []

        if len(self.roles) > 0:
            for r in self.roles:
                if r.from_include:
                    continue
                block_list.extend(r.get_handler_blocks(play=self))

        return block_list
    # Play:
    Play._compile_roles_handlers = compile_roles_handlers
    Play.roles = [
        'role-1',
        'role-2'
    ]
    assert Play._compile_roles_handlers(Play) == [
        'role-1.get_handler_blocks()',
        'role-2.get_handler_blocks()'
    ]

# Generated at 2022-06-13 08:39:18.003880
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = []
    expected = []
    actual = p.get_vars_files()
    assert actual == expected

    p.vars_files = None
    expected = []
    actual = p.get_vars_files()
    assert actual == expected

    p.vars_files = [1]
    expected = [1]
    actual = p.get_vars_files()
    assert actual == expected

# Generated at 2022-06-13 08:39:23.028559
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play_obj = Play()
    def fake_compile_roles_handlers():
        return []
    setattr(play_obj, 'compile_roles_handlers', fake_compile_roles_handlers)
    assert play_obj.compile_roles_handlers() is not None

# Generated at 2022-06-13 08:39:28.522871
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    setattr(p, 'vars_files', None)
    assert p.get_vars_files() == []
    setattr(p, 'vars_files', '/path/to/file')
    assert p.get_vars_files() == ['/path/to/file']
    setattr(p, 'vars_files', ['/path/to/file1', '/path/to/file2'])
    assert p.get_vars_files() == ['/path/to/file1', '/path/to/file2']



# Generated at 2022-06-13 08:39:31.530320
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = "vars_files"
    assert play.get_vars_files() == ["vars_files"]

# Generated at 2022-06-13 08:39:45.154788
# Unit test for method serialize of class Play
def test_Play_serialize():
    from ansible.parsing.dataloader import DataLoader

    _loader = DataLoader()
    _variable_manager = VariableManager()

    p = Play.load(
        dict(
            name="Test Play",
            hosts=["127.0.0.1"],
            gather_facts="no",
            roles=["test_role"],
            vars={
                "key1": "val1",
            },
        ),
        loader=_loader,
        variable_manager=_variable_manager
    )
    data = p.serialize()
    assert data
    assert 'roles' in data
    assert data['roles'][0]
    assert data['roles'][0]['tasks']

# Generated at 2022-06-13 08:39:47.781342
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.compile_roles_handlers()
    return play.compile_roles_handlers() is play.compile_roles_handlers()

# Generated at 2022-06-13 08:39:54.079399
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []

    play = Play()
    play.vars_files = None
    assert play.get_vars_files() == []

    play = Play()
    play.vars_files = 'test.yaml'
    assert play.get_vars_files() == ['test.yaml']

    play = Play()
    play.vars_files = ['test.yaml', 'test2.yaml']
    assert play.get_vars_files() == ['test.yaml', 'test2.yaml']

# Generated at 2022-06-13 08:40:17.477595
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    b1 = Block(task_include='task1')
    b2 = Block(task_include='task2')
    p.add_task

# Generated at 2022-06-13 08:40:18.277197
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass # TODO: Write tests for Play


# Generated at 2022-06-13 08:40:24.638162
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = [[{"action": "shell", "args": "cmd", "name": "fist"}, 
                    {"action": "shell", "args": "cmd2", "name": "second"}, 
                    {"action": "shell", "args": "cmd3", "name": "third"}]]

    assert play.get_tasks() == [[{"action": "shell", "args": "cmd", "name": "fist"}, 
                    {"action": "shell", "args": "cmd2", "name": "second"}, 
                    {"action": "shell", "args": "cmd3", "name": "third"}]]


# Generated at 2022-06-13 08:40:26.848774
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    print("Test Play get tasks")
    play = Play()
    play.compile()

# Generated at 2022-06-13 08:40:39.473915
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    '''
    Unit test for method "get_tasks" of class "Play"
    '''
    play = Play()
    play.pre_tasks = [
        {'name': 'Create message'},
        {'name': 'Create signature'},
        {'name': 'Build message and signature'},
    ]
    play.tasks = [
        {'name': 'Create timestamp'},
        {'name': 'Create nonce'},
        {'name': 'Build request'},
    ]
    play.post_tasks = [
        {'name': 'Send request'},
        {'name': 'Store response'},
    ]

# Generated at 2022-06-13 08:40:52.015029
# Unit test for method get_name of class Play
def test_Play_get_name():
    testdesc =  "testing "+test_Play_get_name.__name__+" method"
    print("("+test_Play_get_name.__name__+")", testdesc.ljust(60,'-'))

    test = Play()
    assert test.get_name() == "", testdesc+"get_name returned empty string if name attribute is not set."

    test.name = "playbook.yml"
    assert test.get_name() == "playbook.yml", testdesc+"get_name returned wrong value."

    test.name = None
    test.hosts = "hosts.yml"
    assert test.get_name() == "hosts.yml", testdesc+"get_name returned wrong value."


# Generated at 2022-06-13 08:40:58.727758
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from .task import Task
    from .block import Block
    from .host import Host
    from .play_context import PlayContext
    from .playbook import Playbook
    try:
        from .loader import DataLoader
    except ImportError:
        from ansible.parsing.dataloader import DataLoader
    try:
        from .vars import VariableManager
    except ImportError:
        from ansible.vars import VariableManager
    try:
        from .inventory import Inventory
    except ImportError:
        from ansible.inventory import Inventory
    try:
        from .inventory import InventoryDirectory
    except ImportError:
        from ansible.inventory.dir import InventoryDirectory
    try:
        from .inventory import Host
    except ImportError:
        from ansible.inventory.host import Host

    test_playbook = Playbook()


# Generated at 2022-06-13 08:41:00.984685
# Unit test for method get_tasks of class Play
def test_Play_get_tasks(): 
    play = Play()
    print(play.get_tasks())

# Generated at 2022-06-13 08:41:08.869414
# Unit test for constructor of class Play
def test_Play():
    # check if a play created empty and has no roles
    play = Play()
    assert not play.roles

    # check if a play created with data
    yaml_data = '''
        - hosts: localhost
          roles:
            - myrolename
    '''
    play = Play.load(data=yaml_data, variable_manager=VariableManager(), loader=DataLoader())
    assert play.roles