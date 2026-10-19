

# Generated at 2022-06-13 11:07:55.098256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import tempfile
    # sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'lib', 'ansible'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'lib'))

    class FakeConnection(object):
        def __init__(self, config):
            self.config = config

    # mock
    class MockModule(object):
        def __init__(self):
            pass

       

# Generated at 2022-06-13 11:08:01.421010
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, {}, {}, None)
    action_module._connection = {}
    action_module._task = {'args': {'delay': 0, 'sleep': 1, 'timeout': 600, 'connect_timeout': 5}}
    action_module._task.args = {}
    action_module._remove_tmp_path = lambda: None
    assert action_module.run({}, {}) == dict(failed=False, elapsed=0, skipped=False)

# Generated at 2022-06-13 11:08:09.715356
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.wait_for_connection import ActionModule
    from ansible.module_utils._text import to_bytes
    import datetime

    am = ActionModule(task=dict(args=dict(sleep=1, timeout=2)), connection=object(), play_context=object(), loader=object(), templar=object(), shared_loader_obj=object())

    assert am.run() == {'_ansible_verbose_always': True, '_ansible_verbose_override': True, 'failed': True, 'msg': u'timed out waiting for ping module test: timed out waiting for connection port up'}

# Generated at 2022-06-13 11:08:13.261502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.config import NetworkConfig
    from ansible.module_utils.network.common.utils import load_provider
    facts = dict(subclass_name='TestConnectionClass')
    connection = Connection(NetworkConfig(load_provider(facts, {}), indent=3), None)
    am = ActionModule(connection, {'a': 1})
    am._execute_module = lambda *s: dict(ansible_facts=dict(subclass_name='TestConnectionClass'))
    am._connection._shell._curdir = "/home/user/"
    result = am.run(None, None)
    assert 'failed' not in result
    assert result['elapsed'] == 0

# Generated at 2022-06-13 11:08:19.069910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = {}
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    try:
        am.do_until_success_or_timeout(lambda: 1, 2, 3, 4, 5)
        error = None
    except TimedOutException as e:
        error = "timed out waiting for ping module test: " + str(e)
    print(error)
    assert error == None

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 11:08:26.264888
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Stub class for self with some of the attributes mocked
    class ActionModuleMockSelf(object):
        def __init__(self):
            self._task = {}
            self._task['args'] = {}
            self._task['args']['timeout'] = 0
            self._task['args']['connect_timeout'] = 0
            self._task['args']['delay'] = 0
            self._task['args']['sleep'] = 0
            self._play_context = {}
            self._play_context.check_mode = False
            self._connection = {}
            self._connection._shell = {}
            self._connection._shell.tmpdir = None
            self._discovered_interpreter_key = None
            self._remove_tmp_path = None

        def run(self, a, b):
            pass


# Generated at 2022-06-13 11:08:27.683556
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None


# Generated at 2022-06-13 11:08:35.311062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ac = ActionModule(
        task=dict(action=dict(module_name='testmodule', module_args=dict(state='present'))),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert ac.TRANSFERS_FILES == False
    assert len(ac._VALID_ARGS) == 4
    assert ac.DEFAULT_CONNECT_TIMEOUT == 5
    assert ac.DEFAULT_DELAY == 0
    assert ac.DEFAULT_SLEEP == 1
    assert ac.DEFAULT_TIMEOUT == 600

# Generated at 2022-06-13 11:08:36.661269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_ActionModule_obj = ActionModule(None, None)
    test_ActionModule_obj.run(None, None)

# Generated at 2022-06-13 11:08:42.245327
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import mock
    import collections

    # Mock object
    test_obj = mock.Mock()

    # Test constructor
    action_obj = ActionModule(task=test_obj, connection=test_obj, play_context=test_obj, loader=test_obj, templar=test_obj, shared_loader_obj=test_obj)

    assert action_obj._task is test_obj
    assert action_obj._connection is test_obj
    assert action_obj._play_context is test_obj
    assert action_obj._loader is test_obj
    assert action_obj._templar is test_obj
    assert action_obj._shared_loader_obj is test_obj
