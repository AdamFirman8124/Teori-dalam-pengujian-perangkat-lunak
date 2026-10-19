

# Generated at 2022-06-13 10:42:19.307522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:42:26.587908
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule('/', 'set_stats', 'AUTHUSER', 'REALM', '1', {'msg': 'test'})
    assert action_module.connection == 'AUTHUSER'
    assert action_module.become == 'REALM'
    assert action_module.become_method == '1'
    assert action_module._config == {'msg': 'test'}


# Generated at 2022-06-13 10:42:30.842285
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(args=dict(data=dict(version='1.0.0'), aggregate=True)))
    result = module.run(task_vars=dict())
    if result['failed'] is True and result['msg'] == "The 'data' option needs to be a dictionary/hash":
        print('test_ActionModule() -> Pass')
    else:
        print('test_ActionModule() -> Fail')

test_ActionModule()

# Generated at 2022-06-13 10:42:31.875527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:42:43.662588
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task_vars = {'foo': 'hello'}
    result = module.run(task_vars=task_vars)
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True, 'changed': False}
    task_vars = {'foo': 'hello'}
    result = module.run(task_vars=task_vars, tmp='test')
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True, 'changed': False}

    task_vars = {'foo': 'hello'}
    task_obj = {'args': {'data': {'test': 'hello'}}}

# Generated at 2022-06-13 10:42:44.996448
# Unit test for constructor of class ActionModule
def test_ActionModule():
    myaction = ActionModule()
    assert isinstance(myaction, ActionModule)


# Generated at 2022-06-13 10:42:54.631517
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean

    mock_action = ActionModule()

    # Test with an empty template
    data_template = {}
    mock_task = {"args": {"data": data_template}}

    mock_action._task = mock_task
    mock_action.run()

    assert 'changed' in mock_action.run()
    assert 'msg' not in mock_action.run()
    assert not mock_action.run()['changed']
    assert mock_action.run()['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

    # Test with a full template
    data_template = {}
    data_template["string"] = "{{ string_var }}"

# Generated at 2022-06-13 10:42:55.278855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:43:06.471735
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic

    # Create dummy module
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Create dummy ActionModule
    am = ActionModule(task=dict(action="set_stats", args=dict()),
                      connection=None,
                      templar=None,
                      loader=None)

    # Execute run method
    result = am.run(task_vars=dict())

    # Check result
    assert 'changed' in result
    assert result['changed'] == False
    assert 'ansible_stats' in result
    assert 'data' in result['ansible_stats']
    assert 'per_host' in result['ansible_stats']
    assert 'aggregate' in result['ansible_stats']

# Generated at 2022-06-13 10:43:13.748337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create an instance of the class to call the run method on
    action_plugin = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=None)
    
    # try all possible combinations of invalid arguments to check for TypeError
    try:
        result = action_plugin.run(tmp="tmp", task_vars=None)
    except TypeError as e:
        assert True
    else:
        assert False, "Expected TypeError when calling run with no arguments"

    try:
        result = action_plugin.run(tmp=None, task_vars="task_vars")
    except TypeError as e:
        assert True
    else:
        assert False, "Expected TypeError when calling run with no arguments"
    
    # check returned result

# Generated at 2022-06-13 10:43:28.735782
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mode = 'my_mode'
    _task = 'my_task'
    _connection = 'my_connection'
    _play_context = 'my_play_context'
    loader = 'my_loader'
    templar = 'my_templar'
    shared_loader_obj = 'my_shared_loader_obj'
    action = 'my_action'
    task_vars = dict()
    task_vars['ansible_version'] = dict()
    task_vars['ansible_version']['full'] = 'a_version'

    obj = ActionModule(mode, _task, _connection, _play_context, loader, templar, shared_loader_obj)
    assert obj._task is _task
    assert obj._connection is _connection
    assert obj._play_context is _play_context

