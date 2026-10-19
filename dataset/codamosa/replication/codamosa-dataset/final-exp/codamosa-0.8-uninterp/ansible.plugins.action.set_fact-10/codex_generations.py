

# Generated at 2022-06-13 10:42:18.848326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=dict(args=dict(hello="world", foo='{{ bar }}')))
    assert am._task.args['hello'] == 'world'
    assert 'baz' not in am._task.args

# Generated at 2022-06-13 10:42:29.315244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: the module_utils/parsing/convert_bool.py does not have assert_equals for boolean()
    assert boolean('yes')
    assert boolean('no')
    assert boolean('true')
    assert boolean('false')

    assert not boolean('foo')

    assert not boolean('', strict=False)  # empty is False
    assert not boolean('', strict=True)
    assert not boolean(None, strict=False)
    assert not boolean(None, strict=True)
    assert boolean(1, strict=False)
    assert not boolean(1, strict=True)

    # test strict mode, do not convert integers
    assert not boolean(0, strict=True)
    assert not boolean(1, strict=True)
    assert not boolean(2, strict=True)

    assert boolean(0) is False
    assert boolean

# Generated at 2022-06-13 10:42:41.887705
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector

    # Create a new instance
    # We need to do this because the default values for the arguments of the _execute_module() method
    # will be different in this test and in normal execution, so the validation code will fail.
    action_obj = ActionModule()
    action_obj._task = type('task', (object,), {})

    import platform
    import sys

    current_os = platform.system()
    if current_os == 'Linux':
        sys_platform = 'Linux'
    elif current_os == 'Darwin':
        sys_platform = 'Darwin'
    else:
        sys_platform = 'Generic'

# Generated at 2022-06-13 10:42:42.907091
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)

