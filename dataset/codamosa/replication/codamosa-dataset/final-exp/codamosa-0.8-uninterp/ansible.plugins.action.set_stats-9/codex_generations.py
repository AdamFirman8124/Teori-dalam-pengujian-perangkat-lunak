

# Generated at 2022-06-13 10:42:18.125357
# Unit test for constructor of class ActionModule
def test_ActionModule():

    actionModule = ActionModule(None, None, None, None, None)
    out = actionModule.run(None, None)
    assert out == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}

# Generated at 2022-06-13 10:42:20.549993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task_vars=[], wrap_async=False)

    print(action._task)
    print(action._play_context)

# Generated at 2022-06-13 10:42:24.328909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:42:27.923231
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(args=dict(data=dict(foo='bar'))))
    assert module._task.args['data'] == {'foo': 'bar'}
    assert module._task.args['data']['foo'] == 'bar'

# Generated at 2022-06-13 10:42:40.521188
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(args=dict()),
        connection=dict(host='localhost', port=1234, user='dummy', password='dummy'),
        play_context=dict(port=1234, remote_addr='localhost'),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert isinstance(action_module.task.args, dict)
    assert action_module.task.args == dict()
    assert isinstance(action_module.connection, dict)
    assert action_module.connection == dict(host='localhost', port=1234, user='dummy', password='dummy')
    assert isinstance(action_module.play_context, dict)

# Generated at 2022-06-13 10:42:47.153416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    datadict = {'1': 2}
    templar = None
    task = None
    assert ActionModule(templar, task).run() == {'ansible_stats': {'per_host': False, 'aggregate': True, 'data': {}}}
    task = {'args': {'aggregate': False, 'per_host': True, 'data': datadict}}
    assert ActionModule(templar, task).run() == {'ansible_stats': {'per_host': True, 'aggregate': False, 'data': datadict}}

# Generated at 2022-06-13 10:42:56.674861
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_result import TaskResult
    from avi.sdk.utils.samples import load_sample_local
    from avi.sdk.tests.mocks import Mock

    play = load_sample_local(
        load_file='avi/ansible/avi_network.yaml', name='avi_network.yaml')

    play_context = play.get_context()
    play_context.network_conf = play.set_network_conf(play_context)
    play_context.cloud_conf = play.set_cloud_conf(play_context)
    play_iterator = PlayIterator(play=play)

# Generated at 2022-06-13 10:42:59.430951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sut = ActionModule.__new__(ActionModule)
    assert sut
    assert isinstance(sut, ActionModule)
    assert sut._task.args == {}

# Generated at 2022-06-13 10:43:09.876915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    class FakeTask(object):
        def __init__(self, args):
            self.args = args


# Generated at 2022-06-13 10:43:10.754149
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict())

# Generated at 2022-06-13 10:43:17.429221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action is not None

# Generated at 2022-06-13 10:43:20.445405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        import mock
    except ImportError:
        print("skipping test_ActionModule, mock module not installed")
    else:
        am = ActionModule()
        assert am._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:43:24.128755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # See lib/ansible/tests/unit/test_action.py for more tests
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module.run(tmp='', task_vars={}) == {'ansible_stats': {'aggregate': True, 'data': {}, 'per_host': False}, 'changed': False}

# Generated at 2022-06-13 10:43:32.082213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.set_stats import ActionModule
    from ansible.cli.adhoc import AdHocCLI
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    def print_object(obj):
        print(obj)
        print('\n')


# Generated at 2022-06-13 10:43:33.602518
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert(obj._templar is None)
    assert(obj._loader is None)
    assert(obj._task is None)

# Generated at 2022-06-13 10:43:38.347530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from io import StringIO
    from ansible.plugins.action import ActionModule as AModule
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible import constants as C

    C.DEFAULT_MODULE_PATH = ''
    add_all_plugin_dirs()

    # 1. Test with simple dictionary
    task = {'args': {'data': {'a': 'b'}}}
    task_vars = {}

    amod = AModule(task, task_vars=task_vars)
    res = amod.run(None, task_vars)
    assert res['ansible_stats']['data']['a'] == 'b'

    # 2. Test with dictionary with templates


# Generated at 2022-06-13 10:43:40.083583
# Unit test for constructor of class ActionModule
def test_ActionModule():
    if not ActionModule:
        raise Exception("Cannot import ActionModule")

# Generated at 2022-06-13 10:43:42.918682
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, dict())
    assert mod._templar is None
    assert mod._task is None
    assert mod._connection is None

# Generated at 2022-06-13 10:43:47.424463
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dict_1 = dict({"data": {}, "per_host": False, "aggregate": True})
    assert ActionModule.run(dict_1, task_vars=None) == dict_1
    assert ActionModule.run({}, task_vars=None) == dict_1

# Generated at 2022-06-13 10:43:54.508909
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup a fake task and module
    task_t = dict(action=dict(module_name='foo', module_args=dict()))
    module_m = dict()

    fake_ansible_module = dict(params=dict())

    # create the modules object and call the run method
    modules = ActionModule(task_t, fake_ansible_module, module_m, 'a', 'b')
    res = modules.run()

    # test the result was false
    assert isinstance(res, dict)
    assert 'ansible_stats' in res
    assert isinstance(res['ansible_stats'], dict)
    assert 'data' in res['ansible_stats']
    assert isinstance(res['ansible_stats']['data'], dict)
    assert 'per_host' in res['ansible_stats']

# Generated at 2022-06-13 10:44:04.476187
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:44:08.697917
# Unit test for constructor of class ActionModule
def test_ActionModule():
    data = dict()
    data['data'] = dict()
    data['per_host'] = False
    data['aggregate'] = True
    new_ActionModule = ActionModule(data, None)
    assert new_ActionModule._task.args == dict()


