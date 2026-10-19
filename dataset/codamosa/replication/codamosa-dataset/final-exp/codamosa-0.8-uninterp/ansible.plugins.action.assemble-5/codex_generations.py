

# Generated at 2022-06-13 09:23:49.122347
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test case of code coverage for #62435
    action_module = ActionModule([], None, None, None, None)
    action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 09:23:50.987239
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None, None, None)
    module.run(None, None)
    assert True

# Generated at 2022-06-13 09:23:53.155027
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:23:56.805807
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test input and output for the following method
    # run(self, tmp=None, task_vars=None)

    pass

# Generated at 2022-06-13 09:23:59.032921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: mock the run::
    # action_module = ActionModule(tmp=None, task_vars=None)
    # assert action_module.run(tmp=None, task_vars=None) == {"changed": False, "msg": "All items completed"}
    assert True

# Generated at 2022-06-13 09:24:07.397552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test for the ActionModule.run method
    """
    # 
    class MockTask(object):
        def __init__(self, args={}):
            self.args = args
        def get_args(self):
            return self.args
    # 
    class MockTaskVars(dict): pass
    # 
    class MockExecuteModule(object):
        def __init__(self, m=None, ma={}):
            self.m = m
            self.ma = ma
        def __call__(self, m=None, ma={}):
            return self.m, self.ma
    # 
    class MockExecuteRemoteStat(object):
        def __init__(self, all_vars=None):
            self.all_vars = all_vars

# Generated at 2022-06-13 09:24:09.535159
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a test ActionModule
    actionModule = ActionModule(loader=None, shared_loader_obj=None, path_loader=None, variables=None)
    # Call the method
    value = actionModule.run()
    # Catch the exception if method fails

# Generated at 2022-06-13 09:24:18.422884
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_dict = {
        '_uses_shell': False,
        '_task': None,
        '_loader': None,
        '_templar': None,
        '_shared_loader_obj': None,
        '_connection': None,
        '_play_context': None,
        '_loaded_action_plugin': None,
        '_task_vars': None,
        '_block_vars': None,
        '_task_vars': None
    }
    action_module = ActionModule(**test_dict)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:24:19.014303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Todo - create test
    pass

# Generated at 2022-06-13 09:24:24.040986
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('test ActionModule')
    import ansible.plugins
    ActionModule = ansible.plugins.action.ActionModule
    task = {'args': {'src': 'test_file'}}
    tmp = 'tmp'
    task_vars = {'a': 1}
    action_module = ActionModule(task, tmp, task_vars)

# Generated at 2022-06-13 09:24:36.288233
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test if the class itself can be created
    a = ActionModule()

# Generated at 2022-06-13 09:24:36.831599
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:24:47.674222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    remote_src = 'yes'
    regexp = None
    delimiter = "\n"
    ignore_hidden = False
    decrypt = True
    follow = False

    fake_task = {'args':
                    {'src': 'test_src_path',
                     'dest': 'test_dest_path',
                     'remote_src': remote_src,
                     'regexp': regexp,
                     'delimiter': delimiter,
                     'ignore_hidden': ignore_hidden,
                     'decrypt': decrypt,
                     'follow': follow
                     }
                 }

    fake_action_module._task = fake_task

    # Test case: 1

# Generated at 2022-06-13 09:24:59.831037
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test
    '''

    # 1. Prepare
    # 1.1 Mock attributes tmp, task_vars
    tmp = None
    task_vars = {}

    # 1.2 Create instance ActionModule
    class MockActionModule(ActionModule):
        '''
        Class MockActionModule
        '''
        def __init__(self, tmp, task_vars):
            '''
            Attributes:
              * tmp
              * task_vars
            '''
            self.tmp = tmp
            self.task_vars = task_vars 

    am = MockActionModule(tmp, task_vars)

    # 1.3 Mock methods _execute_module, _execute_remote_stat, _get_diff_data, _remove_tmp_path, _find_needle, _assemble_from_

# Generated at 2022-06-13 09:25:02.115899
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('test', 'test', {'src': 'src', 'dest': 'dest'}, 'ansible.legacy.assemble')
    assert action_module

# Generated at 2022-06-13 09:25:08.992834
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with open('./tests/fixtures/action_module_assemble_path_fixture.txt') as f:
        path = f.read()

    task_vars = dict()
    args = dict()
    result = dict()

    # instantiate ActionModule
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # call method run with valid arguments
    result = action_module_obj.run(tmp=None, task_vars=task_vars)

    assert result == path

# Generated at 2022-06-13 09:25:13.001156
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.copy import ActionModule

    action_module = ActionModule(task=dict(args=dict()), connection=dict(module_implementation_preferences=[]), play_context=dict())
    assert action_module

# Generated at 2022-06-13 09:25:22.711888
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os.path
    import shutil
    import tempfile
    import unittest

    # Mock class to replace the ActionBase
    class MockActionBase(ActionBase):
        def __init__(self, task_vars=None):
            super(MockActionBase, self).__init__()
            if task_vars is None:
                task_vars = {}
            self._task_vars = task_vars


# Generated at 2022-06-13 09:25:35.300578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Uncomment for debug
    # import logging
    # logging.basicConfig(level=logging.DEBUG)

    # Prepare fake objects
    class FakeModule():
        class FakeArgs():
            def __init__(self, a, b, c, d, e, f, g, h, i):
                self.src = a
                self.dest = b
                self.delimiter = c
                self.remote_src = d
                self.regexp = e
                self.follow = f
                self.ignore_hidden = g
                self.decrypt = h

        class FakeAnsibleModule():
            def __init__(self, name, args, conn):
                self.params = args

        def __init__(self, args, conn):
            self.params = self.FakeArgs(args)


# Generated at 2022-06-13 09:25:38.333704
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = AnsibleActionModule(None, None, None, None)
    assert action is not None

# Generated at 2022-06-13 09:26:03.985077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Write more tests for ActionModule.run()
    # The following tests the happy path:
    # * src and dest are defined
    # * remote_src is not defined or False
    # * no regexp is used
    # * no delimiter is used
    # * ignore_hidden is not defined or False
    # * decrypt is not defined or True
    module = ActionModule()
    vars = {'dest': tempfile.mkstemp()[1]}
    vars['src'] = tempfile.mkdtemp()
    fragmentFileA = tempfile.NamedTemporaryFile('w')
    fragmentFileA.write("line 1\nline 2\nline 3\n")
    fragmentFileA.flush()
    fragmentFileB = tempfile.NamedTemporaryFile('w')

# Generated at 2022-06-13 09:26:05.889690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 09:26:14.961847
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins
    # creating a fake class for the purpose of test
    class FakePluginFactory:
        pass
    # creating a fake class for the purpose of test
    class FakeVarsModule:
        pass
    # creating a fake class for the purpose of test
    class FakeModuleUtils:
        pass
    # creating a fake class for the purpose of test
    class FakeAnsibleModule:
        pass
    # creating a fake class for the purpose of test
    class FakeTask:
        pass
    # creating a fake class for the purpose of test
    class FakeDatastore:
        pass
    # creating a fake class for the purpose of test
    class FakeActionBase:
        pass
    # creating a fake class for the purpose of

# Generated at 2022-06-13 09:26:16.416221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Execute constructor
    print(ActionModule())

# Generated at 2022-06-13 09:26:22.341853
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    src_path = '/source'
    dest_path = '/tmp/destination'
    delimiter = '****'
    regexp = '*.txt'
    ignore_hidden = False
    decrypt = True
    result = {}
    ansible_module = ActionModule()
    ansible_module.run(task_vars, result, src_path, dest_path, delimiter, regexp, ignore_hidden, decrypt)

# Generated at 2022-06-13 09:26:24.261081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None, None), ActionModule)
test_ActionModule.actionmodule_test = True

# Generated at 2022-06-13 09:26:26.951936
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print ('test_ActionModule_run')
    module = ActionModule()
    tmp = None
    task_vars = None
    args = {'ignore_hidden':'yes'}
    module.run(tmp,task_vars,args)

# Generated at 2022-06-13 09:26:37.222972
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import mock
    from ansible.plugins.action import ActionModule

    action = ActionModule(mock.Mock(), task=mock.Mock(), connection=mock.Mock(), play_context=mock.Mock())
    action._loader._get_basedir = mock.Mock(return_value='/some/path')
    action._remove_tmp_path = mock.Mock()
    action._execute_module = mock.Mock(return_value={'rc': 0, 'changed': False})
    action._execute_remote_stat = mock.Mock(return_value={'checksum': 'abc', 'isdir': False, 'exists': True})
    action._remote_expand_user = mock.Mock(return_value='/some/path')
    action._transfer_file = mock

# Generated at 2022-06-13 09:26:39.305710
# Unit test for constructor of class ActionModule
def test_ActionModule():
    utils_module = AnsibleActionModule()
    print(utils_module)

# Generated at 2022-06-13 09:26:40.383227
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule

# Generated at 2022-06-13 09:27:22.155610
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)
    assert action_module is not None

# Generated at 2022-06-13 09:27:36.568222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test normal case when no exception is raised
    m_action_module = ActionModule(
        task=dict(action=dict(module_name='assemble', module_args=dict())),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    m_action_module._execute_module = \
        lambda module_name, module_args, task_vars: dict(changed=True)
    m_action_module._execute_remote_stat = lambda x, y, z: dict(checksum='abcd')
    m_action_module._remote_expand_user = lambda x: x

    result = m_action_module.run(tmp=None, task_vars=dict())

# Generated at 2022-06-13 09:27:38.218175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 09:27:41.461206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Test for positive scenario.
    actionModule = ActionModule(task='', connection='', play_context='', loader='', templar='', shared_loader_obj='')
    assert actionModule


# Generated at 2022-06-13 09:27:42.744212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 09:27:58.223152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # 723c03e7e48b30c0f7a1361df8b9d6b5eac0c7c1
    # test case source: https://github.com/ansible/ansible/blob/723c03e7e48b30c0f7a1361df8b9d6b5eac0c7c1/test/units/plugins/action/test_assemble.py#L7
    from ansible.context import *

    # ansible.context.CLIARGS._ansible_positional_args = ['test_module', 'arg1', 'arg2']
    # ansible.context.CLIARGS._ansible_no_log = False
    # ansible.context.CLIARGS._ansible_debug = False
    # ansible.context.CLI

# Generated at 2022-06-13 09:27:58.923188
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:27:59.483389
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:28:04.874804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, {}, None, None)
    assert not hasattr(action_module, '_task')
    assert not hasattr(action_module, '_supports_check_mode')
    assert not hasattr(action_module, '_supports_async')
    assert not hasattr(action_module, '_supports_subset_metadata')
    assert not hasattr(action_module, '_connection')
    assert not hasattr(action_module, '_play_context')


# Generated at 2022-06-13 09:28:05.612214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:29:29.707799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert hasattr(action_module, 'run')

# Generated at 2022-06-13 09:29:39.318765
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None,
    )

    user = 'root'
    context = PlayContext()
    action = ActionModule(task=Task(), connection='local', play_context=context, loader=None, templar=None, shared_loader_obj=None)
    action.task_queue_manager = tqm
    action._supports_async = True
    action._supports_check_mode = False
    action._supports_async = True
    assert isinstance(action.run(user=user), dict)

# Generated at 2022-06-13 09:29:43.587863
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # construct a mock runner and task so we can invoke constructor
    runner = mock.MagicMock()
    task = mock.MagicMock()
    task.action = 'assemble'
    task.args = dict()
    # No error during construction
    obj = ActionModule(runner, task)

    assert obj._connection._shell.tmpdir == '/tmp'

# Generated at 2022-06-13 09:29:50.470351
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hosts = [dict(ansible_connection='local')]
    test_module = 'assemble'
    test_action = ActionModule(dict(src='/test/src', dest='/test/dest', regexp='test_pattern', remote_src=False),
                               [dict(action=dict(module=test_module, args=dict(src='/test/src', dest='/test/dest', regexp='test_pattern', remote_src=False)))],
                               [dict(connection='local')])
    test_action._shared_loader_obj = object()
    test_action._task = object()
    test_action._play_context = object()
    test_action._connection = object()
    test_action._task_vars = dict()
    test_action._loader = object()
    test_action._templar

# Generated at 2022-06-13 09:29:59.720243
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create mock task object.
    task = {
        'args': {
            'dest': '/tmp/ansible_test_dest'
        },
        'action': {
            '__ansible_module__': 'ansible.legacy.copy'
        }
    }

    c = module_common.CliModuleCommon(task, action=ActionModule())

    c.tmpdir = '/tmp/ansible_test_tmp'
    c.add_cleanup_file(c.tmpdir)
    os.mkdir(c.tmpdir, 0o755)

    # create mock source dir and files.
    src_path = '/tmp/src_01234'
    os.mkdir(src_path, 0o755)
    os.mkdir('{0}/tmp1'.format(src_path), 0o755)

# Generated at 2022-06-13 09:30:05.256015
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = dict(src="src_path", dest="dest_path", regexp="regexp", delimiter="@@", remote_src="False", ignore_hidden="True", follow="True")
    task = dict(action=dict(module="copy", args=args))
    a = ActionModule(task, connection=None, play_context={}, loader=None, templar=None, shared_loader_obj=None)
    assert a.run() == "ActionModule"

# Generated at 2022-06-13 09:30:13.662524
# Unit test for constructor of class ActionModule
def test_ActionModule():

    task_args = dict(
        src='~/my-tmp-dir',
        dest='~/my-tmp-dir',
        delimiter='\n',
        remote_src='yes',
        regexp=None,
        follow=False,
        ignore_hidden=False,
        decrypt=True
    )

    action_module = ActionModule(task=object, connection='localhost', play_context=object, loader=object, templar=object, shared_loader_obj=None)
    action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 09:30:16.537225
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(DummyModuleManager(), '/foo/bar/mymodule.py', 'mymodule', {}, {})
    assert obj != None


# Generated at 2022-06-13 09:30:18.325187
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(ActionModule)
    assert(ActionModule.TRANSFERS_FILES is True)


# Generated at 2022-06-13 09:30:21.850555
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = None
    src = None
    dest = None
    delimiter = None
    remote_src = None
    regexp = None
    follow = None
    ignore_hidden = None
    decrypt = None
    result = ActionModule.run(tmp, task_vars)
    assert result is not None

# Generated at 2022-06-13 09:33:38.218810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test that run calls the assemble_from_fragments method
    # with all the correct parameters, when using local files
    def my_ass_func(src_path, dest, delimiter=None, compiled_regexp=None, ignore_hidden=False, decrypt=True):
        assert src_path == '/fake/path/src'
        assert dest == '/fake/path/dest'
        assert delimiter == ':-'
        assert compiled_regexp.pattern == 'regexp'
        assert ignore_hidden is False
        assert decrypt is False

        return True

    # Fake object that replaces assemble_from_fragments method
    class MyActionModule(object):
        assemble_from_fragments = my_ass_func

    # ActionModule object to be tested
    am = ActionModule()

    # Set fake ActionModule to the