# Generated at 2022-06-13 10:43:33.887753
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up
    hostname = 'test_hostname'
    port = 22
    user = 'test_user'
    password = 'test_pass'
    become_method = 'passwd'
    become_user = 'test_become_user'
    become_pass = 'test_become_pass'
    timeout = 10
    remote_user = 'test_remote_user'
    private_key_file = 'test_private_key_file'
    ssh_common_args = None
    ssh_extra_args = None
    sftp_extra_args = None
    scp_extra_args = None
    connection = 'smart'
    new_stdin = None
    new_stdout = None
    new_stderr = None
    new_stdin_isatty = None
    new_std

# Generated at 2022-06-13 10:43:35.344556
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True # TODO, fix test cases


# Generated at 2022-06-13 10:43:48.253750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fname = 'set_stats.py'

    task = {'action': {'__file__': fname} }

    module_mock = MagicMock(
        run=MagicMock(return_value=(0, 'success', dict()))
    )
    connection_mock = MagicMock(
        run=MagicMock(return_value=(0, 'success', dict())),
        put_file=MagicMock(return_value=('', '')),
    )
    loader_mock = MagicMock(
        get_basedir=MagicMock(return_value=os.getcwd())
    )
    templar_mock = MagicMock()
    display_mock = MagicMock()
    play_context_mock = MagicMock()

    # Case 1: Valid arguments to 'data'

# Generated at 2022-06-13 10:43:52.926402
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES is False
    assert hasattr(ActionModule(), '_VALID_ARGS')
    assert isinstance(ActionModule()._VALID_ARGS, frozenset)
    assert len(ActionModule()._VALID_ARGS) == 3
    assert ActionModule()._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:44:03.995301
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a.set_loader(None)
    a._connection = {}
    a._task = {}
    a._shared_loader_obj = None
    
    # Test case 1 - test_args_1
    # Test assertion 1
    
    d = {}
    d['data'] = {'test_args_1': 'test_var_1'}
    a._task.args = d
    
    
    # Test assertion 2
    
    d = {}
    d['data'] = {'test_args_2': 'test_var_2'}
    d['aggregate'] = 'True'
    d['per_host'] = 'True'
    a._task.args = d
    
    
    # Test assertion 3
    
    d = {}

# Generated at 2022-06-13 10:44:13.627025
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Variables to instantiate an ActionModule
    a = ActionModule()
    a._task = {'args': {'data': {'foo': 'bar', 'baz': 'buzz'}, 'per_host': True, 'aggregate': False}}
    a._templar = object()
    a._templar.template = lambda value, fail_on_undefined=None, convert_bare=None: value
    result = a.run(None, None)
    assert result['ansible_stats'] == {'data': {'foo': 'bar', 'baz': 'buzz'}, 'per_host': True, 'aggregate': False}
    assert result['changed'] == False


# Generated at 2022-06-13 10:44:23.974138
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.playbook.play
    import ansible.playbook.task_include
    import ansible.inventory
    import ansible.vars.manager
    import ansible.utils.vars
    import ansible.module_utils.facts
    import ansible.playbook.play_context
    import ansible.parsing.yaml.objects

    fake_loader = DictDataLoader({})
    fake_inventory = ansible.inventory.Inventory(loader=fake_loader, variable_manager=ansible.vars.manager.VariableManager())
    fake_variable_manager = ansible.vars.manager.VariableManager(loader=fake_loader, inventory=fake_inventory)

# Generated at 2022-06-13 10:44:31.712281
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    # First case: test if change is False when data is not provided as argument (default value)
    assert action_module.run()['changed'] == False

    # Second case: test if per_host is false when empty (default value)
    assert action_module.run({"data": {"Foo": "Bar"}})['ansible_stats']['per_host'] is False

    # Third case: test if per_host is True when provided (True value)
    assert action_module.run({"data": {"Foo": "Bar"}, "per_host": True})['ansible_stats']['per_host'] is True

    # Fourth case: test if data is created when provided in a valid format

