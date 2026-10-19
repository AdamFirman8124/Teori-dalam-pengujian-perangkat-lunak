

# Generated at 2022-06-13 10:05:49.584641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    class MockTask:
        def __init__(self, args):
            self.args = args

        def get_path(self):
            return "path_to_task"

    class MockPlay:
        def __init__(self, options):
            self.options = options
            self.name = "name_of_play"

        def get_variable_manager(self):
            return MockVariableManager


# Generated at 2022-06-13 10:05:54.456595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = ActionModule()

    assert test.__class__ is ActionModule, "Class match"
    #assert test.TRANSFERS_FILES is False, " TRANSFERS_FILES match"
    #assert test._VALID_ARGS is frozenset(('key')), " valid args match"

    return 1


# Generated at 2022-06-13 10:05:59.843561
# Unit test for constructor of class ActionModule
def test_ActionModule():
    groupName = 'testGroupName'
    parentGroups = 'all'
    args = {
        'key': groupName,
        'parents': parentGroups
    }
    task = {'args' : args}
    am = ActionModule(task, {}, {}, {})
    assert (am.run())['add_group'] == 'testGroupName'
    assert (am.run())['parent_groups'] == ['all']

# Generated at 2022-06-13 10:06:00.419586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:06:00.993524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:06:08.523207
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""
    from ansible.plugins.action.group_by import ActionModule
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task._role = None
    task._block = None
    task.args = {'key': 'test_key', 'parents': 'test_parent'}
    task.action = 'test_action'
    task.loop = None
    task.delegate_to = None
    task.delegate_facts = False
    task.check_mode = False
    task.notify = []
    task.tags = set()
    task.when = {}
    task.register = 'test_register'

    play_context = PlayContext()
    play_context.check_mode = False

# Generated at 2022-06-13 10:06:19.991763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json

    class Task:
        def __init__(self, args):
            self.args = args

    action = ActionModule(Task({}), {})
    assert action, 'action object is not created'
    assert action.run(task_vars={}) == {'msg': "the 'key' param is required when using group_by", 'failed': True}, 'action is failed with missing arguments'

    action = ActionModule(Task({'key': 'test_group'}), {})
    assert json.loads(json.dumps(action.run(task_vars={}))) == {'changed': False, 'parent_groups': ['all'], 'add_group': 'test-group'}, 'action is failed with missing arguments'


# Generated at 2022-06-13 10:06:22.213374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    testActionModule = ActionModule()
    testHostResult = testActionModule.run()
    assert testHostResult.get('failed') == True

# Generated at 2022-06-13 10:06:34.673591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task.args = {'key': 'my_key', 'parents': 'my_parent'}
    result = action_module.run()

    assert result == {
            'changed': False,
            'add_group': 'my_key',
            'parent_groups': ['my_parent'],
            'ansible_facts': {},
            '_ansible_no_log': False,
            '_ansible_verbose_always': False,
            'invocation': {'module_args': 'key=my_key parents=my_parent', 'module_name': 'group_by'}
        }

# Generated at 2022-06-13 10:06:41.225581
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(dict(action=dict(group_by=dict(key="key", parents='parents'))))
    result = actionModule.run(task_vars=dict())
    assert isinstance(result, dict)
    assert 'add_group' in result
    assert 'parent_groups' in result
    assert 'failed' in result
    assert 'changed' in result
    assert isinstance(result['add_group'], str)
    assert isinstance(result['parent_groups'], list)
    assert isinstance(result['failed'], bool)
    assert isinstance(result['changed'], bool)

# Generated at 2022-06-13 10:06:47.658452
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None
    # test members of the class ActionModule
    assert action_module._VALID_ARGS == frozenset(('key', 'parents'))

