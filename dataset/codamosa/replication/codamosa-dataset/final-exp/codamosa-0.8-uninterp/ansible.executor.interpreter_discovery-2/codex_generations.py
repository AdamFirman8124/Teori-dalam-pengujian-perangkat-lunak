

# Generated at 2022-06-12 21:30:19.188652
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic

    class action:
        _discovery_warnings = []
        class connection:
            _shell = None
            def __init__(self):
                self._shell = basic.AnsibleModule(
                    argument_spec=dict(),
                    # support check mode
                    bypass_checks=False,
                    no_log=False,
                    check_invalid_arguments=False,
                    mutually_exclusive=list(),
                    required_together=list(),
                    required_one_of=list(),
                    add_file_common_args=False,
                    supports_check_mode=True,
                )

            def has_pipelining(self):
                return True


# Generated at 2022-06-12 21:30:27.939898
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from unittest import TestCase, mock
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.json import json

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_bytes

    try:
        from __main__ import display
    except ImportError:
        display = None

    class TestDiscovery(TestCase):

        def _create_mock_module(self, interpreter_name, discovery_mode):
            def _module(**kwargs):
                mod = mock.Mock(spec=AnsibleModule)
                mod.params = kwargs
                mod.check_mode = False
                mod.no_log = False
                return mod

            mod = _

# Generated at 2022-06-12 21:30:31.169674
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert(discover_interpreter(
        'test_action',
        'python',
        'auto_legacy_silent',
        {'inventory_hostname': 'localhost'},
    ) == '/usr/bin/python')

# Generated at 2022-06-12 21:30:38.655361
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:30:48.422507
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: change this to a proper unit test
    class MockAction:
        def __init__(self):
            self._discovery_warnings = []
            self._connection = MockConnection()

        def _low_level_execute_command(self, *args, **kwargs):
            return self._connection._low_level_execute_command(*args, **kwargs)

    class MockConnection:
        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:30:59.302909
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule
    action = ActionModule(None, dict(ANSIBLE_MODULE_ARGS={'ANSIBLE_MODULE_ARGS': dict(interpreter_discovery_mode='auto')},
                                     ansible_inventory=dict(localhost=dict(vars=dict(ansible_python_interpreter='/usr/bin/python')))))
    assert discover_interpreter(action, 'python', 'auto', dict(inventory_hostname='localhost',
                                                               ansible_python_interpreter='/usr/bin/python')) == u'/usr/bin/python'

# Generated at 2022-06-12 21:31:05.163682
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {
        'inventory_hostname': 'localhost',
        'ansible_connection': 'local',
        'ansible_python_interpreter': 'python'
    }
    res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert res in [u'python', u'/usr/bin/python']

# Generated at 2022-06-12 21:31:14.567017
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.module_common import _load_params

    display.verbosity = 4
    test_module = '/tmp/test_module'
    test_interpreter_dict = {
        'python2.7': '/usr/bin/python2.7',
        'python3.6': '/usr/bin/python3.6',
        'python3.7': '/usr/bin/python3.7',
        'python3.8': '/usr/bin/python3.8',
    }
    test_params = {
        'ANSIBLE_MODULE_ARGS': _load_params(test_module)
    }

    # Test python interpreter discovery

# Generated at 2022-06-12 21:31:25.232015
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    display.verbosity = 3
    display.deprecated_warning = lambda msg: None

    # test exact match
    lin_ver = u'Ubuntu 18.04'
    res = discover_interpreter(None, 'python', 'auto', dict(distribution=lin_ver))
    assert res == u'/usr/bin/python3'

    # test slot match
    lin_ver = u'Ubuntu 18.05'
    res = discover_interpreter(None, 'python', 'auto', dict(distribution=lin_ver))
    assert res == u'/usr/bin/python3'

    # test distro not in distro map
    lin_ver = u'Debian 18.05'

# Generated at 2022-06-12 21:31:38.129687
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import re
    import json
    import platform
    import unittest

    class TestDiscoveryInterpreter(unittest.TestCase):

        def test_discover_interpreter(self):

            import string
            import random
            import os

            LinuxDistro = platform.linux_distribution()

            DISCOVERY_INTERPRETER_NAME = 'python2'  # this function only support python2

            DISCOVERY_INTERPRETER_DISCOVERY_MODE = 'auto'


