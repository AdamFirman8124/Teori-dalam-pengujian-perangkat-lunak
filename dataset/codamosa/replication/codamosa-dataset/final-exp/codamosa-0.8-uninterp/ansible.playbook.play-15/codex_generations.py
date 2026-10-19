

# Generated at 2022-06-13 08:31:36.550847
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Tests if the method Play.deserialize can handle the type of different
    # dictionary key and value
    #
    # Args:
    #    None
    #
    # Returns:
    #    None
    #
    # Raises:
    #    None

    # method variables
    play = Play()
    play.deserialize({"hosts": "localhost", "name": "Test", "roles": [{"name": "test.test", "default_vars": {"name": "test"}, "vars": {}}], "collections": [], "vars_files": [], "registered_variables": {}, "vars": {}, "included_path": ".", "action_groups": {}, "group_actions": {}})
    assert True

# Generated at 2022-06-13 08:31:37.239193
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass



# Generated at 2022-06-13 08:31:49.230653
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
        """
        Checking if the method get_vars_files() of class Play work properly
        """
        playbook_path = 'playbook.yml'
        p = Play.load(
            dict(
                name='fake play',
                hosts='all',
                connection='local',
                gather_facts='no',
                vars_files='setup.yml',
                tasks=[
                    dict(action='set_fact', args=dict(result='pong')),
                ]
            ),
            variable_manager=VariableManager(),
            loader=DataLoader()
        )
        assert(p.get_vars_files() == 'setup.yml')
        
if __name__ == "__main__":
    test_Play_get_vars_files()

# Generated at 2022-06-13 08:31:49.875778
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:31:56.624778
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.parsing.vault import VaultLib
    # Instantiate Play
    play = Play()
    vault_password = VaultLib().decrypt(open("../vault_password", "rb").read())
    # Test case 1
    ds = dict()
    ds['hosts'] = ['webservers', 'dbservers']
    ds['vars'] = dict()
    ds['vars']['foobar'] = ("password", "mypass")
    ds['vars']['foobar'] = dict()
    ds['vars']['foobar']['key'] = "value"
    assert isinstance(play.preprocess_data(ds), dict)


# Generated at 2022-06-13 08:32:09.624711
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.set_name('test_name')
    assert p.get_name() == 'test_name'
    p.name = ''
    assert p.get_name() == ''
    # only validate 'hosts' if a value was passed in to original data set.
    p.load_data({
        'hosts': ['192.168.1.1'],
    })
    assert p.get_name() == '192.168.1.1'
    p.load_data({
        'hosts': ['192.168.1.1', '192.168.1.2']
    })
    assert p.get_name() == '192.168.1.1,192.168.1.2'



# Generated at 2022-06-13 08:32:18.236515
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    h1 = Handler()
    h2 = Handler()
    h3 = Handler()
    r1 = Role()
    r1.handlers = [h1]
    r2 = Role()
    r2.handlers = [h2]
    r3 = Role()
    r3.handlers = [h3]
    play.roles = [r1, r2, r3]
    assert play.compile_roles_handlers() == [h1, h2, h3]


# Generated at 2022-06-13 08:32:33.174609
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()

# Generated at 2022-06-13 08:32:42.865717
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = {
        'name': 'test',
        'roles': [
            {
                'name': 'role_1',
                'tasks': [
                    {
                        'name': 'task_1',
                    }
                ],
                'handlers': [
                    {
                        'name': 'handler_1',
                    }
                ]
            },
            {
                'name': 'role_2',
                'tasks': [
                    {
                        'name': 'task_2',
                    }
                ],
                'handlers': [
                    {
                        'name': 'handler_2',
                    }
                ]
            },
        ]
    }
    play = Play.load(data)
    new_play = play.copy()
    assert new_play.name == 'test'
    assert new_play

# Generated at 2022-06-13 08:32:47.486314
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = [1,2]
    play.tasks = [3,4]
    play.post_tasks = [5,6]
    assert play.get_tasks() == [1,2,3,4,5,6]