# Generated at 2022-06-13 10:06:58.371003
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.modules.extras.cloud.amazon.ec2_vpc_subnet import ec2_vpc_subnet
    source = {'VpcId': 'tototiti',
              'CidrBlock': '10.0.0.0/24',
              'AvailabilityZone': 'eu-west-1a'}
    ec2_source = ec2_vpc_subnet(source, None)
    ec2_source._filter_instance = lambda name: None
    ec2_source.name = 'toto'

    class Task:
        args = {'key': 'test', 'parents': ''}

    class Client:
        def get_inventory_host(self, name):
            return {'variable': 'value'}


# Generated at 2022-06-13 10:07:08.846473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_host = {
        "hostname": "testhost",
        "variables": {
            "group_by_var": "testgroup",
            "test": "testvar"
        }
    }
    test_task = {
        "args": {
            "key": "group_by_var",
            "parents": "all"
        }
    }
    test_loader = {
        "inventory": {
            "groups": {},
            "hosts": {},
            "index": {},
            "patterns": {},
            "cache": {},
            "include": ["testhost"]
        }
    }
    test_play = {
        "hosts": []
    }
    test_result = {}
    test_variable_manager = {}

    # Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:07:17.155528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.group_by import ActionModule

    test_ActionModule = ActionModule(None, {}, None, None, None)

    try:
        test_ActionModule._task.args = {'key':'test_key','parent':'test_parent'}
        result = test_ActionModule.run(task_vars={})
    except Exception as e:
        assert False, 'Exception was thrown: %s'%e

    assert result['parent_groups'] == ['test_parent'], "Parent group was not expected value"
    assert result['add_group'] == 'test_key', "Child group was not expected value"

# Generated at 2022-06-13 10:07:17.998873
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:07:19.524756
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:07:21.023313
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(ActionModule(), None, None)

# Generated at 2022-06-13 10:07:26.009491
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result =  ActionModule.run(['10.10.10.10'],tmp='/tmp/test', task_vars=None)
    assert result.get('msg') == "the 'key' param is required when using group_by"
    assert result.get('failed') == True

test_ActionModule_run()

# Generated at 2022-06-13 10:07:28.261084
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, '_VALID_ARGS')
    assert hasattr(ActionModule, 'TRANSFERS_FILES')


# Generated at 2022-06-13 10:07:31.674764
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_plugin is not None
    assert action_plugin._valid_args == frozenset(('key', 'parents'))

# Generated at 2022-06-13 10:07:46.138739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    assert action_module.run()['failed'] == True
    assert action_module.run(task_vars={'ansible_architecture': 'amd64'})['add_group'] == 'amd64'
    assert action_module.run(task_vars={'spatie': 'linux'}) == {
        'changed': False,
        'add_group': 'linux',
        'parent_groups': ['all'],
    }
    assert action_module.run(
        task_vars={'spatie': 'linux'},
        args={'key': 'spatie', 'parents': 'spatie'}
    ) == {
        'changed': False,
        'add_group': 'linux',
        'parent_groups': ['linux'],
    }
   

# Generated at 2022-06-13 10:07:55.606239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    # create a play to instantiate the task
    play_source = dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='group_by', key='ansible_os_family', parents='all'))
             ]
        )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)



# Generated at 2022-06-13 10:08:03.590864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    # Initialization of the ActionModule       
    module = ActionModule("/tmp","/tmp",{"_ansible_verbosity":0, "_ansible_debug": False})
    # Declaration of the task
    task = {"action":"group_by", "args":{"key":"test", "parents":['linux']}, "id":None, "name":"group_by", "version":None, "vars":{"ansible_ssh_private_key_file":None}}
    
    # Unit test execution
    result_action = module.run(task_vars=None, tmp=None, task=task)
    # Unit test verification
    print(result_action)
    print(result_action.get("changed"))
    
    
    

# Generated at 2022-06-13 10:08:05.619104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    assert act.TRANSFERS_FILES == False
    assert act._VALID_ARGS == frozenset(('key', 'parents'))

# Generated at 2022-06-13 10:08:07.600247
# Unit test for constructor of class ActionModule
def test_ActionModule():
    
    action_module_obj = ActionModule('setup', 'user', 'home', 'tmp')
    assert action_module_obj is not None 