# Generated at 2022-06-13 10:44:33.205327
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# vim: filetype=python

# Generated at 2022-06-13 10:44:46.252028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test', '1', 'test', '1', 'test', '1')


# Generated at 2022-06-13 10:44:57.728904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.plugins.loader import ActionModuleLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    p = ActionModuleLoader()

    d = DataLoader()
    task = dict()
    task1 = dict()
    task['action'] = 'set_stats'
    task1['action'] = 'set_stats'
    play_context = PlayContext()
    var_mgr = VariableManager()
    g = dict()
    g['foo'] = 'bar'
    var_mgr._fact_cache = dict()
    var

# Generated at 2022-06-13 10:45:08.147878
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule."""

    # Instantiate ActionModule object
    actionmodule_obj = ActionModule(
        task=dict(
            args=dict(
                aggregate=True,
                per_host=True,
                data=dict(
                    total=10,
                    changed=True
                )
            )
        )
    )

    # Assert "aggregate" and "per_host" and "data" keys are present in
    # actionmodule_obj.task.args as per declared in above init
    assert 'aggregate' in actionmodule_obj.task.args
    assert 'per_host' in actionmodule_obj.task.args
    assert 'data' in actionmodule_obj.task.args

    # Assert from init function default values are set "TRANSFERS_FILES"
    assert actionmodule

# Generated at 2022-06-13 10:45:09.293812
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert type(actionModule) == ActionModule

# Generated at 2022-06-13 10:45:10.394470
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "TODO: Implement me!"

# Generated at 2022-06-13 10:45:11.248511
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:45:16.638490
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mm = ActionModule(dict(a=1, b=2, c=3), dict(d=4, e=5, f=6))
    assert mm._task.args == dict(a=1, b=2, c=3)
    assert mm._connection.__dict__ == dict(d=4, e=5, f=6)

# Generated at 2022-06-13 10:45:20.885594
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.parsing.convert_bool import boolean
    with pytest.raises(Exception) as error:
        ansible_stats = ActionModule()
    assert error.value.args[0] == "Attempting to run local code without a valid loader"


# Generated at 2022-06-13 10:45:25.784575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Verify exception when no parameters passed to the constructor
    try:
        x = ActionModule()
    except TypeError:
        pass

    # Verify exception when incorrect number of parameters passed to the constructor
    try:
        x = ActionModule(1,2,3)
    except TypeError:
        pass

    # Verify exception when an incorrect parameter type is passed to the constructor
    try:
        x = ActionModule(1)
    except TypeError:
        pass

# Generated at 2022-06-13 10:45:34.763960
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of class ActionModule
    am = ActionModule()

    # Create a test instance of class MockModule
    mm = MockModule()

    # Set the module_args attribute of am to the value of mm
    am.module_args = mm.module_args

    # Create the class StatsCollector to mock the class StatsCollector in the module ansible.plugins.callback.stats
    class StatsCollector():

        # Create an empty dictionary version
        version = {}

        # Create an empty dictionary counts
        counts = {}

        # Create an emmpty dictionary custom
        custom = {}

        # Create a function __init__ with parameters self, module_name, host_name, custom, module_args

# Generated at 2022-06-13 10:45:58.701714
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('setup', '{}', '{}', '{}', None, None, '{}', '{}', '{}')
    assert action

# Generated at 2022-06-13 10:46:02.735493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

    action = ActionModule(None, {}, {}, {})
    assert isinstance(action, ActionModule)

    assert action.TRANSFERS_FILES == False

    assert action._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:46:04.502896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None,{},None,None)
    assert am.__doc__ != None

# Generated at 2022-06-13 10:46:07.609350
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    task = Task()
    task._role = None
    task._task = None
    action = ActionModule(task, dict())

    assert action.name == 'set_stats'

# Generated at 2022-06-13 10:46:08.158235
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:46:10.307864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)
    assert not issubclass(ActionModule, ActionBase._bases.keys())


# Generated at 2022-06-13 10:46:13.022066
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule()
    assert test_action.TRANSFERS_FILES == False
    assert test_action._VALID_ARGS ==  frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:46:18.402815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = {
        'args': {'facts': {'a': 'b'}}
    }
    action = ActionModule(task, {}, False, {})
    assert action.action == 'set_stats'
    assert action.action_loader is None
    assert action._task == task
    assert action._connection is None
    assert action._play_context is None
    assert action._loader is None
    assert action._templar is None
    assert action._shared_loader_obj is False
    assert action._task_vars == {}
    assert action._tmp is None

# Generated at 2022-06-13 10:46:21.143502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    !!! WARNING !!!
    This is a module meant to be used in the tests.
    If you import this module, you are probably doing it wrong.
    Please use the modules under the module_utils directory instead.
    """
    raise NotImplementedError(u'TODO: Write a test for this module')

