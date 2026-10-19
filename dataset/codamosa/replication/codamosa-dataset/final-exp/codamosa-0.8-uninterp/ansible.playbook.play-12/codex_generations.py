

# Generated at 2022-06-13 08:31:37.539675
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    play._ds = { 'user' : 'root' }
    play.preprocess_data(play._ds)
    assert play._ds['remote_user'] == 'root'
    assert 'user' not in play._ds


# Generated at 2022-06-13 08:31:49.907794
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:31:52.079898
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    # Preconditions
    # Correct expectation
    assert p.get_tasks() is []


# Generated at 2022-06-13 08:32:00.274272
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    #here are the variables to test the method get_tasks of class Play
    # test_Play_tasks is a list which contains the tasks of a play
    test_Play_tasks = ['a_task', 'this is a task']
    # test_Play_pre_tasks is a list which contains the pre tasks of a play
    test_Play_pre_tasks = ['a_task', 'this is a task']
    # test_Play_post_tasks is a list which contains the post tasks of a play
    test_Play_post_tasks = ['a_task', 'this is a task']
    # test_Play_blocks is a list which contains the always blocks of a play
    test_Play_blocks = ['a_task', 'this is a task']
    # test_Play_rescue_blocks is a list which contains the

# Generated at 2022-06-13 08:32:15.769218
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []

    p.tasks.append(MockTask('first_task', p))
    assert [t.name for t in p.get_tasks()] == ['first_task']
    p.tasks.append(MockTask('second_task', p))
    assert [t.name for t in p.get_tasks()] == ['first_task', 'second_task']

    p.pre_tasks.append(MockTask('first_pre_task', p))
    p.pre_tasks.append(MockTask('second_pre_task', p))
    assert [t.name for t in p.get_tasks()] == ['first_pre_task', 'second_pre_task', 'first_task', 'second_task']

   

# Generated at 2022-06-13 08:32:18.322226
# Unit test for method get_name of class Play
def test_Play_get_name():
    x = Play()
    assert x.get_name() == ''
    setattr(x, 'name', 'foo')
    assert x.get_name() == 'foo'

# Generated at 2022-06-13 08:32:25.010181
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    host_vars_1 = {'host_var_1': 'host_var_1'}
    host_vars_2 = {'host_var_2': 'host_var_2'}
    host_vars_3 = {'host_var_3': 'host_var_3'}

# Generated at 2022-06-13 08:32:37.977887
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play.load(dict(
        name="dummy_play",
        hosts="dummy_hosts",
        gather_facts=False,
        tasks=[
            dict(name='dummy_task',shell='dummy_shell')
        ]
    ), variable_manager=VariableManager())
    get_tasks = play.get_tasks()
    assert isinstance(get_tasks,list)
    assert isinstance(get_tasks[0],Task)
    assert get_tasks[0].name == 'dummy_task'
    assert get_tasks[0].action == 'shell'
    assert get_tasks[0].args == 'dummy_shell'

# Generated at 2022-06-13 08:32:45.983533
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()
    p.deserialize(data={'name': 'p', 'hosts': 'h', 'roles': [{'metadata': {'name': 'r1'}, 'role_path': 'rp/r1'}, {'metadata': {'name': 'r2'}, 'role_path': 'rp/r2'}]})
    assert 'metadata' in p.roles[0]._ds
    assert 'metadata' in p.roles[1]._ds
    assert 'name' in p.roles[0]._ds['metadata']
    assert 'name' in p.roles[1]._ds['metadata']
    assert p.roles[0]._ds['metadata']['name'] == 'r1'

# Generated at 2022-06-13 08:32:46.399237
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:33:02.258436
# Unit test for constructor of class Play
def test_Play():
    name = 'UnitTest'
    play = Play()
    play.name = name
    assert play.name == name
    assert play.__repr__() == name

# Generated at 2022-06-13 08:33:12.922771
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Setup data
    play_dict = {
        "hosts": "test_hosts",
        "remote_user": "test_remote_user",
        "become": True,
        "become_method": "test_become_method",
        "become_user": "test_become_user",
        "vars": {"test_var": "test_value"},
        "vars_prompt": [{"name": "test_prompt"}],
        "vars_files": "test_vars_files",
        "tasks": None,
        "handlers": None,
        "pre_tasks": None,
        "post_tasks": None,
        "roles": None
    }

    # Set up mocks
    fake_loader = mock.MagicMock()
    fake_variable