# Generated at 2022-06-13 10:42:43.287864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:42:52.811390
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test empty annotations
    test = ActionModule({'args': {}}, {}).run()
    assert test['failed']
    assert test['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # Test correct usage
    test = ActionModule({'args': {'myvar': 'myvalue'}}, {}).run()
    assert not test['failed']
    assert test['ansible_facts'] == {'myvar': 'myvalue'}

    # Test non-identifier variable name
    test = ActionModule({'args': {'with space': 'value'}}, {}).run()
    assert test['failed']
    assert test['msg'] == "The variable name 'with space' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."

# Generated at 2022-06-13 10:43:03.631706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with reasonable arguments
    module = ActionModule(
        task=dict(
            args=dict(
                key1=10,
                key2=20,
                cacheable=False,
            ),
        ),
        connection=dict(),
        play_context=dict(
            ansible_version=dict(
                full='16.01.21.8068',
                major='16',
                minor='01',
                revision='21.8068',
            ),
            revision_hash='1d865e17',
            transport='cli',),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    # Test with reasonable arguments

# Generated at 2022-06-13 10:43:04.813078
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = ActionModule(None, None)
    assert test != None

# Generated at 2022-06-13 10:43:13.480514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test: set allowed keys as a single value
    action_module = ActionModule()
    action_module.allowed_keys = 'test_key_0'
    action_module._task.args = {'test_key_0': 'test_value_0'}
    assert action_module.run()['ansible_facts']['test_key_0'] == 'test_value_0'

    # Test: set allowed keys as a list of values
    action_module = ActionModule()
    action_module.allowed_keys = ['test_key_1', 'test_key_2', 'test_key_3']

# Generated at 2022-06-13 10:43:15.165960
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None)
    assert not hasattr(action, '_templar')

# Generated at 2022-06-13 10:43:21.548804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 10:43:30.586724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    t = Task()
    t._role_name = 'test'
    t._parent = TaskInclude()
    t._parent._role_name = '_test'

    task_vars = dict(a=True)
    tmp = None
    module = t.action
    assert(isinstance(module, ActionModule))
    module.run(tmp, task_vars)

    module = ActionModule()
    result = module.run(tmp, task_vars)
    assert(isinstance(result, dict))
    assert(result == {'ansible_facts': {}, '_ansible_facts_cacheable': False})

    module = ActionModule()
    module._task.args = dict(a=True)

# Generated at 2022-06-13 10:43:36.390998
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    task = TaskInclude()
    setattr(task, '_role_name', 'myrole')
    setattr(task, '_task_name', 'mytask')
    setattr(task, 'args', dict(
        key1='value1',
        key2='value2',
        cacheable='true'
    ))
    context.CLIARGS = dict()

    m = ActionModule(task, dict())

# Generated at 2022-06-13 10:43:43.104540
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test standard ActionModule creation
    action_mod = ActionModule(
        task=dict(action=dict(module_name='debug', args=dict(msg='CHANGED'))),
        connection=dict(host=None, port=None),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert action_mod is not None

# Generated at 2022-06-13 10:43:45.671869
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, {}, None, None)
    assert isinstance(a, ActionModule)
    assert hasattr(a, 'run')

# Generated at 2022-06-13 10:43:46.367468
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:43:47.598385
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:43:53.270987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing ActionModule for exceptions')
    a = ActionModule()

# Generated at 2022-06-13 10:43:55.135250
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:44:08.788356
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    try:
        from ansible.module_utils.facts.system.distribution import Distribution
        Dist = Distribution()
    except ImportError:
        from ansible.module_utils.facts.linux.distribution import Distribution
        Dist = Distribution()

    from ansible.compat.tests.mock import patch
    from ansible.compat.six import BytesIO

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import Distro

    am = AnsibleModule(
        argument_spec = dict(
            cacheable = dict(type='bool', required=False),
        )
    )


# Generated at 2022-06-13 10:44:21.410501
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(action=dict(module_name="setup")),
                                 connection=dict(),
                                 in_data=dict(),
                                 module_name="setup",
                                 task_vars=dict())

    assert action_module.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:44:29.857021
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # since these are all private methods, we don't need to mock anything
    # however we might want to do something about the loop for the last test
    # see https://github.com/ansible/ansible-modules-core/pull/3003
    from ansible.utils import module_docs
    from ansible.plugins.action.set_fact import ActionModule

    # todo: mock up temporary directory
    # using a local tmp directory is not optimal here
    # at least this is why is not working on Travis
    #tmp = tempfile.mkdtemp()
    #print(tmp)

    # hardcode the task vars and the cacheable flag
    # it doesn't really matter if this is true or false
    task_vars = dict()
    cacheable = False

    # init the class

# Generated at 2022-06-13 10:44:30.913946
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:44:34.541970
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert getattr(ActionModule, 'version', False)
    assert getattr(ActionModule, 'run', False)
    assert getattr(ActionModule, 'TRANSFERS_FILES', False)
    assert getattr(ActionModule, '_config_template', False)
    assert getattr(ActionModule, '_filter_result', False)

# Generated at 2022-06-13 10:44:37.121253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(None, None)
    result = actionModule.run(tmp=None, task_vars=None)
    assert result['failed']

# Generated at 2022-06-13 10:44:38.751180
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict(), dict())
    assert isinstance(action, ActionBase)

# Generated at 2022-06-13 10:44:46.095069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_queue_manager
    import ansible.executor.task_result
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader=None
    variable_manager._extra_vars = {'foo':'bar'}

    task_queue_manager.TaskQueueManager._terminated = True
    task_queue_manager.TaskQueueManager._final_q = task_queue_manager.TaskQueueManager._queue
    task = Task()

    task.action = 'set_fact'
    task.args = dict(my_fact='my_value')
    task.set_loader(loader)

# Generated at 2022-06-13 10:44:47.218274
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Not implemented"

# Generated at 2022-06-13 10:44:48.549856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:44:51.108350
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 10:45:08.514006
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_fact as action_module
    action = action_module.ActionModule(None, None, None, None)
    assert action is not None

