

# Generated at 2022-06-13 09:23:53.529827
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Testing constructor
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)._task.action == 'assemble'
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)._task.args == {}

# Generated at 2022-06-13 09:24:04.496930
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.unsafe_proxy import UnsafeProxy


# Generated at 2022-06-13 09:24:10.743395
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Load module
    m = ActionModule()

    # Load module args
    module_args = {
        'src': 'src/path/',
        'dest': 'dest/path/',
        'delimiter': '~~',
        'ignore_hidden': 'yes',
        'remote_src': 'no'
    }

    # Load options
    options = {}

    # Load task
    t = task.Task()

    # Load connection
    c = connection.Connection(module_args)

    # Load play context
    p = play_context.PlayContext()
    p.remote_addr = 'localhost'
    p.network_os = 'linux'
    p.become = False
    p.become_method = 'sudo'
    p.become_user = 'root'

# Generated at 2022-06-13 09:24:13.034107
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  assert isinstance(am, ActionModule)


# Generated at 2022-06-13 09:24:22.493962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import pytest

    from ansible.context import AnsibleContext

    from ansible.module_utils.parsing.convert_bool import boolean

    from ansible.plugins.action.assemble import ActionModule
    from ansible.plugins.action.assemble import _assemble_from_fragments
    from ansible.plugins.action.assemble import test_ActionModule as x
    from ansible.utils.plugin_docs import get_docstring

    # test calling ActionModule constructor directly
    action_module = ActionModule(None, AnsibleContext())
    assert action_module is not None

    # test calling _assemble_from_fragments directly
    src = os.path.join(os.path.dirname(__file__), 'test-data', 'assemble')
    temp_path = x._assemble

# Generated at 2022-06-13 09:24:23.227154
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:24:25.760386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(1)
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------

# Generated at 2022-06-13 09:24:34.223993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_task = dict( action=dict( module='assemble', remote_src=False, src='a', dest='b', delimiter='c', regexp='d', ignore='e', decrpt='f' ))
    am = ActionModule(my_task, DummyPlayContext())
    assert am.remote_src == False
    assert am.src == 'a'
    assert am.dest == 'b'
    assert am.delimiter == 'c'
    assert am.regexp == 'd'
    assert am.ignore_hidden == 'e'
    assert am.decrypt == 'f'


# Generated at 2022-06-13 09:24:44.725905
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_code = {
        "name": "TestAssemble",
        "args": {
            "src": "fake_src",
            "dest": "fake_dest",
            "delimiter": "fake_delimiter",
            "regexp": "fake_regexp",
            "follow": False,
        },
    }
    action_task = ActionModule(action_code)
    assert action_task._task.args['src'] == 'fake_src'
    assert action_task._task.args['dest'] == 'fake_dest'
    assert action_task._task.args['delimiter'] == 'fake_delimiter'
    assert action_task._task.args['regexp'] == 'fake_regexp'
    assert action_task._task.args['follow'] == False

# Generated at 2022-06-13 09:24:49.493942
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.connection import Connection, ConnectionError
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.copy import ActionModule as Copy
    from ansible.module_utils import basic
    from ansible.parsing.vault import VaultLib

    # module_args=dict(src='ssl/private/server.crt', dest='/tmp/newcert.pem')
    # src = 'ssl/private/server.crt'
    # dest = '/tmp/newcert.pem'
    # try:
    #     src = self._find_needle('files', src)
    # except AnsibleError as e:
    #     raise AnsibleActionFail(to_native(e))


    # if not os.path.isdir(src):
    #     raise Ansible

# Generated at 2022-06-13 09:25:03.123698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule('test')
    m.run()
    m.run({'tmp': 'tmp'}, {'task_vars': 'task_vars'})

# Generated at 2022-06-13 09:25:08.745114
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    myremote_tmp = "/tmp/ansible/tmp"
    task_vars = {}
    a = ActionModule(Task(), PlayContext())
    a.setup(myremote_tmp,"task")
    a._task.args["src"] = "/root/Desktop/ansible_test"
    a._task.args["dest"] = "/root/Desktop/myansible"

    a.run(task_vars)

# Generated at 2022-06-13 09:25:14.876141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test of ActionModule class
    '''
    # The class is abstract and can not be directly used.
    # This test executes the constructor only.
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am

# Generated at 2022-06-13 09:25:16.508387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:25:17.481016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:25:20.039160
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, None)
    assert action is not None


# Generated at 2022-06-13 09:25:22.170719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None, None)

# Generated at 2022-06-13 09:25:26.053668
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am=ActionModule(None, None)
    if isinstance(am, ActionModule):
        print("test_ActionModule")
    else:
        print("test_ActionModule not an instance of ActionModule")

# Generated at 2022-06-13 09:25:26.829934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    con = ActionModule()

# Generated at 2022-06-13 09:25:27.905308
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:25:51.554495
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor test
    '''
    t = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert t is not None

# Generated at 2022-06-13 09:25:53.716653
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # initialize AnsibleModule and ActionModule
    action_module = ActionModule(None, None, None, {}, None)
    assert action_module



# Generated at 2022-06-13 09:25:54.259563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:26:00.416989
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Set up test parameters
    name = 'test_ActionModule'
    task_vars = dict()
    task_vars['test_var'] = 42
    task_vars['another_var'] = 43
    inject = dict()
    inject['var_a'] = 44
    inject['var_b'] = 45
    tmp = None
    tmp_path = None
    src = None
    dest = None
    delimiter = None
    remote_src = 'yes'
    regexp = None
    follow = 'yes'
    ignore_hidden = 'yes'
    decrypt = 'yes'

    # Create task
    task = dict()
    task['name'] = name
    task['args'] = dict()
    task['args']['src'] = src
    task['args']['dest'] = dest

# Generated at 2022-06-13 09:26:04.317074
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    PlayContext()
    ActionModule()
    FakeTask()
    TaskQueueManager()


# Generated at 2022-06-13 09:26:07.258068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module != None

# Generated at 2022-06-13 09:26:11.991011
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from test.unit.loader import DictDataLoader
    from test.unit.mock.builtins import Mock

    actM = ActionModule(
        task=Mock(),
        connection=Mock(),
        play_context=Mock(),
        loader=DictDataLoader({}),
        templar=Mock(),
        shared_loader_obj=None
    )

    actM.run()

# Generated at 2022-06-13 09:26:13.300316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__doc__ != None



# Generated at 2022-06-13 09:26:16.471306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(dict(tmp='/tmp/file')), ActionModule)

# Generated at 2022-06-13 09:26:17.946048
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:27:00.294253
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 09:27:10.233540
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_execute import TaskExecutor

    play_ctxt = PlayContext()
    task = Task()
    loader = 'loader'
    tqm = 'tqm'
    shared_loader_obj = 'shared_loader_obj'
    variable_manager = 'variable_manager'
    loader, tmp_path, md = read_docstring(ActionModule._execute_module, verbose=True)
    tmp_path = '/tmp/ansible_tmp'
    task_vars = {}
    task_

# Generated at 2022-06-13 09:27:17.903463
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def _run_module(module_name=None, module_args=None, task_vars=None):
        raise Exception
    class _connection(object):
        class _shell(object):
            tmpdir = '/tmp/test'
        _shell = _shell()
        _shell.tmpdir = '/tmp/test'
        def _transfer_file(self, path, remote_path):
            return remote_path

    task_vars = {
        'ansible_check_mode': False,
        'ansible_host': 'localhost',
        'ansible_port': 22,
        'ansible_connection': 'local',
        'ansible_shell_type': 'csh',
        'ansible_shell_executable': '/bin/csh'
    }


# Generated at 2022-06-13 09:27:20.056855
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    target_run = ActionModule()


# Generated at 2022-06-13 09:27:20.983996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:27:23.617067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:27:37.828018
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(dict(), None)
    assert am.TRANSFERS_FILES
    assert not hasattr(am, '_supports_check_mode')
    assert am._task.args.get('src') is None
    assert am._task.args.get('dest') is None
    assert am._task.args.get('delimiter') is None
    assert am._task.args.get('remote_src') == 'yes'
    assert am._task.args.get('regexp') is None
    assert not am._task.args.get('follow')
    assert not am._task.args.get('ignore_hidden')
    assert am._task.args.get('decrypt')
    assert am._task.args.get('local') is None
    assert am._task.action == 'assemble'

# Unit