# Generated at 2022-06-13 08:33:17.989789
# Unit test for constructor of class Play
def test_Play():

    # Create play
    play = Play()

    # Create roles
    role1 = Role()
    role2_vars = {'var1': 'value1', 'var2': 'value2', 'var3': 'value3'}
    role2_definition = {
        'name': 'role2_name',
        'vars': role2_vars,
    }
    role2 = Role()
    role2.load_data(role2_definition)
    role3_definition = {
        'name': 'role3_name',
        'vars': {
            'var4': 'value4',
            'var5': 'value5',
        }
    }
    role3 = Role()
    role3.load_data(role3_definition)

    # Add 3 roles in different ways
    play.roles

# Generated at 2022-06-13 08:33:31.773157
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():

    # case 1: ds is not instance of dict
    ds = None
    obj = Play()
    try:
        obj.preprocess_data(ds)
    except AnsibleAssertionError as e:
        if str(e) == "while preprocessing data (None), ds should be a dict but was a <class 'NoneType'>":
            print("Exception '" + str(e) + "' successfully catched")
        else:
            assert False

    # case 2: ds is a dict
    ds = {}
    obj = Play()
    try:
        obj.preprocess_data(ds)
    except AnsibleAssertionError as e:
        assert False
    else:
        print("No exception raised for case 2")



# Generated at 2022-06-13 08:33:32.986323
# Unit test for method serialize of class Play
def test_Play_serialize():
    pass


# Generated at 2022-06-13 08:33:40.289534
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = '/tmp/test'
    assert p.get_vars_files() == ['/tmp/test']
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = ['a', 'b', 'c']
    assert p.get_vars_files() == ['a', 'b', 'c']


# Generated at 2022-06-13 08:33:55.112760
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play_obj = Play()
    play_obj.vars_files = None
    # Test 'if self.vars_files is None:' branch
    result = play_obj.get_vars_files()
    assert result == []
    play_obj.vars_files = {'key': 'value'}
    # Test 'elif not isinstance(self.vars_files, list):' branch
    result = play_obj.get_vars_files()
    assert result == [play_obj.vars_files]
    play_obj.vars_files = [{'key': 'value'}, {'key': 'value'}]
    # Test 'return self.vars_files' branch
    result = play_obj.get_vars_files()
    assert result == play_obj.vars_files


# Generated at 2022-06-13 08:34:05.029937
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create the class to be tested
    test_play = Play()

    # Create the role to be tested
    test_role = Role()
    test_play.roles = [test_role]

    # Create the handlers to be tested
    test_handler = Handler()
    test_handler2 = Handler()
    test_role.handlers = [test_handler]
    test_role.handler_blocks[0] = [test_handler, test_handler2]

    # Assert the result has the expected value
    assert test_play.compile_roles_handlers() == [test_handler, test_handler2]

# Generated at 2022-06-13 08:34:10.968437
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    host_list = ['localhost', 'remotehost']
    p = Play()
    p.vars_files = "vars_files"
    assert p.get_vars_files == [p.vars_files]

    p.vars_files = ['vars_files1', 'vars_files2']
    assert p.get_vars_files == p.vars_files

    p.vars_files = None
    assert p.get_vars_files == []

    p.vars_files = ['vars_files1', 'vars_files2', None]
    assert p.get_vars_files == p.vars_files

# Generated at 2022-06-13 08:34:22.328708
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop


# Generated at 2022-06-13 08:34:40.018753
# Unit test for constructor of class Play
def test_Play():
    Play()

# Generated at 2022-06-13 08:34:51.047047
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()

    # handler_name is a string
    class FakeRole(object):
        def __init__(self, handler_name):
            self.handler_name = handler_name

        def get_handler_blocks(self, play):
            pass

        def get_handler_blocks2(self, play):
            return self.handler_name

    handler_name_1 = FakeRole("hi")
    handler_name_2 = FakeRole("bye")

    play.roles = [handler_name_1, handler_name_2]

    assert play.compile_roles_handlers() == ["hi", "bye"]


# Generated at 2022-06-13 08:35:05.582404
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    ds = {'post_tasks': [{'name': 'a', 'register': 'b'}], 'vars': {'c': 'd'}, 'user': 'e'}
    assert p.preprocess_data(ds) == {'post_tasks': [{'name': 'a', 'register': 'b'}], 'vars': {'c': 'd'}, 'remote_user': 'e'}
    ds2 = {'hosts': 'abc', 'user': 'e'}
    assert p.preprocess_data(ds2) == {'hosts': 'abc', 'remote_user': 'e'}