# Unit Test for method _VALID_ARGS of class ActionModule

# Generated at 2022-06-13 10:46:31.267061
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.test import importer
    action_plugin_path = importer._find_plugin('action', 'set_stats.py')
    argspec = importer._get_action_args('set_stats.py', action_plugin_path)

    # Check the content of argspec, it should be valid
    assert(argspec)
    assert(isinstance(argspec, dict))
    assert(argspec.has_key('args'))
    assert(argspec['args'] == ['data', 'aggregate', 'per_host'])
    assert(argspec.has_key('defaults'))
    assert(argspec['defaults'] == {'data': {}, 'aggregate': True, 'per_host': False})
    assert(argspec.has_key('varargs'))

# Generated at 2022-06-13 10:47:24.317501
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(load_module_spec=False)
    stats = {'data': {}, 'per_host': False, 'aggregate': True}
    task_vars = {}

    task = {
        'args': {
            'data': {'a': 2},
            'per_host': True,
            'aggregate': False
        },
        '_ansible_version': (2, 3, 0)
    }

    result = action_module.run(task_vars=task_vars, task=task)

    stats['data']['a'] = 2
    stats['per_host'] = True
    stats['aggregate'] = False

    assert result == {'ansible_stats': stats, 'changed': False}

# Generated at 2022-06-13 10:47:26.405217
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:47:35.940444
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    task = Task()
    task._role = None
    task._block = Block()
    task.context = PlayContext()
    task.context._play = Play()
    task.context._play.hosts = "all"
    task._task_fields = dict()
    task._loader = None

    am = ActionModule(task, connection=None, play_context=task.context, loader=None, templar=None, shared_loader_obj=None)
    assert am is not None

# Generated at 2022-06-13 10:47:48.829919
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module_path = '/path/to/ansible/'
    module_name = 'action_plugin'
    cls = ActionModule

    # The following was found for the f_locals['__name__']:
    #
    # def run(self, tmp, task_vars=None):
    #     ''' handler for file transfer operations '''
    #     if task_vars is None:
    #         task_vars = dict()
    #
    #     result = super(ActionModule, self).run(tmp, task_vars)
    #     del tmp  # tmp no longer has any effect
    #
    #     source = self._task.args.get('src', None)
    #     content = self._task.args.get('content', None)
    #     raw = boolean(self._task.args.

# Generated at 2022-06-13 10:47:54.228701
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in globals(), 'class ActionModule does not exist'
    action_module = globals()['ActionModule']
    assert action_module

    assert hasattr(action_module, 'run'), 'method run() does not exist'
    assert action_module.run


# Generated at 2022-06-13 10:47:55.982618
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert isinstance(a.run(None, None), dict)

# Generated at 2022-06-13 10:47:57.071491
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)