# Generated at 2022-06-12 21:31:59.444469
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionFake:
        pass
    action = ActionFake()
    action._discovery_warnings = []
    action._low_level_execute_command = lambda x, sudoable=False, in_data=None: {'stdout': x} if in_data else {'stdout': 'PLATFORM\ndarwin\nFOUND\n/usr/bin/python\nENDFOUND', 'stderr': ''}
    action._connection = ActionFake()
    action._connection.has_pipelining = True
    task_vars = {}

    print(discover_interpreter(action, 'python', 'auto', task_vars))
    print(discover_interpreter(action, 'python', 'auto_silent', task_vars))
    print(action._discovery_warnings)


# Generated at 2022-06-12 21:32:08.823178
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    interpreter_name = 'python'
    discovery_mode = ['auto', 'auto_legacy', 'auto_silent', 'auto_legacy_silent'][1]
    task_vars = dict()
    action = module.action
    action._connection = module.connection
    try:
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
        print(result)
    except Exception as ex:
        print(ex)

# Generated at 2022-06-12 21:32:20.466315
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic

    # Test Case 1:
    # Test Case for unsupported interpreter
    ums = UMS()
    umask = basic.AnsibleModule
    # task_vars = {'inventory_hostname': 'localhost',
    #             'INTERPRETER_PYTHON_DISTRO_MAP': {'fedora': {'17': u'/usr/bin/python', '18': '/usr/bin/python'},
    #                                               'ubuntu': {'trusty': u'/usr/bin/python', 'xenial': '/usr/bin/python'}},
    #             'INTERPRETER_PYTHON_FALLBACK': [u'/usr/bin/python']}

    test_interpreter = 'python'
    test_discovery_mode = 'auto'
   

# Generated at 2022-06-12 21:32:28.879338
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:32:40.981768
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:32:50.359958
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.executor.executor import PlaybookExecutor
    import ansible.utils

    from ansible.plugins.loader import action_loader

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            self._discovery_warnings = []
            self._low_level_execute_command = ansible.utils.low_level_execute_command
            return discover_interpreter(self, 'python', 'auto', task_vars)

    class TestPlayContext(PlayContext):
        def __init__(self, **kwargs):
            self.connection = 'local'
            self.network_os = 'linux'

# Generated at 2022-06-12 21:33:01.823591
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.discovery import InterpreterDiscoveryRequiredError
    from ansible.module_utils.connection import Connection

    # FIXME: need to mock the action class to remove the 'with'
    class FakeAction():

        def __init__(self):
            self._discovery_warnings = []
            self._connection = Connection()

        def __enter__(self):
            return self

        def __exit__(self, type, value, traceback):
            return

        def _low_level_execute_command(self, cmd, sudoable, in_data=None):
            if in_data:
                return {'stdout': '{ "osrelease_content": "{0}", "platform_dist_result": [] }'.format(cmd[2:])}

# Generated at 2022-06-12 21:33:06.638284
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionModule
    from ansible.utils.sentinel import Sentinel
    from ansible.vars import combine_vars

    # hostvars and play vars for test_hosts
    host_vars = {
        'test_host': {
            'program_name': 'python',
            'hostvars': {},
            'some_variable': 'a'
        },
        'alt_host': {
            'program_name': 'python3',
            'hostvars': {},
            'some_variable': 'b'
        }
    }

    play_vars = {
        'program_name': 'python2.7',
        'some_variable': 'c'
    }

    # create a fake taskvars dict with the above

# Generated at 2022-06-12 21:33:11.681713
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    from collections import namedtuple

    # sys.modules['ansible'].module_utils.distro = None
    import ansible.module_utils.distro

    class ScriptModule:
        class _ActionModule(object):
            def __init__(self):
                self._connection = namedtuple("Connection", ['has_pipelining'])(True)
                self._display = Display()
                self._discovery_warnings = []
                self.DO_NOT_DISCOVER_IPYTHON = False

            def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
                self._display.vvvv('Executing {0}'.format(cmd))

# Generated at 2022-06-12 21:33:23.241952
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.common.collections import ImmutableDict
    assert discover_interpreter(None, 'python', 'auto', ImmutableDict(INTERPRETER_PYTHON_DISTRO_MAP={'rhel':{'6':'foo', '7':'bar', '8':'baz'}})) == 'foo'
    assert discover_interpreter(None, 'python', 'auto', ImmutableDict(INTERPRETER_PYTHON_DISTRO_MAP={'fedora':{'6':'foo', '7':'bar', '8':'baz'}})) == 'foo'