# Generated at 2022-06-13 08:35:12.234920
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # roles
    block1 = Block()
    block1.block = [Task()]
    block1.rescue = []
    block1.always = []

    block2 = Block()
    block2.block = []
    block2.rescue = [Task()]
    block2.always = []

    block3 = Block()
    block3.block = []
    block3.rescue = []
    block3.always = [Task()]

    role = Role()
    role.compiled_as_list = [block1, block2, block3]

    # Play
    block4 = Block()
    block4.block = [Task()]
    block4.rescue = []
    block4.always = []

    block5 = Block()
    block5.block = []

# Generated at 2022-06-13 08:35:24.744580
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from collections import namedtuple

    # mock class to be used instead of class 'Task'

# Generated at 2022-06-13 08:35:36.363526
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # create objects for test of method compile_roles_handlers
    my_loader = DataLoader()
    my_variable_manager = VariableManager()
    my_inventory = Inventory(my_loader, my_variable_manager, "test_host")
    my_variable_manager.set_inventory(my_inventory)
    play_source =  dict(
            name = "Ansible Play test_Play_compile_roles_handlers",
            hosts = 'test_host_1',
            gather_facts = 'no',
            connection = 'local',
            tasks = [
                # code
            ],
            handlers = []
        )
    test_Play = Play().load(play_source, my_variable_manager, my_loader)
    test_Play._play_hosts = my_inventory.get_hosts()
    test

# Generated at 2022-06-13 08:35:47.013662
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from os.path import abspath
    
    cwd = os.getcwd()
    file_name = abspath(
        os.path.join(
            cwd,
            'test_data',
            'compile_roles_handlers_testdata.yml'
        )
    )
    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(
        loader=None,
        options=context.CLIARGS,
        **variable_manager.extra_vars
    )
    loader = DataLoader()
    

# Generated at 2022-06-13 08:35:49.734380
# Unit test for method serialize of class Play
def test_Play_serialize():
    play_serialize_instance = Play()
    play_serialize_instance.serialize()



# Generated at 2022-06-13 08:35:51.862695
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert play.compile_roles_handlers() == []

# Generated at 2022-06-13 08:35:56.347447
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    ds = { 'hosts': 'localhost', 'user': 'noone', 'roles': [] }
    p.preprocess_data(ds)
    assert 'user' not in ds
    assert ds.get('remote_user') == 'noone'

# Generated at 2022-06-13 08:36:26.211149
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.pre_tasks = ["task1"]
    p.tasks = ["task2"]
    p.post_tasks = ["task3"]
    assert p.get_tasks() == ["task1","task2","task3"]

if __name__ == "__main__":
    import os
    import sys
    import yaml
    from collections import namedtuple

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    # since the API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object

# Generated at 2022-06-13 08:36:34.654091
# Unit test for method serialize of class Play
def test_Play_serialize():
    abc = Play()
    abc.get_name()
    abc.serialize()
    block_list = abc._compile_roles()
    abc.get_vars()
    abc.get_vars_files()
    abc.get_handlers()
    abc.get_roles()
    abc.get_tasks()
    abc.deserialize("abc")
    abc.copy()
# ----------------------------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 08:36:46.373203
# Unit test for constructor of class Play
def test_Play():
    '''
    play = Play()

    assert play.name is None
    assert play.hosts == 'all'
    assert play.roles == []
    assert play.vars_prompt == []
    assert play.handlers == []
    assert play.tasks == []
    assert play.tags == frozenset()
    assert play.skip_tags == frozenset()
    assert play.force_handlers == False
    assert play.vars == {}
    assert play.vars_files == []
    assert play.any_vars_set() == False
    assert play.notify is None
    '''
    assert True

# Generated at 2022-06-13 08:36:47.609120
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass  # noop

# Generated at 2022-06-13 08:36:50.897807
# Unit test for constructor of class Play
def test_Play():
    pass

# import module snippets
from ansible.parsing.splitter import parse_kv
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.playbook.conditional import Conditional, ConditionalBlock

# Generated at 2022-06-13 08:37:03.365316
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    def doit(test_data):
        p = Play().load(test_data, variable_manager=None, loader=None)
        return p.compile_roles_handlers()
    # TODO: add more tests
    test_data = dict(
        hosts='all',
        roles=dict(
            role1=dict(
                handlers=['main']
            ),
            role2=dict(
                handlers=dict(
                    main=dict()
                )
            )
        )
    )
    expected = [
        {'main': []},
        {'main': []}
    ]
    r = doit(test_data)
    assert r == expected