# Generated at 2022-06-13 10:45:19.187980
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # AnsibleActionFail is a subclass of AnsibleError, therefore import it
    import ansible.errors as errors
    # C is a class used as constants in Ansible, therefore import it
    import ansible.constants as constants
    # ActionBase class is derived in ActionModule, therefore import it
    from ansible.plugins.action import ActionBase
    # Setting boolean is done in ActionModule, therefore import it
    from ansible.module_utils.parsing.convert_bool import boolean
    # This is used as a dictionary in ActionModule, therefore import it
    from ansible.utils.vars import isidentifier
    # Temporary class to test the constructor of ActionModule class
    class Temp():
        def __init__(self, runsource):
            self.args = {'cacheable': False}
            self.run_source = runsource
   

# Generated at 2022-06-13 10:45:20.248396
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)

    assert action_module is not None

# Generated at 2022-06-13 10:45:21.581467
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MyModule(ActionModule):
        pass

    assert MyModule


# Generated at 2022-06-13 10:45:30.116823
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # sample task
    task = dict(
        action=dict(
            __ansible_module__='set_fact',
            __ansible_arguments__=dict(
                one=1,
                two=2,
                three='3',
                four='4',
                five='off',
                six='on',
                seven=dict(
                    eight=8
                    )
                )
            )
        )

    # create an instance of the action plugin
    am = ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # call the run() method of the action plugin
    result = am.run(task_vars=dict())

    # assert the result of operation

# Generated at 2022-06-13 10:45:33.579067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am

# Generated at 2022-06-13 10:45:41.086830
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(args= {'name': 'value', 'name2': ['a','b','c']}),
        connection=dict(host='localhost'),
        play_context=dict(remote_addr='127.0.0.1'),
        loader=None,
        templar=None,
        shared_loader_obj=False
    )

    assert action is not None

# Generated at 2022-06-13 10:45:46.802357
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fixture = ActionModule('name', {'a': 1, 'b': 2})
    assert fixture.run() == {'ansible_facts': {'a': 1, 'b': 2}, '_ansible_facts_cacheable': False}
    fixture = ActionModule('name', {'a':'true', 'b':'false', 'c':'yes', 'd':'no', 'e':'on', 'f':'off'})
    assert fixture.run() == {'ansible_facts': {'a': True, 'b': False, 'c': True, 'd': False, 'e': True, 'f': False}, '_ansible_facts_cacheable': False}

# Generated at 2022-06-13 10:45:47.245400
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:45:52.380821
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a test instance of ActionModule
    am = ActionModule()

    # Unit test for method run of class ActionModule where the input arguments are:
    # tmp=None task_vars=dict()
    actual_result = am.run()

    expected_result = {'ansible_facts': {}, '_ansible_facts_cacheable': False}

    assert actual_result == expected_result

# Generated at 2022-06-13 10:46:24.928889
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None,None,None)

# Generated at 2022-06-13 10:46:27.745475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ab = ActionModule()
    tmp = None
    task_vars = dict()
    result = ab.run(tmp, task_vars)
    assert result == 'STUB'

# Generated at 2022-06-13 10:46:30.537147
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:46:32.798798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task_vars = {}
    result = module.run(None, task_vars)
    assert result['failed']

# Generated at 2022-06-13 10:46:39.982450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    dict_args = dict(spam='foo')
    module = ActionModule(None, dict_args, False, None)
    
    # Test the member variables
    assert module.TRANSFERS_FILES == False
    
    # Test the internal function run
    # Test valid inputs
    dict_tmp = dict()
    dict_task_vars = dict(foo='bar', foo_facts={'spam': 'foo'})
    result = module.run(dict_tmp, dict_task_vars)
    
    # Test invalid inputs
    dict_task_vars2 = dict(foo='bar')
    
    try:
        module.run(dict_tmp, dict_task_vars2)
    except AnsibleActionFail:
        # Expected failure
        
        pass
    

# Generated at 2022-06-13 10:46:51.042365
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: this test is not complete.
    # We should probably add some error testing and a proper test of the resulting output
    from ansible.utils import prepare_writeable_dir
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import isidentifier
    import os

    tmpdir = prepare_writeable_dir(C.DEFAULT_LOCAL_TMP, os.geteuid())
    localhost = dict(
        ansible_python_interpreter=sys.executable
    )

    # NOTE: I don't know if this is the proper way

# Generated at 2022-06-13 10:46:51.703638
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: We don't have access to _templar
    assert False

# Generated at 2022-06-13 10:46:55.567225
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    am = ActionModule(load_fixture('playbook1.yml', 'playbook1'), dict(action='add_host', hostname='foobar', groupname='barfoo'))
    assert am.run(tmp=None, task_vars=dict(ansible_facts='test')) == {
                                                                      'failed': False,
                                                                      'ansible_facts': {'hostname': 'foobar', 'groupname': 'barfoo'}
                                                                     }



# Generated at 2022-06-13 10:46:56.641836
# Unit test for constructor of class ActionModule
def test_ActionModule():
  module = ActionModule('action_plugins/setup.py', 'setup', {}, None)
  assert module != None

# Generated at 2022-06-13 10:47:07.482393
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # given:
    # test action module instance
    am = ActionModule(
        task=dict(action=dict(module_name='set_fact')),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # when:
    # apply run() of new action module instance
    result = am.run(tmp=None, task_vars=None)
    # then:
    # verify result values
    assert(result['ansible_facts'] == {})
    assert(result['_ansible_facts_cacheable'] == False)
    # when:
    # run() of new action module with arguments
    result = am.run(tmp=None, task_vars=None)
    # then:
    # verify

# Generated at 2022-06-13 10:48:13.336460
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible.plugins.action.ActionModule(None)

# Generated at 2022-06-13 10:48:23.797273
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.include import Include
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    test_task = Task()
    test_task._role = Include()
    test_task._role._role_path = '/etc/ansible/roles/a_role'
    test_task._role._role_name = 'a_role'
    test_task._role._parent = test_task._role
    test_task._role._parent._parent = test_task._role
    test_task._role._parent._parent._parent = test_task._role

# Generated at 2022-06-13 10:48:24.879681
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = AnsibleActionModule()

# Generated at 2022-06-13 10:48:32.311719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json


# Generated at 2022-06-13 10:48:35.930644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    # TODO: Add better test coverage for this class

    module = ActionModule(task_vars=dict())

    assert module.run(tmp=None, task_vars=None) is not None

# Generated at 2022-06-13 10:48:37.319728
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    print(am)

    assert am is not None

# Generated at 2022-06-13 10:48:43.935286
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from units.compat import unittest

    from ansible.module_utils import basic
    from ansible.module_utils.six import iteritems, string_types
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.plugins.action import ActionBase
    import ansible.constants as C

    class FakePlayContext(object):
        def __init__(self):
            self.connection = 'local'
            self.timeout = 10
            self.module_name = 'test'
            self.remote_addr = '127.0.0.1'
            self.remote_tmp = '/tmp'


# Generated at 2022-06-13 10:48:45.611284
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES == 'False'

# Generated at 2022-06-13 10:48:49.571242
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, {}, None)
    assert isinstance(module, ActionModule)
    assert isinstance(module.TRANSFERS_FILES, bool)
    assert isinstance(module._task, dict)
    assert isinstance(module._templar, object)

# Generated at 2022-06-13 10:48:59.926339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.yaml.objects import AnsibleUnicode

    mod = AnsibleModule(
        argument_spec = dict(
            cacheable=dict(type='bool', required=False),
            xxx=dict(type='str', required=False),
        ),
        supports_check_mode=True
    )
    assert mod._name == 'test'


# Generated at 2022-06-13 10:52:09.973910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)
    result = action_module._execute_module(task_vars=dict(), wrap_async=None, tmp=None)
    
    assert(result['failed'])

# Generated at 2022-06-13 10:52:11.469122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())