# Generated at 2022-06-12 21:33:45.152909
# Unit test for function discover_interpreter
def test_discover_interpreter():
    print(discover_interpreter(None, "python", "auto", None))

# Generated at 2022-06-12 21:33:55.971462
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import imp
    import shutil
    import tempfile
    import subprocess
    import simplejson
    import ansible.module_utils.basic
    import ansible.executor.discovery

    TMPDIR = tempfile.mkdtemp()

    # for testing, we're going to put a version-specific libpython here
    LD_LIBRARY_PATH = os.path.join(TMPDIR, 'lib')

    # and a version-specific python here
    EXECUTABLE = os.path.join(TMPDIR, 'bin', 'python')


# Generated at 2022-06-12 21:34:06.320224
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.action.script import ActionModule as ScriptActionModule
    from ansible.plugins.action.raw import ActionModule as RawActionModule
    import os
    import sys

    # Use default script module search path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'lib', 'ansible', 'modules'))

    filename = os.path.join(os.path.dirname(__file__), 'sample_task_python_info.json')
    with open(filename, 'r') as fh:
        python_info = json.load(fh)

    # RedHat 7

# Generated at 2022-06-12 21:34:15.827454
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionModule:
        def __init__(self):
            self._discovery_warnings = []
        def _discovery_failure(self, msg):
            raise Exception(msg)
        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            shell_bootstrap = ("echo PLATFORM; uname; echo FOUND; {0}; echo ENDFOUND".format(cmd))

            shell_bootstrap_result = dict(
                stdout=u'PLATFORM\n Linux\n FOUND\n /usr/bin/python2.7 \n /usr/bin/python3.5\n /usr/bin/python3.6\n ENDFOUND\n'
            )
            return shell_bootstrap_result


# Generated at 2022-06-12 21:34:24.483695
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.debug import enable_debugger
    from ansible.plugins.loader import action_loader

    enable_debugger = enable_debugger  # noqa

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
        run_additional_callbacks=False,
        run_tree=False,
    )

    # ensure the action plugin is loaded
    action = action_loader.get('script', tqm)

    # fake task_vars from a playbook run

# Generated at 2022-06-12 21:34:35.020941
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.vars.hostvars import HostVars

    class FakeAction(ActionBase):
        def _low_level_execute_command(self, cmd, buffer_output=True, executable=None,
                                       in_data=None, sudoable=True, su=False,
                                       shell=None, env=None):
            return {'stdout': cmd, 'stderr': '', 'rc': 0}

        def _execute_module(self, *args, **kwargs):
            pass

    a = FakeAction()
    h = HostVars()
    a.task_vars = {'inventory_hostname': 'test'}

# Generated at 2022-06-12 21:34:39.907586
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic

    assert discover_interpreter(basic.AnsibleModule(
        argument_spec=dict(interpreter_name='str', discovery_mode='str')),
                                 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:34:49.905416
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test Python discovery
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto', {}) == '/usr/bin/python'

    # Test that unsupported interpreters are not supported

# Generated at 2022-06-12 21:34:59.458617
# Unit test for function discover_interpreter
def test_discover_interpreter():
    first_bootstrap_py = '/usr/bin/python'
    last_bootstrap_py = '/usr/bin/python3'
    bootstrap_py_list = [first_bootstrap_py, last_bootstrap_py]

# Generated at 2022-06-12 21:35:05.448838
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest


    class TestInterpreterDiscovery(unittest.TestCase):
        def _make_action(self):
            class TestConnection(object):
                def __init__(self):
                    self.has_pipelining = True

                def reset(self):
                    self.has_pipelining = True

                def low_level_execute_command(self, cmd, sudoable=True, in_data=None, sudo_user=None, sudoable=None,
                                              executable='/bin/sh', in_data=None, sudoable=None, prompt=None,
                                              answer=None, new_stdin=None, prompt_retries=None):

                    res = {}


# Generated at 2022-06-12 21:35:52.207128
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.strategy.linear import StrategyModule

    class TestVars(object):

        def __init__(self):
            self.inventory_hostname = '127.0.0.1'

    class TestAction(object):

        def __init__(self):
            self._discovery_warnings = []
            self._low_level_execute_command = lambda s, sudoable=False, in_data=None: {}

        def set_connection(self, connection):
            self._connection = connection

    test_vars = TestVars()


# Generated at 2022-06-12 21:36:03.126654
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import collections
    import types

    import pytest
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils._text import to_bytes, to_text

    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable=None):
            if isinstance(cmd, (list, tuple)):
                cmd = ' '.join(cmd)

            if executable:
                raise NotImplementedError('executable param not supported here')

            display.vvvv('LL EXEC {0}'.format(cmd.encode('utf-8')))