# Generated at 2022-06-13 08:37:08.704775
# Unit test for method get_name of class Play
def test_Play_get_name():
    '''
    Unit test for method get_name of class Play
    '''
    test = Play()
    actual = test.get_name()
    assert actual == ''

    test = Play()
    test.name = 'test play name'
    actual = test.get_name()
    assert actual == 'test play name'


# Generated at 2022-06-13 08:37:20.374404
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # parameters for function call
    actions = [
        {'name': 'file',
         'args': {
             {'src': 'A'},
             {'dest': 'B'}
         }},
        {'name': 'fail',
         'args': {
             {'msg': 'A'}
         }}
    ]
    handlers = [{
        'name': 'notify',
        'actions': actions
    }]
    tasks = [{
        'name': 'fail',
        'args': {
            'msg': 'A'
        }
    }]
    pre_tasks = []
    post_tasks = []

# Generated at 2022-06-13 08:37:32.253194
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # test that 'self.tasks' list is returned if not None
    play_obj = Play()
    play_obj.tasks = [1, 2, 3]
    assert play_obj.get_tasks() == [1, 2, 3]

    # test that 'self.pre_tasks' and 'self.tasks' lists are returned if 'self.post_tasks' is None
    play_obj = Play()
    play_obj.pre_tasks = [0]
    play_obj.tasks = [1, 2, 3]
    play_obj.post_tasks = None
    assert play_obj.get_tasks() == [0, 1, 2, 3]

    # test that 'self.pre_tasks', 'self.tasks', and 'self.post_tasks' lists are returned if they

# Generated at 2022-06-13 08:37:34.971016
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    testcase_Play = Play()
    assert testcase_Play.get_tasks() == [], "Failed to test Play's get_tasks"



# Generated at 2022-06-13 08:38:16.668145
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    _roles = [{
        "include_tasks": "tasks/main.yml",
        "include_handlers": "handlers/main.yml",
        "name": "my-role"
    }]
    _loader = Mock()
    _tasks = [{
        "include_tasks": "tasks/main.yml",
        "name": "my-role"
    }]
    _handlers = [{
        "name": "debug",
        "include_handlers": "handlers/main.yml",
    }]
    _vm = Mock()
    _vars = {}
    _hosts = 'all'

# Generated at 2022-06-13 08:38:24.992551
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    '''
    unit test for method get_tasks of class Play
    '''

    # See issue #16952
    play_ds = dict(
        name="test_Play_get_tasks",
        connection="network_cli",
        hosts="localhost",
    )
    play = Play.load(
        play_ds,
        variable_manager=VariableManager(),
        loader=DataLoader(),
        vars=dict()
    )
    tasks = play.get_tasks()
    assert len(tasks) == 0

    # See issue #16952
    play_ds = dict(
        name="test_Play_get_tasks",
        connection="network_cli",
        hosts="localhost",
        tasks=[]
    )

# Generated at 2022-06-13 08:38:28.282591
# Unit test for method serialize of class Play
def test_Play_serialize():
    play = Play()
    assert play._serialize() is None
    play = Play(name='test_play')
    assert play._serialize() == 'test_play'


# Generated at 2022-06-13 08:38:30.346854
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    assert False, "No test for method get_tasks"

# Generated at 2022-06-13 08:38:40.454595
# Unit test for method get_name of class Play
def test_Play_get_name():
    # test_Play_get_name() returns True if the name of the play is a concatination of the names of the hosts

    # create a new play with host1 and host2
    play = Play()
    play.hosts = ['host1', 'host2']
    host_names = play.hosts

    # the name should be a concatination of the names of the hosts
    if play.get_name() == ','.join(host_names):
        return True
    return False
# Unit Test for Compile method of class Play

# Generated at 2022-06-13 08:38:41.505154
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:38:56.615665
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play._load_data_ds = {
        "name": "testPlay",
        "hosts": "all",
        "gather_facts": "no",
        "tasks": [
            {
                "name": "task1",
                "debug": "var=hostvars"
            },
            {
                "block": [
                    {
                        "name": "block task1",
                        "debug": "var=hostvars"
                    },
                    {
                        "name": "block task2",
                        "debug": "var=hostvars"
                    }
                ]
            }
        ]
    }
    play._variable_manager = DummyVariableManager()
    play._loader = DummyLoader()
    play.tasks = play._load_tasks()
    play.post_

# Generated at 2022-06-13 08:38:58.277817
# Unit test for constructor of class Play
def test_Play():
    """
    Test: Play creation
    Expected: No Exception
    """
    Play()