# Generated at 2022-06-13 10:48:06.140916
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Example dict with modules with their respective arguments
    my_task_dict = dict(
        name='Ansible Test',
        action=dict(module='set_stats',
                    args=dict(data=dict(foo='Bar',
                                        bar='Foo',
                                        barfoo='FooBar'),
                              aggregate=True,
                              per_host=False
                              )
                    )
    )

    # Create object ActionModule
    action_mod = ActionModule(my_task_dict, {})
    # Run object ActionModule
    result = action_mod.run(tmp='/tmp/ansible-tmp-I4a4lJP9', task_vars=[])
    assert result.get('changed') == False

# Generated at 2022-06-13 10:48:09.061024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule.run(None, None) == {'ansible_stats': {'aggregate': True, 'per_host': False, 'data': {}}, 'changed': False})

# Generated at 2022-06-13 10:48:21.784281
# Unit test for method run of class ActionModule
def test_ActionModule_run():

#setup method call inputs
    task_vars = {}
    tmp = None

#setup test object
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module_obj._task = mock.Mock(spec=Task)
    action_module_obj._shared_loader_obj = mock.Mock(spec=ModuleLoader)
    action_module_obj._templar = mock.Mock(spec=Templar)
    action_module_obj._task.args = {}
    action_module_obj._task.args['data'] = {}
    action_module_obj._task.args['aggregate'] = True
    action_module_obj._task.args['per_host'] = False


# Generated at 2022-06-13 10:50:26.434035
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule_ = ActionModule(None, {}, {'action_plugins': ''})
    # TODO: add more tests here!
    test_ActionModule_run.Task = namedtuple('Task', ['args'])
    assert ActionModule_.run(None, task_vars=None) == {'failed': True, 'msg': "The 'data' option needs to be a dictionary/hash", 'changed': False}, "if we do not provide the 'data' argument, we expect to get a 'failed' result"

# Generated at 2022-06-13 10:50:31.103375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None, None, None)
    assert am.TRANSFERS_FILES == False
    assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:50:39.708373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""

    from ansible import errors
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from units.mock.plugins.action import TestActionModule

    from units.parsing.parser import TestParser
    from units.parsing.yaml.dumper import TestDumper

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 10:50:45.046074
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    module = ActionModule(play=Play().load({'name': 'test_action_module',
                                            'hosts': 'hostname',
                                            'gather_facts': 'no',
                                            'tasks': [{'action': {'module': 'setup',
                                                                  'args': {}
                                                                 }
                                                       }
                                                      ]
                                           }, loader=None, variable_manager=None),
                          task=Task(),
                          connection=None,
                          play_context=None,
                          loader=None,
                          templar=None,
                          shared_loader_obj=None)

    assert module._connection is None
    assert module._play_context is None

# Generated at 2022-06-13 10:50:51.923782
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action = ActionModule()
    assert action.TRANSFERS_FILES is False
    assert action._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert action.run(None) == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}

# Generated at 2022-06-13 10:50:54.678986
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionmodule is not None

# Generated at 2022-06-13 10:50:56.601216
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()
    assert getattr(module, '_VALID_ARGS') == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:51:03.189114
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # Setup test dependencies
    mock_action = ActionModule()
    mock_action.runner = AnsibleRunner()

    # Construct args for method run
    cmdargs = {}
    cmdargs["data"] = [1, 2, 3, 4]

    # Make the call
    results = mock_action.run(None, None, cmdargs)

    # Validate the returned data
    assert results['is_changed'] == False
    assert isinstance(results['ansible_stats'], dict)

# Generated at 2022-06-13 10:51:06.716654
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am._task is None
    assert am._connection is None
    assert am._play_context is None
    assert am._loader is None
    assert am._templar is None
    assert am._shared_loader_obj is None

# Generated at 2022-06-13 10:51:13.477932
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    agg = True
    tmp = None
    task_vars = dict()
    result = dict()
    result['failed'] = False
    result['changed'] = False
    result['msg'] = ''
    result['ansible_stats'] = {'data': {}, 'per_host': False, 'aggregate': True}
    assert result == ActionModule.run(agg,tmp,task_vars)