# Generated at 2022-06-13 10:44:15.766298
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_action_module = ActionModule()

    res = my_action_module.run()
    assert res['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
    assert 'ansible_facts' not in res

    # Here tmp has no effect, so just pass a dummy value
    res = my_action_module.run(tmp=None)
    assert res['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
    assert 'ansible_facts' not in res

    res = my_action_module.run(tmp=None, task_vars={'a': 'b'})
    assert res['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:44:20.337002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit Test for constructor of class ActionModule'''
    a = ActionModule(None,None)
    assert a._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert a.TRANSFERS_FILES == False


# Generated at 2022-06-13 10:44:31.703286
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # Load our testvars
    dataloader = DataLoader()
    testvars = dataloader.load_from_file('test/ansible/data/vars/test_set_stats.yml')

    # Set up the data for our test
    class TaskArgs(object):
        def __init__(self):
            self.args = {}
            self.args['per_host'] = True

# Generated at 2022-06-13 10:44:41.747242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''
    action = ActionModule()
    action.name = 'set_stats'
    action.local_action = True
    stats = {'changed': False, 'ansible_stats': {'data': {'key': 'value'}, 'per_host': False, 'aggregate': True}}

    # Unit test: data = {'key': 'value'}
    data = {'key': 'value'}
    local_action = {'data': data, 'per_host': False, 'aggregate': True}
    result = action.run(task_vars={}, tmp=None, **local_action)
    assert action.name == result['ansible_module_name']
    assert action.local_action == result['local_action']

# Generated at 2022-06-13 10:44:54.958838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(args=dict(
            data=dict(
                a=dict(a=1, b=2)),
            per_host=True,
            aggregate=False),
            verbosity=2,
            no_log=False),
        connection=None,
        play_context=dict(check_mode=False),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    stats = module.run()
    assert 'changed' in stats
    assert 'ansible_stats' in stats
    assert stats['ansible_stats']['aggregate'] == 'False'
    assert stats['ansible_stats']['per_host'] == 'True'

# Generated at 2022-06-13 10:44:55.951589
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:45:06.604278
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fixture = ActionModule(None, {})
    fixture.templar = 'templar'
    fixture._templar = '_templar'
    fixture._task = '_task'
    fixture._task.args = '_task.args'

    # Test with 'data' of a value other than dict
    fixture._task.args = {'data' : 2}
    action_module_res_1 = fixture.run(tmp='tmp', task_vars='task_vars')
    assert action_module_res_1 == {'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}, 'failed': True, 'msg': "The 'data' option needs to be a dictionary/hash"}

    # Test with 'data' of a value other than dict
    fixture

# Generated at 2022-06-13 10:45:09.481214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(load_params=dict())
    ret = a.run(tmp=None, task_vars=None)
    assert ret['changed'] == False
    assert ret['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:45:38.959411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def fake_templar(data):
        return data

    def fake_task_args(args):
        return args

    action_module = ActionModule()
    action_module._last_task_name = 'statistics'
    action_module._templar = fake_templar
    action_module._task = fake_task_args

    # Test with simple data
    action_module._task.args = dict()
    result = action_module.run(None, None)
    # Only changed should be True, everything else should be default
    assert result['changed'] == False
    assert result['ansible_stats']['data'] == dict()
    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['aggregate'] == True

    # Test with simple data
   

# Generated at 2022-06-13 10:45:45.965352
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    from ansible import context
    context._init_global_context(dict(config=dict(fact_caching='memory')))
    task_action = ActionModule(
        task=dict(args=dict()),
        connection=dict(),
        play_context=dict(become_method=None, become_user=None, remote_addr=None, passwords=None),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    test_result = task_action.run()
    assert test_result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
    context._clear_global_context()



# Generated at 2022-06-13 10:45:55.106720
# Unit test for constructor of class ActionModule
def test_ActionModule():
    _module = 'set_stats'
    _data = {'a': '2'}
    _args = {'data': _data, 'per_host': False, 'aggregate': True}
    _task = 'test'
    _task_vars = {'test': 'test'}

    _actionBase = ActionBase()
    _actionBase._task = _task
    _actionBase._task.args = _args

    _actionModule = ActionModule(_actionBase._task, _actionBase._connection, _actionBase._play_context,
                                 _actionBase._loader, _actionBase._templar, _actionBase._shared_loader_obj)

    assert _actionModule
    assert _actionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:46:04.151517
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible import context
    from ansible.playbook.play_context import PlayContext

    context.CLIARGS = {}
    context._init_global_context(CLIARGS=context.CLIARGS)

    context.CLIARGS['tags'] = ['test']
    context.CLIARGS['skip_tags'] = ['skip']
    context.CLIARGS['start_at_task'] = 'test'

    play_context = PlayContext()
    play_context.CLIARGS = context.CLIARGS


# Generated at 2022-06-13 10:46:06.515873
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:46:11.698473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.task import Task

    # initialize required objects
    task = Task()
    task.action = 'test'
    task_vars = dict()

    # this is the action class
    action = action_loader.get('set_stats.py', task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:46:13.634206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert not ActionModule.TRANSFERS_FILES

# Generated at 2022-06-13 10:46:14.954307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, None, None, None, None, None)
    am.run()


# Generated at 2022-06-13 10:46:20.514317
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    import ansible.constants as C
    import sys

    class Conn(object):
        def __init__(self, host):
            self.host = host

    class Runner(object):
        def __init__(self):
            self.host_vars = {
                'test_host_1': {},
                'test_host_2': {}
            }
            self.play = Play()


# Generated at 2022-06-13 10:46:23.308179
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor should create object of class ActionModule
    action_module_object = ActionModule(None, None)
    # The constructor produces a result with the correct keys
    expected_result = { 'changed': False, 'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True} }
    assert(action_module_object.result == expected_result)


# Generated at 2022-06-13 10:47:04.135713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__doc__ == 'Execute a module and set the result in a variable'

# Generated at 2022-06-13 10:47:05.163307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:47:11.723740
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Specify 'data' argument in task args.
    task_args = { 'data' : { 'a': {'b': 'c'}, 'd': False } }
    # Create a ActionModule object.
    action_module = ActionModule( {'task': {'args': task_args}}, {} )
    # Run method of object.
    result = action_module.run( {}, {} )
    # Assert the result is expected.
    assert result.get('ansible_stats') == {'data': {'a': {'b': 'c'}, 'd': False}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:47:22.175088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action as action
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Options:
        module_path = '.'
        connection = 'local'
        remote_user = 'remote_user'
        ack_pass = False
        sudo = False
        sudo_user = 'some_user'
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False

    class VariableManager:
        def __init__(self):
            self.vars = {}


# Generated at 2022-06-13 10:47:35.049495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionModule(ActionModule):
        def __init__(self, args=None, task_vars=None):
            super(MockActionModule, self).__init__(args=args, task_vars=task_vars)
            self.stats = {'data': {}, 'per_host': False, 'aggregate': True}

    class MockConnection(object):
        def __init__(self, ip_addr, port):
            self.ip_addr = ip_addr
            self.port = port
            self.params = {
                'ansible_user': self.ip_addr,
                'ansible_port': self.port
            }

        def get_option(self, key):
            return self.params.get(key, None)


# Generated at 2022-06-13 10:47:42.251396
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = {}
    result_expected = dict(changed = False, ansible_stats = dict(data = {'test':'value'}, per_host = False, aggregate = True))
    action_module._task.args = dict(data = dict(test = 'value'))
    action_module._task.action = 'debug'
    assert result == result_expected, result

# Generated at 2022-06-13 10:47:45.534427
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = ActionModule.run(tmp=None, task_vars=None)
    pass

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:47:53.146351
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action_module = ActionModule()

    task_vars = dict()
    task_vars['ansible_stats'] = {'data': {}, 'per_host': False, 'aggregate': True}
    result = action_module.run(tmp=None, task_vars=task_vars)

    assert 'changed' in result
    assert result['changed'] == False

    assert 'failed' in result
    assert result['failed'] == False

    assert 'ansible_stats' in result
    assert 'data' in result['ansible_stats']
    assert 'per_host' in result['ansible_stats']
    assert 'aggregate' in result['ansible_stats']

# Generated at 2022-06-13 10:47:56.476473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None, None)  # pylint: disable=unused-argument
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:47:59.269439
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)

    # TODO: mock module attributes
    #module.mock_attrs()

    # module.run()
    pass

# Generated at 2022-06-13 10:49:37.753713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule
    """
    actionmodule = ActionModule('test', 'module', 'run', 'task', 'loader')
    assert not actionmodule.TRANSFERS_FILES
    assert actionmodule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:49:47.460569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a class of class ActionModule
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    # Unit test for run method
    def run(self, tmp=None, task_vars=None):
        pass

    action_module.run = run

    assert action_module.TRANSFERS_FILES == False

    # Create a dictionary with key and value
    args = {'per_host': True, 'aggregate': False, 'data': {'key': 'value'}}

    # Create a dictionary with key and value
    task_vars = {'ansible_stats': {'data': {}, 'per_host': False, 'aggregate': True}}

    # Create a dictionary with key and value
    result

# Generated at 2022-06-13 10:49:49.098541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)


# Generated at 2022-06-13 10:49:51.248695
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(args=dict()))
    assert module._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
    assert module.run()['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

# Generated at 2022-06-13 10:49:56.277054
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import tempfile

    tmpdir = tempfile.mkdtemp()

    json_data = {
        "action": "set_stats",
        "index": 1,
        "name": "set_stats",
        "args": {
            "data": {
                "foo": "{{ foo }}.{{ bar }}",
                "bar": "{{ bar }}.{{ foo }}",
            }
        },
        "loop": "inventory_hostname",
        "loop_control": {
            "label": "test_loop_label"
        },
        "delegate_to": "test_delegate_to"
    }

    module = ActionModule(None, task=json_data, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:50:05.617727
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating an instance of class ActionModule
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    # Testing method run with all valid options
    stats = {'data': {'a': 1, 'b': 2}, 'per_host': False, 'aggregate': True}
    results = {'ansible_stats': stats, 'changed': False}
    assert action_module.run(task_vars={'var': 'var'}) == results

    # Testing method run with invalid options
    assert action_module.run(task_vars={'ansible_stats': '123'})['failed'] == True

    # Testing method run with invalid options
    assert action_module.run(task_vars={'ansible_stats': ['123']})['failed'] == True

   

# Generated at 2022-06-13 10:50:07.733825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None)
    assert module is not None

    # TODO: test _VALID_ARGS, TRANSFERS_FILES, run()


# Generated at 2022-06-13 10:50:17.387639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic

    # initialize our module
    basic._ANSIBLE_ARGS = None
    mymod = ActionModule(
        task=dict(args=dict(per_host=False, aggregate=True, data=dict(a=True, b=False, c=1.1, d=2.2, e=3.3, var_to_remove=None))),
        connection=dict(),
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    result = mymod.run(task_vars=dict())
    assert result['failed'] == False
    assert result['changed'] == False
    assert result['ansible_stats']['per_host'] == False

# Generated at 2022-06-13 10:50:24.566413
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_args = dict(
        data = dict(
            value1 = 'test_value1',
            value2 = 'test_value2'
        )
    )

    task_vars = dict()
    result = dict()

    class ActionModuleStub(ActionModule):

        def _execute_module(self, tmp=None, task_vars=None, **kwargs):
            return dict(
                ansible_facts = dict(
                    fact_value = 'test_fact'
                ),
                changed = False,
                msg = "OK"
            )


# Generated at 2022-06-13 10:50:26.288019
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    print (action.__doc__)