# Generated at 2022-06-13 10:08:08.200647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:08:15.897685
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create fake ActionModule instance
    module = ActionModule()

    # Create fake task
    task = dict()
    task["args"] = dict()
    task['args']['key'] = "key instance"
    task['args']['parents'] = None

    # Create fake task_vars
    task_vars = dict()

    # Test
    result = module.run(task_vars=task_vars, task=task)
    assert result['changed'] == False
    assert result['add_group'] == "key-instance"
    assert result['parent_groups'] == ['all']

# Generated at 2022-06-13 10:08:21.376661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        dict(
            name='test_ActionModule_run',
            args=dict(key='foo', parents=['one', 'two'])
        ),
        load_plugins=False,
        runner=None
    )

    result = module.run()
    assert result['changed'] == False
    assert result['add_group'] == 'foo'
    assert result['parent_groups'] == ['one', 'two']



# Generated at 2022-06-13 10:08:25.368463
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    print(a.TRANSFERS_FILES)
    print(a._VALID_ARGS)

# Invoke Unit test
#test_ActionModule()


# -- end of file --

# Generated at 2022-06-13 10:08:35.477708
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = {
        'action': {
            'name': 'test_name',
            'args': {
                'key': 'test_key',
                'parents': ['test_parent_1', 'test_parent_2']
            }
        }
    }
    action_module._play_context = object()
    action_module._loader = object()
    action_module._templar = object()
    action_module._shared_loader_obj = object()
    action_module._connection = object()
    action_module._shell = object()

    result = action_module.run()
    assert result['changed'] == False
    assert result['add_group'] == 'test_key'

# Generated at 2022-06-13 10:08:57.166506
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a test user and a test host
    testuser = ansible.inventory.user.User()
    testuser.name = "testuser"
    testuser.password = "testuser"
    testhost = ansible.inventory.host.Host()
    testhost.name = "testhost"
    testhost.groups = [ansible.inventory.group.Group(name='ungrouped')]
    # create a group
    testgroup = ansible.inventory.group.Group()
    testgroup.name = "test"
    testgroup.user = testuser
    testgroup.hosts = [testhost]
    # create an inventory
    testinv = ansible.inventory.Inventory([testhost])
    testinv.groups = [testgroup]
    # create a runner

# Generated at 2022-06-13 10:08:58.357062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict())
    assert action is not None

# Generated at 2022-06-13 10:09:06.794753
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_name = 'test_group_by'
    task_vars = {}
    _task = '''{"args": {
        "key": "my_group",
        "parents": ["parent_group"]
    }}'''
    def get_task_vars(var=None):
        if var:
            return task_vars.get(var)
        return task_vars

    module_stdout = ''
    module_stderr = ''
    inject = {}
    am = ActionModule(_task, inject, module_name='copy')
    result = am.run(task_vars=get_task_vars)
    assert result == {'changed': False, 'add_group': 'my_group', 'parent_groups': ['parent_group'], 'failed': False}

# Generated at 2022-06-13 10:09:07.496921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:09:19.656858
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Construct a task object
    task = Task()
    task.args = {'key': 'mykey'}
    playbook_context_vars = {'inventory_dir': 'test/integration/inventory',
                             'inventory_file': 'test/integration/inventory/hosts',
                             'ssh_executable': '',
                             'ansible_connection': 'local',
                             'ansible_python_interpreter': 'python'}
    # Construct a variables object
    def get_vars(self, loader, path, entities=None, cache=True):
        pass
    variables = type('Variables', (object,), {'get_vars': get_vars})
    # Construct a host object
    host = Host(name='localhost')
    # Construct a fake tmp directory