# Generated at 2022-06-13 08:39:01.143358
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # given
    d = Object()
    d.name = 'test'
    play = Play()
    play.post_validate = MagicMock()
    # when
    play.preprocess_data(d)
    # then
    assert play.name == 'test'
    play.post_validate.assert_called_once_with(d)


# Generated at 2022-06-13 08:39:03.676752
# Unit test for method get_name of class Play
def test_Play_get_name():
    """Test Play.get_name method return value"""
    play = Play()
    play.name = "test"
    assert play.get_name() == play.name
    play.name = ""
    assert play.get_name() == play.name

# Generated at 2022-06-13 08:39:41.160970
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """
    Test compile_roles_handlers of the Play class
    """
    obj = Play()
    print (obj.compile_roles_handlers())


# Generated at 2022-06-13 08:39:41.694679
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert True

# Generated at 2022-06-13 08:39:43.177474
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    assert p.serialize()

# Generated at 2022-06-13 08:39:52.007432
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Arrange
    play = Play()
    
    # Act
    actual = play.get_vars_files()

    # Assert
    assert actual == [], 'actual: {}'.format(actual)
    
    # Arrange
    play = Play()
    play.vars_files = ""
    
    # Act
    actual = play.get_vars_files()

    # Assert
    assert actual == [''], 'actual: {}'.format(actual)
    
    # Arrange
    play = Play() 
    play.vars_files = []
    
    # Act
    actual = play.get_vars_files()

    # Assert
    assert actual == [], 'actual: {}'.format(actual)
    
    # Arrange
    play = Play()
    play.vars_files

# Generated at 2022-06-13 08:40:01.033078
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Case 1: Hosts list contains only strings 
    # Given
    hosts = "host1"
    # When
    play = Play()
    play.hosts = hosts
    # Then
    assert play.get_name() == "host1"
    # Case 2: Hosts list contains only strings
    # Given
    hosts = ["host1", "host2", "host3"]
    # When
    play = Play()
    play.hosts = hosts
    # Then
    assert play.get_name() == "host1,host2,host3"

if __name__ == '__main__':
    import pytest, sys
    pytest.main(sys.argv)

# Generated at 2022-06-13 08:40:05.049497
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
    Unit test for method compile_roles_handlers of class Play
    '''
    print('Unit test for method compile_roles_handlers of class Play')
    # Call compile_roles_handlers of class Play
    play = Play()
    play.compile_roles_handlers()
    # Return
    return

# Generated at 2022-06-13 08:40:11.279265
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Declare a dict to assign to _ds
    data = dict()
    data["name"] = "Ansible Playbook"
    # Declare a dict to assign to _ds again
    ds = dict()
    ds["tasks"] = []
    ds["post_tasks"] = []
    ds["pre_tasks"] = []
    # Create a task object and assign it to task
    task = Task()
    # Set the task name to "test task"
    task.name = "test task"
    # Add the task to the pre_tasks array in the ds dict
    ds["pre_tasks"].append(task)
    # Create another task object and assign it to task2
    task2 = Task()
    # Set the task name to "test task 2"

# Generated at 2022-06-13 08:40:21.842163
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.roles = [
        # Role01
        Role(name='Role01',
            tasks=[
                # name: task01
                Task(action=dict(module='shell', args='echo "Hello world"')),
                # name: task02
                Task(action=dict(module='shell', args='echo "Goodbye world"')),
            ],
            handlers=[
                # name: handler01
                Handler(action=dict(module='shell', args='echo "Hello world"')),
                # name: handler02
                Handler(action=dict(module='shell', args='echo "Goodbye world"')),
            ]
        ),
    ]
    assert play.compile_roles_handlers() == play.roles[0].get_handler_blocks(play=play)

# Generated at 2022-06-13 08:40:28.983852
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # specify python module file path
    test_file_path = './unit/test_runner_tools.py'
    # specify the test method name
    test_method_name = 'test_Play_compile_roles_handlers'
    # execute the unit test
    unittesting.run_test_method(test_file_path, test_method_name)



# Generated at 2022-06-13 08:40:41.027327
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play_obj = Play()

    # Test for 'vars_file' as a list (including cases when vars_file is an empty list, None or vars_file is not present in Play object)
    setattr(play_obj, 'vars_files', [])
    assert play_obj.get_vars_files() == []
    setattr(play_obj, 'vars_files', None)
    assert play_obj.get_vars_files() == []
    setattr(play_obj, 'vars_files', ['vars/first.yml', 'vars/second.yml'])
    assert play_obj.get_vars_files() == ['vars/first.yml', 'vars/second.yml']

    # Test for 'vars_file' as a string