

# Generated at 2022-06-13 09:34:27.722124
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins import action_plugins
    from ansible.playbook.task import Task

    class Mock(object):

        def __init__(self):
            self.vars = {'a': '1', 'b': '2'}
            self.module_args = {'fail_msg': 'Failed assertion'}

        def get_name(self):
            return 'fail'

        def get_loader(self):
            class LoaderMock(object):
                def load_from_file(self, filename):
                    return 'content'

                def get_basedir(self, filename):
                    return 'basedir'

            return LoaderMock()

    class TaskMock(Task):

        def __init__(self, args):
            self.args = args

        def role_params(self):
            return {}

# Generated at 2022-06-13 09:34:38.707215
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    #create an instance of the class
    test = ActionModule()

    #Test for args = none
    assert test.run(task_vars={}) == {'failed': True, 'evaluated_to': False, 'assertion': None, 'msg': 'Assertion failed'}

    #Test for args = 'fail_msg'
    assert test.run(task_vars={'arg_fail_msg':'Assertion failed'}) == {'failed': True, 'evaluated_to': False, 'assertion': None, 'msg': 'Assertion failed'}

    #Test for args = 'msg'

# Generated at 2022-06-13 09:34:44.637805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(name='test-task')
    task['args'] = {'that': ['a > b'], 'fail_msg': 'Assertion failed'}
    assert not ActionModule(task, dict()).run(None, dict())['failed']


# Generated at 2022-06-13 09:34:53.294640
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

# Generated at 2022-06-13 09:35:07.436082
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """

    module = 'assert'
    timeout = 100
    remote_user = 'root'
    remote_pass = ''
    remote_port = 22
    private_key_file = None
    remote_conn = None
    transport = 'local'
    #task_args = {'that': ''}
    task_vars = {}

    loader = 'something'
    templar = ''

    action_base_obj = ActionBase(loader, templar, task_vars)
    action_base_obj._connection = remote_conn
    action_base_obj._task.args = {}
    action_base_obj._loader = loader
    action_base_obj._templar = templar
    action_base_obj._task_vars = task_v

# Generated at 2022-06-13 09:35:17.505524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_name = "assert"
    module_args = {"that": "1 == 1"}
    kwargs = {}
    kwargs['task_vars'] = {}
    kwargs['tmp'] = {}
    kwargs['task_vars']['service_name'] = 'test'
    kwargs['task_vars']['enabled'] = True
    kwargs['task_vars']['failures_expected'] = True

    ins = ActionModule(module_name, module_args, **kwargs)
    ins.run(module_args, kwargs['task_vars'])


# Generated at 2022-06-13 09:35:24.744373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys

    import ansible.utils.template as template
    import ansible.playbook.conditional as conditional
    import ansible.playbook.play_context as play_context
    import ansible.vars.hostvars as hostvars
    import ansible.vars.manager as vars_manager
    import ansible.vars.hostvars as hostvars
    import ansible.vars.clean as vars_clean

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-13 09:35:34.242808
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action._task is None
    assert action._connection is None
    assert action._play_context is None
    assert action._loader is None
    assert action._templar is None
    assert action._shared_loader_obj is None
    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert not action.TRANSFERS_FILES
    assert not action.BYPASS_HOST_LOOP



# Generated at 2022-06-13 09:35:40.627222
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins
    action = ansible.plugins.action.ActionModule(None, None, False, '/dev/null')
    assert action
    assert type(action._VALID_ARGS) == 'frozenset'
    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:35:42.447951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("testing ActionModule constructor")
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 09:35:50.001190
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 09:35:51.713386
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, {}), ActionModule)

# Generated at 2022-06-13 09:35:53.144369
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_class_instance = ActionModule()
    test_class_instance.run()

# Generated at 2022-06-13 09:35:54.183688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 09:35:56.424647
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    mod2test = ActionModule(ActionBase(), dict())

    assert mod2test.TRANSFERS_FILES == False
    assert mod2test._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))



# Generated at 2022-06-13 09:36:08.297423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    t = Task()
    t.args = {}
    t.action = 'assert'

    action = ActionModule(t, {})

    # Test with fail_msg
    t.args['fail_msg'] = "Fail Msg"
    t.args['success_msg'] = "Success Msg"
    t.args['that'] = ["'name' == 'joe'"]

    task_vars = VariableManager()
    task_vars.extra_vars = {'name': 'joe'}

    # Test with fail_msg as a list
    t.args['fail_msg'] = ["Fail Msg1", "Fail Msg2"]
    t.args['success_msg'] = ["Success Msg1"]


# Generated at 2022-06-13 09:36:16.623071
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_data = {
        'module_name': 'assert',
        '_ansible_no_log': False,
        '_ansible_verbose_always': False,
        'changed': False,
        '_ansible_module_name': 'assert'
    }

    action_module = ActionModule(MockTask(MockTask.TASK_VARS), MockTask(MockTask.TASK_RESULTS))
    action_module._task = MockTask(MockTask.TASK_TMP)
    action_module._task.args = {'fail_msg': 'foo', 'that': ['one', 'two', 'three']}

    assert action_module.run() == mock_data


# Generated at 2022-06-13 09:36:17.441077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:36:17.953307
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:36:24.864603
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test_play_context and test_task are passed as the required arguments to the constructor.
    # To setup those objects we first need to setup loader and variable_manager objects
    options = dict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
                   become_method=None, become_user=None, check=False, diff=False)

    # setup the loader object
    loader = DataLoader()

    # Setup the variable manager
    variable_manager = VariableManager()

    # Instantiate play context
    p_ctx = PlayContext()
    p_ctx._init_globals()
    p_ctx.variable_manager = variable_manager
    p_ctx.loader = loader

    # Setup a test task
    t_vars = dict()

# Generated at 2022-06-13 09:36:50.478440
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    t = Task()
    c = ActionModule(t, dict(), False, None)

    # test with fail_msg
    t.args = dict(that=['item == 1', 'item != 1'], fail_msg='Some fail_msg', quiet=True)
    result = c.run(tmp=None, task_vars=dict(item=1))
    assert result['msg'] == 'Some fail_msg'
    assert result['evaluated_to'] is False
    assert result['assertion'] == 'item != 1'

    # test without fail_msg
    t.args = dict(that='item != 1', quiet=True)
    result = c.run(tmp=None, task_vars=dict(item=1))

# Generated at 2022-06-13 09:36:58.142043
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dict1 = dict(
        ansible_module_name='test',
        ansible_module_args=dict(
            fail_msg='Assertion Failed',
            that='1 == 0',
            quiet=True
        ),
        ansible_facts=dict(),
        ansible_play_hosts='127.0.0.1',
        ansible_playbook_python='/usr/bin/python',
        ansible_version='2.4.0',
        ansible_version_full='2.4.0.0',
        ansible_version_major='2',
        ansible_version_minor='4',
        ansible_version_revision='0'
    )

# Generated at 2022-06-13 09:37:09.278758
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    variable_manager = VariableManager()
    loader = DataLoader()
    results_callback = PlaybookExecutor(playbooks=['/etc/ansible/ansible.cfg'],
                                        inventory=InventoryManager(loader=loader, sources=[]),
                                        variable_manager=variable_manager,
                                        loader=loader, passwords={}).run()
    inv_source = '''[localhost]
    127.0.0.1'''

# Generated at 2022-06-13 09:37:21.135263
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.inventory.manager

# Generated at 2022-06-13 09:37:22.820437
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert not action.TRANSFERS_FILES

# Generated at 2022-06-13 09:37:30.585778
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Test of constructor in case of quiet = False, msg = None and success_msg = None
    failed_result = {'assertion': 'false', 'failed': True, '_ansible_verbose_always': True, 'evaluated_to': False}
    module = ActionModule(task=MockTask({'quiet': False}), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module.run(tmp=None, task_vars=dict()) == failed_result
    module = ActionModule(task=MockTask(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module.run(tmp=None, task_vars=dict()) == failed_result

    # Test of constructor in

# Generated at 2022-06-13 09:37:45.252285
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.plugins.action import ActionBase
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from collections import namedtuple
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    import pprint
    import sys
    import pytest
    from io import StringIO
    import os

    class TaskMock(Task):
        def __init__(self):
            self

# Generated at 2022-06-13 09:37:58.890292
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = 'test1.example.com'
    from ansible import constants as C
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext
    C.HOST_KEY_CHECKING = False
    tmp = None
    task_vars = combine_vars(
        dict(),
        dict(),
        dict(),
    )
    task_vars['ansible_check_mode'] = False
    task_vars['ansible_verbosity'] = 2
    task_vars['ansible_version'] = dict(
        full='2.3.0.0',
        major=2,
        minor=3,
        revision=0,
        string='2.3.0.0',
    )

# Generated at 2022-06-13 09:38:10.633788
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    class AnsibleOptions(object):
        verbosity = 1
        listhosts = False
        subset = None
        extra_vars = []
        only_tags = []
        skip_tags = []
        inventory = None
        ask_vault_pass = False
        vault_password_files = []
        new_vault_password_file = None
        output_file = None
        tags = []
        skip_tags = []
        one_line = None
        tree = None
        ask_sudo_pass = False
        ask_su_pass = False
        sudo = None
        sudo_user = None
        become = None
        become_

# Generated at 2022-06-13 09:38:24.524634
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:39:11.658181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    import ansible.playbook.task
    name = 'assert'
    action1 = action_loader.get(name, class_only=True)()
    action2 = action_loader.get(name, class_only=True)()
    t1 = ansible.playbook.task.Task()
    t1._role = None
    t2 = ansible.playbook.task.Task()
    t2._role = None

    # TypeError exception should be raised if wrong number of arguments are passed to method run
    # of class ActionModule
    try:
        action1.run()
    except TypeError as e:
        assert "foo" not in str(e)

# Generated at 2022-06-13 09:39:15.947857
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    t = Task()
    b = Block()
    t.block = b
    t._role = None
    t.args = {'that': '{{ foo }}'}

    m = ActionModule(t, dict(ANSIBLE_MODULE_ARGS=dict()), False)
    assert m._templar is not None
    assert m._loader is not None

# Generated at 2022-06-13 09:39:17.402720
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        module = ActionModule(load_libs=False)
        assert(isinstance(module, ActionModule))
    except Exception as e:
        print(e)
        assert(False)


# Generated at 2022-06-13 09:39:21.283423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    testhost = 'localhost'
    testport = 22

    print(sys.path)
    print(os.path.abspath(os.path.curdir))
    print(os.path.abspath('.'))
    print(os.path.abspath('../'))

    ans_host = ansible_host.AnsibleHost(testhost,testport)
    print(ans_host.get_port())

    action = ActionModule(ans_host)
    action.run(dict())

if __name__ == '__main__':
    #print(sys.path)
    #print(os.path.abspath(os.path.curdir))
    #print(os.path.abspath('.'))
    #print(os.path.abspath('../'))

    test

# Generated at 2022-06-13 09:39:34.705590
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #from ansible.playbook.task import Task
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.six import string_types

    task_args = {'fail_msg': 'Test Fail Msg', 'success_msg': 'Test Success Msg', 'msg': 'Test Msg', 'quiet': True, 'that': 'a_value'}

# Generated at 2022-06-13 09:39:35.537638
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:39:49.819056
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # For testing, define a class that has same attributes as a real action plugin
    class FakeActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(ActionModule, self).run(tmp, task_vars)
            return result

    # Initialize an action module and a conditional object
    fake_am = FakeActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    cond = Conditional(loader=fake_am._loader)

    # Test when success_msg and fail_msg are passed as list

# Generated at 2022-06-13 09:39:56.364118
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, {}, None, None, None)
    assert am.VERSIONS is None
    am1 = ActionModule(None, {'fail_msg': 'msg'}, None, None, None)
    am2 = ActionModule(None, {'fail_msg': ['msg1', 'msg2']}, None, None, None)
    assert am1._VALID_ARGS == am2._VALID_ARGS
    assert am1.TRANSFERS_FILES == am2.TRANSFERS_FILES

# Generated at 2022-06-13 09:40:02.256538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test if ActionModule constructor can be invoked.
    # If constructor cannot be invoked, test will fail by exception.
    ActionModule(loader=None,shared_loader_obj=None, task=None, connection=None, play_context=None, loader_cache=None,
                 templar=None, ansible_vars=dict(), connection_loader=None, action_loader=None)


# Generated at 2022-06-13 09:40:13.409604
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # expected result
    result_expected = {
        'assertion': '1 == 1',
        'changed': True,
        'evaluated_to': True,
        'item': '1 == 1',
        'msg': 'All assertions passed',
        'when': '1 == 1',
    }

    # create fake task, module
    module_args = {
        'assertion': '1 == 1',
        'success_msg': 'All assertions passed',
        'quiet': False,
    }
    task_args = {
        'module_args': module_args,
    }
    task = {
        'args': task_args,
    }

    # object
    am = ActionModule(task, {})

    # run method
    result = am.run({}, {})

    assert(result == result_expected)

# Generated at 2022-06-13 09:41:20.647220
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json

    test_dest_file = './test_result'

# Generated at 2022-06-13 09:41:30.786415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    action/assert.py ActionModule unit test stub
    '''

    # Construct test object
    class AnsibleModuleMock():
        def __init__(self, argument_spec):
            self.argument_spec = argument_spec
            self.params = []
            self.args = dict()
        def fail_json(self, msg):
            raise AnsibleError(msg)
    class LoaderMock():
        def __init__(self, basedir):
            self.basedir = basedir
            self.path_relative_to_playbook = None
            self.set_basedir('.')
        def set_basedir(self, basedir):
            self.basedir = basedir
    class TaskMock():
        def __init__(self, args):
            self.args = args
    module = Ans

# Generated at 2022-06-13 09:41:37.918598
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_mod = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)
    fail_msg = "fail msg"
    success_msg = "success msg"
    that = ['fail msg', 'success msg']
    with pytest.raises(AnsibleError) as excinfo:
        action_mod.run(task_vars=None)
    excinfo.match('conditional required in "that" string')
    assert excinfo.type == AnsibleError
    result = action_mod.run(task_vars=dict(fail_msg=fail_msg, success_msg=success_msg), that=that)

# Generated at 2022-06-13 09:41:46.915597
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import __builtin__
    setattr(__builtin__, '__file__', '/foo/bar')


# Generated at 2022-06-13 09:41:47.363505
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:41:49.033761
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # No error is raises if the right arguments are passed.
    assert ActionModule({}, {}, '/dev/null') == None


# Generated at 2022-06-13 09:41:51.646439
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six import PY3
    if PY3:
        return

    # placeholder for the test code
    ActionModule()


# test blurb for function fail

# Generated at 2022-06-13 09:41:52.108365
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Test run')

# Generated at 2022-06-13 09:41:59.683566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create objects to be used by the test
    am = ActionModule()

    class ActionModule(object):
        def __init__(self):
            self._task = Task()

    class Task(object):
        def __init__(self):
            self.args = {}

    class AnsibleError(Exception):
        pass

    # Test 1: test run when that value is not specified
    try:
        am.run()
        assert False
    except AnsibleError as e:
        assert "conditional required in 'that' string" == str(e)

    # Test 2: test run when fail_msg or msg are not specified
    task = ActionModule()._task
    task.args['that'] = ['some_value']
    am._task = task
    result = am.run()

# Generated at 2022-06-13 09:42:10.849856
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    cls = ActionModule
    task_vars = dict()
    tmp = None

    # Fail with no fail_msg specified
    module._task.args = dict()
    module._task.args['that'] = '1 == 2'
    module._task.args['quiet'] = False
    module._task.args['success_msg'] = 'All assertions passed'
    result = module.run(tmp, task_vars)
    assert result['failed'] == True
    assert result['changed'] == False
    assert result['assertion'] == '1 == 2'
    assert result['evaluated_to'] == False
    assert result['msg'] == 'Assertion failed'

    # Fail with fail_msg specified
    module._task.args = dict()