# Generated at 2022-06-13 10:09:27.564553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Import modules and methods
    import os
    import glob
    import json
    import textwrap
    import collections
    import unittest

    import ansible.plugins.action.group_by as group_by
    import ansible.playbook.play_context as play_context
    import ansible.playbook.play as play
    import ansible.playbook.task_include as task_include

    from ansible.inventory.manager import InventoryManager

    # Unit test utilities
    class AnsibleExitJson(Exception):
        ''' Exception class to be raised by module.exit_json and caught
        by the test case.
        '''
        pass

    class AnsibleFailJson(Exception):
        ''' Exception class to be raised by module.fail_json and caught
        by the test case.
        '''
        pass


# Generated at 2022-06-13 10:09:39.830802
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    A = ActionModule()

    # test invalid 'key'
    assert A.run()['failed']

    # test valid 'key'
    assert not A.run(None, {}, {'key': 'foo'})['failed']

    # test 'key' normalization
    assert not A.run(None, {}, {'key': ' foo  bar  '})['failed']
    assert A.run(None, {}, {'key': ' foo  bar  '})['add_group'] == 'foo-bar'

    # test 'parents'
    assert not A.run(None, {}, {'key': 'foo', 'parents': 'bar'})['failed']
    assert A.run(None, {}, {'key': 'foo', 'parents': 'bar'})['parent_groups'] == ['bar']
    assert A.run

# Generated at 2022-06-13 10:09:46.459588
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate the class
    a = ActionModule(OptionalArgs=None, TaskVars=None, ArgSpec=None)
    # Check if it is an instance of the class
    assert isinstance(a, ActionModule)
    # Check for the attributes and the values
    assert a.TRANSFERS_FILES == False
    assert a._VALID_ARGS == frozenset(('key', 'parents'))
    # Check if the method run worked correctly
    assert a.run() == {'changed': False, 'add_group': 'None', 'parent_groups': ['all']}

# Generated at 2022-06-13 10:09:51.637405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockConfig(object):
        def __init__(self):
            self.action_plugins = []
    action_base = ActionBase(MockConfig())
    return ActionModule(action_base._play_context, action_base._new_task, action_base._loader, action_base._templar, action_base._shared_loader_obj)

# Generated at 2022-06-13 10:10:00.000857
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    # The name will be _import_role_<hash_of_path_to_role>
    # Constructor of Task class calls _load_role_defaults
    t = Task()
    am = ActionModule(task=t)
    assert am.plugin_name == '_import_role_fda13a0b7dfeb2f2c9e7a1e40d2079d1'
    assert am.name == 'IMPORT ROLE fda13a0b7dfeb2f2c9e7a1e40d2079d1'
    

# Generated at 2022-06-13 10:10:30.147051
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Test Empty Constructor
    dummy_constructor = ActionModule()
    
    #Test Constructor with some parameters
    dummy_constructor_1 = ActionModule(a=1, b=2)
    
    #Test Constructor with all parameters
    dummy_constructor_2 = ActionModule(a=1, b=2, c=3)

# Generated at 2022-06-13 10:10:39.336586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    mock_vars = dict(group=dict(var1='value1', var2='value2'))
    mock_inventory = InventoryManager(loader=DataLoader(), sources="")
    mock_task = dict(
        action=dict(
            module_name='group_by',
            module_args=dict(key='group')
        )
    )

    action = ActionModule(mock_task, mock_inventory, StringIO())
    result = action.run(task_vars=mock_vars)

    assert result['changed'] is False
    assert result['add_group'] == 'group'

# Generated at 2022-06-13 10:10:40.340923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:10:54.499030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block

    loader = 'loader'
    variable_manager = 'variable_manager'
    task = Task()
    task.args = dict(key='group_name')
    include_role = IncludeRole()
    block = Block()

    action_module = ActionModule(loader=loader, variable_manager=variable_manager, task=task)
    assert action_module.run(None, dict())['add_group'] == 'group_name'
    assert action_module.run(None, dict())['parent_groups'] == ['all']


# Generated at 2022-06-13 10:11:00.768928
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize parameters
    _task = {'args': {'key': 'prefix1', 'parents': ['all']}}
    _tmp = None
    _task_vars = None

    # Create new object
    actionModule = ActionModule()

    # Call method under test
    result = actionModule.run(_tmp, _task_vars)

    assert result['changed'] == False
    assert result['add_group'] == 'prefix1'
    assert result['parent_groups'] == ['all']
    