# Generated at 2022-06-13 08:33:09.453984
# Unit test for constructor of class Play
def test_Play():
    # Create a Play
    myPlay = Play()

    # Check for required class variable
    assert myPlay.ROLE_CACHE is not None

    # Check for required class variable
    assert myPlay._included_conditional is None
    assert myPlay._included_path is None
    assert myPlay._removed_hosts == []
    assert myPlay._action_groups == {}
    assert myPlay.only_tags == ('all',)
    assert myPlay.skip_tags == set()

    # Call toString() method
    myPlay.__str__()

    # Call get_name() method
    myPlay.get_name()

    # Check for required class variable
    assert myPlay.ROLE_CACHE == {}

    # Create a Play
    myPlay = Play()

    # Call get_name() method
   

# Generated at 2022-06-13 08:33:13.119419
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    hostvars = {}
    play = Play()
    data = 'test_data'
    play.preprocess_data(data)

# Generated at 2022-06-13 08:33:16.407256
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play1 = Play()
    assert play1.get_vars_files() == []
    play1.vars_files = None
    assert play1.get_vars_files() == []
    play1.vars_files = 'file1'
    assert play1.get_vars_files() == ['file1']
    play1.vars_files = ['file2', 'file3']
    assert play1.get_vars_files() == ['file2', 'file3']


# Generated at 2022-06-13 08:33:27.291621
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
    Unit test for method compile_roles_handlers of class Play
    '''

    AnsibleCore._expect_exception = True

    # Setup
    p = Play()
    p.roles = [
        Role(), Role(), Role(), Role(),
        Role(), Role(), Role(), Role(),
        Role(), Role(), Role(), Role(),
        Role(), Role(), Role(), Role(),
    ]
    # Testing
    result = p.compile_roles_handlers()

    # Verify
    assert result is None


# Generated at 2022-06-13 08:33:30.131508
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
  # Execute on_play_start method of Play
  p = create_play()
  # Execute method get_tasks of class Play with play p
  p.get_tasks()


# Generated at 2022-06-13 08:33:35.711714
# Unit test for method serialize of class Play
def test_Play_serialize():
    from ansiblelint import RulesCollection
    from ansiblelint.runner import Runner
    play = Play()
    collection = RulesCollection.create_from_directory('test/rules')
    runner = Runner(collection)
    play.serialize()
    print(runner.run(play))

# Generated at 2022-06-13 08:33:39.889826
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    ds = {"hosts": "all"}
    data = play.preprocess_data(ds)
    assert data == {"hosts": "all"}

# Generated at 2022-06-13 08:33:44.195189
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = {'some': 'value'}
    test_obj = Play()
    test_obj.preprocess_data(data=ds)
    # test __dict__
    assert test_obj.__dict__['_ds']['some'] == 'value'

# Generated at 2022-06-13 08:33:50.864642
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Setup data for test case
    data = {'hosts': 'localhost'}
    # Execute target method
    p = Play()
    p.preprocess_data(data)

    actual_result = p._ds.get('hosts')

    expected_result = 'localhost'
    assert(actual_result == expected_result)

# Generated at 2022-06-13 08:33:53.691051
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    my_play = Play()
    my_play.compile_roles_handlers()



# Generated at 2022-06-13 08:34:10.957518
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = None
    assert play.get_vars_files() == []

    play.vars_files = 'a/b/c'
    assert play.get_vars_files() == ['a/b/c']

    play.vars_files = ['a', 'b', 'c']
    assert play.get_vars_files() == ['a', 'b', 'c']



# Generated at 2022-06-13 08:34:19.131441
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play_ds = dict(
        name="test play",
        hosts='all',
        gather_facts='no',
        roles=[
            dict(
                import_role=dict(
                    name="foo",
                    tasks_from="main.yml"
                )
            )
        ],
        tasks=[
            dict(
                debug=dict(
                    msg="hello world"
                )
            )
        ]
    )

# Generated at 2022-06-13 08:34:29.389501
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = createPlay()

    play.handlers = [Block(
        task_include('notify.yml', name='notify'),
    )]

    # no roles defined
    assert play.compile_roles_handlers() == play.handlers

    play.roles = [
        createRole(
            handlers=[
                Block(task_include('notify.yml', name='notify')),
            ],
        ),
        createRole(
            handlers=[
                Block(
                    task_include('notify.yml', name='notify'),
                    task_include('notify.yml', name='notify'),
                ),
            ],
        ),
    ]


# Generated at 2022-06-13 08:34:40.395074
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play_data={
        'name': 'Play_Test',
        'hosts': 'all',
        'gather_facts': 'no',
        'connection': 'local',
        'roles': [
            {
                'role': '../common/control_host',
                'control_host': '{{ control_host }}'
            },
            {
                'role': '../common/target_hosts',
                'target_hosts': '{{ target_hosts }}',
                'test_id': '{{ test_id }}'
            }
        ],
        'vars_files': [
            '../../inventory/group_vars/{{ target_hosts }}'
        ]
    }

# Generated at 2022-06-13 08:34:54.285729
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Create Play object to test:
    data = {'foo': 'bar'}
    fake_loader = None
    fake_var_manager = None
    p = Play()
    p.load(ds=data, loader=fake_loader, variable_manager=fake_var_manager)
    # Create data structure to test:
    # test1:
    expected_result1 = []
    # test2:
    data_1 = Task()
    data_2 = Task()
    expected_result2 = [data_1, data_2]
    # test3:
    data_3 = Block()
    data_4 = Task()
    data_5 = Task()
    data_3.block = [data_4, data_5]

# Generated at 2022-06-13 08:34:55.147829
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert True

# Generated at 2022-06-13 08:34:59.328271
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    result = play._load_roles('play', [{'hosts': 'host1'}])
    assert result
    handlers = play.compile_roles_handlers()
    assert handlers

# Generated at 2022-06-13 08:35:06.275473
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    task1 = dict(action='fake')
    task2 = dict(action='fake')
    task3 = dict(action='fake')
    task4 = dict(action='fake')

    task1 = Task()
    task2 = Task()
    task3 = Task()
    task4 = Task()

    block1 = Block()
    block1.block = [task1, task2]
    block1.rescue = [task3, task4]

    tasklist = [block1]
    assert tasklist == Play().get_tasks()

# Generated at 2022-06-13 08:35:08.635108
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Create an instance of Play
    play = Play()
    # Execute the method
    result = play.get_tasks()
    # Verify the result
    assert isinstance(result, list)


# Generated at 2022-06-13 08:35:16.934687
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()

    assert play.get_vars_files() == []

    play.vars_files = None
    assert play.get_vars_files() == []

    play.vars_files = 'testfile1'
    res = play.get_vars_files()
    assert len(res) == 1
    assert res[0] == 'testfile1'

    play.vars_files = ['testfile2', 'testfile3']
    res = play.get_vars_files()
    assert len(res) == 2
    assert 'testfile2' in res
    assert 'testfile3' in res


# Generated at 2022-06-13 08:35:59.371473
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    with pytest.raises(AnsibleParserError):
        play = Play()
        play.vars_files="foo"
        play.get_vars_files()

    play = Play()
    play.vars_files=[{"some value"}, {"some other value"}]
    assert play.get_vars_files() == [{"some value"}, {"some other value"}]

    play = Play()
    play.vars_files=[{"some value"}]
    assert play.get_vars_files() == [{"some value"}]


# Generated at 2022-06-13 08:36:04.081432
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    assert p.get_vars_files() == []
    #p.vars_files = ['/usr/share/ansible/user.yml']
    #assert p.get_vars_files() == '/usr/share/ansible/user.yml'

Play._load_ds = Play._load_roles

# Generated at 2022-06-13 08:36:11.572756
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # set up a Play instance
    p = Play()
    p.vars = {}
    p.hosts = "all"
    # init pre_tasks, tasks, post_tasks
    p.pre_tasks = [{'name': 'pre task 0'}, {'name': 'pre task 1'}]
    p.tasks = [{'name': 'task 0'}, {'name': 'task 1'}]
    p.post_tasks = [{'name': 'post task 0'}, {'name': 'post task 1'}]
    # load all tasks
    p.load_tasks()
    # test
    tasklist = p.get_tasks()
    assert(len(tasklist) == 6)
    assert(tasklist[0].name == "pre task 0")

# Generated at 2022-06-13 08:36:23.293922
# Unit test for method serialize of class Play
def test_Play_serialize():
    from collections import Sequence
    from ansible import errors
    import ansible.playbook.play
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence

    # Constructing object
    p = Play()

    # Constructing object

# Generated at 2022-06-13 08:36:29.307009
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ds = {
        'vars': {},
        'user': 'test'
    }
    p = Play()
    new_ds = p.preprocess_data(ds)
    assert 'user' not in new_ds, \
        "The 'user' variable should have been removed"
    assert 'remote_user' in new_ds and new_ds['remote_user'] is not None, \
        "The variable 'remote_user' should have been created"



# Generated at 2022-06-13 08:36:41.833965
# Unit test for constructor of class Play
def test_Play():
    pb = Play()
    assert pb is not None
    assert pb.get_name() == ''
    assert len(pb.vars) == 0
    assert len(pb.vars_files) == 0
    assert pb.remote_user == C.DEFAULT_REMOTE_USER
    assert pb.remote_port == C.DEFAULT_REMOTE_PORT
    assert len(pb.roles) == 0
    assert pb.handlers == []
    assert pb.tasks == []
    assert len(pb.vars_prompt) == 0
    assert pb.tags == C.DEFAULT_TAGS
    assert pb.gather_facts is True
    assert pb.gather_subset == C.DEFAULT_GATHER_SUBSET
    assert pb.check_mode is False


# Generated at 2022-06-13 08:36:52.196612
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    class _Play(Play):
        _data_source = None
        _data = None
        def __init__(self, p_data_source, p_data):
            self._data_source = p_data_source
            self._data = p_data
        def _get_parent_attribute(self, p_name, p_attribute=None, p_append=False, p_prepend=False):
            return None
        def _get_ds_attr(self, p_name):
            return self._data.get(p_name)
        def _serialize_value(self, p_value):
            return p_value
        def _load_field_attr(self, p_name, p_attribute):
            if p_name == 'hosts':
                return 'test_host'

# Generated at 2022-06-13 08:37:01.466291
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    with pytest.raises(AssertionError):
        play.preprocess_data(1)
    assert play.preprocess_data({}) == {}
    assert play.preprocess_data({'user': 'foo'}) == {'remote_user': 'foo'}
    assert play.preprocess_data({'user': 'foo', 'remote_user': 'bar'}) == {'remote_user': 'bar'}


# Generated at 2022-06-13 08:37:07.125006
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = ['a.yml']
    assert play.get_vars_files() == ['a.yml']
    
    play.vars_files = 1
    assert play.get_vars_files() == [1]

    play.vars_files = None
    assert play.get_vars_files() == []
    

# Generated at 2022-06-13 08:37:13.675474
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    # Setup the play object
    play = Play()

    # Setup the role object
    role = Role()
    handlers = Handler()
    handlers.load(name="Test")
    role.handlers.append(handlers)

    # Setup the list of roles
    play.roles.append(role)

    # Test the method
    assert play.compile_roles_handlers() != [], "Play compile_roles_handlers failed to return the expected list of handlers"

# Generated at 2022-06-13 08:37:35.970610
# Unit test for method serialize of class Play
def test_Play_serialize():
    play_list = ['play', 'roles']
    serialize_list = ['roles']
    dict_list = ['action_groups', 'group_actions', 'roles']

    play = Play()
    for i in play_list:
        if i not in dict_list:
            assert hasattr(play, i)
    for i in serialize_list:
        assert i in play.serialize()

    play.roles = [{'name': 'role1'}, {'name': 'role2'}]
    assert play.serialize()['roles'][0] == {'name':'role1'}
    assert play.serialize()['roles'][1] == {'name':'role2'}



# Generated at 2022-06-13 08:37:48.767339
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Create a play
    name = 'test_get_tasks'
    play = Play.load(data=dict(name=name, hosts='all'), variable_manager=VariableManager(), loader=DataLoader())
    # Create a task
    import ansible.parsing.yaml.objects
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    task_data = dict(action='debug', msg='{{ foo }}')
    task = Task.load(data=task_data, block=Block(), role=None, task_include=TaskInclude(), use_handlers=False, variable_manager=VariableManager(), loader=DataLoader())
    # Add the task to the play
    play.tasks = [task]
    # Check

# Generated at 2022-06-13 08:37:54.934341
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # initialize a Play object for the test
    play = Play()
    play.pre_tasks = [1,2,3]
    play.tasks = [3,4,5]
    play.post_tasks = [6,7,8]

    tasks = play.get_tasks()
    assert tasks == [1,2,3,3,4,5,6,7,8]

if __name__ == '__main__':
    test_Play_get_tasks()

# Generated at 2022-06-13 08:38:06.065225
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    task_list=[]
    task_obj=Task()
    task_obj.set_loader(DictDataLoader({}))
    task_list.append(task_obj);
    block_obj=Block(block=task_list)
    task_list=[]
    task_list.append(block_obj)
    task_obj=Task()
    task_obj.set_loader(DictDataLoader({}))
    task_list.append(task_obj);
    play_obj=Play()
    play_obj.set_loader(DictDataLoader({}))
    play_obj.post_tasks=task_list
    result=play_obj.get_tasks()
    assert result[0].task_loader==task_obj.task_loader
    assert result[1].task_loader==task_obj.task

# Generated at 2022-06-13 08:38:12.335376
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()

    play.vars_files = 'a.yml'
    assert play.get_vars_files() == ['a.yml']

    play.vars_files = ['a.yml','b.yml']
    assert play.get_vars_files() == ['a.yml','b.yml']

    play.vars_files = None
    assert play.get_vars_files() == []

# Generated at 2022-06-13 08:38:22.228570
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    ds = []
    ds.append({'pre_tasks': []})
    ds.append({'tasks': []})
    ds.append({'post_tasks': []})
    ds.append({'pre_tasks': [], 'tasks': [], 'post_tasks': []})
    ds.append({'pre_tasks': {'block': []}})
    ds.append({'tasks': {'block': []}})
    ds.append({'post_tasks': {'block': []}})
    ds.append({'pre_tasks': {'block': []}, 'tasks': {'block': []}, 'post_tasks': {'block': []}})


# Generated at 2022-06-13 08:38:35.551787
# Unit test for method serialize of class Play
def test_Play_serialize():
    test_Play = Play()

# Generated at 2022-06-13 08:38:44.065719
# Unit test for method serialize of class Play
def test_Play_serialize():
    # Create an instance of Play
    my_play = Play()
    my_play.vars = {u'host1': u'localhost'}
    my_play.hosts = u'foo'
    my_play.name = u'bar'
    my_play._variable_manager = {u'host1': u'localhost'}
    my_play._loader = {u'host1': u'localhost'}
    my_play.default_vars = {u'host1': u'localhost'}
    my_play._included_path = None
    my_play._action_groups = {u'host1': u'localhost'}
    my_play._group_actions = {u'host1': u'localhost'}
    my_play._roles = []
    my_play._handlers = []
    my

# Generated at 2022-06-13 08:38:56.284697
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    def test_1():
        play = Play()
        play.vars_files = None
        assert play.get_vars_files() == []
    def test_2():
        play = Play()
        play.vars_files = 'file_name'
        assert play.get_vars_files() == ['file_name']
    def test_3():
        play = Play()
        play.vars_files = ['file1', 'file2']
        assert play.get_vars_files() == ['file1', 'file2']
    test_1()
    test_2()
    test_3()

# Generated at 2022-06-13 08:39:02.745575
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    play = Play(vars_files=None)
    assert play.get_vars_files() == []
    play = Play(vars_files=1)
    assert play.get_vars_files() == [1]
    play = Play(vars_files=[1])
    assert play.get_vars_files() == [1]
    play = Play(vars_files=[1,2])
    assert play.get_vars_files() == [1, 2]

# Generated at 2022-06-13 08:39:38.514689
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    """unit test for get_tasks method
    """
    pb = Play()
    assert pb.get_tasks() == []


# Generated at 2022-06-13 08:39:45.766943
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Instantiate an instance of a play
    play = Play()
    # Set the vars_files attribute as '../../roles/test/vars/main.yml'
    play.vars_files = '../../roles/test/vars/main.yml'
    # Call method get_vars_files
    r = play.get_vars_files()
    assert isinstance(r, list), "The method get_vars_files should return a list"
    # Check length of returned list
    assert len(r) == 1, "The method get_vars_files should return a list of length 1"


# Generated at 2022-06-13 08:39:46.726301
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass    


# Generated at 2022-06-13 08:39:54.737882
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Init
    test_tasks = [
        {'uri': {'url': 'https://raw.githubusercontent.com/ansible/ansible/devel/test/testcases/unit/module_loader/ansible.cfg'}},
        {'block': [
            {'uri': {'url': 'https://raw.githubusercontent.com/ansible/ansible/devel/test/testcases/unit/module_loader/ansible.cfg'}},
            {'uri': {'url': 'https://raw.githubusercontent.com/ansible/ansible/devel/test/testcases/unit/module_loader/ansible.cfg'}}]}
    ]

# Generated at 2022-06-13 08:40:03.543396
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    def mock_post_validation(self, attr):
        self.vars = self._ds.get('vars', dict())

    mock_data = {
        "name": "test",
        "vars": [
            {"a": 1},
            {'b': 2}
        ]
    }
    play = Play()
    setattr(play, "_post_validate_attrs", mock_post_validation)
    play.preprocess_data(mock_data)

    assert isinstance(play.vars, dict)
    assert play.vars['a'] == 1
    assert play.vars['b'] == 2

# Generated at 2022-06-13 08:40:08.801555
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # test Play using python API
    play = Play()
    play.preprocess_data({'hosts': 'localhost'})
    play.preprocess_data({'hosts': 'localhost', 'user': 'test'})
    play.preprocess_data({'hosts': 'localhost', 'remote_user': 'test'})


# Generated at 2022-06-13 08:40:12.525104
# Unit test for constructor of class Play
def test_Play():
    play = Play()
    assert play.connection == 'smart'
    assert play.gather_facts == 'smart'
    assert play.force_handlers is False
    assert play.name == ''
    assert play.remote_user == 'root'

# Generated at 2022-06-13 08:40:15.453266
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = 'test'
    assert p.get_vars_files() == [p.vars_files]
    p.vars_files = ['test']
    assert p.get_vars_files() == p.vars_files



# Generated at 2022-06-13 08:40:24.445385
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Test with a single role
    p = Play()
    p.name = 'test_role'
    r = Role()
    r.name = 'test_role'
    p.roles = [r]
    p._variable_manager = VariableManager()
    p._loader = DataLoader()
    handlers = [Handler(), Handler()]
    r.handlers = handlers
    assert len(p.handlers) == 0
    assert len(p.get_handler_blocks()) == 0
    assert len(p.compile_roles_handlers()) == 2
    assert p.handlers == handlers
    assert p.get_handler_blocks() == handlers

    # Test with 2 roles
    p = Play()
    p.name = 'test_role'
    r = Role()
    r.name = 'test_role'
   

# Generated at 2022-06-13 08:40:38.122630
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    host = MockHost()

    # set up a play to work with
    play_data = {}
    play = Play().load(play_data, variable_manager=VariableManager(), loader=DataLoader())
    play._hosts = host
    play._groups = {
        'group1': MockGroup(),
        'group2': MockGroup(),
    }
    play._vars = {}

    # set up a task to work with
    task_data = {
        'action': 'fake',
        'name': 'fake task',
    }
    task = Task(**task_data)
    task._role = None
    task._block = None
    task._always = None
    task._any_errors_fatal = False
    task._ignore_errors = False
    task._loop = None
    task._loop_args = None
   