# Generated at 2022-06-13 09:27:42.650928
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am
    # test _assemble_from_fragments
    src_path = os.path.abspath("test_data")
    dest_path = am._assemble_from_fragments(src_path)
    assert os.path.exists(dest_path)
    os.remove(dest_path)

# Generated at 2022-06-13 09:27:44.168795
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass


# Generated at 2022-06-13 09:27:59.236710
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.assemble as module_assemble
    import ansible.plugins.action.copy as module_copy
    import ansible.plugins.action.file as module_file
    import ansible.plugins.action.setup as module_setup
    import os
    import shutil
    import tempfile
    import unittest

    class TestActionModule(unittest.TestCase):

        TEST_PATH = u"test_path"
        TEST_PATH_EXPANDED = u"test_path_expanded"

        ##############################################################################
        # _assemble_from_fragments() and associated helper methods
        ##############################################################################

        def _create_test_fragment_dir(self):
            self.test_fragment_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 09:29:22.147758
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None, "Cannot find ActionModule class"

# Generated at 2022-06-13 09:29:24.935127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Test of ActionModule')

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:29:38.234349
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six import binary_type
    from ansible.plugins.action.assemble import ActionModule
    from ansible.utils.hashing import checksum_s
    from ansible.module_utils import basic
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.vars.hostvars import HostVars

    class FakeAction(object):
        def __init__(self):
            self.args = {'src': '', 'dest': 'dest_path', 'regexp': '', 'delimiter': '',
                         'remote_src': 'no', 'ignore_hidden': True}

    class FakeTask(object):
        def __init__(self):
            self.action = FakeAction()


# Generated at 2022-06-13 09:29:47.676686
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    print("\n\n#")
    print("# Starting test_ActionModule_run()")
    print("#\n\n")

    from ansible.plugins.action.assemble import ActionModule
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    ##################################################################################################################
    # init inventory object

    hostvars = {
        'www.example.org': {
            'ansible_user': 'example_user',
            'ansible_password': 'example_pass'
        }}

    inventory = InventoryManager(loader=None, sources='')
    for h in hostvars.keys():
        inventory.add_host(host=h, port=22)

# Generated at 2022-06-13 09:29:56.708407
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(
        ansible_connection='local'
    )
    loader = DictDataLoader({
        'assemble/file1': 'line1\nline2',
        'assemble/file2': 'line3\nline4',
    })
    tmp = tempfile.mkdtemp()
    host_vars = dict(ansible_connection='local')
    connection = Connection(host_vars)
    action = ActionModule(loader=loader, task=Task(), connection=connection)
    result = action.run(tmp=tmp, task_vars=task_vars)
    assert result.get('changed',False)
    assert result.get('checksum',False)

# Generated at 2022-06-13 09:30:02.000956
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Tests for constructor of class ActionModule
    a = ActionModule(None, None)
    assert a._connection
    assert a._loader
    assert a._templar
    assert a._shared_loader_obj
    assert a._connection_info
    assert a._task
    assert a._play_context
    assert a._loader_name
    assert a._task_vars
    assert a._available_variables
    assert a._tempdir
    assert a._keep_remote_files
    assert a._diff

# Generated at 2022-06-13 09:30:05.755827
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(dict(src=tempfile.mkdtemp(), dest=tempfile.mkdtemp(), regexp=r'\d+'), None, None)
    out = a.run(tmp=None, task_vars=None)
    assert out['failed'] == True
    assert out['msg'] == u'Source ({}) is not a directory'.format(a._task.args['src'])

# Generated at 2022-06-13 09:30:17.404077
# Unit test for constructor of class ActionModule
def test_ActionModule():

    def test_ActionModule_task(self):

        task = dict(
                src="source",
                dest="destination",
                delimiter="_",
                remote_src="false",
                regexp="^",
                follow="true",
                ignore_hidden="true",
                decrypt="false"
                )
        task_vars = dict(
                source="source",
                destination="destination"
                )

        action_module = ActionModule(task, task_vars)

        assert action_module
        assert action_module.task == task
        assert action_module.task_vars == task_vars
        assert action_module._supports_check_mode == False

        return None



# Generated at 2022-06-13 09:30:18.268358
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:30:30.082492
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    import shutil

    tmp_path = tempfile.mkdtemp()