# Generated at 2022-06-12 21:36:13.412961
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # first, good input
    # - test for exact match
    platform_info_good = {u'osrelease_content': u'NAME="Amazon Linux"\nVERSION="2"\nID="amzn"\nID_LIKE="centos rhel fedora"\nVERSION_ID="2"\nPRETTY_NAME="Amazon Linux 2"\nANSI_COLOR="0;33"\nCPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"\nHOME_URL="https://amazonlinux.com/"\n', u'platform_dist_result': [u'amzn', u'2', u'']}
    task_vars = dict(INTERPRETER_PYTHON_DISTRO_MAP={'amzn': {'2': '/usr/bin/python2'}})


# Generated at 2022-06-12 21:36:14.862508
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: implement unit tests with mock action and pytest
    return

# Generated at 2022-06-12 21:36:26.692279
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts import ansible_local

    # test against a mixture of supported and unsupported platforms
    res = ansible_local.get_facts(None, dict(
        gather_subset=['all'],
        gather_timeout=5,
        local_tmp='/tmp',
        interpreter_discovery_mode='auto_legacy',
        interpreter_discovery_warning_only=True,
    ))

    # if this fails, we're running the test on a new platform for the first time, and someone needs to update this test
    assert len(res['ansible_facts']['ansible_interpreter_python']) > 1, \
        "Test may need updating to support new OS version/distro"


# Generated at 2022-06-12 21:36:37.052217
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'

    display.verbosity = 2
    display.debug = True
    display._display.verbosity = 2
    display._display.debug = True
    res = discover_interpreter(None, 'python', 'auto', {})
    display.verbosity = 0
    display.debug = False
    display._display.verbosity = 0


# Generated at 2022-06-12 21:36:42.296391
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    class MyTask(Task):
        def __init__(self):
            self._local_action = True

    class MyTaskQueueManager(TaskQueueManager):
        def __init__(self):
            return None

    class FakeAction(object):

        def __init__(self):
            self.task_vars = dict(ansible_python_interpreter='/usr/bin/python')
            self.task = MyTask()
            self.tqm = MyTaskQueueManager()
            self.connection = Connection()
            self.runner_on_failed = ''
            self.runner_on_unreachable = ''
            self.get_var = ''

# Generated at 2022-06-12 21:36:48.279797
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    import ansible.utils.plugin_docs as adoc

    class FakeAction(ActionBase):
        TRANSFERS_FILES = False
        host = 'localhost'
        _display = Display()
        _discovery_warnings = []

        def _low_level_execute_command(self, *args, **kwargs):
            ret = dict(rc=0, stdout='', stderr='')

            if 'raw_stdout' in kwargs:
                ret['stdout'] = kwargs['raw_stdout']
            elif 'raw_stderr' in kwargs:
                ret['stderr'] = kwargs['raw_stderr']

# Generated at 2022-06-12 21:36:56.541885
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader

    class ActionModule(ActionBase):
        def run(self, tmp=None, task_vars=dict()):
            task_vars['inventory_hostname'] = 'foohost'
            interpreter = discover_interpreter(self, 'python', 'auto_legacy_silent', task_vars)
            return TaskResult(host=task_vars.get('inventory_hostname'),
                              interpreter=interpreter)

    action_loader.add_directory(C.DEFAULT_ACTION_PLUGIN_PATH)
    action_loader.add_directory(C.DEFAULT_ACTION_PLUGIN_PATH)

# Generated at 2022-06-12 21:37:06.616214
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """ Unit test for function discover_interpreter """
    from ansible.executor.task_executor import TaskExecutor

    # This function (and associated interpreter discovery methods) works with a TaskExecutor
    this_te = TaskExecutor({})

    # Test non-existent interpreter
    try:
        discover_interpreter(this_te, 'pypy', 'auto_legacy_silent', {})
        assert False, "interpreter discovery should not be supported for this interpreter"
    except ValueError as ex:
        assert 'not supported' in to_text(ex), "unexpected exception encountered during discovery attempt"

    # Test unsupported platform

# Generated at 2022-06-12 21:38:25.638609
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:38:34.340043
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    class DummyActionModule(ActionBase):

        def __init__(self, *args, **kwargs):
            self._discovery_warnings = []
            self._connection = DummyConnection()
            super(DummyActionModule, self).__init__(*args, **kwargs)

        def run(self, *args, **kwargs):
            display.warning(msg='Skipping test due to unsupported execution method')
            return TaskResult(changed=False)

    class DummyConnection(object):

        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:38:43.516417
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play

    class MockActionBase:

        def _get_task_vars(self):
            return {}

    class MockActionModule(MockActionBase):
        def __init__(self):
            self.args = {}


# Generated at 2022-06-12 21:38:54.942916
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # platform_type = 'linux'
    # platform_python_map = {'linux': {'redhat': 'python2', 'ubuntu': 'python3', distro: version}}
    # bootstrap_python_list = ['python', 'python2', 'python3']
    task_vars = {
        'ansible_python_interpreter': '/usr/bin/python',
        'INTERPRETER_PYTHON_DISTRO_MAP': {
            'redhat': {'7': 'python2', '8': 'python3'},
            'ubuntu': {'18.04': 'python3', '16.04': 'python2'}
        },
        'INTERPRETER_PYTHON_FALLBACK': ["python", "python2", "python3"]
    }
    action = None
    # 1

# Generated at 2022-06-12 21:39:05.091546
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class UtilDummyModule:
        def __init__(self, verbosity=None):
            self.verbosity = verbosity
            self.params = {}
            self.fail_json_called = False
            self.fail_json_result = []
            self._ansible_debug = False
            self._ansible_verbose_always = True

        def set_boolean(self, name, value):
            try:
                self.params[name] = bool(int(value))
            except ValueError:
                self.params[name] = False

        def fail_json(self, **kwargs):
            self.fail_json_called = True
            self.fail_json_result = kwargs

    class UtilDummyModuleArgs:
        def __init__(self):
            self.check_mode = False
           

# Generated at 2022-06-12 21:39:11.201692
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = MockActionModule()
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = {}
    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars) == u'/usr/bin/python'
    action.reset_results()
    discovery_mode = 'auto'
    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars) == u'/usr/bin/python'



# Generated at 2022-06-12 21:39:19.076423
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # create an action to test with
    from ansible.plugins.action.script import ActionModule as script_action
    action = script_action(None, None, None, None, None, None, None)

    # emulate a task vars structure
    task_vars = {
        'ansible_python_interpreter': '/fake/python',
        'ansible_python_major_version': 0,
    }

    # test basic discovery
    interpreter = discover_interpreter(action, 'python', 'auto', task_vars)
    assert interpreter == '/usr/bin/python'

    # test with an unsupported platform
    action._connection.has_pipelining = False
    interpreter = discover_interpreter(action, 'python', 'auto', task_vars)
    assert interpreter == '/usr/bin/python'

    #

# Generated at 2022-06-12 21:39:25.822326
# Unit test for function discover_interpreter
def test_discover_interpreter():
    module_utils_path = '/home/ansible/ansible/lib/ansible/module_utils'
    action = MockAction(module_utils_path)
    task_vars = {'ansible_python_interpreter': '/usr/bin/python'}
    interpreter_name = 'python'
    discovery_mode = 'auto'
    res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    print('Interpreter is: ', res)



# Generated at 2022-06-12 21:39:30.252603
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    action = TaskExecutor(None, None, None, None, None, None, None)
    task_vars = {}
    # test_paths = ('/usr/bin/python3.6', '/usr/bin/python3', '/usr/bin/python2.7', '/usr/bin/python', '/bin/python3.6', '/bin/python3', '/bin/python2.7', '/bin/python')
    # test_platform_type = 'linux'
    # test_distro = 'Debian'
    # test_version = '9'
    # test_interpreter = '/usr/bin/python3'

    discovery_mode = 'auto_legacy_silent'

    # display_vars(test_paths=test_path

# Generated at 2022-06-12 21:39:41.490622
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    task_vars = {}
    task_vars['inventory_hostname'] = 'localhost'

    # Test default discovery mode:
    try:
        result = discover_interpreter(action, None, 'auto', task_vars)
        assert result == '/usr/bin/python'
    except Exception as e:
        print(repr(e))
        assert False, 'Unhandled exception: {}'.format(repr(e))

    # Test default discovery mode but with explicit interpreter name ('python')
    try:
        result = discover_interpreter(action, 'python', 'auto', task_vars)
        assert result == '/usr/bin/python'
    except Exception as e:
        print(repr(e))
        assert False, 'Unhandled exception: {}'.format(repr(e))