# Generated at 2022-06-13 10:11:02.578255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_obj = ActionModule(None, None);
    print("Constructor of class ActionModule excuted")
    


# Generated at 2022-06-13 10:11:06.064493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test the constructor of class ActionModule
    """
    action_module = ActionModule()

    assert(action_module.TRANSFERS_FILES is False)
    assert(action_module._VALID_ARGS == frozenset(('key', 'parents')))


# Generated at 2022-06-13 10:11:10.244851
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_arguments = {
        'key': 'test',
        'parents': 'test_group'
    }
    test_task = [{
        'args': test_arguments
    }]
    target = ActionModule(task=test_task)
    assert isinstance(target, ActionModule)



# Generated at 2022-06-13 10:11:10.903335
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	assert 1==1


# Generated at 2022-06-13 10:11:11.398308
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:12:15.967757
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:12:26.890131
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock

    action_module_class = ActionModule(task=mock.Mock(), connection=mock.Mock(), play_context=mock.Mock())
    # Call run method
    run = action_module_class.run()
    assert run['failed'] == True
    assert run['msg'] == "the 'key' param is required when using group_by"
    # Call run method with invalid params
    action_module_class = ActionModule(task=mock.Mock(), connection=mock.Mock(), play_context=mock.Mock())
    action_module_class._task.args = {'key': 'somethin', 'foo': 'bar'}
    run = action_module_class.run()
    assert run['failed'] == True

# Generated at 2022-06-13 10:12:36.933917
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostname = ''
    taskvars = {}
    def myloader(*args, **kwargs):
        return {'myplugin': {'myaction': ActionModule}}
    myclass = ActionModule(loader=myloader, hostname=hostname, taskvars=taskvars)
    myclass.task_vars = taskvars
    myclass.task = {'args': {'key': 'hostname'}}
    assert (myloader == myclass.loader)
    assert (hostname == myclass.hostname)
    assert (taskvars == myclass.task_vars)
    assert (myclass.task['args']['key'] == 'hostname')
    assert (myclass.TRANSFERS_FILES == False)

# Generated at 2022-06-13 10:12:38.337326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    #module.run()
    print(module)

# Generated at 2022-06-13 10:12:39.610845
# Unit test for constructor of class ActionModule
def test_ActionModule():
    group_module = ActionModule()
    assert group_module is not None


# Generated at 2022-06-13 10:12:48.655386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.docker_common import AnsibleDockerClient

    class Host():
        def get_name(self):
            return 'localhost'

    client = AnsibleDockerClient(None, None)
    my_host = Host()

    # Arguments
    my_key= 'single_key'
    my_parents= 'parent_key'
    my_task = {'args': {'key':my_key, 'parents':my_parents}}

    # Parameters
    my_tmp= 'tmp'
    my_task_vars = {'my_task_vars':'my_task_vars'}

    # Start the run
    results = ActionModule(client, my_host, my_task, my_tmp).run(my_tmp, my_task_vars)
    assert results['failed']

# Generated at 2022-06-13 10:12:56.871715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given
    action_module = ActionModule()
    task_vars = dict()
    tmp = '/tmp'
    task = dict(
        action=dict(
            module_name='group_by'
        ),
        args=dict(
            key='key1'
        )
    )

    # When
    result = action_module.run(tmp, task_vars, task=task)

    # Then
    assert result == dict(failed=False, changed=False, _ansible_no_log=False, msg='', add_group='key1', parent_groups=['all'])



# Generated at 2022-06-13 10:13:06.872118
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import types

    # The code to be tested

# Generated at 2022-06-13 10:13:07.762675
# Unit test for constructor of class ActionModule
def test_ActionModule():
	assert True

# Generated at 2022-06-13 10:13:08.355176
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass